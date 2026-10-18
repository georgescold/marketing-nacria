"""Uniform metrics over the viral-script corpus (*.jsonl in this folder, format in SPEC.md).

Usage: python metrics.py  -> prints the summary tables and writes metrics.csv (one row per video).
ASR transcripts often have no punctuation, so everything is measured on words and timed cues, not on sentences.
"""
import csv, glob, json, pathlib, re, statistics as st

HERE = pathlib.Path(__file__).resolve().parent

YOU = {"en": r"\b(you|your|you're|yours|yourself)\b", "fr": r"\b(tu|te|t'|toi|ton|ta|tes|vous|votre|vos)\b",
       "es": r"\b(tú|tu|te|ti|tus|usted|ustedes|vos)\b", "pt": r"\b(você|voce|vocês|seu|sua|seus|suas|te|tu)\b"}
BUT = {"en": r"\b(but|however|actually|instead|except|yet)\b", "fr": r"\b(mais|pourtant|sauf|en fait|en réalité|or)\b",
       "es": r"\b(pero|sin embargo|en realidad|sino)\b", "pt": r"\b(mas|porém|na verdade|só que)\b"}
CTA = r"(follow|subscribe|abonne|abonnez|suis-moi|suivez|sígueme|sigueme|suscríbete|segue|me siga|link in bio|lien en bio)"
QUESTION_START = r"^\s*(why|what|how|did you|do you|have you|is|are|can|pourquoi|comment|est-ce|qu'est-ce|sais-tu|tu sais|" \
                 r"savais-tu|et si|¿|sabías|por qué|qué|cómo|você sabia|por que|o que|como)"
NUM = r"(\d+([.,]\d+)?\s*%?|\b(one|two|three|four|five|six|seven|eight|nine|ten|hundred|thousand|million|un|deux|trois|" \
      r"quatre|cinq|six|sept|huit|neuf|dix|cent|mille|million|uno|dos|tres|cuatro|cinco|diez|cien|mil|millón|" \
      r"um|dois|três|quatro|cinco|dez|cem|milhão)\b)"


def words(s):
    return re.findall(r"[\w'’%-]+", s.lower())


def text_between(cues, t0, t1):
    return " ".join(c[2] for c in cues if c[0] < t1 and c[1] > t0)


def row(v):
    cues = [c for c in v.get("cues") or [] if len(c) >= 3]
    text = v.get("transcript") or " ".join(c[2] for c in cues)
    w = words(text)
    lang = (v.get("language") or "en")[:2]
    spoken = (cues[-1][1] - cues[0][0]) if cues else None
    dur = v.get("duration_s") or spoken
    gaps = [b[0] - a[1] for a, b in zip(cues, cues[1:])]
    first3 = words(text_between(cues, 0, 3.0)) if cues else w[:8]
    last = " ".join(w[-15:])
    return dict(
        id=v.get("id"), account=v.get("account"), lang=lang, niche=v.get("niche"), format=v.get("format"),
        control=bool(v.get("is_control")), views=v.get("views"), followers=v.get("followers"), duration=dur,
        words=len(w), wpm=round(len(w) / spoken * 60) if spoken and spoken > 5 else None,
        speech_start=round(cues[0][0], 2) if cues else None,
        words_first3s=len(first3),
        first_line=(cues[0][2] if cues else " ".join(w[:12]))[:140],
        hook_question=bool(re.search(QUESTION_START, (cues[0][2] if cues else text).lower())),
        hook_you=bool(re.search(YOU.get(lang, YOU["en"]), " ".join(first3))),
        hook_number=bool(re.search(NUM, " ".join(first3))),
        you_per_min=round(len(re.findall(YOU.get(lang, YOU["en"]), text.lower())) / dur * 60, 1) if dur else None,
        but_per_min=round(len(re.findall(BUT.get(lang, BUT["en"]), text.lower())) / dur * 60, 1) if dur else None,
        numbers_per_min=round(len(re.findall(NUM, text.lower())) / dur * 60, 1) if dur else None,
        long_pauses=sum(g > 0.6 for g in gaps),
        cta=bool(re.search(CTA, text.lower())),
        cta_end=bool(re.search(CTA, last)),
        last_words=last,
    )


def summary(rows, label):
    def med(k):
        xs = [r[k] for r in rows if isinstance(r[k], (int, float)) and r[k] is not None]
        return round(st.median(xs), 1) if xs else None

    def share(k):
        return f"{round(100 * sum(1 for r in rows if r[k]) / len(rows))} %" if rows else "-"

    print(f"{label:<28} n={len(rows):<3} dur={med('duration')} s  words={med('words')}  wpm={med('wpm')}  "
          f"start={med('speech_start')} s  first3s={med('words_first3s')} w  you/min={med('you_per_min')}  "
          f"but/min={med('but_per_min')}  num/min={med('numbers_per_min')}  pauses>0.6s={med('long_pauses')}  "
          f"Q-hook={share('hook_question')}  you-hook={share('hook_you')}  num-hook={share('hook_number')}  "
          f"CTA={share('cta')}  CTA-end={share('cta_end')}")


def main():
    rows = []
    for f in sorted(glob.glob(str(HERE / "*.jsonl"))):
        for line in open(f, encoding="utf-8"):
            line = line.strip()
            if line:
                try:
                    v = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if v.get("cues") or v.get("transcript"):
                    r = row(v)
                    r["file"] = pathlib.Path(f).stem
                    rows.append(r)
    seen, uniq = set(), []
    for r in rows:
        if r["id"] not in seen:
            seen.add(r["id"]), uniq.append(r)
    rows = uniq
    with open(HERE / "metrics.csv", "w", newline="", encoding="utf-8") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        wr.writeheader()
        wr.writerows(rows)
    hits = [r for r in rows if not r["control"]]
    summary(hits, "ALL HITS")
    summary([r for r in rows if r["control"]], "ALL CONTROLS")
    for f in sorted({r["file"] for r in rows}):
        summary([r for r in hits if r["file"] == f], f"hits {f}")
        summary([r for r in rows if r["control"] and r["file"] == f], f"controls {f}")
    big = [r for r in hits if (r["views"] or 0) >= 5_000_000]
    summary(big, "HITS >= 5M views")
    for fmt in sorted({(r["format"] or "?").split("-")[0] for r in hits}):
        summary([r for r in hits if (r["format"] or "?").split("-")[0] == fmt], f"format {fmt}")


if __name__ == "__main__":
    main()
