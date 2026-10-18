"""After a new voice: move aside the clips now too short for their shot (and the chained clips that start from them), so
that `assets.py <ep> anim` remakes only those. Usage: python clips_a_refaire.py <episode>"""
import pathlib, shutil, sys

import cv2

import assets
import comptes

ep = sys.argv[1]
e = comptes.EPISODES[ep]
d = comptes.root(e) / ep
need = assets.clip_durations(e, d)
old = d / "_clips_trop_courts"
redo = set()
for i, dur in sorted(need.items()):
    c = d / "scenes" / f"line_{i:02d}.mp4"
    if c.exists():
        cap = cv2.VideoCapture(str(c))
        length = cap.get(cv2.CAP_PROP_FRAME_COUNT) / (cap.get(cv2.CAP_PROP_FPS) or 24)
        cap.release()
        if length < dur - 0.15:
            redo.add(i)
changed = True
while changed:  # a chained clip starts from its source's last frame
    changed = False
    for i, j in e.get("chain", {}).items():
        if j in redo and i not in redo:
            redo.add(i)
            changed = True
old.mkdir(exist_ok=True)
for i in sorted(redo):
    for name in [f"line_{i:02d}.mp4"] + ([f"line_{i:02d}.png"] if i in e.get("chain", {}) else []):
        p = d / "scenes" / name
        if p.exists():
            shutil.move(str(p), str(old / name))
print(f"{ep}: clips to remake {sorted(redo)} ({sum(need[i] for i in redo):.1f} s)")
