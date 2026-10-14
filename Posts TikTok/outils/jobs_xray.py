XRAY = ("Dark cinematic 3D medical illustration, landscape, on a near-black background with subtle floating {color} particles. "
        "A hyper-realistic glossy 3D {item}, VERY LARGE and centred, filling about 60 percent of the image width, glowing intensely {color} "
        "from within, with glowing {color} veins and capillaries branching out around it like a living organ in an anatomy scan. "
        "Behind it only a very faint, barely visible translucent dark-blue outline of a human {view}. The top fifth of the image is dark. "
        "Dramatic lighting, high contrast, vivid. No text, no labels, no logo, no brand name.{where}")
FRONT = ("neck and chest", "")
BACK = ("neck and upper back seen from behind", "")
FRONT_OBJ = ("neck and chest", "")
R, O, B = "red", "orange-red", "electric blue"
X = {
 "x_coeur": ("human heart with its aorta and blood vessels", R, FRONT), "x_foie": ("human liver", O, FRONT),
 "x_reins": ("pair of human kidneys", B, FRONT), "x_hormones": ("thyroid and endocrine glands", B, FRONT),
 "x_intestin": ("human intestines", O, FRONT), "x_uterus": ("female uterus and ovaries", R, FRONT),
 "x_cerveau": ("human brain", B, FRONT_OBJ), "x_main": ("human hand showing its bones", B, FRONT_OBJ),
 "x_doigts": ("pair of fingertips squeezing", R, FRONT_OBJ), "x_creme_solaire": ("tube of sunscreen", O, FRONT_OBJ),
 "x_telephone": ("smartphone", B, FRONT_OBJ), "x_shampoing": ("bottle of shampoo", B, FRONT_OBJ),
 "x_shampoing_sec": ("can of dry shampoo spray", O, FRONT_OBJ), "x_oreiller": ("bed pillow", B, FRONT_OBJ),
 "x_pince": ("hair clip", O, FRONT_OBJ), "x_palette": ("makeup palette and lipstick", R, FRONT_OBJ),
 "x_flacons": ("cluster of many skincare bottles and jars", R, FRONT_OBJ), "x_serviette": ("folded bath towel", B, FRONT_OBJ),
 "x_soleil": ("blazing sun", O, FRONT_OBJ), "x_ecouteurs": ("pair of wireless earbuds", B, FRONT_OBJ),
 "x_casque_audio": ("pair of over-ear headphones", B, FRONT_OBJ), "x_echarpe": ("knitted wool scarf", R, FRONT_OBJ),
 "x_lunettes": ("pair of glasses", B, FRONT_OBJ), "x_apres_shampoing": ("bottle of hair conditioner dripping", B, BACK),
 "x_sac": ("backpack", O, BACK), "x_brassiere": ("sports bra", R, FRONT_OBJ), "x_elastique": ("wet ponytail with a hair elastic", B, BACK),
 "x_rasoir": ("razor", B, FRONT_OBJ), "x_bandeau": ("sports headband", B, FRONT_OBJ), "x_lune": ("crescent moon and alarm clock", B, FRONT_OBJ),
 "x_soda": ("can of soda with sugar cubes", O, FRONT_OBJ), "x_lait": ("glass of milk", B, FRONT_OBJ), "x_pinceaux": ("set of makeup brushes", R, FRONT_OBJ),
 "x_eponge": ("makeup blending sponge", O, FRONT_OBJ), "x_fond_de_teint": ("bottle of liquid foundation", O, FRONT_OBJ),
 "x_primer": ("tube of makeup primer", B, FRONT_OBJ), "x_rouge_levres": ("lipstick", R, FRONT_OBJ), "x_masque": ("disposable face mask", B, FRONT_OBJ),
 "x_dentifrice": ("tube of toothpaste", B, FRONT_OBJ), "x_casque_velo": ("bicycle helmet with its chin strap", O, FRONT_OBJ),
 "x_tshirt": ("sweaty sports t-shirt", R, BACK), "x_shaker": ("protein shaker bottle", O, FRONT_OBJ),
}
JOBS = {k: ("4:3", XRAY.format(view=v[0], where=v[1], item=i, color=c)) for k, (i, c, v) in X.items()}
