"""Build the nutrition account's season plan page (HTML, images embedded) from plan_nutrition.py and the demo covers.

Usage: python page_plan_nutrition.py   -> ../../compte nutrition/vidéo/Plan saison 1.html
"""
import base64, html, io, pathlib

from PIL import Image, ImageDraw

import miniatures_nutrition as mz
from plan_nutrition import CHAPTERS, VERDICTS

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent / "compte nutrition" / "vidéo"
MINI = ROOT / "miniatures"
OUT = ROOT / "Plan saison 1.html"


def uri(im, size, fmt="JPEG"):
    im = im.convert("RGB")
    im.thumbnail(size, Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, fmt, quality=82)
    return f"data:image/{fmt.lower()};base64," + base64.b64encode(buf.getvalue()).decode()


e = html.escape

covers = [(c, k, uri(Image.open(MINI / "covers" / f"C{c['n']}_{k:02d}.jpg").crop((0, 240, 1080, 1680)), (360, 480)))
          for c in CHAPTERS for k in range(1, 9) if (MINI / "covers" / f"C{c['n']}_{k:02d}.jpg").exists()]
cover_html = "\n".join(
    f'<figure class="cover"><img src="{u}" alt="Miniature : {e(c["name"])}, partie {k}, {e(c["eps"][k - 1][0])}" '
    f'loading="lazy"></figure>' for c, k, u in covers)

# the verdict moment of a video, mocked from the first hero: the food, the closing line, the evidence stamp
frame_uri = ""
h1 = mz.hero_path(CHAPTERS[0], 1)
if h1.exists():
    fr = mz.background(CHAPTERS[0]["tint"])
    hi = Image.open(h1).convert("RGB").resize((900, 900), Image.LANCZOS)
    m = Image.new("L", (900, 900), 0)
    ImageDraw.Draw(m).ellipse((90, 90, 810, 810), fill=255)
    from PIL import ImageFilter
    fr.paste(hi, (90, 360), m.filter(ImageFilter.GaussianBlur(70)))
    st = mz.verdict_stamp("PROBABLE", 130)
    fr.paste(st, ((1080 - st.width) // 2, 1080), st)
    d = ImageDraw.Draw(fr)
    f = mz.dmsans(44, 700)
    for k, ln in enumerate(["Ce n'est pas un poison.", "C'est un facteur parmi d'autres."]):
        d.text(((1080 - d.textlength(ln, font=f)) / 2, 1500 + k * 58), ln, font=f, fill=mz.CREAM)
    frame_uri = uri(fr, (420, 746))
stamps_html = "".join(f'<img src="{uri(mz.verdict_stamp(v, 110).convert("RGBA"), (260, 160), "PNG")}" alt="Tampon {e(v)}">'
                      for v in VERDICTS)
persona_html = "".join(f'<figure><img src="{uri(Image.open(p), (300, 300))}" alt="Portrait de Margot, version {i}">'
                       f'<figcaption>Version {i}</figcaption></figure>'
                       for i, p in enumerate(sorted(mz.PERSONA_OUT.glob("margot_*.png")), 1))

chapters_html = []
for c in CHAPTERS:
    eps = "\n".join(f'''
      <li class="ep">
        <p class="ep-head"><span class="ep-n">Partie {k}</span> <span class="ep-title">{e(t)}</span>
          <span class="verdict" style="--v:{VERDICTS[v]}">{e(v)}</span></p>
        <p class="ep-hook">{e(hook)}</p>
        <p class="ep-what">{e(what)}</p>
        <p class="ep-end"><span>Chute</span> {e(end)}</p>
      </li>''' for k, (t, hook, what, end, _o, v) in enumerate(c["eps"], 1))
    chapters_html.append(f'''
  <section class="chapter" style="--tint:{c['tint']}" id="chapitre-{c['n']}">
    <header class="ch-head">
      <span class="ch-chip" aria-hidden="true"></span>
      <div>
        <p class="eyebrow">Chapitre {c['n']} · vidéos {(c['n'] - 1) * 8 + 1} à {c['n'] * 8}</p>
        <h3>{e(c['name'])}</h3>
        <p class="ch-why">{e(c['why'])}</p>
      </div>
    </header>
    <ol class="eps">{eps}
    </ol>
  </section>''')

PAGE = f'''<title>Saison 1 du compte Nutrition</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400..800&family=Fraunces:opsz,wght,SOFT,WONK@9..144,400..900,0..100,0..1&display=swap">
<style>
/* Layout: one reading column like a lab notebook; covers break out into a profile-grid band. Dark first, like the videos. */
:root {{
  --bg: #0a120e; --surface: #12201a; --ink: #faf4e8; --muted: #a9b5ac; --line: #22352b;
  --mint: #8ff0c0; --tomato: #ff5a3c;
  --display: "Fraunces", Georgia, "Times New Roman", serif;
  --sans: "DM Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  color-scheme: dark;
}}
@media (prefers-color-scheme: light) {{
  :root:not([data-theme="dark"]) {{
    --bg: #faf6ee; --surface: #f0eadc; --ink: #12201a; --muted: #56645b; --line: #ddd5c4;
    --mint: #1f8a5a; --tomato: #c8381e; color-scheme: light;
  }}
}}
:root[data-theme="light"] {{
  --bg: #faf6ee; --surface: #f0eadc; --ink: #12201a; --muted: #56645b; --line: #ddd5c4;
  --mint: #1f8a5a; --tomato: #c8381e; color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ background: var(--bg); color: var(--ink); font: 400 1.0625rem/1.6 var(--sans); }}
.wrap {{ max-width: 68rem; margin: 0 auto; padding-inline: max(16px, 4vw); padding-block: 3rem 5rem; }}
.col {{ max-width: 44rem; }}
h1, h2, h3 {{ font-family: var(--display); font-variation-settings: "SOFT" 0, "WONK" 1; font-weight: 800; text-wrap: balance; margin: 0; }}
h1 {{ font-size: clamp(2.2rem, 5vw, 3.4rem); line-height: 1.04; font-weight: 900; }}
h2 {{ font-size: clamp(1.5rem, 3.2vw, 2.1rem); line-height: 1.15; margin-bottom: 1rem; }}
h3 {{ font-size: 1.45rem; line-height: 1.2; }}
p {{ margin: 0 0 1rem; }}
.eyebrow {{ font: 700 0.75rem/1.4 var(--sans); letter-spacing: 0.14em; text-transform: uppercase; color: var(--muted); margin: 0 0 0.4rem; }}
.lede {{ font-size: 1.2rem; color: var(--muted); max-width: 40rem; margin-top: 1rem; }}
section.block {{ margin-top: 4.5rem; display: grid; gap: 1.25rem; }}
.brief {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr)); gap: 1rem; margin-top: 2rem; }}
.brief div {{ border-top: 2px solid var(--line); padding-top: 0.8rem; min-width: 0; }}
.brief strong {{ display: block; font-family: var(--display); font-weight: 800; font-size: 1.15rem; margin-bottom: 0.2rem; }}
.brief span {{ color: var(--muted); font-size: 0.95rem; }}
.rules {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(17rem, 1fr)); gap: 1.5rem 2rem; }}
.rules > div {{ min-width: 0; }}
.rules h4 {{ font: 700 1rem/1.4 var(--sans); margin: 0 0 0.35rem; }}
.rules p {{ color: var(--muted); font-size: 0.97rem; }}
q {{ font-style: italic; }}
.duo {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr)); gap: 1.5rem; align-items: start; }}
.duo > * {{ min-width: 0; }}
.mock img {{ width: 100%; max-width: 20rem; border-radius: 8px; aspect-ratio: 9 / 16; object-fit: cover; display: block; }}
.stamps {{ display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center; }}
.stamps img {{ height: 5.5rem; width: auto; max-width: 100%; }}
.persona {{ display: flex; flex-wrap: wrap; gap: 1rem; }}
.persona figure {{ margin: 0; }}
.persona img {{ width: 11rem; max-width: 100%; aspect-ratio: 1; border-radius: 50%; object-fit: cover; display: block; }}
.persona figcaption {{ text-align: center; font-size: 0.85rem; color: var(--muted); margin-top: 0.3rem; }}
.covers {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(9.5rem, 1fr)); gap: 3px; }}
.cover {{ margin: 0; }}
.cover img {{ width: 100%; max-width: 100%; aspect-ratio: 3 / 4; object-fit: cover; display: block; }}
.note {{ font-size: 0.92rem; color: var(--muted); }}
.chapter {{ margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--line); }}
.ch-head {{ display: flex; gap: 1rem; align-items: flex-start; margin-bottom: 1.25rem; }}
.ch-chip {{ flex: none; width: 2.6rem; height: 2.6rem; border-radius: 50%; margin-top: 0.3rem;
  background: radial-gradient(circle at 40% 35%, var(--tint), #12201a 75%); box-shadow: 0 0 0 1px var(--line); }}
.ch-why {{ color: var(--muted); margin: 0.3rem 0 0; max-width: 42rem; }}
.eps {{ list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(19rem, 1fr)); gap: 1.6rem 2.2rem; }}
.ep {{ min-width: 0; border-left: 2px solid var(--tint); padding-left: 0.9rem; }}
.ep p {{ margin: 0 0 0.3rem; }}
.ep-head {{ display: flex; gap: 0.5rem; align-items: baseline; flex-wrap: wrap; }}
.ep-n {{ font: 700 0.72rem/1 var(--sans); letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); }}
.ep-title {{ font-family: var(--display); font-variation-settings: "SOFT" 0, "WONK" 1; font-size: 1.2rem; font-weight: 800; }}
.verdict {{ font: 800 0.66rem/1 var(--sans); letter-spacing: 0.1em; color: var(--v); border: 1.5px solid var(--v); border-radius: 4px; padding: 0.2rem 0.35rem; }}
.ep-hook {{ font-weight: 600; }}
.ep-what {{ color: var(--muted); font-size: 0.93rem; }}
.ep-end {{ font-size: 0.93rem; }}
.ep-end span {{ font: 700 0.7rem var(--sans); letter-spacing: 0.1em; text-transform: uppercase; color: var(--mint); margin-right: 0.3rem; }}
.tablewrap {{ overflow-x: auto; border: 1px solid var(--line); border-radius: 8px; }}
table {{ border-collapse: collapse; width: 100%; font-size: 0.95rem; min-width: 34rem; }}
th, td {{ text-align: left; padding: 0.6rem 0.8rem; border-bottom: 1px solid var(--line); vertical-align: top; }}
th {{ font: 700 0.72rem/1.3 var(--sans); letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); }}
td.num, th.num {{ text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }}
tr.total td {{ font-weight: 700; border-bottom: 0; }}
.steps {{ padding-left: 1.2rem; margin: 0; display: grid; gap: 0.6rem; }}
a {{ color: var(--mint); }}
:focus-visible {{ outline: 2px solid var(--mint); outline-offset: 2px; }}
</style>

<main class="wrap">
  <header class="col">
    <p class="eyebrow">Compte Nutrition · format « expliqué en 60 secondes »</p>
    <h1>Ce que tu manges, ta peau le montre. Ou pas.</h1>
    <p class="lede">Saison 1 : 6 chapitres, 48 vidéos. Un aliment, une enquête, un verdict tamponné avec son niveau de preuve. Incarné par Margot, un personnage qui parle comme une nutritionniste, sans jamais te dire de te priver.</p>
  </header>

  <div class="brief">
    <div><strong>Une place libre</strong><span>En France, personne ne tient « alimentation et acné adulte ». Les gros comptes nutrition ne parlent pas de peau.</span></div>
    <div><strong>Le verdict tamponné</strong><span>Prouvé, probable, pas prouvé, faux. Personne ne le fait en français, et c'est ce qui fait commenter.</span></div>
    <div><strong>Zéro culpabilité</strong><span>Elle « n'en peut plus de faire gaffe à tout ce qu'elle mange ». Le compte ne prône jamais la restriction.</span></div>
    <div><strong>Même pipeline</strong><span>Voix, musique d'enquête, CTA qui monte, environ 1 à 1,30 $ la vidéo.</span></div>
  </div>

  <section class="block">
    <div class="col">
      <p class="eyebrow">Ce qui marche déjà</p>
      <h2>Ce qu'on a relevé avant de dessiner le compte</h2>
      <p>Les formats viraux du sujet sont connus : un aliment et un verdict, une comparaison A contre B, le démontage d'une tendance, et le ton qui déculpabilise (« life is too short to worry about my skin », 262 000 J'aime). Le code visuel de référence est celui de Glucose Goddess (6,3 M d'abonnés) : une courbe, un aliment détouré, un « ? » qui laisse la question ouverte. Les comptes sans visage faits à l'IA sont ceux qu'on enregistre et partage le plus.</p>
      <p>Mais une bonne part des accroches virales sont fausses : « cortisol face » (157 000 J'aime), tisane de menthe verte, carte du visage. Le fil rouge du compte est une vraie étude française : NutriNet-Santé, 24 452 adultes, où le gras-sucré, les boissons sucrées et le lait sont associés à plus d'acné. Les détails et les sources sont dans les deux rapports de recherche.</p>
    </div>
  </section>

  <section class="block">
    <div class="col">
      <p class="eyebrow">Le personnage</p>
      <h2>Margot, la voix du compte</h2>
      <p>Elle dit « je », elle a ses phrases à elle (« on regarde ce que disent les études »), elle déculpabilise avant d'expliquer. Elle est animée, pas photoréaliste : personne ne peut la prendre pour une vraie soignante. Sa voix est Vindemiatrix, celle que tu avais classée en premier, posée et chaleureuse, et différente de Despina sur les deux autres comptes.</p>
    </div>
    <div class="persona">{persona_html}</div>
    <div class="rules">
      <div><h4>Ce qu'elle peut dire</h4><p>Parler de nutrition, citer les études, donner un niveau de preuve, renvoyer vers un médecin. « Nutritionniste » n'est pas un titre protégé, mais il évoque un médecin : le compte ne l'affiche pas comme un diplôme.</p></div>
      <div><h4>Ce qu'elle ne fera jamais</h4><p>Se dire diététicienne (titre protégé : un an de prison et 15 000 € d'amende en cas d'usurpation), porter une blouse ou un stéthoscope, se faire appeler « Dr », raconter un faux témoignage personnel.</p></div>
      <div><h4>Les mentions obligatoires</h4><p>Le label IA de TikTok et d'Instagram sur chaque vidéo. En bio : « Personnage IA · contenus sourcés ». Idéalement, une relecture par une diététicienne réelle et nommée, qui rend le compte inattaquable.</p></div>
    </div>
  </section>

  <section class="block">
    <div class="col">
      <p class="eyebrow">Direction artistique « food noir et verdict »</p>
      <h2>De la vraie nourriture, filmée comme une pièce à conviction</h2>
    </div>
    <div class="duo">
      <div class="rules" style="grid-template-columns:1fr">
        <div><h4>La nourriture en héroïne</h4><p>Photographie culinaire hyperréaliste sur un fond vert forêt presque noir, une seule lumière de côté, des textures qui brillent (sucre, lait, chocolat). Les mouvements sont ceux d'une pub de luxe au ralenti : le lait qui éclabousse, le sucre qui tombe. Les deux autres comptes sont en argile et en hologramme : sur ta grille, les trois ne se confondent pas.</p></div>
        <div><h4>Le tampon de verdict</h4><p>Sur la chute de chaque vidéo, le tampon tombe avec un impact sonore : prouvé, probable, pas prouvé, faux. C'est la signature du compte. Il est animé en code, donc gratuit.</p></div>
        <div><h4>Une couleur par chapitre</h4><p>La lumière de bord change par chapitre : tomate, agrume, rose, lavande, bleu glacé, basilic. Elle se retrouve dans la miniature, comme sur les deux autres comptes.</p></div>
        <div><h4>Typographie</h4><p><b>Fraunces Black</b> pour les titres, la police d'un magazine culinaire. <b>DM Sans</b> en gras pour les sous-titres, avec les mots-clés en vert menthe.</p></div>
      </div>
      <div class="mock">
        {f'<img src="{frame_uri}" alt="Exemple de fin de vidéo : un verre de lait, la chute et le tampon PROBABLE">' if frame_uri else ''}
        <p class="note">La fin d'une vidéo : la chute, puis le tampon. Ici « Le lait », verdict probable.</p>
      </div>
    </div>
    <div class="stamps">{stamps_html}</div>
  </section>

  <section class="block">
    <div class="col">
      <p class="eyebrow">Miniatures</p>
      <h2>La grammaire du compte modèle, plus un tampon « ACCUSÉ »</h2>
      <p>Même structure que les deux autres comptes : le titre de série en capitales, la pastille « PARTIE N », l'aliment, le sujet en énorme, et dessous l'accusation ou le chiffre qui fait peur (« +12 % de risque d'acné par verre »). Le tampon rouge « ACCUSÉ » dit tout de suite que l'aliment est sur le banc des accusés.</p>
    </div>
    <div class="covers">
{cover_html}
    </div>
    <p class="note">Les 8 miniatures du chapitre 1, puis la partie 1 des chapitres 2 à 6, recadrées comme sur un profil.</p>
  </section>

  <section class="block" id="plan">
    <div class="col">
      <p class="eyebrow">Plan des 48 vidéos</p>
      <h2>Des aliments accusés jusqu'à « manger sans te priver »</h2>
      <p>On commence par les croyances n°1 des commentaires (lait, sucre, gluten). On passe ensuite aux boissons, aux tendances et aux compléments, puis à la mécanique de la glycémie. La saison se referme sur le désir profond de l'avatar : ne plus y penser, ne rien s'interdire. Chaque verdict vient du rapport de preuves ; les études d'observation sont dites « associées à », jamais « causent ».</p>
    </div>
{"".join(chapters_html)}
  </section>

  <section class="block">
    <div class="col">
      <p class="eyebrow">Décisions</p>
      <h2>Ce qui est tranché, ce qui reste ouvert</h2>
      <ol class="steps">
        <li><b>Le compte s'appelle « Ta peau dans l'assiette »</b>, avec le portrait 1 de Margot en photo de profil.</li>
        <li><b>Chapitre 1 renommé « Les aliments qui donnent des boutons »</b> après ton retour sur la partie 1 : un nom qui dit littéralement de quoi on parle, et ce qu'elle tape dans la recherche.</li>
        <li><b>Chaque script suit une enquête à rebondissements</b> : chiffre choc dans les 3 premières secondes, relance, retournement, « Pas si vite », contre-retournement, verdict.</li>
        <li><b>Encore ouvert</b> : une relecture par une diététicienne réelle et nommée.</li>
      </ol>
    </div>
  </section>
</main>
'''

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(PAGE, encoding="utf-8")
print(OUT, f"{len(PAGE) / 1024:.0f} KB", len(covers), "covers")
