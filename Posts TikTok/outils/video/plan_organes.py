"""Plan of the organs account's videos: 6 chapters of 8 parts (48 videos), same format as the acne video account (plan.py).

Each episode: (title, hook, what we explain, closing line, hero object for the thumbnail and the menu icon, glow override).
The closing line is an antithesis that answers the hook (model account formula). The tone is the organs carousels' one:
alarmist hooks, always true answers (a myth is only ever a hook that the video breaks). No product or brand names, no
promise, no diagnosis: when a sign needs a doctor (SOPK, perioral dermatitis), the video says so.
"""

# Art direction « scanner » (from the organs carousels, @factslipv9n style): near-black navy background with tiny floating
# particles, the body as a translucent dark-blue X-ray hologram, the organ of the story glowing intensely from within with
# glowing veins, and the account's alert yellow (#F6E13C): dotted rings around the zone, key words of the subtitles, counters.
INK, INK_EDGE = "#0b1a33", "#05060b"
YELLOW = "#f6e13c"

HERO = ("Dark cinematic 3D medical hologram illustration, square frame: {obj}. The anatomy is a translucent glass-like dark-blue "
        "X-ray hologram with fine luminous edges; the highlighted part glows intensely {glow} from within, with fine glowing {glow} "
        "veins and capillaries branching out around it. Background: near-black deep navy ({ink} behind the subject fading to {edge} "
        "at the edges) with subtle tiny floating {glow} particles. Dramatic lighting, high contrast, vivid, like a medical scan in a "
        "documentary. Centred, the subject occupying about 60 percent of the frame. Full-bleed, no border, no frame, no circle "
        "around the image. No text, no letters, no numbers, no labels, no logo.")

# first frame of a scene in the videos (vertical), same art direction as the covers; {accent} = extra colour instructions
SCENE = ("Dark cinematic 3D medical hologram illustration for a science explainer video, vertical 9:16 frame: {obj}. The anatomy "
         "is a translucent glass-like dark-blue X-ray hologram with fine luminous edges; the highlighted part glows intensely {glow} "
         "from within, with fine glowing {glow} veins and capillaries branching out around it.{accent} Background: near-black deep "
         "navy ({ink} behind the subject fading to {edge} at the edges) with subtle tiny floating {glow} particles. Dramatic "
         "lighting, high contrast, vivid, like a medical scan in a documentary. The subject is centred horizontally, its centre at "
         "about 42 percent of the frame height, occupying about 60 percent of the frame width. The top fifth and the lower third "
         "of the frame stay dark and empty. Full-bleed, no border. No text, no letters, no numbers, no labels, no logo.")

# a REAL spot on real skin, like the top half of the organ carousels (user, 2026-10-15, on O03: « le bouton rouge = boule
# rouge, ce n'est pas du tout réel »): every line that shows the spot itself is a macro photograph in the same dark navy
# light (episode key `photo`); the hologram stays for the organs and the mechanisms
# 2026-10-16, the user on O07: the spots « on voit que ce n'est pas réel » (glossy red beads, symmetric clusters). In a
# benchmark of 4 models on this wording, only Nano Banana Pro (assets.PHOTO_MODEL) drew real acne: pores, vellus hair,
# pustules of different ages, flat brown marks.
PHOTO = ("Photorealistic close-up photograph for a dermatology documentary, vertical 9:16 frame: {obj}. Shot like an "
         "unretouched dermatology reference photo taken with a macro lens: real skin of a woman in her late twenties with "
         "visible pores, fine vellus hair, a natural sebum sheen, slight redness and uneven tone. The spots are real acne "
         "lesions of different ages and sizes, irregular and asymmetric: part of the skin, raised under it, with blurry "
         "diffuse pink-red edges fading into the surrounding skin, the same matte-to-slightly-oily texture as the skin around "
         "them, catching the light like skin does. Never beads, never droplets, never shiny spheres, never perfectly round "
         "dots, never identical spots, no blood. Low-key cinematic lighting: a soft warm key "
         "light on the skin from one side, deep soft shadows, a subtle cold navy-blue rim light, the background near-black "
         "deep navy ({ink} fading to {edge}). The spots are sharp, centred horizontally at about 42 percent of the frame "
         "height, shallow depth of field. The top fifth and the lower third of the frame are darker. No text, no letters, "
         "no numbers, no logo, no watermark, no makeup filter, no retouching.")

# image-to-video prompt prefix (assets.py adds the episode's motion[i])
MOTION = ("Slow, smooth, minimal 3D medical hologram animation, like a premium science documentary. Locked-off static camera: no "
          "camera movement, no zoom, no pan, no shake. The translucent dark-blue anatomy keeps its exact shape and position; only "
          "the glowing parts change as described. Same lighting and dark background throughout. No text. ")

RING = " A bright yellow (#F6E13C) dotted circle surrounds the glowing zone."
HEAD = "a translucent female head and neck seen from the front, eyes closed, calm expression"

CHAPTERS = [
    dict(n=1, name="Ce que tes boutons disent de ton corps", glow="intense red (#FF2A2A)", tint="#FF3B30",
         why="Le format qui a fait les meilleurs chiffres des carrousels : une zone du visage, ce qu'elle dit vraiment. "
             "Chaque mythe du « face mapping » sert d'accroche, puis la vraie cause prend sa place.",
         eps=[
             ("Le menton", "Si tes boutons reviennent toujours sur le menton, ton corps essaie de te dire quelque chose.",
              "Chez la femme adulte, le bas du visage est la zone typique de l'acné hormonale : les androgènes de tes ovaires "
              "et de tes surrénales, qui pèsent plus lourd avant les règles.",
              "Ton menton n'est pas sale. Il suit ton cycle.",
              f"{HEAD}, the chin glowing.{RING}", ""),
             ("La mâchoire", "Les boutons de ta mâchoire ont souvent une cause que tu touches tous les jours.",
              "L'acné mécanique : la main sous le menton, le téléphone, le masque, la sangle du casque, l'écharpe. Pression, "
              "chaleur et frottement bouchent les pores.",
              "Ce n'est pas ta peau qui lâche. C'est ce qui l'écrase.",
              "a translucent female head in three-quarter view with a translucent smartphone pressed against the jawline, the "
              f"jawline glowing.{RING}", ""),
             ("Le front", "Des boutons sur le front ? Et si ton intestin essayait de te prévenir ?",
              "Le « face mapping » qui relie le front à la digestion n'a jamais été prouvé. Les vrais suspects : produits "
              "capillaires gras, frange, casquette, sueur.",
              "Ce n'est pas ton ventre. C'est ce qui touche ton front.",
              f"{HEAD}, with a translucent fringe of hair falling on the forehead, the forehead glowing.{RING}", ""),
             ("Le nez", "Un bouton sur le nez. Et si c'était ton cœur qui parlait ?",
              "Le mythe vient d'une vieille carte du visage. La vraie raison : le nez concentre parmi les pores les plus gros "
              "et les plus nombreux du visage, donc le plus de sébum.",
              "Ce n'est pas ton cœur. C'est ton sébum.",
              f"{HEAD}, the tip of the nose glowing.{RING}", ""),
             ("Les joues", "Des boutons sur les joues ? On dit que ce sont tes poumons qui parlent.",
              "Les joues touchent tout : l'écran du téléphone, la taie d'oreiller, tes mains. Sébum, bactéries et frottements "
              "s'y déposent jour et nuit.",
              "Ce ne sont pas tes poumons. C'est ce qui se pose sur tes joues.",
              f"a translucent female head lying sideways on a translucent pillow, the upper cheek glowing.{RING}", ""),
             ("Entre les sourcils", "Ce bouton entre tes sourcils… Et si c'était ton foie ?",
              "Cette zone fait partie de la zone T, la plus riche en glandes à sébum. Et l'épilation à la pince y ouvre la "
              "porte aux bactéries.",
              "Ce n'est pas ton foie. C'est ta zone T.",
              f"{HEAD}, the small area between the eyebrows glowing.{RING}", ""),
             ("Autour de la bouche", "Ces petits boutons autour de ta bouche ne sont peut-être pas de l'acné.",
              "La dermatite périorale : petits boutons rouges et plaques qui pèlent, souvent après des crèmes trop riches ou "
              "une crème à la cortisone. Elle se soigne autrement, chez un médecin.",
              "Ce n'est pas de l'acné. Et ça ne se traite pas pareil.",
              f"{HEAD}, a ring of small glowing dots around the mouth.{RING}", ""),
             ("Partout à la fois", "Quand les boutons s'installent partout, ce n'est plus une question de zone.",
              "Acné tenace, règles irrégulières, poils qui poussent plus, cheveux qui tombent : ensemble, ces signes peuvent "
              "évoquer un SOPK. Un médecin peut le vérifier.",
              "Ce n'est pas ta peau qui va mal. C'est un signal à faire vérifier.",
              f"{HEAD}, many small glowing spots all over the face.", ""),
         ]),
    dict(n=2, name="Tes hormones décodées", glow="hot pink-red (#FF2E7E)", tint="#FF2E7E",
         why="Le sujet qui touche le plus l'avatar (arrêt de la pilule, acné après 25 ans), raconté organe par organe : "
             "qui fabrique quoi, et pourquoi la peau réagit.",
         eps=[
             ("Les ovaires", "Tes ovaires fabriquent aussi des hormones dites « masculines ».",
              "Les ovaires et les surrénales produisent des androgènes, en petite quantité chez toutes les femmes. Ce sont eux "
              "qui font grossir les glandes à sébum.",
              "Ce n'est pas anormal. C'est une hormone que toutes les femmes ont.",
              "a translucent female pelvis with the uterus and the two ovaries glowing", ""),
             ("Les surrénales", "Deux glandes posées sur tes reins jouent sur tes boutons.",
              "Les surrénales libèrent le cortisol du stress, mais aussi des androgènes. Quand le stress dure, elles tournent "
              "plus fort.",
              "Ce n'est pas dans ta tête. C'est dans tes glandes.",
              "a pair of translucent kidneys with the two small adrenal glands on top of them glowing", ""),
             ("Le cycle", "Ta peau ne réagit pas pareil au jour 5 et au jour 25 de ton cycle.",
              "Après l'ovulation, l'équilibre des hormones laisse plus de place aux androgènes : plus de sébum, des boutons "
              "qui sortent avant les règles.",
              "Ta peau n'est pas imprévisible. Elle a un calendrier.",
              "a translucent uterus at the centre of a holographic ring of 28 segments, the last seven segments glowing", ""),
             ("Le SOPK", "Une femme sur dix a un SOPK. Beaucoup ne le savent pas.",
              "Le syndrome des ovaires polykystiques : règles irrégulières, excès d'androgènes, souvent de l'acné. Il se "
              "diagnostique chez un médecin, et se prend en charge.",
              "Ce n'est pas une fatalité. C'est un diagnostic à poser.",
              "a translucent ovary with a ring of many small round follicles glowing", ""),
             ("L'arrêt de la pilule", "Quelques mois après l'arrêt de la pilule, ta peau peut s'enflammer. Voilà pourquoi.",
              "Certaines pilules freinent les androgènes et le sébum. À l'arrêt, les ovaires reprennent la main : un rebond "
              "fréquent dans les mois qui suivent.",
              "La pilule ne t'a pas abîmé la peau. Ta peau se réveille.",
              "a translucent blister pack of pills next to a translucent ovary, the ovary glowing", ""),
             ("Le stérilet hormonal", "Ton stérilet hormonal peut jouer sur ta peau.",
              "Certains progestatifs ont un léger effet androgénique : chez certaines femmes, l'acné apparaît ou s'aggrave "
              "après la pose. À en parler à son médecin, sans rien retirer seule.",
              "Ce n'est pas toi. C'est une hormone de plus dans l'équation.",
              "a translucent uterus with a small T-shaped intrauterine device inside it, the device glowing", ""),
             ("La grossesse", "Enceinte, certains traitements contre l'acné sont interdits.",
              "Les rétinoïdes, en comprimés comme en crème, sont à éviter pendant la grossesse. Les hormones bougent, la peau "
              "aussi : certaines s'améliorent, d'autres non.",
              "Ce n'est pas le moment de tout essayer. C'est le moment de demander.",
              "a translucent pregnant female abdomen in profile, the uterus glowing", ""),
             ("La prise de sang normale", "Ta prise de sang est normale. Et pourtant, tes boutons sont hormonaux.",
              "La plupart des femmes qui ont de l'acné ont des taux d'hormones normaux. La peau transforme elle-même ces "
              "hormones en une forme plus puissante, la DHT.",
              "Ce n'est pas ton sang. C'est ta peau qui amplifie le signal.",
              "a translucent test tube of blood standing next to a translucent cube of skin with one glowing oil gland inside", ""),
         ]),
    dict(n=3, name="Ton ventre décodé", glow="fiery orange (#FF7A1A)", tint="#FF7A1A",
         why="Ce qu'elle mange, vu de l'intérieur : du pancréas à l'intestin, les liens prouvés et les fausses pistes.",
         eps=[
             ("Le sucre", "Ce pic de sucre peut finir sur ton menton.",
              "Les sucres rapides font grimper l'insuline et l'IGF-1, qui stimulent les glandes à sébum et les androgènes. Une "
              "alimentation à index glycémique bas a réduit l'acné dans des essais.",
              "Ce n'est pas le sucre que tu vois. C'est l'insuline que tu ne vois pas.",
              "a translucent pancreas glowing, with a few translucent sugar cubes floating around it", ""),
             ("Le lait", "Le lait n'est pas innocent pour ta peau.",
              "Le lait, surtout écrémé, fait monter l'IGF-1 et a été associé à plus d'acné dans de grandes études. Le fromage "
              "et le yaourt semblent moins concernés.",
              "Ce n'est pas le gras du lait. C'est le signal de croissance qu'il envoie.",
              "a translucent glass of milk with glowing molecules rising from it", ""),
             ("La whey", "Ton shaker de protéines peut déclencher des boutons.",
              "Les protéines de lactosérum font monter l'insuline et l'IGF-1. Plusieurs séries de cas décrivent des poussées "
              "chez les sportifs qui en prennent.",
              "Ce n'est pas le sport. C'est ce qu'il y a dans le shaker.",
              "a translucent protein shaker bottle, the powder inside glowing", ""),
             ("L'intestin", "Ton intestin et ta peau se parlent.",
              "L'axe intestin-peau : le microbiote influence l'inflammation dans tout le corps. Les études sont encore jeunes, "
              "mais le lien est réel.",
              "Ce n'est pas magique. C'est un dialogue qu'on commence à comprendre.",
              "translucent female torso with the intestines glowing", ""),
             ("Le chocolat", "Le chocolat ne donne pas de boutons. Enfin, pas lui.",
              "Le cacao seul n'a pas d'effet clair. Ce sont le sucre et le lait de la tablette qui comptent.",
              "Ce n'est pas le cacao. C'est ce qu'on met autour.",
              "a translucent bar of chocolate with a few squares broken off, glowing", ""),
             ("Le gras", "Manger gras rend-il ta peau grasse ?",
              "Le sébum est fabriqué par tes glandes, pas déposé par ton assiette. Ce qui compte, c'est l'effet du repas sur "
              "ton insuline.",
              "Ce n'est pas l'huile de tes frites. C'est la tienne.",
              "a translucent cube of skin with one glowing oil gland inside, a few translucent french fries floating beside it", ""),
             ("La vitamine B12", "Ta vitamine B12 peut te donner des boutons.",
              "Les fortes doses de B12, surtout en injection, sont connues pour déclencher des poussées : elle change le "
              "comportement de la bactérie de l'acné.",
              "Ce n'est pas un complément anodin. C'est un déclencheur connu.",
              "a translucent vitamin capsule glowing above a translucent skin pore", ""),
             ("Le gluten", "Tu as arrêté le gluten pour ta peau ? Écoute ça.",
              "Aucune étude ne montre que le gluten cause l'acné. La maladie cœliaque existe, mais elle se diagnostique, et "
              "l'acné n'en est pas un signe.",
              "Ce n'est pas le pain. C'est une mode.",
              "a translucent ear of wheat glowing", ""),
         ]),
    dict(n=4, name="Ton cerveau décodé", glow="electric violet (#B44CFF)", tint="#B44CFF",
         why="Le stress, le sommeil, les gestes : le cerveau comme organe de la peau. L'angle le plus intime du compte.",
         eps=[
             ("Le stress", "Une semaine d'examens peut se voir sur ta peau.",
              "Le stress libère du cortisol et une hormone, la CRH, que les glandes à sébum savent capter. Chez des étudiants, "
              "l'acné s'aggravait en période d'examens.",
              "Ce n'est pas dans ta tête. C'est sur ta peau.",
              "a translucent female head with the brain glowing and glowing nerve paths running down to the face", ""),
             ("Les nerfs", "Tes nerfs fabriquent de l'inflammation dans ta peau.",
              "Sous le stress, les terminaisons nerveuses de la peau libèrent la substance P, qui stimule les glandes à sébum "
              "et l'inflammation.",
              "Ce n'est pas une image. Tes nerfs touchent vraiment tes pores.",
              "a translucent cube of skin with glowing nerve fibres wrapped around an oil gland", ""),
             ("Le sommeil", "Les nuits courtes se paient sur ta peau.",
              "Le manque de sommeil est associé à plus d'acné et à un cortisol plus haut. La nuit, la peau répare sa barrière.",
              "Ce n'est pas un luxe. C'est le moment où ta peau se répare.",
              "a translucent female head asleep on a translucent pillow, the brain glowing softly", ""),
             ("Les mains", "Tu touches ton visage environ 23 fois par heure.",
              "Une étude a filmé des étudiants : 23 contacts par heure, près de la moitié sur la bouche, le nez et les yeux. "
              "Pression et bactéries en prime.",
              "Ce n'est pas ta peau qui va chercher les boutons. Ce sont tes mains.",
              "a translucent hand approaching a translucent female face, the fingertips glowing", ""),
             ("L'envie de percer", "Pourquoi tu n'arrives pas à t'empêcher de percer.",
              "Percer soulage une tension, et le cerveau en fait une récompense. Mais la paroi du pore cède, l'inflammation "
              "s'étend, la marque s'installe.",
              "Ce n'est pas un manque de volonté. C'est un circuit à casser.",
              "a translucent brain with one small reward circuit deep inside glowing", ""),
             ("Le moral", "Tes boutons peuvent toucher ton moral. Ce n'est pas exagéré.",
              "L'acné est associée à un risque plus élevé de dépression, surtout l'année qui suit le diagnostic. En parler fait "
              "partie du soin.",
              "Ce n'est pas superficiel. C'est ta santé.",
              "a translucent female head bowed down, the brain glowing dimly", ""),
             ("La lumière des écrans", "La lumière de ton écran abîme-t-elle ta peau ?",
              "La lumière bleue sert même à traiter l'acné en cabinet. Le vrai souci du téléphone, c'est l'écran collé à ta "
              "joue.",
              "Ce n'est pas la lumière. C'est le contact.",
              "a translucent smartphone casting glowing light onto a translucent female face", ""),
             ("Le cercle vicieux", "Le stress donne des boutons, et les boutons donnent du stress.",
              "La boucle se nourrit d'elle-même : stress, poussée, miroir, stress. On la casse par un seul bout : un geste "
              "régulier, pas la panique.",
              "Tu n'es pas fragile. Tu es dans une boucle.",
              "a translucent brain and a translucent female face joined by one glowing loop", ""),
         ]),
    dict(n=5, name="Les faux coupables", glow="toxic neon green (#2EE59D)", tint="#2EE59D",
         why="Les organes et les croyances qu'on accuse à tort. Des accroches choc, des réponses vraies : le format qui fait "
             "réagir en commentaire.",
         eps=[
             ("Le foie", "Ton foie est-il en train de « s'encrasser » ?",
              "Le foie filtre le sang en continu ; il ne « rejette » rien par ta peau. Aucune cure détox n'a montré d'effet sur "
              "l'acné.",
              "Ce n'est pas ton foie qui déborde. C'est un mythe qui se vend bien.",
              "a translucent female torso with the liver glowing", ""),
             ("Le sang « sale »", "Et si tes boutons venaient d'un sang sale ?",
              "L'idée du « sang impur » date d'avant la médecine moderne. Un bouton naît dans le pore : sébum, cellules mortes, "
              "bactérie, inflammation.",
              "Ce n'est pas ton sang. C'est ton pore.",
              "a translucent blood vessel with glowing blood cells flowing inside", ""),
             ("Les toxines", "Ta peau essaie-t-elle d'évacuer des toxines ?",
              "La sueur est faite d'eau à plus de 99 %. Ce sont le foie et les reins qui éliminent les déchets, pas les pores.",
              "Ce n'est pas une évacuation. C'est un pore qui se bouche.",
              "a translucent cube of skin with glowing sweat glands and a few droplets on its surface", ""),
             ("Les deux litres d'eau", "Tu bois deux litres d'eau par jour pour ta peau. Ça sert vraiment à quelque chose ?",
              "S'hydrater est utile au corps, mais aucune étude ne montre que boire plus fait disparaître l'acné. Les reins "
              "éliminent simplement le surplus.",
              "Ce n'est pas ta soif. C'est ton sébum.",
              "a pair of translucent kidneys glowing next to a translucent glass of water", ""),
             ("Le soleil", "Le soleil sèche tes boutons. Puis il les fait revenir.",
              "Le bronzage masque les rougeurs et épaissit la surface de la peau, ce qui peut boucher les pores. Et les UV "
              "foncent les marques.",
              "Ce n'est pas un traitement. C'est un camouflage qui laisse des traces.",
              "a blazing sun glowing above a translucent female face", ""),
             ("Le dentifrice", "Ne mets jamais de dentifrice sur un bouton.",
              "Le dentifrice irrite et brûle la peau : rougeur, plaques, et parfois une marque plus foncée que le bouton "
              "lui-même.",
              "Ce n'est pas un remède de grand-mère. C'est une brûlure.",
              "a translucent tube of toothpaste, a glowing drop of paste at its tip", ""),
             ("La « purge »", "Ta peau s'aggrave avec ton nouveau soin. Purge… ou alerte ?",
              "Une vraie purge vient des actifs qui accélèrent le renouvellement, dans tes zones habituelles, et dure quelques "
              "semaines. Ailleurs, avec un autre produit, c'est une réaction.",
              "Ta peau ne se nettoie pas. Elle réagit peut-être à un produit.",
              "a translucent cube of skin with several glowing pores emptying upward", ""),
             ("L'acné qui n'en est pas", "Ces petits boutons qui grattent ne sont peut-être pas de l'acné.",
              "La folliculite à Malassezia, une levure : petits boutons tous identiques, qui démangent, sur le front, la "
              "poitrine ou le dos. Les traitements de l'acné ne la soignent pas.",
              "Ce n'est pas de l'acné. C'est une levure.",
              "a translucent hair follicle with tiny glowing round yeast cells inside", ""),
         ]),
    dict(n=6, name="Ta peau décodée", glow="electric cyan (#22D3EE)", tint="#22D3EE",
         why="La peau vue comme un organe : ce qui vit dedans, ce qui la protège, ce qu'elle garde en mémoire. Le chapitre qui "
             "referme la saison et ouvre la suivante.",
         eps=[
             ("Ton plus grand organe", "Ton plus grand organe, c'est ta peau.",
              "Environ 2 m² et plusieurs kilos : une barrière vivante, avec ses glandes, ses nerfs, ses vaisseaux et son "
              "immunité.",
              "Ce n'est pas une surface. C'est un organe.",
              "a translucent standing female body, its whole skin surface glowing", ""),
             ("Les glandes à sébum", "Ton visage compte des centaines de glandes à huile par centimètre carré.",
              "Le visage et le cuir chevelu sont les zones les plus riches en glandes sébacées. Elles protègent la peau ; quand "
              "elles s'emballent, les pores se bouchent.",
              "Ce n'est pas un défaut. C'est une usine qui tourne trop fort.",
              "a translucent cube of skin with many glowing oil glands inside", ""),
             ("Les bactéries", "Un million de bactéries vivent sur chaque centimètre carré de ta peau.",
              "Le microbiome cutané te protège. La bactérie de l'acné en fait partie : c'est son déséquilibre, pas sa "
              "présence, qui pose problème.",
              "Ce n'est pas de la saleté. C'est un écosystème.",
              "a translucent skin surface covered with many tiny glowing bacteria", ""),
             ("Les acariens", "Tu as des acariens sur le visage. Tout le monde en a.",
              "Les Demodex vivent dans les follicules de presque tous les adultes. En nombre normal, ils sont inoffensifs ; en "
              "excès, ils sont liés à la rosacée, pas à l'acné.",
              "Ce n'est pas un manque d'hygiène. C'est un colocataire.",
              "a translucent hair follicle with a few tiny glowing mites inside", ""),
             ("Le renouvellement", "Ta peau change de surface en quelques semaines.",
              "Les cellules montent de la base vers la surface, puis tombent. Dans l'acné, elles collent dans le pore au lieu "
              "de partir : c'est le début du bouchon.",
              "Ta peau n'est pas sale. Elle ne lâche pas ses cellules.",
              "a translucent cross-section of skin layers with glowing cells rising toward the surface", ""),
             ("Le pH", "Ta peau est acide. Et c'est voulu.",
              "Sa surface est autour de pH 5. Les savons très alcalins la déséquilibrent : la barrière s'affaiblit, la peau "
              "s'irrite.",
              "Ce n'est pas une peau à décaper. C'est une peau à respecter.",
              "a translucent cube of skin covered by a thin glowing protective film", ""),
             ("L'immunité", "Ta peau a sa propre armée.",
              "Des cellules immunitaires montent la garde dans l'épiderme. Un bouton rouge, c'est elles qui réagissent.",
              "Ce n'est pas une saleté. C'est une défense.",
              "a translucent cube of skin with many glowing immune cells gathering around one pore", ""),
             ("Les marques", "La marque reste plus longtemps que le bouton.",
              "Après l'inflammation, la peau produit trop de mélanine. La marque s'estompe en quelques mois, mais le soleil "
              "la fonce.",
              "Ce n'est pas une cicatrice. C'est une mémoire qui s'efface.",
              "a translucent cube of skin with glowing pigment cells under one dark spot on its surface", ""),
         ]),
]
