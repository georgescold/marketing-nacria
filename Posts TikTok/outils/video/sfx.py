"""Small sound effects synthesised in code (free), laid over the final mix at given times.

2026-10-16, nutrition new format: the edit must feel « montée par une fille pour des filles » (user). Soft, rounded
sounds only, always well under the voice: a pop when a graphic appears, a pen scribble while a circle draws itself, a
soft whoosh on the big changes of world (plate -> inside the body -> her bathroom), a paper-stamp thud on the verdict,
a small chime on good news. Levels are relative to the voice's speech level.
"""
import numpy as np

SR = 48000
LEVELS = {"pop": -17.0, "scribble": -20.0, "whoosh": -20.0, "stamp": -11.0, "chime": -19.0, "shutter": -20.0}


def _env(n, attack, decay):
    t = np.arange(n) / SR
    return np.minimum(1.0, t / max(attack, 1e-4)) * np.exp(-t / decay)


def pop():
    n = int(0.09 * SR)
    t = np.arange(n) / SR
    f = 260 + 900 * np.exp(-t / 0.012)  # a quick downward sweep: a soft bubble pop
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * _env(n, 0.002, 0.025)
    s += 0.15 * np.random.default_rng(1).standard_normal(n) * _env(n, 0.0005, 0.004)
    return s


def scribble(dur=0.6):
    n = int(dur * SR)
    rng = np.random.default_rng(2)
    noise = rng.standard_normal(n)
    from scipy.signal import butter, sosfilt
    s = sosfilt(butter(2, [1800, 6000], btype="band", fs=SR, output="sos"), noise)
    strokes = 0.55 + 0.45 * np.sin(2 * np.pi * 7 * np.arange(n) / SR) ** 2  # pen strokes
    fade = np.minimum(1, np.arange(n) / (0.04 * SR)) * np.minimum(1, (n - np.arange(n)) / (0.12 * SR))
    return s * strokes * fade


def whoosh(dur=0.45):
    n = int(dur * SR)
    rng = np.random.default_rng(3)
    from scipy.signal import butter, sosfilt
    out = np.zeros(n)
    k = 8
    for j in range(k):  # a band sweeping up then the air settling: chunks with rising centre frequency
        a, size = j * n // k, n // k + 2000
        c = 400 * (6 ** (j / (k - 1)))
        seg = sosfilt(butter(2, [c * 0.6, min(c * 1.8, 20000)], btype="band", fs=SR, output="sos"), rng.standard_normal(size))
        seg *= np.hanning(size)
        end = min(n, a + size)
        out[a:end] += seg[: end - a]
    t = np.arange(n) / n
    return out * np.sin(np.pi * t) ** 1.5


def stamp():
    n = int(0.35 * SR)
    t = np.arange(n) / SR
    body = np.sin(2 * np.pi * (70 + 60 * np.exp(-t / 0.03)) * t) * _env(n, 0.001, 0.07)
    slap = np.random.default_rng(4).standard_normal(n) * _env(n, 0.0005, 0.012)
    from scipy.signal import butter, sosfilt
    slap = sosfilt(butter(2, 2500, btype="low", fs=SR, output="sos"), slap)
    return body + 0.6 * slap


def chime():
    n = int(0.9 * SR)
    t = np.arange(n) / SR
    s = sum(a * np.sin(2 * np.pi * f * t) for f, a in [(1318.5, 1.0), (1975.5, 0.5), (2637, 0.25)])
    return s * _env(n, 0.003, 0.22)


def shutter():
    """A phone camera shutter: two soft mechanical clicks 70 ms apart."""
    n = int(0.16 * SR)
    rng = np.random.default_rng(5)
    from scipy.signal import butter, sosfilt
    s = np.zeros(n)
    for at, a in [(0.0, 1.0), (0.07, 0.7)]:
        k = int(at * SR)
        m = int(0.03 * SR)
        click = rng.standard_normal(m) * _env(m, 0.0004, 0.006) * a
        s[k:k + m] += click
    return sosfilt(butter(2, [700, 7000], btype="band", fs=SR, output="sos"), s)


MAKERS = dict(pop=pop, scribble=scribble, whoosh=whoosh, stamp=stamp, chime=chime, shutter=shutter)


def add(mix_path, events, speech_db):
    """events = [(time s, kind)]: each sound normalised to its LEVELS dB under the voice's speech level, then summed
    into the mix (stereo float, 48 kHz). Rewrites mix_path."""
    import soundfile as sf
    mix, sr = sf.read(str(mix_path), dtype="float32", always_2d=True)
    assert sr == SR
    for t, kind in events:
        s = MAKERS[kind]()
        peak_rms = np.sqrt(np.max(np.convolve(s ** 2, np.ones(960) / 960, mode="same")) + 1e-12)
        s = s / peak_rms * 10 ** ((speech_db + LEVELS[kind]) / 20)
        if kind == "whoosh":
            t -= len(s) / SR / 2  # the whoosh peaks on the cut
        a = int(max(0, t) * SR)
        b = min(len(mix), a + len(s))
        mix[a:b] += s[: b - a, None].astype(np.float32)
    sf.write(str(mix_path), np.clip(mix, -1, 1), SR)
