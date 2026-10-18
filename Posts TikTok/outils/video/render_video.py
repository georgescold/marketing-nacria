"""Assemble an episode into a 1080x1920 vertical video (no music: the user adds it by hand).

Usage: python render_video.py E01_point_noir [t1 t2 ...]   (times = preview stills only)
Reads ../../compte vidéo/<episode>/ (voice.mp3, timestamps.json, scenes/, optional music.mp3) and writes video.mp4 + legende.txt.
Grammar copied from @learning.of.theday: series menu card, one clay scene per spoken line with a soft cross-fade and a slow
push-in, small white subtitles, a big counting number when the line has a figure, cut 0.3 s after the last word, -14 LUFS.
"""
import json, math, pathlib, subprocess, sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

import comptes
from comptes import EPISODES

HERE = pathlib.Path(__file__).resolve().parent
ROOT = comptes.ACCOUNTS["acne"]["root"]  # default account; each episode renders into comptes.root(e) / <episode>
FONT = HERE.parent / "fonts" / "DMSans.ttf"
W, H, FPS = 1080, 1920, 30
# Measured on the original mixes of the model account (12 reels): -14.4 LUFS, and the music alone (in the voice pauses)
# sits 9.7 dB under the voice (median, 7.3 to 11.5), i.e. -22.7 LUFS. No ducking.
MUSIC_GAP, TARGET_LUFS = 9.7, -14.4
BG_CENTRE, BG_EDGE = (13, 38, 52), (2, 3, 8)  # teal series background (model account: #0b212d fading to #020308)
FADE, TAIL = 0.35, 0.3
MONTAGE_STEP = 1.3  # seconds per image in a montage, never less


def font(size, weight=500, path=None):
    f = ImageFont.truetype(str(path or FONT), size)
    try:
        axes = f.get_variation_axes()
        f.set_variation_by_axes([weight if a["name"] in (b"Weight", "Weight") else a.get("default", a["minimum"]) for a in axes])
    except Exception:
        pass
    return f


class Timing:
    """ElevenLabs character timestamps (fal returns them in chunks with cumulative times)."""

    def __init__(self, ts):
        ts = ts if isinstance(ts, list) else [ts]
        self.chars = [c for t in ts for c in t["characters"]]
        self.starts = [x for t in ts for x in t["character_start_times_seconds"]]
        self.ends = [x for t in ts for x in t["character_end_times_seconds"]]
        self.full = "".join(self.chars)

    def find(self, text, pos=0):
        i = self.full.find(text, pos)
        assert i >= 0, f"not in the voice timestamps: {text!r}"
        return i

    def at(self, text, pos=0):
        return self.starts[self.find(text, pos)]


def line_times(lines, tm):
    """Start time and first character index of each spoken line."""
    out, pos = [], 0
    for text, *_ in lines:
        i = tm.find(text[:12], pos)
        out.append((tm.starts[i], i))
        pos = i + len(text)
    return out


def split_phrase(words, maxlen):
    """Cut a phrase into balanced pieces of at most maxlen characters, never ending a piece on a small word."""
    text = " ".join(words)
    if len(text) <= maxlen or len(words) < 2:
        return [text]
    small = {"de", "du", "des", "la", "le", "les", "l'", "un", "une", "à", "au", "aux", "et", "qui", "que", "ne", "pas", "ta",
             "ton", "tes", "sa", "son", "ses", "ma", "mon", "mes", "se", "ce", "en", "dans", "sur", "par", "tu", "je", "il",
             "elle", "on", "plus", "te", "me", "nous", "vous", "leur", "lui", "mais", "ou", "si", "car", "avec", "pour"}
    best = None
    for k in range(1, len(words)):
        a, b = " ".join(words[:k]), " ".join(words[k:])
        cost = abs(len(a) - len(b)) + (40 if words[k - 1].lower() in small else 0)
        if best is None or cost < best[0]:
            best = (cost, k)
    k = best[1]
    return split_phrase(words[:k], maxlen) + split_phrase(words[k:], maxlen)


def word_chunks(text, pos, t1, tm, maxlen=40):
    """Split a line into subtitle chunks (cut at punctuation first), timed on the characters."""
    chunks, cur = [], []
    for w in text.split():
        cur.append(w)
        # a sentence end always cuts; a comma or a colon only once the piece holds a few words: without its punctuation,
        # « Huiles, / cires, / crèmes coiffantes » flashed single words too fast to read (user, 2026-10-15)
        if w[-1] in ".?!" or (w[-1] in ",:;" and len(" ".join(cur)) >= 14):
            chunks += split_phrase(cur, maxlen)
            cur = []
    if cur:
        chunks += split_phrase(cur, maxlen)
    res = []
    for c in chunks:
        i = tm.find(c.split()[0], pos)
        res.append([tm.starts[i], c])
        pos = i + len(c)
    for k in range(len(res)):
        res[k].append(res[k + 1][0] if k + 1 < len(res) else t1)
    return res


def bare(text):
    """A subtitle without its punctuation (user, 2026-10-15: « trop de ponctuation… pas forcément facile à lire »): the
    words only; « ? » and « ! » stay, joined to their word so they never wrap alone. Cuts still follow the punctuation."""
    words = []
    for w in text.split():
        w = w.strip(",.:;…«»\"“”()—–")
        if not w:
            continue
        if w in ("?", "!") and words:
            words[-1] += " " + w
        else:
            words.append(w)
    return " ".join(words)


def rank_layer(number, food, mn):
    """A ranking's band (Dr Berg « SKIM MILK », Doctor Youn's labelled pill): the rank huge in the account's display
    face, the food in capitals on a dark plate beside it. RGBA, centred by the caller near the top of the frame."""
    title = getattr(mn, "rank_font", None) or getattr(mn, "black", None) or (lambda sz, wt=900: font(sz, wt))
    fn = title(150, 900)
    ff = font(58, 800, getattr(mn, "HUD_FONT", None) or HERE.parent / "fonts" / "OpenSans.ttf")
    plate, ink = getattr(mn, "RANK_PLATE", (8, 12, 10, 205)), getattr(mn, "RANK_INK", (250, 244, 232, 255))
    halo_col = getattr(mn, "RANK_HALO", (0, 0, 0, 200))
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    num, name = f"{number}", food.upper()
    nw = d.textlength(num, font=fn)
    fw = d.textlength(name, font=ff)
    pad, gap = 30, 26
    accent = tuple(getattr(mn, "HUD", (143, 240, 192)))
    if len(num) <= 3:  # « 1 » beside « LE LAIT ÉCRÉMÉ »
        h = 190
        w = int(nw + gap + fw + 2 * pad)
        nxy, px, py = (0, h / 2 + 6), int(nw + gap), 52
    else:  # « Jour 7 » above « AUCUN CHANGEMENT »
        fn = title(110, 900)
        nw = d.textlength(num, font=fn)
        w, h = int(max(nw, fw + 2 * pad)) + 40, 260
        nxy, px, py = ((w - nw) / 2, 70), int((w - fw - 2 * pad) / 2), 150
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    dr = ImageDraw.Draw(img)
    dr.rounded_rectangle((px, py, px + fw + 2 * pad, py + 92), radius=14, fill=plate, outline=accent + (160,),
                         width=2)
    dr.text((px + pad, py + 46), name, font=ff, fill=ink, anchor="lm")
    halo = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(nxy, num, font=fn, fill=halo_col, anchor="lm")
    img = Image.alpha_composite(halo.filter(ImageFilter.GaussianBlur(10)), img)
    ImageDraw.Draw(img).text(nxy, num, font=fn, fill=accent + (255,), anchor="lm")
    return img


def hud_layer(text, accent, size=40, plate=(6, 10, 12, 165), ink=(245, 245, 240, 240), path=None):
    """A lab label laid over the visual (@deconstruct.labb: « INERTIE », « 13 900 km/h »): capitals, letter-spaced, on a
    dark glass plate with a thin accent bar on its left; « \\n » starts a second row. RGBA, just the size of the label.
    40 px: at 30 px the labels of T01 v1 could not be read on a phone."""
    f = font(size, 800, path or HERE.parent / "fonts" / "OpenSans.ttf")
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    rows = text.upper().split("\n")
    track = size * 0.12
    widths = [[d.textlength(ch, font=f) for ch in r] for r in rows]
    w = int(max(sum(ws) + track * (len(ws) - 1) for ws in widths)) + 2 * 22 + 8
    lh = size * 1.35
    h = int(lh * len(rows) + size * 0.55)
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    dr = ImageDraw.Draw(img)
    dr.rounded_rectangle((0, 0, w - 1, h - 1), radius=8, fill=plate, outline=accent + (120,), width=1)
    dr.rectangle((0, 6, 4, h - 7), fill=accent + (255,))
    for k, (r, ws) in enumerate(zip(rows, widths)):
        x = 22 + 4
        for ch, cw in zip(r, ws):
            dr.text((x, size * 0.25 + k * lh), ch, font=f, fill=ink)
            x += cw + track
    return img


def key_word(w):
    return w.lower().strip(",.:;?!«»\"'()  ").replace("’", "'")


def text_layer(text, size, weight, width=880, color=(255, 255, 255), shadow=True, align="center", path=None, keys=(), hi=None,
               box=None):
    """Centred text. `keys` (lower-case words) are drawn in `hi`, like the yellow key words of the organs carousels.
    `box` (RGBA): a rounded sticker behind each line, for light art directions (no shadow then)."""
    f = font(size, weight, path)
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    words, lines, cur = [w for w in text.split(" ") if w], [], ""  # not split(): it breaks « front ? » at its no-break space
    for w in words:
        test = (cur + " " + w).strip()
        if d.textlength(test, font=f) > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = test
    lines.append(cur)
    lh = int(size * 1.25)
    img = Image.new("RGBA", (W, lh * len(lines) + 20), (0, 0, 0, 0))
    dr = ImageDraw.Draw(img)
    for k, ln in enumerate(lines):
        x = (W - dr.textlength(ln, font=f)) / 2
        if box:
            tw = dr.textlength(ln, font=f)
            pad = size * 0.38
            dr.rounded_rectangle((x - pad, k * lh + 10 + size * 0.02, x + tw + pad, k * lh + 10 + size * 1.22),
                                 radius=int(size * 0.32), fill=box)
            shadow = False
        if shadow == "halo":  # soft dark halo: readable on bright glows (organs account)
            sh = Image.new("L", img.size, 0)
            ImageDraw.Draw(sh).text((x, k * lh + 10), ln, font=f, fill=200)
            img.paste((0, 0, 0, 255), (0, 0), sh.filter(ImageFilter.GaussianBlur(size * 0.15)))
        if shadow:
            dr.text((x + 2, k * lh + 12), ln, font=f, fill=(0, 0, 0, 200))
        sw = max(3, size // 14) if shadow == "halo" else 0  # organs: a dark outline, coloured key words stay readable on
        # a glow of the same colour (« flamber » in red on the red-glowing face)
        if hi and keys:
            for w in ln.split(" "):
                dr.text((x, k * lh + 10), w, font=f, fill=(hi if key_word(w) in keys else color) + (255,),
                        stroke_width=sw, stroke_fill=(8, 6, 12, 255))
                x += dr.textlength(w + " ", font=f)
        else:
            dr.text((x, k * lh + 10), ln, font=f, fill=color + (255,), stroke_width=sw, stroke_fill=(8, 6, 12, 255))
    return img


def counter_layer(value, unit, progress):
    """Counter like the model account's: extruded light-grey digits on a small plate, counting up to `value`."""
    try:
        v = float(value.replace(",", "."))
        if progress >= 1:
            txt = value
        elif "," in value or "." in value:
            txt = f"{v * max(0, progress):.1f}".replace(".", ",")
        else:
            txt = str(int(v * max(0, progress)))
    except ValueError:
        txt = value
    big, small = font(150, 800), font(62, 800)
    img = Image.new("RGBA", (W, 270), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    tw, uw = d.textlength(txt, font=big), d.textlength(unit, font=small)
    x, y, gap = (W - tw - 14 - uw) / 2, 8, 14
    for k in range(9, 0, -1):  # extrusion
        c = (112 + 4 * k, 92 + 3 * k, 88 + 3 * k, 255)  # warm extrusion
        d.text((x, y + k), txt, font=big, fill=c)
        d.text((x + tw + gap, y + 80 + k), unit, font=small, fill=c)
    face = Image.new("L", img.size, 0)
    fd = ImageDraw.Draw(face)
    fd.text((x, y), txt, font=big, fill=255)
    fd.text((x + tw + gap, y + 80), unit, font=small, fill=255)
    top, bottom = (252, 248, 243), (222, 208, 194)  # ivory porcelain
    grad = Image.new("RGBA", img.size)
    gd = ImageDraw.Draw(grad)
    for row in range(img.size[1]):
        f = min(1, max(0, (row - y - 30) / 140))
        gd.line([(0, row), (W, row)], fill=tuple(int(top[c] + (bottom[c] - top[c]) * f) for c in range(3)) + (255,))
    img.paste(grad, (0, 0), face)
    full = d.textlength(value, font=big) + gap + uw  # plate sized on the final value so it does not jump while counting
    px0, px1, py = (W - full) / 2 - 34, (W + full) / 2 + 34, y + big.getbbox("0")[3] + 22
    sh = Image.new("L", img.size, 0)
    ImageDraw.Draw(sh).ellipse((px0 - 10, py + 14, px1 + 10, py + 40), fill=150)
    img.paste((0, 0, 0, 255), (0, 0), sh.filter(ImageFilter.GaussianBlur(10)))
    d.rounded_rectangle((px0, py + 6, px1, py + 22), radius=8, fill=(120, 96, 90, 255))
    d.rounded_rectangle((px0, py, px1, py + 14), radius=8, fill=(236, 226, 214, 255))
    return img


def counting(value, progress):
    try:
        v = float(value.replace(",", ".").replace(" ", ""))
    except ValueError:
        return value
    if progress >= 1:
        return value
    if "," in value or "." in value:
        return f"{v * max(0, progress):.1f}".replace(".", ",")
    n = int(v * max(0, progress))
    return f"{n:,}".replace(",", " ") if " " in value else str(n)  # « 24 452 » counts with its French thousands space


def counter_mag(value, unit, progress, mn):
    """Nutrition account counter: big cream Fraunces Black figures, like a food-magazine headline, the unit in mint."""
    txt = counting(value, progress)
    big, small = mn.black(170, 900), mn.dmsans(60, 800)
    img = Image.new("RGBA", (W, 280), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    full = d.textlength(value, font=big) + 20 + d.textlength(unit, font=small)  # placed on the final value: no jump
    x, y = (W - full) / 2, 20
    sh = Image.new("L", img.size, 0)
    ImageDraw.Draw(sh).text((x + 3, y + 8), txt, font=big, fill=210)
    img.paste((0, 0, 0, 255), (0, 0), sh.filter(ImageFilter.GaussianBlur(10)))
    d.text((x, y), txt, font=big, fill=mn.CREAM + (255,))
    d.text((x + d.textlength(value, font=big) + 20, y + 100), unit, font=small, fill=mn.rgb(mn.MINT) + (255,))
    return img


def counter_holo(value, unit, progress, mn, colour=None):
    """Organs account counter: big figures in the chapter's display colour that glow like the scan, the unit in white."""
    txt = counting(value, progress)
    big, small = mn.opensans(160, 800), mn.opensans(64, 800)
    img = Image.new("RGBA", (W, 270), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    full = d.textlength(value, font=big) + 18 + d.textlength(unit, font=small)  # placed on the final value: no jump
    x, y = (W - full) / 2, 20
    yellow = colour or mn.rgb(mn.YELLOW)  # the chapter's display colour (organs: one per chapter since 2026-10-15)
    glow = Image.new("L", img.size, 0)
    gd = ImageDraw.Draw(glow)
    gd.text((x, y), txt, font=big, fill=255)
    img.paste(yellow + (255,), (0, 0), glow.filter(ImageFilter.GaussianBlur(22)).point(lambda v: int(v * 0.55)))
    sh = Image.new("L", img.size, 0)
    ImageDraw.Draw(sh).text((x + 4, y + 6), txt, font=big, fill=200)
    img.paste((0, 0, 0, 255), (0, 0), sh.filter(ImageFilter.GaussianBlur(6)))
    d.text((x, y), txt, font=big, fill=yellow + (255,), stroke_width=6, stroke_fill=(8, 6, 12, 255))
    d.text((x + d.textlength(value, font=big) + 18, y + 84), unit, font=small, fill=(255, 255, 255, 255),
           stroke_width=4, stroke_fill=(8, 6, 12, 255))
    return img


def ring_layer(cx, cy, r, t, colour=(246, 225, 60)):
    """The organs carousels' dotted yellow ring, drawn clockwise in 0.45 s around the zone, then breathing gently."""
    p = min(1.0, max(0.0, t / 0.45))
    if p <= 0:
        return None
    rr = r * (1 + 0.035 * math.sin(2 * math.pi * max(0.0, t - 0.45) / 1.6))
    pad = int(rr + 40)
    img = Image.new("RGBA", (2 * pad, 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    n = max(18, int(2 * math.pi * rr / 26))  # one dot every ~26 px, like the carousels
    for k in range(int(n * p)):
        a = -math.pi / 2 + 2 * math.pi * k / n
        x, y = pad + rr * math.cos(a), pad + rr * math.sin(a)
        d.ellipse((x - 6.5, y - 6.5, x + 6.5, y + 6.5), fill=colour + (255,))
    return img, (int(cx - pad), int(cy - pad))



def loudnorm_filter(audio, target=TARGET_LUFS):
    """Two-pass loudnorm: measure the voice first so the output really lands on the target."""
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(audio), "-af", f"loudnorm=I={target}:TP=-1.5:LRA=11:print_format=json",
                          "-f", "null", "-"], capture_output=True, text=True).stderr
    m = json.loads(out[out.rindex("{"):out.rindex("}") + 1])
    return (f"apad,loudnorm=I={target}:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
            f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")


def decode(audio, sr=48000, channels=1):
    import numpy as np
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", str(audio), "-f", "f32le", "-ac", str(channels), "-ar", str(sr), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(out, dtype=np.float32).reshape(-1, channels)


def kpower(y, hop):
    """BS.1770 K-weighted power per `hop` samples (48 kHz), summed over channels."""
    import numpy as np
    from scipy.signal import lfilter
    y = lfilter([1.0, -2.0, 1.0], [1.0, -1.99004745483398, 0.99007225036621],
                lfilter([1.53512485958697, -2.69169618940638, 1.19839281085285], [1.0, -1.69065929318241, 0.73248077421585],
                        y, axis=0), axis=0)
    n = len(y) // hop
    return (y[:n * hop].reshape(n, hop, -1) ** 2).mean(axis=1).sum(axis=1)


def voice_map(voice, hop=960):
    """Speech frames and pause frames (>= 0.4 s, 0.1 s margins, not in the first/last second) from the voice alone."""
    import numpy as np
    v = decode(voice)[:, 0]
    n = len(v) // hop
    ev = 20 * np.log10(np.sqrt((v[:n * hop].reshape(n, hop) ** 2).mean(axis=1)) + 1e-9)
    on = ev > np.percentile(ev, 95) - 25

    def pauses(min_len, margin):
        p = np.zeros(n, bool)
        k = 0
        while k < n:
            if not on[k]:
                j = k
                while j < n and not on[j]:
                    j += 1
                if (j - k) * 0.02 >= min_len and k > 50 and j < n - 50:
                    p[k + margin:j - margin] = True
                k = j
            else:
                k += 1
        return p
    pause = pauses(0.4, 5)
    if pause.sum() < 25:  # a fluid voice (nutrition, one breath per sentence) has no 0.4 s pause: use its short breaths
        pause = pauses(0.2, 2)
    return on, pause


def mix_gap(mix, on, pause, hop=960):
    """The model account's measurement: K-weighted level of the mix during speech minus during the voice pauses (dB)."""
    import numpy as np
    pm = kpower(decode(mix, channels=2), hop)
    n = min(len(pm), len(on))
    return 10 * np.log10(pm[:n][on[:n]].mean()) - 10 * np.log10(pm[:n][pause[:n]].mean())


SOUNDS = comptes.SOUNDS  # shared CTA signature: riser + impact (ElevenLabs sound effects)
RISER, RISER_PEAK, HIT = SOUNDS / "riser_2.mp3", 2.75, SOUNDS / "hit_1.mp3"
# after « abonne-toi » the music stays up, then gets its resolution: held 2.4 s (was 1.3 s: the user felt it cut « un poil
# trop tôt, au moment où le cerveau allait être satisfait », 2026-10-15) and released over its last 0.8 s
CTA_HOLD, CTA_RELEASE = 2.4, 0.8
MAX_RATE = 1.15  # fastest a clip may be played: faster reads as an unexplained speed-up
DRONE = SOUNDS / "drone_2.mp3"  # shared cold-open bed, used only where a track's opening dips to silence


def premix(d, total, loop_at=None, cta_times=None, hits=(), cuts=(), fade_in=1.0, fade_out=1.5, drone=True):
    """Voice alone, or voice + music.mp3 with the music exactly MUSIC_GAP dB under the voice as measured on the model
    account's mixes (same measurement, checked on our mix and corrected until it matches); 1 s fade-in, 1.5 s fade-out.
    Returns the audio file to encode."""
    voice, music = d / "voice.mp3", d / "music.mp3"
    if not music.exists():
        return voice
    out = d / "mix.wav"
    on, pause = voice_map(voice)
    # a generated track can dip to near silence (Lyria: E02 -63 dB in its opening, E03 a -40 dB "breath" section), heard as
    # holes in the voice pauses: lay the shared documentary drone (sons/drone_2.mp3) under every dip
    import numpy as np
    mm = decode(music)[:, 0]
    lv = np.array([10 * np.log10(np.mean(mm[k:k + 12000] ** 2) + 1e-12) for k in range(0, len(mm) - 12000, 12000)])
    med = np.median(lv)
    dips = lv < med - 15  # anywhere in the track: a stop before a hit, a quiet "breath" section, a dying opening
    # drone=False: a sparse, intimate track keeps its quiet moments (the dark drone under it read as « film d'horreur »)
    if dips.any() and drone:
        import soundfile as sf
        dips = dips | np.roll(dips, 1) | np.roll(dips, -1)
        mst = decode(music, channels=2)
        dr = decode(DRONE, channels=2)
        dr = np.tile(dr, (len(mst) // len(dr) + 1, 1))[: len(mst)]
        env = np.repeat(dips.astype(np.float32), 12000)[: len(mst)]
        env = np.pad(env, (0, len(mst) - len(env)))
        k = np.hanning(19200)  # 0.4 s fades
        from scipy.signal import fftconvolve  # np.convolve here took minutes (3 M samples x 19 200 taps)
        env = fftconvolve(env, k / k.sum(), mode="same")
        dl = 10 * np.log10(np.mean(dr[:, 0] ** 2) + 1e-12)
        g = 10 ** (((med - 18) - dl) / 20)  # the bed sits 18 dB under the track's usual level: present, still quiet
        under = d / "music_bed.wav"
        sf.write(under, (mst + dr * g * env[:, None]).astype(np.float32), 48000)
        print(f"music dips filled with the documentary drone: {dips.sum() * 0.25:.1f}s of the track")
        music = under
    fades = f",afade=t=in:d={fade_in:.2f},afade=t=out:st={total - fade_out:.3f}:d={fade_out:.2f}"
    if loop_at is not None:
        # loop: under the bridge line the music cross-fades back into its own opening, and nothing fades in or out,
        # so the end of the video sounds like its beginning
        looped = d / "music_loop.wav"
        x = 0.8
        # the reprise starts at `off` in the opening, chosen so that the last instants of the video sit at the same level as
        # the first instants: the cut back to 0 is then inaudible
        import numpy as np
        m = decode(music)[:, 0]
        lvl = lambda a: 10 * np.log10(np.mean(m[int(a * 48000):int((a + 0.25) * 48000)] ** 2) + 1e-12)
        span = total - loop_at
        off = min(np.arange(0, 6, 0.05), key=lambda o: abs(lvl(o + span - 0.25) - lvl(0)) + 0.3 * o)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(music), "-i", str(music), "-filter_complex",
                        f"[0:a]apad=whole_dur={loop_at + x:.3f},atrim=0:{loop_at + x:.3f}[a];"
                        f"[1:a]atrim={off:.3f}:{off + span + 1:.3f},asetpts=PTS-STARTPTS[b];"
                        f"[a][b]acrossfade=d={x}:c1=tri:c2=tri[m]", "-map", "[m]", str(looped)], check=True)
        music, fades = looped, ",afade=t=in:d=0.05"
    else:
        # a generated track can die out before the video ends (Lyria on E01: silent from 63 s, heard as a cut): before it
        # fades, cross-fade into a reprise of its opening at the same level, so the bed runs to the last frame
        import numpy as np
        m = decode(music)[:, 0]
        lvl = lambda a: 10 * np.log10(np.mean(m[int(a * 48000):int((a + 0.25) * 48000)] ** 2) + 1e-12)
        steps = np.arange(0, len(m) / 48000 - 0.25, 0.25)
        levels = np.array([lvl(t) for t in steps])
        alive = steps[levels > np.median(levels) - 12]
        content_end = float(alive[-1]) + 0.25 if len(alive) else 0.0
        if content_end < total - 0.5:
            x = 1.5
            at = max(0.0, content_end - x - 1.0)  # leave the track before its own fade-out
            need = total - at + 1
            if cta_times:  # a CTA needs momentum: reprise the most intense stretch of the track
                cands = np.arange(5, max(5.05, content_end - need), 0.25)
                off = max(cands, key=lambda o: np.mean([lvl(o + k) for k in np.arange(0, need, 0.5)]))
            else:
                off = min(np.arange(0, 8, 0.05), key=lambda o: abs(lvl(o + x) - lvl(at)) + 0.2 * o)
            extended = d / "music_extended.wav"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(music), "-i", str(music), "-filter_complex",
                            f"[0:a]atrim=0:{at + x:.3f}[a];[1:a]atrim={off:.3f}:{off + total - at + 1:.3f},asetpts=PTS-STARTPTS[b];"
                            f"[a][b]acrossfade=d={x}:c1=tri:c2=tri[m]", "-map", "[m]", str(extended)], check=True)
            print(f"music ends at {content_end:.1f}s < {total:.1f}s: reprise of its opening from {at:.1f}s (offset {off:.2f}s)")
            music = extended

    # music stops: (start, end) windows where the bed goes to true silence, with 15 ms ramps
    stops = "".join(f",volume='clip(max({a:.3f}-t,t-{b:.3f})/0.015,0,1)':eval=frame" for a, b in cuts)

    def render(gain, peak=False):
        if not peak:
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(voice), "-i", str(music), "-filter_complex",
                            f"[0:a]aresample=48000,apad,atrim=0:{total:.3f},pan=stereo|c0=c0|c1=c0[v];"
                            f"[1:a]aresample=48000,volume={gain:.2f}dB{stops},apad,atrim=0:{total:.3f}{fades}[m];"
                            f"[v][m]amix=inputs=2:normalize=0[a]",
                            "-map", "[a]", "-ac", "2", str(out)], check=True)
            return
        # CTA peak: the music climbs +5 dB from "Pour…" to "abonne-toi" and stays up; riser peaks on "abonne-toi"; impact
        # with the "+"; only a 0.15 s cut-fade at the very end
        t0, tb, tc = cta_times
        g = 10 ** (5 / 20)
        ramp = f"volume='if(lt(t,{tb:.3f}),1,if(lt(t,{tc:.3f}),1+{g - 1:.4f}*(t-{tb:.3f})/{tc - tb:.3f},{g:.4f}))':eval=frame"
        r_start = max(0.0, RISER_PEAK - (tc - tb) - 0.3)  # keep the end of the riser so that its peak lands on tc
        r_at = tc - (RISER_PEAK - r_start)
        sp = voice_speech_db
        r_gain = sp - 9 - RISER_DB
        h_gain = sp - 3 - HIT_DB
        # nutrition: the evidence stamp lands with a softer impact (same sound as the CTA's)
        extra = "".join(f"[{4 + j}:a]aresample=48000,volume={sp - 7 - HIT_DB:.2f}dB,adelay={int(ht * 1000)}|{int(ht * 1000)},"
                        f"apad,atrim=0:{total:.3f}[x{j}];" for j, ht in enumerate(hits))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(voice), "-i", str(music), "-i", str(RISER), "-i", str(HIT)]
                       + [a for _ in hits for a in ("-i", str(HIT))] + [
                        "-filter_complex",
                        f"[0:a]aresample=48000,apad,atrim=0:{total:.3f},pan=stereo|c0=c0|c1=c0[v];"
                        f"[1:a]aresample=48000,volume={gain:.2f}dB,apad,atrim=0:{total:.3f},{ramp},"
                        f"afade=t=in:d=1.0,afade=t=out:st={total - CTA_RELEASE:.3f}:d={CTA_RELEASE}[m];"
                        f"[2:a]aresample=48000,atrim={r_start:.3f}:{RISER_PEAK + 0.25:.3f},asetpts=PTS-STARTPTS,"
                        f"volume={r_gain:.2f}dB,adelay={int(r_at * 1000)}|{int(r_at * 1000)},apad,atrim=0:{total:.3f}[r];"
                        f"[3:a]aresample=48000,volume={h_gain:.2f}dB,adelay={int(tc * 1000)}|{int(tc * 1000)},apad,"
                        f"atrim=0:{total:.3f}[h];{extra}[v][m][r][h]{''.join(f'[x{j}]' for j in range(len(hits)))}"
                        f"amix=inputs={4 + len(hits)}:normalize=0[a]",
                        "-map", "[a]", "-ac", "2", str(out)], check=True)

    gain = -10.0
    for _ in range(4):
        render(gain)
        gap = mix_gap(out, on, pause)
        if abs(gap - MUSIC_GAP) < 0.15:
            break
        gain += gap - MUSIC_GAP  # gap too small -> music too loud -> lower it
    print(f"music {gain:+.1f} dB -> {gap:.1f} dB under the voice (model account: {MUSIC_GAP})")
    if cta_times:  # the calibration above is done without the peak; now add it
        import numpy as np
        global voice_speech_db, RISER_DB, HIT_DB
        pv = kpower(decode(voice), 960)
        voice_speech_db = 10 * np.log10(pv[on[:len(pv)]].mean())
        RISER_DB = 10 * np.log10(np.sort(kpower(decode(RISER), 960))[-10:].mean())  # loudest 0.2 s of the riser
        HIT_DB = 10 * np.log10(np.sort(kpower(decode(HIT), 960))[-10:].mean())
        render(gain, peak=True)
        print("CTA peak: music +5 dB from 'Pour', riser peaking and impact on 'abonne-toi'")
    return out


class ClipReader:
    """Frames of an animated scene by time. Decodes forward only; after the end it holds the last frame (the model
    account's scenes do one action, then hold)."""

    def __init__(self, path):
        import cv2
        self.cv2, self.path = cv2, path
        self._open()

    def _open(self):
        self.cap = self.cv2.VideoCapture(str(self.path))
        self.fps = self.cap.get(self.cv2.CAP_PROP_FPS) or 24
        self.n = int(self.cap.get(self.cv2.CAP_PROP_FRAME_COUNT)) or 1
        self.idx, self.raw, self.img, self.img_idx = -1, None, None, -2

    @property
    def length(self):
        return self.n / self.fps

    def at(self, t):
        k = min(max(0, int(t * self.fps)), self.n - 1)
        if k < self.idx:
            self._open()
        while self.idx < k:
            ok, f = self.cap.read()
            if not ok:
                self.n = max(1, self.idx + 1)
                break
            self.idx, self.raw = self.idx + 1, f
        if self.img_idx != self.idx:
            f = self.raw if (self.raw.shape[1], self.raw.shape[0]) == (W, H) else \
                self.cv2.resize(self.raw, (W, H), interpolation=self.cv2.INTER_LANCZOS4)
            self.img, self.img_idx = Image.fromarray(self.cv2.cvtColor(f, self.cv2.COLOR_BGR2RGB)), self.idx
        return self.img


import numpy as np  # noqa: E402

_yy, _xx = np.mgrid[0:H, 0:W].astype(np.float32)
GLOW_MASK = np.exp(-((_xx - W / 2) ** 2 + (_yy - 0.42 * H) ** 2) / (2 * 420.0 ** 2))[..., None]
SWEEP_D = (_xx * 0.94 + _yy * 0.34).astype(np.float32)  # distance along a slightly tilted horizontal axis


def fit(img):
    return img.convert("RGB").resize((W, H), Image.LANCZOS) if img.size != (W, H) else img.convert("RGB")


def soft_paste(frame, icon, size, xy):
    ic = icon.resize((size, size), Image.LANCZOS)
    m = Image.new("L", (size, size), 0)
    ImageDraw.Draw(m).ellipse((size * 0.1, size * 0.1, size * 0.9, size * 0.9), fill=255)
    frame.paste(ic, xy, m.filter(ImageFilter.GaussianBlur(size * 0.08)))


def menu_frame(e, icons, k):
    """Opening card: series title + 4 episode icons (phase 0), then the episode icon + part title (phase 1)."""
    frame = Image.new("RGB", (W, H), BG_EDGE)  # same teal radial gradient as the scenes (measured on the model account)
    glow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(glow).ellipse((-60, 260, 1140, 1460), fill=255)
    frame.paste(Image.new("RGB", (W, H), BG_CENTRE), (0, 0), glow.filter(ImageFilter.GaussianBlur(260)))
    if k == 0:
        t = text_layer(e["series"], 60, 700)
        frame.paste(t, (0, 330), t)
        for i, (label, *_r) in enumerate(e["menu"]):
            cx, cy = (300 if i % 2 == 0 else 780), (720 if i < 2 else 1240)
            soft_paste(frame, icons[i], 400, (cx - 200, cy - 200))
            lab = text_layer(label, 36, 500, shadow=False)
            frame.paste(lab, (cx - W // 2, cy + 165), lab)
    else:
        soft_paste(frame, icons[0], 700, (190, 470))
        t = text_layer(e["part"], 54, 700)
        frame.paste(t, (0, 1200), t)
    return frame


def chapter_menu(e, k):
    """Season art direction. Phase 0: the chapter title and its 8 parts (hero icons, today's part lit, the others dimmed).
    Phase 1: the episode's cover (same image as the thumbnail), shown when "Partie N" is spoken."""
    import re
    mn = comptes.mini(e)
    c = mn.CHAPTERS[e["chapter"] - 1]
    n = int(re.search(r"\d+", e["part"]).group())
    if k == 1:
        p = mn.OUT / "covers" / f"C{c['n']}_{n:02d}.jpg"
        return Image.open(p if p.exists() else mn.cover(c, n)).convert("RGB").resize((W, H), Image.LANCZOS)
    frame = mn.background(c["tint"])
    d = ImageDraw.Draw(frame)
    mn.draw_title(d, c["name"], 200, mn.title_font(72, 500))
    fl = mn.label_font(27, 500)
    size = 250
    for i, ep in enumerate(c["eps"]):
        cx, cy = (300 if i % 2 == 0 else 780), 520 + (i // 2) * 315
        hero = Image.open(mn.hero_path(c, i + 1)).convert("RGB") if mn.hero_path(c, i + 1).exists() else \
            Image.new("RGB", (500, 500), mn.rgb(mn.INK_EDGE))  # a part not yet illustrated stays a dark disc
        if i + 1 != n:
            hero = Image.blend(Image.new("RGB", hero.size, mn.rgb(mn.INK_EDGE)), hero, 0.45)
        soft_paste(frame, hero, size, (cx - size // 2, cy - size // 2))
        lab = f"{i + 1}. {ep[0]}"
        col = mn.TEXT if i + 1 == n else mn.mix(mn.TEXT, mn.rgb(mn.INK), 0.5)
        d.text((cx - d.textlength(lab, font=fl) / 2, cy + size // 2 + 2), lab, font=fl, fill=col)
    return frame


class CtaCard:
    """Follow CTA: phase A the chapter grid (today's part lit), phase B the other parts light up one by one, phase C the
    account emblem (profile picture) with a terracotta "+" badge that pops and pulses, like the follow button."""

    def __init__(self, e, t_b, t_c):
        import re
        mn = comptes.mini(e)
        self.mn, self.c = mn, mn.CHAPTERS[e["chapter"] - 1]
        self.n = int(re.search(r"\d+", e["part"]).group())
        self.t_b, self.t_c = t_b, t_c
        self.base = mn.background(self.c["tint"])
        d = ImageDraw.Draw(self.base)
        mn.draw_title(d, self.c["name"], 200, mn.title_font(72, 500))
        self.fill, self.plus, self.ring = mn.badge(self.c["tint"])
        self.size, self.icons = 250, []
        m = Image.new("L", (self.size, self.size), 0)
        ImageDraw.Draw(m).ellipse((25, 25, 225, 225), fill=255)
        self.mask = m.filter(ImageFilter.GaussianBlur(20))
        halo = Image.new("L", (420, 420), 0)
        ImageDraw.Draw(halo).ellipse((60, 60, 360, 360), fill=200)
        self.halo = halo.filter(ImageFilter.GaussianBlur(50))
        self.fl = mn.label_font(27, 500)
        for i, ep in enumerate(self.c["eps"]):
            p = mn.hero_path(self.c, i + 1)
            lit = (Image.open(p).convert("RGB") if p.exists() else Image.new("RGB", (500, 500), mn.rgb(mn.INK_EDGE))
                   ).resize((self.size, self.size), Image.LANCZOS)
            dim = Image.blend(Image.new("RGB", lit.size, mn.rgb(mn.INK_EDGE)), lit, 0.45)
            self.icons.append((dim, lit, f"{i + 1}. {ep[0]}", (300 if i % 2 == 0 else 780, 520 + (i // 2) * 315)))
        src = Image.open(mn.EMBLEM).convert("RGB")
        k = int(src.width * mn.EMBLEM_CROP)
        src = src.crop(((src.width - k) // 2, (src.height - k) // 2, (src.width + k) // 2, (src.height + k) // 2))
        self.emblem = src.resize((760, 760), Image.LANCZOS)
        em = Image.new("L", (760, 760), 0)
        ImageDraw.Draw(em).ellipse((40, 40, 720, 720), fill=255)
        self.emask = em.filter(ImageFilter.GaussianBlur(28))

    def light(self, i, t):
        """0 = dim, 1 = lit. Today's part is lit; the others light up one by one between t_b and t_c."""
        if i + 1 == self.n:
            return 1.0
        others = [k for k in range(len(self.icons)) if k + 1 != self.n]
        start = self.t_b + others.index(i) / len(others) * (self.t_c - self.t_b) * 0.92
        return max(0.0, min(1.0, (t - start) / 0.22))

    def grid(self, t):
        f = self.base.copy()
        d = ImageDraw.Draw(f)
        tint = self.mn.rgb(self.c["tint"])
        for i, (dim, lit, label, (cx, cy)) in enumerate(self.icons):
            a = self.light(i, t)
            pop = max(0.0, 1 - abs(a - 0.6) / 0.6) if 0 < a < 1 or (i + 1 != self.n and 0 < t - self.t_b) else 0.0
            if 0 < a and i + 1 != self.n:  # a soft terracotta flash as the part lights up
                age = (t - (self.t_b + [k for k in range(len(self.icons)) if k + 1 != self.n].index(i) / (len(self.icons) - 1)
                            * (self.t_c - self.t_b) * 0.92))
                glow = max(0.0, 1 - age / 0.6)
                if glow > 0:
                    f.paste(Image.new("RGB", (420, 420), tint), (cx - 210, cy - 210), self.halo.point(lambda v: int(v * glow * 0.8)))
            ic = Image.blend(dim, lit, a) if 0 < a < 1 else (lit if a >= 1 else dim)
            f.paste(ic, (cx - self.size // 2, cy - self.size // 2), self.mask)
            col = self.mn.mix(self.mn.mix(self.mn.TEXT, self.mn.rgb(self.mn.INK), 0.5), self.mn.TEXT, a)
            d.text((cx - d.textlength(label, font=self.fl) / 2, cy + self.size // 2 + 2), label, font=self.fl, fill=col)
        return f

    def emblem_card(self, t):
        """Emblem + "+" badge: pop at t_c (0 -> 1.15 -> 1 in 0.35 s), then a ring that pulses outward every 0.9 s."""
        f = self.mn.background(self.c["tint"]) if not hasattr(self, "_bg") else self._bg.copy()
        self._bg = getattr(self, "_bg", f.copy())
        f.paste(self.emblem, (160, 420), self.emask)
        k = t - self.t_c
        if 0 <= k < 0.6:  # light flash with the impact
            flash = Image.new("L", (1000, 1000), 0)
            ImageDraw.Draw(flash).ellipse((150, 150, 850, 850), fill=255)
            a = math.exp(-k / 0.14)
            f.paste(Image.new("RGB", (1000, 1000), self.mn.mix(self.mn.rgb(self.c["tint"]), self.mn.TEXT, 0.5)), (40, 300),
                    flash.filter(ImageFilter.GaussianBlur(120)).point(lambda v: int(v * 0.55 * a)))
            f.paste(self.emblem, (160, 420), self.emask.point(lambda v: int(v * (1 - 0.25 * a))))
        scale = 0.0 if k < 0 else (1.15 * k / 0.2 if k < 0.2 else 1.15 - 0.15 * (k - 0.2) / 0.15 if k < 0.35 else 1.0)
        cx, cy, r = 540, 1150, 66
        d = ImageDraw.Draw(f, "RGBA")
        if k > 0.35:  # pulsing ring
            ph = ((k - 0.35) % 0.9) / 0.9
            rr = r + 70 * ph
            d.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), outline=self.ring + (int(200 * (1 - ph)),), width=6)
        if scale > 0:
            rs = r * scale
            d.ellipse((cx - rs, cy - rs, cx + rs, cy + rs), fill=self.fill + (255,), outline=self.mn.TEXT + (255,), width=5)
            w, l = max(4, int(11 * scale)), int(30 * scale)
            d.rounded_rectangle((cx - l, cy - w // 2, cx + l, cy + w // 2), radius=w // 2, fill=self.plus + (255,))
            d.rounded_rectangle((cx - w // 2, cy - l, cx + w // 2, cy + l), radius=w // 2, fill=self.plus + (255,))
        if k > 0.1:  # the call itself, in the series' title face
            a = min(1.0, (k - 0.1) / 0.3)
            ft = self.mn.cta_font(96)
            txt = "Abonne-toi"
            col = tuple(int(self.mn.rgb(self.mn.INK)[j] + (self.mn.TEXT[j] - self.mn.rgb(self.mn.INK)[j]) * a) for j in range(3))
            d.text(((W - d.textlength(txt, font=ft)) / 2, 1290 + 20 * (1 - a)), txt, font=ft, fill=col + (255,))
        return f

    def at(self, t):
        if t < self.t_c - 0.3:
            return self.grid(t)
        if t < self.t_c:  # quick dissolve from the lit grid to the emblem
            return Image.blend(self.grid(t), self.emblem_card(t), (t - self.t_c + 0.3) / 0.3)
        return self.emblem_card(t)


def main(ep, preview=None):
    e = EPISODES[ep]
    d = comptes.root(e) / ep
    mn = comptes.mini(e)
    ts = json.load(open(d / "timestamps.json", encoding="utf-8"))
    tm = Timing(ts)
    times = line_times(e["lines"], tm)
    loop = e.get("loop", False)
    cta = (not loop) and e["lines"][-1][1] is None and "abonne" in e["lines"][-1][0]
    # a loop cuts right after the last word; a CTA holds; e["tail"]: the music breathes out after the last word
    total = tm.ends[-1] + (0.12 if loop else CTA_HOLD if cta else e.get("tail", TAIL))
    # opening: the chapter menu then the part card (model account), or, with open="question" (nutrition since 2026-10-15),
    # line 0 is the question itself, on its own scene, with the question written huge over it
    question = e.get("open") == "question"
    part_at = None if question else tm.at("Partie")  # the menu zooms on the episode when its title is spoken
    n_frames = int(math.ceil(total * FPS))
    first = 0 if question else 1
    icons = [] if "chapter" in e else [Image.open(d / "scenes" / f"icon_{i}.png").convert("RGB") for i in range(len(e["menu"]))]
    clips = {i: ClipReader(d / "scenes" / f"line_{i:02d}.mp4") for i in range(first, len(e["lines"]))
             if (d / "scenes" / f"line_{i:02d}.mp4").exists()}
    scenes = {i: fit(Image.open(d / "scenes" / f"line_{i:02d}.png")) for i in range(first, len(e["lines"]))
              if i not in clips and (e["lines"][i][1] or i in e.get("chain", {}))}
    menu = None if question else \
        [chapter_menu(e, 0), chapter_menu(e, 1)] if "chapter" in e else [menu_frame(e, icons, 0), menu_frame(e, icons, 1)]
    question_layer = mn.question_layer(e) if question else None
    subs = []
    st = mn.SUB  # subtitle style of the account (organs: bold Open Sans, key words in the chapter's colour)
    keys = {key_word(k) for k in e.get("keys", [])}
    disp = mn.display(e["chapter"]) if hasattr(mn, "display") and "chapter" in e else None  # organs: the chapter's colour
    st = dict(st, hi=disp) if disp else st
    for i, (text, *_r) in enumerate(e["lines"]):
        if i == 0:
            continue
        end = times[i + 1][0] if i + 1 < len(times) else (tm.ends[-1] if loop else total)  # loop: clean last frame
        for s, c, t1 in word_chunks(text, times[i][1], end, tm, maxlen=st.get("maxlen", 40)):
            card = e["lines"][i][1] is None and i not in e.get("chain", {})
            subs.append((s, t1, text_layer(bare(c), st["size"], st["weight"], width=900, path=st["font"], keys=keys, hi=st["hi"],
                                           shadow=st.get("shadow", True), color=st.get("color", (255, 255, 255)),
                                           box=st.get("box")), 1700 if card else st.get("y", 1420)))
    cta_card = None
    if cta:
        i0 = times[-1][1]
        pour = "Pour" if "Pour" in tm.full[i0:] else "pour"  # « …il en reste sept : pour décoder… » (organs v5)
        cta_card = CtaCard(e, tm.at(pour, i0), tm.at("abonne", i0))
    montage = {}  # {line: (word, [(image, label)])}: from that word on, the line's visual becomes a montage
    for i, (word, items) in e.get("montage", {}).items():
        frames = []
        for path, label in items:
            if not pathlib.Path(str(path)).suffix:
                path = mn.OUT / "heros" / f"{path}.png"  # « C1_02 » = a hero image
            elif not pathlib.Path(str(path)).is_absolute():
                path = d / path  # « scenes/line_03.png » = one of the episode's own scenes
            src = Image.open(path).convert("RGB")
            if src.width != src.height:  # a 9:16 scene: a tight square centred on its subject (the lit part of the frame)
                lum = np.asarray(src.convert("L").resize((90, 160)), dtype=np.float32)
                ys, xs = np.nonzero(lum > np.percentile(lum, 85))
                cy, cx = ys.mean() / 160 * src.height, xs.mean() / 90 * src.width
                s = int(src.width * 0.7)
                left = int(min(max(0, cx - s / 2), src.width - s))
                top = int(min(max(0, cy - s / 2), src.height - s))
                src = src.crop((left, top, left + s, top + s))
            fr = mn.background(mn.CHAPTERS[e["chapter"] - 1]["tint"])
            size = 820
            m = Image.new("L", (size, size), 0)
            ImageDraw.Draw(m).ellipse((size * 0.1, size * 0.1, size * 0.9, size * 0.9), fill=255)
            fr.paste(src.resize((size, size), Image.LANCZOS), ((W - size) // 2, 390), m.filter(ImageFilter.GaussianBlur(size * 0.08)))
            dr = ImageDraw.Draw(fr)
            fl = mn.title_font(96 if len(label) < 18 else 72, 900)
            dr.text(((W - dr.textlength(label, font=fl)) / 2, 1230), label, font=fl, fill=mn.TEXT)
            frames.append(fr)
        t0 = tm.at(word, times[i][1])
        t1 = times[i + 1][0] if i + 1 < len(times) else total
        # at least MONTAGE_STEP s per image (user, 2026-10-15: 0.6 s « défile trop vite, pas fluide du tout »): the
        # items that do not fit are dropped, never sped up
        frames = frames[:max(1, int((t1 - t0) / MONTAGE_STEP))]
        montage[i] = (t0, frames, max(MONTAGE_STEP, (t1 - t0) / len(frames)))
    hud_accent = tuple(getattr(mn, "HUD", (124, 230, 190)))
    hud_style = dict(plate=getattr(mn, "HUD_PLATE", (6, 10, 12, 165)), ink=getattr(mn, "HUD_INK", (245, 245, 240, 240)),
                     path=getattr(mn, "HUD_FONT", None))
    huds = {i: [(hud_layer(it[0], hud_accent, **hud_style), it[1], it[2], it[3] if len(it) > 3 else None) for it in items]
            for i, items in e.get("hud", {}).items()}  # lab labels, each appearing on its word (or 0.4 s in)
    tracks = {}  # {line: (xs, ys, fps)}: a circled spot followed through the shot's clip by template matching
    for li, items in e.get("graphics", {}).items():
        for kind, params, _w, *_y in items:
            if kind == "circle" and li in clips:
                import cv2
                cap = cv2.VideoCapture(str(d / "scenes" / f"line_{li:02d}.mp4"))
                fps_ = cap.get(cv2.CAP_PROP_FPS) or 24
                ok, f = cap.read()
                g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
                hh, ww = g.shape
                if params[0] is None:  # auto: the reddest spot (a pimple) below the top 40 % of the frame
                    ff = f.astype(np.float32)
                    red = ff[..., 2] - (ff[..., 1] + ff[..., 0]) / 2
                    red[: int(hh * 0.4)] = -999
                    red[:, : int(ww * 0.08)] = -999
                    red[:, int(ww * 0.92):] = -999
                    red = cv2.GaussianBlur(red, (0, 0), ww / 120)
                    yy, xx = np.unravel_index(np.argmax(red), red.shape)
                    params = (xx / ww, yy / hh) + tuple(params[2:])
                    e["graphics"][li] = [(k_, params if k_ == "circle" else p_, w_, *r_) for k_, p_, w_, *r_ in items]
                    print(f"circle on line {li}: spot found at ({params[0]:.3f}, {params[1]:.3f})")
                px, py, half = int(params[0] * ww), int(params[1] * hh), int(ww * 0.07)
                tpl = g[py - half:py + half, px - half:px + half]
                xs, ys = [], []
                while ok:
                    g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
                    x0, y0 = max(0, px - 4 * half), max(0, py - 4 * half)
                    win = g[y0:py + 4 * half, x0:px + 4 * half]
                    _, _, _, mx = cv2.minMaxLoc(cv2.matchTemplate(win, tpl, cv2.TM_CCOEFF_NORMED))
                    px, py = x0 + mx[0] + half, y0 + mx[1] + half
                    xs.append(px / ww)
                    ys.append(py / hh)
                    ok, f = cap.read()
                tracks[li] = (xs, ys, fps_)
    bottom_shade = None
    if getattr(mn, "BOTTOM_SHADE", None):  # (colour, max opacity, height in px): a soft gradient over the bottom
        col, alpha, hgt = mn.BOTTOM_SHADE
        ramp = (np.linspace(0, 1, hgt) ** 1.6 * alpha * 255).astype(np.uint8)
        a = np.zeros((H, W), np.uint8)
        a[H - hgt:] = ramp[:, None]
        bottom_shade = Image.new("RGBA", (W, H), col + (0,))
        bottom_shade.putalpha(Image.fromarray(a))
    stamps = []  # nutrition: (line, verdict, word on which the stamp lands[, claim judged, shown under it]), one per food
    for li, verdict, word, *claim in e.get("verdicts", [e["verdict"]] if "verdict" in e else []):
        stamps.append((li, tm.at(word, times[li][1]), mn.verdict_stamp(verdict, 150, claim[0] if claim else None)))
    ranks = {}  # a ranking: {first line of the item: (number, food)}, the band holds until the next item (None ends it)
    cur = None
    for i in range(len(e["lines"])):
        if i in e.get("rank", {}):
            cur = (e["rank"][i], i) if e["rank"][i] else None
        if cur:
            ranks[i] = cur
    rank_layers = {r: rank_layer(r[0], r[1], mn) for r in {v[0] for v in ranks.values()}}
    # each visual stays from its line start to the next line start
    starts = [0.0] + [times[i][0] for i in range(1, len(times))]

    def n_words(x):
        if isinstance(x, str):
            return len(x.split())
        if isinstance(x, (int, float)):
            return 1
        if isinstance(x, dict):
            return sum(n_words(v) for v in x.values())
        if isinstance(x, (list, tuple)):
            return sum(n_words(v) for v in x)
        return 0

    def line_end(li):
        return starts[li + 1] if li + 1 < len(starts) else total

    gwins = []  # (kind, params, line, t0, t1, where): every element gets about 1 s + 4 words/s, 2 s at least
    for li, items in e.get("graphics", {}).items():
        for kind, params, word, *where in items:
            t0 = tm.at(word, times[li][1]) if word else starts[li] + 0.2
            if kind == "circle":  # drawn on its shot (tracked): it ends with the shot, it lands on its word
                gwins.append((kind, params, li, t0 - 0.08, line_end(li), where))
                continue
            need = max(2.0, 1.0 + n_words(params) / 4)
            t1 = max(line_end(li), t0 + need)
            if t1 > (line_end(li + 1) if li + 1 < len(starts) else total) + 1e-6:
                print(f"graphic {kind} on line {li} dropped: {need:.1f}s needed, not enough time to read it")
                continue
            gwins.append((kind, params, li, t0, t1, where))
    for li, items in e.get("hud", {}).items():  # a lab label lives on its shot: dropped if it cannot be read there
        keep = []
        for it, lay in zip(items, huds.get(li, [])):
            t0 = tm.at(it[3], times[li][1]) if len(it) > 3 and it[3] else starts[li] + 0.4
            if line_end(li) - t0 < max(2.0, 1.0 + len(it[0].split()) / 4):
                print(f"label {it[0]!r} on line {li} dropped: not enough time to read it")
                continue
            keep.append(lay)
        huds[li] = keep

    def visual(i, t):
        if i == 0 and question:  # the opening question on its own scene (overlay added in frame_at)
            return base(0, t)
        if i == 0:
            if t < part_at - FADE:
                return menu[0]
            return Image.blend(menu[0], menu[1], min(1, (t - part_at + FADE) / FADE))
        if e["lines"][i][1] is None and i not in e.get("chain", {}):  # CTA: grid then emblem; loop bridge: opening card
            return cta_card.at(t) if cta_card else menu[0]
        if i in montage and t >= montage[i][0]:  # montage: one image per `step` seconds, each popping in (1.06 -> 1)
            t0, frames, step = montage[i]
            k = t - t0
            n = min(int(k / step), len(frames) - 1)
            f = frames[n]
            into = k - n * step  # each image dissolves in from the previous one (0.35 s), no pop
            if into < 0.35:
                prev = frames[n - 1] if n else base(i, t0)
                return Image.blend(prev, f, into / 0.35)
            return f
        return base(i, t)

    def base(i, t):
        """A line's own visual: its clip (sped up to end at ~90 % of the line) or its still (zoom, glow, fx)."""
        span = (starts[i + 1] if i + 1 < len(starts) else total) - starts[i]
        if i in clips:  # the action finishes at ~90 % of the line (x1 to x2 speed), then holds
            length = clips[i].length * e.get("clip_end", {}).get(i, 1.0)  # clip_end: stop a clip before it overdoes it
            # at most x1.15 (user, 2026-10-15: up to x2 looked « accéléré sans raison »): if the line is shorter than the
            # clip, the clip is simply cut by the cross-fade into the next line
            rate = min(MAX_RATE, max(1.0, length / (0.9 * max(span, 0.1))))
            if e.get("full_motion"):  # the clip covers the whole shot at 1x: it moves until the cut, never held
                rate = 1.0
            return clips[i].at(min((t - starts[i]) * rate, length))
        img = scenes[i]
        p = max(0.0, min(1.0, (t - starts[i]) / max(span, 0.1)))
        z = 1.0 + e.get("zoom", {}).get(i, 0.025) * p  # barely perceptible (the model's camera never moves), unless a
        # long still asks for more (nutrition: Margot's 9 s introduction)
        zw, zh = int(W * z), int(H * z)
        big = img.resize((zw, zh), Image.BILINEAR)
        # the push-in heads for the spot when the line rings it (organs photos), else for the centre; the ringed point
        # stays where the ring is drawn
        fx, fy = e.get("ring", {}).get(i, (0.5, 0.5))[:2]
        x0, y0 = int(fx * (zw - W)), int(fy * (zh - H))
        arr = np.asarray(big.crop((x0, y0, x0 + W, y0 + H)), dtype=np.float32)
        pulse = 0.5 - 0.5 * math.cos(2 * math.pi * (t - starts[i]) / 3.2)  # the light behind the object breathes
        arr *= 1 + 0.08 * pulse * GLOW_MASK
        if e.get("fx", {}).get(i) == "sweep":  # a grazing light sweeps across, left to right, once per line
            pos = -400 + (W + 800) * p
            band = np.exp(-((SWEEP_D - pos) / 170.0) ** 2)[..., None]
            arr += 55 * band * (0.4 + 0.6 * GLOW_MASK) * np.array([1.0, 0.92, 0.82], np.float32)
        if e.get("fx", {}).get(i) == "scan":  # organs: a cold scanner line runs down the subject once per line
            pos = -150 + (H * 0.8 + 300) * min(1.0, (t - starts[i]) / 2.2)
            band = np.exp(-((_yy - pos) / 26.0) ** 2)[..., None] + 0.35 * np.exp(-((_yy - pos + 70) / 90.0) ** 2)[..., None]
            arr += 70 * band * (0.25 + 0.75 * GLOW_MASK) * np.array([0.55, 0.85, 1.0], np.float32)
        return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

    def frame_at(t):
        i = max(k for k in range(len(starts)) if starts[k] <= t)
        frame = visual(i, t)
        card = i + 1 < len(starts) and e["lines"][i + 1][1] is None and i + 1 not in e.get("chain", {})
        fade = 0.9 if card else FADE  # slower into the closing card
        if i + 1 < len(starts) and starts[i + 1] - t < fade:  # cross-fade into the next visual
            frame = Image.blend(frame, visual(i + 1, t), 1 - (starts[i + 1] - t) / fade)
        frame = frame.convert("RGBA")
        if bottom_shade is not None:  # light art directions: TikTok's white captions and buttons stay readable
            frame.alpha_composite(bottom_shade)
        if question and i == 0:  # the question written huge, popping in, gone with the cross-fade into line 1
            a = min(1.0, t / 0.2) * min(1.0, max(0.0, (starts[1] - t) / FADE))
            lay = question_layer if a >= 1 else question_layer.copy()
            if a < 1:
                lay.putalpha(question_layer.getchannel("A").point(lambda v: int(v * a)))
            frame.alpha_composite(lay)
        ring = e.get("ring", {}).get(i)
        if ring and not (i + 1 < len(starts) and starts[i + 1] - t < FADE):  # dotted yellow ring around the zone
            x, y, r, *delay = ring  # x, y as fractions of the frame, r in px, optional delay after the line start (s)
            lay = ring_layer(x * W, y * H, r, t - starts[i] - (delay[0] if delay else 0.35), getattr(mn, "RING", (246, 225, 60)))
            if lay:
                frame.paste(lay[0], lay[1], lay[0])
        counter = e["lines"][i][3] if i > 0 else None
        if counter:  # appears when the figure is spoken, counts up in 0.8 s
            c0 = tm.at(counter[2], times[i][1]) if len(counter) > 2 else starts[i]
            if t >= c0:
                layer = counter_holo(counter[0], counter[1], (t - c0) / 0.8, mn, disp) if mn.COUNTER == "holo" else \
                    counter_mag(counter[0], counter[1], (t - c0) / 0.8, mn) if mn.COUNTER == "magazine" else \
                    counter_layer(counter[0], counter[1], (t - c0) / 0.8)
                frame.alpha_composite(layer, (0, 230))
        if i in ranks:  # the rank band: the number pops in at the item's first line and stays until the item ends
            r, i0 = ranks[i]
            k = t - starts[i0]
            lay = rank_layers[r]
            s = 1.0 + 0.25 * max(0.0, 1 - k / 0.2) ** 2
            a = min(1.0, k / 0.15)
            if not (i + 1 < len(starts) and ranks.get(i + 1, (None,))[0] == r):  # leaves with the item
                a *= min(1.0, max(0.0, (starts[i + 1] - t) / FADE)) if i + 1 < len(starts) else 1.0
            l2 = lay.resize((int(lay.width * s), int(lay.height * s)), Image.BICUBIC) if s > 1.001 else lay.copy()
            if a < 1:
                l2.putalpha(l2.getchannel("A").point(lambda v, a=a: int(v * a)))
            frame.alpha_composite(l2, ((W - l2.width) // 2, 215 - (l2.height - lay.height) // 2))
        for li, stamp_at, stamp_img in stamps:  # the evidence stamp slams in, then holds
            if i != li or t < stamp_at:
                continue
            k = t - stamp_at
            s = 1.0 + 0.6 * max(0.0, 1 - k / 0.16) ** 2  # from 1.6x to 1x in 0.16 s
            st = stamp_img.resize((int(stamp_img.width * s), int(stamp_img.height * s)), Image.BICUBIC)
            if k < 0.16:
                st.putalpha(st.getchannel("A").point(lambda v: int(v * min(1.0, k / 0.08 + 0.2))))
            xy = ((W - st.width) // 2, int(0.62 * H) - st.height // 2)
            sh = Image.new("RGBA", st.size, (0, 0, 0, 0))  # dark halo: the stamp stays readable on milk or sugar
            sh.putalpha(st.getchannel("A").filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(14))
                        .point(lambda v: int(v * 0.75)))
            frame.alpha_composite(sh, xy)
            frame.alpha_composite(st, xy)
        for kind, params, li, t0, t1, where in gwins:  # explanatory graphics, each in its reading window
            if not t0 <= t < t1:
                continue
            if kind == "circle" and li in tracks:  # the circle follows the spot as the phone moves
                xs, ys, fps_ = tracks[li]
                k = min(len(xs) - 1, max(0, int((t - starts[li]) * fps_)))
                params = (xs[k], ys[k]) + tuple(params[2:])
            lay, (gx, gy) = mn.GRAPHICS[kind](params, t - t0)
            if where:  # an optional height (fraction of the frame): above the subject when it sits low
                gy = int(where[0] * H)
            if kind == "circle":
                a = min(1.0, max(0.0, (t1 - t) / 0.15))
            else:  # a soft entrance (0.35 s fade, 24 px slide up) and a soft exit (0.3 s): never « en vif »
                q = min(1.0, (t - t0) / 0.35)
                a = (1 - (1 - q) ** 2) * min(1.0, max(0.0, (t1 - t) / 0.3))
                gy += int(24 * (1 - q) ** 2)
            if a <= 0:
                continue
            if a < 1:
                lay = lay.copy()
                lay.putalpha(lay.getchannel("A").point(lambda v, a=a: int(v * a)))
            frame.alpha_composite(lay, (gx, gy))
        for lay, x, y, word in huds.get(i, []):  # the label slides up 16 px and fades in, and leaves with the line
            t0 = tm.at(word, times[i][1]) if word else starts[i] + 0.4
            a = min(1.0, max(0.0, (t - t0) / 0.3))
            if i + 1 < len(starts):
                a *= min(1.0, max(0.0, (starts[i + 1] - t) / FADE))
            if a > 0:
                l2 = lay if a >= 1 else lay.copy()
                if a < 1:
                    l2.putalpha(lay.getchannel("A").point(lambda v, a=a: int(v * a)))
                frame.alpha_composite(l2, (int(x * W), int(y * H + 16 * (1 - a))))
        for s, t1, layer, y in ([] if cta_card and t >= cta_card.t_c else subs):  # the CTA title replaces the subtitle
            if s <= t < t1:
                frame.alpha_composite(layer, (0, y))
                break
        return frame.convert("RGB")

    if preview:  # a few stills to check the layout, no video
        for t in preview:
            frame_at(t).save(d / f"preview_{t:05.1f}.jpg", quality=88)
        print("lines:", [f"{x[0]:.1f}" for x in times])
        return

    music_cuts = []  # e["music_cuts"]: line -> stop at the line's start (« twist ») or before the verdict (« verdict »)
    for li, kind in e.get("music_cuts", {}).items():
        if kind == "verdict":
            st_ = next(x[1] for x in stamps if x[0] == li)
            music_cuts.append((st_ - 0.45, st_))
        else:
            music_cuts.append((starts[li] - 0.05, starts[li] + 0.4))
    audio = premix(d, total, loop_at=starts[-1] - 0.4 if loop else None,
                   cta_times=(starts[-1], cta_card.t_b, cta_card.t_c) if cta_card else None,
                   hits=[x[1] for x in stamps], cuts=music_cuts,
                   # e["tail"]: the music is there from the first frame and breathes out over the tail
                   fade_in=0.1 if "tail" in e else 1.0, fade_out=e.get("tail", 1.5), drone=e.get("drone", True))
    if e.get("sfx"):  # nutrition new format: soft sound effects on what appears (sfx.py), well under the voice
        import sfx
        ev = [(0.02, "pop")] if question else []  # the hook card lands
        for kind, _p, _li, t0, _t1, _w in gwins:
            ev.append((t0, "scribble") if kind == "circle" else (t0, "pop"))
        if "shutter" in e:  # the amateur phone photo enters
            ev.append((starts[e["shutter"]] + 0.05, "shutter"))
        for li, items in e.get("hud", {}).items():
            for it in items:
                ev.append((tm.at(it[3], times[li][1]) if len(it) > 3 and it[3] else starts[li] + 0.4, "pop"))
        ev += [(x[1], "stamp") for x in stamps]
        ev += [(starts[li], "whoosh") for li in e.get("whoosh", [])]
        ev += [(tm.at(w, times[li][1]), "chime") for li, w in e.get("chime", {}).items()]
        on, _pause = voice_map(d / "voice.mp3")
        pv = kpower(decode(d / "voice.mp3"), 960)
        speech_db = 10 * np.log10(pv[on[:len(pv)]].mean())
        kept = []
        for t_, k_ in sorted(ev):  # never two within 0.4 s (the later one goes), about 12 a minute at most
            if kept and t_ - kept[-1][0] < 0.4:
                continue
            kept.append((t_, k_))
        ev = kept[: int(12 * total / 60) + 1]
        sfx.add(audio, ev, speech_db)
        print(f"sound effects: {len(ev)}")
    cmd = ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", str(audio), "-af", loudnorm_filter(audio), "-ar", "48000", "-c:v", "libx264",
           "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest",
           "-movflags", "+faststart", str(d / "video.mp4")]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in range(n_frames):
        ff.stdin.write(frame_at(f / FPS).tobytes())
    ff.stdin.close()
    ff.wait()
    (d / "legende.txt").write_text(e["caption"], encoding="utf-8")
    print("ok", d / "video.mp4", f"{total:.1f}s")


if __name__ == "__main__":
    main(sys.argv[1], [float(x) for x in sys.argv[2:]] or None)  # comptes.EPISODES: E.. = acne, O.. = organs
