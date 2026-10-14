import html, os, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).parent.resolve()
IMG = HERE.parent / "illustrations source"
OUT = pathlib.Path(r"C:/Users/loysc/Desktop/Marketing Nacre/Posts TikTok/3 premiers posts")
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
e = html.escape

FORMATS = {
    # name: (W, H, art_width, art_top, text_top, text_bottom)
    "tiktok_1080x1920": (1080, 1920, 1080, 440, 190, 930),
    "instagram_1080x1350": (1080, 1350, 1000, 60, 70, 520),
}


def title_slide(img, title, sub=None):
    return dict(img=img, kind="title", title=title, sub=sub)


def zone_slide(img, zone, said, label, bullets):
    return dict(img=img, kind="zone", zone=zone, said=said, label=label, bullets=bullets)


def quote_slide(img, quote, fact):
    return dict(img=img, kind="quote", quote=quote, fact=fact)


def tip_slide(img, head, body):
    return dict(img=img, kind="tip", head=head, body=body)


def end_slide(img, head, lines, small=None, cta=None, ask=None):
    return dict(img=img, kind="end", head=head, lines=lines, small=small, cta=cta, ask=ask)


def stat_slide(img, head, big, body, source):
    return dict(img=img, kind="stat", head=head, big=big, body=body, source=source)


POSTS = {
    "post1_carte_du_visage": [
        title_slide("base_nb.png", "Ce que tes boutons veulent dire", "(spoiler : ton nez ne parle pas de ton cœur)"),
        zone_slide("z_front.png", "Le front", "le foie, la digestion", "À vérifier d'abord",
                   ["tes produits capillaires (huiles, laque, shampoing sec)", "frange, casquette, bandeau", "la transpiration après le sport"]),
        zone_slide("z_nez2.png", "Le nez", "le cœur", "En vrai",
                   ["une des zones les plus riches en sébum", "points noirs et pores visibles y sont fréquents", "aucun lien prouvé avec le cœur"]),
        zone_slide("z_joues.png", "Les joues", "les poumons", "À vérifier d'abord",
                   ["le téléphone contre la joue", "la taie d'oreiller", "les mains sur le visage"]),
        zone_slide("z_bouche.png", "Autour de la bouche", "l'estomac", "À vérifier d'abord",
                   ["un baume à lèvres très gras", "un dentifrice qui irrite", "petits boutons serrés : pas toujours de l'acné, demande l'avis d'un pro"]),
        zone_slide("z_menton.png", "Menton et mâchoire", "« c'est hormonal »", "En partie vrai",
                   ["c'est fréquent chez la femme adulte", "beaucoup voient des poussées avant les règles", "mais la zone seule ne suffit pas à conclure"]),
        stat_slide("z_multi.png", "Et si c'est partout ?", "9 sur 10",
                   "des femmes adultes ont des boutons sur plusieurs zones à la fois. C'est le cas le plus courant.",
                   "Dréno et al., JEADV, 2015"),
        end_slide("p3_s9.png", "Ce qui aide vraiment",
                  ["Une routine simple, la même pendant 12 semaines", "Une photo par semaine, même lumière", "Noter ce qui change : produit, règles, stress"],
                  small="Boutons douloureux, profonds ou qui marquent : va voir un dermato. Repères généraux, pas un diagnostic.",
                  cta="Le suivi semaine par semaine : Nacre, lien en bio"),
    ],
    "post2_conseils_quon_recoit": [
        title_slide("p2_s1.png", "Tous les conseils qu'on reçoit quand on a des boutons à 28 ans 🙃"),
        quote_slide("p2_s2.png", "Bois plus d'eau.", "Boire, c'est bien. Mais aucune étude n'a montré que ça fait partir l'acné."),
        quote_slide("p2_s3.png", "Lave-toi plus souvent le visage.", "2 fois par jour suffit. Frotter et décaper irrite, et ça peut empirer."),
        quote_slide("p2_s4.png", "C'est l'âge, ça va passer.", "Environ 4 acnés de la femme adulte sur 10 commencent après 25 ans."),
        quote_slide("p2_s5.png", "Arrête le chocolat.", "Les preuves sont faibles. Les pistes plus solides : sucres rapides et produits laitiers, et ça varie selon les personnes."),
        quote_slide("p2_s6.png", "Mets du dentifrice dessus.", "Ça dessèche et ça irrite. Un patch fait mieux le travail."),
        quote_slide("p2_s7.png", "Essaie ce sérum, il a tout changé pour moi.", "Changer chaque semaine, c'est ne jamais savoir ce qui marche. Un soin se juge souvent sur 6 à 12 semaines."),
        end_slide("p3_s9.png", "Le seul conseil qui aide vraiment",
                  ["Garder UNE routine assez longtemps pour voir ce qui marche."],
                  ask="Et toi, c'est quoi le pire conseil qu'on t'a donné ? 👇",
                  cta="Routine pharmacie + un point par semaine : Nacre, lien en bio"),
    ],
    "post3_7_habitudes": [
        title_slide("z_multi.png", "7 habitudes qui entretiennent tes boutons", "(sans que tu le saches)"),
        tip_slide("p3_s2.png", "1. Le téléphone contre ta joue", "Contact et frottement à chaque appel. Nettoie l'écran, passe aux écouteurs."),
        tip_slide("p3_s3.png", "2. Ta taie d'oreiller", "Sébum, cheveux, produits : change-la 2 fois par semaine."),
        tip_slide("p3_s4.png", "3. Toucher et percer", "Un bouton percé peut laisser une marque qui dure bien plus longtemps que lui."),
        tip_slide("p3_s5.png", "4. Dormir maquillée", "Même les soirs de flemme : démaquillage doux, puis ta routine."),
        tip_slide("p3_s6.png", "5. Trop de produits en même temps", "Plus tu en mets, plus tu risques d'irriter. Et impossible de savoir lequel marche."),
        tip_slide("p3_s7.png", "6. Tes produits capillaires", "Huiles, laque, shampoing sec : ils finissent sur le front et la mâchoire."),
        tip_slide("p3_s8.png", "7. Changer de routine chaque semaine", "Un soin se juge souvent sur 6 à 12 semaines. Avant, tu ne sais rien."),
        end_slide("p3_s9.png", "Le plan simple",
                  ["Une seule routine, sans en changer", "Une photo par semaine, même lumière", "Tu notes ce que tu changes"],
                  cta="C'est exactement ce que fait Nacre : lien en bio",
                  ask="Enregistre pour plus tard 📌"),
    ],
}


def block(s, ig):
    k = s["kind"]
    if k == "title":
        sub = f'<p class="sub">{e(s["sub"])}</p>' if s.get("sub") else ""
        return f'<h1 class="big">{e(s["title"])}</h1>{sub}'
    if k == "zone":
        lis = "".join(f"<li>{e(b)}</li>" for b in s["bullets"])
        return (f'<h2>{e(s["zone"])}</h2><p class="said"><span class="x">✕</span> On dit : {e(s["said"])}</p>'
                f'<p class="label"><span class="ok">✓</span> {e(s["label"])} :</p><ul>{lis}</ul>')
    if k == "quote":
        return f'<p class="quote">« {e(s["quote"])} »</p><p class="fact">{e(s["fact"])}</p>'
    if k == "tip":
        return f'<h2>{e(s["head"])}</h2><p class="fact">{e(s["body"])}</p>'
    if k == "stat":
        return (f'<h2>{e(s["head"])}</h2><p class="stat">{e(s["big"])}</p><p class="fact">{e(s["body"])}</p>'
                f'<p class="source">Source : {e(s["source"])}</p>')
    if k == "end":
        lis = "".join(f"<li>{e(l)}</li>" for l in s["lines"])
        tag = "ol" if len(s["lines"]) > 1 else "div"
        lines = f'<{tag} class="lines">{lis if tag == "ol" else e(s["lines"][0])}</{tag}>'
        ask = f'<p class="ask">{e(s["ask"])}</p>' if s.get("ask") else ""
        small = f'<p class="small">{e(s["small"])}</p>' if s.get("small") else ""
        cta = f'<p class="cta">{e(s["cta"])}</p>' if s.get("cta") else ""
        return f'<h2>{e(s["head"])}</h2>{lines}{ask}{cta}{small}'
    raise ValueError(k)


def page(s, fmt):
    W, H, aw, at, tt, tb = FORMATS[fmt]
    ig = fmt.startswith("instagram")
    scale = 0.8 if ig else 1.12
    art = (IMG / s["img"]).as_uri()
    font_dm = (HERE / "fonts/DMSans.ttf").as_uri()
    font_fr = (HERE / "fonts/Fraunces.ttf").as_uri()
    left = (W - aw) // 2
    label_top = H - 60 if ig else 885
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:"DM Sans";src:url("{font_dm}");font-weight:100 1000}}
@font-face{{font-family:"Fraunces";src:url("{font_fr}");font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{background:radial-gradient(ellipse 70% 55% at 50% 55%,#ead6c0 0%,#dfc6ac 60%,#d8bc9f 100%);font-family:"DM Sans",sans-serif;color:#2a221d;position:relative}}
.art{{position:absolute;left:{left}px;top:{at}px;width:{aw}px;
 -webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 14%,#000 100%),linear-gradient(to right,transparent 0,#000 6%,#000 94%,transparent 100%);
 -webkit-mask-composite:source-in;mask-composite:intersect}}
.text{{position:absolute;left:{int(70*scale)+10}px;right:{int(70*scale)+10}px;top:{tt}px;height:{tb-tt}px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:{int(18*scale)}px}}
.big{{font-size:{int(92*scale)}px;line-height:1.05;font-weight:800;letter-spacing:-1.5px}}
.sub{{font-family:"Fraunces",serif;font-style:italic;font-size:{int(46*scale)}px;font-weight:500;color:#5b4637}}
h2{{font-size:{int(74*scale)}px;line-height:1.05;font-weight:800;letter-spacing:-1px}}
.said{{font-size:{int(40*scale)}px;font-weight:600;color:#7a5c4c;text-decoration:line-through;text-decoration-thickness:3px;text-decoration-color:rgba(160,60,60,.7)}}
.said .x{{color:#b23b3b;text-decoration:none;display:inline-block;margin-right:6px}}
.label{{font-size:{int(42*scale)}px;font-weight:800;color:#2a221d}}.ok{{color:#3e7d56;margin-right:6px}}
ul{{list-style:none;font-size:{int(42*scale)}px;line-height:1.25;font-weight:600;display:flex;flex-direction:column;gap:{int(10*scale)}px}}
ul li::before{{content:"– "}}
.quote{{font-family:"Fraunces",serif;font-size:{int(82*scale)}px;line-height:1.08;font-weight:700;font-style:italic}}
.fact{{font-size:{int(46*scale)}px;line-height:1.25;font-weight:600;color:#3a2e27;max-width:{int(900*scale)+60}px}}
.stat{{font-family:"Fraunces",serif;font-size:{int(170*scale)}px;line-height:.95;font-weight:800;color:#8a4f6d}}
.source{{font-size:{int(28*scale)}px;color:#6b5546;font-weight:500}}
.lines{{font-size:{int(46*scale)}px;line-height:1.25;font-weight:700;text-align:left;padding-left:{int(56*scale)}px;display:flex;flex-direction:column;gap:{int(10*scale)}px}}
div.lines{{text-align:center;padding:0}}
.ask{{font-size:{int(44*scale)}px;font-weight:800;color:#8a4f6d}}
.cta{{font-size:{int(38*scale)}px;font-weight:700;background:#2a221d;color:#fbf7f2;padding:{int(14*scale)}px {int(26*scale)}px;border-radius:999px}}
.small{{font-size:{int(28*scale)}px;font-weight:500;color:#5b4637;max-width:{int(880*scale)+60}px}}
.label-ai{{position:absolute;left:{int(40*scale)+8}px;top:{label_top}px;font-size:{int(24*scale)+4}px;font-weight:600;color:rgba(42,34,29,.75);background:rgba(251,247,242,.55);padding:4px 12px;border-radius:999px}}
</style></head><body>
<img class="art" src="{art}">
<div class="text">{block(s, ig)}</div>
</body></html>'''


def main(only=None):
    tmp = HERE / "_html"
    tmp.mkdir(exist_ok=True)
    for post, slides in POSTS.items():
        if only and post != only:
            continue
        for fmt, (W, H, *_rest) in FORMATS.items():
            d = OUT / post / fmt
            d.mkdir(parents=True, exist_ok=True)
            for i, s in enumerate(slides, 1):
                h = tmp / f"{post}_{fmt}_{i:02d}.html"
                h.write_text(page(s, fmt), encoding="utf-8")
                png = d / f"slide_{i:02d}.png"
                subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                                f"--window-size={W},{H}", f"--screenshot={png}", "--virtual-time-budget=3000", h.as_uri()],
                               check=True, capture_output=True, timeout=120)
            print("ok", post, fmt, len(slides))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
