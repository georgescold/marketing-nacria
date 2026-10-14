import jobs_x
from jobs_dark import ZONE
X = jobs_x.XRAY
R, O, B = "red", "orange-red", "electric blue"
V = {
 "v_sebum": ("magnified anatomical cross-section of human skin showing a hair follicle with a large swollen sebaceous oil gland full of sebum", O),
 "v_cuir_chevelu": ("magnified anatomical cross-section of the human scalp showing many hair follicles, hair roots and their oil glands", O),
 "v_barriere": ("magnified anatomical cross-section of the layers of human skin, the thin top protective barrier layer cracked and inflamed", B),
 "v_sueur": ("magnified anatomical cross-section of human skin showing coiled sweat glands and their ducts", B),
 "v_sopk": ("pair of human ovaries covered with several small round cysts, attached to the uterus, anatomical", R),
 "v_pancreas": ("human pancreas with glowing insulin-producing islets", O),
 "v_melanine": ("magnified anatomical cross-section of human skin with melanocytes releasing dark melanin pigment, sun rays hitting the surface", O),
 "v_follicule": ("magnified anatomical cross-section of a deep swollen inflamed hair follicle filled with pus under the skin (cystic acne)", R),
}
JOBS = {k: ("4:3", X.format(view="neck and chest", where="", item=i, color=c)) for k, (i, c) in V.items()}
JOBS.update({
 "z_kyste": ("4:3", ZONE.format(z="the jawline", skin="light olive skin").replace("ONE clearly visible red inflamed pimple", "ONE large deep, swollen, red cystic pimple")),
 "z_sopk": ("4:3", ZONE.format(z="the chin, with a few coarse dark hairs", skin="fair skin").replace("ONE clearly visible red inflamed pimple placed exactly in the centre of the frame, a couple of smaller ones nearby", "a cluster of several red pimples in the centre of the frame among a few coarse dark chin hairs")),
 "z_partout": ("4:3", ZONE.format(z="the lower cheek and chin", skin="deep brown skin").replace("ONE clearly visible red inflamed pimple placed exactly in the centre of the frame, a couple of smaller ones nearby", "a sudden dense cluster of many small red inflamed pimples in the centre of the frame")),
})
