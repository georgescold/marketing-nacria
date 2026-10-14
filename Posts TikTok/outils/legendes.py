"""Title, description and 5 hashtags of the 30 posts (accounts A, B, C), keyed by the post folder name.

Hashtags: 2 broad, high-volume tags the model accounts use (#acne 208 bn views, #boutons, #skincare) + 2-3 topic or community tags
from the hashtag volumes in research_notes (#acnehormonal 1.7 bn, #sopk 1.5 bn, #acnepositivity 3.6 bn, #acnescars 12 bn, ...).
Account C captions tell the story in the 3rd person: the heroines are illustrated characters, never presented as real customers.
"""

PISTES = "\n\nCe sont des pistes du quotidien, pas un diagnostic : si ton acné te fait mal ou s'aggrave, parles-en à un dermatologue."
DOUTE = "\n\n⚠️ Ce sont des liens connus, pas un diagnostic. En cas de doute, parles-en à un médecin."

A = {
    "A01_ce_que_tes_boutons_veulent_dire": (
        "Ce que tes boutons veulent dire 😳",
        "Front, nez, joues, menton, mâchoire : chaque zone a ses déclencheurs du quotidien 👀 Enregistre ce post pour ta prochaine "
        "poussée et dis-moi en commentaire où sortent les tiens 👇" + PISTES,
        "#acne #boutons #skincare #astuces #acnehormonal"),
    "A02_boutons_avant_les_regles": (
        "Tes boutons avant les règles, expliqués 🩸",
        "Menton, mâchoire, joues, front : ce qui se passe sur ta peau la semaine avant tes règles. Tu n'es pas « sale », c'est ton "
        "cycle 🤍 Enregistre et envoie-le à ta copine qui a les mêmes boutons chaque mois." + PISTES,
        "#acne #acnehormonal #regles #boutons #skincare"),
    "A03_ce_que_ta_machoire_essaie_de_te_dire": (
        "Ce que ta mâchoire essaie de te dire",
        "Les boutons le long de la mâchoire, c'est l'acné typique de l'adulte. Frottements, marques… et parfois un signe à montrer "
        "à ton médecin (boutons + poils + règles irrégulières). Enregistre pour t'en souvenir 📌" + PISTES,
        "#acne #acneadulte #acnehormonal #sopk #boutons"),
    "A04_boutons_a_30_ans": (
        "Des boutons à 30 ans ? Voilà ce que ça veut dire",
        "L'acné adulte touche surtout les femmes, souvent sur le bas du visage. Tu n'es pas « en retard » : ta peau réagit à ce que "
        "tu vis 🤍 Dis-moi ton âge en commentaire, tu vas voir qu'on est nombreuses 👇" + PISTES,
        "#acne #acneadulte #boutons #skincare #confianceensoi"),
    "A05_boutons_apres_la_pilule": (
        "Tes boutons après la pilule, expliqués 💊",
        "Tu as arrêté la pilule et ta peau a changé ? C'est fréquent : elle se réajuste, et ça peut prendre plusieurs mois. Ce n'est "
        "pas ta faute 🤍 Pour tout ce qui touche à ta contraception, parles-en à ton médecin.",
        "#acne #arretpilule #pilule #acnehormonal #boutons"),
    "A06_ce_que_tes_nuits_font_a_ta_peau": (
        "Ce que tes nuits font à ta peau 🌙",
        "Taie d'oreiller, téléphone contre la joue, crème trop riche, nuits trop courtes : tes nuits laissent des traces sur ta "
        "peau. Enregistre ce post et change ta taie ce soir 😴" + PISTES,
        "#acne #boutons #sommeil #skincare #astuces"),
    "A07_ce_que_ton_stress_fait_a_ta_peau": (
        "Ce que ton stress fait à ta peau",
        "Période chargée = poussée de boutons ? Le stress joue sur le sébum, et tes mains font le reste. Enregistre ce post pour ta "
        "prochaine deadline 🤍" + PISTES,
        "#acne #stress #boutons #skincare #acnehormonal"),
    "A08_ce_que_tes_marques_te_disent": (
        "Ce que tes marques te disent",
        "Marques brunes, rouges, creux ou croûtes : elles ne veulent pas dire la même chose. Crème solaire tous les jours, et pour "
        "les creux, un dermatologue peut t'aider. Enregistre 📌",
        "#acne #acnescars #boutons #skincare #peau"),
    "A09_ce_que_ta_routine_fait_a_ta_peau": (
        "Ce que ta routine fait à ta peau",
        "Tu n'as pas tout essayé. Tu as tout essayé en même temps. Nettoyant décapant, gommage tous les jours, trois actifs le même "
        "soir : ta barrière n'en peut plus. Moins de produits, mais tous les jours 🤍",
        "#acne #skincareroutine #boutons #skincaretips #peau"),
    "A10_boutons_et_assiette": (
        "Ce que tes boutons disent de ton assiette 🍫",
        "Sucre, lait, whey, fast-food : certaines habitudes peuvent jouer sur tes boutons, mais ça varie d'une personne à l'autre. "
        "Pas besoin de tout supprimer : note tes repas et tes poussées pour trouver TES déclencheurs." + PISTES,
        "#acne #boutons #alimentation #skincare #astuces"),
}

B = {
    "B01_ton_corps_te_parle": (
        "Ce que tes boutons disent de ton corps 😳",
        "Menton, mâchoire, nez… mais aussi ton stress, ton sucre et ton sommeil. Ta peau te donne des indices 👀 Enregistre ce post "
        "et envoie-le à quelqu'un qui a des boutons au même endroit." + DOUTE,
        "#acne #boutons #acnehormonal #sante #peau"),
    "B02_boutons_hormonaux": (
        "Tes boutons hormonaux, expliqués 😳",
        "Règles, pilule, poils au menton, fatigue, lait… Les boutons hormonaux ont souvent un point commun : ils reviennent au même "
        "endroit. Boutons + poils + règles irrégulières ? Parles-en à ton médecin 🤍" + DOUTE,
        "#acne #acnehormonal #sopk #pilule #boutons"),
    "B03_ton_quotidien_et_ta_peau": (
        "Ton quotidien abîme ta peau sans que tu le saches 😳",
        "Téléphone, après-shampoing, casque, sport, doigts… et soleil sur tes marques. Enregistre ce post et dis-moi lequel tu fais "
        "tous les jours 👇" + DOUTE,
        "#acne #boutons #skincare #astuces #skincaretips"),
    "B04_ta_routine_et_tes_boutons": (
        "Ta routine aggrave peut-être tes boutons 😳",
        "Gommage, nouvelle crème chaque semaine, pinceaux jamais lavés… Parfois, le problème n'est pas ta peau, c'est la routine. "
        "Moins de produits, mieux choisis 🤍" + DOUTE,
        "#acne #skincareroutine #boutons #skincaretips #peau"),
    "B05_les_saisons_et_ta_peau": (
        "Ce que les saisons font à ta peau 😳",
        "Plage, froid, chaleur, écharpe, fêtes, vacances : chaque saison a ses pièges pour ta peau. Enregistre pour l'été ET pour "
        "l'hiver 📌" + DOUTE,
        "#acne #boutons #skincare #skincaretips #peau"),
    "B06_ton_stress_se_voit": (
        "Ton stress se voit sur ta peau 😳",
        "Stress, examens, grignotage, mains sur le visage… Ton stress laisse des traces, et tes réflexes aussi. Tag la copine qui "
        "est en pleine période de rush 👇" + DOUTE,
        "#acne #stress #boutons #acnehormonal #sante"),
    "B07_emplacement_de_tes_boutons": (
        "Ce que l'emplacement de tes boutons veut dire 😳",
        "Front, nez, joues, menton, mâchoire, tempes : chaque zone a ses déclencheurs. Le tien, c'est lequel ? 👇" + DOUTE,
        "#acne #boutons #acnehormonal #skincare #astuces"),
    "B08_boutons_sur_le_corps": (
        "Tes boutons sur le corps aussi te parlent 😳",
        "Dos, épaules, décolleté, cou, nuque, cuir chevelu : l'acné ne s'arrête pas au visage. Sueur, frottements, produits "
        "capillaires… Enregistre ce post avant ta prochaine séance de sport 📌" + DOUTE,
        "#acne #boutons #sport #skincare #peau"),
    "B09_ce_que_tes_marques_veulent_dire": (
        "Ce que tes marques veulent dire 😳",
        "Taches brunes, marques rouges, creux, croûtes, boutons sous la peau : ne les traite pas tous pareil. Et surtout, ne perce "
        "rien 🙅‍♀️" + DOUTE,
        "#acne #acnescars #boutons #skincare #peau"),
    "B10_les_gestes_qui_empirent_tes_boutons": (
        "Les gestes qui empirent tes boutons 😳",
        "Dentifrice sur un bouton, dormir maquillée, sauter la crème solaire, toucher ton visage, nuits courtes, gommage tous les "
        "jours… Lequel tu fais encore ? 👇" + DOUTE,
        "#acne #boutons #astuces #skincaretips #skincare"),
}

C = {
    "exemple 1": (
        "Elle laissait son miroir décider de sa journée",
        "Elle a 28 ans. Ses boutons sont revenus deux ans après l'arrêt de sa pilule.\n\nLe matin, c'était le miroir qui décidait de "
        "sa journée. Au bureau, elle cachait son menton. Le soir, elle comparait sa peau à des visages filtrés, et elle achetait un "
        "produit de plus.\n\nUn jour, elle a tout simplifié : trois gestes, toujours la même routine, une photo par semaine dans la "
        "même lumière.\n\nSes boutons n'ont pas disparu en une nuit. Mais elle a arrêté de laisser sa peau décider de sa journée. 🤍",
        "#acne #acneadulte #confianceensoi #skincare #acnepositivity"),
    "exemple 2": (
        "Une poussée de boutons 3 semaines avant le mariage de sa sœur",
        "Sa sœur se marie dans trois semaines. Elle est témoin. Et sa peau a choisi ce moment-là pour faire une poussée.\n\nElle a "
        "tout acheté. Le gommage, l'acide, le masque, le sérum « miracle ». Dix produits le même soir. Le lendemain, sa peau était "
        "rouge et lui brûlait.\n\nAlors elle a tout repris à zéro : trois gestes, matin et soir, et une photo par semaine pour arrêter "
        "de paniquer devant le miroir.\n\nLe jour J, ses boutons étaient toujours là. Elle a dansé quand même. Et sur les photos, on "
        "voit surtout son sourire. 🤍",
        "#acne #acneadulte #mariage #confianceensoi #acnepositivity"),
    "exemple 3": (
        "Ses boutons sont arrivés 3 mois après l'arrêt de la pilule",
        "Elle a arrêté la pilule à 26 ans. Trois mois plus tard, sa mâchoire s'est couverte de boutons.\n\nAu repas de famille, sa "
        "tante lui a dit de « faire attention à ce qu'elle mange ». Le premier rendez-vous chez la dermato était dans quatre mois.\n\n"
        "En attendant, elle a arrêté d'écouter tout le monde. Une routine simple, une photo chaque semaine, ses règles notées à côté."
        "\n\nLe jour du rendez-vous, elle n'est pas arrivée en disant « je sais pas, ça va, ça vient ». Elle est arrivée avec ses "
        "photos de chaque semaine. Et pour la première fois, elle s'est sentie écoutée. 🤍",
        "#acne #arretpilule #acneadulte #acnehormonal #confianceensoi"),
    "exemple 4": (
        "Elle a annulé son premier rendez-vous à cause de ses boutons",
        "Elle avait un match. Un vrai, qui la faisait rire depuis deux semaines.\n\nLa veille du rendez-vous, elle a mis trois couches "
        "de fond de teint. Puis elle s'est regardée dans le miroir… et elle a annulé.\n\nSa meilleure amie est venue avec du thé et "
        "lui a dit : « Il veut te voir toi. Pas ta peau. »\n\nQuelques semaines plus tard : une routine simple, moins de maquillage, "
        "et un nouveau message. « On retente ? »\n\nAu café, elle a oublié son menton au bout de cinq minutes. Lui n'a regardé que ses "
        "yeux. 🤍",
        "#acne #acneadulte #premierrendezvous #confianceensoi #acnepositivity"),
    "exemple 5": (
        "Elle coupait sa caméra à chaque réunion",
        "Chaque matin, la même réunion en visio. Et chaque matin, elle coupait sa caméra avant que quelqu'un voie son front.\n\nSon "
        "carré noir avec ses initiales, c'était plus simple. Le soir, elle superposait les couches d'anticernes.\n\nPuis elle a arrêté "
        "de se battre contre sa peau : trois gestes simples, une photo par semaine, toujours dans la même lumière.\n\nUn lundi, elle a "
        "pris une grande inspiration… et elle a allumé sa caméra. Personne n'a parlé de ses boutons. Tout le monde a parlé de son "
        "idée. 🤍",
        "#acne #acneadulte #teletravail #confianceensoi #acnepositivity"),
    "exemple 6": (
        "Elle se levait avant lui pour se maquiller",
        "Tous les matins, elle se levait avant lui. Fond de teint, anticernes, et retour au lit comme si de rien n'était.\n\nUn matin, "
        "il a ouvert la porte de la salle de bain. Elle s'est caché le visage dans les mains.\n\nIl lui a doucement pris les mains. Et "
        "il a souri.\n\nAujourd'hui, le dimanche matin, c'est café au lit. Sans fond de teint. 🤍",
        "#acne #acneadulte #couple #confianceensoi #acnepositivity"),
    "exemple 7": (
        "30 ans, et les mêmes boutons qu'à 15 ans",
        "Pour ses 30 ans, elle a retrouvé une photo d'elle à 15 ans. Mêmes boutons. Même menton.\n\nÀ sa soirée d'anniversaire, elle "
        "s'est cachée derrière son verre. Sur le selfie de groupe, elle a tourné la tête.\n\nPuis une amie lui a montré son propre "
        "menton : « Moi aussi, depuis deux ans. » Elles ont ri pendant dix minutes.\n\nL'acné adulte touche énormément de femmes. "
        "Elle n'était pas en retard. Elle n'était juste pas seule. 🤍",
        "#acne #acneadulte #30ans #confianceensoi #acnepositivity"),
    "exemple 8": (
        "Elle refusait d'enlever son t-shirt à la plage",
        "Dans la cabine d'essayage, elle a vu son dos dans le miroir. Et elle a décidé que cet été, ce serait t-shirt.\n\nÀ la plage, "
        "ses amies l'appelaient depuis l'eau. Elle restait sous le parasol.\n\nPetit à petit, elle a pris soin de sa peau avec trois "
        "gestes simples, et une photo par semaine pour garder le fil sans paniquer.\n\nUn après-midi, elle a enlevé son t-shirt. Ses "
        "boutons étaient toujours là. Elle a couru dans la mer quand même. 🤍",
        "#acne #acneadulte #plage #confianceensoi #acnepositivity"),
    "exemple 9": (
        "Sa petite sœur de 15 ans pleurait à cause de ses boutons",
        "Sa petite sœur de 15 ans pleurait dans son oreiller. Sous son dernier selfie, des commentaires sur ses boutons.\n\nElle "
        "s'est revue au même âge, dans la même chambre, avec les mêmes larmes.\n\nAlors elle a soulevé sa frange : « Regarde. Moi "
        "aussi. À 28 ans. »\n\nCe soir-là, elles ont fait leur routine ensemble. Trois gestes. Des fous rires. Et une promesse : ne "
        "plus jamais se cacher. 🤍",
        "#acne #acneadulte #soeur #confianceensoi #acnepositivity"),
    "exemple 10": (
        "Elle gardait sa capuche à la salle de sport",
        "À la salle, elle gardait sa capuche. Même pendant les squats. Même quand elle avait trop chaud.\n\nDans les vestiaires, elle "
        "regardait son front et ses tempes, là où le bandeau frottait.\n\nElle a simplifié : trois gestes, un bandeau propre, une "
        "douche juste après le sport.\n\nUn jour, elle a baissé sa capuche et attaché ses tresses. Ses boutons étaient toujours là. "
        "Elle a fini le cours en riant. 🤍",
        "#acne #acneadulte #sport #confianceensoi #acnepositivity"),
}
