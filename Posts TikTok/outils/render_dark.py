"""Dark "organ" carousels with the exact structure of @factslipv9n, plus a Nacre CTA slide.

Their post: slide 1 and 2 = one 2:3 panel (1024x1536); slide 3 and 4 = two panels side by side on a 1536x1024 landscape
slide, separated by a thin white line. Each panel: near-black band with two lines of Open Sans Bold (zone in yellow),
extreme close-up with a yellow dotted circle, photo fading into a navy X-ray body with a glowing anatomical visual,
one yellow line at the bottom. No arrow, no title slide.

Usage: python render_dark.py [slug]
Reads posts_dark.py, images from ../compte organes/visuels/, writes ../compte organes/10 posts/.
"""
import html, re, sys
from concurrent.futures import ThreadPoolExecutor

from PIL import Image

import render_gh as R
from posts_dark import POSTS, RING, FOCUS

ROOT = R.HERE.parent / "compte organes"
VIS = ROOT / "visuels"
OUT = ROOT / "10 posts"
W = 1080
YEL = "#f6e13c"
ZOOM = 1.55          # extreme close-up
RING_D = 214
XZ = 1.32            # zoom on the anatomy visual

# Layouts measured on their slides, as fractions of the panel height.
LAYOUT = {
    "single": dict(h=1620, band=.217, photo=.29, xray=.31, text=.814, ring_y=.42, organ=.64),
    "double": dict(h=1456, band=.20, photo=.33, xray=.36, text=.855, ring_y=.45, organ=.665),
}


def nb(t):
    """French spacing: keep ! ? : attached to the previous word."""
    return re.sub(r" ([!?:])", lambda m: " " + m.group(1), t)


def rich(t):
    t = html.escape(nb(t))
    t = re.sub(r"\[(.+?)\]", rf'<span style="color:{YEL}">\1</span>', t)
    return t.replace("|", "<br>")


def css(h):
    return f'''
@font-face{{font-family:"Open Sans";src:url("{(R.HERE / 'fonts/OpenSans.ttf').as_uri()}");font-weight:300 800}}
@font-face{{font-family:"DM Sans";src:url("{(R.HERE / 'fonts/DMSans.ttf').as_uri()}");font-weight:100 1000}}
@font-face{{font-family:"Fraunces";src:url("{(R.HERE / 'fonts/Fraunces.ttf').as_uri()}");font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{h}px;overflow:hidden;background:#07070c}}
body{{font-family:"Open Sans",sans-serif;color:#fff;position:relative}}
.band{{position:absolute;left:0;top:0;width:{W}px;background:#1a151b;display:flex;align-items:center;justify-content:center;
 text-align:center;font-size:86px;line-height:1.2;font-weight:700;letter-spacing:-.5px;padding-top:14px}}
.xray{{position:absolute;-webkit-mask-image:linear-gradient(to bottom,transparent 0,transparent 8%,#000 38%,#000 82%,transparent 100%)}}
.junction{{position:absolute;left:0;width:{W}px;background:linear-gradient(to bottom,rgba(7,7,12,0) 0,rgba(7,7,12,.85) 30%,rgba(7,7,12,.97) 45%,rgba(7,7,12,.6) 72%,rgba(7,7,12,0) 100%)}}
.photo{{position:absolute;left:0;width:{W}px;overflow:hidden;-webkit-mask-image:linear-gradient(to bottom,#000 0,#000 66%,transparent 100%)}}
.photo img{{position:absolute}}
.ring{{position:absolute;width:{RING_D}px;height:{RING_D}px;border-radius:50%;border:8px dotted {YEL}}}
.shade{{position:absolute;left:0;width:{W}px;height:260px;background:radial-gradient(ellipse 62% 50% at 50% 50%,rgba(0,0,0,.72),transparent 75%)}}
.bottom{{position:absolute;left:34px;right:34px;text-align:center;color:{YEL};line-height:1.12;font-weight:700;letter-spacing:-.5px;
 text-shadow:0 0 6px #000,0 0 14px #000,0 0 28px rgba(0,0,0,.95),0 3px 3px #000}}
.lines{{position:absolute;left:80px;right:50px;list-style:none;font-size:44px;line-height:1.32;font-weight:700}}
.lines li::before{{content:"-  ";white-space:pre}}
.lines li.y{{color:{YEL}}}
'''


def bottom_size(t):
    n = len(t)
    return 74 if n <= 24 else 68 if n <= 29 else 62 if n <= 33 else 57


def panel(top, zone, vis, bottom, kind="single"):
    L = LAYOUT[kind]
    h = L["h"]
    band, ph_h = L["band"] * h, L["photo"] * h
    # zoomed close-up, pimple placed around ring_y of the photo box
    px, py = RING.get(zone, (.5, .5))
    with Image.open(VIS / (zone + ".png")) as im:
        ratio = im.height / im.width
    zoom = 1.12 if ratio < .65 else ZOOM  # wide realistic photos (16:9) need less zoom than the 4:3 close-ups
    iw = W * zoom
    ih = iw * ratio
    left = min(0, max(W - iw, W / 2 - px * iw))
    tp = min(0, max(ph_h - ih, ph_h * L["ring_y"] - py * ih))
    rx, ry = left + px * iw, band + tp + py * ih
    if vis in FOCUS:  # anatomy render: centre the organ in the lower part of the panel, zoomed like theirs
        fx, fy, z = FOCUS[vis]
        xw = W * z
        xh = xw * 864 / 1184  # organ renders are 4:3
        xl = min(0, max(W - xw, W / 2 - fx * xw))
        xt = L["organ"] * h - fy * xh
    else:
        xw = W * XZ
        xl, xt = -(xw - W) / 2, L["xray"] * h
    t = L["text"] * h
    fs = bottom_size(bottom)
    return (f'<img class="xray" src="{(VIS / (vis + ".png")).as_uri()}" style="left:{xl:.0f}px;top:{xt:.0f}px;width:{xw:.0f}px">'
            f'<div class="photo" style="top:{band:.0f}px;height:{ph_h:.0f}px"><img src="{(VIS / (zone + ".png")).as_uri()}" '
            f'style="left:{left:.0f}px;top:{tp:.0f}px;width:{iw:.0f}px"></div>'
            f'<div class="junction" style="top:{band + ph_h - 230:.0f}px;height:400px"></div>'
            f'<div class="ring" style="left:{rx - RING_D / 2:.0f}px;top:{ry - RING_D / 2:.0f}px"></div>'
            f'<div class="band" style="height:{band:.0f}px"><div>{rich(top)}</div></div>'
            f'<div class="shade" style="top:{t - 70:.0f}px"></div>'
            f'<div class="bottom" style="top:{t:.0f}px;font-size:{fs}px">{html.escape(nb(bottom))}</div>')


def cta():
    h = LAYOUT["single"]["h"]
    lis = "".join(f'<li class="{c}">{html.escape(t)}</li>' for t, c in [
        ("la mauvaise routine aggrave l'acné", ""), ("trouve ce qui marche pour ta peau", ""), ("lien en bio ↓", "y")])
    return (f'<div class="band" style="height:{.217 * h:.0f}px"><div>{rich("Tu ne sais pas|lequel c’est [chez toi] ?")}</div></div>'
            + R.phone_shot("today", -7, 95, 420) + R.phone_shot("routine", 6, 565, 450)
            + f'<ul class="lines" style="top:1300px">{lis}</ul>')


def shot(body, h, name):
    tmp = R.HERE / "_html_dark"
    tmp.mkdir(exist_ok=True)
    f = tmp / (name + ".html")
    png = tmp / (name + ".png")
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{css(h)}</style></head><body>{body}</body></html>', encoding="utf-8")
    R.subprocess.run([R.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                      f"--window-size={W},{h}", f"--screenshot={png}", "--virtual-time-budget=3000", f.as_uri()],
                     check=True, capture_output=True, timeout=120)
    return Image.open(png).convert("RGB")


def render_post(n, post):
    slug, _caption, slides = post
    d = OUT / f"{n:02d}_{slug}"
    d.mkdir(parents=True, exist_ok=True)
    for k, s in enumerate(slides, 1):
        if isinstance(s[0], tuple):  # two panels side by side, 1536x1024 like theirs
            a, b = (shot(panel(*p, kind="double"), LAYOUT["double"]["h"], f"{slug}_{k}{c}") for p, c in zip(s, "ab"))
            canvas = Image.new("RGB", (1536, 1024), "white")
            canvas.paste(a.resize((760, 1024), Image.LANCZOS), (0, 0))
            canvas.paste(b.resize((760, 1024), Image.LANCZOS), (776, 0))
            canvas.save(d / f"slide_{k:02d}.png")
        else:
            shot(panel(*s), LAYOUT["single"]["h"], f"{slug}_{k}").save(d / f"slide_{k:02d}.png")
    shot(cta(), LAYOUT["single"]["h"], f"{slug}_cta").save(d / f"slide_{len(slides) + 1:02d}.png")
    return f"{n:02d}_{slug} {len(slides) + 1}"


if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    todo = [(n, p) for n, p in enumerate(POSTS, 1) if not only or p[0] == only]
    with ThreadPoolExecutor(4) as ex:
        for line in ex.map(lambda a: render_post(*a), todo):
            print("ok", line, flush=True)
