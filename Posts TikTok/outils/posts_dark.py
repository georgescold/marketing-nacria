"""10 carousels for the dark "organ" account, same structure as @factslipv9n:
slide 1 and 2 = one panel, slide 3 and 4 = two panels side by side, then the Nacre CTA.
Each panel: (top, zone photo, anatomy visual, bottom). In `top`, "|" breaks the line and [..] is yellow.
The organ shown is the one really involved (sebaceous glands, hormones, scalp, skin barrier, sweat, stress, SOPK...)."""

def Z(zone, photo, vis, bottom):
    return ("Si tu as un bouton|" + zone, photo, vis, bottom)

# Building blocks: zone -> body part actually involved
NEZ = lambda p="z_nez1": Z("sur le [Nez]", p, "v_sebum", "Alors prends soin de ton Sébum !")
JOUES = lambda p="z_joue1": Z("sur les [Joues]", p, "v_barriere", "Alors protège ta Barrière cutanée !")
MACHOIRE = lambda p="z_machoire1": Z("sur la [Mâchoire]", p, "x_uterus", "Alors prends soin de tes Hormones !")
MENTON = lambda p="z_menton1": Z("sur le [Menton]", p, "x_uterus", "Alors surveille ton Cycle !")
COU = lambda p="z_cou": Z("sur le [Cou]", p, "x_hormones", "Alors prends soin de tes Hormones !")
SOUS_MENTON = lambda p="z_sous_menton": Z("sous le [Menton]", p, "x_hormones", "Alors prends soin de tes Hormones !")
FRONT = lambda p="z_front1": Z("sur le [Front]", p, "v_cuir_chevelu", "Alors soigne ton Cuir chevelu !")
TEMPES = lambda p="z_tempes": Z("sur les [Tempes]", p, "v_cuir_chevelu", "Alors soigne ton Cuir chevelu !")
NUQUE = lambda p="z_nuque": Z("sur la [Nuque]", p, "v_cuir_chevelu", "Alors soigne ton Cuir chevelu !")
OREILLES = lambda p="z_oreille": Z("sur les [Oreilles]", p, "v_sebum", "Alors prends soin de ton Sébum !")
BOUCHE = lambda p="z_bouche": Z("autour de la [Bouche]", p, "v_barriere", "Alors protège ta Barrière cutanée !")
DOS = lambda p="z_dos": Z("sur le [Dos]", p, "v_sueur", "Alors surveille ta Transpiration !")
DECOLLETE = lambda p="z_decollete": Z("sur le [Décolleté]", p, "v_sueur", "Alors surveille ta Transpiration !")
EPAULES = lambda p="z_epaules": Z("sur les [Épaules]", p, "v_sueur", "Alors surveille ta Transpiration !")
STRESS = lambda p="z_partout": ("Si tu as des boutons|[d'un coup]", p, "x_cerveau", "Alors prends soin de ton Stress !")
SOPK = lambda p="z_sopk": ("Des boutons + des|[règles irrégulières] ?", p, "v_sopk", "Parle du SOPK à ton médecin !")
SUCRE = lambda p="z_cote_menton": ("Si tu as des boutons|après le [Sucre]", p, "v_pancreas", "Alors surveille ta Glycémie !")
PROFOND = lambda p="z_kyste": ("Si tu as un bouton|[profond] et douloureux", p, "v_follicule", "Alors va voir un Dermato !")
MARQUES = lambda p="z_marques": ("Si tes boutons|laissent des [Marques]", p, "v_melanine", "Alors protège-toi du Soleil !")

POSTS = [
    # 1: exact mirror of their post (nose, cheeks, jawline + ears, forehead + nose)
    ("visage", "Ce que tes boutons disent de ton corps 😳", [
        NEZ("z_nez1"), JOUES("z_joue1"), (MACHOIRE("z_machoire1"), OREILLES()), (FRONT("z_front2"), NEZ("z_nez2"))]),
    ("hormones", "Ton corps essaie de te parler 😳", [
        MACHOIRE("z_machoire2"), FRONT("z_front1"), (DOS(), DECOLLETE()), (MENTON("z_menton1"), COU())]),
    ("sopk", "Ne prends pas ça à la légère 😳", [
        SOPK(), MENTON("z_menton2"), (MACHOIRE("z_machoire1"), COU()), (STRESS(), SUCRE())]),
    ("cuir_chevelu", "Personne ne t'a jamais dit ça 😳", [
        FRONT("z_front3"), TEMPES(), (NUQUE(), DOS()), (NEZ("z_nez1"), JOUES("z_joue2"))]),
    ("profond", "Si tu as ça, lis jusqu'au bout 😳", [
        PROFOND(), MARQUES(), (JOUES("z_joue3"), BOUCHE()), (MACHOIRE("z_machoire2"), MENTON("z_menton3"))]),
    ("stress", "Ton corps essaie de te dire quelque chose 😳", [
        STRESS(), SUCRE(), (MENTON("z_menton1"), FRONT("z_front2")), (NEZ("z_nez2"), JOUES("z_joue1"))]),
    ("corps", "Ce que les boutons sur ton corps disent 😳", [
        DOS(), DECOLLETE(), (EPAULES(), NUQUE()), (COU(), MACHOIRE("z_machoire1"))]),
    ("joues", "Ce que tes boutons disent de toi 😳", [
        JOUES("z_joue2"), NEZ("z_nez1"), (FRONT("z_front1"), MENTON("z_menton2")), (PROFOND(), MARQUES())]),
    ("cycle", "Les femmes de 25-35 ans, regardez ça 😳", [
        MENTON("z_menton3"), SOPK(), (SUCRE(), STRESS()), (SOUS_MENTON(), MACHOIRE("z_machoire2"))]),
    ("oreilles", "Tu ne regarderas plus tes boutons pareil 😳", [
        OREILLES(), TEMPES(), (NEZ("z_nez2"), FRONT("z_front3")), (JOUES("z_joue3"), MACHOIRE("z_machoire1"))]),
]


# Position (x, y as a fraction of the photo) of the circled pimple in each close-up.
RING = {
    "z_bouche": (0.51, 0.37), "z_bras": (0.55, 0.58), "z_cote_menton": (0.4, 0.52), "z_cou": (0.55, 0.53), "z_decollete": (0.56, 0.63),
    "z_dos": (0.51, 0.55), "z_epaules": (0.51, 0.61), "z_front1": (0.53, 0.52), "z_front2": (0.54, 0.64), "z_front3": (0.42, 0.44),
    "z_joue1": (0.43, 0.52), "z_joue2": (0.56, 0.48), "z_joue3": (0.45, 0.42), "z_machoire1": (0.51, 0.49), "z_machoire2": (0.47, 0.46),
    "z_marques": (0.41, 0.45), "z_menton1": (0.5, 0.51), "z_menton2": (0.40, 0.45), "z_menton3": (0.49, 0.46), "z_nez1": (0.46, 0.48),
    "z_nez2": (0.54, 0.5), "z_nuque": (0.6, 0.61), "z_oreille": (0.37, 0.55), "z_sous_menton": (0.57, 0.53), "z_tempes": (0.42, 0.55),
    "z_kyste": (0.43, 0.45), "z_sopk": (0.48, 0.45), "z_partout": (0.48, 0.36),
}

# Anatomy visuals (y_*): focus point (x, y as fractions) of the organ and zoom, so it fills the panel like theirs.
FOCUS = {
    "y_ovaires": (.5, .52, 1.75), "y_sopk": (.5, .52, 1.75), "y_hormones": (.5, .52, 1.35), "y_surrenales": (.5, .42, 1.7),
    "y_pancreas": (.47, .64, 1.6), "y_cerveau": (.5, .42, 1.55), "y_sebum": (.5, .5, 1.5),
}

PROTO = ("proto", "Ce que tes boutons disent de ton corps 😳", [
    ("Si tu as un bouton|sur le [Menton]", "z_menton1", "y_ovaires", "Alors surveille ton Cycle !"),
    ("Si tu as des boutons|quand tu es [Stressée]", "z_joue2", "y_surrenales", "Alors baisse ton Cortisol !"),
    (("Si tu as un bouton|sur la [Mâchoire]", "z_machoire1", "y_hormones", "Alors prends soin de tes Hormones !"),
     ("Si tu as des boutons|après le [Sucre]", "z_cote_menton", "y_pancreas", "Alors surveille ta Glycémie !")),
    (("Si tu as un bouton|sur le [Nez]", "z_nez1", "y_sebum", "Alors prends soin de ton Sébum !"),
     ("Si tu as des boutons|quand tu dors [Mal]", "z_front2", "y_cerveau", "Alors prends soin de ton Sommeil !")),
])

# v2 assets (realistic acne photos p_*, close-up organ renders o_*)
RING.update({"p_menton": (0.44, 0.58), "p_stress": (0.50, 0.45), "p_machoire": (0.43, 0.52), "p_sucre": (0.48, 0.52),
             "p_nez": (0.50, 0.33), "p_sommeil": (0.48, 0.45)})
FOCUS.update({"o_ovaires": (.5, .48, 1.12), "o_surrenales": (.5, .5, 1.12), "o_hormones": (.5, .55, 1.08), "o_pancreas": (.45, .55, 1.1),
              "o_sebum": (.5, .5, 1.05), "o_cerveau": (.55, .5, 1.08)})

PROTO2 = ("proto_v2", "Ce que tes boutons disent de ton corps 😳", [
    ("Si tu as un bouton|sur le [Menton]", "p_menton", "o_ovaires", "Prends soin de ton Cycle !"),
    ("Si tu as des boutons|quand tu es [Stressée]", "p_stress", "o_surrenales", "Baisse ton Cortisol !"),
    (("Si tu as un bouton|sur la [Mâchoire]", "p_machoire", "o_hormones", "Prends soin de tes Hormones !"),
     ("Si tu as des boutons|après le [Sucre]", "p_sucre", "o_pancreas", "Surveille ta Glycémie !")),
    (("Si tu as un bouton|sur le [Nez]", "p_nez", "o_sebum", "Prends soin de ton Sébum !"),
     ("Si tu as des boutons|quand tu dors [Mal]", "p_sommeil", "o_cerveau", "Prends soin de ton Sommeil !")),
])
