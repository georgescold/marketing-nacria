"""Account A: render the 10 face-map carousels of posts_A in the @glowhubdaily template (1080x1350) + the Nacria CTA.

Usage: python render_A.py [post number ...]
Reads ../compte carte du visage/visuels/A{NN}_{k}.png (k=0 is the title illustration), writes ../compte carte du visage/10 posts/.
"""
import html, sys
from concurrent.futures import ThreadPoolExecutor

import nacria_ui as UI
import render_gh as R
from posts_A import POSTS

ROOT = R.HERE.parent / "compte carte du visage"
VIS = ROOT / "visuels"
OUT = ROOT / "10 posts"
e = html.escape
FACE = (.30, .36, .70)  # square crop of the face in the portraits, for the photo shown in the app
CTA_BULLETS = ["chaque peau a ses déclencheurs", "Nacria t'aide à trouver les tiens", "lien en bio ↓"]
CTA_MODE = "follow"  # until the account reaches 1,000 followers; "app" brings back the Nacria app CTA
ACCOUNT = "@acnee.solutions"
AVATAR = ROOT / "photo de profil" / "a1_carte.png"
FOLLOW_TITLE = "Tu veux enfin comprendre tes boutons ?"
FOLLOW_BULLETS = ["une zone du visage décodée chaque jour", "des causes concrètes, pas des mythes", "abonne-toi pour décoder ta peau"]
BENEFITS = [(300, "12 semaines", "un plan, étape par étape"), (505, "3 gestes", "pas 10 produits à la fois"),
            (710, "1 photo / semaine", "même lumière, vrai suivi")]


def crop_img(path, top=-382):
    return (f'<div style="position:absolute;left:40px;top:6px;width:1000px;height:990px;overflow:hidden" class="fade">'
            f'<img src="{path.as_uri()}" style="position:absolute;left:0;top:{top}px;width:1000px"></div>')


def title_page(title, path):
    return f'''<div style="position:absolute;left:90px;top:150px;width:900px;height:1190px;overflow:hidden" class="fade">
<img src="{path.as_uri()}" style="position:absolute;left:0;top:0;width:900px"></div>
<div style="position:absolute;left:80px;right:80px;top:110px;text-align:center">
<div class="handle">{e(R.HANDLE)}</div>
<div style="font-size:{70 if len(title) < 42 else 62}px;line-height:1.08;font-weight:800;letter-spacing:-1.5px;margin-top:10px">{e(title)}</div></div>'''


def zone_page(path, items):
    return crop_img(path) + f'<div class="handle" style="position:absolute;right:92px;top:1000px">{e(R.HANDLE)}</div>' + R.bullets(items, 1052)


def cta_follow(n):
    """Follow CTA: a reason to subscribe (daily, concrete, niche) + the TikTok "+" to tap, no app."""
    return (f'<div style="position:absolute;left:170px;top:300px;width:740px;height:700px;overflow:hidden" class="fade">'
            f'<img src="{(VIS / f"A{n:02d}_0.png").as_uri()}" style="position:absolute;left:0;top:-250px;width:740px"></div>'
            f'<div style="position:absolute;left:80px;right:80px;top:96px;text-align:center"><div class="handle">{e(ACCOUNT)}</div>'
            f'<div style="font-size:68px;line-height:1.08;font-weight:800;letter-spacing:-1.5px;margin-top:10px;text-wrap:balance">{e(FOLLOW_TITLE)}</div></div>'
            f'<div style="position:absolute;left:600px;top:820px">{UI.follow_badge(AVATAR.as_uri(), size=120)}</div>'
            + R.bullets(FOLLOW_BULLETS, 1052, green_last=True))


def cta_page(n, head, name):
    tmp = R.HERE / "_html_gh"
    tmp.mkdir(exist_ok=True)
    face = UI.face_crop(VIS / f"A{n:02d}_0.png", FACE, tmp / f"faceA{n:02d}.png")
    l1, l2 = head
    fs = min(70, int(1900 / max(len(l1), len(l2))))
    bens = "".join(f'<div style="position:absolute;left:556px;top:{y + 20}px;width:22px;height:22px;border-radius:50%;background:#8E4630;'
                   f'border:5px solid #dcc2a7"></div><div style="position:absolute;left:600px;top:{y}px;width:440px">'
                   f'<div style="font-family:Fraunces;font-weight:550;font-size:46px;line-height:1.05;color:#8E4630;letter-spacing:-.5px">{a}</div>'
                   f'<div style="font-size:31px;line-height:1.25;font-weight:700;margin-top:8px">{b}</div></div>' for y, a, b in BENEFITS)
    lis = "".join(f'<li class="{"green" if i == 2 else ""}">{e(t)}</li>' for i, t in enumerate(CTA_BULLETS))
    return (f'<div style="position:absolute;left:0;right:0;top:44px;text-align:center;font-family:Fraunces;font-weight:500;font-size:{fs}px;'
            f'line-height:1.05;letter-spacing:-1.5px;color:#2E2A33">{e(l1)}<br><em style="color:#8E4630">{e(l2)}</em></div>'
            + UI.phone(name, face, 46, 250, scale=.86, height=1300) + bens
            + f'<div class="handle" style="position:absolute;left:600px;top:930px">{e(R.HANDLE)}</div>'
            + f'<ul class="bul" style="left:600px;right:40px;top:975px;font-size:38px;line-height:1.25">{lis}</ul>')


def render_post(n):
    slug, _char, title, head, name, slides = POSTS[n - 1]
    d = OUT / f"A{n:02d}_{slug}"
    d.mkdir(parents=True, exist_ok=True)
    pages = ([title_page(title, VIS / f"A{n:02d}_0.png")]
             + [zone_page(VIS / f"A{n:02d}_{k}.png", causes) for k, (_p, causes) in enumerate(slides, 1)]
             + [cta_follow(n) if CTA_MODE == "follow" else cta_page(n, head, name)])
    for k, body in enumerate(pages, 1):
        R.render(body, d / f"slide_{k:02d}.png")
    return f"A{n:02d}_{slug} {len(pages)} slides"


if __name__ == "__main__":
    nums = [int(a) for a in sys.argv[1:]] or range(1, len(POSTS) + 1)
    with ThreadPoolExecutor(4) as ex:
        for line in ex.map(render_post, nums):
            print("ok", line, flush=True)
