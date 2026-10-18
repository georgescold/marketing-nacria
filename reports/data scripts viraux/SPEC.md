# Viral short-video script corpus: collection spec

**Goal:** collect full transcripts and stats of viral short videos (TikTok, YouTube Shorts, Reels) so that a script style can be derived from data.

## Output format

One JSON object per line, appended to `<your_file>.jsonl` in this folder (UTF-8, `ensure_ascii=False`).

```json
{"id": "tiktok_7292116277689060613", "platform": "tiktok", "url": "...", "account": "@dr.jose.garza",
 "followers": 1200000, "views": 7000000, "likes": 0, "comments": 0, "shares": 0, "saves": 0,
 "posted": "2023-10-22", "duration_s": 59, "language": "es", "niche": "skin|health|food|science|...",
 "format": "faceless-3d | faceless-stock | faceless-text | face-talking | voiceover-animation | ...",
 "is_control": false,
 "caption": "the post caption/title",
 "cues": [[0.0, 2.1, "first caption line"], [2.1, 4.0, "..."]],
 "transcript": "full spoken text, in order",
 "transcript_source": "tiktok-webvtt | youtube-json3 | ...",
 "notes": "anything visible from the page: on-screen text style, series name, voice type"}
```

- **`cues`:** keep the original timestamps.
- **Missing stats:** use `null`.
- **`is_control: true`:** for a low performer from the same account, i.e. under 10 % of that account's usual views. Controls show what separates a hit from a flop on the same channel.

## How to get transcripts (no login, no video download)

### TikTok

1. Fetch `https://www.tiktok.com/@user/video/<id>` with a desktop browser User-Agent.
2. Parse the JSON in `<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__">`:
   - `["__DEFAULT_SCOPE__"]["webapp.video-detail"]["itemInfo"]["itemStruct"]`
   - `stats` (playCount, diggCount, commentCount, shareCount, collectCount)
   - `authorStats.followerCount`
   - `video.duration`
   - `video.subtitleInfos[]`: each has a `Url` to a WebVTT file and a `LanguageCodeName`. Pick the original language (ASR); a "MT" source means machine translation.
3. Fetch that VTT and parse its cues.

### YouTube

- The watch page or shorts page holds `ytInitialPlayerResponse`, which contains `captions.playerCaptionsTracklistRenderer.captionTracks[].baseUrl`. Append `&fmt=json3`. This may fail; if so, skip the video.
- Views and length are in `videoDetails`.

### Finding videos

- Use WebSearch, plus the account and video pages you can reach.
- Prefer videos whose view counts you can read on the page.

## Rules

- Public pages only.
- Never sign in, never download video files, never bypass a captcha.
- Transcripts are for internal analysis only.
