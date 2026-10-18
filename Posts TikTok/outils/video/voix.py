"""Post-process a voice-over that has no timestamps (Gemini TTS) so it fits the video pipeline.

tighten(): shortens the silences to the model account's rhythm (median pause 0.33 s, measured on 12 reels of
@learning.of.theday), optionally speeds the voice up without changing its pitch.
natural(): the take as spoken, only its overlong pauses shortened (episodes with fluid=True, through prises.py).
align(): character timestamps from ElevenLabs forced alignment, in the format render_video.py reads (timestamps.json).
"""
import json, subprocess

import numpy as np
import soundfile as sf

MODEL_PAUSE = 0.33  # median pause of the model account (s)


def silences(y, sr, thresh_db=-40, min_len=0.15):
    hop = int(0.01 * sr)
    e = np.array([np.sqrt(np.mean(y[i:i + hop] ** 2) + 1e-12) for i in range(0, len(y) - hop, hop)])
    low = 20 * np.log10(e) < thresh_db
    runs, start = [], None
    for k, v in enumerate(np.append(low, False)):
        if v and start is None:
            start = k
        elif not v and start is not None:
            if (k - start) * 0.01 >= min_len:
                runs.append((start * hop, k * hop))
            start = None
    return runs


def tighten(src, dst, target=MODEL_PAUSE, speed=1.0, floor=0.14):
    """Scale every pause so their median lands on `target` (longer pauses stay relatively longer)."""
    y, sr = sf.read(src)
    if y.ndim > 1:
        y = y.mean(axis=1)
    runs = [r for r in silences(y, sr) if r[0] > 0 and r[1] < len(y)]  # leave the head and tail alone
    if runs:
        med = np.median([(b - a) / sr for a, b in runs])
        ratio = min(1.0, target * speed / med)  # after atempo the pauses shrink by `speed` too
        parts, pos = [], 0
        for a, b in runs:
            keep = max(floor * speed, (b - a) / sr * ratio)
            parts.append(y[pos:a + int(keep * sr / 2)])
            pos = b - int(keep * sr / 2)
        parts.append(y[pos:])
        y = np.concatenate(parts)
    tmp = str(dst) + ".tmp.wav"
    sf.write(tmp, y, sr)
    af = f"atempo={speed}," if speed != 1.0 else ""
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af", af + "aresample=44100", "-b:a", "192k", str(dst)], check=True)
    import os
    os.remove(tmp)


# The longest pause each punctuation mark may keep, in seconds. A shorter pause from the TTS is left as it is.
# History (user, 2026-10-15):
# - Squeezing every pause gave 250 wpm, « pas humain ».
# - Then `regulate` replaced each pause with a calibrated silence, cut word gaps to 0.08 s and time-stretched the
#   sentences to one pace: « mauvaises coupures très légères », and the voice lost its dynamism.
CAP = {"?": 0.7, "!": 0.55, ".": 0.55, "…": 0.6, ":": 0.4, ";": 0.4, ",": 0.32}
WORD_CAP = 0.3  # between two words with no punctuation
OPENING = 0.6  # the breath after the opening question (N03: rushed into the next line, « pas humain »)


def syllables(text):
    """Spoken syllables of a French text: vowel groups, numbers read out, a word-final mute « e »/« es » not counted."""
    import re
    n = 0
    for w in re.findall(r"[a-zàâäéèêëîïôöûùüÿœæç]+", " ".join(spoken(w) for w in text.split())):
        g = re.findall(r"[aeiouyàâäéèêëîïôöûùüÿœæ]+", w)
        n += len(g) - (len(g) > 1 and g[-1] == "e" and re.search(r"es?$", w) is not None)
    return n


def _db(y, sr):
    hop = sr // 100
    return 20 * np.log10(np.sqrt((y[:len(y) // hop * hop].reshape(-1, hop) ** 2).mean(axis=1)) + 1e-9)


def pause_marks(chars, ends, regions, marks_set):
    """Which pause belongs to which punctuation mark: an alignment that keeps both in order. A greedy nearest match
    swapped a comma and a full stop when the aligner drifted. `regions` are (start, end) in seconds. Returns
    ({region index: mark index}, marks), marks = [(time the TTS reached the mark, mark, char index)]."""
    letters = [k for k, c in enumerate(chars) if c.isalnum()]
    marks = []
    for k, c in enumerate(chars):
        before = [j for j in letters if j < k]
        if c in marks_set and before and any(j > k for j in letters):
            marks.append((ends[before[-1]], c, k))
    P, M = regions, marks
    skip_pause = [0.3 + 3 * max(0.0, t1 - t0 - 0.2) for t0, t1 in P]  # a long silence is rarely a plain word gap
    skip_mark = [1.0 if c in ".?!…" else 0.25 for _, c, _ in M]  # a sentence end nearly always has its silence
    cost = np.full((len(P) + 1, len(M) + 1), float("inf"))
    move = np.zeros((len(P) + 1, len(M) + 1), dtype=np.int8)
    cost[0, 0] = 0.0
    for i in range(len(P) + 1):
        for j in range(len(M) + 1):
            if i and cost[i - 1, j] + skip_pause[i - 1] < cost[i, j]:
                cost[i, j], move[i, j] = cost[i - 1, j] + skip_pause[i - 1], 1
            if j and cost[i, j - 1] + skip_mark[j - 1] < cost[i, j]:
                cost[i, j], move[i, j] = cost[i, j - 1] + skip_mark[j - 1], 2
            if i and j:
                (t0, t1), t = P[i - 1], M[j - 1][0]
                dist = max(t0 - 0.05 - t, t - t1 - 0.05, 0.0)
                if dist < 0.8 and cost[i - 1, j - 1] + 2 * dist < cost[i, j]:
                    cost[i, j], move[i, j] = cost[i - 1, j - 1] + 2 * dist, 3
    match, i, j = {}, len(P), len(M)
    while i or j:
        if move[i, j] == 3:
            match[i - 1] = j - 1
        i, j = (i - 1, j) if move[i, j] == 1 else (i, j - 1) if move[i, j] == 2 else (i - 1, j - 1)
    return match, marks


def natural(src, ts_json, dst, cap=None, word_cap=WORD_CAP, opening=OPENING, target_wpm=None, opening_end=None,
            even_db=3.0, log=False):
    """The take as it was spoken; only its overlong pauses are shortened (user, 2026-10-15). No time-stretching, and no
    calibrated silence in place of the TTS's own.
    - A pause is the silence, plus any breath the TTS drew in it, plus the silence after (N03 had 1.3 s after
      « cutanée. »). The breath is kept.
    - When the pause is longer than its punctuation allows (`cap`, `word_cap`), the excess is cut out of the middle of
      its silent parts, with 20 ms cross-fades in silence: nothing audible.
    - The opening question (or the opening line, `opening_end`) gets at least `opening` s of breath.
    - `target_wpm` (organs: 200): when the take is slower than that, every pause is also shortened in proportion, just
      enough to reach it, never below a floor per punctuation; never the speech itself. Tightened pauses are what made
      the organs v2 voice lively (210 wpm, « la dynamique / émotion c'est très bien »); capping only the long pauses
      left it at 168-175 wpm, and a fixed median 0.33 s pushed an already brisk take to 228.
    - A sentence more than `even_db` dB louder or quieter than the others is brought back within it (N02: Margot's
      introduction came out 2-4 dB louder). The gain steps in the middle of the pauses.
    Returns what was done. Re-align afterwards."""
    cap = cap or CAP
    ts = json.load(open(ts_json, encoding="utf-8"))
    ts = ts if isinstance(ts, list) else [ts]
    chars = [c for t in ts for c in t["characters"]]
    ends = [x for t in ts for x in t["character_end_times_seconds"]]
    sr = 44100
    y = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", str(src), "-f", "f32le", "-ac", "1", "-ar", str(sr), "-"],
                                     capture_output=True, check=True).stdout, dtype=np.float32).copy()
    hop = sr // 100
    db = _db(y, sr)
    level = np.median(db[db > -45])
    quiet = np.append(db < max(-55, level - 32), False)  # true silence only: word endings and breaths are not cut
    runs, s = [], None
    for k, q in enumerate(quiet):
        if q and s is None:
            s = k
        elif not q and s is not None:
            if k - s >= 6 and s > 0 and k < len(db):  # 60 ms, head and tail left alone
                runs.append((s, k))
            s = None
    regions = []  # a silence, a breath that never reaches speech level, the silence after: one pause
    for a, b in runs:
        if regions and a - regions[-1]["b"] <= 80 and db[regions[-1]["b"]:a].max() < level - 10:
            regions[-1]["b"] = b
            regions[-1]["runs"].append((a, b))
        else:
            regions.append({"a": a, "b": b, "runs": [(a, b)]})
    match, marks = pause_marks(chars, ends, [(r["a"] / 100, r["b"] / 100) for r in regions], cap)
    # the opening question: the first sentence end, when it is a « ? » (a comma can come before it: « Des boutons sur
    # le menton, toujours au même endroit ? »; taking the first mark gave O01 a 0.31 s opening)
    ends_at = [n for n, (_, c, _) in enumerate(marks) if c in ".?!…"]
    first_q = ends_at[0] if ends_at and marks[ends_at[0]][1] == "?" else None
    if opening_end is not None:  # the opening line (`opening_end` = its last character): its end, whatever the mark
        last = [n for n in ends_at if marks[n][2] <= opening_end + 1]
        first_q = last[-1] if last else first_q
    # never tighter than this: at 0.25 s after a sentence the organs voice ran its sentences together (median 0.20 s);
    # the model account breathes 0.33 s in the median
    floor = {"?": 0.45, "!": 0.35, ".": 0.35, "…": 0.4, ":": 0.25, ";": 0.25, ",": 0.2}
    lengths = [(r["b"] - r["a"]) / 100 for r in regions]
    kinds = [marks[match[n]][1] if n in match else None for n in range(len(regions))]

    def removed(ratio):  # seconds the pauses lose at this ratio (the opening question is never shortened)
        return sum(L - min(cap[c] if c else word_cap, max(floor.get(c, 0.15), L * ratio))
                   for n, (L, c) in enumerate(zip(lengths, kinds)) if not (n in match and match[n] == first_q))
    ratio = 1.0
    if target_wpm and lengths:
        words = len("".join(chars).split())
        need = len(y) / sr - words / target_wpm * 60  # seconds too long for the target pace
        if need > removed(1.0):
            lo, hi = 0.0, 1.0
            for _ in range(30):
                mid = (lo + hi) / 2
                lo, hi = (lo, mid) if removed(mid) < need else (mid, hi)
            ratio = hi
    cuts, inserts = [], []  # in samples: (start, end) removed; (position, length) of silence added
    for n, r in enumerate(regions):
        m = match.get(n)
        c = marks[m][1] if m is not None else None
        length = lengths[n]
        if m is not None and m == first_q:  # the opening's breath: at least `opening`, at most 0.8 s (O03 had 1.05 s)
            if length < opening:
                a, b = max(r["runs"], key=lambda x: x[1] - x[0])
                inserts.append(((a + b) // 2 * hop, int((opening - length) * sr)))
                continue
            excess = length - 0.8
        else:
            excess = length - min(cap[c] if c else word_cap, max(floor.get(c, 0.15), length * ratio))
        for a, b in sorted(r["runs"], key=lambda x: x[0] - x[1]):  # longest silences first, 60 ms kept each side
            take = min(excess, (b - a) / 100 - 0.12)
            if take > 0.03:
                mid = (a + b) / 2 * hop
                cuts.append((int(mid - take * sr / 2), int(mid + take * sr / 2)))
                excess -= take
    if first_q is not None and first_q not in match.values():  # the question said in one breath with what follows
        t = marks[first_q][0]
        lo, hi = int((t - 0.15) * 100), int((t + 0.3) * 100)
        inserts.append(((lo + int(np.argmin(db[lo:hi]))) * hop, int(opening * sr)))
    # the same loudness from one sentence to the next, within even_db
    bounds = [0] + [(r["a"] + r["b"]) // 2 * hop for n, r in enumerate(regions)
                    if n in match and marks[match[n]][1] in ".?!…"] + [len(y)]
    gain = np.ones(len(y), dtype=np.float32)
    lv = []
    for a, b in zip(bounds[:-1], bounds[1:]):
        e = db[a // hop:b // hop]
        lv.append(float(np.median(e[e > e.max() - 25])) if len(e) else level)
    mid, levelled = float(np.median(lv)), 0
    for (a, b), v in zip(zip(bounds[:-1], bounds[1:]), lv):
        off = v - mid
        if abs(off) > even_db:
            gain[a:b] = 10 ** (-(off - np.sign(off) * even_db) / 20)
            levelled += 1
    y = y * gain
    # rebuild: cut silences cross-faded (20 ms), inserted silences in silence
    xf = int(0.02 * sr)
    ramp = np.linspace(0, 1, xf, dtype=np.float32)
    edits = sorted([(a, b, 0) for a, b in cuts] + [(p, p, n) for p, n in inserts])
    out, pos = [], 0
    for a, b, n in edits:
        if a < pos:  # never play anything twice
            continue
        if n:
            out += [y[pos:a], np.zeros(n, dtype=np.float32)]
            pos = a
        else:
            out.append(y[pos:a - xf])
            out.append(y[a - xf:a] * ramp[::-1] + y[b:b + xf] * ramp)
            pos = b + xf
    out.append(y[pos:])
    tmp = str(dst) + ".tmp.wav"
    sf.write(tmp, np.concatenate(out), sr)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-b:a", "192k", str(dst)], check=True)
    import os
    os.remove(tmp)
    done = {"cut": round(sum(b - a for a, b in cuts) / sr, 2), "added": round(sum(n for _, n in inserts) / sr, 2),
            "pause ratio": round(ratio, 2),
            "pauses shortened": len(cuts), "sentences levelled": levelled}
    if log:
        print(" ", done)
    return done


def sentence_speeds(src, ts_json, min_words=6):
    """Each sentence's speed on the sound itself: (syllables per second, text, start s, end s), the bounds taken at the
    silences around it (the aligner's word edges trim short sentences and made them look fast)."""
    ts = json.load(open(ts_json, encoding="utf-8"))
    ts = ts if isinstance(ts, list) else [ts]
    chars = [c for t in ts for c in t["characters"]]
    starts = [x for t in ts for x in t["character_start_times_seconds"]]
    ends = [x for t in ts for x in t["character_end_times_seconds"]]
    y = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", str(src), "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                                     capture_output=True, check=True).stdout, dtype=np.float32)
    # 0.12 s: once the pauses are tightened (floor 0.25 s) a 0.25 s threshold missed them and made short sentences
    # look up to 70 % fast
    gaps = [(a / 16000, b / 16000) for a, b in silences(y, 16000, thresh_db=-45, min_len=0.12)]
    out, first = [], 0
    for k, c in enumerate(chars + ["."]):
        if c in ".?!" and k > first:
            text = "".join(chars[first:k])
            letters = [j for j in range(first, min(k, len(chars))) if chars[j].isalnum()]
            if letters and len(text.split()) >= min_words:
                s0, s1 = starts[letters[0]], ends[letters[-1]]
                s0 = max([b for a, b in gaps if b <= s0 + 0.15] + [s0])
                s1 = min([a for a, b in gaps if a >= s1 - 0.15] + [s1])
                inner = sum(max(0.0, min(b, s1) - max(a, s0)) for a, b in gaps)
                out.append((syllables(text) / max(s1 - s0 - inner, 0.1), text.strip(), s0, s1))
            first = k + 1
    return out


ACCEL = 1.15  # a sentence 15 % faster than the take's median is heard as an acceleration (user: « pas d'accélération »)


def steady(src, ts_json, dst, limit=ACCEL, back_to=1.03, floor=0.82):
    """No acceleration (user, 2026-10-15: « faut pas d'accélération dans les vidéos, tout doit être fluide »). The TTS
    rushes short relaunches and conclusions (« Et ce n'est pas qu'une théorie. » +36 %). Only the sentences more than
    `limit` faster than the median are slowed, back to `back_to`, each in one atempo pass between the silences around it;
    every other sentence is left as spoken. Returns [(text, factor)]. Re-align afterwards."""
    speeds = sentence_speeds(src, ts_json)
    if not speeds:
        return []
    med = float(np.median([r for r, *_ in speeds]))
    fix = [(t, max(floor, back_to * med / r), s0, s1) for r, t, s0, s1 in speeds if r > limit * med]
    if not fix:
        return []
    sr = 44100
    y = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", str(src), "-f", "f32le", "-ac", "1", "-ar", str(sr), "-"],
                                     capture_output=True, check=True).stdout, dtype=np.float32)
    import os, tempfile
    parts, pos = [], 0
    for t, f, s0, s1 in fix:
        a, b = int(s0 * sr), int(s1 * sr)
        tmp_in, tmp_out = tempfile.mktemp(suffix=".wav"), tempfile.mktemp(suffix=".wav")
        sf.write(tmp_in, y[a:b], sr)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp_in, "-af", f"atempo={f:.4f}", tmp_out], check=True)
        seg, _ = sf.read(tmp_out, dtype="float32")
        os.remove(tmp_in), os.remove(tmp_out)
        parts += [y[pos:a], seg if seg.ndim == 1 else seg.mean(axis=1)]
        pos = b
    parts.append(y[pos:])
    tmp = str(dst) + ".tmp.wav"
    sf.write(tmp, np.concatenate(parts), sr)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-b:a", "192k", str(dst)], check=True)
    os.remove(tmp)
    return [(t[:40], round(f, 2)) for t, f, *_ in fix]


def end_rises(src, ts_json, semitones=2.0):
    """Statements whose voice rises at the end, like a question (user, 2026-10-15: « l'intonation, elle monte en fin de
    phrase, elle descend sans raison »). For each sentence ending in « . » or « ! »: the pitch of its last 0.25 s of voice
    against the 0.5 s before; a rise of more than `semitones` counts. Returns the texts."""
    import librosa
    ts = json.load(open(ts_json, encoding="utf-8"))
    ts = ts if isinstance(ts, list) else [ts]
    chars = [c for t in ts for c in t["characters"]]
    ends = [x for t in ts for x in t["character_end_times_seconds"]]
    y = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", str(src), "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                                     capture_output=True, check=True).stdout, dtype=np.float32)
    f0 = librosa.yin(y, fmin=75, fmax=400, sr=16000, frame_length=1024, hop_length=160)
    rms = librosa.feature.rms(y=y, frame_length=1024, hop_length=160)[0][:len(f0)]
    voiced = (rms > 0.02) & (f0 > 80) & (f0 < 390)
    out, first = [], 0
    for k, c in enumerate(chars):
        if c in ".?!" and k > first:
            text = "".join(chars[first:k]).strip()
            letters = [j for j in range(first, k) if chars[j].isalnum()]
            if c in ".!" and letters and len(text.split()) >= 4:
                e = int(ends[letters[-1]] * 100)
                last = f0[max(0, e - 25):e][voiced[max(0, e - 25):e]]
                before = f0[max(0, e - 75):e - 25][voiced[max(0, e - 75):e - 25]]
                if len(last) > 5 and len(before) > 10 and 12 * np.log2(np.median(last) / np.median(before)) > semitones:
                    out.append(text[:45])
            first = k + 1
    return out


def expressiveness(src):
    """How much the voice's pitch moves: standard deviation of F0 in semitones over the voiced frames. A flat delivery
    sits near 2, a lively one near 3-4. Used to keep the most dynamic take (user, 2026-10-15: « on sent la dynamique »)."""
    import librosa
    y = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", str(src), "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                                     capture_output=True, check=True).stdout, dtype=np.float32)
    f0 = librosa.yin(y, fmin=75, fmax=400, sr=16000, frame_length=1024, hop_length=160)
    rms = librosa.feature.rms(y=y, frame_length=1024, hop_length=160)[0][:len(f0)]
    f = f0[(rms > 0.03) & (f0 > 80) & (f0 < 390)]
    st = 12 * np.log2(f / np.median(f))
    return float(np.std(st[np.abs(st) < 12]))  # octave errors out


def align(audio, text, out_json):
    """Character timestamps of `text` in `audio` with ElevenLabs forced alignment (fal), saved in the format that
    render_video.py reads. Whisper word timings were up to 1 s off on synthetic voices; this is exact to the character."""
    import base64, os, time
    import requests
    h = {"Authorization": f"Key {os.environ['FAL_KEY']}", "Content-Type": "application/json"}
    uri = "data:audio/mpeg;base64," + base64.b64encode(open(audio, "rb").read()).decode()
    sub = requests.post("https://queue.fal.run/fal-ai/elevenlabs/forced-alignment", headers=h, timeout=120,
                        json={"audio_url": uri, "text": text}).json()
    while requests.get(sub["status_url"], headers=h, timeout=60).json().get("status") != "COMPLETED":
        time.sleep(1.5)
    chars = requests.get(sub["response_url"], headers=h, timeout=60).json()["characters"]
    assert "".join(c["text"] for c in chars) == text, "alignment does not match the script"
    json.dump([{"characters": [c["text"] for c in chars], "character_start_times_seconds": [c["start"] for c in chars],
                "character_end_times_seconds": [c["end"] for c in chars]}], open(out_json, "w", encoding="utf-8"), ensure_ascii=False)
    return 1.0


# ---------------------------------------------------------------- free local alignment (replaces the $0.22 call)
ALIGN_MODEL = "facebook/wav2vec2-base-10k-voxpopuli-ft-fr"  # French CTC model, 378 MB, downloaded once from Hugging Face
UNITS = ("zéro un deux trois quatre cinq six sept huit neuf dix onze douze treize quatorze quinze seize dix-sept dix-huit "
         "dix-neuf").split()
TENS = {2: "vingt", 3: "trente", 4: "quarante", 5: "cinquante", 6: "soixante", 7: "soixante-dix", 8: "quatre-vingt",
        9: "quatre-vingt-dix"}


def fr_num(n):
    if n < 20:
        return UNITS[n]
    if n < 100:
        t, u = divmod(n, 10)
        if t in (7, 9):
            return TENS[t - 1] + " " + UNITS[10 + u]
        return TENS[t] + ("" if u == 0 else " et un" if u == 1 else " " + UNITS[u])
    if n < 1000:
        c, r = divmod(n, 100)
        return ("cent" if c == 1 else UNITS[c] + " cents") + ("" if r == 0 else " " + fr_num(r))
    k, r = divmod(n, 1000)
    return ("mille" if k == 1 else fr_num(k) + " mille") + ("" if r == 0 else " " + fr_num(r))


def spoken(word):
    """What the voice actually says for a written word (numbers, %), lowercased."""
    import re
    w = word.lower()
    w = re.sub(r"(\d+),(\d+)", lambda m: fr_num(int(m.group(1))) + " virgule " + fr_num(int(m.group(2))), w)
    w = re.sub(r"\d+", lambda m: fr_num(int(m.group())), w)
    return w.replace("%", " pour cent ")


def _ctc_align(logp, targets, blank):
    """Viterbi CTC forced alignment: first frame of each target token."""
    T = logp.shape[0]
    ext = np.full(2 * len(targets) + 1, blank)
    ext[1::2] = targets
    S = len(ext)
    skip = np.zeros(S, bool)
    skip[3::2] = ext[3::2] != ext[1:-2:2]
    neg = -1e30
    alpha = np.full(S, neg)
    alpha[0], alpha[1] = logp[0, ext[0]], logp[0, ext[1]]
    back = np.zeros((T, S), np.int8)
    for t in range(1, T):
        a0 = alpha
        a1 = np.concatenate(([neg], alpha[:-1]))
        a2 = np.where(skip, np.concatenate(([neg, neg], alpha[:-2])), neg)
        stack = np.stack([a0, a1, a2])
        k = stack.argmax(0)
        alpha = stack[k, np.arange(S)] + logp[t, ext]
        back[t] = k
    s = S - 1 if alpha[S - 1] > alpha[S - 2] else S - 2
    path = np.empty(T, int)
    for t in range(T - 1, -1, -1):
        path[t] = s
        s -= int(back[t, s])
    first = {}
    for t, s in enumerate(path):
        if s % 2 == 1 and s // 2 not in first:
            first[s // 2] = t
    last = {}
    for t, s in enumerate(path):
        if s % 2 == 1:
            last[s // 2] = t
    return first, last


def align_local(audio, text, out_json):
    """Character timestamps of `text` in `audio` with a local French wav2vec2 CTC model (free), in the format
    render_video.py reads. Validated on E01 against ElevenLabs forced alignment."""
    import re
    import torch
    import transformers.utils as tu
    import transformers.utils.import_utils as iu
    iu.is_sklearn_available = tu.is_sklearn_available = lambda: False  # broken here (numpy ABI), not needed for CTC
    from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
    proc = Wav2Vec2Processor.from_pretrained(ALIGN_MODEL)
    model = Wav2Vec2ForCTC.from_pretrained(ALIGN_MODEL).eval()
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(audio), "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                         capture_output=True, check=True).stdout
    wav = np.frombuffer(raw, dtype=np.float32)
    with torch.inference_mode():
        x = proc(wav, sampling_rate=16000, return_tensors="pt").input_values
        logp = torch.log_softmax(model(x).logits[0], -1).numpy()
    stride = len(wav) / 16000 / logp.shape[0]
    vocab = proc.tokenizer.get_vocab()
    blank, sep = vocab["<pad>"], vocab["|"]
    words = [(m.start(), m.end(), m.group()) for m in re.finditer(r"\S+", text)]
    targets, owner = [], []  # owner[k] = index of the written word that token k belongs to
    for wi, (_a, _b, w) in enumerate(words):
        chars = [vocab[c] for c in spoken(w).replace("-", " ").replace(" ", "|") if c in vocab]
        chars = [c for k, c in enumerate(chars) if not (c == sep and (k == 0 or chars[k - 1] == sep))]
        if not chars:
            continue
        if targets:
            targets.append(sep)
            owner.append(-1)
        targets += chars
        owner += [wi] * len(chars)
    first, last = _ctc_align(logp, np.array(targets), blank)
    span = {}
    for k, wi in enumerate(owner):
        if wi >= 0 and k in first:
            a, b = first[k] * stride, (last[k] + 1) * stride
            s0, s1 = span.get(wi, (a, b))
            span[wi] = (min(s0, a), max(s1, b))
    starts, ends = [0.0] * len(text), [0.0] * len(text)
    known = sorted(span)
    for wi, (a, b, _w) in enumerate(words):
        if wi not in span:  # pure punctuation: glue to the next spoken word
            nxt = next((j for j in known if j > wi), known[-1])
            span[wi] = (span[nxt][0], span[nxt][0])
        t0, t1 = span[wi]
        for c in range(a, b):
            f = (c - a) / max(1, b - a)
            starts[c], ends[c] = t0 + (t1 - t0) * f, t0 + (t1 - t0) * (c - a + 1) / max(1, b - a)
    for c in range(len(text) - 1, -1, -1):
        if text[c] == " " and c + 1 < len(text):
            starts[c] = ends[c] = starts[c + 1]
    json.dump([{"characters": list(text), "character_start_times_seconds": starts, "character_end_times_seconds": ends}],
              open(out_json, "w", encoding="utf-8"), ensure_ascii=False)
    return len(span) / max(1, len(words))
