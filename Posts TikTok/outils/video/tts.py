"""Text-to-speech through fal (FAL_KEY in env).

tts(): ElevenLabs, returns the character timestamps. gemini(): Google Gemini TTS, native French voices (no timestamps:
render_video.py aligns them locally with Whisper)."""
import json, os, time

import requests

H = {"Authorization": f"Key {os.environ['FAL_KEY']}", "Content-Type": "application/json"}


def tts(text, out_mp3, voice="Alice", model="fal-ai/elevenlabs/tts/multilingual-v2", speed=1.1, stability=0.5, timeout=300):
    args = {"text": text, "voice": voice, "language_code": "fr", "timestamps": True, "stability": stability}
    if "multilingual" in model:
        args["speed"] = speed  # v3/v4 have no speed: the pace comes from the audio tags
    sub = requests.post(f"https://queue.fal.run/{model}", headers=H, json=args, timeout=60)
    sub.raise_for_status()
    sub = sub.json()
    t0 = time.time()
    while requests.get(sub["status_url"], headers=H, timeout=60).json().get("status") != "COMPLETED":
        if time.time() - t0 > timeout:
            raise TimeoutError(model)
        time.sleep(1.5)
    res = requests.get(sub["response_url"], headers=H, timeout=60).json()
    open(out_mp3, "wb").write(requests.get(res["audio"]["url"], timeout=120).content)
    return res.get("timestamps")


GEMINI_STYLE = ("Voix féminine française native, accent parisien neutre, sans aucun accent étranger. Ton doux, calme et posé de "
                "narratrice de documentaire, chaleureux et clair, proche du micro, débit assez rapide et fluide, comme une vidéo "
                "de vulgarisation.")


# "souffle": slightly breathy, like the model account (HNR ~7, H1-H2 ~6 dB, F0 ~170 Hz, measured on its isolated voice)
GEMINI_STYLES = {
    "": GEMINI_STYLE,
    # « reportage »: the user wants the gravity of an investigative documentary, like the model account (2026-10-14)
    "reportage": ("Voix féminine française native, accent neutre, sans aucun accent étranger. Narratrice de reportage "
                  "d'investigation à la télévision : ton grave, sérieux et posé, légèrement soufflé, proche du micro, comme si "
                  "elle révélait quelque chose d'important. Elle appuie les mots clés, marque une courte pause avant chaque "
                  "révélation et ralentit légèrement sur les chiffres. Aucune légèreté, aucun sourire dans la voix, jamais "
                  "enjouée. Débit fluide, sans traîner."),
    # whole script in one take, follow CTA included (same gravity to the end; validated on E01's CTA)
    "reportage_cta": ("Voix féminine française native, accent neutre, sans aucun accent étranger. Narratrice de reportage "
                      "d'investigation à la télévision : ton grave, sérieux et posé, légèrement soufflé, proche du micro, comme si "
                      "elle révélait quelque chose d'important. Elle appuie les mots clés, marque une courte pause avant chaque "
                      "révélation et ralentit légèrement sur les chiffres. Aucune légèreté, aucun sourire dans la voix, jamais "
                      "enjouée. Débit fluide, sans traîner. La dernière phrase, l'appel à s'abonner, garde exactement la même "
                      "gravité et la même énergie : affirmée, avec une fin franche et décidée. Ce n'est pas une invitation "
                      "commerciale, c'est la suite logique de l'enquête."),
    # nutrition account: Margot speaks as « je », a nutrition expert talking to a friend; same gravity on the figures
    "nutri_cta": ("Voix féminine française native, accent neutre, sans aucun accent étranger. Une experte en nutrition qui "
                  "parle à une amie, face caméra : posée, chaleureuse et sûre d'elle, proche du micro. Grave et sérieuse quand "
                  "elle révèle un chiffre ou une étude, jamais moralisatrice, jamais enjouée ni commerciale. Elle appuie les "
                  "mots clés, marque une courte pause avant chaque révélation et ralentit légèrement sur les chiffres. Le "
                  "verdict est dit avec aplomb. Débit fluide, sans traîner. La dernière phrase, l'appel à s'abonner, garde "
                  "la même énergie : affirmée, avec une fin franche et décidée."),
    # nutrition, 2026-10-15 (user: « une voix de vieille », « il faut une voix d'une personne qui a maximum 30 ans », and
    # pauses inside sentences that break the flow): young, punchy, one breath per sentence, no dramatic pause requested
    # v2 (same day): « rapide et continu » gave 250 words a minute, « pas humain »; the model account speaks at 190-210
    # with a real breath after each sentence
    # v3 (same day): « plus vite sur les détails, ralentit sur les chiffres » gave 6.2 to 9.4 syllables/s from one line to
    # the next, « les accélérations de voix »: one steady pace, the energy is in the intonation
    # v4 (same day): « percutante, vive » came out fast and nervous, « plus robot » once its rushed sentences were slowed:
    # the model account's documentary narrator instead, calm and warm, « l'ambiance qui inspire confiance dans la peur »
    # 2026-10-16, nutrition new format, VALIDATED by the user among 6 samples (« Voix B + Musique 3… c'est vraiment le
    # top »): the big sister who read all the studies (reports/DA avatar/son et montage.md, §5d)
    "grande_soeur": ("Voix féminine française native d'une jeune femme d'environ 28 ans, accent neutre, sans aucun accent "
                     "étranger. Une grande sœur qui a lu toutes les études et te parle comme à une amie : chaleureuse, "
                     "complice, posée, avec un sourire dans la voix sur les apartés, nette et ferme sur les chiffres. Débit "
                     "naturel et régulier, environ 185 mots par minute, jamais pressé. Une respiration après chaque phrase, "
                     "aucune pause au milieu des phrases. Fins de phrase qui descendent, jamais de voix cassée ni "
                     "chuchotée. Jamais commerciale, jamais moralisatrice."),
    # 2026-10-16, after T01 final: the same big sister, closer: « encore plus intime… crée vraiment de l'émotion »
    "grande_soeur_intime": ("Voix féminine française native d'une jeune femme d'environ 28 ans, accent neutre, sans aucun "
                            "accent étranger. Une grande sœur qui a lu toutes les études et qui te parle à toi seule, tout "
                            "près, comme un soir sur le canapé : intime, tendre, complice, avec de l'émotion vraie dans la "
                            "voix sur les moments difficiles (le miroir, le bouton qui revient, la fatigue), puis douce et "
                            "rassurante, nette et ferme sur les chiffres. Voix posée et proche, jamais chuchotée, jamais "
                            "cassée. Débit naturel et régulier, environ 185 mots par minute, jamais pressé. Une respiration "
                            "après chaque phrase, aucune pause au milieu des phrases. Fins de phrase qui descendent. Jamais "
                            "commerciale, jamais moralisatrice."),
    "nutri_jeune": ("Voix féminine française native d'une jeune femme d'environ 27 ans, accent neutre, sans aucun accent "
                    "étranger. Narratrice de documentaire, posée et rassurante, légèrement soufflée, proche du micro, "
                    "chaleureuse : elle inspire confiance, et c'est le calme avec lequel elle révèle les faits qui les "
                    "rend inquiétants. Débit naturel et régulier, environ 185 mots par minute, jamais pressé, même sur les "
                    "phrases courtes. Une respiration d'environ une demi-seconde après chaque phrase, aucune pause au "
                    "milieu des phrases. Elle pose la question d'ouverture comme une vraie question, puis laisse un temps. "
                    "Les relances (« Et ce n'est pas le pire. », « Pas si vite. ») sont dites calmement, avec un léger "
                    "appui. Jamais moralisatrice, jamais enjouée ni commerciale. La dernière phrase, l'appel à s'abonner, "
                    "garde la même chaleur, franche et décidée."),
    # organs, after the same feedback (2026-10-15): the reportage gravity with suspense, the hook as a personal alarm
    # back to the first wording (2026-10-15): the user liked its « dynamique / émotion » on O01 v2; the later « même débit
    # du début à la fin » alone made the voice flatter (pitch movement 4.1-4.5 down to 3.8 semitones). But « ralentit sur
    # les chiffres » is gone: « faut pas d'accélération dans les vidéos » (user): the same tempo, the drama in the pauses
    # v6 = the v2 text word for word (the only organs voice the user liked: 210 wpm once its pauses were tightened, pitch
    # movement 4.1), minus « et ralentit légèrement sur les chiffres » (changes of speed: « pas d'accélération »). Every
    # word added since (« même tempo », « débit soutenu », « ne presse jamais ») made it slower or flatter
    "reportage_suspense": ("Voix féminine française native, accent neutre, sans aucun accent étranger. Narratrice de "
                           "reportage d'investigation à la télévision qui raconte une enquête à suspense : grave, intense "
                           "et captivante, légèrement soufflée, proche du micro. Phrases courtes et rythmées. La première "
                           "phrase interpelle directement la spectatrice sur ce qu'elle vit, comme une alerte personnelle. "
                           "Elle fait monter la tension sur les relances (« Et ce n'est pas le pire. », « Le plus "
                           "injuste ? ») avec une courte pause dramatique juste avant chaque révélation. Aucune légèreté, "
                           "jamais enjouée. La dernière phrase, l'appel à s'abonner, garde la même intensité, avec une fin "
                           "franche et décidée."),
    # nutrition, after the user's feedback on N01 (2026-10-15): same persona, but an investigation with suspense and energy
    "nutri_suspense": ("Voix féminine française native, accent neutre, sans aucun accent étranger. Une experte en nutrition "
                       "qui raconte une enquête à suspense, comme une narratrice de reportage d'investigation : grave, "
                       "intense et captivante, proche du micro. Phrases courtes et rythmées. Elle lâche le premier chiffre "
                       "comme une mauvaise nouvelle. Elle fait monter la tension sur les relances (« Et ce n'est pas le "
                       "pire. », « Pas si vite. ») avec une courte pause dramatique juste avant chaque révélation, et pose "
                       "les questions comme si elle attendait la réponse. Quand elle se présente (« Moi c'est Margot »), "
                       "elle garde exactement la même intensité et le même débit que le reste : c'est une relance de "
                       "l'enquête, pas une pause. L'énergie monte jusqu'au verdict, dit avec "
                       "aplomb. Jamais moralisatrice, jamais enjouée ni commerciale. La dernière phrase, l'appel à "
                       "s'abonner, garde la même intensité, avec une fin franche et décidée."),
    "souffle": ("Voix féminine française native, accent parisien neutre, sans aucun accent étranger. Voix douce légèrement "
                "chuchotée et soufflée, intime, très proche du micro, comme une confidence à l'oreille, calme et posée, débit "
                "fluide et assez rapide de narratrice de vidéo de vulgarisation. Parfaitement intelligible."),
}


def gemini(text, out, voice="Vindemiatrix", style=GEMINI_STYLE, model="google/gemini-3.8-flash-tts", timeout=300):
    sub = requests.post(f"https://queue.fal.run/{model}", headers=H, timeout=60,
                        json={"prompt": text, "voice": voice, "style_instructions": style})
    sub.raise_for_status()
    sub = sub.json()
    t0 = time.time()
    while requests.get(sub["status_url"], headers=H, timeout=60).json().get("status") != "COMPLETED":
        if time.time() - t0 > timeout:
            raise TimeoutError(model)
        time.sleep(1.5)
    res = requests.get(sub["response_url"], headers=H, timeout=60).json()
    open(out, "wb").write(requests.get(res["audio"]["url"], timeout=120).content)
