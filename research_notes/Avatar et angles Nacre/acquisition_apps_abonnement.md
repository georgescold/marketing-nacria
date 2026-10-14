# Paid acquisition & funnel playbooks for consumer subscription apps (beauty / skin / wellness / women's health), 2025–2026: benchmarks for Nacre's French launch

Scope note: research done on 1 Oct 2026. Sources are listed with the latest first. "WE" means RevenueCat's "Western Europe" bucket, which includes France (UK, DE, FR, ES, IT, NL, Nordics, BE, AT, CH, IE, PT…). US-only figures are labelled **[US]**. Vendor or agency figures that come from a single company's client base are labelled **[vendor data]**. In RevenueCat's data, "Health & Fitness" (H&F) also includes Medical, and "Social & Lifestyle" includes Lifestyle. Nacre could be listed under either, and Lifestyle apps perform worse.

---

## 1. Funnels: app-store-direct vs web-to-app (quiz → plan → web paywall → download) vs waitlist/pre-launch

### Takeaway
Web-to-app (W2A) has become the default acquisition path for top-grossing health/fitness subscription apps. Vendor data shows about 2× the end-to-end conversion of in-app funnels, plus a large margin gain. That gain is now larger in the EU: from 1 Oct 2026, Apple charges 15% on IAP for small developers versus 2–3% (about 6% all-in) for web payments. W2A is not automatically better, though. It needs its own funnel, its own payments stack (with about 30–50% failed payments to recover) and Meta optimisation on web events, and health and wellness advertisers can be restricted on web events. For a pre-launch app at Nacre's stage, the evidence supports this order: launch with app-store-direct plus an onboarding quiz in the app, build a web quiz → plan → paywall funnel as a second track, and use the waitlist to concentrate installs on launch day.

### Cited Findings

**Web-to-app performance and adoption**
- FunnelFox "State of Web2App 2026" (published Jan 2026, FunnelFox client apps above minimum traffic/revenue thresholds, raw N not disclosed) **[vendor data]**:
  - Web funnels convert 3.0% end-to-end versus 1.5% for in-app funnels ("2× better").
  - 13% of quiz starters reach the paywall, and 3% purchase. "The biggest drop happens before the paywall."
  - Payment methods: Apple Pay ~60%, cards ~20%, PayPal ~18%, Google Pay ~2%.
  - "30–50% of initiated payments fail." The first 3 retry attempts recover almost half, and retry logic adds 15–20% revenue.
  - W2A revenue by plan: monthly 48.8%, weekly 30.5%, annual 12.2%, 3-month 8.4%.
  - W2A revenue by offer: no-trial offers 56.8%, paid trial 28.9%, free trial 14.3%.
  - Revenue by region: US 63.7%, Europe 14.2%.
  - 92% of refunds happen in the first month.
  - Retention to month 12: weekly plans 3%, monthly plans 10%.
  - "82% of top-grossing apps use Web2App". Adoption is up 77% year on year.
  - Sources: [FunnelFox State of Web2App 2026](https://funnelfox.com/state-of-web2app-2026); [GlobeNewswire release, 20 Jan 2026](https://www.globenewswire.com/news-release/2026/01/20/3221719/0/en/FunnelFox-Releases-the-State-of-Web2app-2026-Report.html)
- An earlier FunnelFox summary (2025 edition) put Europe at ~12% of W2A revenue. It also said W2A apps keep 85–97% of revenue, versus 70–85% through IAP. Health & Fitness is the largest W2A category by volume — [FunnelFox State of Web2App (2025)](https://funnelfox.com/state-of-web2app/)
- FunnelFox/Kirill Makarov analysed 311 web funnels (9 Jan 2025) **[vendor data]**:
  - Web funnels launched rose 63% from 2023 to 2024, and spy tools found 600% more W2A ad creatives.
  - Meta reported 50% year-on-year growth in web-to-app spend.
  - Web purchase → app download is about 90–95%.
  - Email capture plus retargeting adds 5–10% of revenue, and up to 20% for market leaders.
  - Offers are moving from paid trials to intro discounts (50–70% off the first period), usually on 3-option paywalls.
  - Noom runs "six different upsells and two upgrade options… 25 screens after the initial purchase".
  - Source: [FunnelFox blog, 2025](https://blog.funnelfox.com/web-to-app-funnels-insights-and-trends)
- RevenueCat "State of Subscription Apps 2026" (SOSA 2026; 115,000+ apps, $16B revenue, 1B+ transactions, mostly 2025 data, iOS/Android/web):
  - 41% of top-revenue-tier apps (Tier 5) earn web revenue. The figure is 28% for Tier 4 and 1.3% for hobby apps (Tier 1).
  - Thomas Petit (consultant, quoted in the report): web revenue "suddenly exploded in 2025". Web-to-app is "now mainstream", and app-to-web link-outs are "just starting".
  - Source: [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps)
- RevenueCat, Daphne Tideman (11 Dec 2025):
  - Web payment processing costs about 2–3%, or about 6% with all fees, versus 15–30% on the app stores.
  - W2A often shows "lower initial conversion" but better retention and LTV.
  - The failed-payment rate is "around 50%" before retries.
  - Suggested offers: a paid trial (e.g. $1 for 7 days), a single annual plan on web with monthly pricing in-app, web-exclusive discounts, money-back guarantees.
  - Source: [RevenueCat blog, 2025](https://www.revenuecat.com/blog/growth/web-to-app-funnels)
- RevenueCat, Nathan Hudson (15 Jul 2025): "web-to-app funnels are not onboarding quizzes". Quizzes suit apps that need deep personalisation, education or an emotional connection, such as H&F. Alternatives include landing page → checkout, email → web paywall, smart banners/QR codes and webinars — [RevenueCat blog, 2025](https://www.revenuecat.com/blog/growth/web-to-app-funnels-are-not-onboarding-quizzes)
- Marcus Burke (Meta ads advisor) to RevenueCat (8 Apr 2025):
  - Both app campaigns and W2A are needed to scale beyond about $500K/month.
  - W2A is "especially interesting for reaching older users".
  - Blinkist's web campaigns delivered about 80% of impressions on Facebook Feed, to older, higher-paying audiences.
  - Source: [RevenueCat blog, 2025](https://www.revenuecat.com/blog/growth/meta-ads-in-2025-tips-for-apps)

**Quiz/funnel structures and lengths (health/beauty examples)**
- FunnelFox teardown (21 Jan 2026):
  - Quiz lengths: Babbel 20+ screens, Flirtist 15–20, Nebula ~30, Lasta Fit (fitness) 30+, Fastic (weight loss) ~60.
  - Common mechanics: micro-rewards between quiz steps "to prevent fatigue", progress bars, "building your plan" screens, social proof mid-funnel, and a profile/plan summary before the paywall.
  - Checkout elements: discount timers, money-back guarantees, trust badges, 3-plan anchoring, per-day price framing (Fastic: "$0.22–$0.86 per day"), and "choose your trial price" (Nebula: €1/€5/€9/€13.67).
  - Source: [FunnelFox blog, 2026](https://blog.funnelfox.com/web2app-funnel-patterns-2026/)
- Noom's web onboarding runs "up to 113 screens", 10–15 minutes. RevenueCat lists 12 principles from it, including:
  - explain why personal questions are asked;
  - reassure after sensitive moments;
  - show results before asking for contact info;
  - use the quiz for commitment, not only data;
  - teach the method during onboarding;
  - build commitment before the price reveal.
  - Source: [RevenueCat, Daphne Tideman, Apr 2026](https://www.revenuecat.com/blog/growth/web-to-app-onboarding-funnel)
- BetterMe: Lazyweb detected about 50 distinct experiments running (July 2026), split between signup/quiz and paywall. That is a two-surface testing pattern typical of quiz-onboarding fitness apps — [Lazyweb, 2026](https://www.lazyweb.com/research/betterme-signup-paywall-experiments) **[vendor data, detection-based]**
- Flo runs a dedicated web user-acquisition team. A "User Acquisition Manager (Web)" role was posted, and app UA roles mention an "8-figure" budget across Meta, TikTok, Snapchat and the stores — [Flo job listing (web UA)](https://jobs.femtechinsider.com/companies/flo-health-2/jobs/74071965-user-acquisition-manager-web); [Flo Greenhouse listing](https://job-boards.greenhouse.io/flohealth/jobs/7602380003). Job postings are a qualitative signal, not performance data.

**Margin advantage: fee rules (EU and US)**
- **EU, effective 1 Oct 2026 (Apple announcement of 18 Aug 2026).** All EU developers move to a single set of terms:
  - App Store IAP: 26% standard, 15% for the Small Business Program and for auto-renewing subscriptions after year one.
  - Alternative in-app PSP: 20%, or 10% in reduced programs.
  - **Link-out to web purchase: 15%, or 10% in reduced programs.**
  - Apps distributed through alternative marketplaces or the web: 5% Core Technology Commission.
  - Sources: [Apple Newsroom, Aug 2026](https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/); [Anadolu Agency, 18 Aug 2026](https://aa.com.tr/en/science-technology/apple-revamps-eu-app-store-fees-to-resolve-regulatory-dispute/4031035)
- **US:**
  - On 30 Apr 2025, Judge Gonzalez Rogers held Apple in contempt. Apple could no longer take a commission on link-out purchases or block steering — [Perkins Coie / search summary](https://legacy.perkinscoie.com/insights/update/european-commission-finds-apples-steering-practices-breach-dma)
  - The Ninth Circuit later upheld the contempt finding. It ruled that a zero-commission remedy went too far, but Apple "should not be able to charge any commission for linked-out purchases until… the district court has approved an appropriate fee" — [Courthouse News](https://courthousenews.com/ninth-circuit-confirms-contempt-finding-against-apple-in-epic-games-battle/); [Digital Policy Alert](https://digitalpolicyalert.org/event/39719-us-court-of-appeals-for-the-ninth-circuit-affirmed-contempt-finding-and-remanded-on-commission-rate-in-epic-games-v-apple)
  - RevenueCat and Paddle launched web checkout for link-outs (June 2025) — [TechCrunch, 2025](https://techcrunch.com/2025/06/04/revenuecat-and-paddle-team-up-to-help-app-developers-profit-from-web-payments)
- **EU DMA:** on 23 Apr 2025 the European Commission found that Apple's anti-steering rules breached DMA Art. 5(4) — [Perkins Coie, 2025](https://legacy.perkinscoie.com/insights/update/european-commission-finds-apples-steering-practices-breach-dma)

**Hard paywall vs freemium (relevant to the in-app funnel)**
- RevenueCat SOSA 2026:
  - Hard paywalls reach a 10.7% median D35 download-to-paid rate (top quartile 20.0%, P90 38.7%). Freemium reaches 2.1% (top quartile 4.5%), so hard paywalls convert about 5× better.
  - **Year-1 retention is about the same**: yearly 27% for hard paywalls vs 28% for freemium, monthly 9% vs 8%.
  - "1/3 of all conversions happen on day zero". More than 60% happen within a week. Hard paywalls show a Day 4–7 spike (25.7%) from 7-day trials expiring.
  - Source: [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps)
- Adapty 2026 (16,000+ apps, $3B+, 2025 data): "Hard paywalls produce 21% higher LTV but soft paywalls outconvert by nearly 50%" — [Adapty State of In-App Subscriptions 2026](https://adapty.io/state-of-in-app-subscriptions-report/). This **conflicts in direction** with RevenueCat's conversion finding. The two likely use different denominators (paywall-view conversion vs download-to-paid), so they should not be mixed.

### Inferences
- For Nacre, a "12-week plan" built on a skin-type, budget and lifestyle quiz fits the profile where quizzes work: personalisation, education and an emotional story. The web quiz can reuse Valère's pre-sell logic (advertorial/quiz pages) almost unchanged. The difference is that the "product page" is a personalised plan plus a paywall instead of a sales letter.
- Suggested sequencing for a pre-launch team:
  - **(a) Launch:** app-store-direct Meta/TikTok app campaigns, with the quiz inside the app before an onboarding paywall. This is simplest, AEM handles attribution, and it ranks the app in the stores.
  - **(b) Within 1–3 months:** add a web quiz → plan reveal → web paywall (Stripe/Paddle via RevenueCat Web or a funnel builder) → download. Run it on Facebook Feed/Reels, where older and higher-paying users are.
  - **(c)** From Oct 2026, Nacre can also use EU link-outs from the app. They cost 10–15% plus processing, which is little better than 15% Small Business Program IAP, so for a small developer the margin gain of in-app link-outs is small. The large margin gain comes from purchases made entirely on the web before install. This is an inference: confirm the treatment of purchases made before install against Apple's EU terms.
- Illustrative net revenue per annual subscriber (assumptions, not sourced data: 20% French VAT, Small Business Program):
  - €39.99 incl. VAT is about €33.33 excl. VAT.
  - Via App Store at 15%: about €28.3 net.
  - Via web at ~6% all-in: about €31.3 net.
  - The gain is about €3 per annual sale, so W2A's main advantage for Nacre is conversion, data and cash flow (annual paid upfront), not fees.
- FunnelFox shows that W2A revenue is mostly no-trial, intro-discount or paid-trial offers, and only 14.3% free trial. If Nacre keeps the 7-day free trial in-app, the web funnel should test a paid trial (e.g. €1 for 7 days) or a first-period discount. Run it against the free trial rather than copying the in-app offer.
- A 3-month plan (8.4% of W2A revenue) could match the "12-week programme" promise. This is a hypothesis to test, not a benchmark.

### Gaps
- No public, audited W2A conversion data specific to France or beauty/skin apps. The FunnelFox figures are mostly US (63.7% of revenue).
- No public numbers for Flo, Simple, Mimo, Bloom, Hers or skin apps. Flo's onboarding is widely described as ~70 screens / ~7 minutes, but no verifiable primary URL was found, so treat it as unverified.
- It is not confirmed whether purchases made on the web before install (no in-app link) are free of any Apple commission under the 1 Oct 2026 EU terms. This is the common reading but needs legal and Apple-terms confirmation.
- The EU 14-day right of withdrawal for digital subscriptions sold on the web (express consent and waiver wording at checkout) was not researched here. It affects refund exposure on web checkout.

---

## 2. Benchmarks: install→trial, trial→paid, by category and region; plan mix, prices, refunds, churn, LTV; hard paywall vs freemium; trial length

### Takeaway
For H&F apps in 2025 data:
- **download→trial**: ~6.9% median (WE all categories 5.0%)
- **trial→paid**: ~37.7% median (WE 29.7%)
- **D35 download→paid**: ~2.9% median (WE 2.0%)

H&F is annual-heavy (68% of subscriptions sold are yearly), with a median yearly price of ~$39.94, almost exactly Nacre's €39.99. 5–9-day trials are the H&F norm (54%) and convert much better than ≤4-day trials (37.4% vs 25.5% median). Year-1 realised LTV per payer is modest: about $35.6 for H&F globally and about $26.6 for Western Europe.

### Cited Findings
**RevenueCat SOSA 2026 (115k+ apps, $16B, mostly 2025 data)** — [RevenueCat](https://www.revenuecat.com/state-of-subscription-apps):
- **Download→trial (D30):**
  - H&F median 6.9%. Business is highest at 9.1% and Gaming 4.4%.
  - Western Europe median 5.0%. North America median 7.1% (top quartile >15.0%).
  - By price tier: high-priced apps 8.9% median, mid 5.4%, low 4.4%.
- **Trial→paid:**
  - H&F median 37.7% (top quartile >51.4%). Travel is highest at 43.5%. Photo & Video is lowest at 22.2%, and Gaming 25.0%.
  - By region: North America 34.2% (top quartile 47.9%), Asia-Pacific 31.9%, **Western Europe 29.7%**, IN/SEA 15.2%.
  - Top 10% reach 60%+ in North America, Asia-Pacific and Western Europe.
- **Trial length:**
  - Median trial→paid by length: 17–32-day trials 42.5% (top quartile 59.4%), 5–9 days 37.4% (top quartile 52.8%), ≤4 days 25.5% (top quartile 38.5%).
  - H&F mostly uses 5–9 days (54.0% of H&F trials).
  - Short trials (≤4 days) are 46.5% of all trials, up 4.4pp year on year, "despite the data".
- **Trial cancellation timing:**
  - Share cancelling on Day 0: 3-day trials 55.4%, 7-day trials 39.8%, 14-day trials 35.7%, 30-day trials 31.1%.
  - Share of cancellations between Day 0 and Day 1: 84% for 3-day trials, 64% for 7-day trials.
- **Day-0 trial starts:** 82.1% of H&F trial starts happen on Day 0. After Day 3, trial starts drop below 5%.
- **D35 download→paid:**
  - By category: H&F 2.9% median (top quartile >6.2%) and Shopping 1.3%.
  - By user region: North America 2.8% (top quartile 6.0%, P90 10.9%), Western Europe 2.0%, IN/SEA 0.7%.
  - By price tier: high-priced 2.8%, mid 2.0%, low 1.4%.
  - By developer HQ: Western Europe 2.0% median.
- **Hard paywall vs freemium:** 10.7% vs 2.1% D35 download→paid, with near-identical year-1 retention (yearly 27% vs 28%).
- **Plan mix (subscriptions sold):**
  - H&F is 68% annual. Gaming is 82% weekly and Productivity is 77% monthly.
  - Western Europe "mirrors North America closely (35% yearly, 41% monthly)". North America is 40% yearly.
- **Paywall design:** 60% of H&F paywalls show 2 plans, the highest of any category. H&F has the lowest share of single-plan paywalls (20%).
- **Prices (global medians):**
  - Weekly $5.99, monthly $10, yearly $34.80 (up from $31.60).
  - North America: monthly $9.99, yearly $39.99. Western Europe yearly $39.44.
  - Western Europe App Store: highest weekly price at $7.03 and highest yearly at $40.12.
  - "Education and Health & Fitness sustain $39.99–$44.99 annual pricing."
- **Intro offers:** the median discount is −50.1%. H&F is among the shallowest at −47%.
- **Renewal rates by geography (medians):**
  - Weekly 1st renewal: Western Europe 42% vs North America 55%.
  - Monthly 1st renewal: Western Europe 55% vs North America 55%.
  - Yearly 1st renewal: Western Europe 28% vs North America 26%.
  - Geographies converge within 5–10% by the 3rd renewal.
  - By category, monthly 1st renewal is 53–61%, but Social & Lifestyle is lowest at 42%.
- **Year-1 retention by plan:** yearly 20–40% median (top quartile 32–59%), monthly 6–14%, weekly 1–2%.
- **Annual-plan cancellations:** Month 1 accounts for 35% of all annual cancellations (23–50% depending on category), with an 11% uptick in Month 12.
- **Refunds:**
  - By category, most cluster at 3–4% median. Productivity is highest at 4.7% and Travel lowest at 2.5%. Outlier apps reach 9–18%.
  - By region: North America 3.4% median, IN/SEA 7.7%. The P25–P75 range is 2–8% across geographies.
  - Higher prices correlate with higher refunds (low-priced median 2.7%).
- **Involuntary churn:** about 31% of Google Play cancellations are involuntary billing failures, versus 14% on the App Store.
- **Revenue per install:**
  - D14: H&F $0.48 median versus $0.23 across all categories. Western Europe $0.25, North America $0.38.
  - D60: H&F $0.66.
- **Realised LTV per payer:**
  - H&F: $24.23 after 1 month and $35.64 after 1 year.
  - Western Europe: $17.89 after 1 month and $26.64 after 1 year. The global 1-year median is $23 and North America is $32.
  - Yearly-plan RLTV by price tier: high-priced $62.19 median, mid $28.75, low $10.69.

**RevenueCat SOSA 2025 (earlier edition)**:
- H&F trial→paid median 39.9%, top 10% 68.3%.
- Trials of 17–32 days convert at a 45.7% median versus 26.8% for ≤4 days.
- "Nearly 30% of annual subscriptions are canceled in the first month."
- H&F D60 RPI median $0.63.
- Source: [Athletech News, 2025](https://athletechnews.com/fitness-apps-monetizable-winner-take-all-or-most/)
- Conflict note: Athletech describes the dataset as about 30,000 apps and $6.7B, while other write-ups of SOSA 2025 cite 75,000 apps. The edition may be mislabelled.
- 82% of trial starts happen on install day (SOSA 2025, 75,000 apps) — [Cloud/SaaStr summary, 2025](https://cloud.substack.com/p/85-of-business-app-trials-start-on)

**Adapty**:
- **2026 report** (16,000+ apps, $3B+, 2025 data, mostly the App Store):
  - H&F is "the only category where annual plans dominate and continue to grow share".
  - Weekly plans generate 55.6% of all app revenue.
  - "7 in 10 apps offer trials".
  - The median annual price is 3× the monthly price globally.
  - European subscription prices rose 18% year on year. Europe's price index is 1.2× the UK baseline (UK, FR, DE, IT, ES).
  - H&F install LTV is $1.20, the highest category. Median 1-year LTV across all plans is $68.90.
  - Trials raise 1-year retention by 43% on weekly plans. In H&F, "users either buy on Day 0 or on Days 4–7".
  - Global refund baseline is 8.3%. This is a different definition from RevenueCat's.
  - Source: [Adapty 2026](https://adapty.io/state-of-in-app-subscriptions-report/)
- **2025 report** ($1.9B revenue, 11,000+ apps):
  - Average prices in Europe: weekly $8.3 (+12.2% YoY), monthly $13.3, annual $42.
  - Europe refund rate about 2.3%, lower than the US and LATAM.
  - H&F annual-plan 12-month LTV is $46.1. Lifestyle averages $18 for premium monthly plans.
  - Europe accounts for 24.8% of global in-app subscription revenue.
  - Source: [Adapty 2025 summary](https://adapty.io/blog/state-of-in-app-subscriptions-2025-in-10-minutes/)

**Competitor price points (acne/skin apps, App Store listings, 2025–2026)**:
- SkinTheory: $4.99/month or $39.99/year — [App Store](https://apps.apple.com/us/app/-/id1490049787)
- Acnetic: $4.99/week, $9.99/month, $49.99/year — [App Store](https://apps.apple.com/app/id6747617559)
- Verified-revenue indie acne apps on TrustMRR (as of 1 Oct 2026):
  - Klear: MRR $436, 75 active subscriptions, €9.99/month or €29.99/year with a 3-day trial, TikTok as channel — [TrustMRR](https://trustmrr.com/startup/klear)
  - Noma: MRR $262, 65 subscriptions, launched July 2025, ASO + TikTok — [TrustMRR](https://trustmrr.com/startup/noma)

### Inferences
- Nacre's €39.99/year matches the H&F yearly median (~$39.94) and the Western Europe yearly median ($39.44). Its €7.99/month is below the H&F median of $9.99. The annual-to-monthly ratio is 5.0× (39.99/7.99), above the ~3× global median Adapty reports, so annual is strongly anchored as the "deal". That is consistent with H&F's 68% annual mix.
- The 7-day trial is well supported. H&F mostly uses 5–9-day trials, which convert at 37.4% versus 25.5% for ≤4 days. Only about 40% of 7-day-trial cancellations happen on Day 0, versus 55% for 3-day trials.
- Plan for Western Europe being roughly 20–30% weaker than North America on trial→paid (29.7% vs 34.2%) and D35 conversion (2.0% vs 2.8%). Planning baseline: ~5–7% download→trial, ~30–38% trial→paid, ~2–3% D35 download→paid. Top quartile is ~6% D35.
- Unit-economics warning (illustrative arithmetic, not a sourced benchmark). Assume a blended CPI of €2–3.5 (see Q3; no reliable France H&F figure exists).
  - At median D35 download→paid (2–2.9%), the cost per payer is about €70–175.
  - That is far above year-1 RLTV per payer (WE ~$26.6; H&F ~$35.6).
  - Paying back within year 1 needs top-quartile conversion (≥6%), a hard paywall (median 10.7%) and/or W2A with annual paid upfront.
  - This is the main way a subscription app differs from Valère's infoproduct model: payback happens over months, not on the first order.
- RevenueCat's H&F bucket includes Medical. If Nacre is listed under Lifestyle, benchmarks may be weaker: Social & Lifestyle has the lowest monthly 1st renewal (42%) and 43.6% of those apps run no trial.

### Gaps
- No France-only conversion, pricing or refund figures were found. All European data is regional (Western Europe or Europe).
- No beauty/skincare-specific category benchmarks. Beauty apps fall into Lifestyle or H&F.
- Adapty's and RevenueCat's refund definitions differ (8.3% vs 3–4% median), so they cannot be reconciled from public pages.
- RevenueCat's Western Europe median monthly price was not confirmed in the page text, so it is omitted.

---

## 3. Paid acquisition costs in France: CPM, CPI, cost per trial and per subscriber on Meta and TikTok; Apple Search Ads

### Takeaway
Credible, category-specific CPI, cost-per-trial or cost-per-subscriber figures for France are not publicly available from AppsFlyer, Liftoff or Business of Apps; AppsFlyer's benchmark tool returned no data. The usable anchors are:
- Apple Ads France: CPT ~$0.92, conversion rate ~57% on search results
- Meta CPM in France: roughly $7–13 (vendor estimates, lower than the UK and Germany)
- TikTok CPM in France: ~€3–8 (vendor estimate)
- ATT opt-in in France: just under 51%
- Blended cost-per-trial rules of thumb: $20–40 is "healthy"

Nacre should treat its first €3–5k of spend as the real benchmark.

### Cited Findings
- **Apple Ads (AppTweak; Jan–Dec 2025; ~2,800 US advertisers; medians)** — [AppTweak, 2026](https://apptweak.com/en/aso-blog/apple-ads-benchmarks):
  - **[US]** H&F: CPT $1.68, **CPI $3.77**, CR 50.3%, TTR 7.5%. H&F, Travel and Finance "convert least".
  - **[US]** Lifestyle: CPT $1.18, CPI $2.62, CR 54.8%, TTR 7.4%.
  - **France (all categories):**
    - Search results placement: CPT $0.92, CPM $71.20, CR 57%, TTR 7.4%.
    - Search tab: CPM $6.45, CR 16%.
    - Today tab: CPM $3.06, CR 9%.
    - Product pages: CPM $16.97, CR 16%.
    - The page also cites "France ($1.78)" as a moderate European acquisition cost. The metric (likely CPI/CPA) is ambiguous in the extract.
- **ATT opt-in:**
  - AppsFlyer (Apr 2025): France "just under 51%", Germany 47%, global 50%. iOS non-organic installs grew 29% year on year versus 21% on Android — [AppsFlyer newsroom, 2025](https://www.appsflyer.com/company/newsroom/pr/post-att-growth-2/)
  - Adjust puts the industry average at 35% (Q2 2025) — [Adjust, 2025](https://www.adjust.com/blog/att-opt-in-rates-2025)
  - The two providers differ by methodology.
- **Meta CPM France (vendor estimates, not audited):**
  - Adamigo 2026: France $8.05 average (UK $10.31, DE $10.05) — [Adamigo](https://www.adamigo.ai/blog/meta-ads-cpm-cpc-benchmarks-by-country-2026)
  - Stackmatix Q1 2026: France Facebook $6.80–11.20, Instagram $7.90–12.80 — [Stackmatix](https://stackmatix.com/blog/platform-ad-cost-benchmarks-country-industry-2026)
  - Adligator 2026: France Facebook $7–10, Instagram $9–13 — [Adligator](https://adligator.com/blog/meta-ads-cpm-by-country-benchmarks)
  - Influee: Instagram in France costs €10–20 CPM and €0.60–2.50 CPC. It recommends a test budget of €10–20/day for 1–2 weeks — [Influee FR, 2026](https://influee.co/fr/blog/how-much-do-instagram-ads-cost)
- **TikTok CPM France (vendor estimate):**
  - €3–8 CPM, "40–60% cheaper than Meta (€12–20)".
  - Global trend in 2025: CPM +16%, CTR +13.74%, CVR −6.2%.
  - Official minimum budget: €50/day per campaign. Meaningful tests start at €300–500 over two weeks.
  - Source: [Influee FR, 2026](https://influee.co/fr/blog/tiktok-ads-benchmarks)
- **CPI ranges (low-confidence aggregators):**
  - H&F: $2.00–5.50 on iOS and $1.00–3.00 on Android. Western Europe average across categories: $3.40 iOS and $1.85 Android (2026) — [The Social Outline](https://thesocialoutline.com/blog/cpi-benchmarks-health-fitness-apps)
  - By channel: Facebook $2.00–5.50, TikTok $1.75–4.00, Google $1.50–4.50 (Udonis, cited by Airbridge) — [Airbridge, 2026](https://airbridge.io/en/blog/cost-per-trial-cost-per-subscription-subscription-app-ua-metrics)
- **Cost per trial / per subscriber:**
  - Blended cost per trial of $20–40 is "healthy", and below $12 is "incredibly aggressive" (Shamanth Rao, cited by Airbridge).
  - Airbridge worked example (not a benchmark): Meta CPI $3.50 × 15% install→trial × 39.9% trial→paid gives about $58 per subscription.
  - Source: [Airbridge, 2026](https://airbridge.io/en/blog/cost-per-trial-cost-per-subscription-subscription-app-ua-metrics)
- Marcus Burke in SOSA 2026: "Cost per trial is a useful starting point and a terrible finishing point". Blended CPT averages over geo, trial length, price and audience, and geo alone moves trial→paid from 19.5% (MEA) to 34.2% (North America) — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps)
- **Placement quality:** Instagram Reels traffic is younger and lower-intent, with a cheaper CPA but weaker trial→paid. Facebook Reels reaches "an older audience yet ha[s] low CPMs" — [RevenueCat/Marcus Burke, 2025](https://www.revenuecat.com/blog/growth/meta-ads-in-2025-tips-for-apps)
- **Data to discard:** Superads' "cost per app install" pages for France show inconsistent numbers, and the page fetch showed no country granularity, so they are excluded as unreliable — [Superads](https://www.superads.ai/facebook-ads-costs/cost-per-app-install/wellness-holistic-health/france)
- **Payback rules of thumb (vendor, not audited):**
  - Subscription apps typically see 0.3–0.5× D7 ROAS and 1.0–2.0× D30 ROAS. Healthy payback is 6–12 months (best case 5–7) with LTV:CAC ≥3:1.
  - Sources: [Segwise, 2026](https://segwise.ai/blog/roas-benchmarks-industry-standards); [Admiral Media](https://admiral.media/cac-payback-period-mobile-apps/)

### Inferences
- Women aged 18–34 are a high-competition audience on Instagram, and Instagram Reels traffic converts less well from trial to paid. Nacre should judge placements on cost per *paid* subscriber, using age brackets collected in onboarding, not on cost per trial.
- A planning grid for France, to be validated with the first test budget:

  | Metric | Planning range |
  |---|---|
  | Meta CPM | ~€7–15 |
  | TikTok CPM | ~€3–8 |
  | CPI (iOS) | ~€2–4 |
  | CPI (Android) | ~€1–2.5 |
  | Cost per trial | ~€20–45 at median conversion |
  | Cost per paid subscriber | ~€60–150 at Western Europe medians |

- The cost per paid subscriber range is above year-1 LTV (see Q2), so offer, funnel and conversion work matters more than buying cheaper media.
- Apple Ads in France looks inexpensive: CPT about $0.92 and a 57% conversion rate on search results. That suits branded and category keywords ("routine acné", "acné adulte") once the app exists.

### Gaps
- No public France-specific Meta/TikTok CPI, cost-per-trial or cost-per-subscriber figures for health, beauty or women's-health apps from AppsFlyer, Liftoff, Adjust or Business of Apps (2024–2026). AppsFlyer's benchmark page rendered no data, and Liftoff's 2025 reports found were gaming-only.
- No public data on CPMs for women 18–34 specifically in France.
- No Apple Ads benchmarks for France by category (Health/Beauty).

---

## 4. Creative formats that win for subscription apps on Meta and TikTok (2025–2026)

### Takeaway
Volume and diversity of concepts win; no single "best format" is supported by audited data. Only ~5–8% of ads become winners (Motion, 550k ads). Formats with practitioner evidence for subscription apps in 2025–2026:
- creator/UGC (ideally run as Partnership or Spark ads)
- text-wall and "native" statics or videos
- infographics
- article-style ads
- faceless AI B-roll with voice-over
- 9:16 video with sound

Classic stranger talking-head UGC is showing fatigue. AI UGC is close to human on hook rate (~26–36% vs ~28–38%) and costs 90%+ less, but in France it carries legal labelling risk.

### Cited Findings
- **Motion "2026 Creative Benchmarks"** (550,000 ads, 6,000 advertisers, $1.3B Meta spend, Sep 2025–Jan 2026):
  - "Only 5–8% of ads become real winners, and about half never get meaningful spend."
  - The example of a personal-care brand spending $100k/month produced about 50 ads/month.
  - Search summaries of the report put the hit rate at about 3.8% for accounts under $10k/month and about 8% for $1M+/month. That split was not shown on the landing page.
  - Source: [Motion, 2026](https://motionapp.com/events/2026-creative-strategy-bootcamp/homebase/2026-creative-benchmarks)
- **Hook rate** (3-second plays ÷ impressions):
  - Average 25.44% across 88,329 sales-objective Meta video ads in H1 2026 (14 industries, $122M spend), ranging from 21.32% to 28.79% by industry.
  - Data source is Billo, a UGC producer. Its own caveat: "No third party audited it."
  - Source: [NovoAds summarising Billo, 2026](https://novoads.ai/blog/video-ad-benchmarks-2026)
  - Practitioner rules of thumb: >30% is a strong hook, 40%+ is "elite" — [Influee](https://influee.co/gb/blog/creative-benchmarks-for-your-ugc-ads) **[vendor]**
- **AI UGC vs human UGC** (Segwise; $115k test across 5 AI-UGC platforms; single DTC client in beauty/skincare/supplements; published 23 Mar 2026) **[vendor data]**:
  - Hook rate: human direct-to-camera UGC 28–38%, high-quality AI avatars 26–36%, robotic early-generation AI 14–20%.
  - Consumer quality approval: AI 68% vs human 81%.
  - Cost per video: AI $5–20 vs human $150–400. That allowed "8x more creative testing in the same timeframe".
  - Best platform: 2.42× ROAS at a $70 CPA.
  - Source: [Segwise, 2026](https://segwise.ai/blog/115k-ai-ugc-platform-test-findings)
- **Meta Partnership Ads (creator-handle ads)**, Agentio analysis of $130M spend, 65,000 Partnership Ads, 137 brands:
  - Versus the same creative run from the brand account: +19% CTR, +10% conversion rate, −5% CPA, despite +19% CPM.
  - By placement: Search placements +45% CTR, +143% CVR, −63% CPA. **Stories placements: +25% CPA.**
  - Sources: [Net Influencer](https://www.netinfluencer.com/meta-partnership-ads-outperform-licensed-ugc-across-130m-usd-in-ad-spend-report-finds/); [MarTech Vibe](https://martechvibe.com/article/creator-ads-deliver-19-higher-ctr-on-meta-partnership-ads)
  - Agentio is a creator-ads vendor **[vendor data]**.
- **Influee case study:** a brand spending €100k/month on Meta lowered CPA by 20% with Partnership Ads — [Influee case study](https://influee.co/it/content-hub/babylovegrow-case-study) **[vendor]**
- **TikTok Spark Ads** (boosting creator/organic posts):
  - TikTok-reported figures: +134% completion rate and +157% 6-second view-through rate versus standard in-feed ads.
  - Caveat from the same source: TikTok "has not published a Spark-versus-standard comparison since 2020–2022", and the 2026 figures "trace back to the same three studies".
  - Source: [Enrich Labs, 2026](https://www.enrichlabs.ai/blog/tiktok-spark-ads-complete-guide-2026)
  - Vendor figure: creator content can lower effective CPM by up to ~20% (Spark $3.54 vs $4.73 average) — [Influee FR](https://influee.co/fr/blog/tiktok-cpm)
- **Formats working for apps** (Marcus Burke, Apr 2025):
  - **Text-wall ads**, static or video, telling a complete story in text ("what users post organically").
  - **Infographics**, especially for habit apps showing results. They "pair well with web-to-app quiz funnels".
  - **Faceless AI content**: B-roll plus AI voice-over.
  - **Article-style ads** that look like news articles native to the Facebook Feed.
  - Tools named: Midjourney/Flux (statics), Runway/Kling (animation), Veo/Luma (video), Arcads/Poolday (AI talking-head UGC).
  - Source: [RevenueCat, 2025](https://www.revenuecat.com/blog/growth/meta-ads-in-2025-tips-for-apps)
- **Beauty/skincare on Meta:** UGC beats studio creative by 35–55% on CTR in cold traffic across every sub-vertical except luxury fragrance. UGC, testimonials, tutorials, founder stories and comparison ads beat polished brand spots — [Webtonic, 2026](https://www.webtonic.io/blog/beauty-skincare-facebook-ads-statistics) **[agency data]**
- **Format specs:**
  - Meta says 9:16 video with sound delivers about 34% lower cost per result than image ads (Meta statistic as cited by secondary sources) — [Metricool, 2026](https://metricool.com/facebook-reels-ads-guide/); [Stackmatix](https://www.stackmatix.com/blog/meta-video-ads)
  - TikTok: one in four top-performing videos runs 21–34 seconds, with about a 1.6× lift in impressions (TikTok data cited secondarily; the original TikTok source was not retrieved).
  - TikTok creatives often burn out within 1–2 weeks, while Meta returns are steadier (practitioner observation in search results; low confidence).
- **Valère's 80% video / 20% static split:** no 2025–2026 source found that sets a video/static ratio for subscription apps. Motion's landing page did not disclose format splits.

### Inferences
- Mapping Valère's method to Nacre:
  - Keep "one benefit = one angle" and 3 angles at launch.
  - Make each of the 9–12 launch creatives a *distinct concept* (format, persona, setting, hook type), not 10 hooks on the same body. Andromeda groups near-duplicates (see Q5).
  - Hook × body × closing permutations are better used to iterate inside a winning concept after it proves itself.
- Concept candidates with practitioner evidence for apps:
  - creator/UGC selfie-camera testimonial about adult acne as a relatable experience, run as a **Partnership Ad**;
  - text-wall "my 12-week journey" statics or Reels;
  - app screen-recording of the personalised routine and budget picker (product demo);
  - infographic ("routine matin/soir à €X/mois");
  - founder talking head ("why we built Nacre");
  - "POV/relatable" text-on-screen;
  - slideshow/carousel of the routine steps.
- Partnership Ads beat brand-account ads on CTR, CVR and CPA, but Stories placements were worse (+25% CPA). Check placement-level results.
- AI UGC is a cheap way to find winning concepts. Given French labelling law (Q5) and lower consumer approval (68% vs 81%), it makes sense to re-shoot winners with real creators and to label AI content where the law requires it.

### Gaps
- No 2025–2026 audited study comparing UGC vs founder vs screen-recording vs slideshow for subscription apps specifically, and none for France.
- No reliable 4:5 vs 9:16 comparison data for app campaigns (a "4:5 beats 1:1 by up to 15%" claim surfaced without a traceable source and is excluded).
- TikTok Creative Center top-ads data for French beauty/health apps was not accessible within this research. Browser tools were excluded and search did not surface it.
- Phiture/AppAgent/Foreplay 2025–2026 quantitative creative reports were not found.

---

## 5. Meta Andromeda / Advantage+ app campaigns, TikTok Smart+, SKAN/AEM, and policy constraints

### Takeaway
Andromeda (Meta's ad-retrieval engine, disclosed in Dec 2024) uses the creative itself to find the audience. That favours broad targeting plus many *conceptually distinct* creatives; practitioners suggest about 8–12 distinct concepts per campaign, or 15–50 new creatives per week at scale. On iOS, most subscription apps optimise for **trial** events measured through Meta AEM (8 prioritised events, near real time). SKAN gives slower, delayed postbacks; use it for weekly audits. Two policy risks apply to an acne app: Meta's 2025 health and wellness restrictions on lower-funnel events, and acne-specific ad-copy rules.

### Cited Findings
- **Andromeda:**
  - Meta engineering blog (2 Dec 2024): Andromeda is the retrieval stage that narrows millions of candidate ads to the few thousand that enter each auction.
  - Meta reports +8% ad quality on selected segments, up to 10,000× more model complexity, and higher serving throughput.
  - Advertisers enabling Advantage+ creative saw about 22% higher ROAS (Meta claim as relayed by search results).
  - Sources: [Meta Engineering, 2024](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/); [MediaPost](https://www.mediapost.com/publications/article/401591)
- **Practitioner guidance on volume and diversity (not Meta official):**
  - App install campaigns need 15–50 creatives per week. Meta recommends 10+ creative variations per campaign — [Web2Wave, 2025](https://web2wave.com/post/q5-2025-ready-web2app-funnels-ua-trends)
  - Advantage+ campaigns: 20–50 creatives, up to 150 testable — [search summary of agency sources, 2025](https://funnel.io/blog/meta-advantage-plus)
  - Advantage+ App Campaign updates: more flexible asset combination, a 7-day click attribution option, split testing, regional insights (same source).
  - **Entity ID**: Meta reportedly groups highly similar ads under one "Entity ID", described as one "ticket" to the retrieval auction. A threshold of "~40% visual similarity" is claimed. Recommended: 8–12 conceptually distinct concepts per campaign, not "30 variations of two ideas".
    - These are practitioner claims, **not confirmed by Meta** — [Brandsearch](https://brandsearch.co/blog/meta-creative-similarity-score-competitor-research); [Nikhil.pro](https://nikhil.pro/meta-ads-creative-similarity-explained/)
- **Optimisation event and budget-stage priorities** (Marcus Burke, Apr 2025):
  - Subscription apps should optimise for trial, not subscription, because of AEM's 7-day window.
  - At $0–20k/month the priority is technical setup. Validate Meta attribution against an in-app "how did you hear about us" survey, targeting a >50% match.
  - At $20–100k/month, run "big swing" tests of "wildly different content types".
  - In some audits "only 10% of trials were being attributed to Meta correctly".
  - Collect age in onboarding using Meta's age brackets so trial→paid can be judged by bracket.
  - Most subscription apps had switched to AEM by 2025: no privacy thresholds, real-time creative-level reporting, but a "black box".
  - Source: [RevenueCat, 2025](https://www.revenuecat.com/blog/growth/meta-ads-in-2025-tips-for-apps)
- **AEM vs SKAN (June 2025):**
  - AEM: up to 8 prioritised events per user, modelled conversions within hours, Meta properties only, default windows 1-day click / 7-day click / 28-day view.
  - SKAN 4: three postback windows (0–2 days, 3–7 days, 8–35 days) with a random 24–48h delay. It under-reports by 5–15% against App Store Connect.
  - Recommendation: use AEM for daily pacing and SKAN for weekly audits once installs pass 200 per week.
  - Source: [Segwise, 2025](https://segwise.ai/blog/meta-aem-vs-skan-2025-ios-attribution)
- **TikTok Smart+ (official case studies):**
  - Alinea (subscription app): +73% subscriptions and −42% CPA versus manual campaigns — [TikTok for Business](https://ads.tiktok.com/business/en-US/inspiration/alinea-smart-plus-app-campaigns)
  - Taimi: −20.9% CPI — [TikTok for Business](https://ads.tiktok.com/business/fr/inspiration/taimi-automation-tiktok-success-story)
  - Whatwapp: −14% CPI and +16% D1 retention over a 12-day test — [TikTok for Business](https://ads.tiktok.com/business/id/inspiration/whatwapp-scopa)
  - These are self-selected platform case studies.
- **Meta health and wellness data restrictions (2025):**
  - From around Jan/Feb 2025, accounts or domains Meta classifies as health and wellness can lose optimisation and audiences on lower-funnel events such as Purchase and Add to Cart. Upper-funnel events (PageView, ViewContent) remain available.
  - Fitness, lifestyle and mental-health apps are named as possibly affected.
  - Meta has also disabled custom conversions and audiences with health-related names (e.g. "acne_interest_list").
  - Sources: [Click Consult, 2025](https://www.click.co.uk/insights/metas-new-advertising-restrictions-impacts-health-and-wellness-brands/); [Angler AI, 2025](https://getangler.ai/blog/what-metas-2025-data-restrictions-mean-for-health-and-wellness-brands); [Accelerated Digital Media, 2026](https://www.accelerateddigitalmedia.com/insights/guide-to-social-media-health-ad-restrictions-2026/)
  - Geographic scope (US-only vs EU) and whether app SDK events are covered were **not confirmed** by these sources.
- **Ad policy for an acne app:**
  - Meta's Personal Attributes policy forbids asserting knowledge of a user's medical condition: avoid "Your acne…" or "Conquer your acne".
  - No "cure/heal/eliminate" claims. Cosmetic and health products must target 18+.
  - Meta prohibits ads that "imply or attempt to generate negative self-perception".
  - Sources: [Accelerated Digital Media, 2026](https://www.accelerateddigitalmedia.com/insights/guide-to-social-media-health-ad-restrictions-2026/); [Meta Transparency Center – Health & Wellness](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness) (page not machine-readable here)
  - A secondary source reports that on 22 Jul 2026 Meta switched health and wellness review to claim-by-claim. Under that change, before/after imagery for cosmetic products is "judged by its claims" rather than auto-rejected. Guaranteed outcomes, outcome timelines and imagery "designed to make the viewer feel bad about their body" stay prohibited — [Adligator, 2026](https://adligator.com/blog/meta-health-wellness-ad-policy-update-2026). The source itself says it is "interpretation, not the rulebook".
  - TikTok prohibits claims to "treat, cure, heal, or prevent any medical condition" in 14 named markets, and asks advertisers not to collect healthcare information through tracking — [Accelerated Digital Media, 2026](https://www.accelerateddigitalmedia.com/insights/guide-to-social-media-health-ad-restrictions-2026/)
- **France — Loi influenceurs n°2023-451 (9 Jun 2023):**
  - Commercial influence content must be labelled "Publicité" or "Collaboration commerciale".
  - Content altered to change the face or silhouette must carry "Image retouchée", and AI-generated content must carry "Image virtuelle". The label must be clear and visible for the whole duration.
  - Penalties: up to 2 years in prison and €300,000 (€1.5M for legal entities).
  - Sources: [Bird & Bird summary](https://www.twobirds.com/-/media/new-website-content/insights/pdfs/resume-de-la-loi-influenceurs-par-bird.pdf); [Swello](https://swello.com/fr/blog/loi-influenceur/)
- **Excluded tactic, noted only as a risk:** cloaking or disguising before/after or health claims to bypass review is policy evasion. On top of the policy breach, the 2025 restrictions show that Meta classifies at the account and domain level, so evasion puts the whole ad account and domain at risk.

### Inferences
- Nacre's setup: one broad Advantage+ app campaign per OS, aged 18–35 women (or Advantage+ audience with age floor 18). Start with 9–12 distinct concepts across 3 angles and add about 5–10 new concepts per week once spend allows. Optimise for trial start (AEM) and send RevenueCat trial and conversion events.
- Name events and audiences neutrally (e.g. "plan_started", not "acne_trial"). Write copy in the first person ("Mon acné adulte…") or as a general statement ("L'acné adulte touche…"), not "Ton acné".
- Before/after selfie content is central to Nacre's "weekly selfie" feature. Even under the reported 2026 claims-based review, avoid guaranteed outcomes and timelines (e.g. "peau nette en 12 semaines"). That matches Nacre's "no guaranteed results" positioning.
- W2A depends on Meta optimising for a web Purchase or trial event. If Nacre's domain is classified as health and wellness, that may be restricted, which favours app campaigns (AEM) at launch. Test whether the web domain is restricted before investing in a web funnel. This is an inference; scope is unconfirmed.
- AI-UGC or AI-avatar ads in France should carry "Image virtuelle" when they fall under commercial influence. Creator content must carry "Publicité/Collaboration commerciale", and filtered skin must carry "Image retouchée". Filtered skin in an acne ad would also be misleading.

### Gaps
- Meta's official minimum or recommended creative counts for Advantage+ app campaigns (2025–2026) were not retrieved from Meta's own documentation. Figures above come from practitioners.
- Whether the 2025 health and wellness event restrictions apply in France/EU, and to app SDK/AEM events, is not confirmed.
- The EU AI Act transparency duties for AI-generated people (from Aug 2026) and EU consumer-law rules on "limited time" claims were not researched here.
- Whether France is among TikTok's 14 "no medicinal claims" markets was not confirmed.

---

## 6. Pre-launch: waitlist growth tactics and waitlist→install conversion

### Takeaway
Published waitlist benchmarks are thin and mostly vendor glossaries. Pre-launch pages typically convert 20–40% of visitors to sign-ups (DTC 10–15%). Lists that go cold convert only 1–3% at launch, and subscribers cool within about 14 days without contact. Store pre-orders and pre-registration count toward launch-day volume. Truthful "founding member" pricing is the reward practitioners favour over generic discounts.

### Cited Findings
- **Pre-launch sign-up rates:**
  - Pre-launch pages often convert 20–40% of visitors, with cold broad traffic converting lower.
  - By product type: SaaS with urgent pain >30%, "DTC brands or non-essential products… 10–15%", AI/PLG products sometimes 50%+.
  - Source: [LaunchList glossary](https://getlaunchlist.com/glossary/waitlist-conversion-rate) **[vendor]**
- **Conversion at launch:** five patterns predict below 2% conversion on launch day, including a single confirmation email followed by silence. Subscribers go cold within 14 days, and those who opened 0–1 emails after the welcome converted at 1–3% — [LaunchList 2026 playbook](https://blog.getlaunchlist.com/blog/convert-waitlist-to-paying-customers) **[vendor]**
- **Referral waitlists:**
  - Mechanics: a personal link per sign-up, a live queue position, a leaderboard and fraud checks.
  - Historic examples: Dropbox grew from 100K to 4M users in 15 months, and Robinhood built about 1M pre-launch sign-ups (pre-2024).
  - "Founding member" pricing and product-value rewards beat discount codes ("'10% off' means nothing").
  - Source: [LaunchList referral guide, 2026](https://blog.getlaunchlist.com/blog/waitlist-referral-program-guide) **[vendor opinion]**
- **Store pre-orders and pre-registration:**
  - App Store pre-orders count toward product-page conversion on the day the pre-order is made, and the later download is not double-counted — [Apple App Store Connect Help](https://developer.apple.com/help/app-store-connect/reference/reporting/performance-metrics/)
  - Pre-registration→install is quoted as 50–80% on Google Play and 60–90% on Apple — [MWM glossary](https://mwm.ai/glossary/preregistration) **[low-confidence vendor glossary]**
- **Store page conversion:** H1 2024 average product-page conversion was about 25% on the US App Store and 27.3% on Google Play, varying widely by category — [Adapty](https://adapty.io/blog/app-store-conversion-rate/)
- **Indie acne apps:** small apps relying on TikTok/ASO reached only $262–436 MRR within months of launch — [TrustMRR Klear](https://trustmrr.com/startup/klear); [TrustMRR Noma](https://trustmrr.com/startup/noma). That suggests organic launch momentum alone is weak in this niche.

### Inferences
- Use the waitlist (nacre-iota.vercel.app) to:
  - (a) send a nurture email at least every 2 weeks: skin tips and behind-the-scenes, to avoid the 14-day cool-off;
  - (b) move sign-ups to an **App Store pre-order and Google Play pre-registration** about 2–4 weeks before launch, so installs concentrate on launch day;
  - (c) offer a **truthful founding-member price**, e.g. first-year annual at a stated discount, for a stated window or for waitlist members only, as the referral reward;
  - (d) reuse the waitlist quiz answers (skin type, budget) to personalise the launch email and in-app onboarding.
- A truthful scarcity frame is "founding price reserved for waitlist members until [date]", which is verifiable. Avoid fake countdowns or "only X spots" claims that are not real.
- Plan conversion conservatively: around 10–30% of waitlist emails installing at launch if the list is nurtured, and low single digits if it is cold. These figures are derived from the vendor ranges above, not a benchmark.

### Gaps
- No audited waitlist→install or waitlist→paid benchmarks for consumer subscription apps (2024–2026), and none for France.
- No 2024–2026 case data on founding-member pricing performance for apps.
- The Google Play pre-registration official documentation (rewards, auto-install behaviour) was not retrieved in detail.

---

## 7. Onboarding and paywall best practices that raise trial→paid for habit apps

### Takeaway
The first session decides almost everything: 82% of H&F trials start on Day 0, and most trial cancellations happen in the first 24 hours. Evidence-backed levers:
- a quiz/onboarding that builds commitment before the price
- a transparent trial timeline with a reminder before charging
- a 5–9-day trial rather than ≤4 days
- 2-plan paywalls with annual anchored (the H&F norm)
- moderate intro discounts (~−47 to −50% median)
- real-person and outcome framing rather than feature lists
- payment-failure recovery

### Cited Findings
- **Day-0 dominance** (RevenueCat SOSA 2026): 82.1% of H&F trial starts happen on Day 0. 55.4% of 3-day-trial cancellations happen on Day 0, and 84% of 3-day / 64% of 7-day trial cancellations happen between Day 0 and Day 1 — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps)
- **Transparency / trial timeline** (Duolingo, Anmol Tiwari, in SOSA 2026):
  - "Show users a timeline of exactly what happens during their trial, when they'll be charged, and how refunds work". Removing uncertainty "drives more conversions than trying to sell harder".
  - Letting users pick the day of their trial-expiry reminder (added friction) boosted conversions.
  - Cutting the trial from 14 to 7 days doubled experimentation velocity.
  - Source: [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps)
- **Blinkist "honest paywall"** (older data, around 2018–2019): a timeline paywall with a reminder before the trial ends gave +23% trial starts and −4% trial cancellations — [UX Collective](https://uxdesign.cc/how-blinkist-increases-trial-opt-in-with-push-notifications-64ef7a38c55a)
- **Trial length:** 5–9-day trials convert at a 37.4% median versus 25.5% for ≤4 days, and H&F mostly uses 5–9 days — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps)
- **Trial value in H&F (Adapty 2026):**
  - Trials raise first renewal by "up to 60%" depending on plan type, and 1-year retention by 43% on weekly plans.
  - H&F users buy "on Day 0 or on Days 4–7".
  - Onboarding paywalls with trials convert at "1.78% on average".
  - Source: [Adapty 2026](https://adapty.io/state-of-in-app-subscriptions-report/)
- **Paywall structure:** 60% of H&F paywalls show 2 plans. The median intro-offer discount is −50.1%, and H&F is shallowest at −47% — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps)
- **Quiz and plan-reveal mechanics:**
  - Progress bars, "building your plan" loading screens, social proof mid-funnel, a profile/plan summary before the paywall, discount timers, money-back guarantees, trust badges and per-day price framing — [FunnelFox, 2026](https://blog.funnelfox.com/web2app-funnel-patterns-2026/)
  - Explain why sensitive questions are asked, reassure afterwards, show results before asking for email, build commitment before the price, teach the method — [RevenueCat on Noom, 2026](https://www.revenuecat.com/blog/growth/web-to-app-onboarding-funnel)
- **Adapty case, Prosto (H&F):** about +30% MRR from paywall A/B testing. Changes:
  - plans moved from annual $30/monthly $3 to bi-annual plus monthly around $15;
  - a photo of the founder replaced artwork;
  - copy moved from features to "impressions and possible outcomes".
  - Source: [Adapty case study](https://adapty.io/case-studies/prosto/) (date not stated)
- **Post-paywall leakage:** web payments see 30–50% failed payment initiations, and retries recover about half (15–20% revenue uplift). On Google Play, about 31% of cancellations are involuntary billing failures, versus 14% on the App Store — [FunnelFox 2026](https://funnelfox.com/state-of-web2app-2026); [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps)
- **Checking test wins:** paywall "wins" can turn net-negative once refunds, cancellations and chargebacks are counted (Sara Grana, Yousician, in SOSA 2026) — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps)

### Inferences
- A Nacre onboarding blueprint, in-app or web, of roughly 15–30 screens. That is shorter than Noom/Fastic, since a skincare routine needs less data:
  1. Goal and acne pattern (jawline, cycle-related), with an explanation of *why* each question is asked.
  2. Skin type, sensitivities, current routine and budget per month.
  3. Lifestyle (sleep, stress) and optional cycle tracking, with reassurance after sensitive questions.
  4. Micro-education ("adult acne is often hormonal or cycle-linked…") without medical claims.
  5. "Building your plan" screen, then the **personalised 12-week plan reveal**: AM/PM routine with real pharmacy products at the chosen budget, and a weekly selfie milestone timeline. Show it as a plan and check-in schedule, not as a promised skin result.
  6. Social proof: early users, waitlist count, pharmacist/dermatologist review if it is true.
  7. Transparent trial timeline (Day 0 access, reminder on Day 5, charge on Day 7) with an opt-in reminder notification.
  8. A 2-plan paywall with annual pre-selected and framed per month (€39.99/year ≈ €3.33/month vs €7.99/month).
- A first-session "aha" (the routine plus a first selfie baseline) addresses Day-0 cancellations. Trial-day push and email nudges should drive the 2nd routine check-in and the Day-7 selfie before billing.

### Gaps
- No 2024–2026 quantified A/B results were found specifically for "plan reveal", "progress projection" or "social proof" screens in beauty/skin apps.
- An unverified claim ("annual pre-selected gives 69% vs 28% annual selection") surfaced via a low-quality aggregator and is excluded.
- No French-language onboarding/paywall benchmark data was found.
