"""TikTok covers of « Ce qui arrive à ta peau » (nutrition new format). Usage: python covers_peau.py  (FAL_KEY in env)"""
import pathlib, sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import comptes  # noqa: E402
import miniatures_porcelaine as mp  # noqa: E402
from fal import run  # noqa: E402

COVERS = {  # episode: (hero object, subject, hook) — the hook asks, it never gives the verdict away
    "T01_sucre": ("two puffed rice cakes topped with thin slices of avocado on a small matte plate", "Les galettes de riz",
                  "plus de sucre que du sucre ?"),
    "T02_lait": ("a tall glass of skimmed milk next to a small jug of milk", "Le lait écrémé",
                 "le pire choix pour ta peau ?"),
    "T03_chocolat": ("a few squares of 85 percent dark chocolate on a small saucer", "Le chocolat noir",
                     "vraiment innocent pour ta peau ?"),
    "T04_whey": ("a protein shaker bottle next to a scoop of pale protein powder", "La whey",
                 "coupable de tes boutons ?"),
    "T05_latte": ("a tall glass of iced caramel latte with a straw", "Le latte au sirop",
                  "ta récompense, ta peau la paie ?"),
    "T06_gluten": ("a few slices of very white gluten-free bread on a matte plate", "Le sans gluten",
                   "tu te prives pour rien ?"),
}


def one(ep):
    obj, subject, hook = COVERS[ep]
    d = comptes.root(comptes.EPISODES[ep]) / ep
    hero = d / "cover_hero.png"
    if not hero.exists():
        run("fal-ai/nano-banana-pro", {"prompt": mp.COVER_HERO.format(obj=obj), "aspect_ratio": "9:16", "num_images": 1},
            hero)
    out = d / f"{ep[:3]} - Miniature.jpg"
    mp.cover_porcelaine(hero, subject, hook, out)
    return f"{ep}: {out.name}"


if __name__ == "__main__":
    with ThreadPoolExecutor(6) as ex:
        for r in ex.map(one, COVERS):
            print(r, flush=True)
