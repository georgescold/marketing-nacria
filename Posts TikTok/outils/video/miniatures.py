"""Covers (thumbnails) of the video account, 1080x1920, from plan.py.

One hero image per episode (Nano Banana Pro, square, the account's art direction) serves as the cover AND as the episode's
icon in the chapter's opening menu. Everything that matters sits in the central 3:4 zone (y 240-1680), which is what the
TikTok and Instagram profile grids show.

Usage: python miniatures.py demo        -> chapter 1 (8 covers) + part 1 of chapters 2 to 6
       python miniatures.py C3          -> one chapter
       python miniatures.py C3.5        -> one episode
FAL_KEY in env to generate missing hero images. Writes ../../compte vidéo/miniatures/heros/ and /covers/.
"""
import pathlib, sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from plan import CHAPTERS, HERO, INK, INK_EDGE  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
FONTS = HERE.parent / "fonts"
OUT = HERE.parent.parent / "compte vidéo" / "miniatures"
W, H = 1080, 1920
IVORY = (251, 247, 242)


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def fraunces(size, weight=500, soft=100):
    f = ImageFont.truetype(str(FONTS / "Fraunces.ttf"), size)
    f.set_variation_by_axes([min(144, max(9, size // 2)), weight, soft, 0])  # opsz, wght, SOFT, WONK
    return f


def dmsans(size, weight=500):
    f = ImageFont.truetype(str(FONTS / "DMSans.ttf"), size)
    f.set_variation_by_axes([min(40, max(9, size // 2)), weight])
    return f


def hero_path(c, k):
    return OUT / "heros" / f"C{c['n']}_{k:02d}.png"


def hero(c, k):
    """Generate the episode's hero image if missing (Nano Banana Pro, $0.15)."""
    from fal import run
    out = hero_path(c, k)
    if out.exists():
        return out
    out.parent.mkdir(parents=True, exist_ok=True)
    title, _hook, _what, _end, obj, accent = c["eps"][k - 1]
    prompt = HERO.format(obj=obj, accent=accent, ink=INK, edge=INK_EDGE, glow=c["glow"])
    run("fal-ai/nano-banana-pro", {"prompt": prompt, "aspect_ratio": "1:1", "resolution": "2K", "num_images": 1}, out)
    return out


def background(tint):
    """Warm plum-ink radial gradient with the chapter's glow, like the scenes."""
    base = Image.new("RGB", (W, H), rgb(INK_EDGE))
    for colour, box, blur, alpha in [(mix(rgb(INK), rgb(tint), 0.10), (-200, 120, 1280, 1500), 220, 255),
                                     (mix(rgb(INK), rgb(tint), 0.35), (190, 330, 890, 1030), 200, 150)]:
        m = Image.new("L", (W, H), 0)
        ImageDraw.Draw(m).ellipse(box, fill=alpha)
        base.paste(Image.new("RGB", (W, H), colour), (0, 0), m.filter(ImageFilter.GaussianBlur(blur)))
    return base


def wrap(text, font, width, draw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=font) > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = test
    lines.append(cur)
    if len(lines) == 2 and len(lines[1].split()) == 1 and len(lines[0].split()) > 1:  # no orphan word
        a = lines[0].split()
        lines = [" ".join(a[:-1]), a[-1] + " " + lines[1]]
    return lines


import colorsys, re  # noqa: E402

# Cover hook line under the subject (model account: « CIGARETTE / ce n'est pas la nicotine qui tue »). Default: the first
# sentence of the episode's closing antithesis, lower-cased.
# open-loop hook lines (user, 2026-10-15): never « ce n'est pas X », which reassures before the click; the cover raises the
# worry or the question, the video closes it
COVER_HOOK = {(1, 1): "ce que ce noir cache vraiment", (1, 2): "ce qui se cache sous ce blanc",
              (1, 3): "ce que ton corps combat en silence", (1, 4): "ce qui se passe si tu le perces",
              (1, 5): "pourquoi il ne sort jamais", (1, 6): "ce qu'ils sont vraiment", (1, 7): "partira-t-elle un jour ?",
              (1, 8): "peut-elle encore se combler ?",
              (2, 1): "pourquoi toujours la même semaine ?", (3, 1): "ton verre de lait, coupable ?",
              (4, 1): "ce qui se passe vraiment sous ta peau", (5, 1): "et si c'était ta routine ?",
              (6, 1): "tu ne vois que la fin de l'histoire"}


def bright(tint):
    """The chapter colour pushed to full brightness: the cover's subject word and pill (model: saturated cyan/orange)."""
    h, s, v = colorsys.rgb_to_hsv(*[x / 255 for x in rgb(tint)])
    return tuple(int(x * 255) for x in colorsys.hsv_to_rgb(h, min(1.0, s * 1.15), 0.95))


def subject(title):
    """« Le point noir » -> « POINT NOIR »: the subject alone, like the model's « COCAÏNE »."""
    return re.sub(r"^(le |la |les |l')", "", title, flags=re.I).upper()


def hook_line(c, k, hooks):
    if (c["n"], k) in hooks:
        return hooks[(c["n"], k)]
    first = re.split(r"(?<=[.!?])\s", c["eps"][k - 1][3])[0].rstrip(".!?")
    return first[0].lower() + first[1:]


def cover_model(c, k, bg, hero_img, st):
    """Model account's cover grammar, everything inside the central square (y 420-1500, what the Instagram grid shows;
    TikTok shows y 240-1680): series title in white capitals, coloured « PARTIE N » pill, the object, the subject in huge
    coloured capitals, the hook line in white."""
    img = bg
    d = ImageDraw.Draw(img)

    def centred(text, y, f, fill, halo=True):
        x = (W - d.textlength(text, font=f)) / 2
        if halo:
            sh = Image.new("L", img.size, 0)
            ImageDraw.Draw(sh).text((x, y), text, font=f, fill=220)
            img.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(max(6, f.size // 9))))
        d.text((x, y), text, font=f, fill=fill)

    fh = st["heavy"](76)
    y = 425
    words = c["name"].upper().split()  # two balanced lines, like « LES ADDICTIONS / EXPLIQUÉES »
    k2 = min(range(1, len(words)), key=lambda j: max(d.textlength(" ".join(words[:j]), font=fh),
                                                      d.textlength(" ".join(words[j:]), font=fh))) if len(words) > 1 else 1
    for ln in [" ".join(words[:k2]), " ".join(words[k2:])] if len(words) > 1 else words:
        centred(ln, y, fh, st["text"])
        y += int(fh.size * 1.02)
    fp = st["heavy"](40)  # pill
    label = f"PARTIE {k}"
    tw = d.textlength(label, font=fp)
    px0, py0 = (W - tw) / 2 - 28, y + 10
    d.rounded_rectangle((px0, py0, px0 + tw + 56, py0 + 62), radius=31, fill=st["pill"])
    d.text(((W - tw) / 2, py0 + 6), label, font=fp, fill=st["pill_text"])
    size = 660  # the object, melted into the background
    top = int(py0 + 40)
    m = Image.new("L", (size, size), 0)
    ImageDraw.Draw(m).ellipse((size * 0.12, size * 0.12, size * 0.88, size * 0.88), fill=255)
    img.paste(hero_img.convert("RGB").resize((size, size), Image.LANCZOS), ((W - size) // 2, top),
              m.filter(ImageFilter.GaussianBlur(size * 0.09)))  # wide feather: no visible square edge
    word = st.get("subject", subject)(c["eps"][k - 1][0])
    keyf = st.get("keyf", st["heavy"])  # the subject's face (nutrition: Fraunces Black)
    for s in range(150, 99, -4):  # as big as fits on one line, else two lines
        fk = keyf(s)
        if d.textlength(word, font=fk) <= 1000:
            lines = [word]
            break
    else:  # two balanced lines, never ending the first on a small word (« PARTOUT / À LA FOIS »)
        fk = keyf(118)
        ws = word.split()
        small = {"À", "DE", "DU", "DES", "LA", "LE", "LES", "EN", "ET", "SOUS", "SUR", "AU", "AUX"}
        j = min(range(1, len(ws)), key=lambda j: max(d.textlength(" ".join(ws[:j]), font=fk),
                                                     d.textlength(" ".join(ws[j:]), font=fk))
                + (400 if ws[j - 1] in small else 0))
        lines = [" ".join(ws[:j]), " ".join(ws[j:])]
    y = top + size - 110 - (fk.size * 0.55 if len(lines) > 1 else 0)
    for ln in lines:
        if st.get("key_glow"):  # organs: the subject glows like an alarm light behind its letters
            gl = Image.new("L", img.size, 0)
            ImageDraw.Draw(gl).text(((W - d.textlength(ln, font=fk)) / 2, y), ln, font=fk, fill=255)
            img.paste(st["key"], (0, 0), gl.filter(ImageFilter.GaussianBlur(28)).point(lambda v: int(v * 0.9)))
        centred(ln, y, fk, st["key"])
        y += int(fk.size * 0.98)
    fo = st["bold"](48)
    for ln in wrap(st["hook"](c, k), fo, 980, d):
        centred(ln, y + 22, fo, st["text"])
        y += int(fo.size * 1.2)
    return img


def cover(c, k):
    tint = bright(c["tint"])
    img = cover_model(c, k, background(c["tint"]), Image.open(hero_path(c, k)),
                      dict(heavy=lambda s: dmsans(s, 800), bold=lambda s: dmsans(s, 700), text=IVORY, key=tint, pill=tint,
                           pill_text=rgb(INK_EDGE), hook=lambda c, k: hook_line(c, k, COVER_HOOK)))
    out = OUT / "covers" / f"C{c['n']}_{k:02d}.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, quality=92)
    return out


def cover_v1(c, k):
    """First cover design (2026-10-14, serif, calm): replaced because it did not make people click."""
    tint = rgb(c["tint"])
    img = background(c["tint"])
    d = ImageDraw.Draw(img)
    # hero object, melted into the background with a soft round mask
    size = 860
    hi = Image.open(hero_path(c, k)).convert("RGB").resize((size, size), Image.LANCZOS)
    m = Image.new("L", (size, size), 0)
    ImageDraw.Draw(m).ellipse((size * 0.06, size * 0.06, size * 0.94, size * 0.94), fill=255)
    img.paste(hi, ((W - size) // 2, 300), m.filter(ImageFilter.GaussianBlur(size * 0.07)))
    # chapter label (top of the safe zone)
    lab = c["name"].upper()
    f = dmsans(30, 600)
    spaced = " ".join(lab)  # letter-spacing
    d.text(((W - d.textlength(spaced, font=f)) / 2, 262), spaced, font=f, fill=mix(tint, IVORY, 0.55))
    # part number + title
    fp = fraunces(56, 400)
    part = f"Partie {k}"
    d.text(((W - d.textlength(part, font=fp)) / 2, 1172), part, font=fp, fill=mix(tint, IVORY, 0.45))
    title = c["eps"][k - 1][0]
    ft = fraunces(108, 520)
    lines = wrap(title, ft, 900, d)
    if len(lines) > 2:
        ft = fraunces(88, 520)
        lines = wrap(title, ft, 920, d)
    y = 1262
    for ln in lines:
        d.text(((W - d.textlength(ln, font=ft)) / 2, y), ln, font=ft, fill=IVORY)
        y += int(ft.size * 1.08)
    # 8 progress dots: where this part sits in the chapter
    n, r, gap = len(c["eps"]), 9, 34
    x0 = (W - (n - 1) * gap) / 2
    for i in range(n):
        cx, cy = x0 + i * gap, 1622
        if i == k - 1:
            d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=tint)
        else:
            d.ellipse((cx - r + 2, cy - r + 2, cx + r - 2, cy + r - 2), outline=mix(tint, rgb(INK), 0.35), width=3)
    out = OUT / "covers" / f"C{c['n']}_{k:02d}.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, quality=92)
    return out


# interface used by render_video.py (chapter menu, CTA card, subtitles, counters); miniatures_organes.py has the same
TEXT = IVORY
title_font, label_font = fraunces, dmsans
EMBLEM, EMBLEM_CROP = OUT.parent / "photo de profil" / "A_coupe_de_peau.png", 0.84  # profile picture, centre used
SUB = dict(font=FONTS / "DMSans.ttf", size=40, weight=500, hi=None)  # subtitles: small and white, like the model account
COUNTER = "porcelain"


def cta_font(size):
    return fraunces(size, 520)


def draw_title(d, text, y, font):
    d.text(((W - d.textlength(text, font=font)) / 2, y), text, font=font, fill=IVORY)


def badge(tint):
    """CTA "+" badge: fill, "+" and pulsing ring colours."""
    return rgb(tint), IVORY, rgb(tint)


def targets(arg):
    if arg == "demo":
        return [(CHAPTERS[0], k) for k in range(1, 9)] + [(c, 1) for c in CHAPTERS[1:]]
    ch = CHAPTERS[int(arg[1:].split(".")[0]) - 1]
    if "." in arg:
        return [(ch, int(arg.split(".")[1]))]
    return [(ch, k) for k in range(1, len(ch["eps"]) + 1)]


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    todo = [t for a in sys.argv[1:] for t in targets(a)]
    with ThreadPoolExecutor(8) as ex:
        list(ex.map(lambda t: hero(*t), todo))
    for t in todo:
        print(cover(*t))
