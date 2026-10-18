"""Nutrition account videos (same format and pipeline as episodes.py; art direction « food noir & verdict », plan_nutrition.py).

Persona: Margot, an AI character who speaks as « je » (voice Gemini Vindemiatrix, warm and grave), never claims a diploma
(« diététicien » is a protected title), AI label on every post, sources in every caption.
Each video ends its explanation on the evidence stamp (plan_nutrition.VERDICTS) before the follow CTA.
Tone: anti-guilt, never restriction, never weight loss; « associé à » for observational studies.
"""

from episodes import SECTION

# the investigative score of the other accounts, warmer: a food documentary that still sounds like an inquiry
FOOD_MUSIC = ["dark cinematic investigative documentary score", "serious and intriguing, like a food investigation on TV",
              "minor key", "warm felt piano motif", "plucked pizzicato strings", "pulsing low synth bass",
              "sparse deep percussion hits", "clear and present sound, not muffled", "wide dynamics with builds and drops",
              "instrumental", "100 BPM"]


def score(*starts):
    return dict(style=FOOD_MUSIC, sections=[(i, name, SECTION[name]) for i, name in starts])


MILK = "a tall clear glass of cold milk"

EPISODES = {
    # 2026-10-15, N01 v4 and N02 v2: the N03 format the user validated, for the whole chapter: open on the question the
    # video answers, written huge over its most striking visual; Margot says what the studies hold; a montage of this episode's own
    # studies (never other foods); the verdict answers the opening question, says what it rests on and writes the claim
    # on the stamp; the young voice in one steady pace (fluid). Same images and clips as before, renumbered. Previous
    # versions in compte nutrition/vidéo/N01_lait/_v3/, N02_sucre/_v1/ and _archives/.
    "N01_lait": dict(
        chapter=1,
        series="Les aliments qui donnent des boutons",
        part="Partie 1 : Le lait",
        # v5 (2026-10-15), the user: v4 « beaucoup moins naturel » than v3 (« superbe ») in suspense, reveals and hook,
        # and the study montage « défile trop vite ». Back to the v3 flow, with only what was asked since: the opening
        # question, Margot « spécialiste de la nutrition cutanée », a verdict that answers the question and says what it
        # rests on. No montage (the studies are told in the script), no clumsy connectors.
        open="question",
        voice="Erinome:nutri_jeune",
        fluid=True,
        lines=[
            ("Est-ce que le lait donne vraiment des boutons ?",
             f"{MILK} on a dark slate, the milk surface perfectly still", "", None),
            ("Un verre de lait par jour : 12 % de risque d'acné en plus.",
             "an empty tall clear glass on a dark slate, a thick stream of milk just starting to pour into it from above",
             "", ("12", "%", "12")),
            ("C'est ce que des chercheurs français ont mesuré, en suivant 24 452 adultes.",
             "dozens of small identical glasses of milk lined up in long neat rows on a dark slate, seen from a low angle, "
             "receding into the darkness", "", ("24 452", "adultes", "24")),
            # one sentence over two shots: alone, « Et ce n'est pas le pire. » and « Celui qu'on choisit… » were rushed
            # by the voice in every take (+25 to +60 %), « parfois un peu trop rapide » (user)
            ("Et ce n'est pas le pire : le lait le plus suspect, c'est l'écrémé,",
             "two tall glasses side by side on a dark slate: on the left creamy whole milk, on the right thinner, slightly "
             "bluish skimmed milk", "", None),
            ("celui qu'on choisit justement pour faire attention.", None, "", None),
            ("Moi c'est Margot, spécialiste de la nutrition cutanée. J'ai lu les grandes études sur le lait et la peau, et "
             "je vais te montrer ce qu'elles cachent.", "persona card", "", None),
            ("Le lait fait grimper deux hormones : l'insuline, et l'IGF-1, un signal de croissance.",
             f"{MILK} on a dark slate, a few tiny glowing golden particles hovering just above the milk surface",
             " The tiny particles glow soft gold.", None),
            ("Et tes glandes à sébum captent ce signal. Elles gonflent, et fabriquent plus d'huile.",
             "a small shallow glass bowl of glossy golden oil on a dark slate, a single drop of golden oil hanging just above "
             "it", "", None),
            ("Alors, le lait est coupable ? Pas si vite.",
             f"a large magnifying glass lying on a dark slate next to {MILK}", "", None),
            ("Des chercheurs danois ont refait l'enquête, dans les gènes de plus de 20 000 personnes.",
             f"{MILK} standing alone in the dark, calm, a soft pool of light around it", "", None),
            ("Et là, le lien disparaît. Complètement.",
             f"{MILK} filled to the brim, standing alone on a dark slate", "", None),
            ("Alors, qui a raison ? Un peu les deux : le lien existe, mais il est faible.", None, "", None),
            ("Donc, le lait donne-t-il des boutons ? Mon verdict : probablement, mais un peu seulement.", None, "", None),
            ("Le lait n'est pas un poison : c'est un facteur parmi d'autres.", None, "", None),  # was rushed x1.9 as two
            ("Le lait, c'est le premier accusé. Il en reste sept. Pour connaître tous les verdicts, abonne-toi.", None, "",
             None),
        ],
        cards={5: "persona"},
        chain={4: 3, 11: 10, 12: 0, 13: 9},  # 11: the glass the Danish study just emptied
        verdict=(12, "PROBABLE", "probablement", "le lait donne des boutons"),
        motion={
            0: "A splash of milk leaps up from the surface in slow motion and falls back into the glass, droplets glistening "
               "in the side light. The camera does not move.",
            1: "A thick stream of milk pours into the glass in slow motion and fills it up to the top. The camera does not "
               "move.",
            6: "The tiny glowing golden particles slowly rise from the milk and multiply, drifting upward like sparks. The "
               "camera does not move.",
            7: "The single drop of golden oil falls into the bowl in slow motion, sending soft glossy ripples across the oil. "
               "The camera does not move.",
            10: "The level of the milk slowly drops as if drained from below, until the glass is completely empty and clean. "
                "The camera does not move.",
        },
        anim=[0, 1, 6, 7, 10],
        clip_end={0: 0.7, 6: 0.6},  # 0: the milk ends up overflowing; 6: the particles end as a heart-shaped cloud
        fx={2: "sweep", 3: "sweep", 4: "sweep", 8: "sweep", 9: "sweep", 11: "sweep", 13: "sweep"},
        zoom={5: 0.09},  # Margot's card: a slow push-in keeps the energy
        keys=["lait", "12", "%", "24", "452", "pire", "écrémé", "Margot", "nutrition", "cutanée", "cachent", "insuline",
              "IGF-1", "sébum", "coupable", "disparaît", "complètement", "faible", "probablement", "peu", "poison",
              "verdicts", "abonne-toi"],
        music=score((0, "Revelation"), (1, "Tension"), (3, "Investigation"), (6, "Danger"), (8, "Breath"),
                    (9, "Investigation"), (10, "Revelation"), (12, "The answer"), (13, "Final word")),
        caption=(
            "Les aliments qui donnent des boutons · Partie 1 : Le lait\n\n"
            "Le lait : ce n'est pas un poison, c'est un facteur parmi d'autres.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Dans la cohorte française NutriNet-Santé (24 452 adultes), chaque verre de lait par jour est associé à un risque "
            "d'acné plus élevé (odds ratio 1,12), tout comme les boissons sucrées et les produits gras et sucrés. C'est une "
            "association, pas une preuve de cause (Penso et al., JAMA Dermatology, 2020).\n\n"
            "Dans les méta-analyses, l'association est modeste et plus nette pour le lait écrémé : OR 1,32 (Juhl et al., "
            "Nutrients, 2018) ; OR 1,82 (Aghasi et al., Clinical Nutrition, 2019).\n\n"
            "Une étude génétique (randomisation mendélienne) sur 20 416 adultes danois ne trouve aucune association (Juhl et "
            "al., Nutrients, 2018).\n\n"
            "Le mécanisme proposé : le lait augmente l'insuline et l'IGF-1, qui stimulent les glandes sébacées (Melnik et "
            "Zouboulis, Experimental Dermatology, 2013). Les recommandations américaines de 2024 ne retiennent aucun régime "
            "contre l'acné (Reynolds et al., JAAD, 2024).\n\n"
            "Margot est un personnage créé par IA. Contenu informatif et sourcé, qui ne remplace pas l'avis d'un médecin ou "
            "d'un·e diététicien·ne.\n\n"
            "#lait #acne #acneadulte #nutrition #peau"),
    ),
    "N02_sucre": dict(
        chapter=1,
        series="Les aliments qui donnent des boutons",
        part="Partie 2 : Le sucre",
        open="question",
        voice="Erinome:nutri_jeune",
        fluid=True,
        # no spoiler: white bread vs table sugar (index 75 vs 65) belongs to « Le pain blanc », sugary drinks to « Les
        # sodas », fruit sugar to « Les fruits »; this episode owns the 12-week low-glycaemic-load trial (Smith 2007) and
        # the biopsy trial (Kwon 2012)
        lines=[
            ("Est-ce que le sucre donne vraiment des boutons ?",
             "a small heap of glistening white sugar cubes on a dark slate", "", None),
            ("Tes pics de sucre nourrissent peut-être tes boutons, et tu ne les sens même pas.",
             "a glossy pastry on a dark slate, thick sugar glaze slowly dripping down its side", "", None),
            ("Moi c'est Margot, spécialiste de la nutrition cutanée. Le sucre, tout le monde croit le connaître, mais les "
             "études racontent autre chose.", "persona card", "", None),
            ("Biscuits, céréales, confiseries : ton sucre grimpe en flèche, et ton corps répond par une vague d'insuline.",
             "a single drop of golden honey falling into a tall glass of clear water", "", None),
            ("Cette insuline, et un autre signal, l'IGF-1, font gonfler tes glandes à sébum. Plus d'huile, des pores qui "
             "se bouchent.", "reused from N01", "", None),
            ("Et ce n'est pas qu'une théorie : des chercheurs ont suivi",
             "a large magnifying glass lying on a small heap of white sugar cubes on a dark slate", "", None),
            ("des jeunes adultes pendant douze semaines.",
             "twelve white sugar cubes lined up in a single neat row on a dark slate", "", None),
            ("Les uns ont gardé leur assiette, les autres ont remplacé leurs sucres rapides par des sucres lents.",
             "two plates side by side on a dark slate: on the left white bread, pastries and sweets, on the right lentils, "
             "vegetables and wholegrain bread", "", None),
            ("Résultat : 23 boutons de moins en moyenne, contre 12 dans l'autre groupe, presque deux fois plus.", None, "",
             ("23", "boutons en moins", "23")),
            ("Et le plus surprenant ? Ils n'avaient pas arrêté le sucre : ils avaient juste choisi des sucres plus lents.",
             "a bowl of rolled oats and a halved apple on a dark slate", "", None),
            ("Un deuxième essai est allé plus loin : au microscope, les glandes à sébum avaient rapetissé.", None, "", None),
            ("Alors, le sucre donne-t-il des boutons ? Mon verdict : probablement, quand il fait des pics.", None, "", None),
            ("Ce n'est pas le sucre en soi : c'est le pic qu'il provoque.", None, "", None),
            ("Le sucre, c'est le deuxième accusé. Il en reste six. Pour connaître tous les verdicts, abonne-toi.", None, "",
             None),
        ],
        cards={2: "persona"},
        reuse={4: ("N01_lait", 6, True)},  # N01's drop of golden oil falling into the bowl: the glands make more oil
        chain={8: 7, 10: 4, 11: 0, 12: 1},  # 10: the bowl of oil, after the drop
        verdict=(11, "PROBABLE", "probablement", "le sucre donne des boutons"),
        motion={
            0: "A few grains of sugar fall onto the heap in slow motion and a sugar cube slowly crumbles, its crystals "
               "sparkling in the side light. The camera does not move.",
            1: "The thick sugar glaze slowly drips down the side of the pastry in slow motion, glistening. The camera does not "
               "move.",
            3: "The drop of honey falls into the water in slow motion and spreads into a swirling golden cloud that rises "
               "and fills the glass. The camera does not move.",
        },
        anim=[0, 1, 3],
        fx={5: "sweep", 6: "sweep", 7: "sweep", 8: "sweep", 9: "sweep", 10: "sweep"},
        zoom={2: 0.09},
        # no montage: « ça défile trop vite, pas fluide du tout » (user, 2026-10-15)
        keys=["sucre", "pics", "sens", "Margot", "nutrition", "cutanée", "études", "flèche", "insuline", "IGF-1", "sébum",
              "bouchent", "théorie", "douze", "lents", "23", "12", "deux", "arrêté", "microscope", "rapetissé",
              "probablement", "pic", "verdicts", "abonne-toi"],
        music=score((0, "Revelation"), (1, "Tension"), (3, "Investigation"), (4, "Danger"), (5, "Revelation"),
                    (6, "Investigation"), (9, "Revelation"), (11, "The answer"), (12, "Final word")),
        caption=(
            "Les aliments qui donnent des boutons · Partie 2 : Le sucre\n\n"
            "Le sucre : ce n'est pas le sucre en soi, c'est le pic qu'il provoque.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Dans un essai randomisé de 12 semaines chez 43 jeunes hommes de 15 à 25 ans, une alimentation à faible charge "
            "glycémique a réduit les lésions d'acné de 23,5 en moyenne, contre 12,0 dans le groupe témoin (Smith et al., "
            "American Journal of Clinical Nutrition, 2007).\n\n"
            "Un autre essai, sur 10 semaines, a montré des glandes sébacées plus petites sur biopsie avec une alimentation à "
            "faible charge glycémique (Kwon et al., Acta Dermato-Venereologica, 2012).\n\n"
            "Le mécanisme proposé : les sucres rapides augmentent l'insuline et l'IGF-1, qui stimulent les glandes "
            "sébacées et les androgènes. Les preuves restent jugées modestes, et les recommandations américaines de 2024 ne "
            "retiennent aucun régime contre l'acné (Reynolds et al., JAAD, 2024).\n\n"
            "Margot est un personnage créé par IA. Contenu informatif et sourcé, qui ne remplace pas l'avis d'un médecin ou "
            "d'un·e diététicien·ne.\n\n"
            "#sucre #acne #acneadulte #nutrition #peau"),
    ),
    "N03_chocolat": dict(
        chapter=1,
        series="Les aliments qui donnent des boutons",
        part="Partie 3 : Le chocolat",
        # v2 (user, 2026-10-15): open on the question the video answers, written huge on the most striking visual; close
        # the hook's promise (switching to dark chocolate); Margot says which studies she went through; the verdict
        # answers the opening question; a younger, punchier voice in one breath per sentence
        open="question",
        voice="Erinome:nutri_jeune",
        fluid=True,
        lines=[
            ("Est-ce que le chocolat donne vraiment des boutons ?", "reused v1", "", None),
            ("Si tu es passée au chocolat noir pour protéger ta peau, écoute bien.", "reused v1", "", None),
            ("Moi c'est Margot, spécialiste de la nutrition cutanée. J'ai épluché toutes les études sur le chocolat et la "
             "peau, et ce que j'y ai trouvé, personne n'ose te le dire.", "persona card", "", None),
            ("Dans la première, 92 adultes ont mangé 50 grammes de chocolat noir à 85 % chaque jour.", "reused v1", "",
             ("50", "grammes", "50")),
            ("Résultat : la peau de 79 d'entre eux a empiré.", None, "", ("79", "sur 92", "79")),
            ("Et le chocolat au lait ? Chez des étudiants, il a fait sortir de nouveaux boutons en seulement 48 heures.",
             "reused v1", "", ("48", "heures", "48")),
            ("Le plus troublant, c'est qu'à sucre égal, des bonbons n'ont rien provoqué.", "reused v1", "", None),
            ("Le suspect n'est donc pas que le sucre : c'est peut-être le cacao lui-même.", "reused v1", "", None),
            ("Dans une autre étude, plus les volontaires avalaient de cacao pur, plus leurs boutons augmentaient.",
             "reused v1", "", None),
            ("Et le chocolat noir, c'est justement le plus riche en cacao.", None, "", None),
            ("Ces études sont petites et souvent faites sur des hommes, mais elles vont toutes dans le même sens.", None, "",
             None),
            ("Alors, le chocolat donne-t-il des boutons ? Mon verdict : probablement oui.", None, "", None),
            ("Le chocolat n'est pas une légende, mais ce n'est pas une sentence.", None, "", None),
            ("Le chocolat, c'est le troisième accusé. Il en reste cinq. Pour connaître tous les verdicts, abonne-toi.", None,
             "", None),
        ],
        cards={2: "persona"},
        # scenes of v1, renumbered (0 snap, 1 melt, 3 rows, 5 milk chocolate, 6 jelly beans, 7 magnifier, 8 cocoa bean)
        chain={4: 1, 9: 0, 10: 7, 11: 0, 12: 4},
        verdict=(11, "PROBABLE", "probablement", "le chocolat donne des boutons"),
        motion={
            0: "A piece of dark chocolate snaps in two in slow motion, tiny cocoa crumbs flying in the side light. The camera "
               "does not move.",
            1: "The square of dark chocolate slowly melts and slumps into a glossy dark puddle. The camera does not move.",
            8: "The split cocoa bean slowly opens a little more, revealing its dark glossy interior in the side light. The "
               "camera does not move.",
        },
        anim=[0, 1, 8],
        clip_end={1: 0.8},
        fx={3: "sweep", 5: "sweep", 6: "sweep", 7: "sweep", 9: "sweep", 10: "sweep"},
        zoom={2: 0.09},
        # no montage: « ça défile trop vite, pas fluide du tout » (user, 2026-10-15)
        keys=["chocolat", "noir", "Margot", "nutrition", "cutanée", "50", "grammes", "92", "79", "empiré", "lait", "48",
              "heures", "troublant", "rien", "cacao", "riche", "probablement", "oui", "légende", "sentence", "verdicts",
              "abonne-toi"],
        music=score((0, "Revelation"), (1, "Tension"), (3, "Investigation"), (4, "Danger"), (6, "Revelation"),
                    (8, "Danger"), (10, "Breath"), (11, "The answer"), (12, "Final word")),
        caption=(
            "Les aliments qui donnent des boutons · Partie 3 : Le chocolat\n\n"
            "Est-ce que le chocolat donne des boutons ? Probablement oui : ce n'est pas une légende, mais ce n'est pas une "
            "sentence.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Dans un essai croisé, 50 g par jour de chocolat noir à 85 % ont aggravé l'acné de 79 participants sur 92 "
            "(Daszkiewicz et al., Foods, 2024).\n\n"
            "Chez 54 étudiants, du chocolat au lait a augmenté le nombre de lésions en 48 heures, contrairement à des "
            "bonbons gélifiés de charge glycémique équivalente (+4,8 contre -0,7 ; Delost et al., JAAD, 2016).\n\n"
            "Avec du cacao pur en gélules, plus la dose était forte, plus les lésions augmentaient (Caperton et al., Journal "
            "of Clinical and Aesthetic Dermatology, 2014). La molécule en cause n'est pas identifiée.\n\n"
            "Ce sont des essais petits et courts, souvent menés sur des hommes : le lien est probable, pas démontré pour "
            "toutes.\n\n"
            "Margot est un personnage créé par IA. Contenu informatif et sourcé, qui ne remplace pas l'avis d'un médecin ou "
            "d'un·e diététicien·ne.\n\n"
            "#chocolat #acne #acneadulte #nutrition #peau"),
    ),
    # ---- chapter 1, parts 4-8 (2026-10-15): the validated N01 v5 recipe (user: « vraiment bien pour absolument tout »).
    # Opening question; Margot introduces herself differently each time; no montage; short sentences joined with « : »
    # or « , » so the calm voice never rushes them; the verdict answers the question and says what it rests on. No
    # spoiler: fruit juices (2.2), sodas (2.1), the « dairy face » (3.3), the whey (4.1), the glycaemic peak in depth (5.1)
    "N04_fromage": dict(
        chapter=1,
        series="Les aliments qui donnent des boutons",
        part="Partie 4 : Le fromage",
        open="question",
        voice="Erinome:nutri_jeune",
        fluid=True,
        lines=[
            ("Est-ce que le fromage donne vraiment des boutons ?",
             "a wedge of aged cheese with a few crumbs on a dark slate, its rind lit from the side", "", None),
            ("C'est le premier aliment qu'on raye quand on rêve d'une peau nette.",
             "a cheese board with three different cheeses pushed to the edge of a dark slate table, half in the shadow", "",
             None),
            ("Raclette, tartiflette, plateau du dimanche : tout y passe.",
             "melted raclette cheese slowly dripping from a wedge onto a small potato on a dark slate", "", None),
            ("Moi c'est Margot, spécialiste de la nutrition cutanée. Et sur le fromage, les études disent quelque chose que "
             "presque personne ne sait.", "persona card", "", None),
            ("Le soupçon a l'air logique : le fromage, c'est du lait.",
             "a tall clear glass of cold milk standing next to a wedge of aged cheese on a dark slate", "", None),
            ("Et le lait fait grimper des hormones qui réveillent tes glandes à sébum.", "reused from N01", "", None),
            ("Alors, le fromage est coupable ? Pas si vite.",
             "a large magnifying glass lying on a dark slate next to a wedge of aged cheese", "", None),
            ("Deux grandes analyses ont rassemblé toutes les études sur les produits laitiers et l'acné.",
             "dozens of small identical cubes of cheese lined up in long neat rows on a dark slate, seen from a low angle, "
             "receding into the darkness", "", None),
            ("Dans l'une, le fromage ne ressort pas du tout, et dans l'autre, les résultats se contredisent.", None, "",
             None),
            ("Alors, le fromage donne-t-il des boutons ? Mon verdict : pas prouvé.", None, "", None),
            ("Ce n'est pas le fromage qui ressort des études : c'est surtout le lait.", None, "", None),
            ("Le fromage, c'est le quatrième accusé. Il en reste quatre. Pour connaître tous les verdicts, abonne-toi.", None,
             "", None),
        ],
        cards={3: "persona"},
        reuse={5: ("N01_lait", 6, True)},  # N01's golden particles rising from the milk: the hormones
        chain={8: 7, 9: 0, 10: 4},
        verdict=(9, "PAS PROUVÉ", "prouvé", "le fromage donne des boutons"),
        motion={
            0: "A thin slice is cut from the wedge of cheese in slow motion and a few crumbs fall onto the slate. The camera "
               "does not move.",
            2: "The melted cheese slowly stretches and drips down onto the potato in slow motion, glistening. The camera does "
               "not move.",
        },
        anim=[0, 2],
        fx={1: "sweep", 4: "sweep", 6: "sweep", 7: "sweep", 8: "sweep", 10: "sweep"},
        zoom={3: 0.09},
        keys=["fromage", "raye", "nette", "Margot", "nutrition", "cutanée", "lait", "hormones", "sébum", "coupable",
              "analyses", "contredisent", "prouvé", "surtout", "verdicts", "abonne-toi"],
        music=score((0, "Revelation"), (1, "Tension"), (3, "Investigation"), (5, "Danger"), (6, "Breath"),
                    (7, "Investigation"), (9, "The answer"), (10, "Final word")),
        caption=(
            "Les aliments qui donnent des boutons · Partie 4 : Le fromage\n\n"
            "Le fromage : ce n'est pas lui qui ressort des études, c'est surtout le lait.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Dans la méta-analyse d'Aghasi et al. (Clinical Nutrition, 2019), le lait est associé à l'acné, mais pas le "
            "fromage ni le yaourt. Dans celle de Juhl et al. (Nutrients, 2018), les résultats pour le yaourt et le fromage "
            "sont moins nets et contradictoires.\n\n"
            "Ce sont des études d'association, qui ne prouvent pas de cause. Les recommandations américaines de 2024 ne "
            "retiennent aucun régime contre l'acné (Reynolds et al., JAAD, 2024).\n\n"
            "Margot est un personnage créé par IA. Contenu informatif et sourcé, qui ne remplace pas l'avis d'un médecin ou "
            "d'un·e diététicien·ne.\n\n"
            "#fromage #acne #acneadulte #nutrition #peau"),
    ),
    "N05_gluten": dict(
        chapter=1,
        series="Les aliments qui donnent des boutons",
        part="Partie 5 : Le gluten",
        open="question",
        voice="Erinome:nutri_jeune",
        fluid=True,
        lines=[
            ("Est-ce que le gluten donne vraiment des boutons ?",
             "a rustic loaf of bread on a dark slate, a few wheat ears beside it", "", None),
            ("Des milliers de femmes ont arrêté le pain pour avoir une peau nette.",
             "a rustic loaf of bread pushed to the edge of a dark slate table, an empty plate beside it, half in the shadow",
             "", None),
            ("Sur les réseaux, ça porte même un nom : la gluten face.",
             "a few slices of white bread fanned out on a dark slate, flour dust in the side light", "", None),
            ("Moi c'est Margot, spécialiste de la nutrition cutanée. J'ai cherché les études qui accusent le gluten, et le "
             "résultat m'a surprise.", "persona card", "", None),
            ("Pas une seule n'a relié le gluten à l'acné.",
             "a large magnifying glass lying on a dark slate next to a rustic loaf of bread", "", None),
            ("Mais attention : chez certaines personnes, le gluten abîme vraiment la peau.",
             "a handful of golden wheat ears lying on a dark slate, lit from the side", "", None),
            ("Ça s'appelle la maladie cœliaque, et elle a sa propre maladie de peau : des cloques qui démangent, sur les "
             "coudes et les genoux.",
             "a small heap of flour on a dark slate with a few grains of wheat, a soft pool of light around it", "", None),
            ("Rien à voir avec l'acné, et ça se diagnostique par une prise de sang.", None, "", None),
            ("Alors, le gluten donne-t-il des boutons ? Mon verdict : pas prouvé.", None, "", None),
            ("Te priver de pain sans diagnostic, c'est suivre une mode, pas une preuve.", None, "", None),
            ("Le gluten, c'est le cinquième accusé. Il en reste trois. Pour connaître tous les verdicts, abonne-toi.", None,
             "", None),
        ],
        cards={3: "persona"},
        chain={7: 6, 8: 0, 9: 1},
        verdict=(8, "PAS PROUVÉ", "prouvé", "le gluten donne des boutons"),
        motion={
            0: "The loaf of bread is slowly torn open by an unseen force in slow motion, a little steam rising from its "
               "crumb. The camera does not move.",
            6: "A light puff of flour slowly rises from the heap and drifts in the side light. The camera does not move.",
        },
        anim=[0, 6],
        fx={1: "sweep", 2: "sweep", 4: "sweep", 5: "sweep", 7: "sweep", 9: "sweep"},
        zoom={3: 0.09},
        keys=["gluten", "pain", "nette", "face", "Margot", "nutrition", "cutanée", "surprise", "seule", "cœliaque",
              "cloques", "diagnostique", "prouvé", "mode", "preuve", "verdicts", "abonne-toi"],
        music=score((0, "Revelation"), (1, "Tension"), (3, "Investigation"), (4, "Revelation"), (5, "Danger"),
                    (8, "The answer"), (9, "Final word")),
        caption=(
            "Les aliments qui donnent des boutons · Partie 5 : Le gluten\n\n"
            "Le gluten : ce n'est pas le pain, c'est la mode.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Aucune étude clinique ne relie le gluten à l'acné. Les recommandations américaines de 2024 ne retiennent aucun "
            "régime contre l'acné (Reynolds et al., JAAD, 2024).\n\n"
            "La maladie cœliaque est une vraie maladie auto-immune déclenchée par le gluten. Sa manifestation cutanée, la "
            "dermatite herpétiforme, donne des vésicules qui démangent, surtout sur les coudes, les genoux et les fesses. Le "
            "dépistage se fait par une prise de sang, avant tout arrêt du gluten.\n\n"
            "Margot est un personnage créé par IA. Contenu informatif et sourcé, qui ne remplace pas l'avis d'un médecin ou "
            "d'un·e diététicien·ne.\n\n"
            "#gluten #acne #acneadulte #nutrition #peau"),
    ),
    "N06_frites": dict(
        chapter=1,
        series="Les aliments qui donnent des boutons",
        part="Partie 6 : Les frites",
        open="question",
        voice="Erinome:nutri_jeune",
        fluid=True,
        lines=[
            ("Est-ce que le gras de tes frites ressort vraiment en boutons ?",
             "a paper cone of golden crispy french fries with flakes of salt on a dark slate", "", None),
            ("C'est l'idée la plus répandue : le gras que tu manges, ta peau le recrache.",
             "a single golden french fry held above a dark slate, a drop of oil hanging from its tip", "", None),
            ("Et elle a l'air logique : du gras dans l'assiette, du gras sur le visage.",
             "golden french fries frying in bubbling hot oil in a dark pan, lit from the side", "", None),
            ("Moi c'est Margot, spécialiste de la nutrition cutanée. Et ce que disent vraiment les études sur le gras, "
             "presque personne ne le sait.", "persona card", "", None),
            ("Ton sébum ne vient pas de ton assiette : il est fabriqué par tes glandes, sur ordre de tes hormones.",
             "reused from N01", "", None),
            ("Alors, les frites sont innocentes ? Pas si vite.",
             "a large magnifying glass lying on a dark slate next to a paper cone of french fries", "", None),
            ("En France, des chercheurs ont suivi plus de 24 000 adultes, et tout ce qu'ils mangeaient.",
             "dozens of small paper cones of french fries lined up in long neat rows on a dark slate, seen from a low "
             "angle, receding into the darkness", "", None),
            ("Ce qui ressort, ce n'est pas le gras seul : c'est le combo gras et sucré, burger, frites, dessert.",
             "a burger, a cone of french fries and a glazed doughnut side by side on a dark slate", "", None),
            ("Chaque portion de plus est associée à 54 % de risque d'acné en plus.", None, "", ("54", "%", "54")),
            ("Alors, le gras de tes frites ressort-il en boutons ? Mon verdict : faux.", None, "", None),
            ("Ce n'est pas l'huile de ton assiette : c'est le combo gras-sucré.", None, "", None),
            ("Les frites, c'est le sixième accusé. Il en reste deux. Pour connaître tous les verdicts, abonne-toi.", None, "",
             None),
        ],
        cards={3: "persona"},
        reuse={4: ("N01_lait", 7, True)},  # N01's drop of golden oil falling into the bowl: the glands make the oil
        chain={8: 7, 9: 0, 10: 7},
        verdict=(9, "FAUX", "faux", "le gras de tes frites ressort en boutons"),
        motion={
            0: "A few golden french fries tumble into the paper cone in slow motion, flakes of salt bouncing in the side "
               "light. The camera does not move.",
            2: "The hot oil bubbles and sizzles around the french fries, tiny droplets glistening in the side light. The "
               "camera does not move.",
        },
        anim=[0, 2],
        fx={1: "sweep", 5: "sweep", 6: "sweep", 7: "sweep", 8: "sweep", 10: "sweep"},
        zoom={3: 0.09},
        keys=["gras", "frites", "boutons", "recrache", "logique", "Margot", "nutrition", "cutanée", "sébum", "hormones",
              "innocentes", "24", "000", "sucré", "54", "%", "faux", "combo", "verdicts", "abonne-toi"],
        music=score((0, "Revelation"), (1, "Tension"), (3, "Investigation"), (5, "Breath"), (6, "Investigation"),
                    (8, "Danger"), (9, "The answer"), (10, "Final word")),
        caption=(
            "Les aliments qui donnent des boutons · Partie 6 : Les frites\n\n"
            "Les frites : ce n'est pas l'huile de ton assiette, c'est le combo gras-sucré.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Le sébum est fabriqué par les glandes sébacées, sous l'influence des hormones : la graisse que l'on mange ne "
            "« ressort » pas telle quelle sur la peau.\n\n"
            "Dans la cohorte française NutriNet-Santé (24 452 adultes), chaque portion quotidienne de produits gras et sucrés "
            "est associée à une acné actuelle plus fréquente (odds ratio 1,54). C'est une association, pas une preuve de "
            "cause (Penso et al., JAMA Dermatology, 2020).\n\n"
            "Margot est un personnage créé par IA. Contenu informatif et sourcé, qui ne remplace pas l'avis d'un médecin ou "
            "d'un·e diététicien·ne.\n\n"
            "#frites #acne #acneadulte #nutrition #peau"),
    ),
    "N07_fruits": dict(
        chapter=1,
        series="Les aliments qui donnent des boutons",
        part="Partie 7 : Les fruits",
        open="question",
        voice="Erinome:nutri_jeune",
        fluid=True,
        lines=[
            ("Est-ce que le sucre des fruits donne vraiment des boutons ?",
             "a ripe halved orange and a few whole berries on a dark slate, drops of juice glistening on the cut fruit", "",
             None),
            ("Une banane, c'est presque trois morceaux de sucre.",
             "a ripe banana lying on a dark slate next to three white sugar cubes", "", None),
            ("Alors certaines arrêtent les fruits, pour protéger leur peau.",
             "a bowl of fresh fruit pushed to the edge of a dark slate table, half in the shadow", "", None),
            ("Moi c'est Margot, spécialiste de la nutrition cutanée. Et sur les fruits, la réponse est plus étonnante que tu "
             "ne crois.", "persona card", "", None),
            ("En France, des chercheurs ont suivi plus de 24 000 adultes, et tout ce qu'ils mangeaient.",
             "dozens of small red apples lined up in long neat rows on a dark slate, seen from a low angle, receding into "
             "the darkness", "", None),
            ("Une fois le reste de l'assiette pris en compte, les fruits ne sont pas associés à l'acné, pas du tout.", None,
             "", None),
            ("Pourquoi ? Le secret est dans le fruit lui-même : ses fibres.",
             "an extreme close-up of the inside of a halved orange, its segments and white fibres glistening in the side "
             "light", "", None),
            ("Elles ralentissent le passage du sucre dans ton sang, et ta peau ne voit pas la différence.",
             "a few whole berries falling into a glass bowl of clear water in slow motion", "", None),
            ("Alors, le sucre des fruits donne-t-il des boutons ? Mon verdict : faux.", None, "", None),
            ("Le fruit n'est pas ton ennemi : ses fibres font tout le travail.", None, "", None),
            ("Les fruits, c'est le septième accusé. Il en reste un. Pour connaître tous les verdicts, abonne-toi.", None, "",
             None),
        ],
        cards={3: "persona"},
        chain={5: 4, 8: 0, 9: 6},
        verdict=(8, "FAUX", "faux", "le sucre des fruits donne des boutons"),
        motion={
            0: "A few berries roll slowly next to the halved orange, a drop of juice running down its cut surface. The camera "
               "does not move.",
            7: "The berries sink slowly through the clear water in slow motion, tiny bubbles rising around them. The camera "
               "does not move.",
        },
        anim=[0, 7],
        fx={1: "sweep", 2: "sweep", 4: "sweep", 5: "sweep", 6: "sweep", 9: "sweep"},
        zoom={3: 0.09},
        keys=["sucre", "fruits", "banane", "trois", "peau", "Margot", "nutrition", "cutanée", "étonnante", "24", "000",
              "pas", "fibres", "ralentissent", "faux", "ennemi", "verdicts", "abonne-toi"],
        music=score((0, "Revelation"), (1, "Tension"), (3, "Investigation"), (5, "Revelation"), (6, "Investigation"),
                    (8, "The answer"), (9, "Final word")),
        caption=(
            "Les aliments qui donnent des boutons · Partie 7 : Les fruits\n\n"
            "Les fruits : ce n'est pas ton ennemi, ses fibres font tout le travail.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Une banane moyenne contient environ 14 g de sucres, soit près de trois morceaux de sucre de 5 g.\n\n"
            "Dans la cohorte française NutriNet-Santé (24 452 adultes), la consommation de fruits n'est pas associée à "
            "l'acné après ajustement sur le reste de l'alimentation (odds ratio 0,97 ; Penso et al., JAMA Dermatology, "
            "2020).\n\n"
            "Les fibres du fruit entier ralentissent l'absorption de ses sucres : sa charge glycémique reste basse.\n\n"
            "Margot est un personnage créé par IA. Contenu informatif et sourcé, qui ne remplace pas l'avis d'un médecin ou "
            "d'un·e diététicien·ne.\n\n"
            "#fruits #acne #acneadulte #nutrition #peau"),
    ),
    "N08_cafe": dict(
        chapter=1,
        series="Les aliments qui donnent des boutons",
        part="Partie 8 : Le café",
        open="question",
        voice="Erinome:nutri_jeune",
        fluid=True,
        lines=[
            ("Est-ce que ton café du matin donne vraiment des boutons ?",
             "a cup of black espresso with a thin wisp of steam on a dark slate, coffee beans around it", "", None),
            ("On l'accuse de tout : du stress, des nuits courtes, et maintenant de ta peau.",
             "a few roasted coffee beans scattered on a dark slate, one bean split open, lit from the side", "", None),
            ("Certaines l'ont même rayé de leur routine.",
             "an empty espresso cup turned upside down on its saucer at the edge of a dark slate table, half in the shadow",
             "", None),
            ("Moi c'est Margot, spécialiste de la nutrition cutanée. J'ai fouillé les études sur le café et la peau, et il y "
             "a une surprise.", "persona card", "", None),
            ("La surprise, c'est qu'il n'y en a pas : aucune étude n'a mesuré le lien entre le café et l'acné.",
             "a large magnifying glass lying on a dark slate next to a cup of black espresso", "", None),
            ("Alors, ton café est innocent ? Pas si vite.", None, "", None),
            ("Regarde plutôt ce qu'il y a dans ta tasse.",
             "a tall glass of iced latte topped with whipped cream and a thick drizzle of caramel syrup on a dark slate", "",
             None),
            ("Un grand latte au sirop peut contenir l'équivalent de plusieurs morceaux de sucre.",
             "a thick stream of golden caramel syrup pouring into a glass of milky coffee", "", None),
            ("Et le sucre, lui, fait grimper ton insuline, que tes glandes à sébum adorent.", None, "", None),
            ("Alors, le café donne-t-il des boutons ? Mon verdict : pas prouvé.", None, "", None),
            ("Ce n'est pas le café : c'est ce que tu mets dedans.", None, "", None),
            ("Le café, c'était le dernier accusé. Pour connaître tous les verdicts, abonne-toi.", None, "", None),
        ],
        cards={3: "persona"},
        chain={5: 4, 8: 7, 9: 0, 10: 6},
        verdict=(9, "PAS PROUVÉ", "prouvé", "le café donne des boutons"),
        motion={
            0: "A thin wisp of steam rises slowly and curls above the espresso in the side light. The camera does not move.",
            7: "The caramel syrup pours slowly into the coffee and swirls through it in slow motion. The camera does not "
               "move.",
        },
        anim=[0, 7],
        fx={1: "sweep", 2: "sweep", 4: "sweep", 5: "sweep", 6: "sweep", 8: "sweep", 10: "sweep"},
        zoom={3: 0.09},
        keys=["café", "matin", "accuse", "peau", "rayé", "Margot", "nutrition", "cutanée", "surprise", "aucune",
              "innocent", "tasse", "sirop", "sucre", "insuline", "sébum", "prouvé", "dedans", "verdicts", "abonne-toi"],
        music=score((0, "Revelation"), (1, "Tension"), (3, "Investigation"), (4, "Revelation"), (5, "Breath"),
                    (6, "Danger"), (9, "The answer"), (10, "Final word")),
        caption=(
            "Les aliments qui donnent des boutons · Partie 8 : Le café\n\n"
            "Le café : ce n'est pas lui, c'est ce que tu mets dedans.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Aucune étude clinique n'a évalué le lien entre le café et l'acné.\n\n"
            "Les boissons aromatisées au sirop peuvent contenir plusieurs dizaines de grammes de sucre. Les sucres rapides "
            "font monter l'insuline, qui stimule les glandes sébacées ; les preuves sur l'acné restent modestes et les "
            "recommandations américaines de 2024 ne retiennent aucun régime (Reynolds et al., JAAD, 2024).\n\n"
            "Margot est un personnage créé par IA. Contenu informatif et sourcé, qui ne remplace pas l'avis d'un médecin ou "
            "d'un·e diététicien·ne.\n\n"
            "#cafe #acne #acneadulte #nutrition #peau"),
    ),

    # 2026-10-16, new format « Ce qui arrive à ta peau », built from what wins in the sub-niche internationally (reports:
    # « inside the body » animations 2.4 to 22 M views, « stop sugar for N days » timelines 4 to 5.9 M, none in French).
    # v2: script from 225 transcribed shorts, full-motion h3 shots. v3: one thread (breakfast -> chin), the hook on her
    # chin, art direction « Porcelaine & lie-de-vin » from the avatar's world (miniatures_porcelaine).
    # v4 (same day), the user on v3: visuals « J'adore vraiment »; but « 8 h 20 » left on screen « n'apporte rien », no
    # « Partie 1 / série » on screen (each video is seen alone), and the viral script is: « le hook doit poser une question
    # clivante/problème, puis on parle du quotidien du spectateur, et que ce qu'il fait = potentiellement une erreur, puis
    # suspens, storytelling ». Now: « Tu manges plutôt sain… et tes boutons reviennent quand même ? » -> her « healthy »
    # breakfast (rice cakes) -> they raise blood sugar more than sugar (GI 82 vs 65) -> the story under her skin -> she
    # blames her cream -> proof -> verdict -> loop. Graphics only where they explain (GI bars, the glucose spike, the
    # study card, a hand-drawn circle on her spot); the edit « par une fille pour des filles » (reports/DA avatar/).
    "T01_sucre": dict(
        chapter=1,
        series="Ce qui arrive à ta peau",
        part="Partie 1 : Les galettes de riz",
        mini="miniatures_porcelaine",
        hook_key="sain",  # the divisive word, in lie-de-vin on the opening card
        open="question",
        voice="Erinome:grande_soeur",  # VALIDATED ambience (2026-10-16): the big-sister voice
        fluid=True,
        drone=False,  # no dark drone under the intimate track
        tail=1.2,  # the music breathes out after the last word (the loop's hard cut was heard as « la musique se coupe »)
        full_motion=True,
        engine="h3",
        lines=[
            ("Tu manges plutôt sain… et tes boutons du menton reviennent quand même ?",
             "a close selfie of her lower face, from the nose to the chin, lips relaxed; on her chin, a little off-centre, one "
             "inflamed red bump under the skin, slightly swollen, without a white head, a smaller pink bump beside it and one "
             "flat brownish mark from an older spot", "", None),
            ("Le matin, c'est galettes de riz, avocat et café : léger, healthy, tu fais attention.",
             "a breakfast table seen at an angle: two puffed rice cakes topped with thin slices of avocado on a small plate, "
             "a cup of coffee beside it", "", None),
            # « plus grimper » was said « plu » and heard as « ne font plus grimper »
            ("Sauf que ces galettes font grimper ton sucre sanguin plus haut… que du sucre en morceaux.",
             "two plain puffed rice cakes next to three white sugar cubes on a small plate", "", None),
            ("Vingt minutes plus tard, ce sucre inonde ton sang.",
             "the inside of a blood vessel, red blood cells drifting through it", "", None),
            ("Ton pancréas s'affole : il envoie une grosse dose d'insuline.",
             "a close macro view of the human pancreas filling most of the frame, its soft pink finely lobed tissue in "
             "volume, with tiny glowing golden cell clusters scattered through it", "", None),
            ("Mais l'insuline ne s'arrête pas au sucre : elle réveille aussi tes glandes à sébum.",
             "a cross-section of human skin showing a single sebaceous gland beneath a pore, the gland a cluster of rounded "
             "lobes filled with oil", "", None),
            ("Elles gonflent, fabriquent plus d'huile… et cette huile bouche un pore.", None, "", None),
            ("Le pire ? Tu ne vois rien : ça se passe sous ta peau, pendant des semaines.",
             "a cross-section of human skin, a single pore seen from the side, deep below the intact surface a small dense "
             "pale plug of oil and dead skin cells forming inside it", "", None),
            ("Alors le jour où le bouton sort, tu accuses ta crème, ton stress… jamais tes galettes.",
             "a crowded bathroom shelf seen up close, covered with half-used skincare tubes, pump bottles and small jars in "
             "plain unbranded packaging, a few caps left open", "", None),
            ("Pourtant, dans un essai, remplacer ces sucres rapides pendant dix semaines a réduit les boutons.",
             "a microscope view filling the whole frame: pink and violet stained human skin cells in fine detail, with a "
             "few rounded golden sebaceous gland lobes among them", "", None),
            ("Et au microscope, les glandes à sébum avaient rétréci.", None, "", None),
            ("Pas besoin de tout supprimer : les fruits, eux, sont innocents.",
             "a breakfast table with a bowl of fresh whole fruit: an orange, a few strawberries, a sliced kiwi and a handful "
             "of raspberries", "", None),
            ("Alors, tes galettes nourrissent-elles tes boutons ? Probablement : un peu, et avec des semaines de retard.",
             None, "", None),
            ("Ton bouton de ce matin a peut-être commencé… dans ton assiette, il y a des semaines.", None, "", None),
        ],
        photo=[0, 13],
        amateur=[8],
        body=[3, 4, 5, 6, 7, 9, 10],
        chain={6: 5, 10: 5, 12: 1, 13: 0},
        # the cards sit near the top (0.16): the plates and the bowl are in the lower half of the food shots
        graphics={0: [("circle", (0.547, 0.72, 95), "boutons")],
                  2: [("gi_bars", [("Galette de riz soufflé", 82, True), ("Sucre de table", 65, False)], "grimper",
                       0.16)],
                  3: [("glucose_curve", dict(label="TA GLYCÉMIE APRÈS LE PETIT-DÉJ", peak="+ 20 min"), "Vingt", 0.16)],
                  7: [("aside", ("LE PIRE ?", -3), "pire")],  # a taped paper note: the « girl edit » aside
                  # shorter and from the start of its line: on « fruits » it came and went before it could be read
                  11: [("stat_card", dict(number="24 452", text="adultes : fruits = aucun lien",
                                          source="NutriNet-Santé · 2020"), None, 0.16)]},
        hud={7: [("Microcomédon", 0.08, 0.70, "peau")],
             9: [("Essai contrôlé · 10 semaines", 0.08, 0.70, "essai")]},
        verdicts=[(12, "PROBABLE", "Probablement", "tes galettes pèsent sur tes boutons")],
        motion={
            # the circle is drawn on her spot: the face must stay put (v3's turn of the chin moved it by half the frame)
            0: "She stays almost still, breathing softly and blinking once, the phone shaking very slightly in her hand; "
               "her face and chin stay in the same place in the frame.",
            1: "A thin wisp of steam rises from the coffee while the soft morning light slowly shifts across the table.",
            2: "Tiny glowing golden particles slowly rise from the rice cakes, many more than from the sugar cubes, drifting "
               "upward like sparks.",
            3: "A flood of tiny sparkling sugar crystals pours into the blood vessel and rushes along with the red blood "
               "cells, faster and faster.",
            4: "Countless tiny glowing particles of insulin burst out of the pancreas and stream away in every direction.",
            5: "The gland lights up from within, glowing brighter and brighter as tiny glowing particles reach it.",
            6: "The glowing gland swells and pushes thick golden oil up into the pore, which slowly fills and closes.",
            7: "Deep inside the pore, the pale plug slowly grows and swells, hidden beneath the intact skin surface.",
            8: "The handheld phone slowly pans along the crowded shelf of half-used skincare tubes and jars.",
            9: "The stained cells shimmer softly and the lobes of the glands pulse gently, as if alive.",
            10: "The glowing gland slowly shrinks to about half its size and its glow softens.",
            11: "The fruit bowl slowly turns a little on the table, catching the morning light. Nothing is poured or dripped "
                "on the fruit.",
            12: "The soft morning light slowly moves across the breakfast table while steam rises from the coffee.",
            13: "She slowly brings the phone closer to her face and the spots on her chin come into sharper focus.",
        },
        anim=list(range(14)),
        keys=["sain", "menton", "healthy", "galettes", "grimper", "sang", "insuline", "glandes", "sébum", "pore", "rien",
              "semaines", "crème", "jamais", "réduit", "rétréci", "innocents", "probablement", "assiette"],
        # VALIDATED ambience (2026-10-16): « Musique 3 (émotion intime) » chosen among 6 samples; the grave score sounded
        # like « un film d'horreur ». The sample track itself is reused (music.mp3); this brief regenerates the same mood.
        music=dict(style=["Intimate emotional minimal instrumental", "90 BPM", "soft R&B-tinged Rhodes chords",
                          "gentle finger snaps", "warm sub bass", "airy pads", "tender and slightly melancholic",
                          "like a heartfelt story told between friends", "starting right away at full level",
                          "sparse mid-range leaving room for a spoken voice"],
                   negative=["horror", "dread", "dark drones", "thriller", "scary", "ominous", "vocals", "singing",
                             "choir", "spoken words", "EDM drop", "corporate upbeat", "music box"],
                   sections=[(0, "Story", ["tender, the Rhodes and the sub bass from the first second"]),
                             (2, "Twist", ["a slightly darker chord, still tender"]),
                             (7, "Breath", ["sparser, airy pads"]),
                             (9, "Story", ["the snaps come back"]),
                             (12, "The answer", ["warmer, a little hopeful"]),
                             (13, "Outro", ["the motif one last time, fading softly"])]),
        # no music stops: heard as « la musique se coupe au début et à la fin sans raison » (user)
        sfx=True,
        shutter=8,  # her bathroom shelf, a phone photo
        whoosh=[3, 8],  # plate -> inside the body, body -> her bathroom
        chime={11: "innocents"},  # the one good news
        caption=(
            "Tu manges plutôt sain… et tes boutons reviennent quand même ?\n\n"
            "Ton bouton de ce matin a peut-être commencé dans ton assiette, il y a des semaines.\n\n"
            "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
            "Index glycémique (glucose = 100), à quantité de glucides égale : galette de riz soufflé ≈ 82, sucre de table "
            "≈ 65 (Atkinson et al., Diabetes Care, 2008). Une galette contient peu de glucides : c'est la vitesse et la "
            "hauteur du pic qui comptent, surtout si elle remplace tout le petit-déjeuner.\n\n"
            "Le mécanisme proposé : les sucres rapides font monter l'insuline et l'IGF-1, qui stimulent les glandes "
            "sébacées (Melnik et Zouboulis, Experimental Dermatology, 2013). Un bouton commence par un microcomédon, "
            "invisible, des semaines avant d'apparaître.\n\n"
            "Dans un essai contrôlé coréen (32 personnes, 10 semaines), une alimentation à charge glycémique basse a réduit "
            "les lésions d'acné et la taille des glandes sébacées à la biopsie (Kwon et al., Acta Dermato-Venereologica, "
            "2012).\n\n"
            "Dans la cohorte française NutriNet-Santé (24 452 adultes), les fruits ne sont pas associés à l'acné (Penso et "
            "al., JAMA Dermatology, 2020).\n\n"
            "Les recommandations américaines de 2024 ne retiennent aucun régime contre l'acné (Reynolds et al., JAAD, "
            "2024) : c'est une piste, pas un traitement. Si ton acné te gêne, parles-en à un·e dermatologue.\n\n"
            "Ce qui arrive à ta peau · Partie 1. Voix et images générées par IA. Contenu informatif et sourcé.\n\n"
            "#acne #acneadulte #galettesderiz #nutrition #peau"),
    ),
}

# ---- « Ce qui arrive à ta peau », the validated recipe (T01, 2026-10-16) for the next episodes -----------------------
# Script: divisive question on her problem -> her daily habit -> it may be the mistake -> suspense and story under the skin
# -> proof (with the honest nuance) -> verdict -> a last line that loops back. Ambience VALIDATED: the big-sister voice,
# more intimate since T01 (« encore plus intime… crée de l'émotion »), and « Musique 3 - émotion intime » reused as the
# account's signature sound. Art direction « Porcelaine & lie-de-vin » (miniatures_porcelaine). Graphics only where they
# explain, readable (render drops what cannot be read), soft entrances. The body shots of T01 are reused (same universe).
SIGNATURE_MUSIC = "T01_sucre/_tests ambiance/_sources/musique_3.mp3"
# reuse={line: ("T01_sucre", shot, False)}: T01's body shots (3 vessel, 4 pancreas, 5 gland, 7 pore, 9 microscope), the
# image only: each clip is made to the new shot's length


def peau(n, food, lines, **kw):
    """An episode of « Ce qui arrive à ta peau » with the validated settings; kw adds or overrides keys."""
    e = dict(chapter=1, series="Ce qui arrive à ta peau", part=f"Partie {n} : {food}", mini="miniatures_porcelaine",
             # the validated big-sister style: the « intime » wordings made Gemini faster (213-229 wpm against 203, measured
             # on T06), so the intimacy is carried by the writing
             open="question", voice="Erinome:grande_soeur", fluid=True, tail=1.2, full_motion=True, engine="h3",
             sfx=True, music_file=SIGNATURE_MUSIC, music=dict(style=[], sections=[]), drone=False, lines=lines,
             # intimate narration: the voice's own breaths are trimmed less (nothing is ever added); with the default caps
             # these scripts came out at 213-222 wpm against T01's 200
             caps={"?": 0.85, "!": 0.7, ".": 0.75, "…": 0.85, ":": 0.5, ";": 0.5, ",": 0.4})
    e.update(kw)
    return e


SELFIE = ("a close selfie of her lower face, from the nose to the chin, lips relaxed; {where}, one inflamed red bump under "
          "the skin, slightly swollen, without a white head, a smaller pink bump near it and one flat brownish mark from an "
          "older spot")
SOURCES_END = ("Les recommandations américaines de 2024 ne retiennent aucun régime contre l'acné (Reynolds et al., JAAD, "
               "2024) : c'est une piste, pas un traitement. Si ton acné te gêne, parles-en à un·e dermatologue.\n\n"
               "Ce qui arrive à ta peau · Partie {n}. Voix et images générées par IA. Contenu informatif et sourcé.\n\n")

EPISODES.update({
    "T02_lait": peau(2, "Le lait écrémé", [
        ("Tu as pris du lait écrémé pour faire attention… et si c'était le pire choix pour ta peau ?",
         SELFIE.format(where="along the right side of her jaw, below the corner of the mouth"), "", None),
        ("Le matin, ton café au lait écrémé : léger, raisonnable. Tu fais tout bien.",
         "a breakfast table seen at an angle: a large cup of milky coffee and a small jug of milk, a few crumbs", "", None),
        ("Et pourtant, il revient. Tu le sens sous ton doigt avant même de le voir.", None, "", None),
        ("Sauf que dans les grandes études, c'est justement le lait écrémé qui ressort le plus.",
         "two tall glasses side by side: on the left creamy whole milk, on the right thinner, slightly bluish skimmed milk",
         "", None),
        ("Le lait fait grimper deux signaux dans ton corps : l'insuline, et l'IGF-1, une hormone de croissance.",
         "the inside of a blood vessel, red blood cells drifting through it", "", None),
        ("Et ces deux signaux visent tes glandes à sébum : elles gonflent, et fabriquent plus d'huile.",
         "a sebaceous gland beneath a pore", "", None),
        ("Une piste : en retirant le gras, on garde toutes les protéines qui font grimper l'insuline.", None, "", None),
        ("Mais je te dois la vérité : une étude danoise, dans les gènes de vingt mille personnes, ne retrouve pas ce lien.",
         "a softly glowing DNA double helix floating in a warm luminous haze, its strands made of fine translucent beads",
         "", None),
        ("Alors non, tu n'as rien fait de mal. Le lait n'est pas un poison : c'est un facteur parmi d'autres.", None, "",
         None),
        ("Si tu veux tester : garde ton fromage, change juste le lait de ton café, pendant trois mois.",
         "a small wooden board with a wedge of aged cheese and a cup of black coffee beside it", "", None),
        ("Alors, ton lait écrémé abîme-t-il ta peau ? Probablement : un peu.", None, "", None),
        ("Le lait le plus léger… est peut-être le plus lourd pour ta peau.", None, "", None),
    ],
        hook_key="écrémé",
        photo=[0, 2, 8, 11], body=[4, 5, 7], reuse={4: ("T01_sucre", 3, False), 5: ("T01_sucre", 5, False)},
        chain={2: 0, 6: 3, 8: 0, 10: 3, 11: 0},
        graphics={0: [("circle", (None, None, 95), "peau")],
                  3: [("gi_bars", dict(title="Risque d'acné associé", items=[("Lait écrémé", 32, True),
                                                                            ("Lait entier", 22, False)],
                                       fmt="+{} %", source="Méta-analyse · 78 529 personnes"), None, 0.16)]},
        hud={4: [("IGF-1 · hormone de croissance", 0.08, 0.70, "IGF-1")]},
        verdicts=[(10, "PROBABLE", "Probablement", "le lait écrémé pèse sur ta peau")],
        whoosh=[4], chime={8: "rien"},
        motion={0: "She stays almost still, breathing softly and blinking once, the phone shaking very slightly in her "
                   "hand; her face and jaw stay in the same place in the frame.",
                1: "A thin wisp of steam rises from the coffee while the soft morning light slowly shifts across the table.",
                2: "She slowly brings a fingertip to her jaw and lightly touches the spot, the phone shaking very slightly.",
                3: "A thin stream of skimmed milk pours slowly into the right glass, small ripples on the surface.",
                4: "Tiny glowing golden particles appear among the red blood cells and drift along with them, more and "
                   "more of them.",
                5: "The gland lights up from within, swells slowly and pushes tiny droplets of golden oil toward the pore.",
                6: "The skimmed milk in the right glass slowly swirls while tiny glowing particles rise from it.",
                7: "The double helix slowly turns on itself, its beads softly glowing.",
                8: "She relaxes, lets out a small breath and the corner of her mouth lifts into a faint smile.",
                9: "A thin wisp of steam rises from the coffee in the soft daylight.",
                10: "The two glasses stand still while the soft daylight slowly moves across them.",
                11: "She slowly brings the phone closer to her face and the spot on her jaw comes into sharper focus."},
        anim=list(range(12)),
        keys=["écrémé", "pire", "peau", "doigt", "études", "insuline", "IGF-1", "glandes", "sébum", "vérité", "rien",
              "poison", "fromage", "probablement", "léger", "lourd"],
        caption=("Tu as pris du lait écrémé pour faire attention… et si c'était le pire choix pour ta peau ?\n\n"
                 "Le lait le plus léger est peut-être le plus lourd pour ta peau.\n\n"
                 "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
                 "Méta-analyse de 14 études (78 529 personnes) : tous produits laitiers OR 1,25 ; lait entier 1,22 ; lait "
                 "écrémé 1,32 (Juhl et al., Nutrients, 2018). Une autre méta-analyse trouve OR 1,82 pour le lait écrémé, "
                 "et pas d'association significative pour le fromage et le yaourt (Aghasi et al., Clinical Nutrition, "
                 "2019). Ce sont des associations, pas des preuves de cause.\n\n"
                 "Le mécanisme proposé : les protéines du lait font monter l'insuline et l'IGF-1, qui stimulent les "
                 "glandes sébacées (Melnik et Zouboulis, Experimental Dermatology, 2013).\n\n"
                 "Une étude génétique (randomisation mendélienne) sur 20 416 adultes danois ne trouve pas d'association "
                 "(Juhl et al., Nutrients, 2018).\n\n" + SOURCES_END.format(n=2) +
                 "#acne #acneadulte #lait #nutrition #peau")),

    "T03_chocolat": peau(3, "Le chocolat noir", [
        ("Tu as remplacé ton chocolat au lait par du noir à 85 %… pour ta peau ?",
         SELFIE.format(where="on her chin, a little off-centre"), "", None),
        ("Le soir, ton carré de noir, c'est ton petit moment à toi. Le seul écart que tu t'autorises.",
         "two squares of dark chocolate on a small saucer next to a cup of herbal tea, on a linen tablecloth", "", None),
        ("On t'a dit que le noir, c'était le bon : moins de sucre, plein d'antioxydants.",
         "a bar of dark chocolate broken into rough pieces, glossy cocoa shards", "", None),
        ("Sauf qu'en 2024, des chercheurs ont donné cinquante grammes de chocolat à 85 % par jour à 92 adultes.",
         "a long row of small squares of dark chocolate lined up on a linen tablecloth, seen at an angle", "", None),
        ("Et leur acné s'est aggravée. Chez 79 d'entre eux.", None, "", None),
        ("Et ce n'est pas le sucre : dans un autre essai, même du cacao pur, en gélules, faisait apparaître plus de "
         "boutons.", "a small heap of raw cocoa beans and fine cocoa powder in a matte ceramic bowl", "", None),
        ("Une piste : le cacao rendrait tes défenses plus réactives aux bactéries de ta peau.",
         "a cross-section of human skin with a single pore", "", None),
        ("Mais je te dois la vérité : ce sont de petits essais, souvent sur de jeunes hommes.", None, "", None),
        ("Alors non, il ne s'agit pas de te priver de ton moment à toi.", None, "", None),
        ("Si ta peau flambe, réduis juste la dose pendant un mois… et regarde ce qui se passe.", None, "", None),
        ("Alors, le chocolat noir donne-t-il des boutons ? Probablement : à forte dose, chez certaines.", None, "", None),
        ("Ce n'est peut-être pas le sucre du chocolat que ta peau te reproche… c'est le cacao.", None, "", None),
    ],
        hook_key="noir",
        photo=[0, 8, 11], body=[6, 7], reuse={6: ("T01_sucre", 7, False)},
        chain={4: 3, 7: 6, 8: 0, 9: 1, 10: 2, 11: 0},
        graphics={0: [("circle", (None, None, 95), "peau")],
                  4: [("stat_card", dict(number="79", text="adultes sur 92 : acné aggravée", source="Essai · 2024"),
                       None, 0.16)]},
        verdicts=[(10, "PROBABLE", "Probablement", "le chocolat noir pèse sur ta peau")],
        whoosh=[6], chime={8: "priver"},
        motion={0: "She stays almost still, breathing softly and blinking once, the phone shaking very slightly in her "
                   "hand; her face and chin stay in the same place in the frame.",
                1: "A thin wisp of steam rises from the tea while the soft light slowly shifts across the table.",
                2: "A few fine cocoa crumbs slowly fall from a broken edge of the chocolate in the side light.",
                3: "The soft daylight slowly moves across the rows of chocolate squares.",
                4: "The soft daylight slowly moves across the rows, a little warmer.",
                5: "A little cocoa powder slowly drifts down onto the beans in a fine cloud.",
                6: "A soft reddish glow slowly spreads in the skin around the pore, tiny glowing particles gathering there.",
                7: "The reddish glow around the pore slowly pulses and softens.",
                8: "She relaxes, lets out a small breath and the corner of her mouth lifts into a faint smile.",
                9: "A thin wisp of steam rises from the tea in the soft light.",
                10: "A few fine cocoa crumbs slowly settle around the chocolate pieces.",
                11: "She slowly brings the phone closer to her face and the spot on her chin comes into sharper focus."},
        anim=list(range(12)),
        keys=["noir", "peau", "moment", "écart", "sucre", "aggravée", "79", "cacao", "défenses", "vérité", "priver",
              "dose", "probablement"],
        caption=("Tu as remplacé ton chocolat au lait par du noir à 85 %… pour ta peau ?\n\n"
                 "Ce n'est peut-être pas le sucre du chocolat que ta peau te reproche : c'est le cacao.\n\n"
                 "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
                 "Essai croisé sur 92 adultes, 50 g par jour de chocolat à 85 % : la sévérité de l'acné a augmenté, chez "
                 "79 participants sur 92 (Daszkiewicz et al., Foods, 2024). Cacao à 100 % en gélules contre placebo, 14 "
                 "hommes : plus de cacao, plus de lésions (Caperton et al., J Clin Aesthet Dermatol, 2014). Ce sont de "
                 "petits essais, courts, surtout masculins.\n\n"
                 "Une piste : la consommation de chocolat augmente la réponse inflammatoire des cellules immunitaires face "
                 "aux bactéries de la peau (Netea et al., Cytokine, 2013).\n\n" + SOURCES_END.format(n=3) +
                 "#acne #acneadulte #chocolat #nutrition #peau")),

    "T04_whey": peau(4, "La whey", [
        ("Depuis que tu prends de la whey après le sport… ta peau a changé ?",
         SELFIE.format(where="along the left side of her jaw"), "", None),
        ("Ton pilates trois fois par semaine, ton shaker de protéines : tu prends soin de toi.",
         # a whole room on the floor made the video model walk a woman in shorts through it (twice): a close-up
         "a close-up of a protein shaker bottle standing on a kitchen counter, a rolled yoga mat leaning against the wall "
         "beside it, a set of keys next to it", "", None),
        ("Et pourtant, ces boutons sur la mâchoire, qui ne partent plus.", None, "", None),
        ("Sur internet, tout le monde accuse la whey. Et une étude va dans leur sens :",
         "a scoop of fine pale protein powder held above an open tub of powder, a little powder falling", "", None),
        ("47 % des personnes avec de l'acné prenaient de la whey… contre 28 % des autres.", None, "", None),
        ("Logique : la whey, c'est la partie du lait qui fait le plus grimper l'insuline.",
         "the inside of a blood vessel, red blood cells drifting through it", "", None),
        ("Et l'insuline réveille tes glandes à sébum.", "a sebaceous gland beneath a pore", "", None),
        ("Sauf que quand on l'a vraiment testée, six mois, contre un placebo… elle n'a pas donné plus de boutons.",
         "two identical plain white shaker bottles side by side on a bright laboratory bench", "", None),
        ("Je te dois la vérité : une seule étude, et faite sur des hommes.", None, "", None),
        ("Alors non, tu n'as pas à choisir entre ton sport et ta peau.", None, "", None),
        ("Si tu as un doute, teste une protéine végétale pendant deux ou trois mois, et regarde ta mâchoire.",
         "a matte ceramic bowl of pale green pea protein powder next to a few dried peas", "", None),
        ("Alors, la whey donne-t-elle des boutons ? Pas prouvé : suspecte, pas coupable.", None, "", None),
        ("Ton shaker n'est peut-être pas l'ennemi… mais il mérite qu'on le surveille.", None, "", None),
    ],
        hook_key="whey",
        photo=[0, 2, 9], amateur=[1, 12], body=[5, 6], reuse={5: ("T01_sucre", 3, False), 6: ("T01_sucre", 5, False)},
        chain={2: 0, 4: 3, 8: 7, 9: 0, 11: 3, 12: 1},
        graphics={0: [("circle", (None, None, 95), "peau")],
                  4: [("gi_bars", dict(title="Prennent de la whey", items=[("Avec de l'acné", 47, True),
                                                                          ("Sans acné", 28, False)],
                                       fmt="{} %", source="Étude cas-témoins"), None, 0.16)]},
        verdicts=[(11, "PAS PROUVÉ", "Pas", "la whey donne des boutons")],
        shutter=1, whoosh=[5, 7], chime={9: "choisir"},
        motion={0: "She stays almost still, breathing softly and blinking once, the phone shaking very slightly in her "
                   "hand; her face and jaw stay in the same place in the frame.",
                # a woman in shorts walked through the first take of this shot: nobody may enter the frame
                1: "A drop of water slowly runs down the side of the shaker while the handheld phone moves very slightly. "
                   "The scene stays empty: nobody enters the frame, no person, no legs, no hands.",
                2: "She slowly runs a fingertip along her jaw, the phone shaking very slightly.",
                3: "Fine powder slowly falls from the scoop into the tub in a soft cloud.",
                4: "The last grains of powder settle slowly in the soft light.",
                5: "Tiny glowing golden particles appear among the red blood cells and rush along with them.",
                6: "The gland lights up from within and swells slowly, tiny droplets of golden oil rising toward the pore.",
                7: "The soft light slowly moves across the two identical shakers.",
                8: "The soft light keeps moving slowly across the bench.",
                9: "She relaxes, lets out a small breath and the corner of her mouth lifts into a faint smile.",
                10: "A little pale green powder slowly slides down the side of the heap in the bowl.",
                11: "A last few grains of powder settle on the tub's rim.",
                12: "Another drop of water slowly runs down the shaker while the handheld phone drifts very slightly. "
                    "The scene stays empty: nobody enters the frame, no person, no legs, no hands."},
        anim=list(range(13)),
        keys=["whey", "peau", "shaker", "mâchoire", "accuse", "47", "28", "insuline", "glandes", "sébum", "placebo",
              "vérité", "choisir", "végétale", "prouvé", "ennemi"],
        caption=("Depuis que tu prends de la whey après le sport… ta peau a changé ?\n\n"
                 "Ton shaker n'est peut-être pas l'ennemi, mais il mérite qu'on le surveille.\n\n"
                 "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
                 "Étude cas-témoins : 47 % des personnes acnéiques prenaient de la whey, contre 27,7 % des témoins "
                 "(Cengiz et al., 2017). Plusieurs séries de cas décrivent une acné apparue avec la whey et améliorée à "
                 "l'arrêt (Silverberg, Cutis, 2012 ; Simonart, Dermatology, 2012).\n\n"
                 "Dans un essai contrôlé de 6 mois (49 hommes, 30 g par jour), la whey n'a pas donné plus d'acné que le "
                 "placebo. Aucune étude solide chez les femmes.\n\n"
                 "La whey est la fraction du lait la plus insulinotrope ; l'insuline stimule les glandes sébacées (Melnik, "
                 "JDDG, 2007).\n\n" + SOURCES_END.format(n=4) + "#acne #acneadulte #whey #sport #peau")),

    "T05_latte": peau(5, "Le latte au sirop", [
        ("Ton latte au caramel de l'après-midi… et si c'était lui qui entretenait tes boutons ?",
         SELFIE.format(where="on her chin, slightly to the left"), "", None),
        ("Seize heures, la réunion s'éternise : tu descends chercher ta récompense de la journée.",
         "an open-plan office desk in the afternoon: a takeaway plastic cup of iced caramel latte next to a laptop and "
         "a notebook", "", None),
        ("Sauf que ce gobelet, c'est du sucre liquide, dissous dans du lait.",
         "golden caramel syrup pouring slowly into a glass of milky iced coffee", "", None),
        ("Et le sucre liquide, c'est le plus rapide : il passe dans ton sang en quelques minutes.",
         "the inside of a blood vessel, red blood cells drifting through it", "", None),
        ("Ajoute le lait, qui fait lui aussi grimper l'insuline : tes glandes à sébum reçoivent un double signal.",
         "a sebaceous gland beneath a pore", "", None),
        ("Dans une étude française sur 24 452 adultes, les boissons sucrées étaient liées à plus d'acné.",
         "rows of glasses of sweet iced drinks and sodas on a linen tablecloth", "", None),
        ("Un litre par jour, et le risque fait plus que doubler.", None, "", None),
        ("Mais ton café, lui ? Aucune étude ne l'accuse.", "a small cup of black espresso on a saucer", "", None),
        ("Ce n'est pas ton café : c'est ce que tu mets dedans.", None, "", None),
        ("Alors garde ton moment de seize heures. Demande juste ton latte sans sirop, ou une seule dose.", None, "",
         None),
        ("Alors, ton latte sucré nourrit-il tes boutons ? Probablement : surtout s'il est quotidien.", None, "", None),
        ("Ta récompense de seize heures… ta peau la paie peut-être des semaines plus tard.", None, "", None),
    ],
        hook_key="latte",
        photo=[0, 11], amateur=[1, 9], body=[3, 4], reuse={3: ("T01_sucre", 3, False), 4: ("T01_sucre", 5, False)},
        chain={6: 5, 8: 7, 9: 1, 10: 2, 11: 0},
        graphics={0: [("circle", (None, None, 95), "boutons")],
                  5: [("stat_card", dict(number="24 452", text="adultes : boissons sucrées = plus d'acné",
                                         source="NutriNet-Santé · 2020"), None, 0.16)]},
        hud={6: [("Risque × 2,3", 0.08, 0.70, "litre")]},  # the longer label could not be read in its 2.8 s
        verdicts=[(10, "PROBABLE", "Probablement", "ton latte sucré pèse sur ta peau")],
        shutter=1, whoosh=[3, 5], chime={7: "Aucune"},
        motion={0: "She stays almost still, breathing softly and blinking once, the phone shaking very slightly in her "
                   "hand; her face and chin stay in the same place in the frame.",
                1: "The handheld phone slowly moves a little closer to the cup, condensation glistening on it.",
                2: "The golden caramel syrup keeps pouring slowly and swirls into the coffee.",
                3: "A flood of tiny sparkling sugar crystals pours into the blood vessel and rushes along with the cells.",
                4: "The gland lights up from within, glowing brighter, swelling slowly as glowing particles reach it.",
                5: "Tiny bubbles slowly rise in the sodas while the soft light moves across the glasses.",
                6: "The bubbles keep rising and the ice slowly shifts in the glasses.",
                7: "A thin wisp of steam rises from the espresso in the soft light.",
                8: "The steam keeps rising slowly from the espresso.",
                9: "The handheld phone slowly drifts across the desk toward the cup.",
                10: "The last drops of caramel slowly sink and swirl into the coffee.",
                11: "She slowly brings the phone closer to her face and the spot on her chin comes into sharper focus."},
        anim=list(range(12)),
        keys=["latte", "boutons", "récompense", "liquide", "rapide", "sang", "insuline", "double", "sucrées", "litre",
              "doubler", "café", "dedans", "sirop", "probablement", "paie"],
        caption=("Ton latte au caramel de l'après-midi… et si c'était lui qui entretenait tes boutons ?\n\n"
                 "Ce n'est pas ton café : c'est ce que tu mets dedans.\n\n"
                 "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
                 "Dans la cohorte française NutriNet-Santé (24 452 adultes), les boissons sucrées sont associées à l'acné "
                 "(aOR 1,18 par verre ; 2,29 pour un litre par jour), tout comme le lait (1,12 par verre). C'est une "
                 "association, pas une preuve de cause (Penso et al., JAMA Dermatology, 2020).\n\n"
                 "Aucune étude clinique n'a évalué le lien entre le café lui-même et l'acné.\n\n"
                 + SOURCES_END.format(n=5) + "#acne #acneadulte #latte #cafe #peau")),

    "T06_gluten": peau(6, "Le sans gluten", [
        ("Tu as arrêté le gluten pour ta peau… et tes boutons sont toujours là ?",
         SELFIE.format(where="on her chin, a little off-centre"), "", None),
        ("Plus de pain, plus de pâtes, tu lis chaque étiquette. Des mois d'efforts.",
         "a kitchen shelf with several packets of gluten-free pasta, crackers and bread in plain unbranded packaging", "",
         None),
        ("Et chaque matin, dans le miroir, ce même bouton sur le menton.", None, "", None),
        ("Je vais te dire ce que personne ne t'a dit : aucune étude ne relie le gluten à l'acné.",
         "a few golden wheat ears lying next to a rustic loaf of bread cut open", "", None),
        ("Pire : beaucoup de pains sans gluten sont faits de farine de riz et d'amidon de maïs…",
         "a few slices of very white, airy gluten-free sandwich bread on a matte plate", "", None),
        ("…qui font grimper ton sucre sanguin au moins autant que le pain blanc.",
         "the inside of a blood vessel, red blood cells drifting through it", "", None),
        ("Et ce sucre-là réveille tes glandes à sébum, exactement comme avant.", "a sebaceous gland beneath a pore", "",
         None),
        ("La maladie cœliaque existe, et elle a sa propre maladie de peau : ça se diagnostique, chez un médecin.",
         "a close macro view filling the whole frame of the inner wall of the small intestine: thousands of tiny soft "
         "finger-like villi, velvety, warm pink", "", None),
        ("Alors si tu te prives pour ta peau… tu t'épuises peut-être pour rien.", None, "", None),
        ("Ce qui compte, ce n'est pas le gluten : c'est la vitesse à laquelle ton pain fait monter ton sucre.",
         "a dark whole-grain sourdough loaf cut open on a wooden board", "", None),
        ("Alors, le gluten donne-t-il des boutons ? Pas prouvé : pas sans maladie cœliaque.", None, "", None),
        ("Tu as arrêté le gluten pour ta peau… elle te demandait peut-être autre chose.", None, "", None),
    ],
        hook_key="gluten",
        photo=[0, 2, 8, 11], amateur=[1], body=[5, 6, 7], reuse={5: ("T01_sucre", 3, False), 6: ("T01_sucre", 5, False)},
        chain={2: 0, 8: 0, 10: 3, 11: 0},
        graphics={0: [("circle", (None, None, 95), "boutons")],
                  3: [("aside", ("AUCUNE ÉTUDE", -3), "aucune")]},
        verdicts=[(10, "PAS PROUVÉ", "Pas", "le gluten donne des boutons")],
        shutter=1, whoosh=[5, 8],
        motion={0: "She stays almost still, breathing softly and blinking once, the phone shaking very slightly in her "
                   "hand; her face and chin stay in the same place in the frame.",
                1: "The handheld phone slowly pans along the shelf of gluten-free packets.",
                2: "She looks at her chin in the light, slowly tilting her face, the phone shaking very slightly.",
                3: "The soft daylight slowly moves across the wheat ears and the loaf.",
                4: "The soft light slowly moves across the white bread slices.",
                5: "A flood of tiny sparkling sugar crystals pours into the blood vessel and rushes along with the cells.",
                6: "The gland lights up from within and swells slowly, tiny droplets of golden oil rising toward the pore.",
                7: "The villi wave slowly and gently, like seaweed in a soft current.",
                8: "She lowers her eyes and lets out a small, tired sigh.",
                9: "The soft daylight slowly moves across the sourdough loaf, a few crumbs on the board.",
                10: "The soft daylight slowly moves across the wheat ears and the loaf.",
                11: "She slowly brings the phone closer to her face and the spot on her chin comes into sharper focus."},
        anim=list(range(12)),
        keys=["gluten", "boutons", "efforts", "miroir", "aucune", "acné", "riz", "maïs", "sucre", "glandes", "cœliaque",
              "médecin", "prives", "rien", "vitesse", "prouvé", "autre"],
        caption=("Tu as arrêté le gluten pour ta peau… et tes boutons sont toujours là ?\n\n"
                 "Ce qui compte, ce n'est pas le gluten : c'est la vitesse à laquelle ton pain fait monter ton sucre.\n\n"
                 "Ce que la vidéo n'a pas eu le temps de dire.\n\n"
                 "Aucune étude ne relie le gluten à l'acné en dehors de la maladie cœliaque, qui a sa propre atteinte "
                 "cutanée (la dermatite herpétiforme) et se diagnostique par une prise de sang et une biopsie.\n\n"
                 "Beaucoup de pains sans gluten sont à base d'amidons raffinés (riz, maïs) et ont un index glycémique "
                 "élevé, comparable ou supérieur à celui du pain blanc (≈ 75) ; les pains complets au levain sont plus bas "
                 "(Atkinson et al., Diabetes Care, 2008). Une alimentation à charge glycémique basse a réduit l'acné dans "
                 "deux essais (Smith et al., 2007 ; Kwon et al., 2012).\n\n" + SOURCES_END.format(n=6) +
                 "#acne #acneadulte #sansgluten #nutrition #peau")),
})
