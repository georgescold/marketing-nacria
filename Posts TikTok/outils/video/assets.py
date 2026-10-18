"""Generate an episode's assets (FAL_KEY in env), step by step, within the $2-per-video budget.

Usage: python assets.py <episode> voice  [voice[:style]] [tts model] [speed]   e.g. voice Despina:souffle
       python assets.py <episode> images                                      scene first frames (Nano Banana, $0.04)
       python assets.py <episode> anim   [h3|wan|grok|ltx]                    AI clips for the lines in e["anim"]
- voice: Gemini native French voice (raw take kept in voix/), pauses tightened to the model account's rhythm, then
  character timestamps from ElevenLabs forced alignment. ElevenLabs voices: the episode's `tags` go before the lines.
- images: episodes with a `chapter` use the season art direction (plan.SCENE, the chapter's glow); the chapter menu and
  the cover reuse the chapter's hero images (miniatures.py), so nothing else to generate here.
- anim: each clip lasts what its line needs (2 to 4 s, paid per second); the other lines move in code (render_video.py).
Writes to ../../compte vidéo/<episode>/ : voice.mp3, timestamps.json, scenes/line_NN.png + .mp4. Existing files are kept.
"""
import base64, math, io, json, os, pathlib, re, sys, time
from concurrent.futures import ThreadPoolExecutor

import requests
from PIL import Image

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from fal import run  # noqa: E402

import comptes  # noqa: E402
from comptes import EPISODES  # noqa: E402
from episodes import STYLE  # noqa: E402
from tts import GEMINI_STYLES, gemini, tts  # noqa: E402
from voix import align, align_local, tighten  # noqa: E402

SCENE_MODEL = "fal-ai/nano-banana"  # $0.04; the hero/cover image uses Nano Banana Pro (miniatures.py)
# real skin (e["photo"]): Nano Banana Pro, $0.15. On 2026-10-16 the user saw that the spots « ne sont pas réels » (glossy beads);
# in a 4-model benchmark only Pro drew real acne (pores, vellus hair, pustules, brown marks)
PHOTO_MODEL = "fal-ai/nano-banana-pro"

# image-to-video engines (real costs from the fal usage API, 2026-10-14)
VIDEO = {
    "h3": ("minimax/h3-max-turbo/image-to-video",  # $0.015/s at 768P
           lambda uri, end, p, dur: {"image_url": uri, "prompt": p, "duration": dur, "resolution": "768P",
                                     "prompt_expansion_mode": "disabled", **({"end_image_url": end} if end else {})}),
    "wan": ("alibaba/wan-3.0/image-to-video",  # $0.05/s at 720p (about 4x that at 1080p)
            lambda uri, end, p, dur: {"start_image_url": uri, "prompt": p, "duration": max(3, round(dur)),
                                      "resolution": "720p", "aspect_ratio": "9:16", "audio": False,
                                      "enable_prompt_expansion": False, **({"end_image_url": end} if end else {})}),
    "grok": ("xai/grok-imagine-video/v1.5/lite/image-to-video",
             lambda uri, end, p, dur: {"image_url": uri, "prompt": p, "duration": max(1, round(dur)), "resolution": "720p"}),
    "ltx": ("lightricks/ltx-2.5/image-to-video/fast",  # 6 s minimum
            lambda uri, end, p, dur: {"image_url": uri, "prompt": p, "duration": 6, "resolution": "720p", "aspect_ratio": "9:16",
                                      "generate_audio": False, **({"end_image_url": end} if end else {})}),
}


def script(e, model):
    tags = e.get("tags", {}) if "elevenlabs" in model and "multilingual" not in model else {}
    return " ".join((tags[i] + " " if i in tags else "") + l[0] for i, l in enumerate(e["lines"]))


def jpeg_uri(png, size=(1080, 1920)):
    buf = io.BytesIO()
    Image.open(png).convert("RGB").resize(size, Image.LANCZOS).save(buf, "JPEG", quality=93)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def animate(png, prompt, out, engine="h3", duration=3.0, end_png=None, timeout=1500):
    """First frame (+ optional last frame, which locks the camera) + motion prompt -> clip without audio."""
    h = {"Authorization": f"Key {os.environ['FAL_KEY']}", "Content-Type": "application/json"}
    model, build = VIDEO[engine]
    args = build(jpeg_uri(png), jpeg_uri(end_png) if end_png else None, prompt, duration)
    sub = requests.post(f"https://queue.fal.run/{model}", headers=h, timeout=120, json=args).json()
    if "status_url" not in sub:
        raise RuntimeError(json.dumps(sub)[:300])
    t0 = time.time()
    while requests.get(sub["status_url"], headers=h, timeout=60).json().get("status") != "COMPLETED":
        if time.time() - t0 > timeout:
            raise TimeoutError(out.name)
        time.sleep(4)
    res = requests.get(sub["response_url"], headers=h, timeout=60).json()
    url = (res.get("video") or {}).get("url") or (re.search(r'"(https://[^"]+\.mp4)"', json.dumps(res)) or [None, None])[1]
    if not url:
        raise RuntimeError(json.dumps(res)[:300])
    out.write_bytes(requests.get(url, timeout=300).content)


def end_frame(png, change, out):
    """Same image, same framing, with only `change` applied: the last frame for animate()."""
    run("fal-ai/nano-banana/edit", {"prompt": "Keep this exact image: same framing, same camera, same objects, same "
        "lighting and background. Change only this: " + change, "image_urls": [jpeg_uri(png)], "num_images": 1}, out)


def scene_prompt(e, obj, accent, i=None):
    if "chapter" in e:
        pl = comptes.plan(e)
        c = pl.CHAPTERS[e["chapter"] - 1]
        glow = e.get("glow", {}).get(i, c["glow"])  # organs: a line can glow another colour (e.g. a gland in gold)
        if i in e.get("photo", ()):  # organs: the spot itself, photographed on real skin (plan_organes.PHOTO)
            return pl.PHOTO.format(obj=obj, ink=pl.INK, edge=pl.INK_EDGE) + accent
        if i in e.get("amateur", ()):  # nutrition: an ordinary phone photo of her world (her bathroom shelf…)
            return pl.AMATEUR.format(obj=obj)
        if i in e.get("body", ()):  # nutrition: where the food goes, inside the body (plan_nutrition.BODY)
            return pl.BODY.format(obj=obj, accent=accent, ink=pl.INK, edge=pl.INK_EDGE, glow=glow)
        return pl.SCENE.format(obj=obj, accent=accent, ink=pl.INK, edge=pl.INK_EDGE, glow=glow)
    return STYLE.format(obj=obj, accent=accent)


def clip_durations(e, d):
    """Seconds of AI video each animated line needs: 80 % of the line, 2 to 4 s (the action, then the frame holds)."""
    from render_video import Timing, line_times
    tm = Timing(json.load(open(d / "timestamps.json", encoding="utf-8")))
    starts = [t for t, _ in line_times(e["lines"], tm)] + [tm.ends[-1]]
    if e.get("full_motion"):  # 2026-10-16, the user on T01: « les arrêts sur image avant de changer de plan rompent le
        # dynamisme »: the clip lasts the whole shot (+ the cross-fade into the next one), played at 1x, never held
        last = starts[-1] + (e.get("tail", 0.3) if not e.get("loop") else 0.12) + 0.3
        end = {i: starts[i + 1] + 0.4 if i + 1 < len(e["lines"]) else last for i in e.get("anim", [])}
        return {i: float(min(15, max(1.5, math.ceil((end[i] - starts[i]) * 10) / 10))) for i in e.get("anim", [])}
    # 65 % of the line in whole seconds (Grok bills per second), 2 to 4 s; the render speeds a clip up to x2 if needed
    return {i: float(min(4, max(2, round((starts[i + 1] - starts[i]) * 0.65)))) for i in e.get("anim", [])}


def voice_over(e, d, voice="Despina", model="google/gemini-3.8-flash-tts", speed="1.0"):
    if (d / "voice.mp3").exists() and (d / "timestamps.json").exists():
        return print("voice exists", flush=True)
    if not model.startswith("google/gemini"):
        return json.dump(tts(script(e, model), d / "voice.mp3", voice=voice, model=model),
                         open(d / "timestamps.json", "w", encoding="utf-8"), ensure_ascii=False)
    name, _, style = voice.partition(":")  # e.g. "Despina:souffle"
    raw = d / "voix" / f"gemini_{name}{'_' + style if style else ''}.wav"
    raw.parent.mkdir(parents=True, exist_ok=True)
    if not raw.exists():
        gemini(script(e, model), raw, voice=name, style=GEMINI_STYLES[style], model=model)
    tighten(raw, d / "voice.mp3", speed=float(speed))
    # free local alignment (wav2vec2 FR): on E01, 15 ms median / 43 ms p95 from ElevenLabs forced alignment ($0.22)
    print(f"aligned {align_local(d / 'voice.mp3', script(e, model), d / 'timestamps.json'):.0%} of the words", flush=True)


def reuse(e, d):
    """e["reuse"] = {i: (episode, j, with_clip)}: line i shows scene j of an earlier episode (same object, free, and the
    series stays continuous); with_clip also copies its animation."""
    import shutil
    for i, (ep, j, with_clip) in e.get("reuse", {}).items():
        src = comptes.root(EPISODES[ep]) / ep / "scenes"
        for ext in [".png"] + ([".mp4"] if with_clip else []):
            out = d / "scenes" / f"line_{i:02d}{ext}"
            if not out.exists():
                shutil.copy(src / f"line_{j:02d}{ext}", out)
                print(f"{out.name} from {ep} scene {j}", flush=True)


def images(e, d):
    (d / "scenes").mkdir(parents=True, exist_ok=True)
    reuse(e, d)
    for i, kind in e.get("cards", {}).items():  # scenes drawn in code by the account (nutrition: Margot speaking)
        out = d / "scenes" / f"line_{i:02d}.png"
        if not out.exists():
            getattr(comptes.mini(e), f"{kind}_scene")(out)
            print(f"{out.name} {kind} card", flush=True)
    jobs = [(d / "scenes" / f"line_{i:02d}.png", scene_prompt(e, obj, accent, i),
             PHOTO_MODEL if i in e.get("photo", ()) or i in e.get("amateur", ()) else SCENE_MODEL)
            for i, (_t, obj, accent, _c) in enumerate(e["lines"])
            if obj and i not in e.get("reuse", {}) and i not in e.get("cards", {})]

    def gen(job):
        out, prompt, model = job
        if out.exists():
            return f"{out.name} exists"
        for _ in range(3):
            try:
                run(model, {"prompt": prompt, "aspect_ratio": "9:16", "num_images": 1}, out)
                return f"{out.name} ok"
            except Exception as err:
                last = str(err)[:120]
        return f"{out.name} ERROR {last}"

    with ThreadPoolExecutor(8) as ex:
        for line in ex.map(gen, jobs):
            print(line, flush=True)


def first_frame(e, d, i):
    """Chained scene: its first frame is the last frame shown of scene `chain[i]` (clip frame at clip_end, or its image)."""
    import cv2
    j = e["chain"][i]
    out = d / "scenes" / f"line_{i:02d}.png"
    clip = d / "scenes" / f"line_{j:02d}.mp4"
    if clip.exists():
        cap = cv2.VideoCapture(str(clip))
        n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        cap.set(cv2.CAP_PROP_POS_FRAMES, max(0, int((n - 1) * e.get("clip_end", {}).get(j, 1.0))))
        ok, f = cap.read()
        Image.fromarray(cv2.cvtColor(f, cv2.COLOR_BGR2RGB)).save(out)  # cv2.imwrite fails on accented Windows paths
    else:
        Image.open(d / "scenes" / f"line_{j:02d}.png").save(out)


def anims(e, d, engine="grok"):
    durs = clip_durations(e, d)

    def one(i):
        out = d / "scenes" / f"line_{i:02d}.mp4"
        if out.exists():
            return f"{out.name} exists"
        end = d / "scenes" / f"line_{i:02d}_end.png"
        for _ in range(2):
            try:
                pl = comptes.plan(e)  # inside-the-body scenes move like 3D anatomy, not like food
                prefix = pl.BODY_MOTION if i in e.get("body", ()) and hasattr(pl, "BODY_MOTION") else \
                    pl.PHOTO_MOTION if (i in e.get("photo", ()) or i in e.get("amateur", ())) and hasattr(pl, "PHOTO_MOTION") \
                    else comptes.motion(e)
                animate(d / "scenes" / f"line_{i:02d}.png", prefix + e["motion"][i], out, engine, durs[i],
                        end if end.exists() else None)
                return f"{out.name} ok ({durs[i]} s)"
            except Exception as err:
                last = str(err)[:160]
        return f"{out.name} ERROR {last}"

    chain = e.get("chain", {})
    todo = sorted(durs)
    while todo:  # waves: a chained scene waits for the scene it continues
        ready = [i for i in todo if i not in chain or chain[i] not in todo]
        for i in ready:
            if i in chain and not (d / "scenes" / f"line_{i:02d}.png").exists():
                first_frame(e, d, i)
        with ThreadPoolExecutor(8) as ex:
            for line in ex.map(one, ready):
                print(line, flush=True)
        todo = [i for i in todo if i not in ready]
    for i, j in chain.items():  # chained still scenes (no clip of their own) start from their source's last frame
        if i not in durs and not (d / "scenes" / f"line_{i:02d}.png").exists():
            first_frame(e, d, i)
            print(f"line_{i:02d}.png from scene {j}", flush=True)


if __name__ == "__main__":
    ep, step, *rest = sys.argv[1:]
    e = EPISODES[ep]
    d = comptes.root(e) / ep
    {"voice": lambda: voice_over(e, d, *rest), "images": lambda: images(e, d), "anim": lambda: anims(e, d, *(rest or [e.get("engine", "grok")]))}[step]()
    print("done", flush=True)
