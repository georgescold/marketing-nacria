"""Organs account videos (same format and pipeline as episodes.py, art direction « scanner » from plan_organes.py).

Each line: (text, scene prompt of its FIRST frame, extra colour instructions, counter). The scene prompt describes the
hologram anatomy; plan_organes.SCENE makes the highlighted part glow in the chapter colour, or in e["glow"][i].
Organs-only keys:
- keys: words drawn in alert yellow in the subtitles (the carousels' « Si tu as un bouton sur le [Menton] »)
- ring: {i: (x, y, r[, delay])}: the carousels' dotted yellow ring drawn around a zone (x, y fractions of the frame, r px)
- fx "scan": a cold scanner line runs down the still scene
- photo: lines that show the spot itself, photographed on real skin (plan_organes.PHOTO), never a glowing ball
Tone: alarmist hooks, true answers; a myth is only a hook that the video breaks. No diagnosis: signs -> a doctor.
"""
from episodes import SECTION

# same investigative score as the acne account, darker and more clinical
SCAN_MUSIC = ["dark cinematic medical thriller documentary score", "serious, grave and tense, like an investigative TV documentary",
              "minor key", "pulsing low synth bass", "a faint heartbeat-monitor-like pulse", "sparse deep percussion hits",
              "cold glassy synth textures", "tense string ostinato", "clear and present sound, not muffled",
              "wide dynamics with builds and drops", "instrumental", "100 BPM"]


def score(*starts):
    return dict(style=SCAN_MUSIC, sections=[(i, name, SECTION[name]) for i, name in starts])


HEAD = "a translucent female head and neck seen from the front, eyes closed, calm expression"
PINK = "hot pink-red (#FF2E7E)"  # reproductive organs, like chapter 2
GOLDEN = "intense golden amber (#FFB020)"  # sebum
ONLY = (" Only the small bumps glow, with very faint thin veins around them; the brain, the eyes and the rest of "
        "the head do not glow.")  # realistic everyday case: a few bumps, nothing else lit (user, 2026-10-15)
# dotted ring around the real spot on each episode's photograph (x, y fractions of the frame, radius px), measured on the
# generated images
RING_O01, RING_O02, RING_O03 = (0.432, 0.497, 100), (0.561, 0.507, 125), (0.5, 0.469, 115)
RING_O04, RING_O05, RING_O06 = (0.477, 0.481, 100), (0.526, 0.534, 100), (0.483, 0.43, 100)
RING_O07, RING_O08 = (0.427, 0.527, 140), (0.476, 0.557, 120)  # O07: around the cluster of small bumps
# pauses of the validated organs voice: room for the drama at the punctuation, never inside a sentence
ORGAN_CAPS = {"?": 0.7, "!": 0.6, ".": 0.6, "…": 0.7, ":": 0.5, ";": 0.5, ",": 0.35}

EPISODES = {
    # 2026-10-15, after the user's review of O01-O03 (« au niveau de la dynamique / émotion c'est très bien »), for all
    # three: (1) the hook hits harder, in the text and on screen: the video opens on the question itself, written huge
    # over a macro photo of the real spot (open="question", as on the nutrition account), no spoken series title first;
    # (2) « le bouton rouge = boule rouge, ce n'est pas du tout réel »: every line that shows the spot is a photograph of
    # real skin (`photo`, plan_organes.PHOTO, like the top half of the carousels), the hologram stays for the organs and
    # the mechanisms; (3) « le test : … » sounded mechanical: the advice is said naturally, and no two videos share it;
    # (4) one steady voice (fluid). Earlier versions in compte organes/vidéo/<episode>/_v*/ and _archives/.
    "O01_menton": dict(
        chapter=1,
        series="Ce que tes boutons disent de ton corps",
        part="Partie 1 : Le menton",
        # v4 (2026-10-15), the user: the v3 « ambiance ne donne pas envie de rester », the opening « pas hyper fluide »,
        # « c'était mieux avant ». What v2 had and v3 lost, and what v3 fixed, both kept:
        # - the opening is an alarming statement written huge on the photo of the real spot (not a neutral question, which
        #   also repeated the next line); then short beats, one idea each: frustration, « pas un hasard », the signal;
        # - the v2 voice instruction (dramatic pause before each revelation), pauses kept up to 0.45 s between words;
        # - motion on every photo in code (scanner line, light sweep, push-in to the spot), free;
        # - kept from v3: real spots, no « le test », no allusion to another video, clean subtitles, no audio cut.
        voice="Despina:reportage_suspense",
        open="question",  # the opening card (a statement here)
        fluid=True,
        wpm=(185, 215),
        caps={"?": 0.7, "!": 0.6, ".": 0.6, "…": 0.7, ":": 0.5, ";": 0.5, ",": 0.35},  # suspense: room for the drama
        word_cap=0.3,  # no pause over 0.3 s inside a sentence (user, on O01 v4: « parfois des pauses dans la voix »)
        target_wpm=200,  # a slow take gets its pauses tightened up to 200 wpm, as on v2 (210): never its speech
        takes=2,  # the intonation changes from take to take: the one that never rises at the end of a statement
        lines=[
            # the hook: a disturbing question that points at the problem and worries (user, 2026-10-15, on v4)
            ("Ce bouton qui revient sans cesse sur ton menton, tu sais ce qu'il cache vraiment ?",
             "a tight close-up of a woman's lower face, from just under the nose to the top of the neck, lips relaxed and "
             "closed, lit from one side; on the chin, a little off-centre, one inflamed red bump under the skin, slightly "
             "swollen, without a white head, and one small older red mark beside it", "", None),
            ("Tu as beau changer de crème, rien n'y fait.",
             "a close-up of a woman's lower face, her fingertip dabbing a small amount of white cream onto a red "
             "spot on her chin, the skin around it slightly reddened", "", None),
            ("Et ce n'est pas un hasard : ton corps essaie de te dire quelque chose.", None, "", None),
            ("Le coupable : les androgènes. Des hormones que ton corps fabrique chaque jour.",
             "a translucent female torso and pelvis seen from the front, with the two ovaries low in the pelvis and the two "
             "small adrenal glands on top of the kidneys glowing", "", None),
            ("Elles voyagent dans ton sang, jusqu'à ta peau.", None, "", None),
            ("Là, elles font gonfler tes glandes à sébum. Et le pore se bouche.",
             "a translucent cube of skin cut in half showing one hair follicle with one small oil gland attached to its side, "
             "the oil gland glowing", "", None),
            ("Et ce n'est pas le pire : chaque mois, ton cycle les relance.",
             "a translucent uterus floating at the centre of a thin holographic ring divided into 28 small segments", "", None),
            ("44 % des femmes qui ont de l'acné la voient flamber juste avant leurs règles.",
             "a tight close-up of a woman's chin and lips, lit from one side; on the chin, two inflamed red bumps close to "
             "each other, one of them with a tiny white head", "", ("44", "%", "44")),
            ("Le plus injuste ? Ça peut commencer après 25 ans, même si tu n'as jamais eu un bouton ado.",
             "a translucent holographic hourglass, its sand glowing as it falls", "", None),
            ("Et plus tu t'acharnes sur ton menton, plus il s'enflamme. Parce que le signal vient de l'intérieur.",
             "a close-up of a woman's lower face, her two index fingers pressing on both sides of a red spot on her chin to "
             "squeeze it, the skin around the spot reddened and irritated", "", None),
            # never point to another video, never leave a loop open (user, 2026-10-15)
            ("Si en plus tes règles sont irrégulières, ne laisse pas passer : parles-en à un médecin. Ce duo peut signaler "
             "un déséquilibre hormonal, et ça se traite.", "a translucent ovary with a ring of many small round follicles "
             "inside it, the follicles glowing", "", None),
            ("Un dermatologue peut proposer des traitements qui agissent sur ce signal.",
             f"{HEAD}, only the chin glowing faintly", "", None),
            ("Ton menton n'est pas sale : il suit ton cycle.", None, "", None),
            ("Le menton, c'est la première zone, et il en reste sept : pour décoder tout ton visage, abonne-toi.", None, "", None),
        ],
        photo=[0, 1, 7, 9],
        glow={3: PINK, 5: GOLDEN, 6: PINK, 10: PINK},
        chain={2: 1, 4: 3, 12: 0},
        motion={
            4: "The ovaries and the adrenal glands pulse with light, and tiny glowing particles rise from them and stream "
               "upward through the blood vessels. The camera does not move.",
            5: "The oil gland slowly swells and fills with glowing golden oil, which rises up along the follicle toward the "
               "surface. The camera does not move.",
            6: "A bright point of light travels clockwise around the thin ring, like the hand of a clock, and the last quarter "
               "of the ring flares intense red as it passes. The camera does not move.",
            8: "The glowing red sand falls steadily through the hourglass, the lower half slowly filling. The camera does not "
               "move.",
            11: "The faint red glow on the chin slowly fades away and turns into a calm soft blue. The camera does not move.",
        },
        anim=[4, 5, 6, 8, 11],
        clip_end={5: 0.6},  # the cube ends as a pool of oil
        fx={1: "sweep", 2: "scan", 3: "scan", 7: "sweep", 9: "scan", 12: "scan"},  # every still moves
        zoom={0: 0.08, 1: 0.05, 2: 0.05, 7: 0.06, 9: 0.06, 12: 0.06},  # a slow push toward the spot
        ring={0: RING_O01, 10: (0.5, 0.5, 250), 12: RING_O01 + (0.6,)},  # measured on the photographs
        keys=["menton", "crème", "hasard", "androgènes", "sang", "sébum", "pire", "cycle", "règles", "44", "%",
              "flamber", "injuste", "25", "ans", "s'enflamme", "l'intérieur", "médecin", "déséquilibre", "traite",
              "dermatologue", "sale", "abonne-toi"],
        music=score((0, "Tension"), (3, "Investigation"), (6, "Danger"), (8, "Revelation"), (10, "Danger"),
                    (11, "The answer"), (12, "Final word")),
        caption=(
            "Ce que tes boutons disent de ton corps · Partie 1 : Le menton\n\n"
            "Le menton : il n'est pas sale, il suit ton cycle.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Chez la femme adulte, l'acné touche souvent le bas du visage (menton, mâchoire), même si d'autres zones sont "
            "fréquemment atteintes aussi (Dréno et al., JEADV, 2015). Elle peut apparaître après 25 ans chez des femmes qui "
            "n'en avaient jamais eu : on parle d'acné tardive.\n\n"
            "Les androgènes, comme la testostérone, sont produits chaque jour par toutes les femmes. Ils stimulent les "
            "glandes sébacées, qui fabriquent plus de sébum (Elsaie, Clinical, Cosmetic and Investigational Dermatology, "
            "2016).\n\n"
            "44 % des femmes qui ont de l'acné décrivent une poussée dans les jours qui précèdent les règles (Stoll et al., "
            "Archives of Dermatology, 2001).\n\n"
            "Percer ou frotter n'agit pas sur cette cause et peut aggraver l'inflammation. Les traitements qui agissent sur la "
            "composante hormonale se discutent avec un dermatologue. Des règles irrégulières associées à de l'acné méritent "
            "un avis médical : elles peuvent signaler un déséquilibre hormonal, qui se traite.\n\n"
            "#acnehormonale #acne #acneadulte #peau #menton"),
    ),
    "O02_machoire": dict(
        chapter=1,
        series="Ce que tes boutons disent de ton corps",
        part="Partie 2 : La mâchoire",
        voice="Despina:reportage_suspense",
        open="question",
        fluid=True,
        wpm=(185, 215),
        caps={"?": 0.7, "!": 0.6, ".": 0.6, "…": 0.7, ":": 0.5, ";": 0.5, ",": 0.35},  # suspense: room for the drama
        word_cap=0.3,  # no pause over 0.3 s inside a sentence (user, on O01 v4: « parfois des pauses dans la voix »)
        target_wpm=200,  # a slow take gets its pauses tightened up to 200 wpm, as on v2 (210): never its speech
        takes=2,  # the intonation changes from take to take: the one that never rises at the end of a statement
        # no spoiler: the phone, the pillow and the hands on the cheeks belong to « Les joues », 23 touches an hour to
        # « Les mains » (chapter 4); the hormonal lower face was « Le menton »
        lines=[
            # v4: the O01 v4 recipe; the hook as a disturbing question that points at the problem (user, 2026-10-15)
            ("Ces boutons toujours du même côté de ta mâchoire… et si c'était toi qui les provoquais ?",
             "a tight close-up of the side of a woman's lower face in three-quarter view, from the ear to the chin, the "
             "jawline sharp; along the jawline on this side, a short line of three small inflamed red bumps, one of them "
             "with a tiny white head", "", None),
            ("Regarde bien : ce côté-là, tu l'abîmes chaque jour, sans même t'en rendre compte.", None, "", None),
            ("Les dermatologues ont un nom pour ça : l'acné mécanique.",
             "a translucent cube of skin cut in half showing one hair follicle, a flat translucent plate pressing down on its "
             "top surface, the follicle glowing", "", None),
            ("Quand quelque chose appuie, frotte ou couvre ta peau pendant des heures, la chaleur monte.", None, "", None),
            ("Le sébum s'étale, les cellules mortes s'écrasent dans le pore, et il se bouche.", None, "", None),
            ("Et le coupable, c'est souvent… ta propre main.",
             "a single translucent hand hologram seen from the front, palm facing the viewer, the palm glowing", "", None),
            ("Ta mâchoire posée dans ta paume, des heures, devant un écran ou en réunion.",
             "a woman resting her jaw in the palm of her hand, close-up of the lower half of her face and her hand, the cold "
             "blue light of a laptop screen on her skin, one small inflamed red bump on the jawline just above her fingers",
             "", None),
            ("Pendant le Covid, les dermatologues ont même inventé un mot : le « maskne ».",
             "a translucent female head seen from the front wearing a translucent face mask over the mouth and chin, the skin "
             "under the mask glowing", "", None),
            ("Écharpe, col roulé, sangle de casque : tout ce qui frotte au même endroit laisse sa trace.",
             "a translucent female head and neck in three-quarter view with a translucent scarf wrapped around the neck and a "
             "thin helmet strap along the jaw, glowing friction lines where they touch the skin", "", None),
            ("Et plus tu frottes pour nettoyer, plus tu entretiens l'inflammation.",
             "a translucent female head in three-quarter view with a translucent scrubbing brush pressed against one side of "
             "the jaw, the skin under the brush glowing", "", None),
            ("Repère ce côté, et pendant quelques semaines, ne laisse plus rien l'écraser. Ni ta main, ni ton col.",
             "the same tight close-up of the side of a woman's lower face in three-quarter view, the jawline sharp; along the "
             "jawline, three small faded pink marks, the skin calmer and healing", "", None),
            ("Ce n'est pas ta peau qui lâche : c'est ce qui l'écrase.", None, "", None),
            ("La mâchoire, c'est la deuxième zone, et il en reste six : pour décoder tout ton visage, abonne-toi.", None, "",
             None),
        ],
        photo=[0, 6, 10],
        chain={1: 0, 3: 2, 4: 3, 11: 0},
        motion={
            2: "The translucent plate slowly presses down on the skin, and the follicle beneath glows brighter and redder. "
               "The camera does not move.",
            3: "Waves of red heat slowly rise through the skin under the plate, glowing brighter. The camera does not move.",
            4: "A glowing plug slowly forms inside the follicle and fills it up to the surface. The camera does not move.",
            5: "The glowing palm pulses brighter and brighter, like an alarm light. The camera does not move.",
            7: "The red glow slowly spreads across the skin under the mask, brighter along its edges. The camera does not "
               "move.",
            9: "The brush scrubs back and forth, and the red patch under it grows wider and brighter. The camera does not "
               "move.",
        },
        anim=[2, 3, 4, 5, 7, 9],
        clip_end={7: 0.55, 9: 0.6},  # 7: the glow ends up flooding the whole neck; 9: the patch ends as a big red blob
        fx={1: "scan", 6: "sweep", 8: "scan", 10: "sweep", 11: "scan"},  # every still moves
        zoom={0: 0.08, 1: 0.05, 6: 0.05, 10: 0.05, 11: 0.06},  # a slow push toward the spot
        ring={0: RING_O02, 11: RING_O02 + (0.6,)},  # measured on the photographs
        keys=["mâchoire", "côté", "l'abîmes", "mécanique", "chaleur", "bouche", "main", "paume", "maskne", "frotte",
              "trace", "inflammation", "l'écraser", "l'écrase", "provoquais", "abonne-toi"],
        music=score((0, "Tension"), (2, "Revelation"), (3, "Investigation"), (5, "Danger"), (7, "Revelation"),
                    (9, "Danger"), (10, "The answer"), (11, "Final word")),
        caption=(
            "Ce que tes boutons disent de ton corps · Partie 2 : La mâchoire\n\n"
            "La mâchoire : ce n'est pas ta peau qui lâche, c'est ce qui l'écrase.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "L'acné mécanique est déclenchée ou aggravée par la pression, le frottement, la chaleur et l'occlusion répétés "
            "sur la peau : sangles, mentonnières, cols, appuis prolongés (Mills et Kligman, Archives of Dermatology, "
            "1975).\n\n"
            "Le port prolongé du masque pendant la pandémie de Covid-19 a fait décrire une forme d'acné sous et autour du "
            "masque, surnommée « maskne » par les dermatologues.\n\n"
            "Un indice : les boutons se concentrent du côté et à l'endroit exacts de la pression, et s'améliorent quand on "
            "la supprime.\n\n"
            "Frotter ou gommer pour « nettoyer » irrite la peau et entretient l'inflammation.\n\n"
            "#acnemecanique #acne #acneadulte #peau #machoire"),
    ),
    "O03_front": dict(
        chapter=1,
        series="Ce que tes boutons disent de ton corps",
        part="Partie 3 : Le front",
        voice="Despina:reportage_suspense",
        open="question",
        fluid=True,
        wpm=(185, 215),
        caps={"?": 0.7, "!": 0.6, ".": 0.6, "…": 0.7, ":": 0.5, ";": 0.5, ",": 0.35},  # suspense: room for the drama
        word_cap=0.3,  # no pause over 0.3 s inside a sentence (user, on O01 v4: « parfois des pauses dans la voix »)
        target_wpm=200,  # a slow take gets its pauses tightened up to 200 wpm, as on v2 (210): never its speech
        takes=2,  # the intonation changes from take to take: the one that never rises at the end of a statement
        # no spoiler: the gut-skin axis is its own episode (chapter 3): only the face-map claim (forehead = digestion) is
        # debunked here; the T-zone and sebum density belong to « Entre les sourcils »
        lines=[
            # the hook: already a disturbing question that points at the problem (kept in v4)
            ("Des boutons sur le front ? Et si ton intestin essayait de te prévenir ?",
             "a tight close-up of a woman's forehead and hairline seen slightly from the side, the eyebrows at the bottom of "
             "the frame, the hair pulled back; on one side of the forehead, off-centre near the hairline, one small inflamed "
             "red bump with a tiny white head, and a few tiny skin-coloured bumps around it", "", None),
            ("C'est ce que répètent des milliers de vidéos : le front, ce serait la digestion.",
             "a translucent female torso seen from the front with the intestines glowing", "", None),
            ("Cette idée vient d'une vieille carte du visage, venue de la médecine traditionnelle chinoise.",
             "a translucent female face seen from the front, covered by a faint glowing grid that divides it into zones",
             "", None),
            ("Mais aucune étude n'a jamais montré que les boutons du front viennent de ton intestin.", None, "", None),
            ("Alors, d'où viennent-ils ? Regarde un peu plus haut.",
             "a close-up of a woman's forehead with a straight fringe of hair falling on it, the eyebrows at the bottom of "
             "the frame; just under the fringe, one small inflamed red bump and a few tiny skin-coloured bumps", "", None),
            ("Tes cheveux : leur sébum, et surtout ce que tu mets dessus.", None, "", None),
            ("Huiles, cires, crèmes coiffantes : en coulant sur ta peau, elles bouchent les pores. Les dermatologues "
             "appellent ça l'acné des pommades.",
             "a translucent female head in profile, a glossy glowing drop of hair oil at the hairline just above the "
             "forehead", "", None),
            ("Et ta frange, collée au front toute la journée, garde la chaleur et le gras contre ta peau.",
             "an extreme close-up of a heavy fringe of hair lying flat against the skin of the forehead, a slight sheen of "
             "oil and sweat on the skin just under the strands, one small inflamed red bump half hidden under the fringe",
             "", None),
            ("Ce n'est pas tout : casquette, bandeau de sport, casque…",
             "a close-up of a woman's forehead under the band of a baseball cap, the edge of the cap pressing across the top "
             "of the forehead, a faint red line where it presses, and one small inflamed red bump just under the band", "",
             None),
            ("La sueur reste coincée dessous, ça frotte, et le pore se bouche.",
             "a translucent cube of skin cut in half showing one hair follicle under a flat translucent plate, the follicle "
             "glowing", "", None),
            ("Essaie d'attacher tes cheveux et de changer de produit coiffant. Dans quelques semaines, ton front te dira si "
             "c'était ça.",
             "a close-up of a woman's forehead and hairline, her hair tied back cleanly, smooth calm skin with only one small "
             "faded pink mark near the hairline", "", None),
            ("Ce n'est pas ton ventre : c'est ce qui touche ton front.", None, "", None),
            ("Le front, c'est la troisième zone, et il en reste cinq : pour décoder tout ton visage, abonne-toi.", None, "",
             None),
        ],
        photo=[0, 4, 7, 8, 10],  # 7 was a hologram cube with a glowing red sphere: read as the « boule rouge » again
        glow={1: "fiery orange (#FF7A1A)"},
        chain={3: 1, 5: 4, 11: 0},
        reuse={9: ("O02_machoire", 4, True)},  # the pore that blocks under pressure: the same mechanism as the jaw
        motion={
            1: "The intestines pulse with light, and thin glowing threads rise from them toward the top of the frame. The "
               "camera does not move.",
            3: "The thin glowing threads rising from the intestines slowly break apart and fade away. The camera does not "
               "move.",
            6: "The glossy glowing drop slowly slides down from the hairline onto the forehead, leaving a glowing trail. The "
               "camera does not move.",
        },
        anim=[1, 3, 6],
        fx={2: "scan", 4: "sweep", 5: "scan", 7: "sweep", 8: "scan", 10: "sweep", 11: "scan"},  # every still moves
        zoom={0: 0.08, 4: 0.05, 5: 0.05, 7: 0.05, 8: 0.05, 10: 0.05, 11: 0.06},  # a slow push toward the spot
        ring={0: RING_O03, 11: RING_O03 + (0.6,)},  # measured on the photographs
        keys=["front", "intestin", "digestion", "carte", "aucune", "cheveux", "dessus", "pommades", "frange", "chaleur",
              "gras", "casquette", "sueur", "bouche", "attacher", "ventre", "abonne-toi"],
        music=score((0, "Tension"), (1, "Investigation"), (3, "Revelation"), (4, "Tension"), (6, "Danger"),
                    (10, "The answer"), (11, "Final word")),
        caption=(
            "Ce que tes boutons disent de ton corps · Partie 3 : Le front\n\n"
            "Le front : ce n'est pas ton ventre, c'est ce qui touche ton front.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Les « cartes du visage » qui relient chaque zone à un organe viennent de traditions anciennes. Aucune étude "
            "n'a montré que les boutons du front signalent un problème digestif.\n\n"
            "Les produits capillaires gras (huiles, cires, crèmes coiffantes) peuvent provoquer de petits boutons sur le "
            "front et la ligne des cheveux : c'est l'« acné des pommades » (Plewig et al., Archives of Dermatology, "
            "1970).\n\n"
            "La frange, la casquette, le bandeau ou le casque ajoutent chaleur, sueur et frottement au même endroit : une "
            "forme d'acné mécanique.\n\n"
            "Si les boutons suivent la ligne des cheveux ou de la casquette, la piste est d'abord là.\n\n"
            "#acnefront #acne #acneadulte #peau #cheveux"),
    ),
    # ---- chapter 1, parts 4-8 (2026-10-15): the validated O01-O03 v5 recipe (user: « vraiment bien pour absolument
    # tout »). Hook = a disturbing question on the photo of the real spot, worded differently every time; short relaunches
    # joined with « : »; every loop closed in the video; no allusion to another video; no spoiler (the hands and the
    # screens belong to chapter 4, the toothpaste and the liver myth in general to chapter 5, the SOPK in depth to 2.4)
    "O04_nez": dict(
        chapter=1,
        series="Ce que tes boutons disent de ton corps",
        part="Partie 4 : Le nez",
        voice="Despina:reportage_suspense",
        open="question",
        fluid=True,
        wpm=(185, 215),
        caps=ORGAN_CAPS,
        word_cap=0.3,
        target_wpm=200,
        takes=2,
        lines=[
            ("Ce bouton sur ton nez… et si c'était ton cœur qui tirait la sonnette d'alarme ?",
             "a tight close-up of a woman's nose, lit from one side, the lips out of the frame; on the rounded tip of the "
             "nose, slightly to one side, one inflamed red bump", "", None),
            ("C'est ce que répètent des milliers de vidéos : le nez serait le miroir du cœur.",
             "a translucent female torso seen from the front, the heart glowing softly in the chest, no blood vessels drawn "
             "outside the chest", "", None),
            ("Sauf que ton cœur, lui, n'a jamais fait pousser un seul bouton.", None, "", None),
            ("La vraie raison est juste sous ta peau : regarde de plus près.",
             "an extreme close-up of the skin on the side of a woman's nose, wide visible pores, a slight sheen of oil, one "
             "small red bump among them", "", None),
            ("Ton nez concentre les pores les plus larges et les plus nombreux de ton visage.", None, "", None),
            ("Et chacun cache une glande à sébum : plusieurs centaines par centimètre carré.",
             "a translucent cube of skin cut in half showing many hair follicles side by side, each with a small oil gland "
             "glowing", "", None),
            ("Plus de sébum, des pores plus larges : c'est le terrain parfait pour qu'ils se bouchent.",
             "a translucent cube of skin with three wide pores on its top surface, the middle pore plugged by a column of "
             "glowing golden sebum reaching up to the surface, no sphere, no ball", "", None),
            ("Et ce n'est pas tout : tes lunettes appuient chaque jour au même endroit.",
             "a close-up of a woman wearing glasses, the nose pad of the glasses resting on the side of her nose, one small "
             "inflamed red bump just under the nose pad", "", None),
            ("La pression, la chaleur, le frottement : il n'en faut pas plus pour enflammer un pore.", None, "", None),
            ("Le pire réflexe, c'est de presser : l'inflammation descend encore plus profond.",
             "a close-up of a woman's nose, two fingertips pressing on both sides of a red bump on the side of the nose, "
             "the skin around it reddened", "", None),
            ("Alors laisse-le tranquille, et choisis des soins qui ne bouchent pas les pores : on dit non comédogènes.",
             "a close-up of a woman's nose and cheek, calm skin, only one small faded pink mark on the side of the nose",
             "", None),
            ("Ton nez ne parle pas de ton cœur : il parle de tes pores.", None, "", None),
            ("Le nez, c'est la quatrième zone, et il en reste quatre : pour décoder tout ton visage, abonne-toi.", None, "",
             None),
        ],
        photo=[0, 3, 7, 9, 10],
        glow={5: GOLDEN, 6: GOLDEN},
        chain={2: 1, 4: 3, 8: 7, 11: 0},
        motion={
            1: "The heart glows and pulses slowly like an alarm light, brighter and dimmer. Nothing else changes. The camera "
               "does not move.",
            5: "The small oil glands slowly fill with glowing golden oil, which rises along the follicles toward the surface. "
               "The camera does not move.",
            6: "A glowing golden plug slowly forms inside the middle pore and fills it up to the surface. The camera does not "
               "move.",
        },
        anim=[1, 5, 6],
        fx={2: "scan", 3: "sweep", 4: "scan", 7: "sweep", 8: "scan", 9: "sweep", 10: "sweep", 11: "scan"},
        zoom={0: 0.08, 3: 0.06, 4: 0.06, 7: 0.05, 8: 0.05, 9: 0.05, 10: 0.05, 11: 0.06},
        ring={0: RING_O04, 11: RING_O04 + (0.6,)},
        keys=["nez", "cœur", "sonnette", "jamais", "pores", "larges", "nombreux", "sébum", "centaines", "bouchent",
              "lunettes", "enflammer", "presser", "profond", "comédogènes", "abonne-toi"],
        music=score((0, "Tension"), (1, "Investigation"), (3, "Revelation"), (5, "Investigation"), (7, "Danger"),
                    (9, "Danger"), (10, "The answer"), (11, "Final word")),
        caption=(
            "Ce que tes boutons disent de ton corps · Partie 4 : Le nez\n\n"
            "Le nez ne parle pas de ton cœur : il parle de tes pores.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Les « cartes du visage » qui relient le nez au cœur viennent de traditions anciennes. Aucune étude ne relie un "
            "bouton sur le nez à un problème cardiaque.\n\n"
            "Le visage compte plusieurs centaines de glandes sébacées par centimètre carré, bien plus que le reste du corps, "
            "et le nez fait partie des zones les plus riches. Plus une zone produit de sébum, plus ses pores sont larges "
            "(Roh et al., British Journal of Dermatology, 2006).\n\n"
            "Les plaquettes des lunettes appuient, chauffent et frottent toujours au même endroit : une forme d'acné "
            "mécanique.\n\n"
            "Presser un bouton pousse l'inflammation plus profond et augmente le risque de marque. Les produits « non "
            "comédogènes » sont formulés pour ne pas boucher les pores.\n\n"
            "#acnenez #acne #acneadulte #peau #pores"),
    ),
    "O05_joues": dict(
        chapter=1,
        series="Ce que tes boutons disent de ton corps",
        part="Partie 5 : Les joues",
        voice="Despina:reportage_suspense",
        open="question",
        fluid=True,
        wpm=(185, 215),
        caps=ORGAN_CAPS,
        word_cap=0.3,
        target_wpm=200,
        takes=2,
        lines=[
            ("Ces boutons sur tes joues… et si c'étaient tes poumons qui s'encrassaient ?",
             "a tight close-up of a woman's cheek and the corner of her eye, lit from one side; on the upper cheek, one "
             "inflamed red bump, and lower on the cheek one small faded pink mark, not aligned", "", None),
            ("Pollution, fumée, poumons fatigués : sur les réseaux, ta joue serait leur miroir.",
             "a translucent female torso seen from the front, the two lungs glowing softly, no other organ glowing", "", None),
            ("La médecine n'a jamais trouvé ce lien : le vrai coupable, tu le touches chaque jour.", None, "", None),
            ("Ton téléphone, collé contre ta joue à chaque appel.",
             "a close-up of a woman holding a smartphone pressed against her cheek during a call, one small inflamed red "
             "bump on the cheek just next to the phone", "", None),
            ("L'écran garde le gras de ta peau, la chaleur monte, et tout s'écrase dans tes pores.",
             "a translucent cube of skin seen from slightly above, a translucent smartphone lying pressed flat on its top "
             "surface, the top layer of skin under the phone glowing red; no human figure, no organ, no body inside the cube",
             "", None),
            ("Et la nuit, ça continue : ta joue passe des heures contre ta taie d'oreiller.",
             "a woman sleeping on her side, close-up of her cheek resting on a white pillowcase in dim blue night light, one "
             "small inflamed red bump on the cheek", "", None),
            ("Une taie gardée une semaine accumule sébum, cellules mortes et restes de tes produits pour cheveux.",
             "a translucent hologram of a rectangular bed pillow seen from above at an angle, tiny glowing specks of oil "
             "and dust scattered across its fabric; no heart, no organ, no human figure", "", None),
            ("Et c'est souvent la même joue : celle sur laquelle tu dors, celle où tu téléphones.", None, "", None),
            ("Ajoute un pinceau de maquillage jamais lavé, et les bactéries d'hier repassent sur ta peau d'aujourd'hui.",
             "a close-up of a makeup brush with powder sweeping across a woman's cheek, one small red bump on the cheek",
             "", None),
            ("Change ta taie plus souvent, nettoie l'écran de ton téléphone, lave tes pinceaux : c'est souvent là que tout se "
             "joue.", "a close-up of a woman's cheek, calm skin, only one small faded pink mark", "", None),
            ("Ce ne sont pas tes poumons qui s'affichent sur ta joue : c'est ce qui la touche, jour et nuit.", None, "",
             None),
            ("Les joues, c'est la cinquième zone, et il en reste trois : pour décoder tout ton visage, abonne-toi.", None, "",
             None),
        ],
        photo=[0, 3, 5, 8, 9],
        chain={2: 1, 7: 5, 10: 0},
        motion={
            1: "The two lungs glow and slowly dim, like a slow breath, brighter and darker. Nothing else changes. The camera "
               "does not move.",
            4: "The phone presses a little harder against the skin and the glow under it grows warmer and redder. The camera "
               "does not move.",
            6: "The tiny glowing particles on the pillow slowly brighten and multiply. The camera does not move.",
        },
        anim=[1, 4, 6],
        fx={2: "scan", 3: "sweep", 5: "sweep", 7: "scan", 8: "sweep", 9: "sweep", 10: "scan"},
        zoom={0: 0.08, 3: 0.05, 5: 0.05, 7: 0.06, 8: 0.05, 9: 0.05, 10: 0.06},
        ring={0: RING_O05, 10: RING_O05 + (0.6,)},
        keys=["joues", "poumons", "encrassaient", "lien", "touches", "téléphone", "gras", "chaleur", "taie", "sébum",
              "même", "pinceau", "bactéries", "lave", "touche", "abonne-toi"],
        music=score((0, "Tension"), (1, "Investigation"), (3, "Revelation"), (5, "Danger"), (7, "Revelation"),
                    (9, "The answer"), (10, "Final word")),
        caption=(
            "Ce que tes boutons disent de ton corps · Partie 5 : Les joues\n\n"
            "Ce ne sont pas tes poumons qui s'affichent sur ta joue : c'est ce qui la touche, jour et nuit.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Aucune étude ne relie les boutons des joues aux poumons : ce lien vient des « cartes du visage » "
            "traditionnelles.\n\n"
            "Le téléphone, la taie d'oreiller et les pinceaux de maquillage frottent, chauffent et déposent sébum, cellules "
            "mortes et résidus de produits au même endroit : une forme d'acné mécanique, souvent d'un seul côté.\n\n"
            "Changer de taie plus souvent, nettoyer l'écran du téléphone et laver ses pinceaux sont des gestes simples "
            "conseillés par les dermatologues.\n\n"
            "#acnejoues #acne #acneadulte #peau #taiedoreiller"),
    ),
    "O06_sourcils": dict(
        chapter=1,
        series="Ce que tes boutons disent de ton corps",
        part="Partie 6 : Entre les sourcils",
        voice="Despina:reportage_suspense",
        open="question",
        fluid=True,
        wpm=(185, 215),
        caps=ORGAN_CAPS,
        word_cap=0.3,
        target_wpm=200,
        takes=2,
        lines=[
            ("Ce bouton pile entre tes sourcils… et si c'était ton foie qui saturait ?",
             "a tight close-up of a woman's eyebrows and the top of her nose, lit from one side; exactly between the "
             "eyebrows, one inflamed red bump", "", None),
            ("Trop d'alcool, trop de gras, un foie fatigué : c'est l'explication qu'on lit partout.",
             "a translucent female torso seen from the front, the liver glowing softly on the right side of the abdomen, no "
             "other organ glowing", "", None),
            ("Sauf que cette petite zone a ses propres raisons de s'enflammer.", None, "", None),
            ("C'est le début de ta zone T, la bande du front, du nez et du menton où ta peau fabrique le plus de sébum.",
             "a translucent female face seen from the front, a soft glow shaped like the letter T: its horizontal bar runs "
             "across the upper forehead, high above the eyebrows, and its vertical stem runs down the middle of the nose; "
             "nothing else glowing, no cross", "", None),
            ("Et cette zone-là, tu la travailles souvent… à la pince à épiler.",
             "a close-up of a woman's eyebrows with a pair of tweezers held near one eyebrow, the skin between the eyebrows "
             "slightly reddened", "", None),
            ("Chaque poil arraché laisse un petit orifice ouvert : une porte d'entrée pour les bactéries.",
             "a translucent cube of skin with one hair being pulled out of its follicle, the open follicle glowing", "", None),
            ("Et le poil qui repousse peut se recourber sous la peau, et former un bouton qui ne part pas.",
             "a translucent cube of skin with one thin dark hair curled back and trapped just under the surface, a faint "
             "reddish glow along the hair only; no sphere, no ball, no orb", "", None),
            ("Ajoute la cire, les gels et les crayons à sourcils qui restent toute la journée sur la peau.",
             "a close-up of a woman's eyebrow being shaped with an eyebrow pencil, a small red bump between the eyebrows",
             "", None),
            ("Désinfecte ta pince, épile après la douche, et laisse la zone tranquille quelques jours.",
             "a close-up of a woman's eyebrows, calm skin between them, only one small faded pink mark", "", None),
            ("Ce n'est pas ton foie qui parle : c'est ta zone T, et ta pince.", None, "", None),
            ("Entre les sourcils, c'est la sixième zone, et il en reste deux : pour décoder tout ton visage, abonne-toi.",
             None, "", None),
        ],
        photo=[0, 4, 7, 8],
        glow={1: "deep amber red (#E0482B)"},
        chain={2: 1, 9: 0},
        motion={
            1: "The liver glows and pulses slowly like an alarm light, brighter and dimmer. Nothing else changes. The camera "
               "does not move.",
            5: "The hair slides out of its follicle and the empty opening glows brighter and redder. The camera does not "
               "move.",
            6: "The curled hair glows and the skin around it slowly swells and reddens into a small bump. The camera does "
               "not move.",
        },
        anim=[1, 5, 6],
        fx={2: "scan", 3: "scan", 4: "sweep", 7: "sweep", 8: "sweep", 9: "scan"},
        zoom={0: 0.08, 4: 0.05, 7: 0.05, 8: 0.05, 9: 0.06},
        ring={0: RING_O06, 9: RING_O06 + (0.6,)},
        keys=["sourcils", "foie", "saturait", "partout", "zone", "sébum", "pince", "arraché", "bactéries", "recourber",
              "cire", "crayons", "désinfecte", "abonne-toi"],
        music=score((0, "Tension"), (1, "Investigation"), (3, "Revelation"), (4, "Danger"), (7, "Investigation"),
                    (8, "The answer"), (9, "Final word")),
        caption=(
            "Ce que tes boutons disent de ton corps · Partie 6 : Entre les sourcils\n\n"
            "Ce n'est pas ton foie qui parle : c'est ta zone T, et ta pince.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Aucune étude ne relie les boutons entre les sourcils au foie : ce lien vient des « cartes du visage » "
            "traditionnelles.\n\n"
            "La zone T (front, nez, menton) est la plus riche en glandes sébacées du visage.\n\n"
            "L'épilation à la pince peut irriter le follicule et favoriser une folliculite ou un poil incarné, qui "
            "ressemblent à des boutons. Une pince propre, une épilation sur peau chaude et propre, et du repos pour la zone "
            "limitent le risque.\n\n"
            "#acne #acneadulte #peau #sourcils #epilation"),
    ),
    "O07_bouche": dict(
        chapter=1,
        series="Ce que tes boutons disent de ton corps",
        part="Partie 7 : Autour de la bouche",
        voice="Despina:reportage_suspense",
        open="question",
        fluid=True,
        wpm=(185, 215),
        caps=ORGAN_CAPS,
        word_cap=0.3,
        target_wpm=200,
        takes=2,
        lines=[
            ("Ces petits boutons autour de ta bouche… et si ce n'était même pas de l'acné ?",
             "a tight close-up of a woman's mouth and chin, lit from one side; a few clusters of tiny red bumps and slightly "
             "flaky pink skin around the corners of the mouth and on the chin, with a thin band of clear skin right along "
             "the edge of the lips", "", None),
            ("Tu les traites comme des boutons… et ils s'étendent encore.", None, "", None),
            ("Ça porte un nom : la dermatite périorale.",
             "a translucent female face seen from the front, a soft diffuse red glow in a ring of skin around the mouth, the "
             "lips themselves not glowing", "", None),
            ("De tout petits boutons rouges, parfois des plaques qui pèlent, autour de la bouche, du nez ou des yeux.",
             "an extreme close-up of the skin beside a woman's mouth, tiny red bumps clustered together and slightly flaky "
             "pink skin", "", None),
            ("Avec un détail qui la trahit : une fine bande de peau intacte, juste au bord des lèvres.", None, "", None),
            ("Elle touche surtout les femmes, entre 16 et 45 ans.", None, "", None),
            ("Le plus fou ? Elle est souvent déclenchée par ce qu'on met pour la calmer.",
             "a close-up of a fingertip spreading a thick white cream next to a woman's mouth, the skin around it slightly "
             "red", "", None),
            ("Les crèmes trop riches, et surtout les crèmes à la cortisone : elles apaisent, puis tout revient en pire.",
             "a translucent tube of cream hologram lying on its side, a thin ribbon of glowing white cream coming out of its "
             "open nozzle; no sphere, no ball, no orb", "", None),
            ("Et les produits anti-acné trop agressifs peuvent encore l'irriter.",
             "a translucent cube of skin, its top surface irritated and glowing red", "", None),
            ("Avant de tartiner quoi que ce soit, montre-la à un médecin : elle se soigne, mais pas comme l'acné.",
             "a close-up of a woman's mouth and chin, calm skin, only a few faint pink marks near the corner of the mouth",
             "", None),
            ("Ce n'est pas de l'acné : c'est pour ça qu'elle résiste à tes crèmes.", None, "", None),
            ("Autour de la bouche, c'est la septième zone, et il en reste une : pour décoder tout ton visage, abonne-toi.",
             None, "", None),
        ],
        photo=[0, 3, 6, 9],
        chain={1: 0, 4: 3, 5: 3, 10: 0},
        motion={
            2: "The soft red glow around the mouth slowly spreads and brightens, the lips staying dark. The camera does not "
               "move.",
            7: "The tube of cream pulses with light, brighter and dimmer, like an alarm. The camera does not move.",
            8: "The red glow on the skin slowly spreads wider and grows brighter. The camera does not move.",
        },
        anim=[2, 7, 8],
        fx={1: "scan", 3: "sweep", 4: "scan", 5: "sweep", 6: "sweep", 9: "sweep", 10: "scan"},
        zoom={0: 0.08, 1: 0.05, 3: 0.06, 4: 0.06, 5: 0.05, 6: 0.05, 9: 0.05, 10: 0.06},
        ring={0: RING_O07, 10: RING_O07 + (0.6,)},
        keys=["bouche", "acné", "étendent", "dermatite", "périorale", "pèlent", "bande", "lèvres", "femmes", "16", "45",
              "déclenchée", "cortisone", "pire", "agressifs", "médecin", "résiste", "abonne-toi"],
        music=score((0, "Tension"), (1, "Danger"), (2, "Revelation"), (5, "Investigation"), (6, "Danger"),
                    (9, "The answer"), (10, "Final word")),
        caption=(
            "Ce que tes boutons disent de ton corps · Partie 7 : Autour de la bouche\n\n"
            "Ce n'est pas de l'acné : c'est pour ça qu'elle résiste à tes crèmes.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "La dermatite périorale donne de petites papules rouges, parfois des squames, autour de la bouche, du nez ou des "
            "yeux, en épargnant typiquement une fine bande de peau au bord des lèvres. Elle touche surtout les femmes de 16 à "
            "45 ans (Lipozenčić et Ljubojević, Clinics in Dermatology, 2011).\n\n"
            "Elle est souvent liée aux corticoïdes appliqués sur le visage, qui la calment puis l'aggravent à l'arrêt, et "
            "aux crèmes trop riches. Les produits irritants peuvent l'entretenir.\n\n"
            "Son traitement diffère de celui de l'acné : un avis médical est nécessaire. N'arrête pas un traitement prescrit "
            "sans en parler à ton médecin.\n\n"
            "#dermatiteperiorale #acne #peau #peausensible #acneadulte"),
    ),
    "O08_partout": dict(
        chapter=1,
        series="Ce que tes boutons disent de ton corps",
        part="Partie 8 : Partout à la fois",
        voice="Despina:reportage_suspense",
        open="question",
        fluid=True,
        wpm=(185, 215),
        caps=ORGAN_CAPS,
        word_cap=0.3,
        target_wpm=200,
        takes=2,
        lines=[
            ("Des boutons partout, des règles qui font n'importe quoi… et si ton corps sonnait l'alarme ?",
             "a close-up of a woman's face from the eyebrows to the chin, lit from one side, worried expression; a few "
             "inflamed red bumps spread across the chin, the jawline and one cheek, not covering the whole face", "", None),
            ("Quand l'acné s'installe sur tout le visage, ce n'est plus une question de zone.", None, "", None),
            ("Et quand d'autres signes s'ajoutent, il faut regarder ailleurs.",
             "a translucent female torso and pelvis seen from the front, with the two ovaries low in the pelvis and the two "
             "small adrenal glands on top of the kidneys glowing", "", None),
            ("Des règles irrégulières, ou qui disparaissent pendant des mois.",
             "a translucent uterus floating at the centre of a thin holographic ring divided into 28 small segments", "", None),
            ("Des poils qui poussent là où ils n'avaient jamais poussé : le menton, la lèvre, le ventre.",
             "a close-up of a woman's chin and jaw in side light, a few fine dark hairs growing on the chin, one small "
             "inflamed red bump nearby", "", None),
            ("Des cheveux qui tombent plus que d'habitude.",
             "a hairbrush lying on a dark wooden surface, many long loose brown hairs tangled in its bristles; no person, "
             "no face", "", None),
            ("Ensemble, ces signes portent un nom : le syndrome des ovaires polykystiques, le SOPK.",
             "a translucent ovary with a ring of many small round follicles inside it, the follicles glowing", "", None),
            ("Il touche environ une femme sur dix.", None, "", ("10", "% des femmes", "dix")),
            ("Le plus inquiétant ? Jusqu'à 70 % des femmes concernées ne le savent pas.", None, "", ("70", "%", "70")),
            ("Parce que, pris un par un, chaque signe paraît banal.", None, "", None),
            ("Si tu te reconnais, parles-en à un médecin : une prise de sang et une échographie suffisent souvent à faire le "
             "point.", "a close-up of a woman's face, calm, her skin calmer with only a few faded pink marks", "", None),
            ("Ça se prend en charge, et ton acné avec.", None, "", None),
            ("Ce n'est pas ta peau qui va mal : c'est un signal à faire vérifier.", None, "", None),
            ("Partout à la fois, c'était la dernière zone : pour décoder tout ce que ton corps te dit, abonne-toi.", None, "",
             None),
        ],
        photo=[0, 4, 5, 10],  # 4: on the hologram the chin hairs came out as a red blob: a real photo instead
        glow={2: PINK, 3: PINK, 6: PINK},
        reuse={2: ("O01_menton", 3, False), 3: ("O01_menton", 6, True), 6: ("O01_menton", 10, False)},
        chain={1: 0, 7: 6, 8: 6, 9: 0, 11: 10, 12: 0},
        motion={},
        anim=[],  # the cycle clip is reused from O01; every still moves in code
        fx={1: "scan", 2: "scan", 4: "sweep", 5: "sweep", 6: "scan", 7: "scan", 8: "scan", 9: "sweep", 10: "sweep",
            11: "sweep", 12: "scan"},
        zoom={0: 0.06, 1: 0.05, 4: 0.05, 5: 0.05, 9: 0.05, 10: 0.05, 11: 0.05, 12: 0.06},
        ring={0: RING_O08, 6: (0.5, 0.5, 250), 12: RING_O08 + (0.6,)},
        keys=["partout", "règles", "alarme", "zone", "ailleurs", "irrégulières", "poils", "cheveux", "SOPK", "10", "%",
              "70", "banal", "médecin", "échographie", "charge", "vérifier", "abonne-toi"],
        music=score((0, "Tension"), (2, "Investigation"), (6, "Revelation"), (8, "Danger"), (10, "The answer"),
                    (12, "Final word")),
        caption=(
            "Ce que tes boutons disent de ton corps · Partie 8 : Partout à la fois\n\n"
            "Ce n'est pas ta peau qui va mal : c'est un signal à faire vérifier.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Le syndrome des ovaires polykystiques (SOPK) touche environ 8 à 13 % des femmes en âge de procréer, et jusqu'à "
            "70 % des femmes concernées ne sont pas diagnostiquées (Organisation mondiale de la santé, 2023).\n\n"
            "Ses signes possibles : cycles irréguliers ou absents, acné persistante, pilosité excessive, chute de cheveux. "
            "Le diagnostic repose sur les signes, une prise de sang et souvent une échographie (recommandations "
            "internationales, Teede et al., 2023).\n\n"
            "Un seul de ces signes ne suffit pas : seul un médecin peut poser le diagnostic. La prise en charge existe, y "
            "compris pour l'acné.\n\n"
            "#sopk #acnehormonale #acne #acneadulte #santefeminine"),
    ),
}
