"""Account B: render the 10 dark "organ" carousels of posts_B with render_dark's panels + the new Nacria CTA.

Usage: python render_B.py [post number ...]
Writes ../compte organes/10 posts/B{NN}_{slug}/slide_01..05.png (slides 3-4 are the 1536x1024 double slides, like the model).
The yellow ring goes on the pimple given in posts_B.RING (automatic detection only for photos missing there).
"""
import sys
from concurrent.futures import ThreadPoolExecutor

import numpy as np
from PIL import Image, ImageFilter

import nacria_ui as UI
import render_dark as D
import render_gh as R
from posts_B import FOCUS, POSTS, RING, panels

OUT = D.ROOT / "10 posts"
NAMES = ["Léa", "Inès", "Camille", "Jade", "Sarah", "Mai", "Emma", "Nour", "Chloé", "Lou"]
RING_FIX = dict(RING)  # positions read by eye; detection is only a fallback for new photos
D.FOCUS.update(FOCUS)


def find_ring(name):
    """Centre of the densest group of small red spots: redness at pimple scale minus redness at a larger scale (so big red
    areas like lips or flushed cheeks don't win), then blurred to favour clusters; searched in the middle of the photo."""
    if name in RING_FIX:
        return RING_FIX[name]
    im = Image.open(D.VIS / f"{name}.png").convert("RGB").resize((480, 270))
    a = np.asarray(im, dtype=float)
    red = Image.fromarray(np.clip(a[..., 0] - (a[..., 1] + a[..., 2]) / 2 + 64, 0, 255).astype("uint8"))
    fine = np.asarray(red.filter(ImageFilter.GaussianBlur(2)), dtype=float)
    wide = np.asarray(red.filter(ImageFilter.GaussianBlur(14)), dtype=float)
    spots = Image.fromarray(np.clip((fine - wide) * 8, 0, 255).astype("uint8"))
    score = np.asarray(spots.filter(ImageFilter.GaussianBlur(10)), dtype=float)
    h, w = score.shape
    y0, y1, x0, x1 = int(h * .15), int(h * .85), int(w * .15), int(w * .85)
    sub = score[y0:y1, x0:x1]
    y, x = np.unravel_index(np.argmax(sub), sub.shape)
    return ((x + x0) / w, (y + y0) / h)


def cta(n, face_uri):
    h = D.LAYOUT["single"]["h"]
    bens = [(470, "12 semaines", "un plan, étape par étape"), (690, "3 gestes", "pas 10 produits à la fois"),
            (930, "1 photo / semaine", "même lumière, vrai suivi"), (1150, "Ton cycle", "noté à côté de ta peau")]
    b = "".join(f'<div style="position:absolute;left:640px;top:{y}px;width:410px"><div style="color:{D.YEL};font-size:46px;font-weight:800;'
                f'line-height:1.05">{t}</div><div style="font-size:32px;font-weight:600;line-height:1.25;margin-top:8px">{s}</div></div>'
                f'<div style="position:absolute;left:600px;top:{y + 18}px;width:22px;height:22px;border-radius:50%;background:{D.YEL};'
                f'border:5px solid #07070c"></div>' for y, t, s in bens)
    lis = '<li>trouve ce qui déclenche tes boutons</li><li class="y">lien en bio ↓</li>'
    return (UI.phone(NAMES[n - 1], face_uri, 40, 410, scale=.97, height=1250) + b
            + f'<div class="band" style="height:{.217 * h:.0f}px"><div>{D.rich("Tu ne sais pas|lequel c’est [chez toi] ?")}</div></div>'
            + f'<ul class="lines" style="left:640px;right:30px;top:1370px;font-size:40px">{lis}</ul>')


CTA_MODE = "follow"  # until 1,000 followers; "app" brings back the Nacria app CTA
PFP = D.ROOT / "photo de profil"


def cta_follow():
    """Follow CTA: why subscribe (one real body signal decoded a day) + the TikTok "+" to tap, no app."""
    h = D.LAYOUT["single"]["h"]
    lis = ('<li>un signal de ton corps décodé par jour</li><li>uniquement des liens réels</li>'
           '<li class="y">abonne-toi pour décoder le tien</li>')
    return (f'<img src="{(PFP / "b2_face.png").as_uri()}" style="position:absolute;left:150px;top:370px;width:780px;height:780px;'
            f'-webkit-mask-image:radial-gradient(circle at 50% 50%,#000 55%,transparent 72%)">'
            + f'<div class="band" style="height:{.217 * h:.0f}px"><div>{D.rich("Ton corps te parle|à travers ta [peau]")}</div></div>'
            + f'<ul class="lines" style="top:1190px;font-size:44px">{lis}</ul>'
            + '<div style="position:absolute;left:80px;top:1420px">'
            + UI.follow_badge((PFP / "b1_profil.png").as_uri(), color="#fff", size=124) + '</div>')


def face_for(n):
    """Square crop around the ringed pimple of the post's first photo, shown as her photo in the app."""
    name = f"b{n:02d}_1"
    x, y = find_ring(name)
    im = Image.open(D.VIS / f"{name}.png").convert("RGB")
    side = int(im.height * .7)
    cx, cy = int(x * im.width), int(y * im.height)
    l = min(max(0, cx - side // 2), im.width - side)
    t = min(max(0, cy - side // 2), im.height - side)
    dst = R.HERE / "_html_dark" / f"faceB{n:02d}.png"
    dst.parent.mkdir(exist_ok=True)
    im.crop((l, t, l + side, t + side)).resize((300, 300), Image.LANCZOS).save(dst)
    return dst.as_uri()


def render_post(n):
    slug = POSTS[n - 1][0]
    d = OUT / f"B{n:02d}_{slug}"
    d.mkdir(parents=True, exist_ok=True)
    slides = panels(n)
    for p in [p for s in slides for p in (s if isinstance(s[0], tuple) else [s])]:
        D.RING[p[1]] = find_ring(p[1])
    for k, s in enumerate(slides, 1):
        if isinstance(s[0], tuple):
            a, b = (D.shot(D.panel(*p, kind="double"), D.LAYOUT["double"]["h"], f"B{n:02d}_{k}{c}") for p, c in zip(s, "ab"))
            canvas = Image.new("RGB", (1536, 1024), "white")
            canvas.paste(a.resize((760, 1024), Image.LANCZOS), (0, 0))
            canvas.paste(b.resize((760, 1024), Image.LANCZOS), (776, 0))
            canvas.save(d / f"slide_{k:02d}.png")
        else:
            D.shot(D.panel(*s), D.LAYOUT["single"]["h"], f"B{n:02d}_{k}").save(d / f"slide_{k:02d}.png")
    D.shot(cta_follow() if CTA_MODE == "follow" else cta(n, face_for(n)), D.LAYOUT["single"]["h"], f"B{n:02d}_cta").save(d / f"slide_{len(slides) + 1:02d}.png")
    return f"B{n:02d}_{slug}"


if __name__ == "__main__":
    nums = [int(a) for a in sys.argv[1:]] or range(1, len(POSTS) + 1)
    with ThreadPoolExecutor(4) as ex:
        for line in ex.map(render_post, nums):
            print("ok", line, flush=True)
