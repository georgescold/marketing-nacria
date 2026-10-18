"""Covers of the nutrition account's videos, 1080x1920, from plan_nutrition.py: the model account's clickable grammar
(miniatures.cover_model) in the « food noir & verdict » art direction, plus a « VRAI OU FAUX ? » stamp that invites comments
(the open question of Glucose Goddess's « ? »). Also the evidence stamp the videos slam in on their verdict line.

Usage: python miniatures_nutrition.py demo | C3 | C3.5 | persona   (FAL_KEY in env for missing images, Nano Banana Pro)
Writes ../../compte nutrition/vidéo/miniatures/heros/ and /covers/, and ../../compte nutrition/photo de profil/.
"""
import math, pathlib, random, sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from plan_nutrition import CHAPTERS, HERO, INK, INK_EDGE, MINT, PERSONA, VERDICTS  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
FONTS = HERE.parent / "fonts"
ACCOUNT = HERE.parent.parent / "compte nutrition"
OUT = ACCOUNT / "vidéo" / "miniatures"
W, H = 1080, 1920
WHITE = (255, 255, 255)
CREAM = (250, 244, 232)


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def black(size, weight=900):
    """Fraunces Black, sharp and a little wonky: the food-magazine face (the acne account uses its soft side)."""
    f = ImageFont.truetype(str(FONTS / "Fraunces.ttf"), size)
    f.set_variation_by_axes([min(144, max(9, size // 2)), weight, 0, 1])  # opsz, wght, SOFT, WONK
    return f


def dmsans(size, weight=700):
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
    obj = c["eps"][k - 1][4]
    run("fal-ai/nano-banana-pro", {"prompt": HERO.format(obj=obj, ink=INK, edge=INK_EDGE, glow=c["glow"]),
                                   "aspect_ratio": "1:1", "resolution": "2K", "num_images": 1}, out)
    return out


PERSONA_OUT = ACCOUNT / "photo de profil"


def persona(variants=2):
    """The persona's portrait (profile picture and CTA emblem), Nano Banana Pro, $0.15 each."""
    from fal import run
    PERSONA_OUT.mkdir(parents=True, exist_ok=True)
    for v in range(1, variants + 1):
        out = PERSONA_OUT / f"margot_{v}.png"
        if not out.exists():
            run("fal-ai/nano-banana-pro", {"prompt": PERSONA, "aspect_ratio": "1:1", "resolution": "2K", "num_images": 1}, out)
        print(out)


def background(tint):
    """Forest-ink gradient with the chapter's rim-light colour and a faint grain, like a dark food set."""
    base = Image.new("RGB", (W, H), rgb(INK_EDGE))
    for colour, box, blur, alpha in [(rgb(INK), (-200, 120, 1280, 1500), 220, 255),
                                     (mix(rgb(INK), rgb(tint), 0.18), (190, 330, 890, 1030), 200, 150)]:
        m = Image.new("L", (W, H), 0)
        ImageDraw.Draw(m).ellipse(box, fill=alpha)
        base.paste(Image.new("RGB", (W, H), colour), (0, 0), m.filter(ImageFilter.GaussianBlur(blur)))
    rnd = random.Random(3)
    grain = Image.new("L", (W // 4, H // 4))
    grain.putdata([int(rnd.gauss(128, 18)) for _ in range(grain.size[0] * grain.size[1])])
    grain = grain.resize((W, H), Image.BILINEAR)
    return Image.composite(base.point(lambda v: min(255, v + 6)), base, grain.point(lambda v: 255 if v > 150 else 0))


def stamp(text, colour, size=150, angle=-9, sub=None):
    """Rubber stamp: double rounded frame, heavy capitals, slightly worn ink, tilted. Returns RGBA."""
    f = black(size, 900)
    d0 = ImageDraw.Draw(Image.new("L", (1, 1)))
    tw = d0.textlength(text, font=f)
    fs = dmsans(int(size * 0.24), 800) if sub else None
    w, h = int(tw + size * 0.9), int(size * (1.45 if not sub else 1.85))
    m = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(m)
    b = max(6, size // 16)
    d.rounded_rectangle((b, b, w - b, h - b), radius=size // 5, outline=255, width=b)
    d.rounded_rectangle((3 * b, 3 * b, w - 3 * b, h - 3 * b), radius=size // 7, outline=255, width=max(3, b // 2))
    d.text(((w - tw) / 2, (h - size * (1.0 if not sub else 1.35)) / 2 - size * 0.08), text, font=f, fill=255)
    if sub:
        d.text(((w - d.textlength(sub, font=fs)) / 2, h - 3 * b - fs.size * 1.55), sub, font=fs, fill=255)
    rnd = random.Random(len(text))  # worn ink: a few speckles knocked out
    holes = Image.new("L", (w, h), 255)
    hd = ImageDraw.Draw(holes)
    for _ in range(int(w * h / 900)):
        x, y, r = rnd.uniform(0, w), rnd.uniform(0, h), rnd.uniform(0.8, 2.6)
        hd.ellipse((x - r, y - r, x + r, y + r), fill=0)
    m = Image.composite(m, Image.new("L", (w, h), 0), holes)
    img = Image.new("RGBA", (w, h), colour + (0,))
    img.putalpha(m)
    return img.rotate(angle, resample=Image.BICUBIC, expand=True)


def verdict_stamp(verdict, size=150, claim=None):
    """The evidence stamp; under the verdict, the claim it judges (user: « on ne sait pas sur quoi le verdict se base »)."""
    return stamp(verdict, rgb(VERDICTS[verdict]), size, sub=(claim or "niveau de preuve").upper())


# the cover states the accusation or the frightening figure (user, 2026-10-15: an open « vrai ou faux » said nothing)
# and they open a loop the video closes, never « ce n'est pas X » (user, 2026-10-15)
COVER_HOOK = {(1, 1): "+12 % de risque d'acné par verre", (1, 2): "le pic qui nourrit tes boutons",
              (1, 3): "même le noir", (1, 4): "faut-il vraiment l'arrêter ?", (1, 5): "tout le monde l'accuse",
              (1, 6): "ce que le gras fait à tes pores", (1, 7): "leur sucre est-il un problème ?",
              (1, 8): "ce que tu mets dedans", (2, 1): "un litre par jour, un risque doublé",
              (3, 1): "ton visage te trahit-il ?", (4, 1): "et si c'était ton shaker ?",
              (5, 1): "30 minutes après un croissant", (6, 1): "ce que ça coûte vraiment"}


def cover(c, k, hero_img=None):
    import miniatures as base
    tint = base.bright(c["tint"])
    img = base.cover_model(c, k, background(c["tint"]), hero_img or Image.open(hero_path(c, k)),
                           dict(heavy=lambda s: dmsans(s, 800), keyf=lambda s: black(s, 900), bold=lambda s: dmsans(s, 700),
                                text=CREAM, key=tint,
                                pill=tint, pill_text=rgb(INK_EDGE), subject=lambda t: base.subject(t).replace("« ", "").replace(" »", ""),
                                hook=lambda c, k: base.hook_line(c, k, COVER_HOOK)))
    st = stamp("ACCUSÉ", rgb("#ff4d4d"), 72, angle=-11)  # the food is on trial, on the right edge of the food
    img.paste(st, (W - st.width - 60, 1000 - st.height // 2), st)
    out = OUT / "covers" / f"C{c['n']}_{k:02d}.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, quality=92)
    return out


# interface used by render_video.py (chapter menu, CTA card, subtitles, counters); same names as miniatures.py
TEXT = CREAM
EMBLEM, EMBLEM_CROP = PERSONA_OUT / "margot_1.png", 0.92  # the persona's portrait
# a little lower than the acne account's (y 1420): tall glasses and bottles reach down into the lower third
SUB = dict(font=FONTS / "DMSans.ttf", size=44, weight=700, hi=rgb(MINT), shadow="halo", maxlen=36, y=1530)
COUNTER = "magazine"


def question_layer(e):
    """The opening question written huge over the first scene (user, 2026-10-15: hook straight away with the question the
    video answers, on an impactful visual). Lower third (the food sits at 42 % of the height): series name, « PARTIE N »
    pill, then the question in Fraunces Black, the food's name in the chapter colour. Full-frame RGBA."""
    import re
    import miniatures as base
    c = CHAPTERS[e["chapter"] - 1]
    tint = base.bright(c["tint"])
    n = int(re.search(r"\d+", e["part"]).group())
    subject = re.sub(r"^(le |la |les |l')", "", e["part"].split(":", 1)[1].strip(), flags=re.I).lower()
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    fq = black(96, 900)
    words, lines, cur = e["lines"][0][0].split(), [], ""
    for w in words:
        if d.textlength((cur + " " + w).strip(), font=fq) > 1010 and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    y0 = 1640 - len(lines) * int(fq.size * 1.08)
    shadow = Image.new("L", (W, H), 0)
    sd = ImageDraw.Draw(shadow)
    fs, fp = dmsans(32, 800), dmsans(36, 800)
    series, part = e.get("series", c["name"]).upper(), f"PARTIE {n}"
    sd.rectangle((0, y0 - 190, W, H), fill=150)  # a soft dark band behind the text
    y = y0
    for ln in lines:
        sd.text(((W - d.textlength(ln, font=fq)) / 2, y), ln, font=fq, fill=255)
        y += int(fq.size * 1.08)
    img.paste((0, 0, 0, 255), (0, 0), shadow.filter(ImageFilter.GaussianBlur(40)).point(lambda v: int(v * 0.85)))
    d.text(((W - d.textlength(series, font=fs)) / 2, y0 - 150), series, font=fs, fill=CREAM + (255,))
    pw = d.textlength(part, font=fp)
    d.rounded_rectangle(((W - pw) / 2 - 26, y0 - 98, (W + pw) / 2 + 26, y0 - 42), radius=28, fill=tint + (255,))
    d.text(((W - pw) / 2, y0 - 96), part, font=fp, fill=rgb(INK_EDGE) + (255,))
    y = y0
    for ln in lines:
        x = (W - d.textlength(ln, font=fq)) / 2
        for w in ln.split(" "):
            hit = subject and subject.split()[0] in w.lower()
            d.text((x, y), w, font=fq, fill=(tint if hit else CREAM) + (255,))
            x += d.textlength(w + " ", font=fq)
        y += int(fq.size * 1.08)
    return img


def persona_scene(out, tint="#FF5A3C"):
    """Scene where Margot herself speaks (her first-person line): her portrait large in a soft circle, her name, and the
    « personnage IA » mention (transparency, AI labelling rules). Code only, free."""
    img = background(tint)
    src = Image.open(EMBLEM).convert("RGB")
    k = int(src.width * EMBLEM_CROP)
    src = src.crop(((src.width - k) // 2, (src.height - k) // 2, (src.width + k) // 2, (src.height + k) // 2))
    size = 760
    m = Image.new("L", (size, size), 0)
    ImageDraw.Draw(m).ellipse((30, 30, size - 30, size - 30), fill=255)
    img.paste(src.resize((size, size), Image.LANCZOS), ((W - size) // 2, 330), m.filter(ImageFilter.GaussianBlur(18)))
    d = ImageDraw.Draw(img)
    f, fs = black(84, 900), dmsans(36, 700)
    d.text(((W - d.textlength("Margot", font=f)) / 2, 1110), "Margot", font=f, fill=CREAM)
    # her role line (user, 2026-10-15). No diploma claimed (« diététicien » is protected); the AI disclosure is the
    # platforms' AI label and the bio, switched on at every upload
    lab = "Spécialiste de la nutrition cutanée"  # the user's wording (2026-10-15); no diploma claimed
    d.text(((W - d.textlength(lab, font=fs)) / 2, 1212), lab, font=fs, fill=rgb(MINT))
    img.save(out)
    return out


def title_font(size, weight=800):
    return black(size, 900)


def label_font(size, weight=600):
    return dmsans(size, 600)


def cta_font(size):
    return black(size, 900)


def draw_title(d, text, y, font):
    """Chapter title of the menu and CTA cards, shrunk to fit (« Les aliments qui donnent des boutons » is long)."""
    size = font.size
    while d.textlength(text, font=font) > 990 and size > 40:
        size -= 4
        font = black(size, 900)
    d.text(((W - d.textlength(text, font=font)) / 2, y + (72 - size) * 0.6), text, font=font, fill=CREAM)


def badge(tint):
    return rgb(MINT), rgb(INK_EDGE), rgb(MINT)


def targets(arg):
    if arg == "demo":
        return [(CHAPTERS[0], k) for k in range(1, 9)] + [(c, 1) for c in CHAPTERS[1:]]
    ch = CHAPTERS[int(arg[1:].split(".")[0]) - 1]
    if "." in arg:
        return [(ch, int(arg.split(".")[1]))]
    return [(ch, k) for k in range(1, len(ch["eps"]) + 1)]


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    if sys.argv[1:] == ["persona"]:
        persona()
        sys.exit()
    todo = [t for a in sys.argv[1:] for t in targets(a)]
    with ThreadPoolExecutor(8) as ex:
        list(ex.map(lambda t: hero(*t), todo))
    for t in todo:
        print(cover(*t))
