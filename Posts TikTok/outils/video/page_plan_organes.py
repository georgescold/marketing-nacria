"""Build the organs account's season plan page (HTML, images embedded) from plan_organes.py and its demo covers.

Usage: python page_plan_organes.py   -> ../../compte organes/vidéo/Plan saison 1.html
"""
import base64, html, io, pathlib

from PIL import Image

from plan_organes import CHAPTERS

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent / "compte organes" / "vidéo"
MINI = ROOT / "miniatures"
OUT = ROOT / "Plan saison 1.html"


def uri(path, size):
    im = Image.open(path).convert("RGB")
    im.thumbnail(size, Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=82)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


e = html.escape

covers = []
for c in CHAPTERS:
    for k in range(1, 9):
        p = MINI / "covers" / f"C{c['n']}_{k:02d}.jpg"
        if p.exists():  # the grid crop: central 3:4 of the 9:16 cover
            im = Image.open(p).convert("RGB").crop((0, 240, 1080, 1680))
            tmp = MINI / "_crop.jpg"
            im.save(tmp, quality=90)
            covers.append((c, k, uri(tmp, (360, 480))))
            tmp.unlink()

scene_dir = ROOT / "O01_menton" / "scenes"
scenes = [(uri(scene_dir / f, (420, 746)), alt) for f, alt in
          [("line_01.png", "Scène : tête en hologramme, le menton allumé en rouge"),
           ("line_03.png", "Scène : bassin en hologramme, ovaires et surrénales allumés"),
           ("line_05.png", "Scène : coupe de peau, la glande à sébum allumée")] if (scene_dir / f).exists()]

cover_html = "\n".join(
    f'<figure class="cover"><img src="{u}" alt="Miniature : {e(c["name"])}, partie {k}, {e(c["eps"][k - 1][0])}" '
    f'loading="lazy"></figure>' for c, k, u in covers)
scene_html = "".join(f'<img src="{u}" alt="{e(a)}">' for u, a in scenes)

chapters_html = []
for c in CHAPTERS:
    eps = "\n".join(f'''
      <li class="ep">
        <p class="ep-head"><span class="ep-n">Partie {k}</span> <span class="ep-title">{e(t)}</span></p>
        <p class="ep-hook">{e(hook)}</p>
        <p class="ep-what">{e(what)}</p>
        <p class="ep-end"><span>Chute</span> {e(end)}</p>
      </li>''' for k, (t, hook, what, end, _o, _g) in enumerate(c["eps"], 1))
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

PAGE = f'''<title>Saison 1 du compte Organes</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700;800&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Layout: one reading column like a scan report; covers break out into a profile-grid band. Dark first, like the videos. */
:root {{
  --bg: #070b16; --surface: #0e1528; --ink: #eef2fb; --muted: #9aa6c2; --line: #1f2a45;
  --alert: #ff3126; --alert-ink: #070b16; --holo: #6f9cff;
  --sans: "Open Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "Cascadia Mono", Consolas, monospace;
  color-scheme: dark;
}}
@media (prefers-color-scheme: light) {{
  :root:not([data-theme="dark"]) {{
    --bg: #f4f6fb; --surface: #e8ecf5; --ink: #0b1226; --muted: #4c5875; --line: #d2d9e8;
    --alert: #8a7600; --alert-ink: #ffffff; --holo: #2c5fd6; color-scheme: light;
  }}
}}
:root[data-theme="light"] {{
  --bg: #f4f6fb; --surface: #e8ecf5; --ink: #0b1226; --muted: #4c5875; --line: #d2d9e8;
  --alert: #8a7600; --alert-ink: #ffffff; --holo: #2c5fd6; color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ background: var(--bg); color: var(--ink); font: 400 1.0625rem/1.6 var(--sans); }}
.wrap {{ max-width: 68rem; margin: 0 auto; padding-inline: max(16px, 4vw); padding-block: 3rem 5rem; }}
.col {{ max-width: 44rem; }}
h1, h2, h3 {{ font-weight: 800; text-wrap: balance; margin: 0; letter-spacing: -0.01em; }}
h1 {{ font-size: clamp(2.1rem, 5vw, 3.3rem); line-height: 1.05; text-transform: uppercase; }}
h1 em {{ font-style: normal; color: var(--alert); }}
h2 {{ font-size: clamp(1.5rem, 3.2vw, 2.1rem); line-height: 1.15; margin-bottom: 1rem; }}
h3 {{ font-size: 1.45rem; line-height: 1.2; }}
p {{ margin: 0 0 1rem; }}
.eyebrow {{ font: 500 0.75rem/1.4 var(--mono); letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); margin: 0 0 0.4rem; }}
.lede {{ font-size: 1.2rem; color: var(--muted); max-width: 40rem; margin-top: 1rem; }}
section.block {{ margin-top: 4.5rem; display: grid; gap: 1.25rem; }}
.brief {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr)); gap: 1rem; margin-top: 2rem; }}
.brief div {{ border-top: 2px solid var(--line); padding-top: 0.8rem; min-width: 0; }}
.brief strong {{ display: block; font-weight: 800; font-size: 1.1rem; margin-bottom: 0.2rem; }}
.brief span {{ color: var(--muted); font-size: 0.95rem; }}
.rules {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(17rem, 1fr)); gap: 1.5rem 2rem; }}
.rules > div {{ min-width: 0; }}
.rules h4 {{ font: 700 1rem/1.4 var(--sans); margin: 0 0 0.35rem; }}
.rules p {{ color: var(--muted); font-size: 0.97rem; }}
mark {{ background: none; color: var(--alert); font-weight: 700; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(8.5rem, 1fr)); gap: 0.75rem; }}
.sw {{ border: 1px solid var(--line); border-radius: 8px; overflow: hidden; background: var(--surface); }}
.sw i {{ display: block; height: 3.2rem; }}
.sw p {{ margin: 0; padding: 0.5rem 0.6rem 0.6rem; font-size: 0.82rem; line-height: 1.35; }}
.sw b {{ display: block; font-weight: 700; }}
.sw code {{ font: 500 0.72rem var(--mono); color: var(--muted); }}
.covers {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(9.5rem, 1fr)); gap: 3px; }}
.cover {{ margin: 0; }}
.cover img {{ width: 100%; max-width: 100%; aspect-ratio: 3 / 4; object-fit: cover; display: block; }}
.note {{ font-size: 0.92rem; color: var(--muted); }}
.duo {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr)); gap: 1.5rem; align-items: start; }}
.duo > * {{ min-width: 0; }}
.scenes {{ display: flex; gap: 0.5rem; }}
.scenes img {{ width: 33%; min-width: 0; border-radius: 6px; aspect-ratio: 9 / 16; object-fit: cover; }}
.chapter {{ margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--line); }}
.ch-head {{ display: flex; gap: 1rem; align-items: flex-start; margin-bottom: 1.25rem; }}
.ch-chip {{ flex: none; width: 2.6rem; height: 2.6rem; border-radius: 50%; margin-top: 0.3rem;
  background: radial-gradient(circle at 50% 50%, var(--tint), #0b1a33 72%); box-shadow: 0 0 18px -2px var(--tint); }}
.ch-why {{ color: var(--muted); margin: 0.3rem 0 0; max-width: 42rem; }}
.eps {{ list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(19rem, 1fr)); gap: 1.6rem 2.2rem; }}
.ep {{ min-width: 0; border-left: 2px solid var(--tint); padding-left: 0.9rem; }}
.ep p {{ margin: 0 0 0.3rem; }}
.ep-head {{ display: flex; gap: 0.5rem; align-items: baseline; flex-wrap: wrap; }}
.ep-n {{ font: 500 0.72rem/1 var(--mono); letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); }}
.ep-title {{ font-size: 1.15rem; font-weight: 800; }}
.ep-hook {{ font-weight: 600; }}
.ep-what {{ color: var(--muted); font-size: 0.93rem; }}
.ep-end {{ font-size: 0.93rem; }}
.ep-end span {{ font: 500 0.7rem var(--mono); letter-spacing: 0.1em; text-transform: uppercase; color: var(--alert); margin-right: 0.3rem; }}
.tablewrap {{ overflow-x: auto; border: 1px solid var(--line); border-radius: 8px; }}
table {{ border-collapse: collapse; width: 100%; font-size: 0.95rem; min-width: 34rem; }}
th, td {{ text-align: left; padding: 0.6rem 0.8rem; border-bottom: 1px solid var(--line); vertical-align: top; }}
th {{ font: 500 0.72rem/1.3 var(--mono); letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); }}
td.num, th.num {{ text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }}
tr.total td {{ font-weight: 700; border-bottom: 0; }}
.steps {{ padding-left: 1.2rem; margin: 0; display: grid; gap: 0.6rem; }}
a {{ color: var(--holo); }}
:focus-visible {{ outline: 2px solid var(--alert); outline-offset: 2px; }}
</style>

<main class="wrap">
  <header class="col">
    <p class="eyebrow">Compte Organes · format « expliqué en 60 secondes »</p>
    <h1>Saison 1 : <em>6 chapitres</em>, 48 vidéos</h1>
    <p class="lede">Le même format que le compte vidéo Acné (chapitres de 8 parties, voix grave de reportage, musique d'enquête, CTA qui monte), avec la direction artistique alarmiste des carrousels Organes et ses propres angles.</p>
  </header>

  <div class="brief">
    <div><strong>8 vidéos par chapitre</strong><span>Une série « … décodé », parties 1 à 8, puis le chapitre suivant. Le menu du chapitre ouvre chaque vidéo.</span></div>
    <div><strong>Une vidéo par jour</strong><span>Le matin. Un chapitre = 8 jours, la saison ≈ 7 semaines.</span></div>
    <div><strong>Moins de 2 $ par vidéo</strong><span>Même pipeline que le compte Acné : environ 1,10 à 1,30 $ facturés.</span></div>
    <div><strong>La DA des carrousels</strong><span>Pas celle de Nacria : le scanner, l'organe qui s'allume, la couleur d'alerte du chapitre.</span></div>
  </div>

  <section class="block">
    <div class="col">
      <p class="eyebrow">Direction artistique « scanner »</p>
      <h2>Ce qui faisait arrêter le pouce sur les carrousels, mis en mouvement</h2>
      <p>Les carrousels Organes marchent sur un contraste : une zone du visage entourée, puis l'organe qui s'allume dans un corps en radiographie. La vidéo garde exactement ces codes, et les anime.</p>
    </div>
    <div class="rules">
      <div><h4>Le corps en hologramme</h4><p>Un corps translucide bleu nuit, comme une radio, sur un fond marine piqué de particules. L'organe de l'histoire brille de l'intérieur, avec ses vaisseaux allumés.</p></div>
      <div><h4>Le cercle pointillé</h4><p>Le cercle pointillé des carrousels se dessine autour de la zone au moment où la voix en parle, puis respire. C'est la signature du compte, faite en code, donc gratuite.</p></div>
      <div><h4>Les mots qui sonnent l'alerte</h4><p>Sous-titres en gras blanc, les mots-clés dans la couleur d'alerte du chapitre (rouge pour le visage), comme « Si tu as un bouton sur le <mark>Menton</mark> ». Les chiffres s'allument dans la même couleur, cernés de noir pour rester lisibles sur l'organe qui brille.</p></div>
      <div><h4>La ligne de scanner</h4><p>Sur les plans fixes, une ligne froide balaie le corps de haut en bas, comme un examen en cours. Le reste bouge par IA, caméra fixe.</p></div>
      <div><h4>Une couleur par chapitre</h4><p>Rouge pour le visage, rose pour les hormones, orange pour le ventre, violet pour le cerveau, vert néon pour les faux coupables, cyan pour la peau. Chaque chapitre forme une bande reconnaissable sur la grille.</p></div>
      <div><h4>Alarmiste, jamais faux</h4><p>L'accroche fait peur, la réponse est vraie et sourcée. Les mythes du « face mapping » (le nez et le cœur, les joues et les poumons) ne servent que d'accroches cassées. Un signe médical renvoie toujours vers un médecin.</p></div>
    </div>
    <div class="swatches">
      <div class="sw"><i style="background:#0b1a33"></i><p><b>Marine scanner</b>fond des vidéos<br><code>#0B1A33</code></p></div>
      <div class="sw"><i style="background:#3d6bc4"></i><p><b>Bleu radio</b>le corps translucide<br><code>#3D6BC4</code></p></div>
      <div class="sw"><i style="background:#ffffff"></i><p><b>Blanc</b>le cercle pointillé<br><code>#FFFFFF</code></p></div>
      <div class="sw"><i style="background:#ff3b30"></i><p><b>Rouge</b>chapitre 1, le visage<br><code>#FF3B30</code></p></div>
      <div class="sw"><i style="background:#ff2e7e"></i><p><b>Rose</b>chapitre 2, les hormones<br><code>#FF2E7E</code></p></div>
      <div class="sw"><i style="background:#ffb020"></i><p><b>Ambre</b>le sébum<br><code>#FFB020</code></p></div>
    </div>
    <div class="duo">
      <div>
        <h3>Typographie et ton</h3>
        <p><b>Open Sans ExtraBold</b>, la police des carrousels, en capitales pour les titres et les miniatures, en gras pour les sous-titres. Même voix grave de reportage que le compte Acné, même musique d'enquête, rendue plus clinique (pulsation de moniteur cardiaque, textures froides).</p>
        <p>On la tutoie. L'accroche part d'une peur ou d'une croyance (« ton nez et ton cœur »), la vidéo la démonte, la chute en antithèse remet la vraie cause à sa place.</p>
      </div>
      <div>
        <h3>Le rendu dans la vidéo</h3>
        <div class="scenes">{scene_html}</div>
        <p class="note">Trois images de départ de la partie 1, « Le menton ». Chacune est animée ou balayée par le scanner.</p>
      </div>
    </div>
  </section>

  <section class="block">
    <div class="col">
      <p class="eyebrow">Miniatures</p>
      <h2>La grammaire du compte modèle, aux couleurs des carrousels</h2>
      <p>Même structure que les miniatures de @learning.of.theday : le titre de série en capitales blanches, la pastille « PARTIE N », l'objet, le sujet en énormes capitales dans la couleur du chapitre, qui brille comme un voyant d'alarme, et l'accroche dessous. Tout tient dans le carré visible sur la grille du profil.</p>
    </div>
    <div class="covers">
{cover_html}
    </div>
    <p class="note">Ci-dessus : les 8 miniatures du chapitre 1, puis la partie 1 des chapitres 2 à 6, recadrées comme sur un profil.</p>
  </section>

  <section class="block" id="plan">
    <div class="col">
      <p class="eyebrow">Plan des 48 vidéos</p>
      <h2>Du visage vers l'intérieur du corps</h2>
      <p>La saison part de ce qui a fait les meilleurs chiffres des carrousels, la carte du visage, puis descend dans le corps : les hormones, le ventre, le cerveau. Elle démonte ensuite les faux coupables et se referme sur la peau elle-même, vue comme un organe. Aucune vidéo ne cite de marque, ne promet de résultat ni ne pose de diagnostic.</p>
    </div>
{"".join(chapters_html)}
  </section>

  <section class="block">
    <div class="col">
      <p class="eyebrow">Budget</p>
      <h2>Environ 1,10 à 1,30 $ par vidéo</h2>
      <p>Les prix sont ceux réellement facturés par fal sur le compte Acné. Les animations en code (cercle pointillé, scanner, lueur, compteurs) ne coûtent rien.</p>
    </div>
    <div class="tablewrap">
      <table>
        <thead><tr><th>Poste</th><th>Choix</th><th class="num">Coût</th></tr></thead>
        <tbody>
          <tr><td>8 images de scène</td><td>Nano Banana, 0,04 $ l'image</td><td class="num">0,32 $</td></tr>
          <tr><td>Image héros (miniature + icône du menu)</td><td>Nano Banana Pro 2K</td><td class="num">0,15 $</td></tr>
          <tr><td>7 animations de 2 à 4 s</td><td>Grok Imagine, facturé à la seconde</td><td class="num">≈ 0,55 $</td></tr>
          <tr><td>Voix</td><td>Gemini, voix Despina « reportage »</td><td class="num">0,05 $</td></tr>
          <tr><td>Calage voix et sous-titres</td><td>Alignement local</td><td class="num">0 $</td></tr>
          <tr><td>Musique composée sur le texte</td><td>Lyria 3.5</td><td class="num">0,10 $</td></tr>
          <tr class="total"><td>Total par vidéo</td><td></td><td class="num">≈ 1,17 $</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="block">
    <div class="col">
      <p class="eyebrow">À valider</p>
      <h2>Pour lancer la suite</h2>
      <ol class="steps">
        <li><b>La direction artistique</b> : scanner, organe lumineux, une couleur d'alerte par chapitre (rouge, rose, orange, violet, vert toxique, cyan), Open Sans.</li>
        <li><b>Les 6 chapitres et leur ordre</b>, et les 48 titres, accroches et chutes ci-dessus. Tout se modifie ligne par ligne.</li>
        <li><b>La partie 1, « Le menton »</b>, produite avec ce pipeline.</li>
      </ol>
    </div>
  </section>
</main>
'''

OUT.write_text(PAGE, encoding="utf-8")
print(OUT, f"{len(PAGE) / 1024:.0f} KB", len(covers), "covers", len(scenes), "scenes")
