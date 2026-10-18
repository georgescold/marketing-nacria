"""Final copies of a rendered episode: video.mp4 -> « <EP> - <title>.mp4 » (created from the part title for a new episode),
legende.txt -> « <EP> - Légende.txt », and the loudness of the result. Done in Python so that accented names (« Le café »,
« Partout à la fois ») are never mangled by a shell. Usage: python finir.py <episode>"""
import re, shutil, subprocess, sys

import comptes

ep = sys.argv[1]
e = comptes.EPISODES[ep]
d = comptes.root(e) / ep
p = ep[:3]
final = next(d.glob(f"{p} - *.mp4"), d / f"{p} - {e['part'].split(':', 1)[1].strip()}.mp4")
shutil.copy(d / "video.mp4", final)
shutil.copy(d / "legende.txt", d / f"{p} - L\u00e9gende.txt")
lufs = re.findall(r"I:\s+(-?[\d.]+) LUFS", subprocess.run(["ffmpeg", "-hide_banner", "-i", str(final), "-af", "ebur128", "-f",
                                                            "null", "-"], capture_output=True, text=True,
                                                           errors="replace").stderr)
print(f"-> {final.name}  ({lufs[-1] if lufs else '?'} LUFS)".encode("ascii", "replace").decode())
