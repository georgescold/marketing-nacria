"""Face-map carousels in the @glowhubdaily template (1080x1350, posted as-is on TikTok and Instagram)."""
import html, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).parent.resolve()
IMG = HERE.parent / "illustrations source"
OUT = pathlib.Path(r"C:/Users/loysc/Desktop/Marketing Nacre/Posts TikTok/3 posts carte du visage")
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
HANDLE = "nacria"
W, H = 1080, 1350
e = html.escape

CTA = ["la mauvaise routine aggrave l'acné", "trouve ce qui marche vraiment pour ta peau"]

POSTS = {
    "1_ce_que_tes_boutons_veulent_dire": {
        "title": "Ce que tes boutons veulent dire",
        "slides": [
            ("z_front.png", ["pas assez de sommeil", "mauvaise digestion", "mauvaise alimentation", "stress"]),
            ("z_nez2.png", ["mauvaise alimentation", "mauvaise digestion", "accumulation de sébum et de bactéries", "stress"]),
            ("z_bouche.png", ["aliments gras", "produits comédogènes", "mauvaise alimentation"]),
            ("z_menton.png", ["hormonal", "visage mal nettoyé", "stress"]),
            ("z_joues.png", ["téléphone", "taie d'oreiller sale", "produits capillaires"]),
            ("z_sourcils.png", ["manger trop ou pas assez", "mauvaise alimentation", "accumulation de bactéries"]),
        ],
    },
    "2_ce_que_tes_boutons_veulent_dire_pt2": {
        "title": "Ce que tes boutons veulent dire pt. 2",
        "slides": [
            ("z_glabelle.png", ["mauvaise alimentation", "stress ou anxiété", "accumulation de sébum et de sueur"]),
            ("z_cheveux.png", ["pores bouchés (par le shampoing)", "dormir avec les cheveux sales", "après-shampoing trop riche", "mauvaise alimentation"]),
            ("z_autour_nez.png", ["trop de produits laitiers", "produits comédogènes", "manque de sommeil"]),
            ("z_joues.png", ["téléphone", "taie d'oreiller sale", "trop de sucre"]),
            ("z_cote_menton.png", ["irritation due au dentifrice", "aliments gras", "déséquilibre intestinal"]),
            ("z_cou.png", ["mauvais drainage lymphatique", "fluctuations hormonales", "nettoyage insuffisant"]),
        ],
    },
    "3_ce_que_lemplacement_de_ton_acne_veut_dire": {
        "title": "Ce que l'emplacement de ton acné veut dire",
        "slides": [
            ("z_front.png", ["produits capillaires gras", "ta frange", "pas assez de sommeil"]),
            ("z_nez2.png", ["crème solaire trop épaisse", "patchs anti-points noirs", "y toucher toute la journée"]),
            ("z_joues.png", ["l'écran de ton téléphone", "taie d'oreiller sale", "pinceaux de maquillage"]),
            ("z_bouche.png", ["dentifrice blanchissant", "baume à lèvres gras", "poser ton menton sur ta main"]),
            ("z_menton.png", ["ton cycle menstruel", "trop de produits laitiers", "la sueur sous ton col"]),
        ],
    },
}

CSS = f'''
@font-face{{font-family:"DM Sans";src:url("{(HERE / 'fonts/DMSans.ttf').as_uri()}");font-weight:100 1000}}
@font-face{{font-family:"Fraunces";src:url("{(HERE / 'fonts/Fraunces.ttf').as_uri()}");font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{background:#dcc2a7;font-family:"DM Sans",sans-serif;color:#111;position:relative}}
.fade{{-webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 9%,#000 88%,transparent 100%),linear-gradient(to right,transparent 0,#000 7%,#000 93%,transparent 100%);-webkit-mask-composite:source-in;mask-composite:intersect}}
.handle{{color:#7c4a9e;font-weight:700;font-size:30px;letter-spacing:.2px}}
.bul{{position:absolute;left:92px;right:80px;list-style:none;font-size:44px;line-height:1.28;font-weight:700;letter-spacing:-.3px}}
.bul li::before{{content:"-  ";white-space:pre}}
.bul li.green{{color:#1f9d4c}}
'''


def crop_img(name):
    # face crop: drop the empty band above the head so the face fills the slide like the reference
    return f'<div style="position:absolute;left:40px;top:6px;width:1000px;height:990px;overflow:hidden" class="fade">' \
           f'<img src="{(IMG / name).as_uri()}" style="position:absolute;left:0;top:-382px;width:1000px"></div>'


def bullets(items, top, green_last=False):
    lis = "".join(f'<li class="{"green" if green_last and i == len(items) - 1 else ""}">{e(t)}</li>' for i, t in enumerate(items))
    return f'<ul class="bul" style="top:{top}px">{lis}</ul>'


def title_page(title):
    return f'''<div style="position:absolute;left:90px;top:150px;width:900px;height:1190px;overflow:hidden" class="fade">
<img src="{(IMG / 'base_nb.png').as_uri()}" style="position:absolute;left:0;top:0;width:900px"></div>
<div style="position:absolute;left:80px;right:80px;top:110px;text-align:center">
<div class="handle">{e(HANDLE)}</div>
<div style="font-size:70px;line-height:1.08;font-weight:800;letter-spacing:-1.5px;margin-top:10px">{e(title)}</div></div>'''


def zone_page(img, items):
    return crop_img(img) + f'<div class="handle" style="position:absolute;right:92px;top:1000px">{e(HANDLE)}</div>' + bullets(items, 1052)


def phone(inner, rot, left, top):
    return f'''<div style="position:absolute;left:{left}px;top:{top}px;width:400px;height:820px;transform:rotate({rot}deg);
border-radius:62px;background:#1b1b1d;padding:13px;box-shadow:0 30px 60px rgba(60,40,20,.35),0 0 0 2px #3a3a3e inset">
<div style="width:100%;height:100%;border-radius:50px;background:#fbf7f2;overflow:hidden;position:relative;font-family:'DM Sans';color:#2e2a33">
<div style="position:absolute;top:12px;left:50%;transform:translateX(-50%);width:118px;height:34px;border-radius:20px;background:#111"></div>
<div style="display:flex;justify-content:space-between;padding:20px 34px 0;font-size:17px;font-weight:700"><span>9:41</span><span>●●● ▮</span></div>
{inner}</div></div>'''


SCREENS = HERE / "app_screens"


def phone_shot(screen, rot, left, top, w=400):
    """Phone mockup showing a real Nacria screen (captured from the app prototype, design/wireframe)."""
    inner_w = w - 26
    inner_h = round(inner_w * 1471 / 771)
    return f'''<div style="position:absolute;left:{left}px;top:{top}px;width:{w}px;height:{inner_h + 26}px;transform:rotate({rot}deg);
border-radius:60px;background:#1b1b1d;padding:13px;box-shadow:0 30px 60px rgba(60,40,20,.35),0 0 0 2px #3a3a3e inset">
<div style="width:100%;height:100%;border-radius:48px;background:#faf7f2;overflow:hidden;position:relative">
<img src="{(SCREENS / (screen + '_screen.png')).as_uri()}" style="position:absolute;left:0;top:0;width:{inner_w}px;height:{inner_h}px">
<div style="position:absolute;left:{inner_w * .845:.0f}px;top:{inner_h * .07:.0f}px;width:{inner_w * .14:.0f}px;height:{inner_h * .03:.0f}px;background:#faf7f2"></div>
<div style="position:absolute;top:10px;left:50%;transform:translateX(-50%);width:{inner_w * .3:.0f}px;height:30px;border-radius:20px;background:#111"></div>
</div></div>'''


def screen_plan():
    steps = [("Nettoyant doux", True), ("Soin ciblé", True), ("Crème hydratante", False)]
    rows = "".join(f'''<div style="display:flex;align-items:center;gap:14px;padding:13px 0;border-top:1px solid #eee3d8">
<div style="width:30px;height:30px;border-radius:50%;{'background:#8a4f6d;color:#fff' if done else 'border:2px solid #c9b6a6'};display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:800">{'✓' if done else ''}</div>
<div style="font-size:21px;font-weight:600">{e(t)}</div></div>''' for t, done in steps)
    return f'''<div style="padding:34px 30px 0">
<div style="font-family:Fraunces;font-size:34px;font-weight:600">Ton plan</div>
<div style="font-size:18px;color:#7a6f78;margin-top:4px">Semaine 3 sur 12</div>
<div style="height:10px;border-radius:10px;background:#eee3d8;margin-top:12px"><div style="width:25%;height:100%;border-radius:10px;background:#8a4f6d"></div></div>
<div style="margin-top:26px;background:#fff;border-radius:22px;padding:18px 20px;box-shadow:0 2px 10px rgba(0,0,0,.05)">
<div style="font-size:16px;font-weight:800;letter-spacing:1px;color:#8a4f6d">CE SOIR</div>{rows}</div>
<div style="margin-top:18px;background:#fff;border-radius:22px;padding:18px 20px;box-shadow:0 2px 10px rgba(0,0,0,.05)">
<div style="font-size:16px;font-weight:800;letter-spacing:1px;color:#8a4f6d">CE MATIN</div>
<div style="font-size:20px;font-weight:600;margin-top:8px">Nettoyant · Hydratant · SPF</div></div>
<div style="margin-top:18px;background:#f3e9f0;border-radius:22px;padding:16px 20px;font-size:19px;font-weight:700">📸 Point peau dimanche</div></div>'''


def screen_point():
    face = (IMG / "z_menton.png").as_uri()
    return f'''<div style="padding:34px 30px 0">
<div style="font-family:Fraunces;font-size:34px;font-weight:600">Point peau</div>
<div style="font-size:18px;color:#7a6f78;margin-top:4px">Semaine 3 · même lumière ✓</div>
<div style="margin-top:20px;height:380px;border-radius:26px;overflow:hidden;position:relative;background:#e9dccd">
<img src="{face}" style="position:absolute;width:560px;left:-102px;top:-210px">
<div style="position:absolute;left:50%;top:53%;transform:translate(-50%,-50%);width:205px;height:270px;border:3px dashed rgba(255,255,255,.85);border-radius:50%"></div></div>
<div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:18px">
<span style="background:#fff;border-radius:999px;padding:9px 16px;font-size:17px;font-weight:700">Règles : jour 2</span>
<span style="background:#fff;border-radius:999px;padding:9px 16px;font-size:17px;font-weight:700">Routine suivie 6/7</span></div>
<div style="margin-top:20px;background:#2e2a33;color:#fbf7f2;border-radius:999px;padding:16px;text-align:center;font-size:20px;font-weight:800">Enregistrer</div></div>'''


def cta_page():
    return (phone_shot("today", -7, 95, 110) + phone_shot("routine", 6, 565, 140)
            + f'<div class="handle" style="position:absolute;right:92px;top:1000px">{e(HANDLE)}</div>'
            + bullets(CTA + ["lien en bio ↓"], 1052, green_last=True))


def render(body, path):
    tmp = HERE / "_html_gh"
    tmp.mkdir(exist_ok=True)
    h = tmp / (path.parent.name + "_" + path.stem + ".html")
    h.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>', encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={W},{H}", f"--screenshot={path}", "--virtual-time-budget=3000", h.as_uri()],
                   check=True, capture_output=True, timeout=120)


def main(only=None):
    for key, post in POSTS.items():
        if only and key != only:
            continue
        d = OUT / key
        d.mkdir(parents=True, exist_ok=True)
        pages = [title_page(post["title"])] + [zone_page(i, b) for i, b in post["slides"]] + [cta_page()]
        for n, body in enumerate(pages, 1):
            render(body, d / f"slide_{n:02d}.png")
        print("ok", key, len(pages))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
