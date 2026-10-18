"""Art direction « Porcelaine & lie-de-vin » of the nutrition account's new format (T01…), 2026-10-16.

Built only from the avatar's world (the user: « tout doit tourner autour de l'avatar », never the app's branding):
reports/DA avatar/marques.md (41 brands Camille buys or follows, colours and fonts read from their CSS) and tendances.md.
- Ground: warm off-white (mean of 18 of her brands), never a dark base (« vert foncé… triste »).
- Ink: a soft warm black; one accent, lie-de-vin, the colour shared by her women's-health, food and fashion brands.
- Titles in Cormorant Garamond (Aime, Polène, Nuxe), text in Manrope (Aime, Musier); square-ish editorial shapes.
- Verdicts in the traffic-light order she reads in Yuka, muted into the palette.
Same interface as miniatures_nutrition for render_video (SUB, HUD…, question_layer, verdict_stamp); an episode picks it
with mini="miniatures_porcelaine".
"""
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from miniatures_nutrition import *  # noqa: F401,F403  (OUT, CHAPTERS, W, H, rgb, mix, TEXT, INK… for the shared code)
from miniatures_nutrition import FONTS, H, W, rgb
from plan_nutrition import BRIQUE, ENCRE, LIE_DE_VIN, OCRE, PORCELAINE, SABLE, SAUGE, TAUPE

VERDICTS = {"PROUVÉ": SAUGE, "PROBABLE": OCRE, "PAS PROUVÉ": TAUPE, "FAUX": BRIQUE}
VERDICT_INK = {"PROUVÉ": "#FFFFFF", "PROBABLE": ENCRE, "PAS PROUVÉ": "#FFFFFF", "FAUX": "#FFFFFF"}  # contrast ≥ 4.8:1


def _font(file, size, weight):
    f = ImageFont.truetype(str(FONTS / file), size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f


def manrope(size, weight=700):
    return _font("Manrope.ttf", size, weight)


def serif(size, weight=700):
    return _font("CormorantGaramond.ttf", size, weight)


# subtitles: Manrope Bold, soft-black ink on a porcelain sticker, key words in lie-de-vin; kept above TikTok's bottom UI
SUB = dict(font=FONTS / "Manrope.ttf", size=50, weight=700, color=rgb(ENCRE), hi=rgb(LIE_DE_VIN),
           box=rgb(PORCELAINE) + (236,), shadow=False, maxlen=30, y=1440)
# lab labels and the timeline band: porcelain plates, lie-de-vin bar and figures, ink capitals
HUD = rgb(LIE_DE_VIN)
HUD_PLATE, HUD_INK, HUD_FONT = rgb(PORCELAINE) + (236,), rgb(ENCRE) + (255,), FONTS / "Manrope.ttf"
RANK_PLATE, RANK_INK, RANK_HALO = rgb(PORCELAINE) + (236,), rgb(ENCRE) + (255,), rgb(PORCELAINE) + (235,)
# TikTok draws its own white captions and buttons over the bottom of the frame: unreadable on porcelain without a shade
BOTTOM_SHADE = (rgb(ENCRE), 0.55, 400)


def rank_font(size, weight=700):
    return serif(int(size * 1.08), 700)


def stamp(text, colour, size=150, angle=-6, sub=None, ink=(255, 255, 255)):
    """The evidence label: a solid editorial tag (square corners, Manrope ExtraBold capitals), slightly tilted. RGBA."""
    f = manrope(int(size * 0.62), 800)
    fs = manrope(int(size * 0.2), 800) if sub else None
    d0 = ImageDraw.Draw(Image.new("L", (1, 1)))
    track = size * 0.05
    tw = sum(d0.textlength(c, font=f) for c in text) + track * (len(text) - 1)
    sw = d0.textlength(sub, font=fs) if sub else 0
    w = int(max(tw, sw) + size * 0.8)
    h = int(size * (0.95 if not sub else 1.3))
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=int(size * 0.07), fill=colour + (255,))
    x = (w - tw) / 2
    for c in text:
        d.text((x, size * 0.14), c, font=f, fill=ink + (255,))
        x += d.textlength(c, font=f) + track
    if sub:
        d.line((size * 0.4, size * 0.93, w - size * 0.4, size * 0.93), fill=ink + (110,), width=2)
        d.text(((w - sw) / 2, size * 1.0), sub, font=fs, fill=ink + (235,))
    return img.rotate(angle, resample=Image.BICUBIC, expand=True)


def verdict_stamp(verdict, size=150, claim=None):
    return stamp(verdict, rgb(VERDICTS[verdict]), size, sub=(claim or "niveau de preuve").upper(),
                 ink=rgb(VERDICT_INK[verdict]))


def question_layer(e):
    """The opening line on a porcelain card near the top, the problem visible below it: the series in lie-de-vin
    capitals, then the hook in Cormorant Garamond, the subject's word in lie-de-vin. Full-frame RGBA."""
    import re
    n = int(re.search(r"\d+", e["part"]).group())
    subject = re.sub(r"^(le |la |les |l')", "", e["part"].split(":", 1)[1].strip(), flags=re.I).lower()
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    fq = serif(98, 700)
    words, lines, cur = e["lines"][0][0].split(" "), [], ""
    for w in words:
        if d.textlength((cur + " " + w).strip(), font=fq) > 900 and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    lh = int(fq.size * 1.02)
    fs = manrope(30, 800)
    series = ""  # user, 2026-10-16: no series name nor part number on screen (each video is seen alone)
    # at the top (under TikTok's tabs): the spots on the chin, lower in the selfie, must stay visible (the trigger)
    top = 300
    card = (60, top, W - 60, top + 40 + len(lines) * lh + 44)
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).rounded_rectangle((card[0], card[1] + 14, card[2], card[3] + 14), radius=22, fill=120)
    img.paste(rgb(ENCRE) + (255,), (0, 0), sh.filter(ImageFilter.GaussianBlur(26)))
    d.rounded_rectangle(card, radius=22, fill=rgb(PORCELAINE) + (246,))
    tr = 30 * 0.12
    sw = sum(d.textlength(c, font=fs) for c in series) + tr * (len(series) - 1)
    x = (W - sw) / 2
    for c in series:
        d.text((x, top + 38), c, font=fs, fill=rgb(LIE_DE_VIN) + (255,))
        x += d.textlength(c, font=fs) + tr
    y = top + 40
    for ln in lines:
        x = (W - d.textlength(ln, font=fq)) / 2
        for w in ln.split(" "):
            key = (e.get("hook_key") or subject.split()[0]).lower()
            hit = key and key in w.lower()
            d.text((x, y), w, font=fq, fill=(rgb(LIE_DE_VIN) if hit else rgb(ENCRE)) + (255,))
            x += d.textlength(w + " ", font=fq)
        y += lh
    return img


# ---- explanatory graphics (render_video draws e["graphics"] = {line: [(kind, params, word)]}) ----------------------
import math  # noqa: E402


def _ease(p):
    p = min(1.0, max(0.0, p))
    return 1 - (1 - p) ** 3


def _card(w, h):
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sh = Image.new("L", (w, h), 0)
    ImageDraw.Draw(sh).rounded_rectangle((18, 26, w - 18, h - 8), radius=22, fill=110)
    img.paste(rgb(ENCRE) + (255,), (0, 0), sh.filter(ImageFilter.GaussianBlur(16)))
    ImageDraw.Draw(img).rounded_rectangle((10, 10, w - 10, h - 22), radius=22, fill=rgb(PORCELAINE) + (246,))
    return img


def _caps(d, xy, text, size, fill, track=0.12, anchor_center=None):
    f = manrope(size, 800)
    widths = [d.textlength(c, font=f) for c in text]
    tw = sum(widths) + size * track * (len(text) - 1)
    x, y = xy
    if anchor_center is not None:
        x = anchor_center - tw / 2
    for c, cw in zip(text, widths):
        d.text((x, y), c, font=f, fill=fill)
        x += cw + size * track
    return tw


def gi_bars(params, p):
    """Bars that grow: params = [(label, value, highlighted)…] (index glycémique) or dict(title, items, fmt, source).
    Returns (RGBA, (x, y))."""
    title, fmt, source = "INDEX GLYCÉMIQUE", "{}", None
    if isinstance(params, dict):
        title, fmt, source = params["title"].upper(), params.get("fmt", "{}"), params.get("source")
        params = params["items"]
    w, h = 940, 120 + 120 * len(params) + (40 if source else 0)
    img = _card(w, h)
    d = ImageDraw.Draw(img)
    _caps(d, (54, 46), title, 30, rgb(LIE_DE_VIN) + (255,))
    if source:
        _caps(d, (54, h - 70), source.upper(), 22, rgb(TAUPE) + (255,))
    vmax = max(v for _, v, _ in params) * 1.08
    for k, (label, v, hot) in enumerate(params):
        y = 110 + k * 120
        q = _ease((p - 0.15 * k) / 0.8)
        d.text((54, y), label, font=manrope(36, 700), fill=rgb(ENCRE) + (255,))
        bw = int((w - 108 - 120) * v / vmax * q)
        col = rgb(LIE_DE_VIN) if hot else rgb(TAUPE)
        d.rounded_rectangle((54, y + 50, 54 + max(bw, 8), y + 90), radius=8, fill=col + (255,))
        shown = round(v * q, 1) if isinstance(v, float) and v != int(v) else int(round(v * q))
        d.text((54 + bw + 18, y + 44), fmt.format(str(shown).replace(".", ",")), font=serif(52, 700), fill=col + (255,))
    return img, ((W - w) // 2, 1050)


def glucose_curve(params, p):
    """The blood-sugar spike drawing itself, then the crash (the curve her world knows from Glucose Goddess).
    params = dict(label=…, peak=…). Returns (RGBA, (x, y))."""
    w, h = 940, 420
    img = _card(w, h)
    d = ImageDraw.Draw(img)
    _caps(d, (54, 46), params.get("label", "TA GLYCÉMIE"), 30, rgb(LIE_DE_VIN) + (255,))
    x0, x1, base, top = 70, w - 70, 320, 110
    d.line((x0, base, x1, base), fill=rgb(TAUPE) + (110,), width=3)  # the calm line
    pts = []
    for k in range(201):
        t = k / 200
        spike = math.exp(-((t - 0.32) / 0.09) ** 2)            # the rise after the breakfast
        crash = -0.32 * math.exp(-((t - 0.58) / 0.08) ** 2)    # then the crash under the baseline
        y = base - (base - top) * (0.06 + spike + crash) / 1.06
        pts.append((x0 + (x1 - x0) * t, y))
    n = max(2, int(len(pts) * _ease(p / 1.0)))
    d.line(pts[:n], fill=rgb(LIE_DE_VIN) + (255,), width=9, joint="curve")
    if n > 70:  # the peak marker once the line has passed it
        px, py = pts[64]
        d.ellipse((px - 13, py - 13, px + 13, py + 13), fill=rgb(LIE_DE_VIN) + (255,))
        d.text((px + 26, py - 12), params.get("peak", "pic de sucre"), font=manrope(34, 800), fill=rgb(ENCRE) + (255,))
    return img, ((W - w) // 2, 1010)


def stat_card(params, p):
    """A study in one card: the big figure counting up, what it shows, the source. params = dict(number, text, source)."""
    w, h = 940, 330
    img = _card(w, h)
    d = ImageDraw.Draw(img)
    num = params["number"]
    digits = int(num.replace(" ", ""))
    shown = f"{int(digits * _ease(p / 0.8)):,}".replace(",", " ")
    d.text((54, 34), shown, font=serif(120, 700), fill=rgb(LIE_DE_VIN) + (255,))
    d.text((54, 170), params["text"], font=manrope(40, 700), fill=rgb(ENCRE) + (255,))
    _caps(d, (54, 240), params["source"].upper(), 24, rgb(TAUPE) + (255,))
    tw = d.textlength(num, font=serif(120, 700))
    for k, (dy, tilt) in enumerate([(0, 0), (12, 3)]):  # a hand double underline once the count-up has ended
        q = _ease((p - 0.8 - 0.08 * k) / 0.18)
        if q > 0:
            y = 168 + dy
            d.line([(54, y), (54 + (tw + 10) * q, y + tilt * q)], fill=rgb(LIE_DE_VIN) + (255,), width=5)
    return img, ((W - w) // 2, 1080)


def circle_doodle(params, p):
    """A hand-drawn circle around the spot, drawing itself in 0.6 s (the « girl edit » annotation). params = (x, y, r)
    as fractions of the frame and px. Returns a full-frame RGBA."""
    x, y, r = params
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    q = _ease(p / 0.6)
    pts = []
    for k in range(int(130 * q) + 1):
        a = -1.9 + 2 * math.pi * 1.12 * k / 130  # a little more than one turn, like a pen
        rr = r * (1 + 0.07 * math.sin(3 * a + 0.6)) * (1 + 0.05 * k / 130)
        pts.append((x * W + rr * math.cos(a) * 1.08, y * H + rr * math.sin(a) * 0.94))
    if len(pts) > 1:
        d.line(pts, fill=rgb(PORCELAINE) + (255,), width=11, joint="curve")
        d.line(pts, fill=rgb(LIE_DE_VIN) + (255,), width=7, joint="curve")
    return img, (0, 0)


def aside(params, p):
    """A small paper note taped on the frame (« LE PIRE ? »): porcelain card, a sable washi-tape strip on a corner,
    lie-de-vin capitals, slightly tilted; pops in (0.90 -> 1.04 -> 1.00). params = (text, angle)."""
    text, angle = params
    f = manrope(54, 800)  # 34 px (v4 first render) could not be read on a phone
    d0 = ImageDraw.Draw(Image.new("L", (1, 1)))
    tw = sum(d0.textlength(c, font=f) for c in text) + 54 * 0.04 * (len(text) - 1)
    w, h = int(tw + 84), 132
    card = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0))
    sh = Image.new("L", card.size, 0)
    ImageDraw.Draw(sh).rounded_rectangle((22, 28, w + 22, h + 26), radius=6, fill=120)
    card.paste(rgb(ENCRE) + (255,), (0, 0), sh.filter(ImageFilter.GaussianBlur(10)))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle((20, 20, w + 20, h + 20), radius=6, fill=rgb(PORCELAINE) + (255,))
    x = 62
    for c in text:
        d.text((x, 20 + (h - 72) / 2), c, font=f, fill=rgb(LIE_DE_VIN) + (255,))
        x += d.textlength(c, font=f) + 54 * 0.04
    tape = Image.new("RGBA", (150, 44), rgb(SABLE) + (205,))
    tape = tape.rotate(-28, expand=True, resample=Image.BICUBIC)
    card.alpha_composite(tape, (w - 60, -6))
    out = card.rotate(angle, expand=True, resample=Image.BICUBIC)  # the renderer fades and slides it in (no pop)
    return out, (70, int(0.30 * H))


GRAPHICS = dict(gi_bars=gi_bars, glucose_curve=glucose_curve, stat_card=stat_card, circle=circle_doodle, aside=aside)


# ---- TikTok covers (2026-10-18): the subject huge in lie-de-vin, the hook under it, over a daylight hero photo -------
# The profile grid shows a centred 3:4 crop of the 9:16 cover: all text stays inside y 300-1620.
COVER_HERO = ("Natural lifestyle food photograph for a social media cover, vertical 9:16 frame: {obj}. Soft directional "
              "window daylight with a warm white balance, gentle natural shadows, slight film grain, real home food on matte "
              "stoneware, a warm off-white linen tablecloth and plaster wall (#F8F4F0 to sand #E9E2D8). The subject sits in "
              "the lower half of the frame, its centre at about 66 percent of the frame height, occupying about 60 percent "
              "of the frame width, sharp and appetising. The upper half of the frame is calm, plain and bright (soft wall). "
              "Full-bleed. No text, no labels, no brand, no logo, no hands, no people.")


def cover_porcelaine(hero_path, subject, hook, out):
    """1080x1920 cover: the hero photo, a soft porcelain veil at the top, the subject in Cormorant Garamond (lie-de-vin),
    the hook in Manrope (ink)."""
    img = Image.open(hero_path).convert("RGB").resize((W, H), Image.LANCZOS).convert("RGBA")
    veil = Image.new("L", (W, H), 0)
    for y in range(0, 1100):
        a = int(200 * max(0.0, min(1.0, (1100 - y) / 700)))
        ImageDraw.Draw(veil).line((0, y, W, y), fill=a)
    img.paste(rgb(PORCELAINE) + (255,), (0, 0), veil)
    d = ImageDraw.Draw(img)
    fs = serif(150 if len(subject) <= 16 else 124, 700)
    words, lines, cur = subject.split(" "), [], ""
    for w in words:
        if d.textlength((cur + " " + w).strip(), font=fs) > 920 and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    y = 360
    for ln in lines:
        d.text(((W - d.textlength(ln, font=fs)) / 2, y), ln, font=fs, fill=rgb(LIE_DE_VIN) + (255,))
        y += int(fs.size * 1.0)
    fh = manrope(62, 700)
    hook = hook.replace(" ?", " ?").replace(" !", " !").replace(" :", " :")  # never a lone « ? »
    hl, cur = [], ""
    for w in hook.split(" "):
        if d.textlength((cur + " " + w).strip(), font=fh) > 880 and cur:
            hl.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    hl.append(cur)
    y += 40
    for ln in hl:
        d.text(((W - d.textlength(ln, font=fh)) / 2, y), ln, font=fh, fill=rgb(ENCRE) + (255,))
        y += 76
    img.convert("RGB").save(out, quality=92)
    return out
