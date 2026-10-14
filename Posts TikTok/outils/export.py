"""Build the "À publier" folder: one folder per account, one sub-folder per post with its slides (JPEG, ready for TikTok)
and texte.txt (title, description, hashtags), plus a recap text and a preview sheet per account.

Usage: python export.py
"""
import glob, pathlib, re, shutil

from PIL import Image

from legendes import A, B, C

HERE = pathlib.Path(__file__).parent.resolve()
ROOT = HERE.parent
OUT = ROOT / "À publier"
ACCOUNTS = [
    ("Compte A - Carte du visage", "A", A, lambda k: ROOT / "compte carte du visage" / "10 posts" / k),
    ("Compte B - Organes", "B", B, lambda k: ROOT / "compte organes" / "10 posts" / k),
    ("Compte C - BD", "C", C, lambda k: ROOT / "compte BD" / k),
]
REMINDER = ("Au moment de publier : mode photo TikTok, slides dans l'ordre, active « Contenu généré par IA » "
            "(les visuels sont générés), son en tendance.")


def safe(t):
    t = re.sub(r'[<>:"/\\|?*]', "", t).replace("…", "")
    t = "".join(ch for ch in t if ord(ch) < 0x2000 or ch == "’")  # no emojis in folder names
    return re.sub(r"\s+", " ", t).strip().rstrip(".,")


def sheet(folders, dst):
    rows = []
    for f in folders:
        ims = [Image.open(p).convert("RGB") for p in sorted(f.glob("*.jpg"))]
        rows.append([im.resize((round(im.width * 260 / im.height), 260)) for im in ims])
    w = max(sum(i.width + 6 for i in r) for r in rows)
    c = Image.new("RGB", (w, len(rows) * 266), "white")
    for y, r in enumerate(rows):
        x = 0
        for im in r:
            c.paste(im, (x, y * 266))
            x += im.width + 6
    c.save(dst, quality=85)


def main():
    if OUT.exists():
        for child in OUT.iterdir():
            shutil.rmtree(child) if child.is_dir() else child.unlink()
    for acc, letter, caps, src in ACCOUNTS:
        d = OUT / acc
        recap, folders = [f"{acc}\n{REMINDER}\n"], []
        for n, (key, (title, desc, tags)) in enumerate(caps.items(), 1):
            p = d / f"{letter}{n:02d} - {safe(title)}"
            p.mkdir(parents=True)
            for k, s in enumerate(sorted(src(key).glob("slide_*.png")), 1):
                Image.open(s).convert("RGB").save(p / f"{k:02d}.jpg", quality=92, optimize=True)
            text = f"TITRE\n{title}\n\nDESCRIPTION\n{desc}\n\nHASHTAGS\n{tags}\n"
            (p / "texte.txt").write_text(text, encoding="utf-8")
            recap.append(f"\n===== {letter}{n:02d} =====\n{text}")
            folders.append(p)
        (d / f"Légendes {acc}.txt").write_text("".join(recap), encoding="utf-8")
        sheet(folders, d / f"Aperçu {acc}.jpg")
        print("ok", acc, len(folders))


if __name__ == "__main__":
    main()
