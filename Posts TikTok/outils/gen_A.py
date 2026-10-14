"""Generate the account A illustrations listed in posts_A (FAL_KEY must be set).

Usage: python gen_A.py [name ...]   (names like A03_2; default: everything missing)
Bases D/E/F come from text (nano-banana); every slide is an edit of its character base (nano-banana/edit).
Images go to ../compte carte du visage/visuels/. Existing files are kept, so a rerun only redoes what is missing.
"""
import pathlib, sys
from concurrent.futures import ThreadPoolExecutor

from fal import run, upload
from posts_A import CHARS, jobs

HERE = pathlib.Path(__file__).parent.resolve()
SRC = HERE.parent / "illustrations source"
VIS = HERE.parent / "compte carte du visage" / "visuels"
VIS.mkdir(parents=True, exist_ok=True)


def base_path(char):
    f = CHARS[char]["file"]
    return SRC / f if (SRC / f).exists() else VIS / f


def make_base(char):
    p = base_path(char)
    if not p.exists():
        run("fal-ai/nano-banana", {"prompt": CHARS[char]["prompt"], "aspect_ratio": "3:4", "num_images": 1}, p)
    return char


def edit(item):
    name, (char, prompt) = item
    out = VIS / f"{name}.png"
    if out.exists():
        return f"{name} exists"
    err = ""
    for _ in range(3):
        try:
            run("fal-ai/nano-banana/edit", {"prompt": prompt, "image_urls": [upload(str(base_path(char)))], "num_images": 1}, out)
            return f"{name} ok"
        except Exception as e:
            err = str(e)[:120]
    return f"{name} ERROR {err}"


if __name__ == "__main__":
    todo = jobs()
    if sys.argv[1:]:
        todo = {k: v for k, v in todo.items() if k in sys.argv[1:]}
    with ThreadPoolExecutor(3) as ex:
        print("bases:", list(ex.map(make_base, sorted({c for c, _ in todo.values()}))), flush=True)
    with ThreadPoolExecutor(8) as ex:
        for line in ex.map(edit, todo.items()):
            print(line, flush=True)
