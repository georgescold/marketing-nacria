"""Account B (dark "organ" carousels, @factslipv9n format): 10 posts of 6 panels + the Nacria CTA.

Structure of each post, like the model: slide 1 and 2 = one panel each (1080x1620), slide 3 and 4 = two panels side by side
(1536x1024), slide 5 = CTA. A panel = (top band with the zone in [yellow], photo id, organ id, bottom yellow line).
Only real, well-known links (no "nose = heart"): hormones and cycle, stress, sleep, sugar and dairy, sebum, friction,
bacteria, sweat, picking, sun and marks, skin barrier, PCOS (pointing to a doctor).
Photo ids are bNN_k (generated from PHOTOS), organ ids are o_* (existing ones + ORGANS below).
"""

PHOTO = ("Realistic close-up skin photograph like a dermatology reference picture of real acne, {what}. The acne is clearly visible even "
         "on a small phone screen: moderate acne, a dense cluster of 8 to 15 raised inflamed red papules and pustules of different sizes "
         "with clear redness around them, one of them bigger and close to the centre of the image. Warm natural light, soft focus, real skin texture with visible pores, slightly matte skin, no makeup "
         "unless described, natural colours, not glossy, not airbrushed, not gory, no blood. Wide landscape framing. No text.")

ORGAN = ("Premium photorealistic 3D medical render, close-up: {organ} fills about 70 percent of the frame width, glossy and slightly "
         "translucent, glowing softly from within in {color}, with fine {vessels} blood vessels. Behind it only a faint dark-blue "
         "translucent outline of the body ({body}). Very dark navy background with tiny light particles. The top 15 percent of the "
         "image is dark. Not gory. No text, no labels, no logo.")

SKIN = "a face in profile"
SKINORG = ("Premium photorealistic 3D medical render: a large glowing magnified {organ}, floating in the centre of the frame and filling "
           "about 70 percent of its width, glossy and slightly translucent, glowing intensely from within in {color}, with fine {vessels} "
           "blood vessels around it, like a precious anatomical organ. Behind it only a faint dark-blue translucent outline of {body}. Very "
           "dark navy background with tiny light particles. The top 15 percent of the image is dark. Not gory. No text, no labels, no logo.")
ORGANS = {
    "o_sopk": ORGAN.format(organ="the uterus with two enlarged ovaries covered with many small round fluid-filled cysts", color="pink-purple",
                           vessels="red", body="hips"),
    "o_follicule": SKINORG.format(organ="a large magnified cut-away of a skin pore: a hair follicle blocked by a plug of sebum and dead skin "
                                      "cells, forming a dark blackhead at the surface", color="orange-yellow", vessels="red", body=SKIN),
    "o_barriere": SKINORG.format(organ="a magnified cut-away of the skin layers whose top protective layer is cracked and broken like dry "
                                     "earth, with small red irritated areas", color="pink-red", vessels="red", body=SKIN),
    "o_melanine": SKINORG.format(organ="a magnified cut-away of the skin layers with star-shaped melanocyte cells releasing dark brown pigment "
                                     "granules toward the surface", color="amber with dark brown pigment", vessels="red", body=SKIN),
    "o_bacteries": SKINORG.format(organ="a magnified view of the skin surface and an open pore covered with clusters of rod-shaped bacteria",
                                color="teal and orange", vessels="red", body=SKIN),
    "o_sueur": SKINORG.format(organ="a magnified cut-away of the skin of the back showing coiled sweat glands and their ducts releasing "
                                  "droplets of sweat next to a hair follicle", color="aqua blue and orange", vessels="red", body="upper back"),
    "o_cuir_chevelu": SKINORG.format(organ="a magnified cut-away of the scalp at the hairline showing hair follicles with their oil glands",
                                   color="orange", vessels="red", body="head"),
    "o_inflammation": SKINORG.format(organ="a magnified cut-away of an inflamed pimple under the skin: a swollen red pocket filled with white "
                                         "immune cells, surrounded by red inflamed tissue", color="red-orange", vessels="red", body=SKIN),
    "o_collagene": SKINORG.format(organ="a magnified cut-away of the skin showing the dermis as a network of collagen fibres, broken and "
                                      "missing under a small depressed scar at the surface", color="pink-white", vessels="red", body=SKIN),
}
# Focus point (x, y as fractions) and zoom of each organ render inside the panel. Existing ones are in posts_dark.FOCUS.
FOCUS = {k: (.5, .5, 1.08) for k in ORGANS}

# (slug, caption title, [6 panels]); panel = (top band, organ, bottom line, photo description)
POSTS = [
    ("ton_corps_te_parle", "Ce que tes boutons disent de ton corps 😳", [
        ("Si tu as un bouton|sur le [Menton]", "o_ovaires", "Prends soin de ton Cycle !",
         "the lower face of a young woman with light skin, lips and chin, a cluster of inflamed pimples on the chin"),
        ("Si tu as des boutons|quand tu es [Stressée]", "o_surrenales", "Baisse ton Cortisol !",
         "the cheek of a young woman with medium olive skin, a cluster of many red papules and a few whiteheads, part of the nose and lips at the edge"),
        ("Si tu as un bouton|sur la [Mâchoire]", "o_hormones", "Prends soin de tes Hormones !",
         "the jawline and lower cheek of a young Black woman with deep brown skin seen in profile, raised inflamed pimples and dark marks along the jaw"),
        ("Si tu as des boutons|après le [Sucre]", "o_pancreas", "Surveille ta Glycémie !",
         "the side of the chin and the corner of the mouth of a young woman with light tan skin, a cluster of red pimples and small bumps"),
        ("Si tu as un bouton|sur le [Nez]", "o_sebum", "Prends soin de ton Sébum !",
         "an extreme close-up of the nose of a young woman with fair skin, one big red inflamed pimple on the tip of the nose, a few blackheads on the sides"),
        ("Si tu as des boutons|quand tu dors [Mal]", "o_cerveau", "Prends soin de ton Sommeil !",
         "the forehead of a young East Asian woman with her hairline at the top, several red pimples across the centre of the forehead"),
    ]),
    ("boutons_hormonaux", "Tes boutons hormonaux, expliqués 😳", [
        ("Si tu as des boutons|avant tes [Règles]", "o_ovaires", "Note ton Cycle !",
         "the chin and lower lip of a young woman with light olive skin, a cluster of deep red inflamed pimples on the chin"),
        ("Si tu as des boutons|après la [Pilule]", "o_hormones", "Tes Hormones se réajustent !",
         "the lower cheek and jawline of a young woman with fair freckled skin, many red pimples and bumps along the jaw"),
        ("Si tu as des boutons|et des [Poils] au menton", "o_sopk", "Parle du SOPK à ton Médecin !",
         "the chin of a young woman with medium brown skin, several inflamed pimples and a few fine dark hairs on the chin"),
        ("Si tu as des boutons|quand tu es [Épuisée]", "o_cerveau", "Dors plus de 7 heures !",
         "the temple and the side of the forehead of a young woman with light skin, a cluster of red pimples, slightly dull tired skin"),
        ("Si tu as des boutons|après le [Lait]", "o_pancreas", "Surveille le Lait !",
         "the side of the chin and the jaw of a young Black woman with dark brown skin, several raised pimples and dark spots"),
        ("Si tu as des boutons|sur le [Cou]", "o_follicule", "Évite les cols qui Frottent !",
         "the side of the neck under the jaw of a young woman with light skin, a cluster of red pimples"),
    ]),
    ("ton_quotidien_et_ta_peau", "Ton quotidien abîme ta peau sans que tu le saches 😳", [
        ("Si tu as des boutons|sur les [Joues]", "o_bacteries", "Nettoie ton Téléphone !",
         "the cheek of a young woman with light skin, the edge of a smartphone pressed against the cheek at the side of the frame, many red pimples on the cheek"),
        ("Si tu as des boutons|sur le [Front]", "o_cuir_chevelu", "Rince ton Après-shampoing !",
         "the forehead and hairline of a young woman with olive skin, damp hair at the top edge, many small red pimples along the hairline"),
        ("Si tu as des boutons|sur les [Tempes]", "o_follicule", "Nettoie ton Casque !",
         "the temple of a young woman with medium brown skin, the cushion of over-ear headphones at the edge of the frame, several red pimples on the temple"),
        ("Si tu as des boutons|sur le [Dos]", "o_sueur", "Douche-toi après le Sport !",
         "the upper back and shoulder blades of a young woman with light skin, a few sweat droplets, many red pimples and bumps"),
        ("Si tu [Perces]|tes boutons", "o_inflammation", "Laisse-les Guérir !",
         "the chin of a young woman with fair skin, two fingertips close to a big red inflamed pimple, the skin around it red"),
        ("Si tes boutons laissent|des [Taches]", "o_melanine", "Mets ta Crème solaire !",
         "the cheek of a young woman with medium tan skin, many flat brown post-acne marks and two red pimples"),
    ]),
    ("ta_routine_et_tes_boutons", "Ta routine aggrave peut-être tes boutons 😳", [
        ("Si tu as des boutons|et la peau qui [Brûle]", "o_barriere", "Protège ta Barrière cutanée !",
         "the cheek of a young woman with fair skin, red irritated slightly flaky skin with several red pimples"),
        ("Si tu as des boutons|après un [Gommage]", "o_inflammation", "Gomme moins souvent !",
         "the forehead of a young woman with light olive skin, red irritated skin and a cluster of inflamed pimples"),
        ("Si tu as des boutons|avec ta [Nouvelle] crème", "o_follicule", "Un seul Nouveau produit !",
         "the forehead of a young Black woman with dark brown skin, many small skin-coloured bumps (closed comedones) and a few inflamed pimples"),
        ("Si tu as des points noirs|sur le [Nez]", "o_sebum", "Nettoie sans Décaper !",
         "an extreme close-up of the nose of a young woman with light skin, many blackheads on the nose and one red pimple near the centre"),
        ("Si tu as des boutons|sous ton [Maquillage]", "o_bacteries", "Lave tes Pinceaux !",
         "the cheek of a young woman with light skin wearing slightly cakey foundation over red pimples, a makeup brush at the edge of the frame"),
        ("Si tes boutons laissent|des [Marques]", "o_melanine", "Mets du SPF tous les jours !",
         "the cheek and jaw of a young North African woman with light brown skin, many brown post-acne marks and a few red pimples"),
    ]),
    ("les_saisons_et_ta_peau", "Ce que les saisons font à ta peau 😳", [
        ("Si tu as des boutons|après la [Plage]", "o_melanine", "Mets ta Crème solaire !",
         "the cheek of a young woman with tanned skin, a few grains of sand, red pimples and darker marks"),
        ("Si tu as des boutons|quand il fait [Froid]", "o_barriere", "Hydrate ta Barrière !",
         "the cheek of a young woman with fair skin, red dry chapped skin from the cold, a knitted scarf at the edge, several red pimples"),
        ("Si tu as des boutons|quand il fait [Chaud]", "o_sueur", "Rince ta Sueur !",
         "the forehead of a young woman with medium brown skin, beads of sweat and many red pimples"),
        ("Si tu as des boutons|sous ton [Écharpe]", "o_follicule", "Évite ce qui Frotte !",
         "the jaw and neck of a young woman with light skin, a wool scarf touching the jaw at the bottom edge, a cluster of red pimples along the jaw"),
        ("Si tu as des boutons|après les [Fêtes]", "o_pancreas", "Doucement sur le Sucre !",
         "the chin of a young woman with olive skin, a little glitter makeup left on the cheek, several inflamed pimples"),
        ("Si tu as des boutons|en [Vacances]", "o_cerveau", "Dors à heures Fixes !",
         "the cheek of a young woman with light sun-kissed freckled skin, several red pimples"),
    ]),
    ("ton_stress_se_voit", "Ton stress se voit sur ta peau 😳", [
        ("Si tu as des boutons|quand tu es [Stressée]", "o_surrenales", "Baisse ton Cortisol !",
         "the jaw of a young woman with medium brown skin, many inflamed red pimples along the jawline"),
        ("Si tu as des boutons|pendant tes [Examens]", "o_cerveau", "Protège ton Sommeil !",
         "the forehead of a young woman with fair skin and a messy bun at the top edge, a cluster of red pimples"),
        ("Si tu [Tritures]|tes boutons", "o_inflammation", "Lâche ton Miroir !",
         "the chin of a young woman with olive skin, red picked pimples with small scabs and redness"),
        ("Si tu as des boutons|quand tu [Grignotes]", "o_pancreas", "Surveille ta Glycémie !",
         "the corner of the mouth and the chin of a young woman with light skin, several red pimples, a crumb of chocolate on the lip"),
        ("Si tu as des boutons|avant tes [Règles]", "o_ovaires", "Note ton Cycle !",
         "the chin of a young Black woman with deep brown skin, deep raised pimples and dark marks"),
        ("Si tu as un bouton|sur le [Menton]", "o_hormones", "Prends soin de tes Hormones !",
         "the chin of a young East Asian woman with light skin, a cluster of red pimples"),
    ]),
    ("emplacement_de_tes_boutons", "Ce que l'emplacement de tes boutons veut dire 😳", [
        ("Si tu as un bouton|sur le [Front]", "o_cuir_chevelu", "Vérifie ton Shampoing !",
         "the forehead of a young woman with light skin, a fringe of hair at the top edge, several red pimples under the fringe"),
        ("Si tu as un bouton|sur le [Nez]", "o_sebum", "Prends soin de ton Sébum !",
         "an extreme close-up of the nose of a young woman with medium brown skin, one big red inflamed pimple on the side of the nose"),
        ("Si tu as un bouton|sur les [Joues]", "o_bacteries", "Change ta Taie d'oreiller !",
         "the cheek of a young woman with fair freckled skin resting on a white pillow, many red pimples on the cheek"),
        ("Si tu as un bouton|sur le [Menton]", "o_ovaires", "Prends soin de ton Cycle !",
         "the chin of a young woman with olive skin, a cluster of inflamed pimples"),
        ("Si tu as un bouton|sur la [Mâchoire]", "o_hormones", "Prends soin de tes Hormones !",
         "the jawline of a young Black woman with deep brown skin, raised inflamed pimples and dark marks"),
        ("Si tu as un bouton|sur les [Tempes]", "o_follicule", "Nettoie tes Lunettes !",
         "the temple of a young woman with light skin, the arm of her glasses at the edge of the frame, several red pimples on the temple"),
    ]),
    ("boutons_sur_le_corps", "Tes boutons sur le corps aussi te parlent 😳", [
        ("Si tu as des boutons|sur le [Dos]", "o_sueur", "Douche-toi après le Sport !",
         "the upper back of a young woman with medium brown skin, many raised red pimples and dark marks"),
        ("Si tu as des boutons|sur les [Épaules]", "o_follicule", "Gare aux Bretelles !",
         "the shoulder of a young woman with light skin, a bra strap on the shoulder, a cluster of red pimples under and around the strap"),
        ("Si tu as des boutons|sur le [Décolleté]", "o_sebum", "Prends soin de ton Sébum !",
         "the upper chest (décolleté) of a young woman with olive skin, many red pimples"),
        ("Si tu as des boutons|sur le [Cou]", "o_hormones", "Prends soin de tes Hormones !",
         "the side of the neck of a young Black woman with deep brown skin, several raised pimples and dark marks"),
        ("Si tu as des boutons|sur la [Nuque]", "o_bacteries", "Lave ta Taie d'oreiller !",
         "the nape of the neck of a young woman with fair skin, her hair lifted up, several red pimples along the hairline"),
        ("Si tu as des boutons|dans le [Cuir chevelu]", "o_cuir_chevelu", "Rince bien tes Cheveux !",
         "the scalp of a young woman with light skin and brown hair seen from above along a parting, several red bumps along the parting"),
    ]),
    ("ce_que_tes_marques_veulent_dire", "Ce que tes marques veulent dire 😳", [
        ("Si tu as des|taches [Brunes]", "o_melanine", "Mets ta Crème solaire !",
         "the cheek of a young woman with medium brown skin, many flat dark brown post-acne marks and two raised pimples"),
        ("Si tu as des|marques [Rouges]", "o_inflammation", "Laisse ta peau Guérir !",
         "the cheek of a young woman with fair skin, many flat red and pink post-acne marks and two raised pimples"),
        ("Si tu as des [Creux]|après tes boutons", "o_collagene", "Parles-en à un Dermato !",
         "the cheek of a young woman with light olive skin, clearly visible depressed pitted acne scars (round dents in the skin, like a dermatology picture of atrophic scars) and two red pimples"),
        ("Si tu as des boutons|que tu [Perces]", "o_bacteries", "Ne les perce Jamais !",
         "the chin of a young woman with light skin, a squeezed red pimple with redness around it and two other pimples"),
        ("Si tu arraches|tes [Croûtes]", "o_barriere", "Laisse-les tomber Seules !",
         "the chin of a young woman with deep brown skin, small healing scabs over pimples and dark marks"),
        ("Si tu as un bouton|[Sous] la peau", "o_sebum", "Ne le presse surtout Pas !",
         "the cheek of a young woman with light skin, one deep, swollen, red bump under the skin without a white head, near the centre"),
    ]),
    ("les_gestes_qui_empirent_tes_boutons", "Les gestes qui empirent tes boutons 😳", [
        ("Si tu mets du|[Dentifrice] dessus", "o_barriere", "Ça irrite, ça ne soigne Pas !",
         "the chin of a young woman with olive skin, a dab of white toothpaste on a red pimple, other pimples around"),
        ("Si tu dors|[Maquillée]", "o_follicule", "Démaquille-toi chaque Soir !",
         "the cheek of a young woman with light skin, smudged foundation and a little mascara residue near the eye at the edge, several red pimples"),
        ("Si tu sautes la|[Crème solaire]", "o_melanine", "Le Soleil fonce tes Marques !",
         "the cheek of a young woman with medium brown skin in bright sunlight, brown post-acne marks and a few red pimples"),
        ("Si tu touches|ton [Visage]", "o_bacteries", "Garde tes Mains loin !",
         "fingers resting on the cheek of a young woman with fair skin, several red pimples on the cheek"),
        ("Si tu dors|[Peu]", "o_cerveau", "Dors 7 à 9 Heures !",
         "the forehead and temple of a young East Asian woman with light skin, slightly tired skin, a cluster of red pimples"),
        ("Si tu [Gommes]|tous les jours", "o_inflammation", "Gomme moins Souvent !",
         "the cheek of a young woman with fair skin, red irritated shiny skin and several inflamed pimples"),
    ]),
]


def panels(n):
    """Slides of post n (1-based) in the render_dark format: 2 single panels, then 2 pairs."""
    _slug, _title, ps = POSTS[n - 1]
    p = [(top, f"b{n:02d}_{k}", organ, bottom) for k, (top, organ, bottom, _what) in enumerate(ps, 1)]
    return [p[0], p[1], (p[2], p[3]), (p[4], p[5])]


def photo_jobs():
    return {f"b{n:02d}_{k}": PHOTO.format(what=what)
            for n, (_s, _t, ps) in enumerate(POSTS, 1) for k, (_top, _o, _b, what) in enumerate(ps, 1)}

# Position (x, y as fractions of the photo) of the circled pimple, read on the generated photos.
RING = {
    "b01_1": (.49, .64), "b01_2": (.47, .46), "b01_3": (.45, .52), "b01_4": (.48, .45), "b01_5": (.57, .47), "b01_6": (.5, .5),
    "b02_1": (.47, .56), "b02_2": (.45, .48), "b02_3": (.5, .55), "b02_4": (.5, .44), "b02_5": (.46, .52), "b02_6": (.43, .56),
    "b03_1": (.47, .52), "b03_2": (.46, .5), "b03_3": (.46, .48), "b03_4": (.48, .56), "b03_5": (.5, .46), "b03_6": (.5, .48),
    "b04_1": (.6, .42), "b04_2": (.5, .49), "b04_3": (.53, .42), "b04_4": (.5, .42), "b04_5": (.53, .45), "b04_6": (.52, .44),
    "b05_1": (.48, .52), "b05_2": (.55, .48), "b05_3": (.47, .5), "b05_4": (.51, .5), "b05_5": (.47, .5), "b05_6": (.52, .5),
    "b06_1": (.5, .48), "b06_2": (.52, .57), "b06_3": (.42, .5), "b06_4": (.46, .6), "b06_5": (.47, .5), "b06_6": (.5, .47),
    "b07_1": (.5, .55), "b07_2": (.44, .47), "b07_3": (.6, .42), "b07_4": (.48, .5), "b07_5": (.45, .46), "b07_6": (.5, .53),
    "b08_1": (.5, .52), "b08_2": (.55, .52), "b08_3": (.51, .58), "b08_4": (.54, .5), "b08_5": (.48, .63), "b08_6": (.5, .51),
    "b09_1": (.47, .5), "b09_2": (.53, .45), "b09_3": (.53, .47), "b09_4": (.46, .45), "b09_5": (.53, .42), "b09_6": (.5, .49),
    "b10_1": (.52, .38), "b10_2": (.52, .48), "b10_3": (.51, .52), "b10_4": (.56, .45), "b10_5": (.45, .48), "b10_6": (.48, .4),
}
