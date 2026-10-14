"""Generate the account B photos (bNN_k, 16:9) and the new organ renders (o_*, 4:3) listed in posts_B (FAL_KEY must be set).

Usage: python gen_B.py [name ...]   (default: everything missing). Images go to ../compte organes/visuels/.
"""
import pathlib, sys
from concurrent.futures import ThreadPoolExecutor

from fal import run
from posts_B import ORGANS, photo_jobs

VIS = pathlib.Path(__file__).parent.resolve().parent / "compte organes" / "visuels"


def job(item):
    name, (ratio, prompt) = item
    out = VIS / f"{name}.png"
    if out.exists():
        return f"{name} exists"
    err = ""
    for _ in range(3):
        try:
            run("fal-ai/nano-banana", {"prompt": prompt, "aspect_ratio": ratio, "num_images": 1}, out)
            return f"{name} ok"
        except Exception as e:
            err = str(e)[:120]
    return f"{name} ERROR {err}"


if __name__ == "__main__":
    todo = {k: ("16:9", p) for k, p in photo_jobs().items()}
    todo.update({k: ("4:3", p) for k, p in ORGANS.items()})
    if sys.argv[1:]:
        todo = {k: v for k, v in todo.items() if k in sys.argv[1:]}
    with ThreadPoolExecutor(8) as ex:
        for line in ex.map(job, todo.items()):
            print(line, flush=True)
