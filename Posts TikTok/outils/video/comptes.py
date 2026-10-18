"""The accounts that share this video pipeline: output folder, plan, episodes and art direction (DA) of each.

An episode belongs to the account whose episodes module defines it (acne: episodes.py, E01_...; organs:
episodes_organes.py, O01_...). Everything else (voice, alignment, music, mix, CTA peak, render) is shared.
"""
import importlib, pathlib

POSTS = pathlib.Path(__file__).resolve().parent.parent.parent  # "Posts TikTok"

ACCOUNTS = {
    # « Les boutons expliqués »: replaces the « Acné solution » carousel account; DA porcelaine nacrée
    "acne": dict(root=POSTS / "compte vidéo", plan="plan", mini="miniatures", episodes="episodes"),
    # « Ton visage décodé »…: the organs carousel account turned video; DA « scanner » (hologram + alert yellow)
    "organes": dict(root=POSTS / "compte organes" / "vidéo", plan="plan_organes", mini="miniatures_organes",
                    episodes="episodes_organes"),
    # « Les aliments accusés »…: food x skin with the persona Margot; DA « food noir & verdict » (evidence stamp)
    "nutrition": dict(root=POSTS / "compte nutrition" / "vidéo", plan="plan_nutrition", mini="miniatures_nutrition",
                      episodes="episodes_nutrition"),
}
SOUNDS = ACCOUNTS["acne"]["root"] / "sons"  # riser, impact and drone, shared by every account

EPISODES = {}
for _name, _a in ACCOUNTS.items():
    for _k, _e in importlib.import_module(_a["episodes"]).EPISODES.items():
        _e.setdefault("account", _name)
        EPISODES[_k] = _e


def account(e):
    return ACCOUNTS[e["account"]]


def root(e):
    return account(e)["root"]


def plan(e):
    return importlib.import_module(account(e)["plan"])


def mini(e):
    """The account's drawn elements; an episode can pick another art direction (nutrition T01…: miniatures_porcelaine)."""
    return importlib.import_module(e.get("mini") or account(e)["mini"])


def motion(e):
    """Image-to-video prompt prefix of the episode's account."""
    return getattr(plan(e), "MOTION", None) or importlib.import_module(account(e)["episodes"]).MOTION
