"""Covers (thumbnails) of the organs account's videos, 1080x1920, from plan_organes.py. Same layout as miniatures.py
(hero image, chapter label, « Partie N », title, 8 progress dots, all inside the 3:4 profile-grid zone y 240-1680), in the
« scanner » art direction: navy background with the chapter's glow, Open Sans ExtraBold like the carousels, alert yellow.

Usage: python miniatures_organes.py demo | C3 | C3.5   (FAL_KEY in env to generate missing hero images, Nano Banana Pro)
Writes ../../compte organes/vidéo/miniatures/heros/ and /covers/.
"""
import pathlib, random, sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from plan_organes import CHAPTERS, HERO, INK, INK_EDGE, YELLOW  # noqa: E402

# display colour: alert red, not yellow (user, 2026-10-15: « le jaune n'attire pas la peur »). Bright enough to read on
# the navy with the dark halo; the dotted ring around the zone stays yellow (a red ring would vanish on the red glow)
ALERT = "#ff3341"

HERE = pathlib.Path(__file__).resolve().parent
FONTS = HERE.parent / "fonts"
OUT = HERE.parent.parent / "compte organes" / "vidéo" / "miniatures"
W, H = 1080, 1920
WHITE = (255, 255, 255)


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def opensans(size, weight=700):
    f = ImageFont.truetype(str(FONTS / "OpenSans.ttf"), size)
    f.set_variation_by_axes([weight, 100])  # wght, wdth
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
    _title, _hook, _what, _end, obj, glow = c["eps"][k - 1]
    prompt = HERO.format(obj=obj, ink=INK, edge=INK_EDGE, glow=glow or c["glow"])
    run("fal-ai/nano-banana-pro", {"prompt": prompt, "aspect_ratio": "1:1", "resolution": "2K", "num_images": 1}, out)
    return out


def background(tint):
    """Navy radial gradient with the chapter's glow and a few floating particles, like the scenes."""
    base = Image.new("RGB", (W, H), rgb(INK_EDGE))
    for colour, box, blur, alpha in [(rgb(INK), (-200, 120, 1280, 1500), 220, 255),
                                     (mix(rgb(INK), rgb(tint), 0.22), (190, 330, 890, 1030), 200, 150)]:
        m = Image.new("L", (W, H), 0)
        ImageDraw.Draw(m).ellipse(box, fill=alpha)
        base.paste(Image.new("RGB", (W, H), colour), (0, 0), m.filter(ImageFilter.GaussianBlur(blur)))
    rnd = random.Random(7)
    dots = Image.new("L", (W, H), 0)
    dd = ImageDraw.Draw(dots)
    for _ in range(90):
        x, y, r = rnd.uniform(0, W), rnd.uniform(0, H), rnd.uniform(1.2, 3.2)
        dd.ellipse((x - r, y - r, x + r, y + r), fill=int(rnd.uniform(60, 190)))
    base.paste(Image.new("RGB", (W, H), mix(rgb(tint), WHITE, 0.3)), (0, 0), dots.filter(ImageFilter.GaussianBlur(0.8)))
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


def shadowed(img, xy, text, font, fill):
    """Text with a soft dark halo, readable on the glows (the carousels' bold white on dark)."""
    sh = Image.new("L", img.size, 0)
    ImageDraw.Draw(sh).text(xy, text, font=font, fill=230)
    img.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(10)))
    ImageDraw.Draw(img).text(xy, text, font=font, fill=fill)


# hook lines that make you feel you are missing something (user, 2026-10-15: « on a l'impression de louper quelque chose »)
# ...and that open a loop the video closes (user, 2026-10-15: « ce n'est pas ton foie » reassures, so nobody clicks; a myth
# stays a worrying question on the cover, the video answers it)
COVER_HOOK = {(1, 1): "le signal que tu ignores peut-être", (1, 2): "ce que tu fais sans le savoir",
              (1, 3): "et si c'était ton intestin ?", (1, 4): "et si c'était ton cœur ?", (1, 5): "et si c'étaient tes poumons ?",
              (1, 6): "et si c'était ton foie ?", (1, 7): "ce n'est peut-être pas de l'acné", (1, 8): "le signe à ne pas ignorer",
              (2, 1): "ils fabriquent des hormones « masculines »", (3, 1): "le pic que tu ne vois pas",
              (4, 1): "il se voit sur ta peau", (5, 1): "ton foie est-il « encrassé » ?", (6, 1): "ce qu'elle cache sous la surface"}


def display(c):
    """The chapter's display colour (user, 2026-10-15: one colour per theme, striking and frightening, never the soft
    yellow): the chapter tint pushed to full saturation and brightness. `c` = chapter dict, chapter number or tint."""
    import colorsys
    tint = c["tint"] if isinstance(c, dict) else CHAPTERS[c - 1]["tint"] if isinstance(c, int) else c
    h, s, v = colorsys.rgb_to_hsv(*[x / 255 for x in rgb(tint)])
    return tuple(int(x * 255) for x in colorsys.hsv_to_rgb(h, min(1.0, max(s, 0.85)), 1.0))


def on(colour):
    """Text colour that reads on a pill of `colour`: white on dark or saturated reds/violets, ink on light cyan/green."""
    lum = 0.2126 * colour[0] + 0.7152 * colour[1] + 0.0722 * colour[2]
    return rgb(INK_EDGE) if lum > 150 else WHITE


def cover(c, k, hero_img=None):
    """Model account's clickable grammar (miniatures.cover_model) in the scanner DA: white capitals, the subject in the
    chapter's display colour glowing like an alarm light, and a hook line that makes you feel you are missing something."""
    import miniatures as base
    col = display(c)
    img = base.cover_model(c, k, background(c["tint"]), hero_img or Image.open(hero_path(c, k)),
                           dict(heavy=lambda s: opensans(s, 800), bold=lambda s: opensans(s, 700), text=WHITE,
                                key=col, pill=col, pill_text=on(col), key_glow=True,
                                hook=lambda c, k: base.hook_line(c, k, COVER_HOOK)))
    out = OUT / "covers" / f"C{c['n']}_{k:02d}.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, quality=92)
    return out


def cover_v1(c, k):
    tint = rgb(c["tint"])
    img = background(c["tint"])
    d = ImageDraw.Draw(img)
    size = 880
    hi = Image.open(hero_path(c, k)).convert("RGB").resize((size, size), Image.LANCZOS)
    m = Image.new("L", (size, size), 0)
    ImageDraw.Draw(m).ellipse((size * 0.06, size * 0.06, size * 0.94, size * 0.94), fill=255)
    img.paste(hi, ((W - size) // 2, 290), m.filter(ImageFilter.GaussianBlur(size * 0.07)))
    spaced = " ".join(c["name"].upper())  # chapter label, letter-spaced
    f = opensans(30, 700)
    shadowed(img, ((W - d.textlength(spaced, font=f)) / 2, 262), spaced, f, mix(tint, WHITE, 0.6))
    fp = opensans(58, 800)
    part = f"PARTIE {k}"
    shadowed(img, ((W - d.textlength(part, font=fp)) / 2, 1168), part, fp, rgb(YELLOW))
    title = c["eps"][k - 1][0]
    ft = opensans(112, 800)
    lines = wrap(title, ft, 940, d)
    if len(lines) > 2 or max(d.textlength(ln, font=ft) for ln in lines) > 980:
        ft = opensans(90, 800)
        lines = wrap(title, ft, 960, d)
    y = 1258
    for ln in lines:
        shadowed(img, ((W - d.textlength(ln, font=ft)) / 2, y), ln, ft, WHITE)
        y += int(ft.size * 1.1)
    n, r, gap = len(c["eps"]), 10, 36  # 8 progress dots: where this part sits in the chapter
    x0 = (W - (n - 1) * gap) / 2
    for i in range(n):
        cx, cy = x0 + i * gap, 1622
        if i == k - 1:
            d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=rgb(YELLOW))
        else:
            d.ellipse((cx - r + 2, cy - r + 2, cx + r - 2, cy + r - 2), outline=mix(WHITE, rgb(INK), 0.55), width=3)
    out = OUT / "covers" / f"C{c['n']}_{k:02d}.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, quality=92)
    return out


# interface used by render_video.py (chapter menu, CTA card, subtitles, counters); same names as miniatures.py
TEXT = WHITE
# profile picture with its dotted ring turned white (no yellow left in the DA); the original b1_profil.png is untouched
EMBLEM, EMBLEM_CROP = OUT.parent.parent / "photo de profil" / "b1_profil_anneau_blanc.png", 0.9
# bold, key words in the chapter's display colour (render_video asks display()); lower than the acne account's (y 1420)
# because the zones (chin, mouth) sit low on the hologram head
# 3-4 words a chunk on one line, a little bigger, no punctuation (render_video.bare): easier to read (user, 2026-10-15)
SUB = dict(font=FONTS / "OpenSans.ttf", size=54, weight=800, hi=rgb(ALERT), shadow="halo", maxlen=24, y=1515)
COUNTER = "holo"
RING = (255, 255, 255)  # the dotted ring around the zone: white, readable on every chapter's glow (was the carousels' yellow)


def title_font(size, weight=800):
    return opensans(size, 800 if weight >= 500 else 600)


def label_font(size, weight=600):
    return opensans(size, 600)


def cta_font(size):
    return opensans(size, 800)


def draw_title(d, text, y, font):
    """White title, last word in the chapter's display colour (the carousels' « Si tu as un bouton sur le [Menton] »)."""
    ch = next((c for c in CHAPTERS if c["name"] == text), CHAPTERS[0])
    head, _, last = text.rpartition(" ")
    head = head + " " if head else ""
    size = font.size  # shrink to fit (« Ce que tes boutons disent de ton corps » is long)
    while d.textlength(head + last, font=font) > 990 and size > 40:
        size -= 4
        font = opensans(size, 800)
    x = (W - d.textlength(head + last, font=font)) / 2
    d.text((x, y), head, font=font, fill=WHITE)
    d.text((x + d.textlength(head, font=font), y), last, font=font, fill=display(ch))


def badge(tint):
    """CTA "+" badge: fill, "+" and pulsing ring colours, in the chapter's display colour."""
    col = display(tint)
    return col, on(col), col


SMALL = {"le", "la", "les", "l'", "de", "du", "des", "ta", "ton", "tes", "sur", "et", "si", "un", "une", "à", "au", "en", "te",
         "tu", "ce", "se", "ne", "que", "qui", "pour", "par", "dans", "avec"}


def balanced(text, font, width, draw):
    """Lines of even width that fit `width`, never ending on a small word (« sur le / menton »): the fewest lines, then
    the most even ones."""
    from itertools import combinations
    import re
    words = re.sub(r" ([?!:;»])", lambda m: "\u00a0" + m.group(1), text).split(" ")  # « front ? » keeps its « ? »
    for n in range(1, len(words) + 1):
        best = None
        for cuts in combinations(range(1, len(words)), n - 1):
            parts = [" ".join(words[a:b]) for a, b in zip((0,) + cuts, cuts + (len(words),))]
            widths = [draw.textlength(p, font=font) for p in parts]
            if max(widths) > width or any(p.split()[-1].lower() in SMALL for p in parts[:-1]):
                continue
            cost = max(widths) - min(widths)
            if best is None or cost < best[0]:
                best = (cost, parts)
        if best:
            return best[1]
    return wrap(text, font, width, draw)


def question_layer(e):
    """The opening question written huge over the photo of the spot (user, 2026-10-15: « les hooks, il faut les renforcer
    visuellement et dans le texte », as on the nutrition account). Lower third, the spot sits at 42 % of the height: series
    name in white capitals, « PARTIE N » pill and the zone's name in the chapter's display colour, like the covers. RGBA."""
    import re
    col = display(e["chapter"])
    n = int(re.search(r"\d+", e["part"]).group())
    subject = re.sub(r"^(le |la |les |l')", "", e["part"].split(":", 1)[1].strip(), flags=re.I).lower()
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for size in (100, 94, 88, 82, 76):  # the biggest size that holds the question in three even lines
        fq = opensans(size, 800)
        lines = balanced(e["lines"][0][0], fq, 1000, d)
        if len(lines) <= 3:
            break
    lh = int(fq.size * 1.12)
    y0 = 1690 - len(lines) * lh
    fs, fp = opensans(34, 800), opensans(38, 800)
    series, part = CHAPTERS[e["chapter"] - 1]["name"].upper(), f"PARTIE {n}"
    shade = Image.new("L", (W, H), 0)  # a soft dark band behind the text, so the photo stays visible above it
    sd = ImageDraw.Draw(shade)
    sd.rectangle((0, y0 - 200, W, H), fill=170)
    for k, ln in enumerate(lines):
        sd.text(((W - d.textlength(ln, font=fq)) / 2, y0 + k * lh), ln, font=fq, fill=255)
    band = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    band.paste((0, 0, 0, 255), (0, 0), shade.filter(ImageFilter.GaussianBlur(45)).point(lambda v: int(v * 0.88)))
    d.text(((W - d.textlength(series, font=fs)) / 2, y0 - 160), series, font=fs, fill=WHITE + (255,))
    pw = d.textlength(part, font=fp)
    d.rounded_rectangle(((W - pw) / 2 - 28, y0 - 104, (W + pw) / 2 + 28, y0 - 44), radius=30, fill=col + (255,))
    d.text(((W - pw) / 2, y0 - 101), part, font=fp, fill=on(col) + (255,))
    glow = Image.new("L", (W, H), 0)  # the zone's name glows like an alarm light, as on the covers
    gd = ImageDraw.Draw(glow)
    for k, ln in enumerate(lines):
        x = (W - d.textlength(ln, font=fq)) / 2
        for w in ln.split(" "):
            hit = subject.split()[0] in re.sub(r"[^\w]", "", w.lower())
            if hit:
                gd.text((x, y0 + k * lh), w, font=fq, fill=200)
            d.text((x, y0 + k * lh), w, font=fq, fill=(col if hit else WHITE) + (255,),
                   stroke_width=3 if hit else 0, stroke_fill=(20, 0, 0, 255))
            x += d.textlength(w + " ", font=fq)
    halo = Image.new("RGBA", (W, H), col + (0,))
    halo.putalpha(glow.filter(ImageFilter.GaussianBlur(22)).point(lambda v: int(v * 0.7)))
    return Image.alpha_composite(Image.alpha_composite(band, halo), img)


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
