"""Compare Gemini voices on the same lines: generates one sample per voice, measures median pitch (F0), speaking rate and
pauses, and writes the samples to <account root>/tests voix/ for listening.

Usage: python essai_voix.py <account> <style> <voice> [<voice> ...]   (FAL_KEY in env, about $0.012 per sample)
"""
import pathlib, sys

import numpy as np

import comptes
from render_video import decode
from tts import GEMINI_STYLES, gemini
from voix import silences

SAMPLE = ("Tu es passée au chocolat noir pour protéger ta peau ? Mauvaise nouvelle. Moi c'est Margot, je décortique les "
          "études et ce que je vais te révéler, personne n'ose te le dire.")


def f0(y, sr=16000):
    """Median pitch of the voiced frames (autocorrelation, 75-400 Hz)."""
    hop, win, out = 160, 640, []
    for i in range(0, len(y) - win, hop):
        fr = y[i:i + win] - y[i:i + win].mean()
        if np.sqrt((fr ** 2).mean()) < 0.02:
            continue
        ac = np.correlate(fr, fr, "full")[win - 1:]
        lo, hi = sr // 400, sr // 75
        k = lo + int(np.argmax(ac[lo:hi]))
        if ac[k] > 0.4 * ac[0]:
            out.append(sr / k)
    return float(np.median(out)) if out else 0.0


def main(account, style, *voices):
    out = comptes.ACCOUNTS[account]["root"] / "tests voix"
    out.mkdir(parents=True, exist_ok=True)
    for v in voices:
        p = out / f"{v}_{style}.wav"
        if not p.exists():
            gemini(SAMPLE, p, voice=v, style=GEMINI_STYLES[style])
        y = decode(p, 16000)[:, 0]
        runs = [(b - a) / 16000 for a, b in silences(y, 16000) if a > 0 and b < len(y)]
        speech = len(y) / 16000 - sum(runs)
        rate = sum(c.isalpha() for c in SAMPLE) / speech
        print(f"{v:14s} F0 {f0(y):5.0f} Hz | {rate:4.1f} lettres/s | {len(runs):2d} pauses, max "
              f"{max(runs) if runs else 0:.2f}s | {len(y) / 16000:.1f}s", flush=True)


if __name__ == "__main__":
    main(*sys.argv[1:])
