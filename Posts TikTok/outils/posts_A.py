"""Account A (face map, @glowhubdaily format): 10 posts, their illustration prompts and their CTA settings.

Each post: one character (base portrait in the beige painted style), a title slide, 4-5 zone slides (illustration +
3 short causes) and the Nacria CTA. Illustrations are nano-banana edits of the character base, with the acne clearly
visible (user rule, 2026-10-05).
"""

# Base portraits: existing ones (A, B, C) and new ones generated from text with the same style prompt.
BASE = ("Soft digital painting illustration, editorial and minimal. Front-facing head-and-shoulders portrait of {who}, eyes gently "
        "closed, calm neutral expression, {hair}, bare shoulders, smooth even skin with no blemishes, symmetrical face looking straight "
        "at the viewer. Plain warm pearly beige background with a very subtle nacre sheen. Soft diffuse light, muted warm palette. The "
        "face and shoulders occupy the lower two thirds of the frame, generous empty background space above the head. No text, no "
        "logo, no jewelry.")
CHARS = {
    "A": dict(file="base_nb.png"),
    "B": dict(file="B_base1.png"),
    "C": dict(file="C_base1.png", dark=True),
    "D": dict(file="D_base.png", prompt=BASE.format(who="a young adult French woman of East Asian descent around 27 with light warm skin",
                                                    hair="straight black hair tied in a low ponytail with a few loose strands")),
    "E": dict(file="E_base.png", prompt=BASE.format(who="a young adult French woman of North African descent around 29 with light olive-tan skin",
                                                    hair="long dark-brown wavy hair falling on her shoulders")),
    "F": dict(file="F_base.png", prompt=BASE.format(who="a young adult French woman around 25 with very fair skin and light freckles",
                                                    hair="long wavy copper-red hair")),
}

KEEP = ("Keep the exact same woman, face, hair, pose, framing, background, lighting and painting style; change nothing else. "
        "Eyes stay closed. ")
ACNE = ("Draw the acne so it is clearly visible even on a small phone screen and looks like real acne, softly painted: small and medium "
        "red papules, matte (never glossy bubbles or beads), with a little diffuse pinkish-red redness around them, a few tiny whiteheads, "
        "varied sizes, irregular placement. Not gory, no blood, no red lines or streaks. Never on hair, eyebrows or lips.")
ONLY = (" IMPORTANT: every part of her face not named above stays exactly as clean and smooth as in the reference image, and her neck "
        "and shoulders stay exactly as in the reference image.")
DARK = (" On her deep brown skin the pimples are slightly raised matte bumps a little darker than her skin with a reddish-purple tint, "
        "blended into the skin (never beads), with flat dark marks around them, still clearly visible.")
FRECKLES = " The pimples are clearly red and raised, easy to tell apart from her flat light freckles."


def zone(where):
    return f"Add clearly visible acne {where}. "


TITLE = zone("on several areas: a few pimples on the forehead, more on the cheeks, the chin and along the jaw")

# (slug, character, title, CTA headline (line 1, line 2 in terracotta), first name in the app, slides)
# slide = (image prompt, [3 causes])
POSTS = [
    ("ce_que_tes_boutons_veulent_dire", "A", "Ce que tes boutons veulent dire", ("Ta peau te parle.", "Apprends à l’écouter."), "Léa", [
        (zone("only on the forehead (8 to 12 pimples)"), ["produits coiffants qui coulent", "frange qui frotte", "taie d'oreiller pas changée"]),
        (zone("only on the nose and right beside the nostrils"), ["sébum en excès", "toucher ton nez toute la journée", "crème solaire trop épaisse"]),
        (zone("only on both cheeks (a scattered cluster on each cheek)"), ["écran de téléphone", "pinceaux pas lavés", "mains sur les joues"]),
        (zone("only on the chin"), ["variations hormonales", "stress", "menton posé sur la main"]),
        (zone("only along the jawline on both sides"), ["cycle menstruel", "écharpe ou col qui frotte", "démaquillage trop rapide"]),
    ]),
    ("boutons_avant_les_regles", "B", "Ce que tes boutons avant les règles veulent dire", ("Ce n’est pas toi.", "C’est ton cycle."), "Chloé", [
        (zone("only on the chin (a dense cluster)"), ["hormones qui varient avant les règles", "peau plus grasse ces jours-là", "main sous le menton"]),
        (zone("only along the jawline: a few bigger, deeper, swollen red bumps without white heads"),
         ["pic d'hormones en fin de cycle", "pores qui se bouchent plus vite", "stress des jours avant les règles"]),
        (zone("only on both cheeks"), ["envies de sucre", "tu dors moins bien", "tu touches plus ton visage"]),
        (zone("only on the forehead; her nose, cheeks, chin and jaw stay completely clear"), ["fatigue", "routine du soir sautée", "cheveux plus gras"]),
    ]),
    ("ce_que_ta_machoire_essaie_de_te_dire", "C", "Ce que ta mâchoire essaie de te dire", ("Tes boutons ne disent rien", "de ta valeur."), "Awa", [
        (zone("only along the jawline on both sides"), ["variations hormonales", "stress qui dure", "mains sur la mâchoire"]),
        (zone("only under the jawline and on the top of the neck"), ["col roulé ou écharpe", "jugulaire de casque", "téléphone coincé contre l'épaule"]),
        (zone("only on the chin"), ["main sous le menton", "masque ou cache-cou qui frotte", "baume à lèvres qui déborde"]),
        ("Add many flat round dark-brown post-acne marks along the jawline, and three or four small raised pimples among them. ",
         ["boutons percés ou triturés", "soleil sans crème solaire", "gommage trop fort"]),
        (zone("on the chin and along the jaw, and add a few fine dark hairs on the chin"),
         ["déséquilibre hormonal (SOPK)", "souvent avec des poils au menton", "et des règles irrégulières", "parles-en à ton médecin"]),
    ]),
    ("boutons_a_30_ans", "D", "Ce que tes boutons à 30 ans veulent dire", ("Des boutons à 30 ans ?", "Tu n’es pas en retard."), "Mai", [
        (zone("only on the chin"), ["variations hormonales", "arrêt ou changement de pilule", "charge mentale"]),
        (zone("only along the jawline on both sides"), ["stress au travail", "nuits trop courtes", "col ou écharpe qui frotte"]),
        (zone("only on both cheeks, with the skin of the cheeks slightly red"), ["trop de produits en même temps", "gommages trop fréquents", "nettoyant trop agressif"]),
        (zone("only on the forehead, along the hairline"), ["casquette ou bandeau", "produits capillaires", "sueur du sport"]),
    ]),
    ("boutons_apres_la_pilule", "E", "Ce que tes boutons après la pilule veulent dire", ("Ta peau se réajuste.", "Laisse-lui du temps."), "Yasmine", [
        (zone("only on the chin (a dense cluster)"), ["arrêt de la pilule", "hormones qui se rééquilibrent", "peau plus grasse qu'avant"]),
        (zone("only along the jawline on both sides"), ["retour de ton cycle naturel", "hormones qui varient avant les règles", "stress du changement"]),
        (zone("only on both cheeks; her forehead, nose, chin and jaw stay completely clear"), ["trop de nouveaux produits d'un coup", "gommages pour « rattraper »", "maquillage pour cacher"]),
        (zone("only on the forehead"), ["stress de « tout gérer »", "sommeil en vrac", "routine qui change chaque semaine"]),
    ]),
    ("ce_que_tes_nuits_font_a_ta_peau", "F", "Ce que tes nuits font à ta peau", ("Prends soin de tes nuits.", "Ta peau aussi les vit."), "Lou", [
        (zone("only on one cheek, the left cheek, a dense cluster"), ["toujours dormir du même côté", "taie d'oreiller pas changée", "téléphone contre la joue au lit"]),
        (zone("only on the forehead"), ["cheveux sur le visage la nuit", "produits coiffants sur l'oreiller", "frange la nuit"]),
        (zone("only on the chin"), ["main sous le menton en dormant", "crème de nuit trop riche", "dormir maquillée"]),
        (zone("on the forehead, both cheeks and the chin, and her face looks tired with light dark circles"),
         ["moins de 7 h de sommeil", "coucher tard et décalé", "stress qui empêche de dormir"]),
    ]),
    ("ce_que_ton_stress_fait_a_ta_peau", "A", "Ce que ton stress fait à ta peau", ("Ta peau encaisse", "ce que tu tais."), "Léa", [
        (zone("only on the chin and around the mouth corners, not on the lips"), ["stress qui augmente le sébum", "deadlines et charge mentale", "menton dans la main"]),
        (zone("only on both cheeks, a few of them picked and red with tiny scabs"), ["tu touches ton visage sans y penser", "tu tritures tes boutons", "téléphone collé à la joue"]),
        (zone("only on the forehead"), ["nuits trop courtes", "repas sautés puis sucre", "café à la place de l'eau"]),
        (zone("only along the jawline on both sides"), ["main sur la mâchoire en réunion", "col qui frotte toute la journée", "casque ou écouteurs toute la journée"]),
    ]),
    ("ce_que_tes_marques_te_disent", "C", "Ce que tes marques te disent", ("Tes marques racontent", "ce que tu as traversé."), "Awa", [
        ("Add many flat round dark-brown post-acne marks on both cheeks, and two or three small raised pimples. ",
         ["bouton percé ou trituré", "soleil sans crème solaire", "inflammation qui a duré"]),
        ("Add flat dark red-purple marks where pimples healed on the chin and the jaw, and two raised pimples. ",
         ["inflammation récente", "frotter ou gommer", "eau trop chaude"]),
        ("Add several small round shallow depressed acne scars (pitted, ice-pick and rolling scars) on both cheeks. ",
         ["boutons profonds", "boutons percés ou triturés", "inflammation qui a duré longtemps"]),
        ("Add three or four small healing scabs over picked pimples and a few raised pimples on the chin. ",
         ["arracher les croûtes", "patchs retirés trop tôt", "pas de crème solaire"]),
    ]),
    ("ce_que_ta_routine_fait_a_ta_peau", "D", "Ce que ta routine fait à ta peau", ("Tu n’as pas tout essayé.", "Tu as tout essayé en même temps."), "Mai", [
        ("Her cheeks look red, irritated and slightly flaky, with several raised red pimples on them. ",
         ["nettoyant trop décapant", "eau trop chaude", "frotter avec la serviette"]),
        (zone("on the forehead: many small skin-coloured and pink bumps (closed comedones) and a few bigger red pimples"),
         ["trop de produits en même temps", "nouvelle crème chaque semaine", "crème trop riche"]),
        (zone("only on the nose, with visible blackheads and the skin of the nose slightly red"), ["gommage tous les jours", "patchs anti-points noirs", "brosse nettoyante trop souvent"]),
        (zone("on the chin, the skin around the pimples red, dry and slightly peeling"),
         ["acides + rétinol le même soir", "gommage par-dessus", "pas de crème hydratante"]),
    ]),
    ("boutons_et_assiette", "B", "Ce que tes boutons disent de ton assiette", ("Ton assiette compte.", "Ta culpabilité, non."), "Chloé", [
        (zone("only on the forehead; her nose, cheeks, chin and jaw stay completely clear"), ["beaucoup de sucres rapides", "boissons sucrées", "grignotage tard le soir"]),
        (zone("only on the chin"), ["beaucoup de lait (surtout écrémé)", "protéines en poudre (whey)", "repas sautés puis sucre"]),
        (zone("only on both cheeks"), ["fast-food fréquent", "alcool le week-end", "peu de fruits et légumes"]),
        (zone("on the forehead, both cheeks and the chin"), ["repas très sucrés", "grignotage toute la journée", "boissons énergisantes"]),
    ]),
]


def prompt(char, text):
    p = KEEP + text + ACNE
    if "several areas" in text or "tired" in text:
        p += " Her neck and shoulders stay exactly as in the reference image."
    elif "neck" not in text:
        p += ONLY
    if CHARS[char].get("dark"):
        p += DARK
    if char == "F":
        p += FRECKLES
    return p


def jobs():
    """name -> (character, prompt) for every illustration of the batch."""
    out = {}
    for n, (slug, char, *_rest, slides) in enumerate(POSTS, 1):
        out[f"A{n:02d}_0"] = (char, prompt(char, TITLE))
        for k, (text, _causes) in enumerate(slides, 1):
            out[f"A{n:02d}_{k}"] = (char, prompt(char, text))
    return out
