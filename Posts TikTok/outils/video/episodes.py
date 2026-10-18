"""Video account (@learning.of.theday format, about acne): one entry per episode.

Each line of `lines` is spoken by the voice and gets its own animated visual: (text, scene prompt, accent, counter).
- scene prompt: the FIRST frame, what the matte grey clay objects show before they move (see STYLE)
- accent: the colours allowed in that first frame ("" = fully grey)
- counter: big number shown above the object while the line is spoken, e.g. ("2", "%", "0,5") or None
`motion[i]`: what moves during line i (image-to-video, locked camera): one clear action tied to the sentence, like the model
account (objects enter, fill, change colour, break apart, then hold).
Colour code of the series: golden oil = sebum, black = oxidised plug, red = inflammation.
Script rules (from the analysis of the model account): series title first, a myth or number hook, the path in the body,
"en temps normal / avec X", rising consequences with figures, one nuance, and a closing antithesis that is also the title.
"""

# The model account uses one background colour per series (dark teal-blue on 7 reels out of 12, amber on 5); this series: teal.
STYLE = ("Minimalist 3D render for a premium science explainer video, vertical 9:16 frame: {obj}, made of smooth matte light-grey "
         "clay, soft studio lighting with gentle ambient occlusion, high detail, crisp clean edges. Centred horizontally, its centre at "
         "about 42 percent of the frame height, occupying about 50 percent of the frame width, floating just above a soft blurred "
         "elliptical shadow. Background: a smooth dark teal-blue radial gradient, deep teal (#0b212d) behind the object fading to "
         "near-black (#020308) at the edges, no floor line, no horizon. Everything monochrome light grey{accent}. Calm, clean, "
         "museum-like educational style. The top fifth and the lower third of the frame stay empty. No text, no letters, no numbers, no logo.")

ICON = ("Minimalist 3D icon render, square frame: {obj}, made of smooth matte light-grey clay, soft studio lighting, crisp clean "
        "edges, centred, background a smooth dark teal-blue radial gradient (#0b212d fading to near-black). Monochrome light "
        "grey{accent}. No text, no letters, no numbers.")

# image-to-video prompt: prefix + the episode's motion[i]
MOTION = ("Smooth, slow, minimal 3D motion-design animation of warm ivory porcelain objects, like a premium educational explainer. "
          "Locked-off static camera: no camera movement, no zoom, no shake. The objects keep their shapes and materials, nothing "
          "else morphs. Same lighting and background throughout. No text. ")

GOLD = " except the oil, which is glossy translucent honey-gold"
RED = " except the bump, which is soft terracotta red"

# the season's score (validated on E01-E03): an investigative documentary, then each episode's sections follow its script
DOC_MUSIC = ["dark cinematic investigative documentary score", "serious, grave and tense, like a true-crime TV documentary",
             "minor key", "pulsing low synth bass", "sparse deep percussion hits", "felt piano motif", "tense string ostinato",
             "clear and present sound, not muffled", "wide dynamics with builds and drops", "instrumental", "100 BPM"]
SECTION = {"Cold open": ["no drums", "low mysterious drone", "ticking clock-like pulse", "single grave piano notes"],
           "Investigation": ["low pulsing bass enters", "tense string ostinato", "steady and serious"],
           "Tension": ["darker harmony", "rising tension", "sub bass swells"],
           "Revelation": ["a deep impact hit at the start", "grave descending piano motif", "suspense"],
           "Danger": ["darkest and most intense part", "heartbeat-like kick", "dissonant strings", "building up"],
           "Breath": ["stripped back", "a single sustained low note", "quiet tension"],
           "The answer": ["determined steady pulse returns", "still serious", "strings rise with a hint of resolve"],
           "Final word": ["one last deep impact hit", "then a dark sustained drone", "grave"]}


def score(*starts):
    """music=score((0, "Cold open"), (2, "Investigation"), ...): DOC_MUSIC with the standard sections at those lines."""
    return dict(style=DOC_MUSIC, sections=[(i, name, SECTION[name]) for i, name in starts])

EPISODES = {
    "E01_point_noir": dict(
        chapter=1,  # plan.py: art direction, glow colour, the chapter menu (8 hero icons) and the cover
        series="Les boutons expliqués",
        part="Partie 1 : Le point noir",
        menu=[("Point noir", "a stylised human nose with a few tiny dark dots on it", " except the tiny dots, which are black"),
              ("Bouton du menton", "a stylised chin with one round bump", " except the bump, which is soft red"),
              ("Kyste", "a cube of skin seen in cross-section with a deep round swelling inside", " except the swelling, which is soft red"),
              ("Marque brune", "a cube of skin with a flat round spot on its top surface", " except the spot, which is brown")],
        lines=[
            ("Les boutons expliqués. Partie 1. Le point noir.", None, "", None),
            ("Le noir d'un point noir, ce n'est pas de la saleté.",
             "a large stylised human nose seen from three-quarter view, with about eight tiny black dots scattered irregularly on "
             "the rounded tip and on the wings beside the nostrils, none on the bridge", " except the tiny dots, which are deep black", None),
            ("Sur ton nez, chaque pore est l'ouverture d'un poil, relié à une petite glande qui fabrique du sébum, l'huile de ta peau.",
             "a cube of skin cut in half showing a single hair follicle going down from the surface with a hair inside, and a small "
             "round empty gland attached to its side", "", None),
            ("En temps normal, le sébum remonte le long du poil et s'étale à la surface.",
             "a cube of skin cut in half showing a single hair follicle with a hair inside, and a small round gland attached to its "
             "side, the gland full of glossy honey-gold oil", GOLD, None),
            ("Mais les cellules mortes qui tapissent le pore peuvent rester collées entre elles.",
             "a short vertical transparent glass tube, its inner walls lined with many thin flat ivory flakes", "", None),
            ("Elles se mélangent au sébum, et forment un bouchon.",
             "a cube of skin cut in half showing a single hair follicle going down from the surface, with a small round gland "
             "attached to its side; inside the follicle, a few thin flat flakes float loose in glossy honey-gold oil", GOLD, None),
            ("Si le pore reste ouvert, le haut du bouchon touche l'air, et s'oxyde.",
             "a cube of skin cut in half showing a follicle filled with a solid rounded ivory plug whose top is level with the "
             "open surface", "", None),
            ("Il fonce, comme une pomme coupée qui brunit.",
             "half an apple seen from the front, its cut face fresh and pale", " except the cut face, which is pale cream", None),
            ("C'est le point noir. Fermé sous la peau, le même bouchon reste blanc : c'est le point blanc.",
             "a block of skin with two small pores side by side: on the left an open pore whose plug top is black, on the right "
             "an open pore with a light plug", " except the left plug top, which is black", None),
            ("Si tu le presses, tu peux faire craquer la paroi du pore, sous la peau.",
             "a cube of skin cut in half showing a follicle under a small bump on the top surface, and two thick ivory clay "
             "arrows on both sides of the bump, pointing inward toward it, the wall of the follicle intact", "", None),
            ("Le sébum se répand, ton corps l'attaque, et le point noir devient un bouton rouge.",
             "a cube of skin with a small black dot on its top surface", " except the small dot, which is black", None),
            ("Et un pore n'a pas de muscle. L'eau chaude ne l'ouvre pas, l'eau froide ne le ferme pas.",
             "a shower head floating above a small cube of skin with one pore on top, and a simple thermometer standing next to them",
             " except the thermometer liquid, which is soft terracotta red", None),
            ("Ce qui agit, c'est un actif qui se dissout dans le gras, comme l'acide salicylique.",
             "a ball-and-stick model of a small organic molecule with a benzene ring, floating above a round drop of glossy golden "
             "oil", " except the oil drop, which is glossy translucent honey-gold", None),
            ("Il entre dans le pore, et défait le bouchon de l'intérieur. Dans les soins, 0,5 à 2 % suffisent.",
             "a cube of skin cut in half showing the follicle filled with a solid plug whose top is black, a few tiny ivory "
             "molecules floating just above the opening", " except the top of the plug, which is black", ("2", "%", "0,5")),
            ("Ce n'est pas de la saleté. C'est un bouchon qui a pris l'air.",
             "a single rounded ivory plug, like a small cork, floating alone", "", None),
            # follow CTA in the energy of the documentary (user, 2026-10-14): the series is the reason (8 pimples, this was the
            # first), said with the same gravity; visual: the chapter grid lights up, then the account emblem with a "+" badge
            ("Le point noir n'est que le premier. Pour enfin comprendre tous les autres, abonne-toi.", None, "", None),
        ],
        motion={
            1: "The faint grey dots on the nose slowly darken to deep black, one after another.",
            2: "The small round gland slowly fills with glossy honey-gold oil that glows softly.",
            3: "Golden oil droplets rise slowly along the hair from the gland up to the opening, then spread as a thin glossy "
               "golden layer on the top surface of the block. The whole block stays fully in frame at the same size: the camera "
               "does not move and does not zoom in at all.",
            4: "The thin flakes slowly detach from the walls and stick together into one compact clump in the middle of the tube.",
            5: "The flakes and the honey-gold oil slowly thicken and set into one solid, opaque, ivory plug, like a cork, that "
               "completely fills the follicle from the bottom up to the surface. The block stays fully in frame, the camera does "
               "not move.",
            6: "Faint white swirls of air drift slowly over the opening, and the top of the plug slowly darkens from light grey "
               "to deep black.",
            7: "The cut face of the apple slowly turns brown, from the edges towards the centre.",
            8: "On the right, the skin slowly closes over the light plug and forms a smooth closed white dome, while the left "
               "pore stays open with its black top.",
            9: "The two clay arrows slowly push inward against the small bump. Below the surface, the wall of the vertical "
               "channel splits along a thin line that lights up soft terracotta red.",
            10: "The black dot slowly swells into a round inflamed bump that turns soft terracotta red, and a soft terracotta halo spreads around it.",
            11: "Clear water drops fall from the shower head onto the cube; the red liquid in the thermometer rises, then falls; "
                "the pore on the cube stays exactly the same size.",
            12: "The molecule slowly rotates and sinks into the honey-gold oil drop, dissolving into it.",
            13: "The tiny molecules slip down into the pore, and the plug slowly breaks apart into small particles that drift up "
                "out of the opening and fade away.",
            14: "The plug slowly rotates on itself while faint white swirls of air drift around its top, which slowly darkens "
                "to deep black.",
        },
        anim=[2, 3, 4, 5, 6, 7, 9, 10, 13],
        clip_end={6: 0.6, 9: 0.8},  # 6: the whole cube turns black at the end; 9: drops fall under the cube
        music=dict(
            # investigative documentary score, one section per beat of the script; each change lands just before its line.
            # Measured on the model account: clear, present music (centroid ~1 kHz, not muffled), sparse hits (~2/s), wide
            # dynamics (~20 dB) with builds and drops.
            style=["dark cinematic investigative documentary score", "serious, grave and tense, like a true-crime TV documentary",
                   "minor key", "pulsing low synth bass", "sparse deep percussion hits", "felt piano motif",
                   "tense string ostinato", "clear and present sound, not muffled", "wide dynamics with builds and drops",
                   "instrumental", "100 BPM"],
            sections=[(0, "Cold open", ["no drums", "low mysterious drone", "ticking clock-like pulse", "single grave piano notes"]),
                      (2, "Investigation", ["low pulsing bass enters", "tense string ostinato", "steady and serious"]),
                      (4, "Tension", ["darker harmony", "rising tension", "sub bass swells"]),
                      (6, "Revelation", ["a deep impact hit at the start", "grave descending piano motif", "suspense"]),
                      (9, "Danger", ["darkest and most intense part", "heartbeat-like kick", "dissonant strings", "building up"]),
                      (11, "Silence", ["sudden drop to near silence", "a single sustained low note"]),
                      (12, "The answer", ["determined steady pulse returns", "still serious", "strings rise with a hint of resolve"]),
                      (14, "Final word", ["one last deep impact hit", "then a long dark reverb tail", "grave ending"])]),
        tags={0:"[calm, confident documentary narrator, brisk pace]", 1: "[intrigued]", 9: "[gently warning]",
              11: "[matter-of-fact]", 14: "[softly, with a knowing smile]"},
        caption=(
            "Les boutons expliqués · Partie 1 : Le point noir\n\n"
            "Le point noir : ce n'est pas de la saleté, c'est un bouchon qui a pris l'air.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Un point noir est un « comédon ouvert ». Tout commence par un microcomédon, invisible à l'œil nu, qui se forme des "
            "semaines avant d'apparaître : c'est le point de départ de toutes les lésions d'acné (Cunliffe, Clinics in Dermatology, 2004).\n\n"
            "Beaucoup de « points noirs » du nez n'en sont pas : ce sont des filaments sébacés, du sébum normal qui remplit le pore. "
            "Ils sont grisâtres, plats, et reviennent même quand on les vide.\n\n"
            "Les patchs arrachent le haut du bouchon, pas ce qui le fabrique : le pore se remplit de nouveau.\n\n"
            "L'acide salicylique est soluble dans le gras, ce qui lui permet d'entrer dans le pore, là où le bouchon se forme "
            "(Arif, Clinical, Cosmetic and Investigational Dermatology, 2015). En vente libre, il est dosé de 0,5 à 2 %.\n\n"
            "Les rétinoïdes agissent plus en amont : ils empêchent les cellules mortes de se coller dans le pore. Ce sont les "
            "traitements de référence des comédons (Leyden, Dermatology and Therapy, 2017).\n\n"
            "Presser un point noir peut rompre la paroi du pore sous la peau : c'est ce qui transforme un comédon en bouton "
            "inflammatoire, et parfois en marque.\n\n"
            "#pointnoir #acne #acneadulte #peau #skincare"),
    ),
    "E02_point_blanc": dict(
        chapter=1,
        series="Les boutons expliqués",
        part="Partie 2 : Le point blanc",
        voice="Despina:reportage_cta",
        lines=[
            ("Les boutons expliqués. Partie 2. Le point blanc.", None, "", None),
            ("Le point blanc, c'est un point noir qui n'a jamais vu le jour.",
             "a cube of skin with one small smooth closed white dome on its top surface", " except the dome, which is pure white", None),
            ("Au départ, c'est le même bouchon : du sébum et des cellules mortes, coincés dans un pore.",
             "a cube of skin cut in half showing a single follicle filled with a solid ivory plug of oil and thin flakes, its top "
             "open at the surface", "", None),
            ("Mais ici, l'entrée du pore est fermée par une fine couche de peau.", None, "", None),
            ("Le bouchon ne touche jamais l'air. Il ne s'oxyde pas, il ne noircit pas.", None, "", None),
            ("Il reste blanc, ou couleur peau, à peine en relief.",
             "the top surface of a block of skin seen at a low angle, with a few tiny smooth closed bumps barely raised, some "
             "white and some skin-coloured", "", None),
            ("On le voit surtout sur le front, le menton et les joues, quand la lumière arrive de côté.",
             "a smooth gently curved porcelain skin surface like a soft hill, with several tiny closed white bumps, lit by a low "
             "grazing light from the side so that each bump casts a tiny shadow", "", None),
            ("Et contrairement à ce qu'on croit, ce blanc n'est pas du pus.", None, "", None),
            ("Le pus, ce sont des globules blancs. Ici, il n'y a pas d'inflammation : juste un bouchon enfermé.",
             "a small group of round pure white cells floating on the left, and on the right a calm cube of skin in cross-section "
             "with a pale ivory plug sealed under a closed surface", " except the round cells, which are bright pure white", None),
            ("Le problème, c'est qu'un pore fermé ne peut pas se vider.", None, "", None),
            ("Si tu le presses, le bouchon n'a pas de sortie : il s'enfonce et fait craquer la paroi.", None, "", None),
            ("C'est souvent comme ça qu'un point blanc devient un bouton rouge.", None, "", None),
            ("Les crèmes trop riches et certains produits pour cheveux peuvent en faire apparaître sur le front.",
             "a small open jar of thick rich cream and a small pump bottle of hair product standing on a gently curved block of "
             "skin with a few tiny closed white bumps", "", None),
            ("Ce qui les fait partir, ce sont les actifs qui renouvellent la peau, comme les rétinoïdes. Il faut compter environ "
             "12 semaines.",
             "a dropper bottle hovering above a cube of skin seen in cross-section with thin stacked layers and a few tiny closed "
             "white bumps on its top surface", "", ("12", "semaines", "12")),
            ("Ce n'est pas du pus. C'est un bouchon resté dans le noir.",
             "a pale ivory plug resting inside a closed dark rounded cavity carved into a porcelain block, a faint light from above",
             "", None),
            ("Le point blanc, c'est le deuxième. Il en reste six. Pour enfin tous les comprendre, abonne-toi.", None, "", None),
        ],
        # first frame of a scene = last frame of an earlier scene showing the same object (no new image, and continuity)
        chain={3: 2, 4: 3, 7: 1, 9: 3, 10: 9, 11: 10},  # 9 starts from the clean closed pore (4 ends with an air ring)
        motion={
            1: "Faint white swirls of air drift over the surface and slide past the closed white dome without getting in; the "
               "dome stays perfectly white.",
            3: "A thin layer of ivory skin slowly grows over the opening of the follicle until it is completely closed, sealing "
               "the plug inside. The camera does not move.",
            4: "Faint white swirls of air drift over the closed surface and bounce off it; the plug sealed inside stays pale "
               "ivory, it never darkens. The camera does not move.",
            7: "The white dome slowly becomes semi-transparent, like frosted glass, revealing inside it a solid pale ivory plug "
               "with a firm texture, not a liquid. Nothing else changes. The camera does not move.",
            9: "The sealed ivory plug slowly swells and presses against the closed opening, which stays shut. The camera does "
               "not move.",
            10: "Two thick ivory clay arrows slide in from both sides and press on the surface; the plug is pushed downward and "
                "the wall of the follicle splits along a thin line that lights up soft terracotta red. The camera does not move.",
            11: "The surface right above the follicle slowly swells into one small, low, round inflamed bump, no wider than the "
                "follicle, that turns soft terracotta red, with a faint terracotta halo around it. The camera does not move.",
            13: "A single drop falls from the dropper onto the cube; the top layers slowly renew and flake away, and the tiny "
                "white bumps flatten until the surface is smooth. The camera does not move.",
        },
        anim=[1, 3, 4, 7, 9, 10, 11, 13],
        fx={6: "sweep"},  # code animation: a grazing light sweeps across the bumps
        music=dict(
            style=["dark cinematic investigative documentary score", "serious, grave and tense, like a true-crime TV documentary",
                   "minor key", "pulsing low synth bass", "sparse deep percussion hits", "felt piano motif",
                   "tense string ostinato", "clear and present sound, not muffled", "wide dynamics with builds and drops",
                   "instrumental", "100 BPM"],
            sections=[(0, "Cold open", ["no drums", "low mysterious drone", "ticking clock-like pulse", "single grave piano notes"]),
                      (2, "Investigation", ["low pulsing bass enters", "tense string ostinato", "steady and serious"]),
                      (4, "Tension", ["darker harmony", "rising tension", "sub bass swells"]),
                      (7, "Revelation", ["a deep impact hit at the start", "grave descending piano motif", "suspense"]),
                      (9, "Danger", ["darkest and most intense part", "heartbeat-like kick", "dissonant strings", "building up"]),
                      (12, "Breath", ["stripped back", "a single sustained low note", "quiet tension"]),
                      (13, "The answer", ["determined steady pulse returns", "still serious", "strings rise with a hint of resolve"]),
                      (14, "Final word", ["one last deep impact hit", "then a dark sustained drone", "grave"])]),
        caption=(
            "Les boutons expliqués · Partie 2 : Le point blanc\n\n"
            "Le point blanc : ce n'est pas du pus, c'est un bouchon resté dans le noir.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Un point blanc est un « comédon fermé » : le même bouchon de sébum et de kératine qu'un point noir, mais sous un "
            "pore dont l'ouverture est fermée. Sans contact avec l'air, il ne fonce pas.\n\n"
            "Les comédons fermés sont petits (1 à 3 mm), souvent couleur peau, et se voient mieux en lumière rasante ou en "
            "tendant la peau.\n\n"
            "Ce ne sont pas des lésions inflammatoires : le blanc n'est pas du pus. Le pus, ce sont des globules blancs, qu'on "
            "trouve dans les pustules (Plewig et Kligman, Acne and Rosacea).\n\n"
            "Un comédon fermé ne peut pas se vider par le haut : le presser pousse son contenu vers le bas et peut rompre la "
            "paroi du follicule, ce qui déclenche l'inflammation.\n\n"
            "Certains cosmétiques très riches et produits capillaires gras peuvent favoriser des comédons fermés sur le front et "
            "les tempes : c'est l'« acné cosmétique » (Kligman et Mills, Archives of Dermatology, 1972).\n\n"
            "Les rétinoïdes topiques sont le traitement de référence des comédons ; leur effet s'évalue sur environ 12 semaines "
            "(Leyden, Dermatology and Therapy, 2017).\n\n"
            "#pointblanc #acne #acneadulte #peau #skincare"),
    ),
    "E03_bouton_rouge": dict(
        chapter=1,
        series="Les boutons expliqués",
        part="Partie 3 : Le bouton rouge",
        voice="Despina:reportage_cta",
        lines=[
            ("Les boutons expliqués. Partie 3. Le bouton rouge.", None, "", None),
            ("Un bouton rouge, c'est d'abord ton corps qui se défend.",
             "a cube of skin with one round swollen bump on its top surface", " except the bump, which is soft terracotta red", None),
            # scene 2 reuses E02's closed pore with its plug (copied before generation: free, and the series stays continuous)
            ("Au départ, c'est le même bouchon que le point noir et le point blanc.", "reused from E02", "", None),
            ("À l'intérieur, sans air, vit une bactérie que tout le monde a sur la peau.", None, "", None),
            ("Elle se nourrit de sébum, et se multiplie.", None, "", None),
            ("Tendue, la paroi du pore finit par céder sous la peau.", None, "", None),
            ("Pour ton corps, c'est une intrusion. Il envoie ses défenses.",
             "a cube of skin cut in half with a small torn follicle in the middle leaking a little honey-gold oil, and thin "
             "channels running towards it from both sides", GOLD, None),
            ("Les vaisseaux se dilatent : la peau rougit, chauffe, et gonfle.", None, "", None),
            ("Et ça fait mal, parce que l'enflure appuie sur les nerfs.",
             "a round swollen bump on a cube of skin cut in half, with thin ivory nerve fibres branching just beneath it",
             " except the bump, which is soft terracotta red", None),
            ("Ce n'est pas un manque d'hygiène : cette bactérie vit aussi sur les peaux les plus nettes.",
             "two identical smooth cubes of skin side by side, both with a few tiny soft terracotta dots scattered on their top "
             "surfaces", " except the tiny dots, which are soft terracotta", None),
            ("Frotter plus fort ne l'élimine pas. Ça irrite, et ça entretient l'inflammation.",
             "a stiff scrubbing brush hovering above a cube of skin whose top surface has one small red bump",
             " except the small bump, which is soft terracotta red", None),
            ("Un bouton rouge fait moins de 5 millimètres. Plus gros et plus profond, on parle de nodule.",
             "a cube of skin cut in half showing a small shallow red bump near the surface and, deeper below, a larger round red "
             "swelling", " except the bump and the swelling, which are soft terracotta red", ("5", "mm", "5")),
            ("Ce qui aide, c'est un actif qui détruit la bactérie sans créer de résistance, comme le peroxyde de benzoyle.",
             "a cube of skin with one small bump on its top surface, a cluster of small bubbles hovering just above it",
             " except the bump, which is soft terracotta red", None),
            ("Ce n'est pas une question d'hygiène. C'est une alerte qui s'allume.", None, "", None),
            ("Le bouton rouge, c'est le troisième. Il en reste cinq. Pour enfin tous les comprendre, abonne-toi.", None, "", None),
        ],
        chain={3: 2, 4: 3, 5: 4, 7: 6, 13: 1},  # 13: the opening bump comes back as the "alert" of the closing line
        motion={
            1: "The swollen terracotta bump pulses slowly like a heartbeat, its soft red glow brightening and dimming. The camera "
               "does not move.",
            3: "Tiny soft terracotta dots appear inside the sealed ivory plug and slowly multiply. The camera does not move.",
            4: "The tiny terracotta dots keep multiplying and the plug slowly swells, stretching the wall of the follicle. The "
               "camera does not move.",
            5: "The wall of the follicle under the surface splits along a thin line that lights up soft terracotta red, and a "
               "little honey-gold oil and a few tiny dots leak out into the surrounding skin. The camera does not move.",
            6: "Many tiny round pure white cells stream in through the channels from both sides and gather around the torn "
               "follicle. The camera does not move.",
            7: "The thin channels widen and glow soft terracotta red, and the surface above the follicle slowly swells into a "
               "low round red bump. The camera does not move.",
            10: "The brush scrubs back and forth over the surface, and the skin around the bump slowly turns redder and "
                "irritated. The camera does not move.",
            12: "The small bubbles slowly sink onto the bump and burst, and the bump's red colour slowly fades as it shrinks a "
                "little. The camera does not move.",
        },
        anim=[1, 3, 4, 5, 6, 7, 10, 12],
        fx={9: "sweep"},
        music=dict(
            style=["dark cinematic investigative documentary score", "serious, grave and tense, like a true-crime TV documentary",
                   "minor key", "pulsing low synth bass", "sparse deep percussion hits", "felt piano motif",
                   "tense string ostinato", "clear and present sound, not muffled", "wide dynamics with builds and drops",
                   "instrumental", "100 BPM"],
            sections=[(0, "Cold open", ["low mysterious drone", "ticking clock-like pulse", "single grave piano notes"]),
                      (2, "Investigation", ["low pulsing bass enters", "tense string ostinato", "steady and serious"]),
                      (3, "Tension", ["darker harmony", "rising tension", "sub bass swells"]),
                      (5, "Revelation", ["a deep impact hit at the start", "grave descending piano motif", "suspense"]),
                      (6, "Danger", ["darkest and most intense part", "heartbeat-like kick", "dissonant strings", "building up"]),
                      (9, "Breath", ["stripped back", "a single sustained low note", "quiet tension"]),
                      (12, "The answer", ["determined steady pulse returns", "still serious", "strings rise with a hint of resolve"]),
                      (13, "Final word", ["one last deep impact hit", "then a dark sustained drone", "grave"])]),
        caption=(
            "Les boutons expliqués · Partie 3 : Le bouton rouge\n\n"
            "Le bouton rouge : ce n'est pas une question d'hygiène, c'est une alerte qui s'allume.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Le bouton rouge s'appelle une « papule » : une lésion inflammatoire, en relief, de moins de 5 mm. Plus grosse et "
            "plus profonde, on parle de nodule (Zaenglein et al., Journal of the American Academy of Dermatology, 2016).\n\n"
            "La bactérie en cause, Cutibacterium acnes, vit sur la peau de presque tout le monde. Elle prolifère dans le "
            "bouchon, pauvre en oxygène et riche en sébum (Dréno et al., JEADV, 2018).\n\n"
            "L'inflammation commence parfois avant même que la paroi du pore ne cède (Jeremy et al., Journal of Investigative "
            "Dermatology, 2003).\n\n"
            "Rougeur, chaleur, gonflement, douleur : ce sont les signes classiques d'une réaction de défense, pas d'une saleté. "
            "Frotter ou décaper irrite la peau et entretient l'inflammation.\n\n"
            "Le peroxyde de benzoyle tue la bactérie sans créer de résistance, contrairement aux antibiotiques utilisés seuls "
            "(Zaenglein et al., 2016).\n\n"
            "#boutonrouge #acne #acneadulte #peau #skincare"),
    ),
    "E04_tete_blanche": dict(
        chapter=1,
        series="Les boutons expliqués",
        part="Partie 4 : La tête blanche",
        voice="Despina:reportage_cta",
        lines=[
            ("Les boutons expliqués. Partie 4. La tête blanche.", None, "", None),
            ("Une tête blanche ne veut pas dire que ton bouton est prêt à être percé.",
             "a cube of skin with one swollen bump on its top surface, topped by a small white head",
             RED + ", and its small head, which is white", None),
            ("Au départ, c'est un bouton rouge : une inflammation autour d'un pore bouché.", "reused from E03", "", None),
            ("Pour le combattre, ton corps envoie des globules blancs, par milliers.", "reused from E03", "", None),
            ("En se battant, ils meurent, et s'accumulent juste sous la surface. Ce blanc, c'est ça : le pus.", None, "", None),
            ("La tête blanche, c'est la partie visible de ce combat. Mais l'inflammation, elle, est plus bas.", None, "", None),
            ("Si tu presses, une partie du pus sort. L'autre est poussée vers le fond.",
             "a cube of skin cut in half showing a swollen bump topped by a small white head with a small white pocket under "
             "it, and two thick ivory clay arrows on both sides of the bump pointing inward toward it",
             RED + ", and the head and the pocket under it, which are white", None),
            ("La paroi se déchire sous la peau, et l'inflammation s'étale.", None, "", None),
            ("Résultat : un bouton plus gros, qui dure plus longtemps, et un risque de marque.",
             "a cube of skin with one large round swollen bump on its top surface and, next to it, one flat round spot",
             RED + ", and the flat spot, which is warm brown", None),
            ("Laissée tranquille, une tête blanche s'assèche, et se résorbe en quelques jours.", None, "", None),
            ("Un patch peut aider : il protège le bouton, et empêche tes doigts d'y toucher.",
             "a small round thin translucent patch hovering just above a cube of skin with one swollen bump topped by a small "
             "white head", RED + ", and its small head, which is white", None),
            ("Et si elles reviennent par dizaines, un dermatologue peut traiter ce qui les fabrique.",
             "a gently curved block of skin with many small swollen bumps scattered on its top surface, each topped by a tiny "
             "white head", " except the bumps, which are soft terracotta red, and their tiny heads, which are white", None),
            ("Ce n'est pas un signal pour percer. C'est ton corps qui fait le ménage.", None, "", None),
            ("La tête blanche, c'est la quatrième. Il en reste quatre. Pour enfin tous les comprendre, abonne-toi.", None, "", None),
        ],
        # 2: E03's pulsing red bump; 3: E03's white cells streaming to the torn follicle (both with their clips, free)
        reuse={2: ("E03_bouton_rouge", 1, True), 3: ("E03_bouton_rouge", 6, True)},
        chain={4: 3, 5: 4, 7: 6, 9: 1, 12: 3},  # 12: the white cells again, "ton corps qui fait le ménage"
        motion={
            1: "The small white head on top of the terracotta bump glows brighter and dimmer, slowly, like a warning light. "
               "Nothing else changes. The camera does not move.",
            4: "The tiny white cells slowly crowd together and rise to the top of the follicle, forming a small white pocket "
               "right under the surface, which bulges into a small white head on top of the skin. The camera does not move.",
            6: "The two clay arrows slowly push inward against the bump: a tiny white drop escapes at the top, while the white "
               "pocket is pushed downward and the wall below splits along a thin line that lights up soft terracotta red. The "
               "camera does not move.",
            7: "Soft terracotta red slowly spreads outward from the split wall into the surrounding skin, and the bump on top "
               "grows wider and redder. The camera does not move.",
            9: "The small white head slowly flattens and disappears, and the terracotta bump slowly shrinks and fades toward "
               "the ivory of the skin. The camera does not move.",
            10: "The thin translucent patch slowly descends and settles flat over the bump, covering it completely. The camera "
                "does not move.",
        },
        anim=[1, 4, 6, 7, 9, 10],
        clip_end={7: 0.6, 10: 0.8},  # 7: the whole cube ends up red; 10: the patch melts at the end
        fx={5: "sweep", 8: "sweep"},
        music=score((0, "Cold open"), (2, "Investigation"), (4, "Revelation"), (6, "Danger"), (9, "Breath"),
                    (10, "The answer"), (12, "Final word")),
        caption=(
            "Les boutons expliqués · Partie 4 : La tête blanche\n\n"
            "La tête blanche : ce n'est pas un signal pour percer, c'est ton corps qui fait le ménage.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Un bouton à tête blanche s'appelle une « pustule » : une lésion inflammatoire dont le sommet contient du pus, "
            "c'est-à-dire des globules blancs (des neutrophiles) venus combattre la bactérie (Zaenglein et al., Journal of "
            "the American Academy of Dermatology, 2016).\n\n"
            "Le pus n'est que la partie visible : l'inflammation entoure le follicule plus en profondeur. Presser pousse une "
            "partie du contenu vers le bas, peut rompre la paroi et étendre l'inflammation dans le derme.\n\n"
            "Plus une acné est inflammatoire et sévère, plus le risque de marque et de cicatrice augmente (Tan et al., Journal "
            "of Drugs in Dermatology, 2017).\n\n"
            "Les patchs hydrocolloïdes absorbent le liquide et protègent la lésion ; surtout, ils évitent d'y toucher (Chao et "
            "al., Journal of Cosmetic Science, 2006).\n\n"
            "Quand les pustules sont nombreuses ou reviennent sans cesse, un traitement de fond prescrit par un dermatologue "
            "agit sur leur cause.\n\n"
            "#pustule #acne #acneadulte #peau #skincare"),
    ),
    "E05_bouton_sous_la_peau": dict(
        chapter=1,
        series="Les boutons expliqués",
        part="Partie 5 : Le bouton sous la peau",
        voice="Despina:reportage_cta",
        lines=[
            ("Les boutons expliqués. Partie 5. Le bouton sous la peau.", None, "", None),
            ("Celui qui fait mal, qui gonfle, et qui ne sort jamais.",
             "a cube of skin with one broad, low, rounded swelling on its top surface, smooth, with no head",
             " except the swelling, which is soft terracotta red", None),
            ("Il ne naît pas à la surface, mais dans le derme, la couche profonde de la peau.",
             "a solid cube of skin whose front face is cut open like an anatomy model, showing a thin top layer and a thick "
             "lower layer; buried deep in the lower layer, one large round swelling; the top surface of the cube above it is "
             "perfectly smooth and flat, in one piece", " except the swelling, which is soft terracotta red", None),
            ("Au départ, c'est le même scénario : un pore bouché, une bactérie qui se multiplie.", "reused from E03", "", None),
            ("Mais ici, la paroi cède tout au fond du pore.", "reused from E03", "", None),
            ("L'inflammation s'étale en profondeur, là où il n'y a aucune sortie.", None, "", None),
            ("Ça forme une boule dure, de plus de 5 millimètres, qui peut durer des semaines.", None, "", ("5", "mm", "5")),
            ("Elle appuie sur les nerfs. C'est pour ça qu'elle fait mal, même sans tête.", "reused from E03", "", None),
            ("La presser ne sert à rien : il n'y a rien à faire sortir.",
             "a cube of skin with one broad, low, rounded swelling on its top surface, and two thick ivory clay arrows on both "
             "sides of it, pointing inward toward it", " except the swelling, which is soft terracotta red", None),
            ("Tu enfonces l'inflammation, et tu abîmes le collagène, le filet qui soutient ta peau.",
             "a cube of skin cut in half showing one large deep round swelling surrounded by a dense mesh of thin ivory fibres",
             " except the swelling, which is soft terracotta red", None),
            ("C'est ce bouton-là qui laisse le plus souvent des cicatrices en creux.",
             "a cube of skin with one small rounded crater on its top surface", "", None),
            ("Ce qui soulage : de la glace, enveloppée dans un tissu, quelques minutes.",
             "an ice cube wrapped in a folded soft cloth resting next to a cube of skin with one broad, low, rounded swelling on "
             "its top surface", " except the swelling, which is soft terracotta red", None),
            ("Et s'il revient souvent, un dermatologue a des traitements qui agissent en profondeur.",
             "a solid cube of skin whose front face is cut open like an anatomy model, showing a thin top layer and a thick "
             "lower layer; deep in the lower layer, only one tiny faint pale spot remains; the top surface is smooth and flat, "
             "in one piece", " except the tiny spot, which is pale soft terracotta", None),
            ("Il ne refuse pas de sortir. Il est trop profond pour sortir.", None, "", None),
            ("Le bouton sous la peau, c'est le cinquième. Il en reste trois. Pour enfin tous les comprendre, abonne-toi.",
             None, "", None),
        ],
        # 3-4: E03's plug where the bacteria multiply, then its wall splitting (with clips); 7: E03's nerves under a bump
        reuse={3: ("E03_bouton_rouge", 3, True), 4: ("E03_bouton_rouge", 5, True), 7: ("E03_bouton_rouge", 8, False)},
        chain={5: 4, 6: 2, 13: 2},
        motion={
            1: "The broad red swelling pulses slowly like a heartbeat, its soft red glow brightening and dimming. The camera "
               "does not move.",
            2: "The deep round swelling slowly grows larger and glows a deeper terracotta red, while the surface above stays "
               "smooth and intact. The camera does not move.",
            5: "Soft terracotta red slowly spreads deep into the lower layer of the skin, forming one large round red swelling "
               "far below the intact surface. The camera does not move.",
            8: "The two clay arrows slowly push inward against the swelling; nothing comes out, and the swelling turns a deeper "
               "red and spreads wider. The camera does not move.",
            9: "The thin ivory fibres right around the red swelling slowly loosen, break apart and fade away, leaving an empty "
               "gap around it. The camera does not move.",
            11: "The red swelling slowly softens, flattens a little and its red colour fades. The camera does not move.",
        },
        anim=[1, 2, 5, 8, 9],  # 11 (ice) stays still: Grok turned the bump into dripping red jelly
        clip_end={5: 0.3, 8: 0.55},  # both end as a giant glossy red ball
        fx={7: "sweep", 10: "sweep", 12: "sweep"},
        music=score((0, "Cold open"), (2, "Investigation"), (4, "Tension"), (6, "Revelation"), (8, "Danger"),
                    (11, "Breath"), (12, "The answer"), (13, "Final word")),
        caption=(
            "Les boutons expliqués · Partie 5 : Le bouton sous la peau\n\n"
            "Le bouton sous la peau : il ne refuse pas de sortir, il est trop profond pour sortir.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Un bouton profond, dur et douloureux, de plus de 5 mm, s'appelle un « nodule » (Zaenglein et al., Journal of the "
            "American Academy of Dermatology, 2016). On parle souvent de « kyste », mais la plupart ne contiennent pas de "
            "vraie poche.\n\n"
            "L'inflammation se situe dans le derme, loin sous la surface : il n'y a pas d'ouverture par où la vider. La "
            "presser l'enfonce davantage et abîme le tissu.\n\n"
            "Ce sont les lésions qui laissent le plus de cicatrices : l'inflammation profonde détruit une partie du collagène "
            "(Zaenglein et al., 2016).\n\n"
            "Pour calmer la douleur et le gonflement, l'American Academy of Dermatology conseille de la glace enveloppée "
            "dans un linge, quelques minutes.\n\n"
            "Quand ces boutons reviennent, il existe des traitements de fond, et parfois une injection de cortisone pour un "
            "nodule isolé : ils se discutent avec un dermatologue.\n\n"
            "#boutonsouslapeau #acne #acneadulte #peau #skincare"),
    ),
    "E06_faux_points_noirs": dict(
        chapter=1,
        series="Les boutons expliqués",
        part="Partie 6 : Les faux points noirs",
        voice="Despina:reportage_cta",
        lines=[
            ("Les boutons expliqués. Partie 6. Les faux points noirs.", None, "", None),
            ("Ces petits points gris sur ton nez ne sont pas des points noirs.",
             "a large stylised human nose seen from three-quarter view, its tip and the wings beside the nostrils smooth and "
             "clean, with no dots yet", "", None),
            ("Ce sont des filaments sébacés. Et tout le monde en a.",
             "a single enlarged skin pore seen in cross-section in a cube of skin, lined from the bottom to the opening with a "
             "thin soft column of pale grey oil", "", None),
            ("Chaque pore est relié à une glande qui fabrique du sébum, l'huile de ta peau.", "reused from E01", "", None),
            ("Ce sébum remonte le long du poil, et tapisse le pore, comme un petit tube.", "reused from E01", "", None),
            ("Sur le visage, il y a jusqu'à 900 glandes par centimètre carré. Le pore se remplit en permanence.",
             "the top surface of a block of skin seen at a low angle, with many tiny evenly spaced flat pale grey dots",
             " except the tiny dots, which are pale grey", ("900", "/cm²", "900")),
            ("Un vrai point noir est un bouchon dur et bombé, qui obstrue le pore. Le filament, lui, est souple et plat.",
             "a block of skin cut in half showing two pores side by side: on the left a pore lined with a thin soft column of "
             "pale grey oil, on the right a pore completely filled with a solid rounded plug whose top is black",
             " except the right plug top, which is black", None),
            ("Si tu le presses, il sort un petit ver beige. Le pore paraît vide.",
             "a cube of skin cut in half showing one pore lined with a thin soft column of pale grey oil, and two thick ivory "
             "clay arrows on both sides of the pore opening, pointing inward toward it", "", None),
            ("Mais il se remplit à nouveau en quelques semaines : c'est son rôle.", None, "", None),
            ("À force de presser, tu irrites ta peau, et tu risques de l'abîmer.",
             "a smooth gently curved porcelain skin surface with a few visible pores, the skin around them slightly reddened "
             "and irritated", " except the reddened areas, which are soft terracotta", None),
            ("Pour les rendre moins visibles : l'acide salicylique, qui entre dans le pore, ou les rétinoïdes.",
             "a dropper bottle hovering above a large stylised human nose seen from three-quarter view, with many tiny evenly "
             "spaced flat pale grey dots on its tip and wings", " except the tiny dots, which are pale grey", None),
            ("Ils ne disparaîtront jamais complètement. Ta peau a besoin de son sébum.", None, "", None),
            ("Ce n'est pas un défaut. C'est ta peau qui fonctionne.", None, "", None),
            ("Les faux points noirs, c'est le sixième. Il en reste deux. Pour enfin tous les comprendre, abonne-toi.",
             None, "", None),
        ],
        # 3-4: E01's gland filling with golden sebum, then the sebum rising along the hair (with clips)
        reuse={3: ("E01_point_noir", 2, True), 4: ("E01_point_noir", 3, True)},
        chain={8: 7, 11: 10, 12: 2},
        motion={
            1: "Many tiny evenly spaced flat pale grey dots slowly appear one after another on the tip and the wings of the "
               "nose, all the same size. The camera does not move.",
            7: "The two clay arrows slowly push inward, and a thin soft pale beige string of oil slowly squeezes up out of the "
               "pore opening, leaving the pore empty. The camera does not move.",
            8: "The pale beige string fades away, and the empty pore slowly fills up again from the bottom with a thin soft "
               "column of pale grey oil. The camera does not move.",
            10: "A single clear drop falls from the dropper onto the nose, and the tiny pale grey dots slowly become fainter, "
                "without disappearing completely. The camera does not move.",
        },
        anim=[1, 7, 8, 10],
        clip_end={1: 0.6, 7: 0.5, 8: 0.7, 10: 0.6},  # 1: dots end as polka dots; 7: the string runs off screen; 10: drips
        fx={5: "sweep", 6: "sweep", 9: "sweep"},
        music=score((0, "Cold open"), (2, "Investigation"), (5, "Tension"), (7, "Revelation"), (9, "Danger"),
                    (10, "The answer"), (12, "Final word")),
        caption=(
            "Les boutons expliqués · Partie 6 : Les faux points noirs\n\n"
            "Les faux points noirs : ce n'est pas un défaut, c'est ta peau qui fonctionne.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Les petits points gris ou beiges du nez sont le plus souvent des filaments sébacés : du sébum et des cellules qui "
            "tapissent normalement le canal du follicule. Ils sont plats, réguliers, et reviennent même quand on les vide.\n\n"
            "Un vrai point noir (comédon ouvert) est un bouchon compact qui obstrue et dilate le pore, avec un sommet "
            "foncé.\n\n"
            "Le visage est l'une des zones les plus riches en glandes sébacées : de 400 à 900 par centimètre carré (Thody et "
            "Shuster, Physiological Reviews, 1989).\n\n"
            "Vider un filament ne sert à rien : le canal se remplit à nouveau en quelques semaines. Presser souvent irrite la "
            "peau.\n\n"
            "L'acide salicylique, soluble dans le gras, et les rétinoïdes peuvent les rendre moins visibles, sans les faire "
            "disparaître.\n\n"
            "#pointsnoirs #acne #acneadulte #peau #skincare"),
    ),
    "E07_marque_brune": dict(
        chapter=1,
        series="Les boutons expliqués",
        part="Partie 7 : La marque brune",
        voice="Despina:reportage_cta",
        lines=[
            ("Les boutons expliqués. Partie 7. La marque brune.", None, "", None),
            ("Le bouton est parti depuis des semaines. Mais la marque, elle, est toujours là.", "reused from E03", "", None),
            ("Ce n'est pas une cicatrice : la peau n'est pas creusée. C'est de la couleur.", None, "", None),
            ("Pendant l'inflammation, des signaux chimiques réveillent les mélanocytes, les cellules qui fabriquent le pigment.",
             "a cube of skin cut in half showing thin stacked layers, with a row of small star-shaped cells with thin branches "
             "along the base of the top layer", "", None),
            ("Elles en produisent trop, et ce pigment reste piégé dans la peau.", None, "", None),
            ("Plus ta peau est mate ou foncée, plus elle marque fort, et longtemps.",
             "three cubes of skin side by side, each with one flat round darker spot on its top surface",
             " except the cubes, which go from light ivory on the left to medium beige to deep brown porcelain on the right, "
             "and their spots, which are a darker brown than their cube", None),
            ("Seule, elle s'estompe, souvent en 6 à 12 mois. Plus profonde, elle peut durer des années.",
             "a cube of skin with one flat round warm brown spot on its top surface, next to a small stack of thin porcelain "
             "calendar pages", " except the spot, which is warm brown", ("12", "mois", "12")),
            ("Son pire ennemi, c'est le soleil.",
             "a stylised porcelain sun glowing softly above a cube of skin with one flat round warm brown spot on its top "
             "surface", " except the sun, which is warm honey-gold, and the spot, which is warm brown", None),
            ("Les UV relancent la fabrication de pigment : la marque fonce, et dure plus longtemps.", None, "", None),
            ("Une crème solaire chaque matin, même l'hiver, raccourcit vraiment sa durée.",
             "a small tube of sunscreen standing next to a cube of skin with one flat round warm brown spot on its top surface",
             " except the spot, which is warm brown", None),
            ("Certains actifs l'accélèrent : l'acide azélaïque, la niacinamide, les rétinoïdes.",
             "a dropper bottle hovering above a cube of skin with one flat round warm brown spot on its top surface",
             " except the spot, which is warm brown", None),
            ("Ce n'est pas une cicatrice. C'est une trace qui s'efface.", None, "", None),
            ("La marque brune, c'est la septième. Il en reste une. Pour enfin tous les comprendre, abonne-toi.", None, "", None),
        ],
        reuse={1: ("E03_bouton_rouge", 1, False)},  # E03's red bump: here it flattens into the brown mark
        chain={2: 1, 4: 3, 8: 7, 11: 10},
        motion={
            1: "The round red bump slowly flattens into the surface and leaves in its place one flat round warm brown spot. "
               "The camera does not move.",
            3: "The small star-shaped cells slowly turn warm brown and release tiny warm brown granules around them. The "
               "camera does not move.",
            4: "The tiny warm brown granules slowly drift upward and gather in the layers just under the surface, forming a "
               "brown patch. The camera does not move.",
            6: "The calendar pages slowly flip one after another, and the brown spot slowly becomes fainter. The camera does "
               "not move.",
            7: "Soft rays of warm light fall from the sun onto the cube, and the brown spot slowly darkens. The camera does "
               "not move.",
            9: "A thin translucent glossy veil slowly spreads over the whole top surface of the cube. The camera does not move.",
            10: "A single clear drop falls from the dropper onto the brown spot, and the spot slowly lightens. The camera does "
                "not move.",
        },
        anim=[1, 3, 4, 6, 7, 9, 10],
        clip_end={7: 0.6, 9: 0.5},  # 7: the sun itself turns brown; 9: the veil ends as a draped cloth
        fx={2: "sweep", 5: "sweep", 8: "sweep"},
        music=score((0, "Cold open"), (2, "Investigation"), (3, "Tension"), (7, "Danger"), (9, "The answer"),
                    (11, "Final word")),
        caption=(
            "Les boutons expliqués · Partie 7 : La marque brune\n\n"
            "La marque brune : ce n'est pas une cicatrice, c'est une trace qui s'efface.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "La tache qui reste après un bouton s'appelle une hyperpigmentation post-inflammatoire : l'inflammation stimule "
            "les mélanocytes, qui produisent trop de mélanine. La peau n'est pas creusée : c'est de la couleur.\n\n"
            "Elle est plus fréquente et plus intense sur les peaux mates à foncées (Davis et Callender, Journal of Clinical "
            "and Aesthetic Dermatology, 2010).\n\n"
            "Sans traitement, elle s'estompe souvent en 6 à 12 mois ; un pigment plus profond, dans le derme, peut persister "
            "des années.\n\n"
            "Les UV relancent la production de mélanine : une protection solaire quotidienne est la base de tout traitement "
            "des taches.\n\n"
            "L'acide azélaïque, la niacinamide et les rétinoïdes peuvent accélérer leur disparition (Davis et Callender, "
            "2010).\n\n"
            "#marquesacne #acne #acneadulte #peau #skincare"),
    ),
    "E08_cicatrice_en_creux": dict(
        chapter=1,
        series="Les boutons expliqués",
        part="Partie 8 : La cicatrice en creux",
        voice="Despina:reportage_cta",
        lines=[
            ("Les boutons expliqués. Partie 8. La cicatrice en creux.", None, "", None),
            ("Une cicatrice en creux, ce n'est pas le bouton qui est resté. C'est de la peau qui manque.",
             "a cube of skin with one small rounded crater on its top surface", "", None),
            ("Sous la surface, ta peau tient grâce à un filet de fibres : le collagène.",
             "a cube of skin cut in half showing, inside its thick middle layer, a dense even mesh of thin ivory fibres under a "
             "smooth surface", "", None),
            ("Quand l'inflammation est profonde, comme dans un nodule, elle détruit une partie de ce filet.", "reused from E05",
             "", None),
            ("En réparant, la peau ne reconstruit pas tout. La surface s'affaisse.", None, "", None),
            ("Et le creux reste, même quand la rougeur est partie.", None, "", None),
            ("Chez les personnes qui consultent pour de l'acné, 43 % ont des cicatrices.",
             "ten small smooth cubes of skin arranged in two neat rows of five", "", ("43", "%", "43")),
            ("Il en existe trois formes : en pic à glace, en cuvette, et en caisson.",
             "three cubes of skin cut in half side by side: the first with a narrow deep V-shaped pit in its surface, the "
             "second with a wide shallow rounded dip, the third with a box-shaped depression with sharp vertical edges", "", None),
            ("Ce qui augmente le risque : une acné sévère, traitée tard, et des boutons manipulés.",
             "a cube of skin with one large round swollen bump on its top surface, and a small porcelain hourglass standing "
             "next to it", RED, None),
            ("Les crèmes ne comblent pas un creux. La peau seule non plus.",
             "a small open jar of thick cream standing next to a cube of skin with one small rounded crater on its top surface",
             "", None),
            ("Ce qui marche se fait en cabinet : laser, microneedling, peelings. Le but : relancer le collagène.",
             "a cube of skin cut in half showing a small rounded crater on its surface and, beneath it, a sparse mesh of thin "
             "ivory fibres, with a fine beam of soft light touching the crater from above",
             " except the beam, which is soft warm honey-gold light", None),
            ("Ça améliore, souvent nettement. Mais rarement à cent pour cent.", None, "", None),
            ("La meilleure arme, c'est d'éviter le creux : traiter tôt, et ne pas percer.", None, "", None),
            ("La peau n'a pas gardé le bouton. Elle n'a pas pu tout reconstruire.", None, "", None),
            ("La cicatrice en creux, c'est la dernière. Le chapitre suivant parle de tes hormones. Pour ne pas le rater, "
             "abonne-toi.", None, "", None),
        ],
        reuse={3: ("E05_bouton_sous_la_peau", 9, True)},  # E05's collagen mesh breaking around the deep swelling
        chain={4: 3, 5: 4, 11: 10, 12: 2, 13: 1},
        motion={
            4: "The red swelling slowly fades away, and the smooth top surface above the empty gap slowly sinks into a small "
               "rounded crater. The camera does not move.",
            6: "One after another, four of the ten cubes slowly sink a small rounded crater into their top surface; the other "
               "six stay smooth. The camera does not move.",
            8: "The sand in the hourglass slowly runs down while the red bump slowly grows larger and redder. The camera does "
               "not move.",
            10: "Under the crater, new thin ivory fibres slowly grow and weave into the mesh, and the crater slowly becomes a "
                "little shallower. The camera does not move.",
        },
        anim=[4, 6, 8, 10],
        clip_end={6: 0.45},  # 4 cubes out of 10 cratered, like the 43 %; later Grok craters them all
        fx={1: "sweep", 5: "sweep", 7: "sweep", 9: "sweep"},
        music=score((0, "Cold open"), (2, "Investigation"), (3, "Danger"), (6, "Revelation"), (9, "Breath"),
                    (10, "The answer"), (13, "Final word")),
        caption=(
            "Les boutons expliqués · Partie 8 : La cicatrice en creux\n\n"
            "La cicatrice en creux : la peau n'a pas gardé le bouton, elle n'a pas pu tout reconstruire.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Une cicatrice atrophique (en creux) apparaît quand une inflammation profonde détruit une partie du collagène du "
            "derme : en se réparant, la peau n'en reconstruit pas assez, et la surface s'affaisse.\n\n"
            "Chez les patients qui consultent un dermatologue pour de l'acné, 43 % ont des cicatrices ; le premier facteur de "
            "risque est la sévérité de l'acné (Tan et al., Journal of Drugs in Dermatology, 2017).\n\n"
            "On distingue trois formes : en pic à glace (étroite et profonde), en cuvette (large et arrondie) et en caisson "
            "(bords nets) (Jacob et al., Journal of the American Academy of Dermatology, 2001).\n\n"
            "Les crèmes ne comblent pas un creux. Les techniques qui relancent le collagène se font en cabinet : lasers, "
            "microneedling, peelings, souvent combinés. Elles améliorent, souvent nettement, rarement à 100 %.\n\n"
            "La meilleure prévention : traiter tôt une acné inflammatoire, et ne pas manipuler les boutons.\n\n"
            "#cicatriceacne #acne #acneadulte #peau #skincare"),
    ),
}
