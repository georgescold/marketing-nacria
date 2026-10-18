"""Compose the episode's background music with ElevenLabs Music (fal, FAL_KEY in env), one chunk per section of the script.

Usage: python musique.py E01_point_noir      (needs timestamps.json: the sections start on the episode's lines)
Writes ../../compte vidéo/<episode>/music.mp3 (instrumental, as long as the video). render_video.py mixes it under the voice.

What the model account does (measured on the Demucs stems of 12 reels): one instrumental per video, clear and present
(centroid ~1 kHz), sparse hits (~2/s), wide dynamics; a fade-in of about 1 s under the series title; constant level 9.7 dB
under the voice, no ducking; fade-out on the last line. The user wants the gravity of an investigative documentary.
Here the sections follow the script. Engines: elevenlabs (composition plan, $0.60/min), lyria ($0.10), minimax ($0.002/s).
Usage: python musique.py <episode> [elevenlabs|lyria|minimax]
"""
import json, os, pathlib, re, sys, time

import requests

import comptes
from comptes import EPISODES
from render_video import TAIL, Timing, line_times

H = {"Authorization": f"Key {os.environ['FAL_KEY']}", "Content-Type": "application/json"}
NEGATIVE = ["vocals", "singing", "choir", "humming", "spoken words", "lo-fi", "cozy", "muffled low-pass", "upbeat",
            "happy", "EDM drop"]


def plan(e, times, total):
    m = e["music"]
    secs = m["sections"]  # (line index, section name, styles)
    starts = [0.0] + [times[i][0] - 0.25 for i, *_ in secs[1:]]  # the change lands just before the line
    ends = starts[1:] + [total + 0.6]
    chunks = []
    for k, ((_i, name, styles), a, b) in enumerate(zip(secs, starts, ends)):
        chunks.append({"text": f"[{name}]", "duration_ms": max(3000, int(round((b - a) * 1000))),
                       "positive_styles": (m["style"] if k == 0 else []) + styles, "negative_styles": NEGATIVE})
    return chunks


def brief(e, chunks, total):
    """The same plan as one text prompt with timestamps, for engines without a composition plan (Lyria, MiniMax)."""
    t, parts = 0.0, []
    for c in chunks:
        d = c["duration_ms"] / 1000
        parts.append(f"{int(t // 60)}:{t % 60:04.1f}-{int((t + d) // 60)}:{(t + d) % 60:04.1f} {c['text'].strip('[]')}: "
                     + ", ".join(c["positive_styles"] if c is not chunks[0] else c["positive_styles"][len(e["music"]["style"]):]))
        t += d
    never = (" Never: " + ", ".join(e["music"]["negative"]) + ".") if e["music"].get("negative") else ""
    return ("Instrumental, no vocals. " + ", ".join(e["music"]["style"]) + f". Exactly {total:.0f} seconds long, ending "
            "cleanly. Structure with timestamps: " + " | ".join(parts) + "." + never)


def compose(engine, e, chunks, total):
    if engine == "elevenlabs":
        return "elevenlabs/music/v2.5", {"composition_plan": {"chunks": chunks}, "output_format": "mp3_48000_192"}
    if engine == "lyria":
        return "google/lyria-3.5", {"prompt": brief(e, chunks, total)}
    if engine == "minimax":
        tags = "\n".join(f"[{'intro' if k == 0 else 'outro' if k == len(chunks) - 1 else 'instrumental'}]" for k in range(len(chunks)))
        return "minimax/music-3", {"prompt": brief(e, chunks, total), "lyrics": tags, "duration": round(total + 1)}
    raise ValueError(engine)


def main(ep, engine="elevenlabs"):
    e0 = comptes.EPISODES[ep]
    if e0.get("music_file"):  # a validated track reused as is (free): the account's signature sound
        import shutil
        d0 = comptes.root(e0) / ep
        src = comptes.root(e0) / e0["music_file"]
        for name in ("music_lyria.mp3", "music.mp3"):
            shutil.copy(src, d0 / name)
        print(f"ok {d0 / 'music_lyria.mp3'} (reused {e0['music_file']})")
        return
    """Writes music.mp3 (ElevenLabs) or music_<engine>.mp3."""
    e = EPISODES[ep]
    d = comptes.root(e) / ep
    tm = Timing(json.load(open(d / "timestamps.json", encoding="utf-8")))
    times = line_times(e["lines"], tm)
    total = tm.ends[-1] + TAIL
    chunks = plan(e, times, total)
    for c in chunks:
        print(f"{c['duration_ms'] / 1000:5.1f}s {c['text']:16s} {', '.join(c['positive_styles'])[:100]}")
    model, args = compose(engine, e, chunks, total)
    sub = requests.post(f"https://queue.fal.run/{model}", headers=H, timeout=60, json=args).json()
    if "status_url" not in sub:
        raise RuntimeError(json.dumps(sub)[:400])
    t0 = time.time()
    while requests.get(sub["status_url"], headers=H, timeout=60).json().get("status") != "COMPLETED":
        if time.time() - t0 > 600:
            raise TimeoutError("music")
        time.sleep(3)
    res = requests.get(sub["response_url"], headers=H, timeout=60).json()
    url = (res.get("audio") or {}).get("url") or (re.search(r'"(https://[^"]+\.(?:mp3|wav|flac))"', json.dumps(res)) or [None, None])[1]
    if not url:
        raise RuntimeError(json.dumps(res)[:500])
    out = d / ("music.mp3" if engine == "elevenlabs" else f"music_{engine}.mp3")
    data = requests.get(url, timeout=120).content
    if not url.endswith(".mp3"):  # keep one format for the mixer
        tmp = out.with_suffix(".tmp" + url[url.rindex("."):])
        tmp.write_bytes(data)
        import subprocess
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-b:a", "192k", str(out)], check=True)
        tmp.unlink()
    else:
        out.write_bytes(data)
    print("ok", out)


if __name__ == "__main__":
    main(*sys.argv[1:])
