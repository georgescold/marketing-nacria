# Writing and pacing short-form vertical video scripts: evidence and practitioner frameworks

Scope: TikTok, Instagram Reels and YouTube Shorts, 30–90 s, voice-over explainers. Compiled 2026-10-16.

**Evidence labels used throughout**

| Label | Meaning |
|---|---|
| **[PLAT]** | Platform-published data or statement (YouTube, TikTok, Meta/Instagram). Often from ads, so read it as a direction, not a law. |
| **[ACAD]** | Peer-reviewed paper or arXiv preprint with a stated method. |
| **[VEND]** | Vendor or agency analysis (OpusClip, Socialinsider, Content Labs, Dash Hudson…). Usually large samples but opaque methods and a commercial interest. |
| **[PRAC]** | Practitioner opinion or experience (Kallaway, Galloway, Hoyos, MrBeast doc, Kane, Hormozi). Some of it comes only from secondhand summaries; that is flagged where it applies. |

Caveat: almost all of the evidence is English-language. French-specific data on short-form scripting was not found.

---

## 0. The ten things that matter most

1. **Most viewers are lost at the very start.** On real TikTok feeds:
   - 24 % of views are skipped before 20 % of the video has played.
   - 40 % are skipped before the halfway point.
   - Only about 45 % are watched to the end.
   - Skips concentrate in the first 5 s.

   The hook is a 1–3 s problem, not a 10 s one. [ACAD]
2. **Platforms now score the first seconds explicitly.**
   - YouTube: "Viewed vs swiped away" and "engaged views".
   - Instagram: "Skip rate" = share who leave within 3 s (since Aug 2025).
   - TikTok: completion is a strong ranking signal. [PLAT]
3. **Total watch time, not percentage, drives reach.**
   - Shorts holding more than 50 s of average view duration (AVD) averaged 4.1 M views (Galloway, 5,400 Shorts).
   - Reels of 45–60 s get the most median views (Socialinsider, 6 M Reels).
   - A geoscience TikTok account found ~60 s lecture-style videos beat shorter ones.

   [PRAC/VEND/ACAD]
4. **Negative framing lifts clicks; explicit fear words do not.**
   - Each negative word raised headline click-through by about 2.3 %.
   - Fear-word density slightly lowered it (−0.7 % per SD).

   This comes from 22,743 Upworthy A/B tests. Fear appeals do persuade, but mainly when paired with an efficacy message. [ACAD]
5. **The hook is three channels: spoken, on-screen text and visual.** They must say the same thing. On-screen text and direct address ("you") measurably raise hook rates in TikTok ad data. [PLAT/PRAC]
6. **Body structure is conflict, not a list.** Use "but / therefore" beats instead of "and then". Open small loops and close them, and rehook before attention drops. [PRAC; no controlled data]
7. **Faster, energetic narration engages more**, up to 2× within a length bucket (6.9 M edX sessions). The mechanism is enthusiasm, not raw speed. [ACAD]
8. **Pace: change the visual every few seconds, but do not hyper-cut science content.** In 14,492 short videos, including 10,000 science TikToks, sensation value had an inverted-U relation with engagement. About 12 shots per 60 s was optimal and 24 was too many. [ACAD]
9. **Endings:**
   - End on the peak and cut abruptly.
   - Close every loop.
   - Keep any call to action (CTA) short, after the payoff or at a mid-video peak.

   [PRAC; partial ad data]
10. **For health myths, follow the Debunking Handbook.**
    - Order: fact → myth stated once with a warning → why it is wrong → causal alternative → fact.
    - "Myth then correction" beat "correction only" in a TikTok experiment (N = 1,169).

    [ACAD]

---

## 1. Quantitative evidence on retention

### 1.1 How each platform measures "watched" vs "swiped"

**YouTube Shorts**

- **"Viewed vs swiped away"** (also shown as "chose to view") is the share of feed impressions where the viewer stayed rather than swiping.
- **Since 31 Mar 2025**, a public Shorts view counts every start or replay, with no minimum watch time.
- **"Engaged views"** is the old metric, renamed. It needs a meaningful watch threshold and excludes loops. It is what counts for YPP eligibility and revenue. https://techcrunch.com/2025/03/26/youtube-is-changing-how-youtube-shorts-views-are-counted [PLAT, via press]
- **Todd Sherman, Shorts product lead (2023):**
  - A swipe-past is not a view; YouTube applies an unpublished "meaningful threshold" so it cannot be gamed.
  - Recommendations start from a "seed audience" and expand or fade with its response.
  - **No specific length is rewarded:** make the length the story needs.

  https://techcrunch.com/2023/08/25/youtube-demystifies-the-shorts-algorithm-views-and-answers-other-creator-questions/ [PLAT]

**TikTok**

- The official ranking explainer says a strong interest signal ("whether a user finishes watching a longer video from beginning to end") outweighs weak ones. Follower count is not a direct factor. https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you [PLAT]
- Creator Rewards pays only on videos over 60 s, with "qualified views" of at least 5 s. This is an incentive to cross 1 min, not a ranking rule. https://metricool.com/tiktok-creator-fund/ [secondary]

**Instagram Reels**

- **Skip rate** (Reels Insights, Aug 2025, replacing "view rate") is the share of viewers who leave in the first 3 s. A retention curve was added at the same time. Instagram's wording: a high skip rate means the beginning was not engaging. https://marketing4ecommerce.net/en/retention-and-skip-rate-reels/ [PLAT, via press]
- No official benchmark exists. The "under 30–40 % is healthy" figures are unsourced vendor lore.
- Mosseri (Jan 2025) named watch time, likes per reach and sends per reach as the top Reels signals. https://stackinfluence.com/how-does-the-algorithm-for-reels-work-in-2025/ [secondary]

### 1.2 How many people leave, and when

**Real TikTok behaviour**

Zannettou et al., CHI '24, used data donations: 347 users and 9.2 M recommended videos, with viewing time inferred from timestamps. https://homes.cs.washington.edu/~franzi/pdf/zannettou-tiktok-chi24.pdf [ACAD]

| Measure | Value |
|---|---|
| Video views watched to the end | 45 % |
| Skipped before 20 % of duration | 24 % |
| Skipped before 50 % of duration | 40 % |
| Median "attention" (share of the video watched) | 82 % |
| Completion, videos from non-followed accounts | 44–46 % |
| Completion, videos from followed accounts | Lower |

Attention stayed stable across 120 days of tenure. Note that the For You feed rewards strangers' content.

**Lab replication on YouTube Shorts**

arXiv 2603.22663 (2026): 50 participants, 100 Shorts of 4–81 s (mean 35 s). https://arxiv.org/html/2603.22663v1 [ACAD, small]

- About 70 % of viewing sessions ended before 20 % of the video had played.
- **Biology and War had the lowest median retention; Animals the highest.** That is a warning sign for health and biology topics.

**When skips happen**

On the KuaiRand-Pure (Kuaishou, 1.19 M interactions) and MVA datasets, "most skips occur within the first five seconds", while video durations are spread evenly. https://arxiv.org/html/2504.03107 [ACAD]

**TikTok ads**

Salminen et al. (HT '24) studied one e-commerce account: most viewers left within the first quarter of the video. https://acua.qcri.org/blog/engagement-patterns-in-tiktok-an-analysis-of-short-video-ads/ [ACAD]

**Meta (Facebook) feed research, 2016–17, with Nielsen**

- On mobile, 47 % of a video ad's value was delivered in the first 3 s and 74 % in the first 10 s. https://www.socialmediatoday.com/social-business/facebook-releases-new-report-maximizing-potential-your-video-assets
- People spend about 1.7 s on a mobile feed item vs 2.5 s on desktop.
- Content is recalled after 0.25 s of exposure. https://beet.tv/2016/02/br16facebookduggan.html

[PLAT]

**TikTok Marketing Science**

The "Elements of Attention" study (2022; 1,650 users, 40 ads) found:

- 50 % of an ad's impact lands in the first 2 s.
- The first 6 s capture 90 % of ad-recall impact and about 80 % of awareness impact.

https://www.creatoriq.com/press/releases/tiktok-creatoriq-release-special-report-with-data-backed-keys-to-success-for-advertisers [PLAT]

TikTok's auction-ad guidance adds that more than 63 % of the highest-CTR videos state their key message within the first 3 s. https://ads.tiktok.com/business/en-US/blog/9-creative-tips-to-drive-auction-ad-performance [PLAT]

**YouTube Shorts outcomes (Paddy Galloway)**

Galloway's study covered 3.3 B views, 33 channels and 5,400 Shorts (Apr 2023, preliminary). https://threadreaderapp.com/thread/1646898356419981315.html [PRAC with data]

- Shorts with viewed-vs-swiped (VVSA) under 60 % rarely performed well; the best performers sat at 70–90 %.
- Shorts with AVD over 50 s averaged 4.1 M views.
- Likes, comments and shares showed no strong relationship with performance.
- His advice: "Treat your intro like a thumbnail."

**Completion benchmarks**

- Dash Hudson H1 2024: TikTok completion of about 25–30 % vs 67 % for YouTube. Secondary report, definitions unclear. https://www.netinfluencer.com/tiktok-instagram-reels-neck-and-neck-in-reach-report/ [VEND, unverified]
- Business videos viewed by intent (Vidyard: 66 % finish videos under 60 s; Wistia: 50 % engagement under 1 min) are **not comparable** to feed viewing. https://www.marketingprofs.com/charts/2023/49949/business-video-benchmarks-retention-rates-by-length, https://wistia.com/about/state-of-video-2022 [VEND]

**Myth to ignore: the "8-second goldfish attention span"**

It traces to an unverifiable "Statistic Brain" figure cited by Microsoft Canada in 2015. Attention researchers report stable attention across decades. The real constraint is feed competition, not human capacity. https://internet.psych.wisc.edu/wp-content/uploads/532-Master/532-UnitPages/Unit-09/Goldfish_MythBusting.pdf

### 1.3 Length vs completion vs reach

**General rule:** completion percentage falls with length, but reach follows total watch time and satisfaction. A longer video that holds people wins.

| Source | Finding | Label |
|---|---|---|
| Galloway | Longer Shorts did better on average, with outliers at every length; most creators made 20–40 s Shorts | [PRAC] |
| YouTube (Sherman) | No length preference | [PLAT] |
| Socialinsider, 6 M Reels, H1 2026 | Median views: 1–30 s 4,700; 30–45 s 8,564; **45–60 s 10,374** (engagement rate 0.35 %); 60–90 s 9,790; 90–120 s 8,000; over 180 s 4,428 (0.15 %). https://socialinsider.io/blog/instagram-reels-length/ | [VEND] |
| Socialinsider TikTok, 2023 vs 2024 | Contradict each other: 2023 said view rate fell 16.55 % past 15 s; 2024 said 90–120 s was the sweet spot. Treat TikTok length studies as noise. https://socialinsider.io/blog/how-long-are-tiktok-videos | [VEND] |
| TikTok ads | 21–34 s ads showed a +280 % conversion lift vs shorter or longer ads. https://ads.tiktok.com/business/en-US/blog/creative-that-drives-conversions | [PLAT] |
| TikTok, earlier guidance | 1 in 4 top videos were 21–34 s, with 1.6× impressions. https://onlinemarketing.de/social-media-marketing/3-minuten-videos-tiktok-videolaengen-vergleich | [PLAT] |
| Terra Explore (geoscience TikTok, 48 videos; Geoscience Communication 2022) | See below. https://gc.copernicus.org/articles/5/363/2022/ | [ACAD, single account] |
| Guo, Kim & Rubin 2014 (edX, 6.9 M sessions) | Shortest videos (0–3 min) were most engaging: 75 % of sessions watched over ¾. Median engagement was capped at about 6 min whatever the length. https://up.csail.mit.edu/other-pubs/las2014-pguo-engagement.pdf | [ACAD] |

Terra Explore findings in detail:

- Average watch was 44 % of a video; only 19 % watched to the end.
- Videos under 30 s had the highest share watched (63 %), and length correlated negatively with share watched (r = −0.41).
- The top-10 videos averaged 67 s and 58 % watched; the bottom-10 averaged 44 s and 37 %.
- Length correlated positively with like rate (r = .34) and share rate (r = .46).
- The authors' conclusion: about 60 s lecture-style videos worked best; demonstrations worked best under 30 s.

### 1.4 Loops and rewatches

- YouTube counts replays as public views (since Mar 2025), but engaged views exclude loops. Loops still add watch time, so average percentage viewed (APV) can exceed 100 %. https://www.creatoressentials.com/glossary/shorts-engaged-views/ [secondary]
- TikTok "retention" can exceed 100 % on rewatches (Dash Hudson definitions). In Zannettou's data, ≥ 200 % means a rewatch. [VEND/ACAD]
- **Practitioners:**
  - Hoyos: rewatches drive retention, and Shorts under 30 s "need >100 % retention". She plans the last line early. https://videohighlight.com/v/As7abwNhG7Y
  - Kallaway: decide the last line first; in looping videos it can set up the opening.

  [PRAC; secondhand summaries]
- **Caution:** a rewatch spike in the middle of a retention curve can also signal confusion; check where it happens. No controlled data shows that engineered seamless loops raise reach.

---

## 2. Hook science

### 2.1 What the data says

**Timing**

See §1.2. The core message must land within 2–3 s, and skips concentrate in the first 5 s.

**Negativity beats positivity, but "fear" words are not the lever**

Robertson et al., *Nature Human Behaviour* 2023: 22,743 Upworthy RCTs, 105k headline variants, 370 M impressions. https://www.psypost.org/a-particular-type-of-language-boosts-online-news-consumption-study-suggests/, paper https://epub.ub.uni-muenchen.de/94951/1/s41562-023-01538-4.pdf [ACAD]

| Word type | Effect on click-through |
|---|---|
| Each negative word | +2.3 % |
| Each positive word | −1 % |
| Sadness (per SD) | +0.7 % |
| Joy (per SD) | −0.9 % |
| Fear (per SD) | −0.7 % |
| Anger | No significant effect |

Implication: frame the hook as a loss or harm the viewer is causing ("what you do every night makes it worse"), not with scary adjectives.

**Arousal drives sharing**

Berger & Milkman 2012 (about 7,000 NYT articles plus experiments): high-arousal emotions (awe, anger, anxiety) are shared more; low-arousal sadness is shared less. https://faculty.wharton.upenn.edu/wp-content/uploads/2011/11/Virality.pdf [ACAD]

The two results look in tension, but they are not: one measures clicks and the other shares. Use negativity to get the stop, and arousal (surprise, mild alarm, awe) to get the share.

**Fear appeals do work, conditionally**

Tannenbaum et al. 2015 meta-analysis: 127 articles, 248 samples, N = 27,372. https://pubmed.ncbi.nlm.nih.gov/26501228/ [ACAD]

- Overall effect d ≈ 0.29 on attitudes, intentions and behaviours.
- Larger effects when the message includes **efficacy statements** and depicts high severity and susceptibility.
- No backfire found.

So a scary hook must be followed by a doable fix.

**Curiosity gap**

Loewenstein (1994, *Psychological Bulletin*): curiosity is the felt deprivation of an information gap. It requires some prior knowledge and a gap that seems closable. Total ignorance produces no curiosity. https://www.pbs.org/wgbh/nova/article/how-to-stimulate-curiosity/ [ACAD, via summary]

Implication: name something the viewer already knows (their forehead, their chin), then withhold the cause.

**Question vs statement hooks**

Content Labs, 14,424 TikTok and Instagram videos from 355 accounts, with views normalised to each account's typical views. https://thecontentlabs.app/blog/question-hooks-data-study [VEND]

- Spoken question hooks averaged 10.08× typical views vs 7.04× for statements.
- But the share reaching 2× typical was nearly identical (30.4 % vs 29.9 %). The gap comes from a few huge outliers.
- A statement that withholds the payoff is as good as a question.

**Hook-type rankings**

OpusClip classified 34,635 clips by AI: "comparative showdown", "direct audience engagement", "absurd statement" and "process explainer" ranked high. Generic "shock/surprise" was the most common type and below average. There are no controls and the top category has only 40 clips. https://www.opus.pro/research/best-video-hooks-tiktok [VEND, weak]

**"You" and direct address**

- TikTok × CreatorIQ (ad data) [PLAT]:
  - Saying "you" in the first 5 s: +128 % purchase intent.
  - Speaking directly to the audience: 1.5× more likely to hook.
  - Text overlays: 1.4× more likely to hook.
  - A person in the first 2 s: +50 % hooking power.

  https://www.creatoriq.com/press/releases/tiktok-creatoriq-release-special-report-with-data-backed-keys-to-success-for-advertisers
- TikTok auction ads: one in three top view-through-rate ads address the viewer directly, and 40 % use text overlays. [PLAT]
- BuzzSumo (100 M headlines, 2017): "will make you" was the top trigram, more than 2× the engagement of the runner-up. https://www.prdaily.com/?p=259705 [VEND]
- Learning research: conversational, second-person "personalization" improves processing (Ginns et al. 2013 meta-analysis, d = 0.62 on effective cognitive processing). https://researchers.westernsydney.edu.au/en/publications/designing-instructional-text-in-a-conversational-style-a-meta-ana/ [ACAD]

**Early on-screen text**

In TikTok gaming ads, text in the first 7 s gave +43 % conversion vs text that appeared later. https://ads.tiktok.com/business/en-US/blog/creative-that-drives-conversions [PLAT]

### 2.2 Practitioner frameworks

**Kallaway (Kane Callaway; >1 B short-form views; Blueprint newsletter)** [PRAC]

From a transcript of his hooks training: https://sozai.app/transcript/psychology-killer-hooks/index.md

- **Interrupt theory.** The goal is a ~1 s "freeze point" (an orienting response). The hook must answer two questions instantly: *what is this about* (subject) and *what do I get* (outcome).
- **Four S's:**
  - Subject.
  - Stakes.
  - Speed, meaning compression rather than talking faster. An 8-word hook beats a 28-word one.
  - Clarity, meaning only one possible reading.
- **Triple hook:** spoken, text and visual hooks must each predict the others. Misalignment is "the most common reason videos fail".
- **Text hook:**
  - At most 2 lines, about ⅓ down the screen.
  - On screen about 3 s.
  - Distinct from the captions.
  - Specific numbers ("22 days", not "a few weeks").
  - Built as a subject repeater plus a pain point, dream outcome or state change.
- **Visual hook:** the least important of the three. The 80/20 rule: move the body, move the visual, or move the text.
- **Lock-in zone:** the next 2–4 sentences (about 5–10 s). It must confirm the hook's claim (no bait-and-switch) and pass a rapid trust check: look, production, relatability, and proof (a "trust anchor" such as a study or screenshot).
- **Three-step hook:** "context lean → scroll-stop interjection → contrarian snapback". This comes from AI summaries only. In short: set up the expected frame, interrupt it (often with "but"), then flip it. https://opentools.ai/youtube-summary/how-to-create-irresistible-hooks-and-blow-up-your-content

**Paddy Galloway**

- Make the first second punchy and treat the intro like a thumbnail.
- Use the VVSA thresholds in §1.2.

[PRAC with data]

**Jenny Hoyos (about 13 M average views per Short, 1.6 B views over 124 Shorts)** [PRAC]

Sources: https://marketing-examined.beehiiv.com/p/jenny-hoyos-shortform-video-playbook, https://videohighlight.com/v/As7abwNhG7Y, https://www.demandcurve.com/newsletters/growth-newsletter-187

- Hook of 3 s or less, visual first frame, and at least 10 hook variants per idea.
- Power words ("free", "secret", "banned") and exact prices ("$1").
- Right after the hook, foreshadow: what is coming, what the conflict is, and what you will get.
- Target retention of 90 % or more.
- Readability at or below 5th grade, "from analysis of thousands of shorts". This is a secondhand summary.

**Brendan Kane (*Hook Point*)** https://muratulker.com/en/how-to-stand-out-in-a-3-second-world/ [PRAC]

- Generate 50–100 hook concepts, cut to 3, then iterate.
- Use an if/then structure (state the problem, then the solution).
- Put on-screen text that restates the hook.
- Never overpromise: the opening must be paid off.

**Alex Hormozi**

"Hook → Retain → Reward" (*$100M Leads*). The hook earns attention, retention keeps it (lists, steps, stories), and the reward pays off the reason the viewer came. Known only through secondary summaries. https://aivolve.beehiiv.com/p/hook-retain-reward [PRAC]

**MrBeast production memo (2024 leak, long-form)** [PRAC]

https://www.alexanderjarvis.com/memo-how-to-succeed-in-mrbeast-production/

- The first minute is where most viewers leave.
- The opening must match the promise of the title and thumbnail.
- Plan "re-engagement" moments at fixed points.
- "No dull moments."
- Endings must be abrupt "to protect retention".
- Keep it simple enough for a mass audience.

**Not found:** Vanessa Lau and Ali Abdaal. No primary, data-backed short-form scripting guidance was found; only generic "Hook–Value–CTA" blog posts misattributed to them.

---

## 3. Body structure

**"But / therefore" beats**

- Trey Parker and Matt Stone (NYU Tisch class, 2011): replace every "and then" between beats with "but" or "therefore", so each beat causes the next. https://thehustle.co/the-storytelling-secrets-that-netted-matt-stone-and-trey-parker-600-million-dollars [PRAC]
- Kallaway's "dance" alternates context and conflict, citing a Stanley Cup video with four "but then" turns in its first 30 s. https://sozai.app/transcript/become-master-storyteller/index.md [PRAC]

**Open loops and rehooks**

- Kallaway: a video is a chain of "set-up + rehook" pairs, not intro/body/conclusion. Each unanswered question is a "mental itch", and more loops mean longer stays. https://www.castmagic.io/podcast/rhythm-hooks-and-a-billion-views-kane-kallaways-short-form-video-content-secrets [PRAC]
- Hoyos re-states the premise mid-video for newcomers and keeps a recurring visual progress marker (the cup filling). [PRAC]
- No controlled data gives an optimal rehook interval. Practitioner lore says 5–10 s, consistent with Kallaway's lock-in zone and with skip-timing data.

**Payoff placement**

- Deliver partial value early: the lock-in zone confirms the claim.
- Keep the biggest reveal for the last third.
- Every loop opened must be closed in the same video. MrBeast's memo and Kane both warn that unpaid promises destroy trust. [PRAC]

**Sentence length and rhythm**

- Analysis of 3,931 TED talks against YouTube engagement found engagement highest at about 8 words per sentence, recommending brief sentences and plain referential language. *Electronic Commerce Research* 26(1), 2026. https://researchwith.montclair.edu/en/publications/what-makes-things-catch-on-understanding-consumer-engagement-with/ [ACAD, correlational]
  - The same abstract's "0.8 s per word" works out to about 75 wpm. That probably includes pauses and conflicts with Guo's data, so ignore it.
- A 2026 preprint scored 1,239 TED transcripts with LLMs and found clarity the strongest predictor of likes and views. https://arxiv.org/abs/2604.04583 [ACAD, preprint]
- Kallaway: vary sentence length (short, medium, long, after Gary Provost); uniform sentences sound monotonous. [PRAC]

**One idea per sentence and cutting extras**

Mayer's coherence principle (removing extraneous words, sounds and pictures) has a median effect of about d = 0.86 on learning in lab tests. https://resolve-he.cambridge.org/core/books/cambridge-handbook-of-multimedia-learning/principles-for-reducing-extraneous-processing-in-multimedia-learning-coherence-signaling-redundancy-spatial-contiguity-and-temporal-contiguity-principles/CD5B7AE1279A9AB81F8EEBB53DBEC86E [ACAD]

**Reading level and jargon**

- Jargon impairs processing fluency, increases resistance to persuasion and lowers interest, **even when definitions are provided**.
  - Bullock et al. 2019, *Public Understanding of Science*, N = 650: https://comm.osu.edu/sites/comm.osu.edu/files/PUS%202019-%20Bullock%20et%20al..pdf
  - Shulman et al. 2020: https://pmc.ncbi.nlm.nih.gov/articles/PMC7540871

  [ACAD]
- Hoyos targets 5th-grade readability or lower. [PRAC]

**Speaking rate**

Guo, Kim & Rubin 2014 (edX, 6.9 M sessions) [ACAD]:

- Speaking rates ranged from 48 to 254 wpm (mean 156).
- Within each length bucket, engagement rose **up to 2×** with faster speech.
- The 145–165 wpm bucket was the least energetic and least engaging.
- The authors found no comprehension problems even at 254 wpm when visuals carried the same information.
- They attribute the effect to enthusiasm, not raw speed: speeding up a flat speaker will not help.
- edX editors strip "umm", fillers and dead pauses.

Kallaway adds that slow, podcast-style pacing underperforms on TikTok and Reels. [PRAC]

The project's convention (native-French voice at 190–210 wpm, constant pace) sits in the high-engagement zone of this data.

**Numbers and specificity**

- Statistical evidence moves beliefs and attitudes more; narrative evidence moves intention more. Zebregs et al. 2015 meta-analysis, *Health Communication*: https://pubmed.ncbi.nlm.nih.gov/24836931/ [ACAD]
- Pair one concrete number with one concrete case.
- Kallaway, Hoyos and Kane all push exact numbers and prices over vague quantities. [PRAC]

**Second person**

See §2.1: "you" in the first 5 s, direct address, and the personalization effect.

---

## 4. Pacing and editing

**Shot length baseline**

Average shot length in Hollywood film fell from 8–10 s (1960s) to 3–4 s (2005) (Cutting, DeLong & Nothelfer 2010, 150 films). The authors frame this as filmmakers controlling attention better, not as attention spans shrinking. https://www.nationalgeographic.com/culture/article/100225-foxnews-science-of-hollywood-films-chaos-theory [ACAD]

**Too much stimulation hurts engagement**

Xue et al. 2026 built a computational "message sensation value" (MSV) model from cuts, motion, loudness, faces and brightness. It was trained on 1,200 videos and validated on 14,492, including 10,000 science-related TikToks. https://arxiv.org/pdf/2604.19995 [ACAD, preprint]

- MSV is linearly related to sensory arousal.
- But it has an **inverted-U** relation with likes, comments and shares.
- Example: about 12 shots per 60 s (one shot ≈ 5 s) was optimal, while the high-MSV version with about 24 shots "may distract".
- An earlier study cited there (W. Zhang et al. 2023) found MSV *negatively* predicted engagement for authoritative TikTok accounts.

**More scenes help ads up to a point**

TikTok ad data [PLAT]:

- Multiple scenes: +38 % conversion vs one continuous shot (e-commerce).
- Five or more scenes: +171 % (gaming).
- Seamless transitions: +60 % ad recall.
- Music above 120 BPM: higher view-through rate.
- High-energy pacing: +162 % (beauty sample).

Sources: https://ads.tiktok.com/business/en-US/blog/creative-that-drives-conversions, https://ads.tiktok.com/business/en-US/blog/9-creative-tips-to-drive-auction-ad-performance

**Music tempo for expert debunks**

Li, Li & Yang 2024, *Journal of Computer-Mediated Communication*: in medical-expert TikTok videos debunking a vaccine-infertility myth, **high-tempo background music made the correction more effective**, mainly by suppressing counterarguing. It did not do the same for lay testimonials. https://doi.org/10.1093/jcmc/zmae007 [ACAD]

**Static frames**

- In Guo's data, Khan-style continuous drawing kept engagement high even at slow speech; the continuous motion was the authors' explanation. [ACAD]
- Kallaway's minimal visual rule: something must move (body, visual or text). [PRAC]
- OpusClip claims "pattern interrupts every 4 s gave 58 % vs 41 % retention" but gives no source or sample. https://www.opus.pro/blog/tiktok-length-format-retention-data [VEND, weak]

**B-roll must match the words**

Mayer's temporal contiguity principle (narration simultaneous with the matching image) has the largest effect of the multimedia principles, about d ≈ 1.3. Signaling (highlighting key words and visuals) is about d ≈ 0.4–0.7. [ACAD]

In practice: the image on screen should depict the noun being spoken at that moment.

**On-screen text and captions**

- 69 % of US adults watch with the sound off in public, and 80 % say they are more likely to finish a captioned video (self-report). Verizon Media / Publicis 2019, n = 5,616. https://www.streamingmedia.com/Articles/News/Online-Video-News/80-of-Video-Caption-Users-Arent-Hearing-Impaired-Finds-Verizon-131860.aspx
- Facebook's internal tests: captions raised view time by 12 %. https://3playmedia.com/blog/captions-increase-viewership-for-facebook-video-ads
- TikTok × Kantar (2021): 88 % of users say sound is essential on TikTok. https://www.socialmediatoday.com/news/tiktok-shares-new-insights-into-the-importance-of-sound-for-marketing-promo/601569
- TikTok ads: captions or on-screen text showing the offer gave +80 % conversion. [PLAT]
- Mayer's redundancy principle: verbatim on-screen text plus narration plus animation can hurt *learning* in lab settings. Feed reality (sound-off viewers) outweighs this.
- **Net:** design for both sound-on and sound-off. Use short keyword captions synced to the voice, plus a separate text hook.

---

## 5. Endings

**Peak, then cut**

- MrBeast memo: endings "must always be abrupt to protect retention", and do not signal the ending early. [PRAC]
- Hoyos ends on the highest-intensity moment (punchline, twist or heart-warming beat), then cuts. Lingering after the high note kills rewatches. [PRAC]
- Kallaway: make the final line shareable. [PRAC]

**Loop endings**

A last line that flows back into the first can create rewatches, which add watch time and, since 2025, public YouTube views. There is no controlled evidence on reach, and a forced loop can feel like a trick (see §1.4). [PRAC]

**CTAs**

- Data on CTAs in organic shorts is thin.
- Ad data shows clear CTAs drive *action* [PLAT]:
  - Explicit text CTA: +152 % conversion.
  - Strong written CTA: +205 % purchase intent.
- Practitioners report retention dips during CTAs and recommend putting the ask right after the value lands, or mid-video at a peak. [PRAC]
  - Hoyos's $1 ice-cream Short slips a humorous "one subscriber" CTA in halfway at peak action.
  - Galloway saw better subscriber conversion from Shorts on channels with over 1 M subscribers, and speculated that stronger CTAs were one reason.

**Educational and health accounts**

- Zhu & Che 2024, *Behavioral Sciences*, 81 Douyin nutrition videos from one institute [ACAD]:
  - Ending with an explicit *recommendation* was associated with 2.5× comments.
  - An explicit *conclusion* statement was associated with **fewer shares** (OR 0.56).
  - Practical-skill topics had the strongest effects (OR ≈ 6.6 likes, 7.1 shares).
  - Personification and science visualisation were associated with more new followers (OR ≈ 1.55–1.61).

  https://pmc.ncbi.nlm.nih.gov/articles/PMC10968627/
- Debunking Handbook: end by restating the fact, with a causal alternative. [ACAD consensus]

**Synthesis**

- Close every loop and land the payoff.
- Restate the takeaway in one line.
- CTA of 3 s or less with a reason ("abonne-toi pour…").
- Hard cut.
- No "next video" teaser: it opens a loop that the video does not close.

---

## 6. Faceless voice-over, documentary and health explainers

### AI and synthetic voices

- Modern TTS can match human narration for learning. Mayer & DaPra 2012 found no difference, and Craig & Schroeder 2017 found a modern engine rated similar to a human for learning and credibility. That summary comes from a vendor. https://www.readspeaker.com/blog/elearning-voice [ACAD, via vendor]
- **Labelling** a voice as AI lowers trust and advice-following, even when the audio is identical. https://escholarship.org/uc/item/8vr8s6h8 [ACAD]
- Studio Resonate measured −27 % trust when listeners were primed that a voice was AI, while listeners could not tell AI from human beyond chance. https://www.contentgrip.com/studio-resonate-ai-voice-study/ [VEND], https://www.arxiv.org/pdf/2602.20061 [ACAD]
- Implication: invest in a natural, warm, native voice, and comply with platform AI-content labels. Credibility then has to come from content cues, not the voice.

### Credibility in health and science

- Debunking Handbook 2020 (consensus of 22 misinformation scholars) [ACAD]:
  - For corrections, perceived **trustworthiness matters more than expertise**.
  - Health professionals or organisations are ideal.
  - Use a messenger the target group trusts.

  https://sks.to/db2020
- A faceless account with no diploma cannot claim expertise. It can borrow it: show the source (institution, journal, year) on screen as a Kallaway-style "trust anchor", and keep a neutral, non-salesy tone.
- An experiment (*Health Communication* 2024, n = 956, ~30 s TikTok-style videos) tested an expert vs a user and a visible scientific reference vs none. Results were not retrieved; worth reading before deciding on on-screen citations. https://www.informahealthcare.com/doi/full/10.1080/10410236.2023.2301201

### What acne content performs

- **Top-100 #acne TikToks, June 2023** (Cureus): https://pmc.ncbi.nlm.nih.gov/articles/PMC10576439/ [ACAD]
  - Physician videos averaged 712k views vs 312k for non-physicians.
  - **Personal-experience** videos had the most views (668k) and the best DISCERN quality score.
  - **Home remedies** drew the most shares (1,305) and saves (3,272).
  - Pure "educational" videos had the fewest views (435k).
- **Top 300 acne-treatment videos per platform** (*JMIR Dermatology* 2023): https://pmc.ncbi.nlm.nih.gov/articles/PMC10448278/ [ACAD]
  - Laypersons had by far the highest engagement but the lowest quality: DISCERN 36.3 vs 46.1 for dermatologists.
  - Mean views per video: TikTok 1.64 M vs YouTube Shorts 690k vs Reels 27k.
- **Implication:** wrap education in a personal case and a practical, saveable takeaway. Pure lecture underperforms.

### Myth-busting structure

- **Debunking Handbook order:**
  1. **Fact** first, if it is short and sticky.
  2. **Warn** that a myth is coming, and state the **myth once**.
  3. Explain the **fallacy**: why it misleads.
  4. Give the **fact** again, with a **causal alternative** that fills the gap the myth leaves.
- Backfire effects are rare, and one repetition of the myth directly before the correction helps belief updating. https://sks.to/db2020 [ACAD]
- Bhargava et al. 2023, Harvard Misinformation Review, N = 1,169 [ACAD]:
  - Showing the TikTok myth and then a TikTok debunk reduced false belief (d = −0.17).
  - That beat correction alone (d = −0.12).
  - Effects on truth discernment were marginal.

  https://misinforeview.hks.harvard.edu/article/how-effective-are-tiktok-misinformation-debunking-videos/
- This fits the project's "myth as debunked hook" model, as long as the myth is clearly flagged and corrected in the same video.

### Tone and emotion

- Fear plus efficacy (Tannenbaum).
- Negativity without fear vocabulary (Robertson).
- Statistics plus a story (Zebregs).
- Moderate sensation, not hyper-edited (Xue).
- High-tempo music for expert-style debunks (Li et al.).

### Faceless and documentary formats

- Zack D Films, a leading faceless 3D explainer channel, hires for "20–45 second 3D clips" (job post). https://remotestack.in/jobs/3d-generalist-zack-d-films-llc-ee47b683-739f-4404-9e5a-f2d2244e828f
- Terra Explore found lecture-style about 60 s optimal (§1.3).
- The COFCO nutrition institute uses a 30–40 s format.
- Biology topics retain worst in the lab study (§1.2). Anchor the explanation on a visible, personal stake (*your* skin, *this* spot) rather than abstract physiology.

---

## 7. Twenty rules for a 45–75 s French faceless health explainer script

**Tags:**

- **DATA:** backed by platform or academic data.
- **MIXED:** data plus practitioner inference.
- **PRAC:** practitioner opinion only.

### Hook (0–3 s)

1. **No intro. State subject and stakes in the first spoken line: about 10 words or fewer, under 2 s.** Never open with "Aujourd'hui on va parler de…". **DATA**
   - More than 63 % of top-CTR TikTok ads state the key message within 3 s.
   - 50 % of ad impact lands in the first 2 s.
   - Meta: 47 % of video value in the first 3 s.
   - Most skips happen under 5 s, and 24 % of TikTok views die before 20 % of the video.

2. **Frame 1 is a thumbnail.** The subject (the zone, the spot) is visible and already moving at 0.0 s, and the text hook is on screen from the first frame. **MIXED**
   - Galloway: "treat your intro like a thumbnail".
   - Text overlays are 1.4× more likely to hook.
   - Text in the first 7 s gave +43 % conversion (TikTok).

3. **Align the triple hook.** Voice, text and image make one claim. The text hook is at most 2 lines, about ⅓ down the screen, held about 3 s, and separate from the captions. **PRAC** (Kallaway), partly **DATA** (TikTok text-overlay figures).

4. **Frame the hook as a loss or harm the viewer causes, not with fear adjectives.** Any threat raised in the hook must get a concrete, doable fix later in the video. **DATA**
   - Robertson 2023: +2.3 % CTR per negative word, but −0.7 %/SD for fear words.
   - Tannenbaum 2015: fear appeals work mainly with efficacy statements, plus high severity and susceptibility.

5. **Say "tu" within the first 5 s and keep second person throughout.** **DATA** (ad and learning contexts)
   - TikTok × CreatorIQ: "you" in the first 5 s gave +128 % purchase intent; direct address was 1.5× more hooking.
   - Personalization meta-analysis.

6. **Open one closable curiosity gap.** Name something the viewer already knows (their chin, their pillowcase) and withhold the cause or answer. A question or a payoff-withholding statement both work. Write at least 10 hook variants and keep the clearest. **MIXED**
   - Loewenstein 1994.
   - Content Labs: question hooks +43 % mean, but equal at the median.
   - Hoyos's 10-hook practice; Kane's 50–100 concepts.

### Lock-in and body (3–60 s)

7. **Seconds 3–10 (lock-in zone): confirm the hook's claim and show one trust anchor**, such as a figure with a named source on screen (institution plus year). No bait-and-switch. **MIXED**
   - Kallaway's lock-in zone and trust anchor [PRAC].
   - Debunking Handbook: source credibility and trustworthiness drive corrections [DATA].

8. **Build 3–5 beats linked by "mais" or "donc", never "et puis".** End each beat on a new question, i.e. a rehook roughly every 8–12 s. **PRAC**
   - Parker & Stone; Kallaway's "dance" and set-up/rehook pairs; Hoyos foreshadowing.
   - No controlled data exists on the interval.

9. **Myth format: fact (if pithy) → "on t'a dit que…" (the myth once, flagged) → why it is wrong → the real cause (causal alternative) → fact again.** Never repeat the myth a second time. **DATA**
   - Debunking Handbook 2020.
   - Bhargava 2023: myth-then-correction d = −0.17 vs −0.12 for correction only.

10. **One idea per sentence, averaging about 8–12 words, with a mix of very short and longer sentences.** **MIXED**
    - TED engagement peaked near 8 words per sentence (n = 3,931).
    - Mayer coherence d ≈ 0.86.
    - Kallaway on rhythm.

11. **No unexplained jargon:** "pore bouché", not "comédon"; "hormones mâles", not "androgènes". Jargon still hurts processing even when defined, so replace it rather than define it. **DATA**
    - Bullock 2019 (N = 650); Shulman 2020.

12. **Use exact, true numbers ("3 semaines", "1 adulte sur 4"), each tied to a source you can show.** Never invent precision. **MIXED**
    - Kallaway on specific numbers [PRAC].
    - Zebregs 2015: statistics move beliefs [DATA].
    - Project rule: no false health claims.

13. **Pair every key statistic with a micro-case** (one person, one spot, one habit). Statistics shift beliefs; narrative shifts intention to act. **DATA**
    - Zebregs 2015.
    - #acne TikTok: personal-experience videos had the most views and the best quality.

14. **Narrate at 190–210 wpm with energy and a constant pace; strip fillers and dead pauses, keeping breaths.** **DATA** for direction (Guo 2014: up to 2× engagement for faster, enthusiastic speech; 145–165 wpm was the least engaging), **PRAC** for the exact French figure (project convention). Word budgets:

    | Duration | Words |
    |---|---|
    | 45 s | about 140–150 |
    | 60 s | about 190–200 |
    | 75 s | about 235–250 |

    Deduct about 5–8 s for the visual hook beat and the CTA.

15. **Let the script set the length within 45–75 s, but every second must hold.** Total watch time beats completion percentage.
    - Targets: viewed vs swiped away of 70 % or more (YouTube); a flat retention curve; Instagram skip rate as low as possible.
    - Do not pad past 60 s just for TikTok rewards if the curve sags.
    - **DATA:**
      - Galloway: VVSA under 60 % rarely worked; AVD over 50 s averaged 4.1 M views.
      - Socialinsider: 45–60 s Reels get the most median views.
      - Terra Explore: about 60 s lecture-style videos did best.
      - YouTube: no length preference.

### Visuals and sound

16. **Change the image every 3–5 s, and make each shot show the noun being spoken.** Avoid hyper-cutting at 24 or more shots per minute on science content. **DATA**
    - Xue 2026: inverted U, with about 12 shots per 60 s optimal across 10k science TikToks.
    - Mayer temporal contiguity d ≈ 1.3.
    - TikTok: multiple scenes +38 %.
    - Film average shot length 3–4 s.

17. **No frozen frame longer than about 4–5 s.** If a scene must be held, something moves: a slow push-in, animated text or a moving element. **MIXED**
    - Guo: continuous motion sustained engagement [DATA].
    - Kallaway's "move something" rule [PRAC].
    - OpusClip's 4 s figure [VEND, weak].

18. **Design for sound-off:**
    - Burned-in keyword captions synced word-by-word (no punctuation, per project style).
    - A separate text hook.
    - Key numbers on screen.
    - Captions must not cover the subject.

    **DATA**
    - 69 % watch sound-off in public; captions gave +12 % view time (Facebook).
    - 40 % of top view-through-rate TikTok ads use text overlays.
    - Mayer's redundancy caution means keywords, not paragraphs.

19. **Keep a driving pulse in the music,** even with a grave, documentary score: a tempo of 120 BPM or more, kept well under the voice. A slow, ambient bed is the weakest choice for debunks. **DATA**
    - TikTok: tracks above 120 BPM drive higher view-through rate.
    - Li, Li & Yang 2024: high-tempo music made expert debunks more persuasive by reducing counterarguing.
    - Note: this partly tensions with a purely "grave" score. Test a grave-but-pulsed track against a slow one.

### Ending

20. **Close every loop, put the strongest line last, then cut hard.** **MIXED**
    - The CTA ("abonne-toi" + reason) is 3 s or less and comes right after the payoff (or as a mid-video aside at a peak).
    - Restate the fact once.
    - No "next part" teaser.
    - Sources:
      - MrBeast memo: abrupt endings [PRAC].
      - Hoyos: peak ending [PRAC].
      - Debunking Handbook: finish on the fact [DATA].
      - TikTok: clear text CTA +152 % conversion (ads) [DATA].
      - Zhu & Che: a recommendation ending gave 2.5× comments, while a "conclusion" statement went with fewer shares [DATA].

### Where the evidence is weakest

- The interval between rehooks.
- Loop effects on reach.
- CTA cost and benefit in organic content.
- Exact French speech-rate optimum.
- Hook-type rankings: vendor data, outlier-driven.

A/B test these on the accounts themselves: same topic, one variable changed, compared on viewed-vs-swiped and skip rate.

---

## Source index (primary first)

**Platforms**

- https://techcrunch.com/2025/03/26/youtube-is-changing-how-youtube-shorts-views-are-counted
- https://techcrunch.com/2023/08/25/youtube-demystifies-the-shorts-algorithm-views-and-answers-other-creator-questions/
- https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you
- https://ads.tiktok.com/business/en-US/blog/9-creative-tips-to-drive-auction-ad-performance
- https://ads.tiktok.com/business/en-US/blog/creative-that-drives-conversions
- https://www.creatoriq.com/press/releases/tiktok-creatoriq-release-special-report-with-data-backed-keys-to-success-for-advertisers
- https://www.socialmediatoday.com/social-business/facebook-releases-new-report-maximizing-potential-your-video-assets
- https://beet.tv/2016/02/br16facebookduggan.html
- https://marketing4ecommerce.net/en/retention-and-skip-rate-reels/

**Academic**

- Zannettou CHI '24: https://homes.cs.washington.edu/~franzi/pdf/zannettou-tiktok-chi24.pdf
- arXiv 2603.22663: https://arxiv.org/html/2603.22663v1
- arXiv 2504.03107: https://arxiv.org/html/2504.03107
- Salminen HT '24: https://acua.qcri.org/blog/engagement-patterns-in-tiktok-an-analysis-of-short-video-ads/
- Guo 2014: https://up.csail.mit.edu/other-pubs/las2014-pguo-engagement.pdf
- Terra Explore: https://gc.copernicus.org/articles/5/363/2022/
- Robertson 2023: https://epub.ub.uni-muenchen.de/94951/1/s41562-023-01538-4.pdf
- Berger & Milkman: https://faculty.wharton.upenn.edu/wp-content/uploads/2011/11/Virality.pdf
- Tannenbaum 2015: https://pubmed.ncbi.nlm.nih.gov/26501228/
- Zebregs 2015: https://pubmed.ncbi.nlm.nih.gov/24836931/
- Xue et al. (MSV): https://arxiv.org/pdf/2604.19995
- Li, Li & Yang 2024: https://doi.org/10.1093/jcmc/zmae007
- Bullock 2019: https://comm.osu.edu/sites/comm.osu.edu/files/PUS%202019-%20Bullock%20et%20al..pdf
- Shulman 2020: https://pmc.ncbi.nlm.nih.gov/articles/PMC7540871
- TED engagement (*Electronic Commerce Research* 2026): https://researchwith.montclair.edu/en/publications/what-makes-things-catch-on-understanding-consumer-engagement-with/
- TED clarity preprint: https://arxiv.org/abs/2604.04583
- Ginns 2013: https://researchers.westernsydney.edu.au/en/publications/designing-instructional-text-in-a-conversational-style-a-meta-ana/
- Debunking Handbook: https://sks.to/db2020
- Bhargava 2023: https://misinforeview.hks.harvard.edu/article/how-effective-are-tiktok-misinformation-debunking-videos/
- #acne TikTok (Cureus): https://pmc.ncbi.nlm.nih.gov/articles/PMC10576439/
- Acne multi-platform (*JMIR Dermatology*): https://pmc.ncbi.nlm.nih.gov/articles/PMC10448278/
- Zhu & Che 2024: https://pmc.ncbi.nlm.nih.gov/articles/PMC10968627/
- AI voice labelling: https://escholarship.org/uc/item/8vr8s6h8
- AI voice detection: https://www.arxiv.org/pdf/2602.20061
- Health Communication 2024 (expert vs user): https://www.informahealthcare.com/doi/full/10.1080/10410236.2023.2301201
- Mayer, *Cambridge Handbook*: https://resolve-he.cambridge.org/core/books/cambridge-handbook-of-multimedia-learning/principles-for-reducing-extraneous-processing-in-multimedia-learning-coherence-signaling-redundancy-spatial-contiguity-and-temporal-contiguity-principles/CD5B7AE1279A9AB81F8EEBB53DBEC86E
- Cutting (shot length): https://www.nationalgeographic.com/culture/article/100225-foxnews-science-of-hollywood-films-chaos-theory

**Vendor**

- https://socialinsider.io/blog/instagram-reels-length/
- https://socialinsider.io/blog/how-long-are-tiktok-videos
- https://thecontentlabs.app/blog/question-hooks-data-study
- https://www.opus.pro/research/best-video-hooks-tiktok
- https://www.opus.pro/blog/tiktok-length-format-retention-data
- https://www.streamingmedia.com/Articles/News/Online-Video-News/80-of-Video-Caption-Users-Arent-Hearing-Impaired-Finds-Verizon-131860.aspx
- https://3playmedia.com/blog/captions-increase-viewership-for-facebook-video-ads
- https://www.contentgrip.com/studio-resonate-ai-voice-study/
- https://www.marketingprofs.com/charts/2023/49949/business-video-benchmarks-retention-rates-by-length
- https://wistia.com/about/state-of-video-2022
- https://www.prdaily.com/?p=259705

**Practitioners**

- Galloway: https://threadreaderapp.com/thread/1646898356419981315.html
- Kallaway: https://sozai.app/transcript/psychology-killer-hooks/index.md, https://sozai.app/transcript/become-master-storyteller/index.md, https://www.castmagic.io/podcast/rhythm-hooks-and-a-billion-views-kane-kallaways-short-form-video-content-secrets
- Hoyos: https://marketing-examined.beehiiv.com/p/jenny-hoyos-shortform-video-playbook, https://videohighlight.com/v/As7abwNhG7Y, https://www.demandcurve.com/newsletters/growth-newsletter-187
- MrBeast memo: https://www.alexanderjarvis.com/memo-how-to-succeed-in-mrbeast-production/
- Kane: https://muratulker.com/en/how-to-stand-out-in-a-3-second-world/
- Parker & Stone: https://thehustle.co/the-storytelling-secrets-that-netted-matt-stone-and-trey-parker-600-million-dollars
- Hormozi (secondary): https://aivolve.beehiiv.com/p/hook-retain-reward
