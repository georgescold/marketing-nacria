"""Plan of the nutrition account's videos: 6 chapters of 8 parts (48 videos), same format as the other video accounts.

Research behind it (2026-10-14): reports/Recherche compte nutrition - viral.md and - preuves.md.
- Nobody owns « food x adult acne » in French; big nutrition accounts never talk about skin.
- What goes viral: one food, one verdict; A/B comparisons; debunking a trend; anti-guilt tone. Many viral hooks are false
  (cortisol face, spearmint tea): showing the level of evidence is the account's edge.
- The audience is exhausted by food rules (« je n'en peux plus de faire gaffe à tout ce que je mange ») and does not
  want to give things up: the account never pushes restriction, never frames weight loss.

Each episode: (title, hook, what we explain, closing antithesis, hero object for the cover, verdict). The verdict is the
evidence stamp shown at the end of the video and is always that of the evidence report: PROUVÉ, PROBABLE, PAS PROUVÉ, FAUX.
Persona: « Margot », an AI character who speaks as « je », with no diploma claimed (« diététicien » is a protected title),
no white coat, AI label on every post; sources in every caption.
"""

# Art direction « food noir & verdict »: hyper-real food photography on a deep forest-ink background, one dramatic side
# light, glistening textures (sugar, milk, chocolate), one rim-light colour per chapter; Fraunces Black for titles (food
# magazine), DM Sans for subtitles; the evidence stamp slams in on the verdict line.
INK, INK_EDGE = "#12201a", "#060a08"
MINT = "#8ff0c0"  # account accent: subtitle key words, counters
VERDICTS = {"PROUVÉ": "#3ddc84", "PROBABLE": "#ffc93c", "PAS PROUVÉ": "#b4bac6", "FAUX": "#ff4d4d"}

# 2026-10-16, art direction « Porcelaine & lie-de-vin », built only from the avatar's world (the user: « vert foncé
# c'est assez triste », « tout doit tourner autour de l'avatar », never the app's branding). Sources:
# reports/DA avatar/marques.md (41 brands she buys/follows, colours read from their CSS: warm off-white is the mean of 18
# of them, wine/plum the one accent shared by her women's-health, food and French-fashion brands) and tendances.md
# (lightness drives pleasure; warm light images get more likes; dark desaturated bases read sad, especially to women).
PORCELAINE, SABLE, ENCRE = "#F8F4F0", "#E9E2D8", "#1F1B18"
LIE_DE_VIN, SAUGE, OCRE, TAUPE, BRIQUE = "#722A43", "#3D6B5A", "#C8963E", "#7A716A", "#B0392C"

HERO = ("Hyper-realistic premium food photography, square frame: {obj}. One dramatic soft light from the side, rich "
        "glistening textures and fine details, natural vivid colours, shallow depth of field, a subtle {glow} rim light on the "
        "edges of the food. Background: a plain dark studio backdrop in deep green-black ({ink} behind the subject fading to near-black {edge}), no trees, no landscape, no window, a dark "
        "slate surface. Centred, the food occupying about 55 percent of the frame. Moody, appetising, like a high-end "
        "documentary. Full-bleed, no border, no frame. No text, no labels, no brand, no logo, no packaging print, no hands.")

SCENE = ("Natural lifestyle food photograph for a science explainer video, vertical 9:16 frame: {obj}. Soft directional "
         "window daylight with a warm white balance, gentle natural shadows, a slight film grain and low contrast. Real home "
         "food on matte stoneware, a few crumbs allowed, no glossy food styling.{accent} Background: a warm off-white linen "
         "tablecloth and plaster wall (#F8F4F0 to sand #E9E2D8), calm and uncluttered. The subject is centred horizontally, "
         "its centre at about 42 percent of the frame height, occupying about 55 percent of the frame width. The top fifth "
         "and the lower third of the frame stay calm and uncluttered. Full-bleed, no border. No text, no labels, no brand, "
         "no logo, no packaging print, no hands, no people.")

MOTION = ("Slow, smooth, appetising food motion like a premium food commercial shot in slow motion. Locked-off static camera: "
          "no camera movement, no zoom, no pan, no shake. The food keeps its shape and position except for the described "
          "action. Same daylight and background throughout. No text, no hands, no people. ")

# 2026-10-16, format « ce qui arrive à ta peau » (international winners: inside-the-body animation, 2.4 to 22 M views;
# « stop sugar for N days » timelines, 4 to 5.9 M): the food in food noir, then where it goes inside the body, in the
# cinematic dark 3D of @deconstruct.labb, then the real skin. Lines listed in e["body"] / e["photo"] use these prompts.
BODY = ("Bright, airy, photorealistic 3D medical visualization for a premium science documentary, vertical 9:16 frame: "
        "{obj}. Macro view inside the human body, organic translucent textures and fine details, soft diffused daylight-like "
        "light, gentle depth of field. The subject keeps natural vivid colours (blood cells deep red, oil and glands warm "
        "golden, tissue soft pink){accent}, set against a soft warm porcelain-to-sand haze (#F8F4F0 to #E9E2D8) instead of "
        "darkness: luminous, clean and calm, like a high-end medical illustration. The subject is centred horizontally, its "
        "centre at about 42 percent of the frame height. The top fifth and the lower third of the frame stay calm. "
        "Full-bleed, no border. No text, no labels, no letters, no numbers, no logo, no watermark, not a cartoon, no "
        "hologram grid, no people.")

BODY_MOTION = ("Slow, smooth, cinematic 3D medical animation like a premium science documentary. Locked-off static camera: no "
               "camera movement, no zoom, no pan, no shake. The anatomy keeps its exact shape and position except for the "
               "described action. Same soft light and background throughout. No text. ")

# real acne needs Nano Banana Pro (assets.PHOTO_MODEL) and this wording (plan_organes.PHOTO, 2026-10-16 benchmark).
# 2026-10-16, the user on T01: even Pro's studio close-ups are « pas encore rendu amateur »: the skin is now an
# unedited phone photo she took herself (the real close-ups of the niche's hits), not a lit portrait. {ink}/{edge} unused.
PHOTO = ("An unedited amateur smartphone photo, vertical 9:16 frame: {obj}. Taken by a woman in her late twenties with her "
         "own phone's front camera, held close and a little crooked, in her bathroom: flat natural daylight from a small "
         "window mixed with a warm ceiling bulb, slightly soft focus, a little phone-camera noise and JPEG softness, an "
         "ordinary white-tiled background out of focus. Her real skin: visible pores, fine vellus hair, a natural sebum "
         "sheen, slight redness and uneven tone, no makeup. The spots are real acne lesions of different ages and sizes, "
         "irregular and asymmetric: part of the skin, raised under it, with blurry diffuse pink-red edges fading into the "
         "surrounding skin, the same matte-to-slightly-oily texture as the skin around them, catching the light like skin "
         "does. Never beads, never droplets, never shiny spheres, never perfectly round dots, never identical spots, no "
         "blood. Not a studio photo, not cinematic, no dramatic lighting, no beauty filter, no retouching, not a model. No "
         "text, no letters, no numbers, no logo, no watermark, no phone visible.")

AMATEUR = ("An unedited amateur smartphone photo, vertical 9:16 frame: {obj}. Taken quickly with an ordinary phone in a "
           "real, ordinary French home or office, as described: flat natural daylight from a window mixed with warm indoor "
           "light, slightly "
           "soft focus, a little phone-camera noise and JPEG softness, slightly crooked framing. Real, lived-in and a bit "
           "messy. Not a studio photo, not styled, no dramatic lighting. No people, no text, no readable labels, no brand "
           "names, no logos.")

PHOTO_MOTION = ("Handheld smartphone video, natural and unedited: a very slight hand shake, real-time natural movement, the "
                "same bathroom daylight throughout. The woman moves only as described; her skin and spots keep their exact "
                "look. No zoom, no text. ")

PERSONA = ("Stylized 3D animated feature-film character portrait, square frame: Margot, a warm and confident French woman in her "
           "early thirties, wavy chestnut hair in a loose low bun, light freckles, natural skin texture with a few tiny "
           "natural imperfections, no heavy makeup, a knowing friendly half-smile, looking straight at the camera. She wears "
           "a sage-green linen apron over a cream top and holds half a fresh fig. Warm cinematic kitchen light at night, "
           "dark forest-green background softly out of focus. Head and shoulders centred, face large in the frame. Clearly an "
           "animated character, not a photograph. No white coat, no stethoscope, no text, no logo.")

CHAPTERS = [
    dict(n=1, name="Les aliments qui donnent des boutons", glow="tomato red (#FF5A3C)", tint="#FF5A3C",
         why="Le format qui fait réagir : un aliment, une enquête, un verdict. Le nom dit littéralement ce qu'elle tape "
             "dans la recherche TikTok. Les croyances n°1 relevées dans les commentaires (lait, sucre, gluten) passent "
             "en premier.",
         eps=[
             ("Le lait", "Un verre de lait par jour : 12 % de risque d'acné en plus.",
              "Sur 24 452 Français, chaque verre de lait est associé à 12 % de risque en plus ; le lait écrémé ressort le plus "
              "dans les méta-analyses. Une association modeste, pas une cause.",
              "Ce n'est pas un poison. C'est un facteur parmi d'autres.",
              "a tall glass of cold milk with a splash of milk frozen in mid-air above it", "PROBABLE"),
             ("Le sucre", "Ce n'est pas le sucre que tu vois qui compte.",
              "Les sucres rapides font grimper l'insuline et l'IGF-1, qui poussent les glandes à sébum. Dans un essai de 12 "
              "semaines, l'assiette à charge glycémique basse a fait baisser les boutons deux fois plus.",
              "Ce n'est pas le sucre en soi. C'est le pic qu'il provoque.",
              "a small heap of glistening white sugar cubes, a few grains of sugar falling", "PROBABLE"),
             ("Le chocolat", "Le chocolat noir n'est pas aussi innocent qu'on le dit.",
              "Dans un essai, 50 g par jour de chocolat à 85 % ont aggravé l'acné de 79 participants sur 92. De petits essais, "
              "courts, mais qui vont tous dans le même sens.",
              "Ce n'est pas une légende. Mais ce n'est pas une sentence.",
              "a bar of dark chocolate broken into rough pieces, glossy cocoa shards", "PROBABLE"),
             ("Le fromage", "Le fromage, premier sacrifié des régimes « peau nette ». À raison ?",
              "Pour le fromage et le yaourt, les données se contredisent et ne sont pas significatives dans une grande "
              "méta-analyse. C'est surtout le lait qui ressort.",
              "Ce n'est pas le fromage. C'est surtout le lait.",
              "a wedge of aged cheese with a few crumbs, its rind lit from the side", "PAS PROUVÉ"),
             ("Le gluten", "Des milliers de femmes ont arrêté le gluten pour leur peau. Ont-elles eu raison ?",
              "Aucune étude ne relie le gluten à l'acné. La maladie cœliaque existe, avec sa propre maladie de peau, et elle "
              "se diagnostique.",
              "Ce n'est pas le pain. C'est la mode.",
              "a rustic loaf of bread cut open, its crumb glistening, a few wheat ears beside it", "PAS PROUVÉ"),
             ("Les frites", "Ces frites d'hier soir, tu les retrouveras sur ton visage ?",
              "Le sébum est fabriqué par des glandes pilotées par les hormones. Ce que les études associent à l'acné, c'est le "
              "combo gras et sucré : plus 54 % par portion chez les Français.",
              "Ce n'est pas l'huile de ton assiette. C'est le combo gras-sucré.",
              "a paper cone of golden crispy french fries with flakes of salt", "FAUX"),
             ("Les fruits", "Le sucre des fruits, ennemi caché de ta peau ?",
              "Un fruit entier a une charge glycémique basse, freinée par ses fibres : aucune association avec l'acné après "
              "ajustement. Le jus, en revanche, c'est autre chose.",
              "Ce n'est pas le fruit. C'est le jus.",
              "a ripe halved orange and a few whole berries, drops of juice glistening", "FAUX"),
             ("Le café", "Ton café du matin peut-il te donner des boutons ?",
              "Il n'existe pas de données sur le café et l'acné. Ce qui compte, c'est ce qu'on y ajoute : sucre, sirop, lait.",
              "Ce n'est pas le café. C'est ce que tu mets dedans.",
              "a cup of black espresso with a thin wisp of steam, coffee beans around it", "PAS PROUVÉ"),
         ]),
    dict(n=2, name="Tes boissons expliquées", glow="citrus amber (#FFB238)", tint="#FFB238",
         why="Le chiffre le plus fort de l'étude française : un litre de boisson sucrée par jour, un risque d'acné "
             "multiplié par 2,3. Et les boissons « bien-être » démontées une par une.",
         eps=[
             ("Les sodas", "Un litre de soda par jour, et le risque d'acné fait plus que doubler.",
              "Chez 24 452 Français, chaque verre de boisson sucrée est associé à 18 % de risque en plus ; à un litre par "
              "jour, à un risque multiplié par 2,3. Une association, pas une preuve de cause.",
              "Ce n'est pas une boisson. C'est un pic de sucre liquide.",
              "a tall glass of dark cola with ice cubes and rising bubbles", "PROBABLE"),
             ("Les jus de fruits", "Un jus d'orange n'est pas un fruit.",
              "Sans ses fibres, le sucre du fruit passe vite dans le sang : sa charge glycémique se rapproche de celle d'un "
              "soda. Le fruit entier, lui, n'est pas associé à l'acné.",
              "Ce n'est pas un fruit pressé. C'est du sucre sans frein.",
              "a glass of fresh orange juice next to a whole orange", "FAUX"),
             ("Les deux litres d'eau", "Deux litres d'eau par jour pour une peau nette. Vraiment ?",
              "Boire plus améliore à peine l'hydratation de la peau, et aucune étude ne montre d'effet sur l'acné. Le sébum "
              "ne se dilue pas.",
              "Ce n'est pas un manque d'eau. C'est ton sébum.",
              "a large clear glass carafe of water with light refracting through it", "FAUX"),
             ("L'eau citronnée", "Ton eau citronnée du matin. Et si elle abîmait ta peau ?",
              "Aucun essai ne montre d'effet détox. Du jus de citron vert sur la peau, puis du soleil : brûlure et taches "
              "brunes, une réaction connue.",
              "Ce n'est pas une détox. Au soleil, c'est une brûlure.",
              "a glass of water with a slice of lemon and a slice of lime floating in it", "FAUX"),
             ("Le thé vert", "Le thé vert, star des routines peau. Les études sont plus timides.",
              "Chez 80 femmes, un extrait de thé vert a réduit les boutons du nez et du menton, mais pas le total. Une piste, "
              "pas une preuve.",
              "Ce n'est pas un remède. C'est une piste.",
              "a glass cup of green tea with a few loose tea leaves beside it", "PAS PROUVÉ"),
             ("La tisane de menthe verte", "La tisane qui fait le buzz contre l'acné hormonale n'a jamais été testée sur "
              "l'acné.",
              "Chez 42 femmes avec un SOPK, elle a baissé la testostérone en 30 jours, sans changer la pilosité. Aucun essai "
              "sur l'acné.",
              "Ce n'est pas un traitement. C'est une hypothèse.",
              "a glass cup of fresh spearmint tea with sprigs of mint", "PAS PROUVÉ"),
             ("L'alcool", "L'alcool se voit sur ta peau. Mais pas là où tu crois.",
              "Le lien avec l'acné n'est pas établi. Avec la rosacée, si : chez 82 737 femmes, le risque monte à partir de "
              "30 g d'alcool par jour.",
              "Ce n'est pas de l'acné. C'est de la rosacée.",
              "a glass of red wine with a slow swirl of wine inside", "PAS PROUVÉ"),
             ("Les jus détox", "Trois jours de jus détox pour purifier ta peau. Que se passe-t-il vraiment ?",
              "Aucun essai sur les cures détox. Le foie et les reins éliminent les déchets en continu ; les jus apportent "
              "surtout du sucre.",
              "Ce n'est pas une détox. C'est un jeûne sucré.",
              "three glass bottles of colourful cold-pressed juice, green, orange and red", "FAUX"),
         ]),
    dict(n=3, name="Les tendances décodées", glow="hot pink (#FF4FA3)", tint="#FF4FA3",
         why="Les tendances TikTok qui font des centaines de milliers de J'aime (« cortisol face », « sugar face », "
             "collagène) passées au crible. Les accroches sont déjà virales ; la réponse vraie est notre différence.",
         eps=[
             ("Le « sugar face »", "Le « sugar face » existe-t-il vraiment ?",
              "Il n'y a pas de carte du sucre sur le visage. Mais une glycémie élevée est associée à un visage perçu plus "
              "âgé : la glycation abîme le collagène.",
              "Ce n'est pas une carte. C'est un vieillissement plus discret.",
              "a slow cascade of sparkling sugar crystals falling onto a dark slate", "PAS PROUVÉ"),
             ("Le « cortisol face »", "Ton visage gonflé le matin… Et si c'était un « cortisol face » ?",
              "Le visage arrondi par le cortisol, c'est le syndrome de Cushing ou un traitement par corticoïdes. Le stress du "
              "quotidien est lié à l'acné, pas à cette transformation.",
              "Ce n'est pas ton stress. C'est une tendance.",
              "a small hourglass with dark sand next to a cup of camomile tea", "FAUX"),
             ("Le « dairy face »", "Le lait laisse-t-il une signature sur ton visage ?",
              "Aucun signe facial n'est propre aux produits laitiers. Le seul lien sérieux est modeste : le lait et l'acné.",
              "Ce n'est pas un visage type. C'est un lien modeste.",
              "a white ceramic jug of milk with a thin stream of milk pouring into a glass", "FAUX"),
             ("Les huiles de graines", "Les huiles de graines, nouvel ennemi de TikTok. Faut-il les jeter ?",
              "Aucune étude ne relie ces huiles à l'acné. Le sébum des peaux acnéiques manque même d'acide linoléique, "
              "l'acide gras de ces huiles.",
              "Ce n'est pas l'huile. C'est la peur du moment.",
              "a glass bottle of golden sunflower oil with sunflower seeds scattered around", "PAS PROUVÉ"),
             ("Le collagène à boire", "Ton collagène en poudre, il finit où exactement ?",
              "Il est digéré en petits morceaux comme toute protéine. Sur 23 essais, l'effet disparaît dans les études "
              "indépendantes et de bonne qualité.",
              "Ce n'est pas un soin. C'est une promesse.",
              "a glass of pink collagen drink with powder swirling into it", "PAS PROUVÉ"),
             ("« Mange ta skincare »", "« Mange ta skincare » : la phrase qui fait vendre.",
              "Aucun aliment n'efface une tache ou un bouton. Quelques pistes existent, comme les légumes, mais rien ne "
              "remplace un traitement.",
              "Ce n'est pas une crème. C'est une assiette.",
              "a halved avocado, a handful of blueberries and a few walnuts arranged like a skincare flat lay", "FAUX"),
             ("Le jeûne intermittent", "Le jeûne pour la peau ? Une seule étude, et sans groupe témoin.",
              "Les données viennent d'une étude avant-après pendant le Ramadan, sans comparaison. Impossible d'en tirer une "
              "règle.",
              "Ce n'est pas une preuve. C'est un témoignage.",
              "an empty white plate with a fork and knife placed on it and a clock reflection", "PAS PROUVÉ"),
             ("Le défi zéro sucre", "« J'ai arrêté le sucre 30 jours. » Voilà ce que les essais disent vraiment.",
              "Les essais qui marchent baissent la charge glycémique pendant 10 à 12 semaines, sans tout supprimer. L'effet "
              "est réel, mais modeste.",
              "Ce n'est pas un défi. C'est une habitude.",
              "a single sugar cube standing alone in the centre of an empty dark slate", "PROBABLE"),
         ]),
    dict(n=4, name="Les compléments expliqués", glow="lavender violet (#A98BFF)", tint="#A98BFF",
         why="Ce qu'elle avale « pour sa peau » : certains compléments déclenchent des boutons, d'autres faussent ses "
             "prises de sang. Le chapitre le plus utile, et le plus partagé.",
         eps=[
             ("La whey", "Et si c'était ton shaker de protéines qui te donnait des boutons ?",
              "Des cas de poussées existent chez les sportifs, mais un essai de 6 mois n'a pas trouvé plus d'acné qu'avec un "
              "placebo.",
              "Ce n'est pas la whey. Ce sont certaines peaux.",
              "a scoop of protein powder spilling from a metal scoop, a shaker bottle behind it", "PAS PROUVÉ"),
             ("La vitamine B12", "Une seule injection de B12 peut déclencher des boutons.",
              "À forte dose, la B12 change le comportement de la bactérie de l'acné, qui fabrique des molécules "
              "inflammatoires : 1 volontaire sur 10 a eu de l'acné.",
              "Ce n'est pas une vitamine anodine. C'est un déclencheur connu.",
              "a few translucent red vitamin capsules glowing softly on a dark slate", "PROBABLE"),
             ("La biotine", "La biotine « pour la peau » peut fausser tes prises de sang.",
              "Aucune preuve sur la peau. Mais l'agence américaine du médicament alerte : elle fausse certaines analyses, "
              "dont la thyroïde.",
              "Ce n'est pas un soin. C'est un risque d'erreur.",
              "a small heap of white tablets next to a glass test tube", "FAUX"),
             ("Le zinc", "Le zinc marche contre l'acné. Moins bien que tu crois.",
              "À 30 mg par jour, il réussit chez 31 % des patients, contre 63 % pour un antibiotique. Les dermatologues "
              "français le placent en deuxième intention.",
              "Ce n'est pas un miracle. C'est un appoint.",
              "a few metallic grey tablets and a halved oyster shell", "PROBABLE"),
             ("La vitamine A", "La vitamine A en gélules contre l'acné ? La dose efficace est dangereuse.",
              "Elle n'a marché qu'à 300 000 UI par jour, 30 fois la limite de sécurité, et elle est dangereuse pendant une "
              "grossesse.",
              "Ce n'est pas un complément. C'est un danger.",
              "a few glossy amber vitamin capsules next to a carrot cut lengthwise", "FAUX"),
             ("La vitamine D", "Une carence en vitamine D et des boutons : le lien se précise.",
              "Chez 39 patients carencés, la supplémentation a baissé les boutons inflammatoires de 35 %, contre 6 % sous "
              "placebo. Une piste, à vérifier par une prise de sang.",
              "Ce n'est pas un remède universel. C'est une carence à vérifier.",
              "a few golden soft-gel capsules catching a ray of light", "PAS PROUVÉ"),
             ("Les oméga-3", "L'anti-inflammatoire que ta peau aime peut-être.",
              "Dans un essai de 10 semaines, 2 g d'oméga-3 par jour ont réduit les boutons. Un seul essai, mais une vraie "
              "piste.",
              "Ce n'est pas une preuve solide. C'est une piste sérieuse.",
              "a fillet of fresh salmon with glossy omega-3 capsules beside it", "PAS PROUVÉ"),
             ("Les algues", "Ton complément « naturel » aux algues peut te donner des boutons.",
              "Les algues concentrent l'iode, qui peut déclencher des éruptions qui ressemblent à de l'acné.",
              "Ce n'est pas naturel donc sans risque. C'est de l'iode.",
              "a small bowl of dark green seaweed powder and dried kelp", "PROBABLE"),
         ]),
    dict(n=5, name="Ta glycémie expliquée", glow="icy blue (#7CC8FF)", tint="#7CC8FF",
         why="La mécanique derrière les chiffres, avec la courbe qui a fait la célébrité de Glucose Goddess, appliquée à la "
             "peau, uniquement avec des chiffres d'études.",
         eps=[
             ("Le pic de sucre", "Ce qui se passe dans ton sang 30 minutes après un croissant.",
              "Le glucose monte, l'insuline suit, puis l'IGF-1 : les trois messagers qui poussent les glandes à sébum.",
              "Ce n'est pas le croissant. C'est la courbe.",
              "a golden flaky croissant with buttery layers", "PROBABLE"),
             ("L'insuline", "L'hormone qui relie ton assiette à ta peau.",
              "L'insuline stimule les androgènes des ovaires et l'IGF-1, qui font grossir les glandes à sébum.",
              "Ce n'est pas qu'une hormone du sucre. C'est une hormone de ta peau.",
              "a single drop of golden honey falling from a honey dipper", "PROBABLE"),
             ("Le petit-déjeuner", "Ton petit-déj est peut-être le repas le plus sucré de ta journée.",
              "Céréales, jus, viennoiseries : la charge glycémique du matin est souvent la plus haute de la journée.",
              "Ce n'est pas le matin. C'est ce qu'on met dans le bol.",
              "a bowl of sugary breakfast cereal with milk being poured", "PROBABLE"),
             ("Le pain blanc", "Le pain blanc fait monter ton sucre plus vite que du sucre de table.",
              "Son index glycémique, environ 75, dépasse celui du sucre de table, environ 65. Le pain complet ou au levain "
              "fait une courbe plus douce.",
              "Ce n'est pas le gluten. C'est l'index glycémique.",
              "two slices of soft white bread next to a slice of dark seeded wholegrain bread", "PROBABLE"),
             ("L'ordre des aliments", "Manger tes légumes en premier change ta courbe de sucre.",
              "Chez des personnes diabétiques, commencer par les légumes et les protéines a baissé le pic de glucose du "
              "repas. Sur la peau, rien n'est encore mesuré.",
              "Ce n'est pas un hack peau. C'est une courbe plus douce.",
              "a plate with green vegetables in front and a small portion of pasta behind", "PAS PROUVÉ"),
             ("Les boissons au repas", "Le verre qui accompagne ton repas compte autant que l'assiette.",
              "Un soda au repas ajoute un pic de sucre liquide ; l'eau n'ajoute rien. C'est l'un des gestes les plus simples.",
              "Ce n'est pas le plat. C'est le verre.",
              "a plate of food with a glass of cola on one side and a glass of water on the other", "PROBABLE"),
             ("Douze semaines à index bas", "Douze semaines d'assiette à index bas : ce que les essais ont montré.",
              "Moins 23,5 boutons contre moins 12 dans l'essai de référence, et des glandes à sébum plus petites dans un "
              "autre. Sans rien interdire.",
              "Ce n'est pas un régime. C'est une charge plus légère.",
              "a colourful plate of lentils, roasted vegetables and wholegrains", "PROBABLE"),
             ("Le SOPK", "Avec un SOPK, ton assiette compte double.",
              "L'insuline est souvent en cause. Une alimentation à index bas a rendu le cycle régulier chez 95 % des femmes, "
              "contre 63 %. Aucun régime n'est supérieur aux autres.",
              "Ce n'est pas un régime miracle. C'est un levier de plus.",
              "a bowl of mixed berries, seeds and plain yogurt", "PROBABLE"),
         ]),
    dict(n=6, name="Manger sans te priver", glow="basil green (#6FD38A)", tint="#6FD38A",
         why="Le désir profond de l'avatar : ne plus y penser, ne pas se priver. Le chapitre qui referme la saison sur "
             "« tu n'as pas tout essayé, tu as tout essayé en même temps ».",
         eps=[
             ("Le régime d'éviction", "Supprimer dix aliments pour ta peau ? Voilà ce que ça coûte.",
              "Aucune preuve que tout supprimer aide la peau. En revanche, la charge mentale explose, et les régimes "
              "restrictifs peuvent mener à des troubles alimentaires.",
              "Ce n'est pas de la discipline. C'est de l'épuisement.",
              "a long empty dark table with a single small plate at the end", "FAUX"),
             ("Un changement à la fois", "Pourquoi tu ne sais jamais ce qui a marché.",
              "Si tu changes tout en même temps, impossible de savoir quoi a aidé. Les essais testent un changement à la "
              "fois, pendant 10 à 12 semaines.",
              "Tu n'as pas tout essayé. Tu as tout essayé en même temps.",
              "a single fresh fig standing alone on a dark slate", "PROBABLE"),
             ("L'assiette méditerranéenne", "L'assiette la plus étudiée pour la peau n'interdit rien.",
              "Plus elle est suivie, moins l'acné est sévère dans plusieurs études. Légumes, poissons, huile d'olive, "
              "légumineuses.",
              "Ce n'est pas un régime. C'est une façon de manger.",
              "a generous Mediterranean plate of tomatoes, olives, grilled fish and olive oil", "PROBABLE"),
             ("Les légumes", "L'aliment le plus associé à une peau calme est le moins viral.",
              "Dans une méta-analyse récente, manger des légumes est associé à deux fois moins d'acné. Personne n'en fait "
              "une tendance.",
              "Ce n'est pas un superaliment. C'est un légume.",
              "a vibrant bunch of fresh green vegetables, broccoli, spinach and courgette", "PROBABLE"),
             ("« Associé à »", "« Associé à » ne veut pas dire « cause ». Et ça change tout.",
              "Une étude d'observation montre un lien, pas une cause. Seuls les essais comparent vraiment. Beaucoup de "
              "vidéos virales confondent les deux.",
              "Ce n'est pas une preuve. C'est un indice.",
              "a magnifying glass resting on a slice of cake", "PROUVÉ"),
             ("Ce que dit ton dermato", "Les dermatologues américains ne recommandent aucun régime contre l'acné.",
              "Leurs recommandations de 2024 n'en retiennent aucun : les preuves sont trop faibles. Le traitement reste la "
              "base ; l'assiette, un appoint.",
              "Ce n'est pas ton assiette d'abord. C'est ton traitement.",
              "a simple balanced plate next to a small tube of cream", "PROUVÉ"),
             ("L'écart d'hier", "Ce bouton ce matin… c'est la pizza d'hier ?",
              "Un bouton se prépare dans le pore pendant des semaines. Un repas isolé pèse peu : ce sont les habitudes "
              "répétées qui ressortent dans les études.",
              "Ce n'est pas un écart. C'est une habitude.",
              "a single slice of pizza with stretching melted cheese", "PROBABLE"),
             ("Le bilan", "Ce que 24 452 Français nous ont appris sur la peau et l'assiette.",
              "Le gras-sucré, les boissons sucrées et le lait sont associés à plus d'acné ; une alimentation variée, à moins. "
              "Aucun aliment seul ne décide.",
              "Ce n'est pas un aliment. C'est un ensemble.",
              "a long table seen from above with many colourful dishes", "PROBABLE"),
         ]),
]
