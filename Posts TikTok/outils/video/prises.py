"""Voice in one take, chosen among several (user, 2026-10-15: a spliced line always sounds like « une coupure de
dynamisme »). Generates N takes of the full script (Gemini, about $0.04 each), aligns each locally (free), and keeps the
best one as spoken. Writes voice.mp3 + timestamps.json.

Episodes with fluid=True keep their take as spoken: voix.natural only shortens overlong pauses (no time-stretching:
it made the voice « robotique », « en double », and calibrated silences made « des coupures »). The take is chosen on:
- its pace, close to the middle of the episode's `wpm` band (the model account: 190-210);
- how even that pace is from one line to the next (the user hears every change of speed);
- line `line` (nutrition: Margot's introduction) at the same speed and level as the rest;
- how lively the voice is (pitch movement): the user wants « la dynamique ».

Usage: python prises.py <episode> [takes=1] [line=1]   (FAL_KEY in env)

One take by default (about $0.06): the user wants every cost optimised; a second take only if the first one
fails clearly (pace far out of the band, flat voice).
"""
import json, re, shutil, subprocess, sys

import numpy as np

import comptes
from render_video import Timing, decode, line_times
from tts import GEMINI_STYLES, gemini
from voix import ACCEL, align_local, end_rises, expressiveness, natural, sentence_speeds, silences, steady, syllables, tighten


def stats(e, mp3, ts):
    """Per spoken line: (index, syllables per second of speech, speech level in dB); and the take's duration."""
    tm = Timing(json.load(open(ts, encoding="utf-8")))
    v = decode(mp3, 16000)[:, 0]
    gaps = [(a / 16000, b / 16000) for a, b in silences(v, 16000, thresh_db=-45, min_len=0.1)]
    times = line_times(e["lines"], tm)
    rows = []
    for i in range(len(times)):
        a = times[i][1]
        b = times[i + 1][1] if i + 1 < len(times) else len(tm.chars)
        k = [j for j in range(a, b) if tm.chars[j].isalnum()]
        s0, s1 = tm.starts[k[0]], tm.ends[k[-1]]
        talk = s1 - s0 - sum(max(0.0, min(y, s1) - max(x, s0)) for x, y in gaps)
        seg = v[int(s0 * 16000):int(s1 * 16000)]
        fr = seg[:len(seg) // 320 * 320].reshape(-1, 320)
        r = np.sqrt((fr ** 2).mean(axis=1))
        rows.append((i, syllables(tm.full[a:b]) / max(talk, 0.1), 20 * np.log10(np.median(r[r > r.max() * 0.1]) + 1e-9)))
    return rows, tm.ends[-1]


def main(ep, n=1, line=1, most=2):
    e = comptes.EPISODES[ep]
    d = comptes.root(e) / ep
    t = d / "voix" / "prises"
    t.mkdir(parents=True, exist_ok=True)
    name, _, style = e["voice"].partition(":")
    script = " ".join(l[0] for l in e["lines"])
    lo, hi = e.get("wpm", (195, 215))
    best = None
    k = 0
    while k < n:
        k += 1
        raw, mp3, ts = t / f"take_{k}.wav", t / f"take_{k}.mp3", t / f"take_{k}.json"
        try:
            if not raw.exists():
                instr = GEMINI_STYLES[style]
                if e.get("pace"):  # a script that comes out fast (O03: 216-228 wpm on 4 takes) is asked a slower pace
                    instr = re.sub(r"environ \d+ mots par minute", f"environ {e['pace']} mots par minute", instr)
                gemini(script, raw, voice=name, style=instr)
            if not ts.exists():
                if e.get("fluid"):
                    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-ar", "44100", "-b:a", "192k", str(mp3)],
                                   check=True)
                    align_local(mp3, script, ts)
                    done = natural(mp3, ts, mp3, cap=e.get("caps"), word_cap=e.get("word_cap", 0.3),
                                   target_wpm=e.get("target_wpm"),
                                   opening_end=len(e["lines"][0][0]) - 1 if e.get("open") else None)
                    print(f"take {k}: {done}", flush=True)
                    align_local(mp3, script, ts)
                    if e.get("steady"):  # organs only: the nutrition voice sounded « plus robot » once slowed
                        print(f"take {k}: rushed sentences slowed back {steady(mp3, ts, mp3)}", flush=True)
                else:
                    tighten(raw, mp3)
                align_local(mp3, script, ts)
            rows, dur = stats(e, mp3, ts)
        except Exception as err:  # a take can come back unreadable (N03: « Format not recognised »): skip it
            print(f"take {k}: skipped ({str(err)[:80]})", flush=True)
            raw.unlink(missing_ok=True)
            if k == n and n < most:
                n += 1
            continue
        long = [(i, r, l) for i, r, l in rows if len(e["lines"][i][0]) > 30]  # long lines: stable measures
        rates = np.array([r for _, r, _ in long])
        even = float(rates.std() / rates.mean())  # 0.05 = steady, 0.12 = audible changes of speed
        rest = [(r, l) for i, r, l in long if i != line]
        r0, l0 = next((r, l) for i, r, l in rows if i == line)
        rr, ll = np.median([r for r, _ in rest]), np.median([l for _, l in rest])
        wpm = len(script.split()) / dur * 60
        lively = expressiveness(mp3)
        score = (2 * abs(wpm - (lo + hi) / 2) / 200 + max(0.0, lo - wpm, wpm - hi) / 20  # pace, out of the band is costly
                 + 2 * even + abs(r0 - rr) / rr + abs(l0 - ll) / 6 - 0.3 * lively)  # liveliness: « la dynamique »
        print(f"take {k}: {dur:.1f}s, {wpm:.0f} wpm, pace spread {even:.0%}, line {line} {r0:.1f} vs {rr:.1f} syl/s, "
              f"{l0:.1f} vs {ll:.1f} dB, liveliness {lively:.2f} st -> {score:.3f}", flush=True)
        speeds = sentence_speeds(mp3, ts)
        med = float(np.median([r for r, *_ in speeds]))
        fast = [(round(r / med, 2), t[:40]) for r, t, *_ in speeds if r > ACCEL * med]
        print(f"take {k}: still faster than the rest {fast or 'none'}", flush=True)
        score += sum(5 * (x - ACCEL) for x, _ in fast)  # how much it still rushes (O01: +22 % beats +59 %)
        if (max([x for x, _ in fast] or [1.0]) > 1.3 or len(fast) >= 3) and k == n and n < most:
            n += 1  # it rushes: one more take (cost: never more than `most`); checked here, also on a take made earlier
        rises = end_rises(mp3, ts)  # statements said like questions: « l'intonation monte en fin de phrase »
        print(f"take {k}: statements rising at the end {rises or 'none'}", flush=True)
        score += 0.5 * len(rises)
        if best is None or score < best[0]:
            best = (score, k)
    k = best[1]
    shutil.copy(t / f"take_{k}.mp3", d / "voice.mp3")
    shutil.copy(t / f"take_{k}.json", d / "timestamps.json")
    print("kept take", k, flush=True)


if __name__ == "__main__":
    main(sys.argv[1], *[int(x) for x in sys.argv[2:]])
