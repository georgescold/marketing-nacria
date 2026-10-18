"""Build the season plan page (HTML, images embedded) from plan.py and the demo covers.

Usage: python page_plan.py   -> ../../compte vidéo/Plan saison 1.html
"""
import base64, html, io, pathlib

from PIL import Image

from plan import CHAPTERS

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent / "compte vidéo"
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
        if p.exists():
            covers.append((c, k, uri(p, (360, 640))))

scenes = [uri(MINI / "scenes_test" / f, (420, 740)) for f in ("scene_sebum.png", "scene_bouton.png")]

cover_html = "\n".join(
    f'<figure class="cover"><img src="{u}" alt="Miniature : {e(c["name"])}, partie {k}, {e(c["eps"][k - 1][0])}" '
    f'loading="lazy"><figcaption>{e(c["eps"][k - 1][0])}</figcaption></figure>' for c, k, u in covers)

chapters_html = []
for c in CHAPTERS:
    eps = "\n".join(f'''
      <li class="ep">
        <p class="ep-head"><span class="ep-n">Partie {k}</span> <span class="ep-title">{e(t)}</span></p>
        <p class="ep-hook">{e(hook)}</p>
        <p class="ep-what">{e(what)}</p>
        <p class="ep-end">{e(end)}</p>
      </li>''' for k, (t, hook, what, end, _o, _a) in enumerate(c["eps"], 1))
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

PAGE = f'''<title>Saison 1 du compte vidéo</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400..700&family=Fraunces:opsz,wght,SOFT@9..144,300..650,0..100&display=swap">
<style>
/* Layout: one reading column like the scripts themselves; the covers break out into a profile-grid band. Dark first, like the videos. */
:root {{
  --bg: #17121a; --surface: #211a23; --ink: #f3ece4; --muted: #b9aeb3; --line: #3a2f3b;
  --terracotta: #c27359; --sage: #9fb7aa; --gold: #d3a654;
  --serif: "Fraunces", Georgia, "Times New Roman", serif;
  --sans: "DM Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  color-scheme: dark;
}}
@media (prefers-color-scheme: light) {{
  :root:not([data-theme="dark"]) {{
    --bg: #fbf7f2; --surface: #f3ebe2; --ink: #2e2a33; --muted: #6b6168; --line: #e3d8cd;
    --terracotta: #a95a3e; --sage: #5f7d6e; --gold: #9a6f22; color-scheme: light;
  }}
}}
:root[data-theme="light"] {{
  --bg: #fbf7f2; --surface: #f3ebe2; --ink: #2e2a33; --muted: #6b6168; --line: #e3d8cd;
  --terracotta: #a95a3e; --sage: #5f7d6e; --gold: #9a6f22; color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ background: var(--bg); color: var(--ink); font: 400 1.0625rem/1.6 var(--sans); }}
.wrap {{ max-width: 68rem; margin: 0 auto; padding-inline: max(16px, 4vw); padding-block: 3rem 5rem; }}
.col {{ max-width: 44rem; }}
h1, h2, h3 {{ font-family: var(--serif); font-variation-settings: "SOFT" 100; font-weight: 450; text-wrap: balance; margin: 0; }}
h1 {{ font-size: clamp(2.2rem, 5vw, 3.4rem); line-height: 1.05; }}
h2 {{ font-size: clamp(1.6rem, 3.4vw, 2.2rem); line-height: 1.15; margin-bottom: 1rem; }}
h3 {{ font-size: 1.5rem; line-height: 1.2; }}
p {{ margin: 0 0 1rem; }}
.eyebrow {{ font: 600 0.75rem/1.4 var(--sans); letter-spacing: 0.14em; text-transform: uppercase; color: var(--muted); margin: 0 0 0.4rem; }}
.lede {{ font-size: 1.2rem; color: var(--muted); max-width: 40rem; margin-top: 1rem; }}
section.block {{ margin-top: 4.5rem; display: grid; gap: 1.25rem; }}
.brief {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr)); gap: 1rem; margin-top: 2rem; }}
.brief div {{ border-top: 1px solid var(--line); padding-top: 0.8rem; min-width: 0; }}
.brief strong {{ display: block; font-family: var(--serif); font-weight: 500; font-size: 1.15rem; margin-bottom: 0.2rem; }}
.brief span {{ color: var(--muted); font-size: 0.95rem; }}
.rules {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(17rem, 1fr)); gap: 1.5rem 2rem; }}
.rules > div {{ min-width: 0; }}
.rules h4 {{ font: 600 1rem/1.4 var(--sans); margin: 0 0 0.35rem; }}
.rules p {{ color: var(--muted); font-size: 0.97rem; }}
q, .quote {{ font-family: var(--serif); font-style: italic; color: var(--ink); }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(8.5rem, 1fr)); gap: 0.75rem; }}
.sw {{ border: 1px solid var(--line); border-radius: 10px; overflow: hidden; background: var(--surface); }}
.sw i {{ display: block; height: 3.2rem; }}
.sw p {{ margin: 0; padding: 0.5rem 0.6rem 0.6rem; font-size: 0.82rem; line-height: 1.35; }}
.sw b {{ display: block; font-weight: 600; }}
.sw code {{ font-size: 0.75rem; color: var(--muted); font-variant-numeric: tabular-nums; }}
.covers {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(9.5rem, 1fr)); gap: 3px; }}
.cover {{ margin: 0; position: relative; }}
.cover img {{ width: 100%; aspect-ratio: 3 / 4; object-fit: cover; display: block; }}
.cover figcaption {{ position: absolute; inset: auto 0 0 0; padding: 0.3rem 0.5rem; font-size: 0.72rem; color: #f3ece4; background: linear-gradient(transparent, rgba(14, 11, 15, 0.85)); opacity: 0; transition: opacity .2s; }}
.cover:hover figcaption, .cover:focus-within figcaption {{ opacity: 1; }}
.note {{ font-size: 0.92rem; color: var(--muted); }}
.duo {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr)); gap: 1.5rem; align-items: start; }}
.duo > * {{ min-width: 0; }}
.scenes {{ display: flex; gap: 0.75rem; }}
.scenes img {{ width: 50%; border-radius: 8px; aspect-ratio: 9 / 16; object-fit: cover; }}
.words {{ display: flex; flex-wrap: wrap; gap: 0.5rem; padding: 0; margin: 0; list-style: none; }}
.words li {{ border: 1px solid var(--line); border-radius: 999px; padding: 0.25rem 0.75rem; font-size: 0.9rem; }}
.words.no li {{ text-decoration: line-through; color: var(--muted); }}
.chapter {{ margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--line); }}
.ch-head {{ display: flex; gap: 1rem; align-items: flex-start; margin-bottom: 1.25rem; }}
.ch-chip {{ flex: none; width: 2.6rem; height: 2.6rem; border-radius: 50%; margin-top: 0.3rem;
  background: radial-gradient(circle at 40% 35%, var(--tint), #2a2029 75%); box-shadow: 0 0 0 1px var(--line); }}
.ch-why {{ color: var(--muted); margin: 0.3rem 0 0; max-width: 42rem; }}
.eps {{ list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(19rem, 1fr)); gap: 1.6rem 2.2rem; }}
.ep {{ min-width: 0; border-left: 2px solid var(--tint); padding-left: 0.9rem; }}
.ep p {{ margin: 0 0 0.3rem; }}
.ep-head {{ display: flex; gap: 0.5rem; align-items: baseline; flex-wrap: wrap; }}
.ep-n {{ font: 600 0.72rem/1 var(--sans); letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); }}
.ep-title {{ font-family: var(--serif); font-variation-settings: "SOFT" 100; font-size: 1.2rem; font-weight: 500; }}
.ep-hook {{ font-family: var(--serif); font-style: italic; }}
.ep-what {{ color: var(--muted); font-size: 0.93rem; }}
.ep-end {{ font-size: 0.93rem; }}
.ep-end::before {{ content: "Chute · "; font-weight: 600; color: var(--muted); font-size: 0.72rem; letter-spacing: 0.1em; text-transform: uppercase; }}
.tablewrap {{ overflow-x: auto; border: 1px solid var(--line); border-radius: 10px; }}
table {{ border-collapse: collapse; width: 100%; font-size: 0.95rem; min-width: 34rem; }}
th, td {{ text-align: left; padding: 0.6rem 0.8rem; border-bottom: 1px solid var(--line); vertical-align: top; }}
th {{ font: 600 0.75rem/1.3 var(--sans); letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); }}
td.num, th.num {{ text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }}
tr.total td {{ font-weight: 600; border-bottom: 0; }}
.steps {{ padding-left: 1.2rem; margin: 0; display: grid; gap: 0.6rem; }}
a {{ color: var(--terracotta); }}
:focus-visible {{ outline: 2px solid var(--terracotta); outline-offset: 2px; }}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; }} }}
</style>

<main class="wrap">
  <header class="col">
    <p class="eyebrow">Compte vidéo acné · format « expliqué en 60 secondes »</p>
    <h1>Saison 1 : 6 chapitres, 48 vidéos</h1>
    <p class="lede">La structure du compte, sa direction artistique et le plan de chaque vidéo, à valider avant de produire. Construit sur l'étude d'avatar du 1er octobre et sur l'analyse du compte modèle.</p>
  </header>

  <div class="brief">
    <div><strong>8 vidéos par chapitre</strong><span>Comme le compte modèle : une série « … expliqués », parties 1 à 8, puis le chapitre suivant.</span></div>
    <div><strong>Une vidéo par jour</strong><span>Le matin, comme le modèle (12 vidéos en 10 jours). Un chapitre = 8 jours, la saison ≈ 7 semaines.</span></div>
    <div><strong>Moins de 2 $ par vidéo</strong><span>Budget calculé sur les prix réellement facturés par fal, détaillé plus bas.</span></div>
    <div><strong>Une DA pour elle</strong><span>La grammaire du modèle, recolorée avec ses codes à elle et la charte Nacria.</span></div>
  </div>

  <section class="block">
    <div class="col">
      <p class="eyebrow">Structure</p>
      <h2>Un chapitre, c'est une série de 8 vidéos qui se répondent</h2>
      <p>Chaque vidéo s'ouvre sur la carte du chapitre, avec ses 8 icônes, puis zoome sur la partie du jour. Le spectateur voit qu'il y a une suite, et l'abonnement devient le moyen de ne rien manquer. Les chapitres s'enchaînent sans pause : le modèle publie la partie 8 d'une série la veille de la partie 1 de la suivante.</p>
      <p>Chaque vidéo suit la même trame : une accroche (un mythe ou un chiffre, dans ses mots à elle), le mécanisme expliqué pas à pas, puis une chute en antithèse qui répond à l'accroche. C'est la phrase qu'on retient et qu'on partage.</p>
      <p>Le format est infini : après la saison 1, d'autres chapitres prennent le relais (le dos et le décolleté, les marques, la peau selon l'âge, les mythes de la peau). Quand le compte grandit, deux séries peuvent tourner en parallèle, comme le fait déjà le modèle.</p>
    </div>
  </section>

  <section class="block">
    <div class="col">
      <p class="eyebrow">Direction artistique</p>
      <h2>Ce qu'elle aime, ce qu'elle fuit, et ce qu'on en fait</h2>
      <p>Notre avatar, « l'adulte prise de court », a 24 à 32 ans. Elle ne veut pas d'abord une peau parfaite : elle veut <q>ne plus y penser</q>. La DA garde la force du modèle (fond sombre, objets sculptés, caméra fixe, une seule couleur qui raconte) et la recolore pour elle.</p>
    </div>
    <div class="rules">
      <div><h4>Une adulte parle à une adulte</h4><p>Sa blessure n°1 : <q>je suis adulte et j'ai une peau d'ado</q>. Donc pas de pastel adolescent ni d'emoji : un fond sombre de documentaire et une typographie serif éditoriale, celle d'un magazine.</p></div>
      <div><h4>Jamais une pub, jamais un visage</h4><p>Elle zappe ce qui ressemble à de la pub (<q>Is this an ad??</q>, mouvement deinfluencing) et trouve <q>assez violent</q> de voir un visage acnéique dessiné. Donc aucune marque, aucun produit nommé, aucun visage : des objets en porcelaine.</p></div>
      <div><h4>Ses codes à elle</h4><p>Les carrousels acné les plus vus de notre étude sont beiges et terre (illustration beige uniforme : 24,1 M de vues) ou éditoriaux en serif sur fond vert (2,6 M). Hypothèse : ce sont ses codes. On reprend la palette Nacria : ivoire, terracotta, rose poudré, sauge.</p></div>
      <div><h4>La signature : la porcelaine nacrée</h4><p>Les objets passent du gris du modèle à un ivoire chaud au reflet nacré, le clin d'œil au nom de la marque. Le fond devient une encre prune, plus intime que le bleu clinique.</p></div>
      <div><h4>Rassurer avant d'expliquer</h4><p>Les chutes répètent ce qu'elle a besoin d'entendre : ce n'est pas de la saleté, ce n'est pas dans ta tête, ce n'est pas un échec. Ça répond aux <q>réflexions déplacées sur mon hygiène</q> qu'elle subit.</p></div>
      <div><h4>Du calme, pas de l'urgence</h4><p>Voix douce et soufflée, musique feutrée qui suit l'émotion du texte, mouvements lents. Le contraire du miroir du matin et de sa <q>boule au ventre</q>.</p></div>
    </div>

    <div class="col"><h3>La palette</h3></div>
    <div class="swatches">
      <div class="sw"><i style="background:#2a2029"></i><p><b>Encre prune</b>fond des vidéos<br><code>#2A2029</code></p></div>
      <div class="sw"><i style="background:#fbf7f2"></i><p><b>Ivoire nacré</b>objets, titres<br><code>#FBF7F2</code></p></div>
      <div class="sw"><i style="background:#d3a654"></i><p><b>Miel</b>le sébum<br><code>#C9973F</code></p></div>
      <div class="sw"><i style="background:#a95a3e"></i><p><b>Terracotta</b>l'inflammation<br><code>#A95A3E</code></p></div>
      <div class="sw"><i style="background:#0e0b0f"></i><p><b>Noir</b>le bouchon oxydé<br><code>#0E0B0F</code></p></div>
      <div class="sw"><i style="background:#8fa89a"></i><p><b>Sauge</b>l'apaisement, la solution<br><code>#8FA89A</code></p></div>
      <div class="sw"><i style="background:#8b5a3c"></i><p><b>Brun</b>les marques<br><code>#8B5A3C</code></p></div>
    </div>
    <p class="note">Chaque chapitre a sa lueur derrière les objets : terracotta, rose poudré, miel, argile, sauge, lavande. Sur la grille du profil, chaque chapitre forme une bande de couleur reconnaissable. Le modèle fait pareil avec deux couleurs (bleu pétrole et ambre).</p>

    <div class="duo">
      <div>
        <h3>Typographie et ton</h3>
        <p><b>Fraunces</b> en version douce pour les titres, la carte du chapitre et les miniatures. <b>DM Sans</b> pour les sous-titres, en petit et en blanc comme le modèle. Les deux polices de la charte Nacria.</p>
        <p>On la tutoie comme une grande sœur qui a lu les études. Phrases courtes, un chiffre sourcé par vidéo, les sources dans la légende.</p>
        <p class="eyebrow" style="margin-top:1rem">Ses mots, repris dans les accroches</p>
        <ul class="words">
          <li>« ça revient »</li><li>« bois plus d'eau »</li><li>« le zinc, ça fonctionne pas »</li><li>« c'est hormonal »</li>
          <li>« à 30 ans »</li><li>« ce n'est pas de la saleté »</li><li>« ne plus y penser »</li><li>« moins, pas zéro »</li>
          <li>« tu as tout essayé en même temps »</li>
        </ul>
        <p class="eyebrow" style="margin-top:1rem">Mots bannis</p>
        <ul class="words no"><li>parfaite</li><li>miracle</li><li>guérir</li><li>avant / après</li><li>noms de marques</li><li>diagnostic</li></ul>
      </div>
      <div>
        <h3>Le rendu dans la vidéo</h3>
        <div class="scenes"><img src="{scenes[0]}" alt="Scène : coupe d'un pore avec du sébum doré"><img src="{scenes[1]}" alt="Scène : bouton terracotta sur un cube de peau ivoire"></div>
        <p class="note">Deux images de départ de scène, faites avec le modèle économique prévu pour la production (0,04 $ l'image). Chacune sera animée, caméra fixe.</p>
      </div>
    </div>
  </section>

  <section class="block">
    <div class="col">
      <p class="eyebrow">Miniatures</p>
      <h2>Une grille qui se lit par chapitre</h2>
      <p>Chaque miniature reprend l'objet de l'épisode, le nom du chapitre, « Partie N », le titre en Fraunces et 8 points qui montrent où l'on en est dans la série. Tout tient dans la zone 3:4 visible sur la grille du profil TikTok et Instagram. La même image sert aussi d'icône dans la carte d'ouverture du chapitre, sans coût de plus.</p>
    </div>
    <div class="covers">
{cover_html}
    </div>
    <p class="note">Ci-dessus : les 8 miniatures du chapitre 1, puis la partie 1 des chapitres 2 à 6, recadrées comme sur un profil. Survole une miniature pour voir son titre.</p>
  </section>

  <section class="block" id="plan">
    <div class="col">
      <p class="eyebrow">Plan des 48 vidéos</p>
      <h2>Six chapitres, de la question la plus large à son désir le plus profond</h2>
      <p>L'ordre va du vocabulaire de base vers ce qui la touche le plus : les hormones, la nourriture, les gestes, la routine, puis la saison se referme sur « Pourquoi ça revient » et son désir profond, ne plus y penser. Aucune vidéo ne cite de marque, ne promet de résultat ni ne pose de diagnostic. Quand un sujet relève du médecin (SOPK, traitements), la vidéo explique le mécanisme et renvoie vers lui.</p>
    </div>
{"".join(chapters_html)}
  </section>

  <section class="block">
    <div class="col">
      <p class="eyebrow">Budget</p>
      <h2>Environ 1,50 à 1,90 $ par vidéo</h2>
      <p>Les prix ci-dessous sont ceux réellement facturés sur ton compte fal (relevé de consommation du 14 octobre), pas les tarifs affichés. Le surcoût de l'épisode 1 venait de l'animation en 1080p, facturée environ 1 $ la scène. On ne paie plus que les secondes utiles, et seules les scènes qui en ont besoin sont animées par IA ; les autres bougent en code, gratuitement (entrée de l'objet, lueur, particules, compteur).</p>
    </div>
    <div class="tablewrap">
      <table>
        <thead><tr><th>Poste</th><th>Choix</th><th class="num">Coût</th></tr></thead>
        <tbody>
          <tr><td>12 images de scène</td><td>Nano Banana, 0,04 $ l'image</td><td class="num">0,48 $</td></tr>
          <tr><td>Image héros (miniature + icône du menu)</td><td>Nano Banana Pro 2K</td><td class="num">0,15 $</td></tr>
          <tr><td>8 animations de 3 s</td><td>MiniMax H3 Turbo, 0,015 $ la seconde ; 4 scènes animées en code</td><td class="num">0,36 $</td></tr>
          <tr><td>Voix</td><td>Gemini, voix Despina « souffle »</td><td class="num">0,05 $</td></tr>
          <tr><td>Calage voix, sous-titres, images</td><td>Alignement ElevenLabs</td><td class="num">0,22 $</td></tr>
          <tr><td>Musique composée sur le texte</td><td>ElevenLabs Music (0,60 $) ou Lyria / MiniMax Music (0,10 à 0,12 $), à choisir à l'oreille</td><td class="num">0,10 à 0,60 $</td></tr>
          <tr><td>Marge de reprises (environ 10 %)</td><td></td><td class="num">0,15 $</td></tr>
          <tr class="total"><td>Total par vidéo</td><td></td><td class="num">1,51 à 2,01 $</td></tr>
        </tbody>
      </table>
    </div>
    <div class="col">
      <p class="note">Avec la musique ElevenLabs, le total frôle les 2 $ : si l'oreille ne fait pas la différence avec Lyria ou MiniMax Music, on prend la moins chère. Le premier jour de production, je teste sur 3 scènes le modèle d'animation (H3 Turbo avec image de fin pour bloquer la caméra, contre deux autres modèles à moins de 0,05 $ la scène) et les trois moteurs de musique, puis je fige les choix. L'épisode 1 actuel, en bleu pétrole, est à refaire dans la nouvelle DA.</p>
    </div>
  </section>

  <section class="block">
    <div class="col">
      <p class="eyebrow">À valider</p>
      <h2>Pour lancer la production</h2>
      <ol class="steps">
        <li><b>La direction artistique</b> : encre prune, porcelaine nacrée, une couleur par chapitre, Fraunces.</li>
        <li><b>Les 6 chapitres et leur ordre</b>, et les 48 titres, accroches et chutes ci-dessus. Tout peut se modifier ligne par ligne.</li>
        <li><b>Le budget par vidéo</b> et les tests du premier jour.</li>
        <li><b>Le crédit fal</b> : il reste 7,03 $. Compter environ 15 $ pour le chapitre 1 avec les tests, puis environ 1,80 $ par vidéo.</li>
      </ol>
    </div>
  </section>
</main>
'''

OUT.write_text(PAGE, encoding="utf-8")
print(OUT, f"{len(PAGE) / 1024:.0f} KB", len(covers), "covers")
