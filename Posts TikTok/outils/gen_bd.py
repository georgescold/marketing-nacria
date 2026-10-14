"""Generate and render the account 3 (BD) story carousels listed in bd_stories.STORIES.

Usage (FAL_KEY must be set in the environment): python gen_bd.py [story ...]
For each story: s1 from text (nano-banana), s2-s7 as edits of s1 (same woman, same style), saved in
../compte BD/visuels <exemple>/, then render_bd.py builds ../compte BD/<exemple>/slide_01..08.png.
About 7 images x $0.04 = $0.28 per carousel. Existing images are kept, so a rerun only redoes what is missing.
"""
import sys
from concurrent.futures import ThreadPoolExecutor

import render_bd
from bd_stories import ACNE, SAME, STORIES, STYLE
from fal import run, upload

BD = render_bd.R.HERE.parent / "compte BD"


def vis(name):
    d = BD / f"visuels {STORIES[name]['folder']}"
    d.mkdir(parents=True, exist_ok=True)
    return d


def first(name):
    out = vis(name) / "s1.png"
    if not out.exists():
        st = STORIES[name]
        run("fal-ai/nano-banana", {"prompt": STYLE + st["char"] + ACNE + "Scene: " + st["s1"], "aspect_ratio": "3:4", "num_images": 1}, out)
    return name


def edit(job):
    name, k = job
    out = vis(name) / f"{k}.png"
    if out.exists():
        return f"{name} {k} exists"
    scene = STORIES[name][k]
    prompt, refs = (scene[0], ["s1"] + scene[1]) if isinstance(scene, tuple) else (SAME + scene, ["s1"])
    if any(not (vis(name) / f"{r}.png").exists() for r in refs):
        return f"{name} {k} waiting for {refs}"
    err = ""
    for _ in range(3):
        try:
            run("fal-ai/nano-banana/edit", {"prompt": prompt, "image_urls": [upload(str(vis(name) / f"{r}.png")) for r in refs],
                                            "num_images": 1}, out)
            return f"{name} {k} ok"
        except Exception as e:
            err = str(e)[:120]
    return f"{name} {k} ERROR {err}"


if __name__ == "__main__":
    names = sys.argv[1:] or list(STORIES)
    with ThreadPoolExecutor(3) as ex:
        print("s1 ok:", list(ex.map(first, names)), flush=True)
    jobs = [(n, f"s{i}") for n in names for i in range(2, 8)]
    for _ in range(2):  # second pass for scenes that use another scene as an extra reference
        with ThreadPoolExecutor(8) as ex:
            for line in ex.map(edit, jobs):
                print(line, flush=True)
    for n in names:
        if all((vis(n) / f"s{i}.png").exists() for i in range(1, 8)):
            render_bd.main(vis(n), BD / STORIES[n]["folder"])
