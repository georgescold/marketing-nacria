"""Render a batch of face-map carousels in the @glowhubdaily template.

Usage: python render30.py <posts_module_path> [slug]
The posts module defines POSTS = [(slug, title, title_image, [(image, [bullets]), ...], hashtag), ...]
Images are read from ../illustrations source/.
"""
import html, importlib.util, pathlib, sys
from concurrent.futures import ThreadPoolExecutor

import render_gh as R

OUT = R.HERE.parent / "30 posts"
e = html.escape

# Vertical offset (px, image shown 1000 px wide) of the crop window. Default suits head-and-shoulders portraits.
OFFSETS = {}
DEFAULT_OFFSET = -382


def crop_img(name):
    top = OFFSETS.get(name, DEFAULT_OFFSET)
    return (f'<div style="position:absolute;left:40px;top:6px;width:1000px;height:990px;overflow:hidden" class="fade">'
            f'<img src="{(R.IMG / name).as_uri()}" style="position:absolute;left:0;top:{top}px;width:1000px"></div>')


def title_page(title, img):
    return f'''<div style="position:absolute;left:90px;top:150px;width:900px;height:1190px;overflow:hidden" class="fade">
<img src="{(R.IMG / img).as_uri()}" style="position:absolute;left:0;top:0;width:900px"></div>
<div style="position:absolute;left:80px;right:80px;top:110px;text-align:center">
<div class="handle">{e(R.HANDLE)}</div>
<div style="font-size:{70 if len(title) < 48 else 62}px;line-height:1.08;font-weight:800;letter-spacing:-1.5px;margin-top:10px">{e(title)}</div></div>'''


def zone_page(img, items):
    return crop_img(img) + f'<div class="handle" style="position:absolute;right:92px;top:1000px">{e(R.HANDLE)}</div>' + R.bullets(items, 1052)


def render_post(n, post):
    slug, title, timg, slides, _tag = post
    d = OUT / f"{n:02d}_{slug}"
    d.mkdir(parents=True, exist_ok=True)
    pages = [title_page(title, timg)] + [zone_page(i, b) for i, b in slides] + [R.cta_page()]
    for k, body in enumerate(pages, 1):
        R.render(body, d / f"slide_{k:02d}.png")
    return f"{n:02d}_{slug} {len(pages)}"


def main():
    spec = importlib.util.spec_from_file_location("posts", sys.argv[1])
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    OFFSETS.update(getattr(mod, "OFFSETS", {}))
    only = sys.argv[2] if len(sys.argv) > 2 else None
    todo = [(n, p) for n, p in enumerate(mod.POSTS, 1) if not only or p[0] == only]
    with ThreadPoolExecutor(4) as ex:
        for line in ex.map(lambda a: render_post(*a), todo):
            print("ok", line, flush=True)


if __name__ == "__main__":
    main()
