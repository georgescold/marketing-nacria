# TikTok monde : carrousels (mode photo) et vidéos sur l'acné qui performent, slide par slide (relevé du 2026-10-01)

> **Méthode, à lire avant les chiffres.** 144 publications en mode photo (carrousels) et 49 vidéos. Les statistiques viennent du JSON public intégré aux pages TikTok (`__UNIVERSAL_DATA_FOR_REHYDRATION__` : playCount, diggCount, commentCount, shareCount, collectCount, isAd, imagePost, textLanguage, locationCreated), relevé via curl/Python le 2026-10-01. Je n'ai pas utilisé le navigateur intégré. Les slides ont été téléchargées puis lues une par une.
> **Biais de l'échantillon :** il a été construit par recherches de mots-clés (acne, hormonal acne, acne routine, acne app, face mapping, PCOS, chin acne… en EN/ES/DE/IT/FR). J'ai aussi ajouté volontairement les comptes d'apps et de leurs ambassadrices, ce qui sur-représente l'archétype APP. Ce n'est donc pas un tirage aléatoire de TikTok.
> **« Favoris »** = collectCount (enregistrements). **« Abonnés »** = valeur au jour du relevé, pas au jour de la publication : le ratio vues/abonnés est donc indicatif. **Langue** = champ TikTok ; « un » veut dire non déterminé, souvent quand la légende ne contient que des hashtags. **Pays** = locationCreated. TikTok arrondit les vues (ex. 31.4M).
> Ce dossier ne reprend pas l'étude francophone existante (`organique_tiktok_instagram.md`). Ici, le périmètre est mondial et l'accent porte sur les carrousels.

## 1. Quels carrousels acné performent dans le monde, et avec quelles statistiques ?

### Takeaway
Sur 144 carrousels, la médiane organique est d'environ 650K vues et de 0,95 % de favoris par vue.
- **Les plus gros succès (20 à 31M vues)** sont de trois types :
  - des cartes du visage illustrées (« What your spots mean ») ;
  - un classement de produits ouvert par un selfie ;
  - un « je n'y croyais plus → peau nette » en 3 slides.
- **Les favoris viennent des carrousels longs.** Ceux de 9 slides et plus (n=25) ont une médiane de 1,4M vues et 1,65 % de favoris, contre 0,78 % pour les carrousels de 1 à 2 slides.
- **Les micro-comptes percent régulièrement.** Des comptes de moins de 5K abonnés dépassent 1M vues, avec des ratios vues/abonnés de 1 000 à 10 000×.

### Cited Findings
**Agrégats** (calcul propre sur les 144 URL du tableau 1.1 ; organique = isAd « non », n=137) :

- **Ensemble organique :** médiane 650,5K vues, 7,3K favoris, 0,95 % de favoris/vue, 0,15 % de partages/vue, ratio vues/abonnés 90×.
- **Publications payées :** les 7 carrousels marqués isAd ont une médiane de 1,4M vues mais seulement 0,26 % de favoris et 0,03 % de partages. Exemples : [@lifewithmils](https://www.tiktok.com/@lifewithmils/photo/7589914914874084628), [@mia.srxx](https://www.tiktok.com/@mia.srxx/photo/7600029357171576096), [@elisa_mthx](https://www.tiktok.com/@elisa_mthx/photo/7626042137511202071), [@adermio_](https://www.tiktok.com/@adermio_/photo/7598278605809929494), [@daisyycbj](https://www.tiktok.com/@daisyycbj/photo/7678523196798258446), [@isabelle.skin.sto](https://www.tiktok.com/@isabelle.skin.sto/photo/7561834128119745824), [@glowupgirlies8](https://www.tiktok.com/@glowupgirlies8/photo/7415661659764624645).
- **Nombre de slides (organique, médiane 6) :**

  | Slides | n | Vues médianes | Favoris médians |
  |---|---|---|---|
  | 1–2 | 22 | 549,6K | 0,78 % |
  | 3–5 | 31 | 509K | 0,81 % |
  | 6–8 | 59 | 630,8K | 1,35 % |
  | 9 et plus | 25 | 1,4M | 1,65 % |

  Calcul sur le tableau 1.1.
- **Taille du compte :**

  | Abonnés | n | Vues médianes |
  |---|---|---|
  | moins de 5K | 50 | 437K |
  | 5K à 50K | 49 | 843,5K |
  | plus de 50K | 38 | 1,2M |

  Calcul sur le tableau 1.1.
- **Langue :**

  | Langue | n | Vues médianes |
  |---|---|---|
  | en | 105 | 660,8K |
  | es | 8 | 1,4M |
  | de | 3 | 1,4M |
  | fr | 3 | 575K |
  | indéterminée (un) | 17 | 569K |

  L'espagnol et l'allemand performent mais les effectifs sont faibles. Calcul sur le tableau 1.1.
- **Année de publication :** 2024 (n=21) médiane 630,8K ; 2025 (n=53) 705,4K ; 2026 (n=63) 617,9K. Je n'observe pas d'essoufflement du format. Calcul sur le tableau 1.1.
- **Taux de favoris les plus élevés :**
  - recette « DRINK YOUR RETINOL », 6,26 % (544,4K favoris pour 8,7M vues) — [Source](https://www.tiktok.com/@yogawithflorentia/photo/7490927112233176328) ;
  - « healing your gut… », 6,24 % — [Source](https://www.tiktok.com/@kimi.ditto/photo/7532912583200754950) ;
  - « Let's talk PCOS: part 2 », 5,77 % — [Source](https://www.tiktok.com/@otiliabuciuneanu/photo/7532968580636298518) ;
  - « for 6 months.. », 5,44 % — [Source](https://www.tiktok.com/@ofeemi7/photo/7631209994641362208) ;
  - routine produits en espagnol, 5,23 % — [Source](https://www.tiktok.com/@candy.dulcedulce/photo/7642473124734405909) ;
  - « how i stopped hormonal acne breakouts – full detailed guide », 5,21 % — [Source](https://www.tiktok.com/@danakim_82992/photo/7672998737383279903).
- **Taux de partages les plus élevés :**
  - recette « retinol », 0,84 % (73K partages) — [Source](https://www.tiktok.com/@yogawithflorentia/photo/7490927112233176328) ;
  - « What your spots mean », 0,75 % (179,9K partages pour 24,1M vues) — [Source](https://www.tiktok.com/@glowhubdaily/photo/7560799878457150742) ;
  - face mapping « pimple on Nose → Heart », 0,45 % (49K partages) — [Source](https://www.tiktok.com/@factslipv9n/photo/7617159938795785494).
- **Recyclage de templates :**
  - « What your spots mean (acne version) pt. 2 » de @dewbyr (3,8K abonnés, 9,2M vues) reprend les mêmes illustrations que le pt. 2 de @glowhubdaily (20,4M vues), sans le filigrane — [dewbyr](https://www.tiktok.com/@dewbyr/photo/7669262433793379597) ; [glowhubdaily pt.2](https://www.tiktok.com/@glowhubdaily/photo/7561185115200654614).
  - Le pt. 1 de @glowhubdaily porte lui-même le filigrane d'un autre compte (« jack.glo ») — [Source](https://www.tiktok.com/@glowhubdaily/photo/7560799878457150742).
  - Un « pt. 3 » sur le même son « Manchild » fait 626,9K vues — [Source](https://www.tiktok.com/@nimacare/photo/7686532521252703520).
  - Le son « Manchild » revient sur 5 carrousels du top (glowhubdaily ×2, tkgrace0, glowupgirlies8, nimacare). Voir la colonne Son du tableau 1.1.
- **Funnel d'app caché derrière les deux carrousels n° 3 et 4.** @glowhubdaily (55,9K abonnés) ne cite aucune app dans ses slides. Sa bio dit « Get your personalized skincare routine 👇 » et renvoie vers getskinroutine.com — [Profil](https://www.tiktok.com/@glowhubdaily) (relevé JSON du profil).
- **Carrousel n° 1 (31,4M vues) :** publication marquée isAd. La légende contient un code promo de marque (« ad code LIFEWITHMILS »). Le taux de favoris n'est que de 0,09 % — [Source](https://www.tiktok.com/@lifewithmils/photo/7589914914874084628).

**Tableau 1.1 : 144 carrousels acné, classés par vues.** Archétypes : voir section 4. Styles visuels : SELFIE, FLATLAY (produits posés à plat), ILLU (illustration), AI-ILLU (illustration générée par IA), INFOG (infographie), DESIGN (slides graphiques), PINTEREST (esthétique moodboard), APP-UI (captures d'app), BA (avant/après), BA-COLLAGE, TYPO (typographie seule), FOOD, MEME.

| # | Auteur (abonnés) | Date | Vues | Likes | Comm. | Partages | Favoris | Favoris % | Vues/abonnés | Slides | Langue (pays) | isAd | Son | Archétype | Style visuel | Slide 1 (accroche, ≤15 mots) | URL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | @lifewithmils (363.7K) | 2025-12-31 | 31.4M | 73.3K | 275 | 2.9K | 27.2K | 0.09% | 86× | 4 | en (IT) | oui | original sound | RANKED | SELFIE | rating skincare I used to clear my acne: | https://www.tiktok.com/@lifewithmils/photo/7589914914874084628 |
| 2 | @kylahamlin0 (233.9K) | 2025-08-20 | 24.6M | 2.5M | 3.3K | 24.1K | 195.6K | 0.80% | 105× | 3 | en (US) | non | original sound | JOURNEY | SELFIE+MEME | my skin is so clogged, this is never going to get better | https://www.tiktok.com/@kylahamlin0/photo/7540478128888483085 |
| 3 | @glowhubdaily (55.9K) | 2025-10-13 | 24.1M | 1.4M | 4.9K | 179.9K | 422.5K | 1.75% | 431× | 7 | un (US) | non | Manchild | FACEMAP | ILLU | What your spots mean | https://www.tiktok.com/@glowhubdaily/photo/7560799878457150742 |
| 4 | @glowhubdaily (55.9K) | 2025-10-14 | 20.4M | 1.0M | 4.1K | 54.0K | 276.4K | 1.35% | 365× | 7 | un (GB) | non | Manchild | FACEMAP | ILLU | What your spots mean pt. 2 | https://www.tiktok.com/@glowhubdaily/photo/7561185115200654614 |
| 5 | @factslipv9n (8.5K) | 2026-03-14 | 11.0M | 287.3K | 2.1K | 49.0K | 85.0K | 0.77% | 1301× | 4 | en (PK) | non | original sound | FACEMAP | ILLU | If you have pimple on Nose / Then take care of Heart! | https://www.tiktok.com/@factslipv9n/photo/7617159938795785494 |
| 6 | @moceaane (20.5K) | 2025-09-01 | 9.4M | 1.2M | 5.4K | 11.3K | 40.6K | 0.43% | 459× | 7 | fr (FR) | non | original sound | JOURNEY | AI-ILLU | (no text) AI illustration: woman with acne at mirror | https://www.tiktok.com/@moceaane/photo/7545184841336179990 |
| 7 | @dewbyr (3.8K) | 2026-08-02 | 9.2M | 317.2K | 2.4K | 16.3K | 87.3K | 0.95% | 2427× | 7 | en (US) | non | оригинальный звук | FACEMAP | ILLU | What your spots mean (acne version) pt. 2 | https://www.tiktok.com/@dewbyr/photo/7669262433793379597 |
| 8 | @yogawithflorentia (84.5K) | 2025-04-08 | 8.7M | 745.2K | 1.8K | 73.0K | 544.4K | 6.26% | 103× | 13 | en (CH) | non | snow elves | LIFESTYLE | FOOD | DRINK YOUR RETINOL for clear skin / swipe for recipe | https://www.tiktok.com/@yogawithflorentia/photo/7490927112233176328 |
| 9 | @elumiex (94.1K) | 2024-12-27 | 8.5M | 717.4K | 1.5K | 31.7K | 380.3K | 4.47% | 90× | 6 | en (GB) | non | original sound | HOLYGRAIL | FLATLAY | Products that helped my acne | https://www.tiktok.com/@elumiex/photo/7453086703767588118 |
| 10 | @tkgrace0 (10.5K) | 2025-07-08 | 7.7M | 531.4K | 2.3K | 6.9K | 166.3K | 2.16% | 733× | 17 | en (US) | non | Manchild | RANKED | SELFIE+PRODUCT | Ranking face washes as someone who struggled with ... hormonal acne for years | https://www.tiktok.com/@tkgrace0/photo/7524689650481401119 |
| 11 | @lume.37 (5.9K) | 2025-08-08 | 7.6M | 160.2K | 574 | 19.8K | 28.0K | 0.37% | 1292× | 5 | un (US) | non | Lost Soul | APP | AI-ILLU | No Acne (water) vs Acne (soda) | https://www.tiktok.com/@lume.37/photo/7536196645587848466 |
| 12 | @glowjournalmamata (202.4K) | 2024-12-18 | 6.8M | 318.2K | 1.3K | 38.7K | 8.4K | 0.12% | 34× | 12 | en (AU) | non | The Months of the Year | JOURNEY | SELFIE | January (month-by-month timeline) | https://www.tiktok.com/@glowjournalmamata/photo/7449577681324100871 |
| 13 | @meyybeauty (10.6K) | 2025-07-13 | 6.7M | 278.3K | 2.2K | 12.8K | 79.9K | 1.19% | 632× | 3 | en (NL) | non | original sound | MAKEUP | FLATLAY | Is my concealer acne safe? | https://www.tiktok.com/@meyybeauty/photo/7526612059514031392 |
| 14 | @sari_chu (14.0K) | 2025-06-24 | 5.3M | 327.2K | 1.1K | 9.0K | 142.2K | 2.68% | 379× | 8 | en (NO) | non | original sound | HOLYGRAIL | FLATLAY | My top 3 korean skincare products | https://www.tiktok.com/@sari_chu/photo/7519595473410395415 |
| 15 | @ofeemi7 (189.3K) | 2026-07-11 | 5.0M | 428.9K | 1.1K | 19.6K | 255.8K | 5.12% | 26× | 9 | en (DE) | non | som original | LIFESTYLE | SELFIE | solving your skin problems (with 0$) | https://www.tiktok.com/@ofeemi7/photo/7661402703075052832 |
| 16 | @candy.dulcedulce (1.1M) | 2026-05-21 | 4.3M | 392.5K | 484 | 21.1K | 224.9K | 5.23% | 4× | 7 | es (MX) | non | high fashion x track 10 mix | HOLYGRAIL | PINTEREST | productos que te cambiarán la vida | https://www.tiktok.com/@candy.dulcedulce/photo/7642473124734405909 |
| 17 | @hiridew (1.1K) | 2026-05-10 | 3.7M | 329.8K | 947 | 6.3K | 107.2K | 2.90% | 3407× | 8 | en (US) | non | Les (Instrumental Slowed) | LIFESTYLE | PINTEREST | ACTUAL glow up tips | https://www.tiktok.com/@hiridew/photo/7638350422905851150 |
| 18 | @edreiglow (105.9K) | 2026-03-26 | 3.6M | 80.5K | 140 | 1.3K | 8.8K | 0.24% | 34× | 6 | un (NI) | non | I Wouldnt Mind | MISTAKES | SELFIE | X: "Deja de comer azúcar" | https://www.tiktok.com/@edreiglow/photo/7621349821672197389 |
| 19 | @honestbeautyreviewer (14.5K) | 2025-05-06 | 3.5M | 90.0K | 894 | 2.8K | 66.2K | 1.89% | 241× | 5 | en (GB) | non | Aesthetic Sunset | RANKED | FLATLAY | Azelaic acid Honest review / For acne, redness & Hormonal acne | https://www.tiktok.com/@honestbeautyreviewer/photo/7501330464959958294 |
| 20 | @lysxtmendez (510) | 2025-08-19 | 3.2M | 272.4K | 1.6K | 14.7K | 25.8K | 0.81% | 6275× | 3 | en (US) | non | crying and puking | CYCLE | PHOTO+INFOG | i told him i struggle with something that takes over my whole life | https://www.tiktok.com/@lysxtmendez/photo/7540383336431111455 |
| 21 | @kathrynsgrwms (30.6K) | 2025-12-09 | 3.2M | 384.7K | 833 | 5.5K | 16.0K | 0.50% | 105× | 2 | en (US) | non | xanny | RELATABLE | SELFIE | "why do you always have your hair down?" | https://www.tiktok.com/@kathrynsgrwms/photo/7581976256736955662 |
| 22 | @only1aliya (2.5M) | 2025-09-05 | 3.1M | 234.4K | 594 | 3.8K | 16.3K | 0.53% | 1× | 10 | en (US) | non | lacy | RELATABLE | SELFIE | your (phrase split across slides: baddies have acne) | https://www.tiktok.com/@only1aliya/photo/7546703055484472607 |
| 23 | @silviany_mtzz (617) | 2025-06-15 | 3.0M | 129.7K | 1.3K | 7.8K | 20.8K | 0.69% | 4862× | 14 | es (MX) | non | original sound | EDU | BA-COLLAGE | ACNÉ HORMONAL (tipos de acné) | https://www.tiktok.com/@silviany_mtzz/photo/7516080715486743864 |
| 24 | @pureskincareoficial (27.7K) | 2026-04-11 | 2.9M | 165.0K | 531 | 12.3K | 117.4K | 4.05% | 105× | 8 | es (PE) | non | champagne | ROUTINE | FLATLAY | Rutina skincare Día - piel mixta/grasa | https://www.tiktok.com/@pureskincareoficial/photo/7627592324448668948 |
| 25 | @laura.ckrm (2.6K) | 2026-03-31 | 2.9M | 70.8K | 255 | 5.0K | 12.0K | 0.41% | 1098× | 8 | de (DE) | non | Dracula (with JENNIE) | JOURNEY | SELFIE | before microneedling | https://www.tiktok.com/@laura.ckrm/photo/7623523423888657696 |
| 26 | @ajcrying (1.6K) | 2026-03-11 | 2.8M | 386.6K | 501 | 3.5K | 32.1K | 1.15% | 1704× | 9 | un (US) | non | original sound | JOURNEY | SELFIE | cuz we can stay heree | https://www.tiktok.com/@ajcrying/photo/7616132054635253023 |
| 27 | @natalie_oneillll (1.1M) | 2026-04-01 | 2.6M | 121.3K | 1.1K | 4.7K | 75.1K | 2.89% | 2× | 8 | en (GB) | non | marys_theme.mp4 | EDU | DESIGN | THE ONLY azelaic acid post you'll ever need | https://www.tiktok.com/@natalie_oneillll/photo/7623844761480269078 |
| 28 | @drbarbella (34.5K) | 2026-04-07 | 2.5M | 29.5K | 189 | 5.1K | 9.0K | 0.36% | 72× | 1 | en (CA) | non | Luxury Real Estate | CYCLE | INFOG | 70% of women who have PCOS are undiagnosed | https://www.tiktok.com/@drbarbella/photo/7626090953341799698 |
| 29 | @kimi.ditto (9.8K) | 2025-07-30 | 2.1M | 208.8K | 309 | 9.0K | 131.0K | 6.24% | 215× | 5 | en (CZ) | non | original sound | LIFESTYLE | SELFIE | healing your gut is the KEY to clear skin | https://www.tiktok.com/@kimi.ditto/photo/7532912583200754950 |
| 30 | @vcxeii6 (3.2K) | 2026-03-09 | 2.0M | 73.1K | 324 | 5.3K | 45.5K | 2.27% | 634× | 8 | en (MA) | non | Life Will Be | EDU | DESIGN | KNOW & TREAT YOUR SKIN CONCERN - 1. ACNE & ITS TYPES | https://www.tiktok.com/@vcxeii6/photo/7615308097523059989 |
| 31 | @sweetskinsorbet (17.6K) | 2026-04-05 | 2.0M | 61.2K | 375 | 2.6K | 36.9K | 1.85% | 114× | 6 | en (GB) | non | charli xcx 360 sped up | HOLYGRAIL | FLATLAY | Best serums for ........ | https://www.tiktok.com/@sweetskinsorbet/photo/7625299232479644950 |
| 32 | @isis_15_01 (5.3K) | 2025-08-23 | 2.0M | 23.5K | 215 | 1.3K | 7.2K | 0.36% | 379× | 2 | es (DO) | non | Papasito | FACEMAP | INFOG | MAPA FACIAL DEL ACNÉ | https://www.tiktok.com/@isis_15_01/photo/7541613045164870917 |
| 33 | @mia.srxx (1.4K) | 2026-01-27 | 2.0M | 76.7K | 79 | 9.9K | 42.1K | 2.10% | 1390× | 6 | un (FR) | oui | original sound | APP | SELFIE+APP-UI | the photo i sent | https://www.tiktok.com/@mia.srxx/photo/7600029357171576096 |
| 34 | @cheekygirlforyou (53.7K) | 2026-03-25 | 1.8M | 303.8K | 922 | 3.6K | 11.3K | 0.63% | 34× | 7 | en (US) | non | original sound | RELATABLE | SELFIE | I have acne now | https://www.tiktok.com/@cheekygirlforyou/photo/7620992195830500638 |
| 35 | @acnefromatoz (95.4K) | 2024-03-06 | 1.7M | 51.5K | 611 | 2.8K | 14.9K | 0.88% | 18× | 10 | en (US) | non | RUNAWAY | EDU-HORMONAL | DESIGN | HORMONAL ACNE SYMPTOMS - Watch Out For These 6 Signs | https://www.tiktok.com/@acnefromatoz/photo/7343223970587495712 |
| 36 | @skincare22n (4.2K) | 2026-06-27 | 1.7M | 73.9K | 619 | 2.4K | 36.4K | 2.14% | 402× | 8 | en (AU) | non | suara asli - 𝟑𝟎𝟑 𝐍𝐨𝐚.`𖤐 | HOLYGRAIL | FLATLAY | My favorite product from every category for acne prone skin | https://www.tiktok.com/@skincare22n/photo/7655868145088957704 |
| 37 | @drbarbella (34.5K) | 2026-04-14 | 1.6M | 32.8K | 190 | 4.9K | 14.3K | 0.89% | 46× | 1 | en (CA) | non | Life | CYCLE | INFOG | How your cycle affects your face, skin & hair | https://www.tiktok.com/@drbarbella/photo/7628690371832253703 |
| 38 | @glowupgirlies8 (8.0K) | 2025-08-01 | 1.6M | 70.7K | 813 | 2.4K | 49.1K | 3.07% | 199× | 6 | en (CA) | non | Manchild | HOLYGRAIL | FLATLAY | Products I switched in my routine | https://www.tiktok.com/@glowupgirlies8/photo/7533628481280773381 |
| 39 | @lailapaul7 (2.2M) | 2026-09-08 | 1.6M | 101.0K | 196 | 4.6K | 65.8K | 4.11% | 1× | 14 | en (JE) | non | som original | HOLYGRAIL | BA-COLLAGE | Skin concerns>>> | https://www.tiktok.com/@lailapaul7/photo/7683216618184396054 |
| 40 | @elisa_mthx (1.3K) | 2026-04-07 | 1.6M | 32.0K | 45 | 3.3K | 16.6K | 1.04% | 1223× | 6 | un (PT) | oui | What can i do | APP | SELFIE+APP-UI | la photo que j'ai prise y'a 3 mois : | https://www.tiktok.com/@elisa_mthx/photo/7626042137511202071 |
| 41 | @her.soft.glow1 (23.4K) | 2026-07-07 | 1.6M | 102.5K | 555 | 7.4K | 47.3K | 2.96% | 68× | 5 | en (XK) | non | original sound | FACEMAP | COLLAGE | For acne on forehead (apples) | https://www.tiktok.com/@her.soft.glow1/photo/7659906394920848647 |
| 42 | @acnefromatoz (95.4K) | 2024-03-18 | 1.5M | 45.6K | 383 | 2.6K | 13.6K | 0.91% | 16× | 10 | en (US) | non | Little Life | EDU-HORMONAL | DESIGN | HORMONAL ACNE SIGNS - Keep an Eye on These 6 Major Symptoms | https://www.tiktok.com/@acnefromatoz/photo/7347690519683714337 |
| 43 | @misspeytonsmith (214.8K) | 2026-04-14 | 1.5M | 87.6K | 435 | 1.8K | 24.7K | 1.65% | 7× | 12 | en (AU) | non | original sound | RELATABLE | SELFIE | "Just moisturise" | https://www.tiktok.com/@misspeytonsmith/photo/7628477751904734484 |
| 44 | @acnetrack_app (2.9K) | 2025-07-16 | 1.5M | 21.4K | 135 | 247 | 3.9K | 0.26% | 524× | 4 | en (US) | non | original sound | APP | AI-ILLU | Acne on forehead / No acne | https://www.tiktok.com/@acnetrack_app/photo/7527713138083466526 |
| 45 | @lifewithmils (363.7K) | 2026-04-11 | 1.4M | 126.8K | 301 | 1.3K | 7.3K | 0.52% | 4× | 10 | en (GB) | non | original sound | JOURNEY | SELFIE | we could stay here... | https://www.tiktok.com/@lifewithmils/photo/7627471704171875604 |
| 46 | @dermarkologist (1.2M) | 2025-10-10 | 1.4M | 58.6K | 351 | 2.1K | 36.2K | 2.59% | 1× | 8 | en (US) | non | Rocky Mountain Way | EXPERT | SELFIE+PRODUCT | 8 years as a dermatologist and still no one believes me... | https://www.tiktok.com/@dermarkologist/photo/7559600092651539742 |
| 47 | @veribeautiful (6.3K) | 2024-05-08 | 1.4M | 50.3K | 976 | 3.8K | 12.1K | 0.86% | 221× | 10 | de (AT) | non | Tell Ur Girlfriend | EDU | BA-COLLAGE | Hormonelle Akne (Akne Typen) | https://www.tiktok.com/@veribeautiful/photo/7366522095750237473 |
| 48 | @daisyycbj (945.0K) | 2026-08-27 | 1.4M | 5.4K | 283 | 285 | 1.1K | 0.08% | 1× | 6 | en (US) | oui | original sound | JOURNEY | SELFIE | "Is it contagious?" | https://www.tiktok.com/@daisyycbj/photo/7678523196798258446 |
| 49 | @aamnaadel (1.8M) | 2024-05-22 | 1.3M | 122.3K | 516 | 2.9K | 51.7K | 3.97% | 1× | 6 | en (GB) | non | original sound | EXPERT | SELFIE | HYGIENE HACKS you *NEED* to know from a dermatologist | https://www.tiktok.com/@aamnaadel/photo/7371891844583673120 |
| 50 | @alexmorleyx (30.0K) | 2024-01-23 | 1.2M | 12.0K | 143 | 197 | 2.8K | 0.23% | 40× | 3 | en (GB) | non | two chopper 200 shots bang | EDU-HORMONAL | SELFIE | "drink more water" "go on accutane" "just go on the pill again" | https://www.tiktok.com/@alexmorleyx/photo/7327437129871543584 |
| 51 | @yourfav.tip (37.8K) | 2024-03-25 | 1.2M | 67.8K | 94 | 2.4K | 18.6K | 1.55% | 32× | 2 | en (US) | non |  | FACEMAP | TEXT | Want to know why you have acne? >> | https://www.tiktok.com/@yourfav.tip/photo/7350265185233292587 |
| 52 | @kiki.13521 (44.8K) | 2026-02-19 | 1.2M | 36.4K | 111 | 3.7K | 18.6K | 1.55% | 27× | 5 | en (DE) | non | original sound | APP | SELFIE+APP-UI | the photo i sent | https://www.tiktok.com/@kiki.13521/photo/7608626660803448086 |
| 53 | @riri.03d (10.2K) | 2025-12-26 | 1.2M | 77.4K | 190 | 2.1K | 28.0K | 2.33% | 118× | 5 | un (KE) | non | son original | LIFESTYLE | SELFIE-COLLAGE | ways of getting a clear skin | https://www.tiktok.com/@riri.03d/photo/7588086682520522006 |
| 54 | @dermarkologist (1.2M) | 2026-05-25 | 1.1M | 42.9K | 696 | 5.8K | 42.9K | 3.90% | 1× | 6 | en (US) | non | The One That Got Away | EXPERT | SELFIE | 8 years as a dermatologist and still no one believes me | https://www.tiktok.com/@dermarkologist/photo/7643881873197780255 |
| 55 | @gotnomoneyinmypockets (5.5K) | 2026-03-24 | 1.1M | 54.1K | 267 | 2.6K | 5.1K | 0.47% | 200× | 11 | en (CA) | non | original sound | JOURNEY | SELFIE | my skin before accutane | https://www.tiktok.com/@gotnomoneyinmypockets/photo/7620626105153735943 |
| 56 | @mariee.lgx (429) | 2026-03-21 | 1.1M | 161.3K | 1.1K | 4.7K | 8.5K | 0.77% | 2564× | 2 | en (CA) | non | original sound | RELATABLE | SELFIE | "Uh girl just wash your face" | https://www.tiktok.com/@mariee.lgx/photo/7619823261651635476 |
| 57 | @sereanova (50.2K) | 2025-02-07 | 1.0M | 41.9K | 217 | 1.2K | 26.6K | 2.66% | 20× | 8 | en (DE) | non | son original | HOLYGRAIL | FLATLAY | The skincare routine that healed my hormonal acne.. | https://www.tiktok.com/@sereanova/photo/7468643547667844374 |
| 58 | @adermio_ (3.5K) | 2026-01-22 | 1.0M | 3.0K | 23 | 339 | 2.6K | 0.26% | 286× | 5 | fr (FR) | oui | original sound | APP | SELFIE+APP-UI | la photo que j'ai envoyé : | https://www.tiktok.com/@adermio_/photo/7598278605809929494 |
| 59 | @elyseeeeeeeeeeee (2.5K) | 2025-10-05 | 991.5K | 121.2K | 277 | 1.5K | 7.4K | 0.75% | 390× | 8 | en (US) | non | original sound | RELATABLE | SELFIE | makeup for school (pov acne) | https://www.tiktok.com/@elyseeeeeeeeeeee/photo/7557579229722889527 |
| 60 | @willixm_nja (12.2K) | 2026-03-15 | 907.0K | 97.9K | 288 | 1.6K | 22.9K | 2.52% | 74× | 9 | en (DE) | non | original sound | LIFESTYLE | SELFIE | 7 Tipps to glow up | https://www.tiktok.com/@willixm_nja/photo/7617584780460297504 |
| 61 | @mostsecretspammsz (733) | 2025-12-08 | 888.1K | 65.8K | 188 | 1.7K | 29.6K | 3.33% | 1212× | 6 | en (US) | non | original sound - Altare | HOLYGRAIL | SELFIE | products i swear by that changed my acne | https://www.tiktok.com/@mostsecretspammsz/photo/7581630974774037791 |
| 62 | @kenzwolffofficial (142.5K) | 2024-03-13 | 882.4K | 12.3K | 205 | 622 | 2.1K | 0.23% | 6× | 2 | en (US) | non | End of Beginning | JOURNEY | SELFIE | week 1 of spironolactone & adapalene | https://www.tiktok.com/@kenzwolffofficial/photo/7345992605798272298 |
| 63 | @drbarbella (34.5K) | 2026-06-01 | 848.1K | 12.8K | 134 | 1.4K | 6.4K | 0.75% | 25× | 1 | en (CA) | non | Flowers (Nature Sounds) | EDU-HORMONAL | INFOG | Your Hormonal Acne Type & location depending on your Hormone Imbalance | https://www.tiktok.com/@drbarbella/photo/7646247599908932872 |
| 64 | @danicolexx (1.7M) | 2024-01-24 | 846.3K | 56.6K | 167 | 243 | 12.7K | 1.51% | 0× | 8 | en (US) | non | som original | FACEMAP | SELFIE | Your face tells you how to help clear acne | https://www.tiktok.com/@danicolexx/photo/7327788252864220449 |
| 65 | @girlcoded.4 (6.1K) | 2026-05-29 | 843.5K | 27.3K | 85 | 2.1K | 15.1K | 1.79% | 139× | 5 | en (DE) | non | original sound | EDU | DESIGN | comedonal acne = [skin] + CeraVe + Differin | https://www.tiktok.com/@girlcoded.4/photo/7645289236471483680 |
| 66 | @modosop (55.5K) | 2025-08-14 | 739.5K | 14.6K | 189 | 2.8K | 5.7K | 0.77% | 13× | 7 | es (ES) | non | Steven Universe | EDU-HORMONAL | DESIGN | CÓMO MEJORAR EL ACNÉ HORMONAL (SIN SOLUCIONES MÁGICAS) | https://www.tiktok.com/@modosop/photo/7538484803197340950 |
| 67 | @isabellamonberg (32.4K) | 2025-06-29 | 711.7K | 18.4K | 119 | 895 | 2.4K | 0.34% | 22× | 20 | en (DK) | non | original sound | JOURNEY | SELFIE | Acne to clear skin journey | https://www.tiktok.com/@isabellamonberg/photo/7521256558878100758 |
| 68 | @cureandkind (5.7K) | 2025-12-08 | 708.3K | 3.5K | 57 | 136 | 478 | 0.07% | 123× | 1 | en (NG) | non | ESCALADIZZY X WITH YOU JMK R | EDU-HORMONAL | DESIGN | 10 Signs your Acne is Hormonal | https://www.tiktok.com/@cureandkind/photo/7581502925063703815 |
| 69 | @prettywellnessco (3.1K) | 2025-07-01 | 705.4K | 11.1K | 88 | 196 | 3.7K | 0.52% | 226× | 1 | en (US) | non | original sound - jhonriel vh | RANKED | FLATLAY | Best / Average (products tier) | https://www.tiktok.com/@prettywellnessco/photo/7522068282506038583 |
| 70 | @ofeemi7 (189.3K) | 2026-04-21 | 680.2K | 76.5K | 117 | 2.8K | 37.0K | 5.44% | 4× | 9 | en (DE) | non | original sound | LIFESTYLE | SELFIE | for 6 months.. | https://www.tiktok.com/@ofeemi7/photo/7631209994641362208 |
| 71 | @yayacareyourskin (358) | 2025-10-02 | 675.2K | 15.9K | 108 | 875 | 7.0K | 1.04% | 1886× | 6 | en (TH) | non | พี่ชอบหนูที่สุดเลย (I Like Y | EDU-HORMONAL | DESIGN | Is Your Acne Hormonal? Here's How to Tell | https://www.tiktok.com/@yayacareyourskin/photo/7556477767160810760 |
| 72 | @holistic.abby (6.9K) | 2025-10-03 | 660.8K | 17.4K | 80 | 582 | 10.6K | 1.61% | 96× | 7 | en (US) | non | original sound | RANKED | FLATLAY | WHAT HEALED MY HORMONAL ACNE VS. WHAT DIDN'T HEAL IT | https://www.tiktok.com/@holistic.abby/photo/7557136260360359198 |
| 73 | @cleyra.app (1.8K) | 2025-12-24 | 655.0K | 9.8K | 67 | 931 | 3.8K | 0.58% | 357× | 6 | en (US) | non | original sound - Altare | APP | DESIGN | the accutane "nose job" explained | https://www.tiktok.com/@cleyra.app/photo/7587283290646760734 |
| 74 | @jk1d21 (5.0K) | 2026-08-17 | 650.5K | 59.7K | 312 | 2.6K | 30.1K | 4.62% | 130× | 8 | un (NZ) | non | sonido original | ROUTINE | SELFIE | How to get clear skin - it gets progressively more advanced | https://www.tiktok.com/@jk1d21/photo/7674812092699954452 |
| 75 | @skinwithlisa (11.7K) | 2026-06-09 | 631.5K | 29.3K | 447 | 731 | 10.7K | 1.69% | 54× | 5 | en (AU) | non | original sound | ROUTINE | SELFIE | If your skin looks like this.... | https://www.tiktok.com/@skinwithlisa/photo/7649340249520229653 |
| 76 | @natalie_oneillll (1.1M) | 2024-09-11 | 630.8K | 18.0K | 200 | 180 | 3.6K | 0.56% | 1× | 7 | en (GB) | non | heatwaves x diet pepsi by ad | MISTAKES | SELFIE | 4 things that are ruining your skin | https://www.tiktok.com/@natalie_oneillll/photo/7413385749397048608 |
| 77 | @nimacare (4.0K) | 2026-09-17 | 626.9K | 9.7K | 17 | 670 | 2.0K | 0.31% | 158× | 7 | un (MA) | non | Manchild | FACEMAP | ILLU | What your spots mean pt. 3 | https://www.tiktok.com/@nimacare/photo/7686532521252703520 |
| 78 | @zayjagonzalez (2.2K) | 2026-03-07 | 617.9K | 23.3K | 212 | 404 | 5.0K | 0.81% | 276× | 8 | es (MX) | non | I've Seen It | JOURNEY | SELFIE | Hace un año mi piel estaba así. Y a mis 25 años nunca había tenido acné | https://www.tiktok.com/@zayjagonzalez/photo/7614313104343649543 |
| 79 | @danakim_82992 (25.6K) | 2026-08-12 | 614.1K | 49.1K | 198 | 2.3K | 32.0K | 5.21% | 24× | 13 | en (US) | non | full version on my youtube | ROUTINE | SELFIE-COLLAGE | how i stopped hormonal acne breakouts - full detailed guide 2025-2026 | https://www.tiktok.com/@danakim_82992/photo/7672998737383279903 |
| 80 | @francesca__aagostinelli (102.6K) | 2024-05-24 | 613.9K | 18.4K | 74 | 79 | 1.2K | 0.19% | 6× | 3 | en (US) | non | What Was I Made For? [From T | CYCLE | SELFIE | My acne when I got my period before... | https://www.tiktok.com/@francesca__aagostinelli/photo/7372650204610317614 |
| 81 | @chloefkr (12.5K) | 2025-02-07 | 575.4K | 69.7K | 108 | 2.5K | 22.3K | 3.88% | 46× | 9 | fr (FR) | non | Real Love Baby | LIFESTYLE | SELFIE | Manger sa skincare > | https://www.tiktok.com/@chloefkr/photo/7468616298235235586 |
| 82 | @esteticatech (13.7K) | 2024-11-24 | 569.3K | 11.3K | 62 | 1.1K | 4.4K | 0.78% | 42× | 1 | un (ES) | non | Stargazing | FACEMAP | INFOG | MAPA DE ACNÉ - lo que dice en tu rostro | https://www.tiktok.com/@esteticatech/photo/7440632699200572704 |
| 83 | @hannah_brot (97.1K) | 2026-04-05 | 567.5K | 23.6K | 108 | 539 | 21.7K | 3.82% | 6× | 6 | de (DE) | non | HATE STARS | ROUTINE | SELFIE+PRODUCT | Ich bin der Beweis dass Drogerie Skincare absolut ausreicht | https://www.tiktok.com/@hannah_brot/photo/7625309246850075937 |
| 84 | @lifewithmils (363.7K) | 2026-04-24 | 543.6K | 31.6K | 78 | 693 | 19.4K | 3.57% | 1× | 12 | en (ES) | non | Originalton | LIFESTYLE | SELFIE | simple changes i made to clear my hormonal acne... | https://www.tiktok.com/@lifewithmils/photo/7632237177165942037 |
| 85 | @onlybig_slenderty (2.9K) | 2026-05-13 | 530.0K | 93.7K | 420 | 744 | 4.6K | 0.86% | 181× | 2 | en (NG) | non | End Of Beginning by DJO | JOURNEY | SELFIE | Another version of me.... | https://www.tiktok.com/@onlybig_slenderty/photo/7639448013043371284 |
| 86 | @caramelcupcakeangel (14.4K) | 2026-03-06 | 517.4K | 87.4K | 460 | 1.6K | 6.0K | 1.16% | 36× | 2 | en (US) | non | original sound | RELATABLE | SELFIE | "just wash your face" | https://www.tiktok.com/@caramelcupcakeangel/photo/7614209214231235854 |
| 87 | @glassglowapp (1.1K) | 2026-03-26 | 509.0K | 1.7K | 7 | 37 | 192 | 0.04% | 444× | 5 | en (ZA) | non | Little Things | APP | TYPO | 63% of women notice worse skin before their period | https://www.tiktok.com/@glassglowapp/photo/7621512327224904982 |
| 88 | @tesalonicaaaa (462) | 2026-01-02 | 509.0K | 14.3K | 385 | 295 | 2.1K | 0.42% | 1102× | 3 | en (PH) | non | original sound | JOURNEY | SELFIE | Before | https://www.tiktok.com/@tesalonicaaaa/photo/7590768241325116690 |
| 89 | @isabelle.skin.sto (49) | 2025-10-16 | 504.1K | 2.0K | 15 | 93 | 365 | 0.07% | 10288× | 5 | en (TH) | oui | Moulaga - Sped up | JOURNEY | SELFIE | Lets get rid of acne! | https://www.tiktok.com/@isabelle.skin.sto/photo/7561834128119745824 |
| 90 | @noeliacadenass (80.0K) | 2025-08-04 | 485.8K | 14.6K | 124 | 357 | 2.5K | 0.51% | 6× | 6 | es (ES) | non | original sound | EDU-HORMONAL | SELFIE | Síntomas del Acné Hormonal | https://www.tiktok.com/@noeliacadenass/photo/7534835686462049558 |
| 91 | @otiliabuciuneanu (33.0K) | 2025-07-30 | 476.4K | 36.5K | 108 | 1.5K | 27.5K | 5.77% | 14× | 3 | en (RO) | non | i love vlada | CYCLE | SELFIE | Let's talk PCOS: part 2 | https://www.tiktok.com/@otiliabuciuneanu/photo/7532968580636298518 |
| 92 | @beauty.archives (716) | 2025-02-16 | 464.0K | 5.2K | 23 | 185 | 2.7K | 0.57% | 648× | 5 | en (ID) | non | sonido original | LIFESTYLE | BA | before / after (habits & tips to stop my chin acne) | https://www.tiktok.com/@beauty.archives/photo/7472031625761606917 |
| 93 | @shaserafini (7.4K) | 2024-04-18 | 462.1K | 17.8K | 178 | 1.0K | 13.3K | 2.88% | 62× | 6 | it (IT) | non | i like the way you kiss me | MAKEUP | FLATLAY | RECAP TRUCCHI LOW COST ACNE SAFE | https://www.tiktok.com/@shaserafini/photo/7359167490041204001 |
| 94 | @saravalentinaldn (2.8K) | 2026-05-20 | 458.3K | 17.7K | 65 | 129 | 1.5K | 0.32% | 163× | 8 | en (AE) | non | original sound | JOURNEY | SELFIE | We can stay here... | https://www.tiktok.com/@saravalentinaldn/photo/7641979279684668694 |
| 95 | @elizacesle (1.9K) | 2026-05-27 | 451.8K | 14.9K | 88 | 272 | 3.9K | 0.86% | 235× | 7 | en (LV) | non | original sound | JOURNEY | SELFIE | October 2025 (timeline) | https://www.tiktok.com/@elizacesle/photo/7644605286740692246 |
| 96 | @nextgen.nutriskin (389) | 2025-08-20 | 446.5K | 16.1K | 54 | 988 | 6.5K | 1.45% | 1148× | 7 | en (MY) | non | Being a Girl | FACEMAP | ILLU | ACNE FACE MAPPING - What Your Pimples Are Trying to Tell You | https://www.tiktok.com/@nextgen.nutriskin/photo/7540513582488849682 |
| 97 | @beautywollie (840) | 2025-07-12 | 443.9K | 23.6K | 86 | 872 | 11.1K | 2.50% | 528× | 7 | en (US) | non | Illegal | EXPERT | SELFIE | girlies, … here is what a dermatologist WON'T tell you! | https://www.tiktok.com/@beautywollie/photo/7526004693621886222 |
| 98 | @salmeen_c (11.7K) | 2026-01-14 | 434.0K | 10.9K | 92 | 781 | 6.9K | 1.59% | 37× | 6 | en (CA) | non | they come and go | EDU-HORMONAL | PHOTO | Signs your jawline acne is tied to blood sugar and gut, not just hormones | https://www.tiktok.com/@salmeen_c/photo/7595354229791837447 |
| 99 | @your_.skinn (513) | 2025-12-24 | 430.8K | 19.6K | 64 | 656 | 3.8K | 0.89% | 840× | 2 | en (SG) | non | original sound | MISTAKES | ILLU | Acne Mistakes | https://www.tiktok.com/@your_.skinn/photo/7587290708864879892 |
| 100 | @clearskinemily (706) | 2025-04-06 | 430.3K | 4.8K | 42 | 142 | 4.5K | 1.06% | 609× | 5 | en (US) | non | original sound | APP | BA-COLLAGE+APP-UI | Products I used to solve... | https://www.tiktok.com/@clearskinemily/photo/7490302216369196319 |
| 101 | @cocoonskinco (7.8K) | 2024-12-11 | 423.5K | 3.6K | 73 | 244 | 2.2K | 0.52% | 54× | 5 | en (CA) | non | cool water | CYCLE | SELFIE | "I only break out around my mouth and chin... worsens before my period" "WHY???" | https://www.tiktok.com/@cocoonskinco/photo/7447279524724641030 |
| 102 | @thrlxn (981) | 2026-06-27 | 417.4K | 10.2K | 118 | 201 | 1.2K | 0.29% | 425× | 6 | en (PH) | non | drop dead | JOURNEY | SELFIE | One night I was covered in acne / August 2025 | https://www.tiktok.com/@thrlxn/photo/7655878069990870290 |
| 103 | @glowy.cloudy.angel (2.1K) | 2026-03-31 | 407.3K | 13.0K | 64 | 818 | 3.4K | 0.84% | 197× | 3 | en (DE) | non | som original | MAKEUP | FLATLAY | Is my Concealer Acne safe? Drogerie Edition | https://www.tiktok.com/@glowy.cloudy.angel/photo/7623449220099378464 |
| 104 | @francesca__aagostinelli (102.6K) | 2025-05-02 | 389.9K | 7.8K | 58 | 680 | 4.1K | 1.05% | 4× | 3 | en (US) | non | original sound | CYCLE | BA-COLLAGE | HOW I TOOK MY HORMONAL ACNE before my periods from this... | https://www.tiktok.com/@francesca__aagostinelli/photo/7499952719914962222 |
| 105 | @lifewithmils (363.7K) | 2025-12-26 | 386.4K | 20.0K | 66 | 192 | 4.2K | 1.09% | 1× | 2 | en (GB) | non | Trunks | MISTAKES | SELFIE | things I thought would clear my acne | https://www.tiktok.com/@lifewithmils/photo/7588078322400218388 |
| 106 | @lumiskin.app (12.2K) | 2026-05-27 | 383.7K | 19.7K | 116 | 396 | 7.4K | 1.92% | 31× | 1 | en (DE) | non | Golden Hour Echoes | RANKED | FLATLAY | Ranking products for skin barrier | https://www.tiktok.com/@lumiskin.app/photo/7644656006508580116 |
| 107 | @roottoglow (2.9K) | 2025-08-12 | 375.7K | 28.6K | 227 | 552 | 4.1K | 1.08% | 128× | 2 | en (MY) | non | suara asli - astrooo🪐 | MISTAKES | SELFIE | skincare mistakes youre probably making | https://www.tiktok.com/@roottoglow/photo/7537728543132896520 |
| 108 | @kenzwolffofficial (142.5K) | 2024-08-05 | 367.8K | 8.6K | 50 | 309 | 6.9K | 1.86% | 3× | 5 | en (US) | non | original sound | ROUTINE | SELFIE | post hormonal acne skincare routine | https://www.tiktok.com/@kenzwolffofficial/photo/7399691476449398058 |
| 109 | @backup.kikijr (37.4K) | 2026-07-28 | 363.6K | 22.1K | 125 | 534 | 1.6K | 0.44% | 10× | 10 | un (CH) | non | original sound - Isaac | JOURNEY | SELFIE | (no text, male selfie) | https://www.tiktok.com/@backup.kikijr/photo/7667690144555666710 |
| 110 | @jadia_off (2.2K) | 2025-09-14 | 346.5K | 7.6K | 47 | 1.5K | 4.5K | 1.29% | 155× | 1 | fr (FR) | non | Hot Blooded | FACEMAP | INFOG | Ce que ton acné te dit | https://www.tiktok.com/@jadia_off/photo/7549989014674115842 |
| 111 | @feelbetterroutine (108.1K) | 2026-05-29 | 342.2K | 4.1K | 45 | 893 | 2.4K | 0.72% | 3× | 1 | en (TR) | non | Tenderness | FACEMAP | INFOG | WHAT YOUR ACNE LOCATION MEANS | https://www.tiktok.com/@feelbetterroutine/photo/7645339329992183071 |
| 112 | @iwantcandy77 (1.7M) | 2025-09-01 | 332.4K | 26.4K | 192 | 158 | 572 | 0.17% | 0× | 8 | en (IT) | non | Vienna | RELATABLE | SELFIE | skin that looks like this... | https://www.tiktok.com/@iwantcandy77/photo/7545157534819077389 |
| 113 | @kiki.13521 (44.8K) | 2026-05-03 | 327.1K | 8.8K | 36 | 675 | 4.2K | 1.27% | 7× | 6 | un (DE) | non | CHIHIRO | APP | SELFIE | the photo I took 6 months ago: | https://www.tiktok.com/@kiki.13521/photo/7635734511262633248 |
| 114 | @samliao94 (624) | 2026-08-31 | 326.4K | 15.5K | 100 | 551 | 7.4K | 2.26% | 523× | 8 | un (US) | non | Ain't In LA | ROUTINE | SELFIE+APP-UI | How I CLEAR acne step by step | https://www.tiktok.com/@samliao94/photo/7680017444768894222 |
| 115 | @ap.ugc (2.0K) | 2024-04-28 | 326.2K | 2.6K | 54 | 49 | 806 | 0.25% | 160× | 8 | en (GB) | non | Nothing's New | JOURNEY | SELFIE | BEEN EXPERIENCING CHIN ACNE FOR A MONTH NOW | https://www.tiktok.com/@ap.ugc/photo/7362974574587170081 |
| 116 | @cenchct (4.8K) | 2025-10-21 | 316.1K | 11.8K | 145 | 279 | 2.9K | 0.90% | 65× | 2 | un (PH) | non | original sound | MISTAKES | SELFIE | things i tried to clear my hormonal acne | https://www.tiktok.com/@cenchct/photo/7563501402220203284 |
| 117 | @emmamcarey (72) | 2025-05-16 | 315.7K | 10.4K | 64 | 102 | 320 | 0.10% | 4385× | 13 | en (US) | non | original sound | JOURNEY | SELFIE | my acne journey | https://www.tiktok.com/@emmamcarey/photo/7504900099026226474 |
| 118 | @noeliacadenass (80.0K) | 2026-02-25 | 312.0K | 16.4K | 106 | 1.4K | 10.4K | 3.32% | 4× | 9 | es (ES) | non | Originalton | LIFESTYLE | SELFIE+FOOD | "Mi acné hormonal jamás se curará..." | https://www.tiktok.com/@noeliacadenass/photo/7610768311281896726 |
| 119 | @teawithmd (788.0K) | 2024-11-22 | 310.8K | 8.2K | 67 | 546 | 7.4K | 2.37% | 0× | 6 | en (US) | non | APT. | EXPERT | SELFIE | POV: Dermatologist creates you an acne skincare routine | https://www.tiktok.com/@teawithmd/photo/7440173817353309483 |
| 120 | @benk1.m (33.3K) | 2026-06-14 | 310.0K | 9.4K | 95 | 391 | 5.3K | 1.73% | 9× | 7 | en (US) | non | som original | ROUTINE | SELFIE | the skincare routine that took my skin from this | https://www.tiktok.com/@benk1.m/photo/7651059823437450526 |
| 121 | @cleyra.app (1.8K) | 2025-12-23 | 300.9K | 12.7K | 95 | 578 | 3.4K | 1.14% | 164× | 7 | en (US) | non | I Walk This Earth All By Mys | APP | DESIGN | Accutane timeline - what usually happens (and when) | https://www.tiktok.com/@cleyra.app/photo/7586850500780248351 |
| 122 | @dermguru (1.7M) | 2026-04-24 | 300.6K | 6.6K | 62 | 211 | 6.0K | 1.99% | 0× | 8 | en (US) | non | original sound | EXPERT | SELFIE | the best drugstore retinols (from a dermatologist) | https://www.tiktok.com/@dermguru/photo/7632284968655293726 |
| 123 | @glowupgirlies8 (8.0K) | 2024-09-17 | 285.4K | 6.3K | 125 | 344 | 5.0K | 1.76% | 36× | 7 | en (CA) | oui | gilmore lala | APP | APP-UI | The best skincare app >>> | https://www.tiktok.com/@glowupgirlies8/photo/7415661659764624645 |
| 124 | @bylillybell (11.2K) | 2026-06-12 | 275.9K | 13.1K | 211 | 122 | 5.4K | 1.96% | 25× | 19 | en (GB) | non | original sound | RANKED | SELFIE+PRODUCT | skincare that healed or destroyed my skin as a 23 year old acne prone girl | https://www.tiktok.com/@bylillybell/photo/7650607516040138006 |
| 125 | @sirisano (24.1K) | 2024-07-25 | 251.1K | 2.4K | 51 | 169 | 1.2K | 0.47% | 10× | 6 | en (US) | non | 9am in Calabasas | APP | SELFIE+APP-UI | AI saved me from Acne... | https://www.tiktok.com/@sirisano/photo/7395677479567887662 |
| 126 | @stella.dlx (109) | 2026-09-11 | 198.1K | 8.5K | 16 | 894 | 5.8K | 2.92% | 1817× | 6 | un (PT) | non | original sound | APP | SELFIE+APP-UI | La foto che ho inviato: | https://www.tiktok.com/@stella.dlx/photo/7684249697422183712 |
| 127 | @mia.srxx (1.4K) | 2026-05-18 | 182.5K | 9.7K | 22 | 330 | 2.2K | 1.20% | 127× | 7 | un (FR) | non | Originalton - Iron Mindset | APP | SELFIE+APP-UI | And you're gonna fail | https://www.tiktok.com/@mia.srxx/photo/7641225703043648800 |
| 128 | @lightofdestani (2.1K) | 2024-08-19 | 175.6K | 9.6K | 104 | 522 | 4.4K | 2.49% | 83× | 35 | en (US) | non | original sound | APP | PHOTO+APP-UI | Scanning skincare products at Walmart so you don't have to | https://www.tiktok.com/@lightofdestani/photo/7404978660295396638 |
| 129 | @skincare.luvr4 (293) | 2024-09-26 | 139.7K | 1.3K | 9 | 43 | 876 | 0.63% | 477× | 5 | en (US) | non | ariana grande . ill do it | APP | SELFIE+APP-UI | Struggling with acne? | https://www.tiktok.com/@skincare.luvr4/photo/7418756357131717930 |
| 130 | @clearskinemily (706) | 2025-04-11 | 118.9K | 564 | 20 | 47 | 429 | 0.36% | 168× | 7 | en (US) | non | оригинальный звук - :) | APP | APP-UI | Yuka vs Thea app | https://www.tiktok.com/@clearskinemily/photo/7492171761610394911 |
| 131 | @glow.by.uk (1.7K) | 2026-06-22 | 108.0K | 1.4K | 14 | 116 | 1.0K | 0.94% | 65× | 7 | en (PK) | non | suara asli - TEMPLATE FOR YO | EDU | BA-COLLAGE | INFLAMMATORY ACNE | https://www.tiktok.com/@glow.by.uk/photo/7654365495658908949 |
| 132 | @dracneapp (837) | 2025-09-29 | 86.1K | 313 | 15 | 43 | 79 | 0.09% | 103× | 1 | en (CO) | non | original sound | APP | ILLU | DEEP ACNE NODULE | https://www.tiktok.com/@dracneapp/photo/7555651429512269067 |
| 133 | @kiki.13521 (44.8K) | 2026-03-06 | 74.5K | 1.7K | 18 | 53 | 461 | 0.62% | 2× | 8 | en (DE) | non | original sound | APP | SELFIE+APP-UI | "Acne is hormonal, you can't do anything about it" | https://www.tiktok.com/@kiki.13521/photo/7614205405337570582 |
| 134 | @heyitsme_laine23 (712) | 2026-06-28 | 69.2K | 1.7K | 36 | 45 | 412 | 0.60% | 97× | 4 | en (PH) | non | full song on soundcloud | JOURNEY | SELFIE | Where I Started (February 2026) | https://www.tiktok.com/@heyitsme_laine23/photo/7656409972355484935 |
| 135 | @kiki.13521 (44.8K) | 2026-05-20 | 68.9K | 1.7K | 17 | 91 | 598 | 0.87% | 2× | 5 | en (DE) | non | original sound | APP | SELFIE+APP-UI | the photo i sent | https://www.tiktok.com/@kiki.13521/photo/7642064015161609505 |
| 136 | @elle_skincarejrny (39) | 2026-07-18 | 63.1K | 994 | 6 | 72 | 115 | 0.18% | 1618× | 7 | en (PH) | non | original sound - DJ KEV1Z 🇱🇦 | APP | SELFIE+APP-UI | 2025... (vs 2026) | https://www.tiktok.com/@elle_skincarejrny/photo/7663699527194496277 |
| 137 | @alyssaskincarequeen (2.4K) | 2025-05-19 | 62.4K | 335 | 0 | 4 | 188 | 0.30% | 27× | 6 | en (US) | non | original sound | APP | APP-UI | i found all of these products from the thea app | https://www.tiktok.com/@alyssaskincarequeen/photo/7506004951169273134 |
| 138 | @clearskinalyssa (15.8K) | 2025-10-01 | 51.6K | 385 | 4 | 16 | 89 | 0.17% | 3× | 3 | en (US) | non | plug walk remix | APP | SELFIE+APP-UI | personalize your skincare | https://www.tiktok.com/@clearskinalyssa/photo/7556390331189611790 |
| 139 | @stella.dlx (109) | 2026-09-26 | 46.6K | 1.1K | 7 | 72 | 589 | 1.26% | 428× | 7 | un (FR) | non | SMASHITHARDER | APP | SELFIE+APP-UI | Finalmente un'IA affidabile per l'acne | https://www.tiktok.com/@stella.dlx/photo/7689854522226658592 |
| 140 | @kiki.13521 (44.8K) | 2026-03-18 | 44.5K | 1.6K | 24 | 38 | 342 | 0.77% | 1× | 6 | en (DE) | non | original sound - naddy🩹 | APP | SELFIE+APP-UI | Try the AcneTrack App | https://www.tiktok.com/@kiki.13521/photo/7618658853542186243 |
| 141 | @skinnbysummer (3.3K) | 2025-09-15 | 43.0K | 461 | 5 | 17 | 206 | 0.48% | 13× | 3 | un (US) | non | original sound | APP | SELFIE | after years, the only thing that helped | https://www.tiktok.com/@skinnbysummer/photo/7550463488183848222 |
| 142 | @clearskinalyssa (15.8K) | 2026-02-20 | 40.0K | 562 | 8 | 21 | 565 | 1.41% | 3× | 5 | en (US) | non | My Love | APP | SELFIE+APP-UI | i mean thea is saying good match but idk?? | https://www.tiktok.com/@clearskinalyssa/photo/7608777637481237790 |
| 143 | @miri_ngiri (3.0K) | 2025-08-04 | 38.0K | 256 | 13 | 7 | 115 | 0.30% | 13× | 2 | en (US) | non | Super Shy | APP | APP-UI | Checking if my skincare routine is safe | https://www.tiktok.com/@miri_ngiri/photo/7534571547906854199 |
| 144 | @clearskinchloe (8) | 2025-09-29 | 37.7K | 202 | 1 | 13 | 213 | 0.56% | 4712× | 5 | en (US) | non | original sound | APP | BA-COLLAGE+APP-UI | How I healed my hormonal acne: | https://www.tiktok.com/@clearskinchloe/photo/7555597905264954655 |

### Inferences
- **Le reach maximal va au « diagnostic utile et partageable ».** La carte du visage en est l'exemple type, même quand le contenu est pseudo-scientifique : la version « organes » de @factslipv9n associe le nez au cœur et la mâchoire au foie. Nacre peut en reprendre la mécanique (une zone par slide, 2 à 4 facteurs, une illustration neutre) sans aucune allégation sur les organes.
- **Pour les favoris, il faut de la longueur et de l'utilitaire :** listes, recettes, routines, guides de 8 à 13 slides. Pour le reach, des formats émotionnels de 2 à 3 slides suffisent (selfie + phrase), mais ils sont peu enregistrés.
- **Le payé (isAd) augmente les vues mais pas les favoris.** Un Spark ad Nacre devrait donc viser le clic, alors que l'organique devrait viser l'enregistrement.
- **Le format se copie et se re-poste vite.** Un format qui marche chez Nacre sera cloné : il vaut mieux y apposer une identité visuelle forte et récurrente.

### Gaps
- TikTok ne publie pas de données par slide (taux de swipe, abandon), ni l'origine du trafic (FYP, recherche, profil). Je ne peux pas mesurer quelle slide retient.
- Le drapeau isAd ne capte pas forcément tous les Spark ads ou boosts. Certains gros chiffres organiques peuvent être sponsorisés sans marquage.
- Je n'ai pas l'âge des créatrices, ni celui de leur audience. La cible 25–35 ans n'est pas vérifiable par compte.
- Instagram n'est pas couvert.

## 2. Que disent les ~30 meilleurs carrousels, slide par slide ?

### Takeaway
Quatre structures dominent :
1. **Accroche-problème → preuve (selfie) → liste notée**, par exemple les notations x/10 et les « holy grail ».
2. **Une zone ou un signe par slide**, comme la carte du visage ou les « 6 signes ».
3. **Chronologie de selfies**, mois par mois ou jour par jour.
4. **Phrase blessante ou conseil non sollicité → twist**, en 2 à 6 slides.

La marque ou l'app est presque toujours absente des slides 1 à 3. Quand elle apparaît, c'est sur la dernière slide, dans un filigrane, dans la légende (code promo) ou dans la bio.

### Cited Findings
Format de chaque fiche : vues · favoris % · nombre de slides · style. S = slide. Les résumés font au plus 15 mots ; les citations sont dans la langue d'origine.

**#1 @lifewithmils.** 31,4M · 0,09 % · 4 slides · isAd · selfie, puis produit tenu en main. [Source](https://www.tiktok.com/@lifewithmils/photo/7589914914874084628)
- S1 : selfie souriant, « rating skincare I used to clear my acne: ».
- S2 : profil avec acné, « (the acne in question) », « body acne too ».
- S3 : spot treatment noté « 100000000/10 » (azélaïque + salicylique + bakuchiol, « no purge »).
- S4 : version roll-on notée « ∞/10 », mention de l'acné du corps.
- Légende : produit de marque et code promo.

**#2 @kylahamlin0.** 24,6M · 0,80 % · 3 slides · selfie + mème. [Source](https://www.tiktok.com/@kylahamlin0/photo/7540478128888483085)
- S1 : selfie peau texturée, « my skin is so clogged, this is never going to get better ».
- S2 : carton noir « Directed by Robert B. Weide » (mème du générique).
- S3 : selfie peau nette, « stopped listening to my dermatologist & taught myself ».
- Légende : « a long time coming but we made it ».

**#3 @glowhubdaily.** 24,1M · 1,75 % · 7 slides · illustration beige uniforme. [Source](https://www.tiktok.com/@glowhubdaily/photo/7560799878457150742)
- S1 : titre « What your spots mean », visage illustré yeux fermés.
- S2 : front → sommeil, digestion, alimentation, stress.
- S3 : nez → alimentation, digestion, sébum, bactéries, stress.
- S4 : contour des lèvres → gras, produits comédogènes, alimentation.
- S5 : bas du visage et mâchoire → « hormonal », nettoyage, stress.
- S6 : joues → téléphone, taie d'oreiller, produits capillaires.
- S7 : sourcils → alimentation, bactéries.
- Légende : hashtags seulement. La bio renvoie vers getskinroutine.com.

**#4 @glowhubdaily pt. 2.** 20,4M · 1,35 % · 7 slides · même template. [Source](https://www.tiktok.com/@glowhubdaily/photo/7561185115200654614)
- S2 : entre les sourcils → alimentation, stress, sueur.
- S3 : ligne des cheveux → shampoing, cheveux sales, après-shampoing.
- S4 : autour du nez → laitages, produits comédogènes, sommeil.
- S5 : pommettes → téléphone, taie, sucre.
- S6 : menton → dentifrice, gras, intestin.
- S7 : cou → drainage lymphatique, « hormonal fluctuations », nettoyage.

**#5 @factslipv9n.** 11,0M · 0,77 % · 4 slides · illustration réaliste générée par IA (aigc=2) avec organes. [Source](https://www.tiktok.com/@factslipv9n/photo/7617159938795785494)
- Formule répétée : « If you have pimple on [zone] / Then take care of [organe]! ». Nez = cœur, joues = digestion, mâchoire = foie, oreilles = reins, front = hormones.
- À ne pas reproduire : ce sont des allégations santé infondées.

**#6 @moceaane (FR).** 9,4M · 0,43 % · 7 slides · BD générée par IA, puis photo réelle. [Source](https://www.tiktok.com/@moceaane/photo/7545184841336179990)
- S1 : miroir.
- S2 : moqueries à l'école.
- S3 : comparaison avec Instagram.
- S4 : pleurs.
- S5 : se filme.
- S6 : sourit.
- S7 : vrai selfie avec acné, assumée.
- Aucun texte sur les slides. Légende longue : « plus de 10 ans » d'acné, « À 26 ans », reprise de confiance.

**#7 @dewbyr.** 9,2M · 0,95 % · 7 slides. Copie quasi identique du #4 (voir section 1). [Source](https://www.tiktok.com/@dewbyr/photo/7669262433793379597)

**#8 @yogawithflorentia.** 8,7M · 6,26 % · 13 slides · photos culinaires. [Source](https://www.tiktok.com/@yogawithflorentia/photo/7490927112233176328)
- S1 : « DRINK YOUR RETINOL for clear skin », « swipe for recipe ».
- S2 : liste d'ingrédients (carottes, oranges, citron, gingembre, eau de coco).
- S3 à S13 : étapes (couper, laver, mixer…).
- Légende : bénéfices (« fight breakouts from within »).

**#9 @elumiex.** 8,5M · 4,47 % · 6 slides · produits K-beauty posés sur un drap, notés. [Source](https://www.tiktok.com/@elumiex/photo/7453086703767588118)
- S1 : « Products that helped my acne ».
- S2 : crème, « THE BESTTTT MOISTURIZER ON THIS PLANET », ∞/10.
- S3 : SPF, « perfect sunscreen for acne prone », 200/10.
- S4 : toner, « HOW DID MY FUNGAL ACNE HEAL IN 2 WEEKS », ∞/10.
- S5 : sérums vitamine C, « Dark spots & Hyperpigmentation GONE », 100/10.
- S6 : ampoule, « skin barrier unbreakable », 345542/10.

**#10 @tkgrace0.** 7,7M · 2,16 % · 17 slides · selfie + packshots. [Source](https://www.tiktok.com/@tkgrace0/photo/7524689650481401119)
- S1 : « Ranking face washes as someone who struggled with… hormonal acne for years ».
- S2 : selfie « proof! », « still see my scars but no acne ».
- S3 à S17 : un nettoyant par slide avec note sur 10 et verdict franc. Exemples : CeraVe 3/10, Cetaphil 2/10, Garnier 0/10 « no explanation ».

**#11 @lume.37 (compte officiel Lumé Skin App).** 7,6M · 0,37 % · 5 slides · anime généré par IA. [Source](https://www.tiktok.com/@lume.37/photo/7536196645587848466)
- S1 à S4 : écran partagé « No Acne » / « Acne » (eau / soda, sommeil / téléphone la nuit, salade / burger, démaquillée / dort maquillée).
- S5 : « Uses the Lumé Skin App » / « Doesn't use ».
- Légende vide.

**#12 @glowjournalmamata.** 6,8M · 0,12 % · 12 slides · selfies. [Source](https://www.tiktok.com/@glowjournalmamata/photo/7449577681324100871)
- Un mois par slide, de « January » à décembre. L'acné s'aggrave d'avril à août.
- Légende : « April and June was by far the toughest month ».
- Je n'ai lu que les slides 1 à 8.

**#13 @meyybeauty.** 6,7M · 1,19 % · 3 slides · catalogue produits sur fond crème. [Source](https://www.tiktok.com/@meyybeauty/photo/7526612059514031392)
- S1 : « Is my concealer acne safe? ».
- S2 : « Safe » (16 correcteurs).
- S3 : « Not Safe » (16 correcteurs).
- Légende : « your concealer might be the problem ».

**#14 @sari_chu.** 5,3M · 2,68 % · 8 slides · flat-lay sur drap, médailles 1-2-3. [Source](https://www.tiktok.com/@sari_chu/photo/7519595473410395415)
- S1 : « My top 3 korean skincare products ».
- S2 à S8 : une catégorie par slide (huile démaquillante, nettoyant, toner, sérum, contour des yeux, crème, SPF).

**#15 @ofeemi7.** 5,0M · 5,12 % · 9 slides · selfies de masques maison. [Source](https://www.tiktok.com/@ofeemi7/photo/7661402703075052832)
- S1 : « solving your skin problems (with 0$) ».
- S2 à S9 : un masque par slide avec le problème visé. Curcuma (taches), café (cernes), riz (cicatrices), lin, betterave, thé vert (« inflammation & breakouts »), ail sur bouton.
- À ne pas reproduire tel quel : remèdes non validés.

**#16 @candy.dulcedulce (ES, MX).** 4,3M · 5,23 % · 7 slides · esthétique Pinterest (bureau, iPad). [Source](https://www.tiktok.com/@candy.dulcedulce/photo/7642473124734405909)
- S1 : « productos que te cambiarán la vida ».
- S2 à S7 : un produit tenu en main et un problème par slide. Boutons sur les fesses → acide glycolique ; taches → crème ; SPF « cero cara grasosa »…

**#17 @hiridew.** 3,7M · 2,90 % · 8 slides · Pinterest et avant/après. [Source](https://www.tiktok.com/@hiridew/photo/7638350422905851150)
- S1 : « ACTUAL glow up tips », sur une photo de cascade.
- S2 à S8 : sourcils, lèvres, points noirs, rehaussement de cils, taches de rousseur au henné, taches pigmentaires, dégonflement. Une astuce par slide, avec avant/après.
- Légende : liste d'objectifs (eau, sport…).

**#18 @edreiglow (ES).** 3,6M · 0,24 % · 6 slides · selfies gros plan. [Source](https://www.tiktok.com/@edreiglow/photo/7621349821672197389)
- S1 à S4 : conseils reçus, « X: "Deja de comer azúcar" », « Lávate la cara », « bebe más agua », « Usa pasta de dientes ».
- S5 : peau nette, « Fortalecer la barrera cutánea + cuidar mi salud intestinal ».
- S6 : selfie net avec des cœurs.

**#19 @honestbeautyreviewer.** 3,5M · 1,89 % · 5 slides · flat-lay sur satin, texte dense. [Source](https://www.tiktok.com/@honestbeautyreviewer/photo/7501330464959958294)
- S1 : « Azelaic acid Honest review », « For acne, redness & Hormonal acne ».
- S2 à S5 : un produit par slide, note (8/10, 9/10, 7/10, en test) et pour/contre. Exemple : « helped clear my hormonal acne! ».

**#20 @lysxtmendez.** 3,2M · 0,81 % · 3 slides · photos d'hôpital + infographie. [Source](https://www.tiktok.com/@lysxtmendez/photo/7540383336431111455)
- S1 : « i told him i struggle with something that takes over my whole life ».
- S2 : « he said "oh like anxiety?" ».
- S3 : infographie SOPK (dont « Acne or dark patches of skin ») et « #holyairball ».
- Légende : deuil de son corps.

**#21 @kathrynsgrwms.** 3,2M · 0,50 % · 2 slides · selfies. [Source](https://www.tiktok.com/@kathrynsgrwms/photo/7581976256736955662)
- S1 : « "why do you always have your hair down?" ».
- S2 : selfie cheveux tirés, acné visible, sans texte.

**#22 @only1aliya.** 3,1M · 0,53 % · 10 slides · selfies avec acné. [Source](https://www.tiktok.com/@only1aliya/photo/7546703055484472607)
- Un mot par slide : « your / skin / does / not / define / the / person / you… ».
- Légende : « i've had it for 3 years now… you're not alone ».

**#23 @silviany_mtzz (ES).** 3,0M · 0,69 % · 14 slides · collages de photos de peau. [Source](https://www.tiktok.com/@silviany_mtzz/photo/7516080715486743864)
- Un type d'acné par slide : « ACNÉ HORMONAL », de peau grasse, bactérien, digestif, fongique, excorié, léger, vulgaire…
- Légende : « Ya conocías estos diferentes tipos de acné? ».

**#24 @pureskincareoficial (ES, PE, compte de boutique).** 2,9M · 4,05 % · 8 slides · flat-lay alignés, légendés. [Source](https://www.tiktok.com/@pureskincareoficial/photo/7627592324448668948)
- Alternance « Día » / « Noche » par type de peau : mixte-grasse, sèche, « piel con acné – sensible », sensible.
- 4 à 5 produits nommés par slide.
- La légende précise qu'il n'est pas nécessaire d'avoir tous les produits.

**#25 @laura.ckrm (DE).** 2,9M · 0,41 % · 8 slides · selfies jour par jour. [Source](https://www.tiktok.com/@laura.ckrm/photo/7623523423888657696)
- « before microneedling » → « immediatly after » → « the same evening » → « the next morning: bruises » → « Day 2 » → « Day 3 » → « Day 4 » (nouveaux boutons) → « one week after: fully healed, clear skin, glowy ».

**#27 @natalie_oneillll.** 2,6M · 2,89 % · 8 slides · design éditorial vert, typographie serif. [Source](https://www.tiktok.com/@natalie_oneillll/photo/7623844761480269078)
- S1 : « THE ONLY azelaic acid post you'll ever need ».
- S2 : « your 6 month plan », avant/après « MARCH '23 → MARCH '25 ».
- S3 : « 101: how it works », 4 mécanismes.
- S4 : « retinoid vs AA » (✓/✗).
- S5 : « STEP ONE: introducing AA » (1 à 2 fois par semaine au début).
- S6 : « STEP TWO: your routine ».
- S7 : « STEP THREE: trust the process », environ 6 mois.
- S8 : CTA vers son Substack.

**#35 @acnefromatoz (pharmacienne).** 1,7M · 0,88 % · 10 slides · design rouge corail + photos. [Source](https://www.tiktok.com/@acnefromatoz/photo/7343223970587495712)
- S1 : « HORMONAL ACNE SYMPTOMS – Watch Out For These 6 Signs ».
- S2 : front clair.
- S3 : « JAWLINE & CHIN BREAKOUTS ».
- S4 : « PRODUCTS DON'T WORK ».
- S5 : acné kystique profonde.
- S6 : dos et décolleté.
- S7 : tendance aux cicatrices.
- S8 : « THIS IS NOT HORMONAL ACNE » (intestinale, fongique, bactérienne).
- S9 et S10 : non lues.

**#50 @alexmorleyx.** 1,2M · 0,23 % · 3 slides · selfies. [Source](https://www.tiktok.com/@alexmorleyx/photo/7327437129871543584)
- S1 : conseils entendus, « "drink more water" », « "go on accutane" », « "just go on the pill again" ».
- S2 : « "you'll grow out of it" ».
- S3 : selfie net à la plage, « no let me actually tell you how I cleared my skin ».

**#57 @sereanova.** 1,0M · 2,66 % · 8 slides · flat-lay notés. [Source](https://www.tiktok.com/@sereanova/photo/7468643547667844374)
- S1 : « The skincare routine that healed my hormonal acne.. ».
- S2 à S8 : un produit par slide avec note (100/10, 10/10, ∞/10, 1000/10). On y lit par exemple « Calmed my hormonal acne down » et « MY HORMONAL ACNE WAS HEALED AFTER ONLY A FEW WEEKS! ».

**#79 @danakim_82992.** 614K · 5,21 % · 13 slides · collage de selfies + produits annotés. [Source](https://www.tiktok.com/@danakim_82992/photo/7672998737383279903)
- S1 : « how i stopped hormonal acne breakouts – full detailed guide 2025-2026 ».
- S2 : « now: ».
- S3 : « stop wasting ur money on viral skincare ».
- S4 : trétinoïne et acide azélaïque, avec mode d'emploi.
- S5 : « Barrier repair is key ».
- S6 : papier matifiant.
- S7 : nettoyage doux.
- S8 : sport et cortisol.
- Je n'ai lu que les slides 1 à 8.

**#84 @lifewithmils.** 544K · 3,57 % · 12 slides · selfies + objets. [Source](https://www.tiktok.com/@lifewithmils/photo/7632237177165942037)
- S1 : « simple changes i made to clear my hormonal acne… ».
- S2 : avant, « as someone who's skin looked like this ».
- S3 : latte au curcuma.
- S4 : spray d'acide hypochloreux après le sport.
- S5 : 2 noix du Brésil par jour.
- S6 : « skin cycling ».
- S7 : intestin et probiotiques.
- S8 : rétinoïde, « 9 weeks difference », avec code promo.

**#101 @cocoonskinco (marque de complément).** 424K · 0,52 % · 5 slides · gros plans du menton. [Source](https://www.tiktok.com/@cocoonskinco/photo/7447279524724641030)
- S1 : « "I only break out around my mouth and chin… worsens before my period" "WHY???" ».
- S2 : explication « estrogen dominance » et liste de symptômes de SPM, « sound like you? ».
- S3 : flacon du complément, « see the results ».
- S4 : « after 1 month ».
- S5 : « after 1 month », puis « take our free hormone quiz ».
- Les allégations sont fortes.

**#104 @francesca__aagostinelli.** 390K · 1,05 % · 3 slides · collage avant/après. [Source](https://www.tiktok.com/@francesca__aagostinelli/photo/7499952719914962222)
- S1 : « HOW I TOOK MY HORMONAL ACNE before my periods from this… ».
- S2 : « TO THIS ».
- S3 : texte sur la phase lutéale (progestérone, sébum), aliments et actifs recommandés.

### Inferences
- **La slide 1 porte tout.** On y trouve soit une promesse de liste (« rating », « top 3 », « 6 signs »), soit une phrase émotionnelle. Les slides suivantes répètent une unité stable : un produit, une zone ou un mois par slide.
- **Le chiffrage ludique crée un rythme de swipe.** Les notes x/10, ∞/10 ou 345542/10 et les médailles 1-2-3 apparaissent chez elumiex, sereanova, tkgrace0, sari_chu et honestbeautyreviewer.
- **Les contenus « cycle / hormonal » qui marchent montrent le menton en gros plan et le calendrier.** Exemples : cocoonskinco, francesca, acnefromatoz S3. Ils sont pourtant souvent portés par des marques de compléments avec des allégations (« flush out excess estrogen »). Nacre peut occuper ce terrain avec du suivi plutôt qu'avec des promesses.
- Plusieurs top carrousels contiennent des allégations non conformes pour une marque : « HEALED », « GONE », remèdes maison, organes. Ils servent de référence de format, pas de wording.

### Gaps
- Slides non lues : 9 à 12 de glowjournalmamata, 9 à 17 de tkgrace0, 9 et 10 d'acnefromatoz, 9 à 13 de danakim, 9 à 12 de lifewithmils, 9 à 13 de yogawithflorentia. Je les ai résumées par extrapolation de la structure, sans les citer.
- Les classements #26 à #34 et #36 à #49 ont été vérifiés seulement sur la slide 1 (planches d'accroches), pas slide par slide.

## 3. Quelles formules d'accroche en slide 1 reviennent, et lesquelles parlent d'âge, de cycle, de menton, d'abandon ou d'argent ?

### Takeaway
Les accroches les plus vues sont de quatre types :
- des promesses de décodage (« What your spots mean », « If you have pimple on… ») ;
- des notations (« rating… », « ranking… ») ;
- des citations de conseils non sollicités (« just wash your face », « drink more water ») ;
- des phrases de désespoir qu'on renverse ensuite (« this is never going to get better »).

L'âge adulte (25+ / 30+) n'apparaît presque jamais en slide 1 des carrousels : 1 cas sur 144. Il apparaît plutôt dans les vidéos et les légendes. Le cycle (8 accroches) et le menton (4) sont présents mais restent minoritaires : c'est un espace peu saturé.

### Cited Findings
Étiquettes : [ÂGE] mention d'âge, [CYCLE] règles / SOPK / pilule, [MENTON] menton ou mâchoire, [ABANDON] lassitude ou résignation, [ARGENT] argent ou budget.

1. **Notation de ce que j'ai utilisé.** « rating skincare I used to clear my acne: », 31,4M — [Source](https://www.tiktok.com/@lifewithmils/photo/7589914914874084628)
2. **Désespoir puis twist.** [ABANDON] « my skin is so clogged, this is never going to get better », 24,6M — [Source](https://www.tiktok.com/@kylahamlin0/photo/7540478128888483085)
3. **Décodage.** « What your spots mean », 24,1M — [Source](https://www.tiktok.com/@glowhubdaily/photo/7560799878457150742)
4. **Si X alors Y.** « If you have pimple on Nose / Then take care of Heart! », 11,0M — [Source](https://www.tiktok.com/@factslipv9n/photo/7617159938795785494)
5. **Paradoxe + recette.** « DRINK YOUR RETINOL for clear skin », 8,7M — [Source](https://www.tiktok.com/@yogawithflorentia/photo/7490927112233176328)
6. **Ce qui m'a aidée.** « Products that helped my acne », 8,5M — [Source](https://www.tiktok.com/@elumiex/photo/7453086703767588118)
7. **Classement par une concernée.** [ABANDON] « Ranking face washes as someone who struggled with… hormonal acne for years », 7,7M — [Source](https://www.tiktok.com/@tkgrace0/photo/7524689650481401119)
8. **Binaire illustré.** « No Acne » / « Acne », 7,6M — [Source](https://www.tiktok.com/@lume.37/photo/7536196645587848466)
9. **Chronologie mensuelle.** « January », 6,8M — [Source](https://www.tiktok.com/@glowjournalmamata/photo/7449577681324100871)
10. **Question de vérification.** « Is my concealer acne safe? », 6,7M — [Source](https://www.tiktok.com/@meyybeauty/photo/7526612059514031392)
11. **Top 3.** « My top 3 korean skincare products », 5,3M — [Source](https://www.tiktok.com/@sari_chu/photo/7519595473410395415)
12. **Gratuit.** [ARGENT] « solving your skin problems (with 0$) », 5,0M — [Source](https://www.tiktok.com/@ofeemi7/photo/7661402703075052832)
13. **Ça va changer ta vie (ES).** « productos que te cambiarán la vida », 4,3M — [Source](https://www.tiktok.com/@candy.dulcedulce/photo/7642473124734405909)
14. **Les vrais conseils.** « ACTUAL glow up tips », 3,7M — [Source](https://www.tiktok.com/@hiridew/photo/7638350422905851150)
15. **Conseil non sollicité (ES).** « X: "Deja de comer azúcar" », 3,6M — [Source](https://www.tiktok.com/@edreiglow/photo/7621349821672197389)
16. **Avis honnête.** « Azelaic acid Honest review / For acne, redness & Hormonal acne », 3,5M — [Source](https://www.tiktok.com/@honestbeautyreviewer/photo/7501330464959958294)
17. **Incompréhension.** [CYCLE] « i told him i struggle with something that takes over my whole life », 3,2M (SOPK) — [Source](https://www.tiktok.com/@lysxtmendez/photo/7540383336431111455)
18. **Question blessante.** « "why do you always have your hair down?" », 3,2M — [Source](https://www.tiktok.com/@kathrynsgrwms/photo/7581976256736955662)
19. **Affirmation mot à mot.** « your skin does not define the person you… », 3,1M — [Source](https://www.tiktok.com/@only1aliya/photo/7546703055484472607)
20. **Le seul post nécessaire.** « THE ONLY azelaic acid post you'll ever need », 2,6M — [Source](https://www.tiktok.com/@natalie_oneillll/photo/7623844761480269078)
21. **Statistique choc.** [CYCLE] « 70% of women who have PCOS are undiagnosed », 2,5M — [Source](https://www.tiktok.com/@drbarbella/photo/7626090953341799698)
22. **La clé.** « healing your gut is the KEY to clear skin », 2,1M — [Source](https://www.tiktok.com/@kimi.ditto/photo/7532912583200754950)
23. **La photo envoyée (app).** « the photo i sent », 2,0M, isAd — [Source](https://www.tiktok.com/@mia.srxx/photo/7600029357171576096)
24. **Aveu.** « I have acne now », 1,8M — [Source](https://www.tiktok.com/@cheekygirlforyou/photo/7620992195830500638)
25. **Signes.** « HORMONAL ACNE SYMPTOMS – Watch Out For These 6 Signs », 1,7M — [Source](https://www.tiktok.com/@acnefromatoz/photo/7343223970587495712)
26. **Cycle et visage.** [CYCLE] « How your cycle affects your face, skin & hair », 1,6M — [Source](https://www.tiktok.com/@drbarbella/photo/7628690371832253703)
27. **Conseil absurde.** « "Just moisturise" », 1,5M — [Source](https://www.tiktok.com/@misspeytonsmith/photo/7628477751904734484)
28. **Autorité frustrée.** « 8 years as a dermatologist and still no one believes me… », 1,4M — [Source](https://www.tiktok.com/@dermarkologist/photo/7559600092651539742)
29. **Question des autres.** « "Is it contagious?" », 1,4M, isAd — [Source](https://www.tiktok.com/@daisyycbj/photo/7678523196798258446)
30. **Hacks d'expert.** « HYGIENE HACKS you *NEED* to know from a dermatologist », 1,3M — [Source](https://www.tiktok.com/@aamnaadel/photo/7371891844583673120)
31. **Liste de conseils entendus.** [CYCLE] « "drink more water" "go on accutane" "just go on the pill again" », 1,2M — [Source](https://www.tiktok.com/@alexmorleyx/photo/7327437129871543584)
32. **Curiosité + flèche.** « Want to know why you have acne? >> », 1,2M — [Source](https://www.tiktok.com/@yourfav.tip/photo/7350265185233292587)
33. **Avant traitement.** « my skin before accutane », 1,1M — [Source](https://www.tiktok.com/@gotnomoneyinmypockets/photo/7620626105153735943)
34. **La routine qui a marché.** « The skincare routine that healed my hormonal acne.. », 1,0M — [Source](https://www.tiktok.com/@sereanova/photo/7468643547667844374)
35. **Âge et première fois (ES).** [ÂGE] « Hace un año mi piel estaba así. Y a mis 25 años nunca había tenido acné », 617,9K — [Source](https://www.tiktok.com/@zayjagonzalez/photo/7614313104343649543)
36. **Guide daté.** « how i stopped hormonal acne breakouts – full detailed guide 2025-2026 », 614,1K — [Source](https://www.tiktok.com/@danakim_82992/photo/7672998737383279903)
37. **Règles avant / après.** [CYCLE] « My acne when I got my period before… », 613,9K — [Source](https://www.tiktok.com/@francesca__aagostinelli/photo/7372650204610317614)
38. **Preuve budget (DE).** [ARGENT] « Ich bin der Beweis dass Drogerie Skincare absolut ausreicht », 567,5K — [Source](https://www.tiktok.com/@hannah_brot/photo/7625309246850075937)
39. **Petits changements.** « simple changes i made to clear my hormonal acne… », 543,6K — [Source](https://www.tiktok.com/@lifewithmils/photo/7632237177165942037)
40. **Statistique cycle (app).** [CYCLE] « 63% of women notice worse skin before their period », 509K — [Source](https://www.tiktok.com/@glassglowapp/photo/7621512327224904982)
41. **Pas seulement les hormones.** [MENTON] « Signs your jawline acne is tied to blood sugar and gut, not just hormones », 434K — [Source](https://www.tiktok.com/@salmeen_c/photo/7595354229791837447)
42. **Citation + pourquoi.** [MENTON] [CYCLE] « I only break out around my mouth and chin… worsens before my period », 423,5K — [Source](https://www.tiktok.com/@cocoonskinco/photo/7447279524724641030)
43. **De ça à ça.** [CYCLE] « HOW I TOOK MY HORMONAL ACNE before my periods from this… », 389,9K — [Source](https://www.tiktok.com/@francesca__aagostinelli/photo/7499952719914962222)
44. **Ça dure depuis un mois.** [MENTON] « BEEN EXPERIENCING CHIN ACNE FOR A MONTH NOW », 326,2K — [Source](https://www.tiktok.com/@ap.ugc/photo/7362974574587170081)
45. **Résignation citée (ES).** [ABANDON] « "Mi acné hormonal jamás se curará…" », 312K — [Source](https://www.tiktok.com/@noeliacadenass/photo/7610768311281896726)
46. **Bilan avec âge.** [ÂGE, 23 ans] « skincare that healed or destroyed my skin as a 23 year old acne prone girl », 275,9K — [Source](https://www.tiktok.com/@bylillybell/photo/7650607516040138006)
47. **Fatalisme cité (app).** [ABANDON] « "Acne is hormonal, you can't do anything about it" », 74,5K — [Source](https://www.tiktok.com/@kiki.13521/photo/7614205405337570582)
48. **Répétition de l'échec.** « And you're gonna fail » (×4), puis « And then you win. », 182,5K — [Source](https://www.tiktok.com/@mia.srxx/photo/7641225703043648800)
49. **Après des années.** [ABANDON] « after years, the only thing that helped », 43K — [Source](https://www.tiktok.com/@skinnbysummer/photo/7550463488183848222)

**Comptages sur les 144 accroches de slide 1** (vérifiés à la main) :

| Thème | Accroches | Détail |
|---|---|---|
| Âge 25+ / 30+ | 1 | « a mis 25 años » ; 1 autre mentionne 23 ans |
| Cycle / règles / SOPK / pilule | 8 | |
| Menton / mâchoire | 4 | |
| Abandon / résignation | 5 | |
| Argent / budget / « drugstore » | 5 | « 0$ », « Drogerie » ×2, « LOW COST », « drugstore retinols » |

- Le thème argent revient aussi dans le corps des slides, par exemple « stop wasting ur money on viral skincare » — [Source](https://www.tiktok.com/@danakim_82992/photo/7672998737383279903).
- **Cluster « conseil non sollicité cité »** : n=7, médiane 1,1M vues. Il réunit [edreiglow 3,6M](https://www.tiktok.com/@edreiglow/photo/7621349821672197389), [misspeytonsmith 1,5M](https://www.tiktok.com/@misspeytonsmith/photo/7628477751904734484), [alexmorleyx 1,2M](https://www.tiktok.com/@alexmorleyx/photo/7327437129871543584), [mariee.lgx 1,1M](https://www.tiktok.com/@mariee.lgx/photo/7619823261651635476), [caramelcupcakeangel 517K](https://www.tiktok.com/@caramelcupcakeangel/photo/7614209214231235854), [noeliacadenass 312K](https://www.tiktok.com/@noeliacadenass/photo/7610768311281896726) et [kiki.13521 74,5K](https://www.tiktok.com/@kiki.13521/photo/7614205405337570582).
- **L'âge 30+ apparaît dans les vidéos plutôt que dans les carrousels :**
  - « When you've had clear skin your entire life and suddenly get acne in your 30s » — [Source](https://www.tiktok.com/@eliseshd_/video/7469751732466322690) ;
  - légende « acné hormonale à 30 ans » — [Source](https://www.tiktok.com/@priscillathachh/video/7669819240202997022) ;
  - 30 ans et arrêt de la pilule (isAd) — [Source](https://www.tiktok.com/@trishabaker/video/7552957780190137630).

### Inferences
- **L'angle « acné adulte qui arrive à 25-30 ans sans prévenir » est quasi absent des slides 1 de carrousels** à l'échelle mondiale. C'est un créneau différenciant pour Nacre, à condition de ne pas viser l'attribut personnel en publicité (voir section 6).
- Le cluster « conseil non sollicité » mélange relatable et éducatif, et se décline facilement en français. Exemples : « Bois plus d'eau », « Arrête le sucre », « Reprends la pilule », « T'as qu'à te laver le visage ».
- Le combo cycle + menton est très visuel (gros plan du menton, calendrier) et reste peu exploité hors des marques de compléments.

### Gaps
- Je n'ai pas de mesure de la rétention de la slide 1 seule. L'effet de l'accroche est confondu avec celui du compte et du son.
- Les accroches non anglophones sont peu nombreuses (es 8, de 3, it 1, fr 3) : les conclusions par langue sont fragiles.

## 4. Archétypes récurrents de carrousels : vues et favoris médians par archétype

### Takeaway
- **HOLYGRAIL** (produits qui m'ont aidée, flat-lay noté) et **EDU** (types d'acné, actifs) ont les meilleures médianes de vues : 1,7M chacun.
- **LIFESTYLE**, **HOLYGRAIL** et **ROUTINE** ont les meilleurs taux de favoris : environ 3 à 3,6 %.
- **JOURNEY** (avant/après) est l'archétype le plus fréquent (19) mais il est peu enregistré : 0,43 %.
- **APP** a la médiane la plus basse (129K, 0,60 %). Les exceptions sont des publications payées ou des mèmes IA.

### Cited Findings
Organique uniquement ; calcul propre sur le tableau 1.1, chaque ligne y est sourcée par son URL.

| Archétype (définition) | n | Vues médianes | Favoris médians | Favoris % médian | Partages % médian | Vues/abonnés médian | Exemple phare |
|---|---|---|---|---|---|---|---|
| HOLYGRAIL : produits qui m'ont aidée, notes | 9 | 1,7M | 49,1K | 3,07 % | 0,17 % | 114× | [elumiex 8,5M](https://www.tiktok.com/@elumiex/photo/7453086703767588118) |
| EDU : types d'acné, actifs, mode d'emploi | 6 | 1,7M | 18,0K | 1,37 % | 0,25 % | 180× | [silviany_mtzz 3,0M](https://www.tiktok.com/@silviany_mtzz/photo/7516080715486743864) |
| RELATABLE : phrase blessante ou affirmation + selfie | 8 | 1,3M | 9,9K | 0,69 % | 0,16 % | 35× | [kathrynsgrwms 3,2M](https://www.tiktok.com/@kathrynsgrwms/photo/7581976256736955662) |
| FACEMAP : carte du visage, zones → causes | 13 | 1,2M | 12,7K | 1,29 % | 0,22 % | 158× | [glowhubdaily 24,1M](https://www.tiktok.com/@glowhubdaily/photo/7560799878457150742) |
| LIFESTYLE : alimentation, habitudes, recettes, glow-up | 11 | 907K | 28,0K | 3,57 % | 0,39 % | 74× | [yogawithflorentia 8,7M](https://www.tiktok.com/@yogawithflorentia/photo/7490927112233176328) |
| EXPERT : dermato ou pharmacienne face caméra | 6 | 772K | 23,7K | 2,54 % | 0,19 % | 1× | [dermarkologist 1,4M](https://www.tiktok.com/@dermarkologist/photo/7559600092651539742) |
| EDU-HORMONAL : signes d'acné hormonale | 9 | 739,5K | 6,4K | 0,77 % | 0,16 % | 25× | [acnefromatoz 1,7M](https://www.tiktok.com/@acnefromatoz/photo/7343223970587495712) |
| RANKED : notation x/10, tier list | 6 | 683K | 9,0K | 1,91 % | 0,08 % | 161× | [tkgrace0 7,7M](https://www.tiktok.com/@tkgrace0/photo/7524689650481401119) |
| JOURNEY : avant → après, chronologie de selfies | 19 | 618K | 3,9K | 0,43 % | 0,09 % | 181× | [kylahamlin0 24,6M](https://www.tiktok.com/@kylahamlin0/photo/7540478128888483085) |
| CYCLE : règles, SOPK, phase lutéale | 7 | 614K | 9,0K | 0,81 % | 0,20 % | 46× | [lysxtmendez 3,2M](https://www.tiktok.com/@lysxtmendez/photo/7540383336431111455) |
| ROUTINE : matin/soir, étapes, par type de peau | 8 | 591K | 16,2K | 3,04 % | 0,15 % | 39× | [pureskincareoficial 2,9M](https://www.tiktok.com/@pureskincareoficial/photo/7627592324448668948) |
| MAKEUP : maquillage « acne safe » | 3 | 462K | 13,3K | 1,19 % | 0,20 % | 197× | [meyybeauty 6,7M](https://www.tiktok.com/@meyybeauty/photo/7526612059514031392) |
| MISTAKES : erreurs, « ce que j'ai essayé » | 6 | 409K | 4,0K | 0,90 % | 0,07 % | 50× | [edreiglow 3,6M](https://www.tiktok.com/@edreiglow/photo/7621349821672197389) |
| APP : contenu d'app ou d'ambassadrice | 26 | 129K | 593 | 0,60 % | 0,07 % | 115× | [lume.37 7,6M](https://www.tiktok.com/@lume.37/photo/7536196645587848466) |
| **Tout l'organique** | 137 | 650,5K | 7,3K | 0,95 % | 0,15 % | 90× | |
| isAd (payé) | 7 | 1,4M | 5,0K | 0,26 % | 0,03 % | 286× | |

**Sous-formats transverses :**
- **« La photo que j'ai envoyée » (app) :** 3 versions payées font 2,0M, 1,6M et 1,0M vues — [mia.srxx](https://www.tiktok.com/@mia.srxx/photo/7600029357171576096), [elisa_mthx](https://www.tiktok.com/@elisa_mthx/photo/7626042137511202071), [adermio_](https://www.tiktok.com/@adermio_/photo/7598278605809929494). Les versions organiques font 1,2M, 327K, 198K et 69K — [kiki 1,2M](https://www.tiktok.com/@kiki.13521/photo/7608626660803448086), [kiki 327K](https://www.tiktok.com/@kiki.13521/photo/7635734511262633248), [stella.dlx 198K](https://www.tiktok.com/@stella.dlx/photo/7684249697422183712), [kiki 69K](https://www.tiktok.com/@kiki.13521/photo/7642064015161609505).
- **Notation x/10 sur drap blanc :** elumiex 4,47 %, sari_chu 2,68 % et sereanova 2,66 % de favoris (voir les liens ci-dessus).

### Inferences
- **Pour l'enregistrement** (signal fort de valeur et de futur clic sur la bio), les archétypes à privilégier sont HOLYGRAIL, ROUTINE et LIFESTYLE. Pour Nacre, cela donne des routines par budget, des produits de pharmacie notés et des habitudes.
- **Pour le reach**, ce sont FACEMAP, RELATABLE et JOURNEY.
- **Pour le téléchargement**, les données montrent que l'archétype APP organique est faible. Mieux vaut glisser l'app dans un archétype à forte valeur (routine, carte du visage) que faire un carrousel « pub d'app ».

### Gaps
- Les effectifs par archétype sont petits (3 à 26). Les médianes sont indicatives et ne sont pas statistiquement robustes.
- La classification est faite par moi à partir des slides et des accroches. D'autres codeurs pourraient classer autrement les cas limites (EDU ou EDU-HORMONAL, LIFESTYLE ou ROUTINE).

## 5. Comment se comparent les meilleures vidéos acné mondiales (accroches des 3 premières secondes, formats) ?

### Takeaway
Dans cet échantillon, les vidéos ne battent pas les carrousels.
- **Comparaison top 49 contre top 49 :**

  | | Vues médianes | Favoris % | Partages % | Likes % |
  |---|---|---|---|---|
  | Vidéos | 1,9M | 0,50 % | 0,11 % | 5,4 % |
  | Carrousels | 2,9M | 1,15 % | 0,18 % | 4,7 % |

- **Les vidéos gagnantes sont très courtes :** médiane d'environ 9 s, et 25 sur 49 durent 9 s ou moins.
- **Elles reposent sur trois leviers :** un texte écran en POV ou relatable posé sur un son tendance, une réaction ou un stitch de dermatologue, et des scripts d'ambassadrices d'apps fondés sur un contraste de durée (« in a week not a month »).

### Cited Findings
- Médianes vidéo calculées sur les 49 URL du tableau 5.1. Médianes carrousels calculées sur les 49 carrousels les plus vus du tableau 1.1. Durées : 5 à 147 s, médiane 9 s. 8 vidéos sur 49 sont isAd.
- **Formule « X not Y » (durée), réutilisée par plusieurs apps :**
  - Skan : « how i cleared my acne in a week not a month », 1,1M — [Source](https://www.tiktok.com/@jskintea/video/7627180150731459870). Même script mot pour mot, 881,8K — [Source](https://www.tiktok.com/@beautybybibii/video/7614325680599321869).
  - Thea : « how i cured my hormonal acne in 2 months, not 2 years », 615,5K — [Source](https://www.tiktok.com/@delaneyskincarequeen/video/7621963780028648717).
  - Puffin : « lock in babe, this clear skin took 1 week not 6 years », 996,6K — [Source](https://www.tiktok.com/@bellaskindiaries/video/7666964577912999199).
- **Cycle et menton en vidéo :** « Every time my period comes, my chin breaks out » (isAd), 2,5M — [Source](https://www.tiktok.com/@dewylouie/video/7665859829537213726). « POV: You stop taking birth control… », 8,8M — [Source](https://www.tiktok.com/@laramariekremer/video/7674668819788352801).

**Tableau 5.1 : 49 vidéos acné mondiales (hors France), classées par vues.**

| # | Créateur (abonnés) | Date | Durée | Vues | Likes | Comm. | Partages | Favoris | Favoris % | isAd | Pays | Accroche 0-3 s (≤15 mots) | Format | URL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V1 | @erin.wilsonnnn (212.7K) | 2024-08-02 | 17 s | 89.1M | 10.8M | 16.0K | 296.8K | 517.5K | 0.58% | non | GB | Texte écran « there was before you » + audio tendance (citation poétique) | Avant/pendant/après (trend audio) | https://www.tiktok.com/@erin.wilsonnnn/video/7398659790647414048 |
| V2 | @danicolexx (1.7M) | 2026-04-26 | 17 s | 27.3M | 3.6M | 15.1K | 211.5K | 672.4K | 2.46% | non | US | « POV you started putting rice on your face… » (texte écran) | POV remède maison | https://www.tiktok.com/@danicolexx/video/7633161023519755542 |
| V3 | @drvanitarattan (1.5M) | 2024-12-30 | 87 s | 25.6M | 1.3M | 3.6K | 25.5K | 62.1K | 0.24% | non | GB | Réponse à commentaire « Skincare routine pls » + duo dermato (incrustation) | Duo/réaction dermato sur routine | https://www.tiktok.com/@drvanitarattan/video/7454260752724086049 |
| V4 | @belzkys (345.2K) | 2026-01-22 | 19 s | 23.1M | 127.3K | 2.0K | 10.2K | 43.4K | 0.19% | oui | ID | « the treatment vs » (texte écran, produit appliqué) | Produit spot (pub) | https://www.tiktok.com/@belzkys/video/7598133978700205330 |
| V5 | @simphiwee_mb (97.3K) | 2024-01-04 | 24 s | 13.0M | 252.4K | 3.7K | 6.6K | 8.5K | 0.07% | non | ZA | Audio : « Every cell in my body is beautiful. » | Affirmations / acne positivity | https://www.tiktok.com/@simphiwee_mb/video/7320288048535653638 |
| V6 | @.ameliazep (9.8K) | 2026-07-14 | 6 s | 11.0M | 598.5K | 283 | 8.9K | 9.1K | 0.08% | non | US | « not on my watch. » (texte écran, audio tendance) | Relatable / mème | https://www.tiktok.com/@.ameliazep/video/7662420626656791822 |
| V7 | @ericanic0le (335.4K) | 2024-03-31 | 11 s | 10.7M | 514.2K | 1.6K | 12.3K | 53.5K | 0.50% | non | US | « pov: you clear up your acne in 6 days » | POV ironique | https://www.tiktok.com/@ericanic0le/video/7352563397847715102 |
| V8 | @laramariekremer (160.4K) | 2026-08-16 | 9 s | 8.8M | 645.4K | 3.6K | 27.7K | 18.1K | 0.21% | non | DE | « POV: You stop taking birth control… » | POV arrêt de la pilule | https://www.tiktok.com/@laramariekremer/video/7674668819788352801 |
| V9 | @verysuperrsecrettt (12.2K) | 2026-08-24 | 7 s | 7.0M | 1.1M | 689 | 28.0K | 31.5K | 0.45% | non | US | « when i start to randomly get pimples everywhere and wonder why » | Relatable / mème | https://www.tiktok.com/@verysuperrsecrettt/video/7677624364715609374 |
| V10 | @asupriya2 (2.3K) | 2026-05-23 | 12 s | 6.2M | 164.1K | 1.2K | 26.4K | 43.9K | 0.71% | non | NP | « Day 1 of using 345 cream » + audio « one day or day one? » | Jour 1 produit | https://www.tiktok.com/@asupriya2/video/7643104885277347090 |
| V11 | @abigailpalmr (184.7K) | 2026-05-05 | 12 s | 5.8M | 621.3K | 1.2K | 15.7K | 65.0K | 1.12% | non | KR | Selfie sans texte, légende « no filter.. just real progress » | Progrès sans filtre | https://www.tiktok.com/@abigailpalmr/video/7636538423465004296 |
| V12 | @lindyskindiaries (643) | 2026-04-01 | 7 s | 5.5M | 85.3K | 74 | 164 | 1.8K | 0.03% | oui | US | « how do i explain an app cleared my skin faster than any product » | App (Nolla) – pub | https://www.tiktok.com/@lindyskindiaries/video/7623631081115340046 |
| V13 | @giabartram (10.4K) | 2024-12-10 | 13 s | 5.1M | 415.2K | 2.6K | 3.0K | 13.6K | 0.27% | non | US | Audio : « Does anybody else think their acne looks better in the morning? » | Story-time relatable | https://www.tiktok.com/@giabartram/video/7446794933886946606 |
| V14 | @erin.wilsonnnn (212.7K) | 2026-01-27 | 9 s | 3.7M | 492.7K | 396 | 9.3K | 16.9K | 0.46% | non | GB | « My skin on a Friday night: » (légende « Hormonal acne for you ») | Relatable hormonal | https://www.tiktok.com/@erin.wilsonnnn/video/7599987390656138518 |
| V15 | @doctorhasia (165.9K) | 2025-07-21 | 24 s | 3.5M | 106.3K | 274 | 6.0K | 27.6K | 0.79% | non | AE | Audio : « Forehead acne, dandruff, genetics, and hairstyles… » | Face mapping dermato | https://www.tiktok.com/@doctorhasia/video/7529515174680743190 |
| V16 | @konstanse.20 (1.8K) | 2026-06-20 | 7 s | 3.4M | 530.6K | 14.1K | 4.5K | 11.7K | 0.34% | non | US | « Cleaning your fyp: This is what a regular face looks like » | Vraie peau / jour 2 des règles | https://www.tiktok.com/@konstanse.20/video/7653472684616994078 |
| V17 | @trishabaker (427) | 2025-09-22 | 9 s | 3.1M | 13.2K | 94 | 303 | 1.2K | 0.04% | oui | US | « when someone brings up acne after getting off birth control… » | Âge 30 + pilule (pub) | https://www.tiktok.com/@trishabaker/video/7552957780190137630 |
| V18 | @gina.ugc37 (6.5K) | 2025-03-29 | 6 s | 2.9M | 127.3K | 227 | 6.5K | 55.1K | 1.90% | non | US | « Your Acne Healing Map » (carte du visage) | Face map habitudes | https://www.tiktok.com/@gina.ugc37/video/7487209875731221791 |
| V19 | @wellfromscratch (30.9K) | 2025-11-10 | 9 s | 2.8M | 355.5K | 521 | 3.8K | 29.6K | 1.06% | non | IT | « LAST OCTOBER » (avant) puis aujourd’hui | Avant/maintenant 1 an | https://www.tiktok.com/@wellfromscratch/video/7571164978162584854 |
| V20 | @dewylouie (691.1K) | 2026-07-23 | 64 s | 2.5M | 100.7K | 245 | 754 | 3.7K | 0.15% | oui | US | Audio : « Every time my period comes, my chin breaks out. » | Cycle + menton (pub) | https://www.tiktok.com/@dewylouie/video/7665859829537213726 |
| V21 | @drcharlesmd1 (1.7M) | 2025-08-18 | 54 s | 2.4M | 61.1K | 284 | 1.9K | 33.1K | 1.38% | non | US | « How is this legal??? » / audio « If you have these, take this… » | Stitch dermato qui corrige un hack | https://www.tiktok.com/@drcharlesmd1/video/7540045363256773918 |
| V22 | @drabby6 (572.8K) | 2026-04-08 | 7 s | 2.4M | 93.6K | 344 | 2.6K | 12.0K | 0.50% | non | US | « Advice I give as a dermatologist… if I wasn’t afraid of hurting your feelings » | Vérités de dermato | https://www.tiktok.com/@drabby6/video/7626530935390997790 |
| V23 | @natalie_oneillll (1.1M) | 2025-06-29 | 60 s | 2.1M | 144.4K | 433 | 1.9K | 13.5K | 0.64% | non | GB | Audio : « four sneaky ways I was accidentally giving myself breakouts » | Erreurs cachées | https://www.tiktok.com/@natalie_oneillll/video/7521418237544860950 |
| V24 | @juni.engen.sjogree (8.7K) | 2026-03-11 | 17 s | 2.1M | 43.6K | 128 | 1.4K | 6.2K | 0.29% | oui | NO | « Day 1 » (acide azélaïque, phase lutéale en hashtag) | Jour 1 produit (pub) | https://www.tiktok.com/@juni.engen.sjogree/video/7616037037933595926 |
| V25 | @skincare.w.mare (1.2K) | 2026-08-18 | 6 s | 1.9M | 156.0K | 222 | 1.2K | 22.8K | 1.20% | non | US | « I’ll never forget the girl who told me the secret… » | App Thea (ambassadrice) | https://www.tiktok.com/@skincare.w.mare/video/7675418204306525454 |
| V26 | @sunnyfromsunnybread (550.1K) | 2026-07-03 | 147 s | 1.8M | 121.3K | 682 | 8.2K | 70.2K | 3.90% | non | KR | « Let’s FIX that SKIN Pt.5 Hormonal Acne » | Série éducative lifestyle | https://www.tiktok.com/@sunnyfromsunnybread/video/7658445616095251730 |
| V27 | @teawithmd (788.0K) | 2026-07-24 | 43 s | 1.7M | 115.5K | 1.6K | 15.0K | 85.9K | 5.05% | non | US | « Dermatologist react incoming » / audio « I’ve been waiting for this » | Réaction dermato produits | https://www.tiktok.com/@teawithmd/video/7666109557336247566 |
| V28 | @hannahhrosaliee (67.0K) | 2025-01-07 | 53 s | 1.6M | 117.1K | 609 | 3.5K | 60.0K | 3.75% | non | US | Audio : « I took my skin from this to this in 4 months. » | Avant/après + méthode (iPad) | https://www.tiktok.com/@hannahhrosaliee/video/7457256080431844654 |
| V29 | @heylina2484 (176.8K) | 2026-01-26 | 8 s | 1.6M | 63.9K | 363 | 4.1K | 18.2K | 1.14% | non | KR | « Your Acne Map » (carte du visage) | Face map | https://www.tiktok.com/@heylina2484/video/7599700705250708754 |
| V30 | @gracemayofficial (375.6K) | 2026-08-04 | 45 s | 1.5M | 172.5K | 678 | 4.6K | 5.4K | 0.36% | non | US | « POV: the dermatologist appointment you waited 6 months for » | Sketch coût/attente dermato | https://www.tiktok.com/@gracemayofficial/video/7670006056264682783 |
| V31 | @hiwaste (214.0K) | 2026-05-29 | 18 s | 1.4M | 12.4K | 121 | 355 | 1.5K | 0.11% | oui | KR | « Nobody warned you about THIS 7-day transformation… (Watch till the end) » | Journal 7 jours (pub) | https://www.tiktok.com/@hiwaste/video/7645133446435638560 |
| V32 | @abbeyyung (3.1M) | 2025-10-02 | 9 s | 1.2M | 38.1K | 167 | 1.2K | 10.9K | 0.91% | non | US | « POV: You’re sick of skincare & makeup making you greasy… » | Âge 30 (légende) + produit | https://www.tiktok.com/@abbeyyung/video/7556737542930877726 |
| V33 | @jskintea (3.6K) | 2026-04-10 | 5 s | 1.1M | 110.2K | 255 | 689 | 11.8K | 1.07% | non | US | « how i cleared my acne in a week not a month » | App Skan (ambassadrice) | https://www.tiktok.com/@jskintea/video/7627180150731459870 |
| V34 | @mary.michael12 (8.9K) | 2026-08-19 | 7 s | 1.1M | 99.5K | 1.1K | 918 | 4.8K | 0.44% | non | US | « When my hormonal acne patient finally agrees to spironolactone » | Mème soignante | https://www.tiktok.com/@mary.michael12/video/7675779992034364703 |
| V35 | @bellaskindiaries (3.6K) | 2026-07-26 | 5 s | 996.6K | 190.2K | 412 | 2.5K | 18.1K | 1.82% | non | US | « lock in babe, this clear skin took 1 week not 6 years. » | App Puffin (ambassadrice) | https://www.tiktok.com/@bellaskindiaries/video/7666964577912999199 |
| V36 | @lilyclearskin (976) | 2026-07-28 | 6 s | 892.7K | 84.6K | 944 | 624 | 4.0K | 0.45% | non | US | « remember when you made fun of my acne Bella? » | App Puffin (revanche) | https://www.tiktok.com/@lilyclearskin/video/7667699056461778190 |
| V37 | @beautybybibii (2.8K) | 2026-03-07 | 5 s | 881.8K | 50.0K | 71 | 241 | 5.2K | 0.59% | non | US | « how i cleared my acne in a week not a month » | App Skan (même script) | https://www.tiktok.com/@beautybybibii/video/7614325680599321869 |
| V38 | @skinwithgemma (468) | 2026-08-12 | 6 s | 879.1K | 128.2K | 1.3K | 672 | 3.0K | 0.35% | non | US | « Just payed $102 for 1M views. You were bought. » | App MyGlowApp (méta-accroche) | https://www.tiktok.com/@skinwithgemma/video/7673109828163751181 |
| V39 | @thepcosmentor (1.1M) | 2026-03-23 | 22 s | 853.1K | 19.1K | 309 | 1.7K | 6.1K | 0.72% | non | AU | Audio : « 5 signs your skin is telling you about your PCOS » | Liste SOPK | https://www.tiktok.com/@thepcosmentor/video/7620584290887372053 |
| V40 | @priscillathachh (119.9K) | 2026-08-03 | 9 s | 825.7K | 72.4K | 486 | 2.9K | 3.7K | 0.45% | non | US | « The pain of going from this » (légende : acné hormonale à 30 ans) | Âge 30 + avant/après | https://www.tiktok.com/@priscillathachh/video/7669819240202997022 |
| V41 | @drbarbella (34.5K) | 2026-08-03 | 13 s | 747.5K | 6.8K | 126 | 1.2K | 3.5K | 0.47% | non | CA | « Hormonal acne types that DO NOT respond to skincare… » | Infographie hormones (allégations) | https://www.tiktok.com/@drbarbella/video/7669894007299902727 |
| V42 | @kiki.13521 (44.8K) | 2026-02-17 | 17 s | 707.6K | 53.3K | 279 | 1.4K | 4.6K | 0.65% | non | DE | « BRO, your acne will never go away » (puis app) | App AcneTrack (ambassadrice) | https://www.tiktok.com/@kiki.13521/video/7607823428732669206 |
| V43 | @delaneyskincarequeen (388) | 2026-03-27 | 8 s | 615.5K | 25.4K | 58 | 164 | 4.8K | 0.77% | non | US | « how i cured my hormonal acne in 2 months, not 2 years » | App Thea (ambassadrice) | https://www.tiktok.com/@delaneyskincarequeen/video/7621963780028648717 |
| V44 | @clearskinalexa1 (376) | 2026-08-21 | 8 s | 593.4K | 78.3K | 121 | 2.2K | 3.9K | 0.66% | non | US | « when i say my skin is basically clear but i have acne scars… » | App Thea (#theapartner) | https://www.tiktok.com/@clearskinalexa1/video/7676351087925808398 |
| V45 | @jujugot_uu (115.7K) | 2026-09-22 | 74 s | 515.0K | 9.7K | 271 | 318 | 1.3K | 0.25% | oui | US | « Period!!! » / audio « Period boys, get out! » | Cycle (pub nettoyant) | https://www.tiktok.com/@jujugot_uu/video/7688359792246557966 |
| V46 | @hannahbail3y (139.1K) | 2025-10-28 | 7 s | 434.8K | 22.3K | 79 | 529 | 852 | 0.20% | non | GB | « your reminder it’s normal to have clear skin during your [règles] but… » | Ovulation relatable | https://www.tiktok.com/@hannahbail3y/video/7566339159191850262 |
| V47 | @radiantarely (186) | 2025-09-17 | 11 s | 305.9K | 3.6K | 46 | 189 | 2.9K | 0.93% | oui | US | Réponse à commentaire « plssss what is it » | App Nolla (pub) | https://www.tiktok.com/@radiantarely/video/7550852704604572983 |
| V48 | @eliseshd_ (1.5K) | 2025-02-10 | 6 s | 299.4K | 7.6K | 888 | 284 | 546 | 0.18% | non | AE | « When you’ve had clear skin your entire life and suddenly get acne in your 30s » | Âge 30 + appel à l’aide | https://www.tiktok.com/@eliseshd_/video/7469751732466322690 |
| V49 | @jwalker.aesthetics (41.3K) | 2026-01-25 | 6 s | 268.6K | 4.1K | 68 | 197 | 114 | 0.04% | non | US | « The devil couldn’t reach me so he gave me post birth control acne… » | Pilule + humour | https://www.tiktok.com/@jwalker.aesthetics/video/7599139378572578103 |

### Inferences
- Pour Nacre, **les carrousels sont le format principal à tester en organique** : plus de favoris, et une production facile (selfies, flat-lays, captures d'app).
- **Les vidéos de 6 à 9 s** (texte écran POV ou relatable + son tendance) sont le bon format pour le reach et pour tester des accroches avant de les décliner en carrousel.
- La formule « en X semaines, pas Y années » est très utilisée par les apps concurrentes, mais c'est une allégation de résultat. Nacre doit la reformuler en promesse de méthode, par exemple « 12 semaines pour tenir une routine, pas 12 produits au hasard ».

### Gaps
- Je n'ai pas de transcription audio complète. Les accroches 0-3 s sont reconstituées à partir du texte écran, de la couverture et des métadonnées du son.
- Les vidéos ont été sélectionnées par recherche : l'échantillon n'est pas représentatif de tout TikTok.

## 6. Comment les apps acné et skin utilisent les slideshows pour générer des téléchargements

### Takeaway
Trois schémas reviennent :
1. **Le récit « selfie → écran d'analyse → routine → selfie après → page App Store »**, porté par des personas ou des ambassadrices. On le voit chez Adermio, AcneTrack et Thea. Les versions payées dépassent 1M vues ; les versions organiques font généralement de 40K à 330K, avec une exception à 1,2M (kiki.13521, AcneTrack).
2. **Le mème binaire illustré par IA** (« Acne / No acne ») avec l'app révélée en dernière slide (Lumé, AcneTrack). Il apporte beaucoup de reach mais peu de favoris.
3. **Le contenu purement utile** (carte du visage, éducatif), avec l'app uniquement dans la bio ou en filigrane (glowhubdaily → getskinroutine.com, Glamly). C'est ce schéma qui obtient le plus de vues : 24,1M et 20,4M.

Les wordings de CTA sont simples et sans lien : « It's called "AcneTrack" on the App Store », « I tested this AI for free on Adermio », « The App is called GlassAI », « Its free rn! », « JOIN THE WAITLIST ».

### Cited Findings
**AcneTrack (Bsr Labs)**
- **Compte officiel** (@acnetrack_app, 2,9K abonnés) : mème IA en 4 slides (« Acne on forehead / No acne », « Acne on jawline / No acne »…). L'app apparaît seulement en S4, avec « This app is the best to clear your acne », « It's called "AcneTrack" on the App Store » et une capture de la fiche App Store. 1,5M vues, 0,26 % de favoris — [Source](https://www.tiktok.com/@acnetrack_app/photo/7527713138083466526).
- **Ambassadrice @kiki.13521** (44,8K abonnés), version « la photo envoyée » : 1,2M vues, légende « @AcneTrack App » — [Source](https://www.tiktok.com/@kiki.13521/photo/7608626660803448086).
  - S1 : selfie « the photo i sent ».
  - S2 : écran de résultat, « the results I got ».
  - S3 : écran de routine, « this app even builds a custom routine based on your skin ».
  - S4 : selfie « my skin 3 months later ».
  - S5 : fiche App Store, « I use this app!! It's called Acnetrack ».
- **Allégations affichées dans l'interface** (slide S2 ci-dessus) : « Main acne cause Hormon. », « Clear skin in 178 days », « Clear up to 89% of your acne », « Acne score 22/100 » — même source.
- **Version « l'app au milieu »** : S1 « "Acne is hormonal, you can't do anything about it" » ; S2 « My skin 5 months later » ; S3 à S5 conseils (aliments anti-inflammatoires, SPF, routine adaptée) ; S6 et S7 écrans de l'app ; S8 conseil sur les serviettes. 74,5K vues — [Source](https://www.tiktok.com/@kiki.13521/photo/7614205405337570582).
- **Autres :** vidéo de la même ambassadrice « BRO, your acne will never go away », 707,6K — [Source](https://www.tiktok.com/@kiki.13521/video/7607823428732669206). Micro-compte dont la bio dit « AcneTrack found my trigger », 63,1K — [Source](https://www.tiktok.com/@elle_skincarejrny/photo/7663699527194496277).

**Adermio (IA dermatologique, FR)**
- **Template identique en EN, FR et IT** sur des comptes « persona ». Les bios disent « I help you take care of your skin ✨ The dermatological AI… » ou « Je vous aide à prendre soin de votre peau ✨ » et renvoient vers adermio.com.
  - S1 : selfie avec acné, « the photo i sent ».
  - S2 : écran de diagnostic, « the result i got » (Inflammatory Acne, Moderate, zones Cheeks • Jawline • Chin, Score 92 %).
  - S3 : routine matin/soir/hebdo avec Avène, The Ordinary, La Roche-Posay, INKEY, « this AI even builds a custom routine based on your skin ».
  - S4 : radar et texte d'expert, « a detailed acne analysis + how to actually treat it ».
  - S5 : selfie « my skin 6 months later ».
  - S6 : écran d'accueil, « I tested this AI for free on Adermio », « Accuracy 98.5% », « ~30 sec », bouton « Start Analysis ».
- **Versions et chiffres :**
  - @mia.srxx, isAd, 2,0M — [Source](https://www.tiktok.com/@mia.srxx/photo/7600029357171576096) ;
  - @elisa_mthx (FR, « la photo que j'ai prise y'a 3 mois »), isAd, 1,6M — [Source](https://www.tiktok.com/@elisa_mthx/photo/7626042137511202071) ;
  - compte officiel @adermio_, isAd, 1,0M, légende « Analyse ta peau gratuitement et en 30 sec avec Adermio » — [Source](https://www.tiktok.com/@adermio_/photo/7598278605809929494) ;
  - @stella.dlx (IT), 198,1K — [Source](https://www.tiktok.com/@stella.dlx/photo/7684249697422183712).
- **Mêmes selfies sous deux identités.** Les carrousels FR (@elisa_mthx) et IT (@stella.dlx) utilisent exactement les mêmes selfies (t-shirt bleu, voiture en haut jaune), sous deux prénoms différents. C'est un signal de personas fabriquées — [FR](https://www.tiktok.com/@elisa_mthx/photo/7626042137511202071), [IT](https://www.tiktok.com/@stella.dlx/photo/7684249697422183712).
- **Variante « And you're gonna fail »** (×4 en gros plan), puis « And then you win. », puis analyse et routine. 182,5K — [Source](https://www.tiktok.com/@mia.srxx/photo/7641225703043648800).

**Thea**
- **Ambassadrices** dont la bio indique « thea ambassador ».
- **« Products I used to solve… » :**
  - S1 : collage avant/après par problème (acné, cicatrices, filaments sébacés).
  - S2 à S5 : captures des fiches produits Thea (« Good Match », bouton « Buy »), en surimpression « I used Curology's custom formula… helped clear up my hormonal acne », « Pro tip: I use Thea to research products… ».
  - Légende : « I healed my skin with Thea! ».
  - 430,3K vues — [Source](https://www.tiktok.com/@clearskinemily/photo/7490302216369196319).
- **App citée seulement dans la légende** : 3 selfies (« when people see me with clear skin & think I don't know ball.. » → « trust me.. » → « i. know. ball »), légende « thank u to the thea app for clearing my skin ». 51,6K — [Source](https://www.tiktok.com/@clearskinalyssa/photo/7556390331189611790).
- **Comparatif** « Yuka vs Thea app » : 118,9K — [Source](https://www.tiktok.com/@clearskinemily/photo/7492171761610394911).
- **Vidéos :** 1,9M — [Source](https://www.tiktok.com/@skincare.w.mare/video/7675418204306525454) ; « in 2 months, not 2 years », 615,5K — [Source](https://www.tiktok.com/@delaneyskincarequeen/video/7621963780028648717) ; #theapartner, 593,4K — [Source](https://www.tiktok.com/@clearskinalexa1/video/7676351087925808398).

**Skan (AI Skincare)**
- **« The best skincare app >>> »** (isAd), 285,4K — [Source](https://www.tiktok.com/@glowupgirlies8/photo/7415661659764624645) :
  - S1 : fond esthétique en mosaïque rose, « The best skincare app >>> ».
  - S2 : en-tête de la fiche App Store, « This 🥰 ».
  - S3 : question d'onboarding (« You can put your skin type, concerns »).
  - S4 : scores du scan, « It instantly analyzes your skin ».
  - S5 et S6 : correspondance produits et ingrédients.
  - S7 : suivi des progrès, « It also helps you accurately track your skins progress! ».
  - Légende : « Its free rn! ». La bio du compte renvoie vers l'App Store de Skan.
- **Autres :** compte nommé « Skan AI Analyzer App », « Struggling with acne? », 139,7K — [Source](https://www.tiktok.com/@skincare.luvr4/photo/7418756357131717930). Vidéos au script dupliqué « in a week not a month », 1,1M et 881,8K (voir section 5).

**Glass AI**
- Créateur masculin, 24,1K abonnés, 251,1K vues. Légende : « Search on the app store for Glass: AI Skincare & Acne Scan » — [Source](https://www.tiktok.com/@sirisano/photo/7395677479567887662).
  - S1 : « AI saved me from Acne… ».
  - S2 : « I couldn't find the right products for me.. ».
  - S3 : onboarding, « My friend recommended me this app.. It asked me about my skin ».
  - S4 : selfie de scan, « It analyzed my skin with AI ».
  - S5 : scores et routine avec prix, « The App is called GlassAI ».
  - S6 : « Now I have clear skin for life ».

**Lumé Skin**
- Compte officiel, mème anime IA « No Acne / Acne ». L'app est en S5 : « Uses the Lumé Skin App » / « Doesn't use ». 7,6M vues, 19,8K partages, 0,37 % de favoris — [Source](https://www.tiktok.com/@lume.37/photo/7536196645587848466).

**GlassGlow (pré-lancement, liste d'attente : le cas le plus proche de Nacre)**
- 5 slides typographiques sur fond crème. 509K vues mais 192 favoris (0,04 %) et 1,7K likes. Légende « Your skin has a cycle… glassglow.app » — [Source](https://www.tiktok.com/@glassglowapp/photo/7621512327224904982).
  - S1 : « 63% of women notice worse skin before their period ». Aucune source n'est citée sur la slide.
  - S2 : « It's not your routine failing you. ».
  - S3 : « It's your hormones. ».
  - S4 : « Tracking your glow reveals the pattern. ».
  - S5 : logo, « See your skin cycle. Plan around it. », « JOIN THE WAITLIST ».

**Nolla**
- Ambassadrice (bio « nolla derm ambassador ») : S1 « the product that took my skin from this: » → S2 « to this: » → S3 écran de routine sur téléphone, « thank you nolla acne app ». 43K — [Source](https://www.tiktok.com/@skinnbysummer/photo/7550463488183848222).
- Vidéos payées : 5,5M — [Source](https://www.tiktok.com/@lindyskindiaries/video/7623631081115340046) ; 305,9K — [Source](https://www.tiktok.com/@radiantarely/video/7550852704604572983).

**Apps citées seulement en bio ou en filigrane**
- **getskinroutine.com :** @glowhubdaily, cartes du visage à 24,1M et 20,4M — [Source](https://www.tiktok.com/@glowhubdaily/photo/7560799878457150742).
- **Glamly :** @her.soft.glow1 (bio « I use Glamly app to glow up ») ; carte zones/aliments en 5 slides, 1,6M, avec seulement le filigrane du compte — [Source](https://www.tiktok.com/@her.soft.glow1/photo/7659906394920848647).
- **Lumi :** une slide « Ranking products for skin barrier », 383,7K, 1,92 % de favoris ; bio lumiskin.app/download/tiktok — [Source](https://www.tiktok.com/@lumiskin.app/photo/7644656006508580116).
- **Cleyra (compagnon Accutane) :** éducatif design, 655K — [Source](https://www.tiktok.com/@cleyra.app/photo/7587283290646760734) ; 300,9K — [Source](https://www.tiktok.com/@cleyra.app/photo/7586850500780248351). Légendes sans CTA.
- **Dr.Acne :** une illustration « DEEP ACNE NODULE », 86,1K, 79 favoris — [Source](https://www.tiktok.com/@dracneapp/photo/7555651429512269067).
- **SkinSort :** bio « the app i use is @SkinSort », 38K — [Source](https://www.tiktok.com/@miri_ngiri/photo/7534571547906854199).

**Puffin et MyGlowApp (vidéos seulement)**
- Puffin : « lock in babe… » 996,6K — [Source](https://www.tiktok.com/@bellaskindiaries/video/7666964577912999199). « remember when you made fun of my acne Bella? » 892,7K — [Source](https://www.tiktok.com/@lilyclearskin/video/7667699056461778190).
- MyGlowApp : méta-accroche « Just payed $102 for 1M views. You were bought. », 879,1K — [Source](https://www.tiktok.com/@skinwithgemma/video/7673109828163751181).

**Synthèse de la position de l'app dans le carrousel** (à partir des fiches ci-dessus)

| Position de l'app | Exemples |
|---|---|
| Slide 1 | Skan « The best skincare app >>> » ; Glass « AI saved me… » ; Adermio, implicitement, par « the photo i sent » |
| Milieu | Thea S2 à S5 ; AcneTrack (kiki, version « hormonal ») S6 et S7 ; Adermio S2 à S4 |
| Dernière slide | AcneTrack officiel S4 ; Lumé S5 ; GlassGlow S5 ; Nolla S3 ; Adermio S6 (bouton CTA) ; kiki S5 (App Store) |
| Légende ou bio seulement | glowhubdaily, her.soft.glow1, clearskinalyssa, Lumi, Cleyra |

### Inferences
- **Le format « selfie → écran → routine → selfie après → store » est devenu un standard concurrentiel.** Les écrans d'analyse y apportent la preuve visuelle, et la routine en marques de pharmacie (Avène, LRP, CeraVe, The Ordinary) rassure. Nacre a exactement ces assets : routine multi-marques par budget, selfie hebdomadaire, cycle optionnel. Il faut retirer les scores de précision, les « clear skin in X days » et les pourcentages de disparition.
- **Le cas GlassGlow sert d'avertissement direct pour Nacre.** Une app pré-lancement sur le cycle, en typographie seule, obtient du reach (509K) mais quasiment zéro favori ni like. Le visuel peau réelle (selfie, menton) manque, tout comme la valeur actionnable.
- **Les plus gros volumes pour une app viennent de contenus utiles non brandés**, avec l'app en bio (24M). Il faut donc un compte « média » (carte du visage, routines) en plus du compte de marque.
- **Personas aux photos dupliquées et allégations chiffrées :** ce sont les pratiques des concurrents que Nacre doit éviter pour rester crédible et conforme. Les visages IA doivent être étiquetés « Image virtuelle ».

### Gaps
- Je n'ai trouvé aucun carrousel ni aucune vidéo identifiable pour **MochiSkin, BeautyDecoded, Klear et Skinely**. Les handles testés pour Puffin, Thea, Glamly et Lumé (puffin.app, theaskincare, glamly.app, lumeskin.app) ne renvoient pas de compte sous ces noms (relevé JSON vide).
- Les téléchargements attribuables à chaque publication ne sont pas observables. Le lien entre vues et installations n'est pas mesurable de l'extérieur.
- Je n'ai pas pu vérifier le caractère rémunéré des ambassadrices au-delà des bios (« ambassador ») et des hashtags (#theapartner).

## 7. Dix templates de carrousels que Nacre pourrait produire (plans slide par slide, en français, conformes)

### Takeaway
Les 10 plans ci-dessous transposent les archétypes et accroches gagnants (sections 2 à 6) au positionnement de Nacre : acné adulte, plan de 12 semaines, routine matin/soir multi-marques par budget, selfie hebdomadaire, cycle optionnel.

Garde-fous appliqués à tous les plans :
- aucune promesse de guérison ni de délai (« peau nette en X jours ») ;
- pas de « ton acné » ni de « tes boutons » dans la version publicitaire (Spark ad) : utiliser le « je » ou le « elle » ;
- tout visage généré par IA est marqué « Image virtuelle » sur la slide ;
- mention « ne remplace pas un avis médical » quand on parle d'hormones ;
- Nacre n'est pas un dispositif médical.

### Cited Findings
Chaque template cite la source du format qu'il adapte. Les chiffres sont ceux des sections précédentes.
- T1 adapte la carte du visage : [glowhubdaily 24,1M](https://www.tiktok.com/@glowhubdaily/photo/7560799878457150742).
- T2 adapte le conseil non sollicité : [edreiglow 3,6M](https://www.tiktok.com/@edreiglow/photo/7621349821672197389), [alexmorleyx 1,2M](https://www.tiktok.com/@alexmorleyx/photo/7327437129871543584).
- T3 adapte la notation x/10 : [tkgrace0 7,7M](https://www.tiktok.com/@tkgrace0/photo/7524689650481401119), [elumiex 8,5M](https://www.tiktok.com/@elumiex/photo/7453086703767588118).
- T4 adapte la chronologie : [glowjournalmamata 6,8M](https://www.tiktok.com/@glowjournalmamata/photo/7449577681324100871), [laura.ckrm 2,9M](https://www.tiktok.com/@laura.ckrm/photo/7623523423888657696).
- T5 adapte cycle + menton : [cocoonskinco](https://www.tiktok.com/@cocoonskinco/photo/7447279524724641030), [francesca](https://www.tiktok.com/@francesca__aagostinelli/photo/7499952719914962222).
- T6 adapte la routine par type et par budget : [pureskincareoficial 2,9M, 4,05 %](https://www.tiktok.com/@pureskincareoficial/photo/7627592324448668948), [hannah_brot « Drogerie »](https://www.tiktok.com/@hannah_brot/photo/7625309246850075937).
- T7 adapte les signes : [acnefromatoz 1,7M](https://www.tiktok.com/@acnefromatoz/photo/7343223970587495712).
- T8 adapte la photo envoyée (app) : [kiki.13521 1,2M](https://www.tiktok.com/@kiki.13521/photo/7608626660803448086), [mia.srxx 2,0M isAd](https://www.tiktok.com/@mia.srxx/photo/7600029357171576096).
- T9 adapte le binaire illustré : [lume.37 7,6M](https://www.tiktok.com/@lume.37/photo/7536196645587848466).
- T10 adapte relatable / affirmation : [kathrynsgrwms 3,2M](https://www.tiktok.com/@kathrynsgrwms/photo/7581976256736955662), [only1aliya 3,1M](https://www.tiktok.com/@only1aliya/photo/7546703055484472607).
- Le guide long et détaillé ([natalie_oneillll 2,89 %](https://www.tiktok.com/@natalie_oneillll/photo/7623844761480269078), [danakim 5,21 %](https://www.tiktok.com/@danakim_82992/photo/7672998737383279903)) inspire la structure « plan en étapes » de T6 et T8.

### Inferences
**T1. « Menton, mâchoire, front : ce que chaque zone peut refléter »**
- Archétype : FACEMAP. Objectif : reach et partages.
- Style : illustration beige uniforme, une zone rougie par slide, filigrane Nacre.

| Slide | Contenu |
|---|---|
| S1 | « Ce que tes boutons essaient de te dire (version adulte) » + visage illustré |
| S2 | Front : sommeil, stress, cheveux/produits capillaires, frange |
| S3 | Joues : téléphone, taie d'oreiller, maquillage, mains |
| S4 | Autour de la bouche : baume ou dentifrice, frottements du masque |
| S5 | Menton et mâchoire : « souvent cité en lien avec le cycle chez l'adulte* » |
| S6 | Cou et dos : sueur, cheveux, sac à dos |
| S7 | « Le vrai test : noter OÙ et QUAND, pendant plusieurs semaines » |
| S8 | « C'est ce que fait Nacre : un selfie par semaine + cycle (optionnel) » |

- *Astérisque à afficher : « Repères généraux, pas un diagnostic. »
- À ne pas faire : aucune mention d'organe (foie, cœur…).

**T2. « Ce qu'on m'a conseillé contre mes boutons à 27 ans »**
- Archétype : conseil non sollicité. Objectif : reach + commentaires.

| Slide | Contenu |
|---|---|
| S1 | « "Bois plus d'eau" » sur un selfie |
| S2 | « "Arrête le sucre" » |
| S3 | « "Lave-toi le visage" » |
| S4 | « "Reprends la pilule" » |
| S5 | « "C'est l'âge, ça passera" » |
| S6 | « Ce qui m'a vraiment aidée : UNE routine simple, tenue 12 semaines » |
| S7 | Matin / soir en 3 produits |
| S8 | « + une photo par semaine pour voir l'évolution réelle » |
| S9 | Nacre |

- Selfies réels ou visage IA étiqueté « Image virtuelle ».

**T3. « J'ai noté tout ce que j'ai acheté contre mes boutons (et combien ça m'a coûté) »**
- Archétype : RANKED et argent. Objectif : favoris.
- Style : flat-lay sur drap blanc, note x/10 dans un cartouche blanc, prix en €.

| Slide | Contenu |
|---|---|
| S1 | « 7 ans d'acné adulte, 1 tiroir plein : je note tout » |
| S2 à S8 | Un produit par slide : note, prix, verdict honnête en 10 mots |
| S9 | « Total : XXX € » |
| S10 | « Ce que j'aurais dû faire : une routine par budget, et la garder » |
| S11 | Nacre (routines 15 / 30 / 60 €) |

- Garde-fous : pas de dénigrement nominatif agressif de marques ; noter « pour ma peau ».

**T4. « Semaine 1 → semaine 12 : je montre tout, même les rechutes »**
- Archétype : JOURNEY. Objectif : reach + confiance.

| Slide | Contenu |
|---|---|
| S1 | « Semaine 1 » (selfie, lumière identique) |
| S2 à S12 | Une semaine par slide, une note courte (ex. « S6 : poussée avant les règles ») |
| S13 | « Ce que j'ai appris : la régularité > les produits miracles » |

- Pas de promesse : écrire « mon évolution », jamais « résultat garanti ».
- Pour les Spark ads, utiliser un témoignage réel et consenti, et vérifier la politique avant/après de TikTok.

**T5. « Mon menton suit mon calendrier ? »**
- Archétype : CYCLE + MENTON. Objectif : favoris + différenciation.
- Style : gros plans du menton (réels ou « Image virtuelle ») + mini-calendrier.

| Slide | Contenu |
|---|---|
| S1 | « Je ne fais des boutons qu'autour du menton… et toujours la même semaine » |
| S2 | J-7 |
| S3 | J-3 |
| S4 | J1 |
| S5 | J+7 |
| S6 | « Je ne savais pas si c'était lié, alors j'ai noté pendant 3 cycles » |
| S7 | Écran Nacre : selfie hebdo + cycle (optionnel) |
| S8 | « À montrer à ton médecin ou dermato si ça se répète » |

- Pas de statistique non sourcée en S1 (contre-exemple : le « 63 % » de GlassGlow).

**T6. « Ma routine acné adulte pour 15 €, 30 € ou 60 € »**
- Archétype : ROUTINE + argent. Objectif : favoris.
- Style : produits alignés sur fond uni, nom sous chaque produit (style pureskincareoficial).

| Slide | Contenu |
|---|---|
| S1 | « Routine boutons adulte : 3 budgets, que des produits de pharmacie » |
| S2 | Matin 15 € |
| S3 | Soir 15 € |
| S4 | Matin 30 € |
| S5 | Soir 30 € |
| S6 | Matin 60 € |
| S7 | Soir 60 € |
| S8 | « Les erreurs qui gâchent n'importe quel budget » |
| S9 | « Nacre te propose la tienne selon ta peau et ton budget » |

**T7. « 6 signes que ce n'est plus "l'acné d'ado" »**
- Archétype : EDU-HORMONAL. Objectif : favoris.
- Style : design aplat de couleur Nacre + photo.

| Slide | Contenu |
|---|---|
| S1 | Titre |
| S2 | Apparue ou revenue après 25 ans |
| S3 | Surtout bas du visage |
| S4 | Boutons profonds et douloureux |
| S5 | Rythme régulier (cycle) |
| S6 | Résiste aux produits « anti-boutons » classiques |
| S7 | Laisse des marques |
| S8 | « Ce sont des repères fréquemment décrits, pas un diagnostic : parles-en à un professionnel » |
| S9 | Nacre pour suivre et préparer le rendez-vous |

- Formulation prudente obligatoire : « souvent », « peut ».

**T8. « La photo de ma semaine 1 »**
- Archétype : APP-UI. Objectif : téléchargements (organique et Spark ad).

| Slide | Contenu |
|---|---|
| S1 | Selfie « la photo de ma semaine 1 » |
| S2 | Écran Nacre : plan 12 semaines |
| S3 | Écran routine matin/soir (marques de pharmacie, budget affiché) |
| S4 | Écran rappel selfie + cycle optionnel |
| S5 | Selfie « semaine 8 », sans filtre |
| S6 | « L'app s'appelle Nacre » + fiche store ou liste d'attente |

- Interdits, contrairement à AcneTrack et Adermio : pas de score de précision, pas de « clear skin in X days », pas de pourcentage d'amélioration.
- Version publicitaire à la première personne, sans « ton acné ».

**T9. « Elle change de crème chaque semaine / Elle tient 12 semaines »**
- Archétype : binaire illustré. Objectif : reach top-funnel.
- Style : illustration IA étiquetée « Image virtuelle », écran partagé.

| Slide | Contenu |
|---|---|
| S1 à S4 | Comparaisons (10 produits contre 3 ; dort maquillée contre se démaquille ; zéro photo contre une photo par semaine ; panique avant les règles contre anticipation) |
| S5 | « Celle qui utilise Nacre » |

- Attendu : peu de favoris (cf. Lumé, 0,37 %). À réserver à la notoriété.

**T10. « "Pourquoi tu laisses toujours tes cheveux détachés ?" »**
- Archétype : RELATABLE. Objectif : reach et communauté.

| Slide | Contenu |
|---|---|
| S1 | La question, sur selfie cheveux détachés |
| S2 | Selfie cheveux attachés, acné visible, sans texte |
| S3 (option, variante mot à mot) | « ta / peau / ne / dit / pas / qui / tu / es » |

- Légende : témoignage sur l'acné adulte. Pas de CTA app, ou alors CTA en bio seulement.

**Recommandations transverses** (inférences tirées des sections 1 à 6) :
- viser 8 à 13 slides pour les formats « utiles » (T3, T6, T7) ;
- 2 à 3 slides pour les formats émotionnels (T10) ;
- l'app en dernière slide ou en bio, jamais en slide 1 en organique ;
- tester chaque accroche d'abord en vidéo de 6 à 9 s ;
- un son tendance réutilisé par les gros comptes du format (ex. « Manchild » pour les cartes du visage) peut aider ;
- pour les Spark ads, partir des posts organiques qui ont le meilleur taux de favoris.

### Gaps
- Je n'ai pas vérifié la politique publicitaire de TikTok et de Meta sur les avant/après et les attributs personnels pour la catégorie « soin de la peau / acné » : à vérifier avant toute diffusion payante.
- Je n'ai pas de statistique sourcée et fiable sur « acné prémenstruelle chez les femmes adultes » qui soit utilisable en slide 1. Il faudra en trouver une dans la littérature avant d'utiliser T5 avec un chiffre.
- Les performances attendues de ces templates sont extrapolées de comptes anglophones et hispanophones. Le comportement de l'audience française 25-35 ans n'est pas mesuré ici.
