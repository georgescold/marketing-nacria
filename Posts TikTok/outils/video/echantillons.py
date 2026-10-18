"""Short voice + music samples to choose the nutrition account's ambience (user, 2026-10-16: the grave score sounds like
« un film d'horreur », the warm pop one was « incohérent avec le script » : « fais-moi plusieurs prises sur une courte
portion… pour que je puisse comparer et choisir »).

Same 15 s of script for every sample. Voices A–D over music 1 (compare the voice), voice B over musics 1–3 (compare the
music). Output: compte nutrition/vidéo/T01_sucre/_tests ambiance/*.mp3 (voice + music only, -14.4 LUFS).
Usage: python echantillons.py   (FAL_KEY in env)
"""
import pathlib, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import requests

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import comptes  # noqa: E402
from tts import GEMINI_STYLES, H, gemini  # noqa: E402

OUT = comptes.ACCOUNTS["nutrition"]["root"] / "T01_sucre" / "_tests ambiance"
TEXT = ("Tu manges plutôt sain… et tes boutons du menton reviennent quand même ? "
        "Le matin, c'est galettes de riz, avocat et café : léger, healthy, tu fais attention. "
        "Sauf que ces galettes font grimper ton sucre sanguin plus haut… que du sucre en morceaux. "
        "Vingt minutes plus tard, ce sucre inonde ton sang.")

BASE = "Voix féminine française native d'une jeune femme d'environ 28 ans, accent neutre, sans aucun accent étranger. "
SISTER = (BASE + "Une grande sœur qui a lu toutes les études et te parle comme à une amie : chaleureuse, complice, posée, "
          "avec un sourire dans la voix sur les apartés, nette et ferme sur les chiffres. Débit naturel et régulier, "
          "environ 185 mots par minute, jamais pressé. Une respiration après chaque phrase, aucune pause au milieu des "
          "phrases. Fins de phrase qui descendent, jamais de voix cassée ni chuchotée. Jamais commerciale, jamais "
          "moralisatrice.")
CONFIDANTE = (BASE + "Une amie qui te raconte un secret au café, comme une animatrice de podcast : intime, vivante, "
              "curieuse, un brin espiègle, très naturelle, elle te parle à toi seule. Débit naturel et régulier, environ "
              "185 mots par minute, jamais pressé. Une respiration après chaque phrase, aucune pause au milieu des "
              "phrases. Fins de phrase qui descendent. Jamais commerciale, jamais moralisatrice.")
VOICES = {
    "A": ("Voix A - actuelle", "Erinome", GEMINI_STYLES["nutri_jeune"]),
    "B": ("Voix B - grande soeur", "Erinome", SISTER),
    "C": ("Voix C - grande soeur timbre chaud", "Sulafat", SISTER),
    "D": ("Voix D - confidente podcast", "Aoede", CONFIDANTE),
}

NEVER = ("Never: horror, dread, dark drones, thriller, scary, ominous, vocals, singing, choir, spoken words, EDM drop, "
         "corporate upbeat, music box.")
MUSICS = {
    "1": ("Musique 1 - suspense doux",
          "Soft cinematic suspense instrumental for a women's wellness documentary, 105 BPM, minor key but tender and "
          "warm, felt piano motif, soft warm strings, a gentle pulsing pluck and a soft kick, curious and emotional, "
          "intimate, clear and present, sparse mid-range leaving room for a spoken voice."),
    "2": ("Musique 2 - enquete podcast",
          "Light mysterious investigative podcast groove instrumental, 100 BPM, muted plucked synths, soft kick and "
          "brushed snare, warm round bass, curious and intriguing like a true-story podcast for women, clean modern "
          "production, sparse mid-range leaving room for a spoken voice."),
    "3": ("Musique 3 - emotion intime",
          "Intimate emotional minimal instrumental, 90 BPM, soft R&B-tinged Rhodes chords, gentle finger snaps, warm "
          "sub bass, airy pads, tender and slightly melancholic, like a heartfelt story told between friends, sparse "
          "mid-range leaving room for a spoken voice."),
}
PAIRS = [("A", "1"), ("B", "1"), ("C", "1"), ("D", "1"), ("B", "2"), ("B", "3")]
GAP_DB = 9.7  # music under the voice, as on every validated video


def lyria(prompt, out):
    import time
    sub = requests.post("https://queue.fal.run/google/lyria-3.5", headers=H, timeout=60,
                        json={"prompt": f"Instrumental, no vocals. {prompt} Exactly 25 seconds long, starting right away "
                                        f"at full level with no silent intro, ending cleanly. {NEVER}"}).json()
    t0 = time.time()
    while requests.get(sub["status_url"], headers=H, timeout=60).json().get("status") != "COMPLETED":
        if time.time() - t0 > 600:
            raise TimeoutError(out.name)
        time.sleep(3)
    res = requests.get(sub["response_url"], headers=H, timeout=60).json()
    url = (res.get("audio") or res.get("audio_file") or {}).get("url")
    out.write_bytes(requests.get(url, timeout=120).content)


def pcm(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", "48000", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)


def speech_db(x):
    fr = x[: len(x) // 960 * 960].reshape(-1, 960)
    p = (fr ** 2).mean(1)
    on = p > np.percentile(p, 90) * 0.05
    return 10 * np.log10(p[on].mean() + 1e-12)


def live_start(m):
    """Where the track is really playing: Lyria often opens on silence or a long quiet intro (9 s on music 2), heard as
    music missing at the start. First instant whose 2 s average reaches the track's median level - 4 dB."""
    lv = np.array([10 * np.log10(np.mean(m[k:k + 12000] ** 2) + 1e-12) for k in range(0, len(m) - 12000, 12000)])
    avg = np.convolve(10 ** (lv / 10), np.ones(8) / 8, mode="valid")
    med = np.median(lv)
    return float(np.argmax(10 * np.log10(avg + 1e-12) > med - 4)) * 0.25


def mix(voice, music, out):
    """Voice from 0.3 s, music under it at GAP_DB from the first instant (no fade-in hole), 1.2 s tail, -14.4 LUFS."""
    v, m = pcm(voice), pcm(music)
    off = live_start(m)
    m = m[int(off * 48000):]
    gain = speech_db(v) - GAP_DB - (10 * np.log10((m ** 2).mean() + 1e-12))
    dur = 0.3 + len(v) / 48000 + 1.2
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(voice), "-i", str(music), "-filter_complex",
                    f"[0:a]aresample=48000,adelay=300|300,apad,atrim=0:{dur:.2f}[v];"
                    f"[1:a]aresample=48000,atrim={off:.2f}:{off + dur:.2f},asetpts=PTS-STARTPTS,volume={gain:.2f}dB,"
                    f"afade=t=in:d=0.08,"
                    f"afade=t=out:st={dur - 1.0:.2f}:d=1.0[m];[v][m]amix=inputs=2:normalize=0,"
                    f"loudnorm=I=-14.4:TP=-1.5:LRA=11[a]", "-map", "[a]", "-ac", "2", "-ar", "48000", "-b:a", "192k",
                    str(out)], check=True)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    work = OUT / "_sources"
    work.mkdir(exist_ok=True)

    def voice_job(k):
        name, v, style = VOICES[k]
        raw, trimmed = work / f"voix_{k}.wav", work / f"voix_{k}_trim.wav"
        if not raw.exists():
            gemini(TEXT, raw, voice=v, style=style)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-af",
                        "silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
                        "silenceremove=start_periods=1:start_threshold=-45dB,areverse", str(trimmed)], check=True)
        return f"{name}: {len(pcm(trimmed)) / 48000:.1f} s"

    def music_job(k):
        out = work / f"musique_{k}.mp3"
        if not out.exists():
            lyria(MUSICS[k][1], out)
        return f"{MUSICS[k][0]}: {len(pcm(out)) / 48000:.1f} s"

    with ThreadPoolExecutor(8) as ex:
        for r in ex.map(lambda f: f(), [lambda k=k: voice_job(k) for k in VOICES] + [lambda k=k: music_job(k) for k in MUSICS]):
            print(r, flush=True)
    for vk, mk in PAIRS:
        out = OUT / f"{VOICES[vk][0]} + {MUSICS[mk][0]}.mp3"
        mix(work / f"voix_{vk}_trim.wav", work / f"musique_{mk}.mp3", out)
        print("->", out.name, flush=True)


if __name__ == "__main__":
    main()
