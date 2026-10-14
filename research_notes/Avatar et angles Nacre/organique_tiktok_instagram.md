# Organique TikTok / Instagram — formats, accroches et créateurs (acné adulte) + playbooks d'apps à abonnement

> Notes de recherche — collecte du 2026-10-01. Complète (sans dupliquer) le premier scan TikTok du 2026-09-30 (98 publications, 38 créateurs, 88 hashtags, sans vues ni accroches).
>
> **Méthode propre à cette note (faits observés)** :
> - Statistiques des vidéos TikTok (vues, likes, commentaires, partages, favoris, durée, abonnés de l'auteur, drapeau `isAd`) lues le 2026-10-01 dans le JSON public embarqué des pages vidéo (`__UNIVERSAL_DATA_FOR_REHYDRATION__`). 84 des 98 publications du premier scan + 14 publications photo récupérées via l'URL `/video/` + 20 publications supplémentaires trouvées par recherche web = **118 publications avec chiffres**.
> - Accroches : transcription automatique TikTok (sous-titres ASR « whisper », 5 premières secondes) = **audio**, pas le texte à l'écran. Erreurs ASR possibles (ex. « procès » pour « poussée », « corou » pour Koru). Les publications photo et vidéos musicales n'ont pas d'ASR : la légende est donnée à la place.
> - Volumes de hashtags : compteurs **cumulés mondiaux, toutes périodes** (publications + vues) lus via l'endpoint public `m.tiktok.com/api/challenge/detail` le 2026-10-01. **Pas de filtre France, pas de fenêtre 30/120 jours.**
> - Google Trends : séries hebdomadaires 5 ans (2021-10 → 2026-10) via l'API publique de trends.google.com le 2026-10-01 ; valeurs **relatives à l'intérieur de chaque lot de 5 mots-clés** (0-100). Un lot France sur l'acné a été bloqué (HTTP 429).
> - Abonnés Instagram : balise `og:description` publique des profils (2026-10-01).
> - Drapeau `isAd = true` (12 publications) : publication marquée publicitaire/boostée par TikTok (Spark Ads ou contenu de marque promu). Ces vues ne sont **pas** de l'organique pur.
> - Données brutes : `vids98.json`, `vids_ext.json`, `users.json`, `users2.json`, `hashtags_tt.json` dans le scratchpad de session (C:/Users/loysc/AppData/Local/Temp/claude/C--Users-loysc-Desktop-Marketing-Nacre/f235f64f-b782-4ad8-83ab-4da2b23c437b/scratchpad/).

## 1. Quels formats de contenu acné performent le mieux, avec quels chiffres ?

### Takeaway
Sur TikTok, les plus gros volumes acné viennent (a) du **vécu filmé sans filtre** (GRWM en pleine poussée, « update de ma peau », témoignage d'âge « j'ai 28/30 ans et de l'acné »), (b) des **listes éducatives « à enregistrer »** (cartographie des boutons, « packaging moche = produit efficace ») qui génèrent les meilleurs taux de favoris, et (c) des **avant/après en mode photo** postés par de micro-comptes (jusqu'à 4 000× leur nombre d'abonnés). En France, le thème « boutons avant les règles » est déjà massivement occupé par la campagne payante Ducray Keracnyl. Les vidéos longues (> 60 s) ont la médiane de vues la plus élevée de l'échantillon.

### Cited Findings

**Référence académique (international)**
- Étude AJD 2025 sur les 150 premières vidéos #acne (septembre 2023, 2 Md de vues cumulées) : éducatif 34 % des vidéos / 324 M vues ; transformations (avant/après) 24 % / 440 M ; pimple popping 17 % / 804 M (88 K partages, engagement le plus fort) ; positivité acné 13 % / 160 M ; « réalité / fardeau » 11 % / 79 M. 11 % seulement des vidéos postées par des cliniciens ; ~14 % promeuvent explicitement un produit (dont isotrétinoïne). — [Dermatology Times, 3 mars 2025, résumant Iyengar et al., Australas J Dermatol 2025](https://www.dermatologytimes.com/view/acne-and-tiktok-what-do-dermatologists-need-to-know-)
- Créateurs acné : le pimple popping fait grossir très vite des comptes (ex. @alexpops47 de 4 000 à 86 000 abonnés en un mois ; @_alliechen 264 000 abonnés), et les créatrices décrivent une pression algorithmique à continuer de montrer leur acné même une fois la peau améliorée. — [Dazed, 24 juin 2026](https://www.dazeddigital.com/beauty/article/70510/1/i-went-viral-for-acne-content-then-my-pimples-disappeared-skin-influencer-tiktok)

**Statistiques agrégées de l'échantillon (118 publications, collecte 2026-10-01 ; échantillon non aléatoire issu des recherches du premier scan + recherches ciblées ; ER = (likes+comm.+partages+favoris)/vues)**
- Tout l'échantillon : médiane 101,6 K vues ; ER médian 5,9 % ; favoris médians 0,67 % des vues ; partages 0,12 %. — [Données : tableau en fin de section, URLs TikTok individuelles]
- Vidéos > 60 s : médiane 143,4 K vues (n=37) ; 21-60 s : 97,0 K (n=31) ; ≤ 20 s : 51,3 K (n=36) mais moyenne tirée par quelques méga-hits (moyenne 1,2 M). — [idem]
- Mode photo (carrousel TikTok, n=14) : médiane 73,2 K vues, ER 4,1 %, favoris 0,79 % ; vidéo (n=104) : médiane 105,7 K, ER 6,0 %. — [idem]
- Publications audio en français (n=57) : médiane 109,3 K vues, **favoris médians 1,15 %** (vs 0,67 % pour tout l'échantillon). — [idem]
- Publications `isAd` (n=12) : médiane 422,4 K vues mais ER 2,4 % et favoris 0,19 % → signature d'une diffusion payée ; à exclure des benchmarks organiques. — [idem]
- Comptes < 10 K abonnés (n=41) : médiane 28,8 K vues ; comptes ≥ 100 K (n=41) : médiane 413,2 K. — [idem]

**Exemples concrets par format (chiffres au 2026-10-01)**

*GRWM avec acné / sans maquillage*
- @erinnoelleh — GRWM en pleine poussée, **357 s**, 18,7 M vues, 1,6 M likes, 35,8 K commentaires, 20,3 K partages, 62,6 K favoris (27/04/2025, compte 221 K). La vidéo la plus vue de l'échantillon, et l'une des plus longues. — [TikTok](https://www.tiktok.com/@erinnoelleh/video/7498015564615437599)
- @laviniarusanda — GRWM d'école sans maquillage, 700,1 K vues (2024). — [TikTok](https://www.tiktok.com/@laviniarusanda/video/7330347878272994565)
- FR : @lolatagliaferroo — « pov j'ai un bouton qui m'est sorti dans la nuit » (GRWM, 142 s), 143,4 K vues, 3,5 K favoris. — [TikTok](https://www.tiktok.com/@lolatagliaferroo/video/7494602172278050070)
- Contre-exemple : @thatkaitysmith (296,6 K abonnés), GRWM naturel avec patchs, 12,9 K vues seulement. — [TikTok](https://www.tiktok.com/@thatkaitysmith/video/7659960100102114591)

*« Update de ma peau » / skin check-in / journal*
- FR : @oceanepedrosa_ — « Update de ma peau… 24 ans et je continue de me battre » (119 s), 614,1 K vues, 65,2 K likes, 740 comm., 1,6 K favoris (24/09/2026 ; compte 91,9 K → 6,7× ses abonnés). — [TikTok](https://www.tiktok.com/@oceanepedrosa_/video/7689148085674577185)
- FR : @almasch_ — « Il y a 1 an ma peau ressemblait à ça, aujourd'hui… » (102 s), 296,3 K vues, 11,3 K favoris (compte 22,2 K). — [TikTok](https://www.tiktok.com/@almasch_/video/7590733807192378646)
- @laviniarusanda — « day 1 of Arazlo… documenter tout le parcours » (réponse à un commentaire), 214,8 K vues. — [TikTok](https://www.tiktok.com/@laviniarusanda/video/7393046199034465542)
- Le label « skin diary » est quasi inutilisé : #skindiary = 952 publications / 2,3 M vues cumulées ; #acneupdate = 973 / 32,7 M ; #skinupdate = 14,3 K / 328,7 M. — [TikTok #skindiary](https://www.tiktok.com/tag/skindiary) ; [#acneupdate](https://www.tiktok.com/tag/acneupdate)

*Avant/après — mode photo (micro-comptes)*
- @lana.hpny — carrousel 7 images « Et vous pensez que c'est impossible ? #acne #transformation », **3,7 M vues** avec 872 abonnés (4 243× ses abonnés), 86,6 K likes, 10,1 K favoris (22/03/2026). — [TikTok](https://www.tiktok.com/@lana.hpny/photo/7620160093228715286)
- @nellssskincare — carrousel 7 images, 2,7 M vues, 2 285 abonnés (21/07/2026). — [TikTok](https://www.tiktok.com/@nellssskincare/photo/7664944526817119506)
- FR : @sarah.hym — « Avant / après en 6 mois sur mon acné », 1,2 M vues, 368 abonnés (04/04/2026) ; repérée dans la recherche « app acné » du premier scan. — [TikTok](https://www.tiktok.com/@sarah.hym/photo/7624844858896796950)
- FR : @skinglowbyp — « J'ai essayé tous les produits anti acné et ça n'a fait que décaper ma peau », 261,6 K vues, 7,0 K favoris, 1 257 abonnés. — [TikTok](https://www.tiktok.com/@skinglowbyp/photo/7623100146267491606)
- @isabellapmayer — carrousel 8 images #adultacne, 494,8 K vues. — [TikTok](https://www.tiktok.com/@isabellapmayer/photo/7537060844580965654)

*Listes éducatives « enregistre »*
- FR : @myssyjym — cartographie « bouton sur la joue → change ta taie d'oreiller… » (20 s), **7,7 M vues, 514,3 K likes, 86,4 K partages, 254,9 K favoris** (12/03/2026) — la vidéo FR la plus vue et la plus sauvegardée de l'échantillon. NB : le « face mapping » est une interprétation non validée médicalement. — [TikTok](https://www.tiktok.com/@myssyjym/video/7616408279551462678)
- FR : @skincarebysamy — « Packaging moche = produit efficace » (60 s), 877 K vues, 55,8 K favoris (**6,4 % des vues**), 6,4 K partages. — [TikTok](https://www.tiktok.com/@skincarebysamy/video/7650181872038841632)
- FR : @askcalvin_ — « Si t'as de l'acné sur ces parties du visage… » + nom de l'app AcneTrack, 1,0 M vues, 11,9 K favoris. — [TikTok](https://www.tiktok.com/@askcalvin_/video/7552675674654280982)
- FR : @nuniverse__ — « Ta routine ado en 3 produits PAS PLUS », 698,8 K vues, ER 19,2 %, 27,3 K favoris (compte 36,1 K ; cible ado, hors cœur Nacre). — [TikTok](https://www.tiktok.com/@nuniverse__/video/7663242067157552417)

*Sélections pharmacie / parapharmacie*
- FR : @francesca.skincare — « mes produits acné safe préférés en parapharmacie partie 1 », 62,8 K vues, 1,7 K favoris (compte 35,7 K). — [TikTok](https://www.tiktok.com/@francesca.skincare/video/7642374408232783126)
- UK : @sparklesandskin — « Top drugstore acne treatments at Boots », 35,2 K vues (compte 133,3 K). — [TikTok](https://www.tiktok.com/@sparklesandskin/video/7574786041152851203)
- Francophone : @mireilleskincare1 — crèmes anti-taches « vendues en pharmacie », 560 K vues (isAd). — [TikTok](https://www.tiktok.com/@mireilleskincare1/video/7617873273090592022)

*Réaction / duo / stitch d'expert*
- @dermarkologist (dermatologue, 1,2 M abonnés) — duo réagissant à « routine pour clear mon acné en 6 mois », 936,5 K vues, 19 K favoris. — [TikTok](https://www.tiktok.com/@dermarkologist/video/7348039310555335982)
- FR : @skincarebysamy — « cette fille a de l'acné sévère et je réagis à sa routine », 221,2 K vues (2023). — [TikTok](https://www.tiktok.com/@skincarebysamy/video/7290958203851001120)
- @drabby6 (dermatologue) — « on peut être une excellente dermato même avec de l'acné », 593,9 K vues. — [TikTok](https://www.tiktok.com/@drabby6/video/7537830682697960735)

*Story-time / témoignage (âge, pilule, SOPK, Roaccutane)*
- FR : @plurielmedia — interview d'Océane (acné, SOPK, confiance), 417,3 K vues, 172 s. — [TikTok](https://www.tiktok.com/@plurielmedia/video/7607903545056251139)
- FR : @leazlook — « j'ai 30 ans, j'ai de l'acné et je reviens de chez le dermato », 266,5 K vues, 2,1 K favoris. — [TikTok](https://www.tiktok.com/@leazlook/video/7447218196161039638)
- FR : @elo.mzr — acné à 28 ans depuis l'arrêt de la pilule en 2023, 71,8 K vues. — [TikTok](https://www.tiktok.com/@elo.mzr/video/7676124722442046752)
- FR : @laulevy — SOPK, 3 mois sous spironolactone (réponse à un commentaire), 133,5 K vues, 351 comm. — [TikTok](https://www.tiktok.com/@laulevy/video/7532536183356771606)
- @courtneyjones5252 — « Before I started Accutane », 10,2 M vues (2023, 8 s). — [TikTok](https://www.tiktok.com/@courtneyjones5252/video/7296915573307378977)

*Demande d'aide / vulnérabilité (machine à commentaires)*
- FR : @celeste111555 — « celles qui s'en sont sorties comment ??? je vous en supplie », 406,2 K vues, **3 348 commentaires (0,82 % des vues, ratio le plus élevé de l'échantillon)**. — [TikTok](https://www.tiktok.com/@celeste111555/video/7645760032977521952)
- FR : @oceanepedrosa_ — stress d'une visite d'appart « pas crédible à cause de ma peau », 185 K vues. — [TikTok](https://www.tiktok.com/@oceanepedrosa_/video/7686533237509803297)
- FR : @reb.szw — ne plus se filmer à cause de son acné, 24,2 K vues, 175 comm. (compte 7,8 K). — [TikTok](https://www.tiktok.com/@reb.szw/video/7551055476453182722)

*Réponse à un commentaire*
- FR : @oceanepedrosa_ — « Réponse à @Kl Beauty » routine du matin, 102,1 K vues, 2,4 K favoris. — [TikTok](https://www.tiktok.com/@oceanepedrosa_/video/7664646494439460129)

*Mythe / contre-pied*
- FR : @celialetteri (nutri-thérapeute, 4 628 abonnés) — « l'acné hormonale ça n'existe pas », 114,7 K vues (25× ses abonnés). — [TikTok](https://www.tiktok.com/@celialetteri/video/7618266469335305494)
- FR : @francesca.skincare — « Je me lave pas le visage le matin », 30,4 K vues. — [TikTok](https://www.tiktok.com/@francesca.skincare/video/7613450444047748374)
- @ericanic0le — « la pilule n'est qu'un pansement pour l'acné », 161,2 K vues (2023). — [TikTok](https://www.tiktok.com/@ericanic0le/video/7191154979082767662)

*Cycle / boutons avant les règles*
- @lifewithmils — « si tu fais ce genre de poussée la semaine avant tes règles… », 387,5 K vues, 11,1 K favoris. — [TikTok](https://www.tiktok.com/@lifewithmils/video/7599392455837977877)
- @mvp_macrae — « Why? » / « Does this happen to anyone else », 293,8 K vues (7 s). — [TikTok](https://www.tiktok.com/@mvp_macrae/video/7393033121223970078)
- FR : @marieaimee013 — « Et chaque mois en plus » (8 s), 154,1 K vues avec 7 032 abonnés. — [TikTok](https://www.tiktok.com/@marieaimee013/video/7689143632875588882)
- FR : @lfvrmorgane — boutons selon les phases du cycle, 27,6 K vues. — [TikTok](https://www.tiktok.com/@lfvrmorgane/video/7434275236075375905)
- FR, campagne Ducray Keracnyl (publications `isAd`) : @maelle.ugc 3,3 M vues (1 988 abonnés ; ER 0,4 %) ; @thecleanjunky 3,0 M (ER 0,2 %) ; @_kayyh 2,9 M (ER 0,5 %) ; @myssyjym 85,6 K ; @skincarebysamy 89,6 K ; @amoudaxtiktok 15,9 K ; @pharmaciegaresevran 21,2 K. Hashtag de campagne observé : #balanceyourcyclicacne. — [@maelle.ugc](https://www.tiktok.com/@maelle.ugc/video/7521430392935664918) ; [@thecleanjunky](https://www.tiktok.com/@thecleanjunky/video/7615305310303014166) ; [@_kayyh](https://www.tiktok.com/@_kayyh/video/7614223938238909729) ; [@myssyjym](https://www.tiktok.com/@myssyjym/video/7619419067622968598)

*Promotion d'apps acné par comptes « ambassadeurs » (voir §6)*
- @kiki.13521 — « They told me to cleanse my skin, and I did it using the AcneTrack app », **10,8 M vues**, 461,5 K likes, 33,7 K favoris (19 s, musique, sans voix ; bio : compte secondaire « main @qxnn190 »). — [TikTok](https://www.tiktok.com/@kiki.13521/video/7627904891175832864)
- @alyssaskincarequeen (bio « thea ambassador », 2 349 abonnés) — 533,1 K vues. — [TikTok](https://www.tiktok.com/@alyssaskincarequeen/video/7634036334503496990)
- @ellaclearskin (bio « I 💟 the puffin acne app », 591 abonnés) — 488,9 K vues. — [TikTok](https://www.tiktok.com/@ellaclearskin/video/7667327392385355021)
- FR : @clearskinfrance (6 432 abonnés) — « Envoi « Skin » en DM pour avoir le nom de la crème », 1,3 M vues, 14,4 K favoris (funnel par mot-clé en DM ; lien bio beacons.ai/acneboy). — [TikTok](https://www.tiktok.com/@clearskinfrance/video/7623120066569145622)

**Tableau complet — 118 publications avec chiffres (collecte 2026-10-01)**

\* ER = (likes + commentaires + partages + favoris) / vues. \*\* `isAd` = publication marquée publicitaire/boostée par TikTok.

| # | Vues | Likes | Comm. | Partages | Favoris | ER* | Créateur (abonnés) | Date | Format | Spark/Ad** | Langue audio | Légende (extrait) | URL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 18.7M | 1.6M | 35.8K | 20.3K | 62.6K | 9.2% | @erinnoelleh (221.0K) | 2025-04-27 | Vidéo 357s | non | eng-US | GRWM ! 💗🧡 s/o to anyone that makes to the | https://www.tiktok.com/@erinnoelleh/video/7498015564615437599 |
| 2 | 10.8M | 461.5K | 1757 | 7610 | 33.7K | 4.7% | @kiki.13521 (44.8K) | 2026-04-12 | Vidéo 19s | non | n/d | They told me to cleanse my skin, and I did | https://www.tiktok.com/@kiki.13521/video/7627904891175832864 |
| 3 | 10.2M | 433.1K | 5198 | 5483 | 17.0K | 4.5% | @courtneyjones5252 (951.0K) | 2023-11-02 | Vidéo 8s | non | n/d | Before I started Accutane💖 #accutanejourney #acne #acneskin #acnefighter #acnejourney | https://www.tiktok.com/@courtneyjones5252/video/7296915573307378977 |
| 4 | 7.7M | 514.3K | 2428 | 86.4K | 254.9K | 11.1% | @myssyjym (922.7K) | 2026-03-12 | Vidéo 20s | non | fra-FR | Si tu as une poussée de boutons sur une zone | https://www.tiktok.com/@myssyjym/video/7616408279551462678 |
| 5 | 5.5M | 33.7K | 196 | 1095 | 5223 | 0.7% | @heylina2484 (176.8K) | 2026-05-29 | Vidéo 14s | oui | eng-US | As long as I have my azelaic acid, I’m not | https://www.tiktok.com/@heylina2484/video/7645343692257070344 |
| 6 | 3.7M | 86.6K | 194 | 4158 | 10.1K | 2.7% | @lana.hpny (872) | 2026-03-22 | Photo (7 img) | non | n/d | Et vous pensez que c’est impossible ? #acne #transformation | https://www.tiktok.com/@lana.hpny/photo/7620160093228715286 |
| 7 | 3.3M | 10.4K | 98 | 328 | 1669 | 0.4% | @maelle.ugc (1988) | 2025-06-29 | Vidéo 18s | oui | fra-FR | Les boutons juste avant les règles ? J’en avais marre | https://www.tiktok.com/@maelle.ugc/video/7521430392935664918 |
| 8 | 3.0M | 3756 | 9 | 219 | 841 | 0.2% | @thecleanjunky (22.5K) | 2026-03-09 | Vidéo 56s | oui | fra-FR | Mon meilleur ami pour mon acné hormonal 🤝 Découvert en | https://www.tiktok.com/@thecleanjunky/video/7615305310303014166 |
| 9 | 2.9M | 11.8K | 24 | 211 | 1334 | 0.5% | @_kayyh (373.5K) | 2026-03-06 | Vidéo 46s | oui | fra-FR | L’acné hormonale avant les règles… on en parle ? 🥲 | https://www.tiktok.com/@_kayyh/video/7614223938238909729 |
| 10 | 2.7M | 49.0K | 302 | 6350 | 4749 | 2.2% | @nellssskincare (2285) | 2026-07-21 | Photo (7 img) | non | n/d | #skincare #foryou #viral | https://www.tiktok.com/@nellssskincare/photo/7664944526817119506 |
| 11 | 1.6M | 143.0K | 2494 | 1814 | 4911 | 9.5% | @alexandre.lln_ (150.3K) | 2026-03-02 | Vidéo 13s | non | n/d | tête de oim dans 3 mois j’ai plus rien #fyp | https://www.tiktok.com/@alexandre.lln_/video/7612718502503271702 |
| 12 | 1.6M | 98.6K | 402 | 2684 | 11.0K | 7.0% | @chiii._sommm (1.0M) | 2026-04-14 | Vidéo 96s | oui | eng-US | This is how I cured my hormonal acne 💁🏻‍♀️@DERMATURM | https://www.tiktok.com/@chiii._sommm/video/7628646180724968711 |
| 13 | 1.3M | 42.8K | 1147 | 2936 | 14.4K | 4.7% | @clearskinfrance (6432) | 2026-03-30 | Vidéo 48s | non | fra-FR | Envoi « Skin » En DM pour avoir le nom | https://www.tiktok.com/@clearskinfrance/video/7623120066569145622 |
| 14 | 1.2M | 27.5K | 45 | 990 | 2794 | 2.6% | @sarah.hym (368) | 2026-04-04 | Photo (7 img) | non | n/d | Avant / après en 6 mois sur mon acné🙏🏼 #acne | https://www.tiktok.com/@sarah.hym/photo/7624844858896796950 |
| 15 | 1.0M | 39.9K | 374 | 2805 | 11.9K | 5.5% | @askcalvin_ (162.0K) | 2025-09-21 | Vidéo 50s | non | fra-FR | Est ce que t’as de l’acné sur ses parties du | https://www.tiktok.com/@askcalvin_/video/7552675674654280982 |
| 16 | 936.5K | 64.8K | 135 | 1019 | 19.0K | 9.1% | @dermarkologist (1.2M) | 2024-03-19 | Vidéo 60s | non | eng-US | #duet with @justin derm reacts: skincare routine I used to | https://www.tiktok.com/@dermarkologist/video/7348039310555335982 |
| 17 | 930.5K | 18.4K | 285 | 1124 | 1685 | 2.3% | @dr.farzan (2.0M) | 2023-03-12 | Vidéo 8s | non | n/d | If you’re getting acne on chin/ jawline once a month | https://www.tiktok.com/@dr.farzan/video/7209676576504433926 |
| 18 | 877.0K | 63.2K | 361 | 6382 | 55.8K | 14.3% | @skincarebysamy (1.1M) | 2026-06-11 | Vidéo 60s | non | fra-FR | PACKAGING MOCHE = PRODUIT EFFICACE ✅ Liste des produits cités | https://www.tiktok.com/@skincarebysamy/video/7650181872038841632 |
| 19 | 744.3K | 49.9K | 1108 | 4154 | 1648 | 7.6% | @emmsskin (7384) | 2026-09-12 | Vidéo 14s | non | n/d | There’s something so liberating about sharing your biggest insecurity and | https://www.tiktok.com/@emmsskin/video/7684591248535063830 |
| 20 | 700.1K | 39.0K | 163 | 60 | 1296 | 5.8% | @laviniarusanda (493.3K) | 2024-01-31 | Vidéo 190s | non | eng-US | Never feel pressured to wear makeup or cover your skin! | https://www.tiktok.com/@laviniarusanda/video/7330347878272994565 |
| 21 | 699.4K | 91.0K | 223 | 1196 | 10.7K | 14.7% | @erinnoelleh (221.0K) | 2026-08-31 | Vidéo 114s | non | eng-US | My nightly skincare routine (if I do it lol) #acnetransformation | https://www.tiktok.com/@erinnoelleh/video/7680002379323919647 |
| 22 | 698.8K | 100.8K | 1739 | 4510 | 27.3K | 19.2% | @nuniverse__ (36.1K) | 2026-07-16 | Vidéo 36s | non | fra-FR | Ta routine ado en 3 produits PAS PLUS 💛 🌅 | https://www.tiktok.com/@nuniverse__/video/7663242067157552417 |
| 23 | 615.3K | 45.6K | 374 | 5200 | 16.4K | 11.0% | @askcalvin_ (162.0K) | 2026-07-17 | Vidéo 77s | non | fra-FR | Cette expérience sur la crème solaire va te choquer #acnetrack | https://www.tiktok.com/@askcalvin_/video/7663572684718050593 |
| 24 | 614.1K | 65.2K | 740 | 726 | 1638 | 11.1% | @oceanepedrosa_ (91.9K) | 2026-09-24 | Vidéo 119s | non | fra-FR | Update de ma peau de mon acné archi difficile ce | https://www.tiktok.com/@oceanepedrosa_/video/7689148085674577185 |
| 25 | 593.9K | 58.0K | 756 | 576 | 1909 | 10.3% | @drabby6 (572.8K) | 2025-08-12 | Vidéo 64s | non | fra-FR | I don’t know who needs to hear this but you | https://www.tiktok.com/@drabby6/video/7537830682697960735 |
| 26 | 586.8K | 15.5K | 470 | 1308 | 5451 | 3.9% | @elsbellusskincare (1.0M) | 2024-08-29 | Vidéo 112s | non | fra-FR | Pour avoir une consultation réservez vos places en cliquant sur | https://www.tiktok.com/@elsbellusskincare/video/7408608295004556576 |
| 27 | 560.0K | 17.5K | 251 | 6924 | 8085 | 5.9% | @mireilleskincare1 (927.7K) | 2026-03-16 | Vidéo 111s | oui | fra-FR | Meilleurs crème visage anti tache vendu en pharmacie | https://www.tiktok.com/@mireilleskincare1/video/7617873273090592022 |
| 28 | 533.1K | 42.4K | 15 | 238 | 4913 | 8.9% | @alyssaskincarequeen (2348) | 2026-04-29 | Vidéo 5s | non | n/d | for my acne prone girlies, it’s called thea <3 #theaapp | https://www.tiktok.com/@alyssaskincarequeen/video/7634036334503496990 |
| 29 | 494.8K | 40.5K | 132 | 281 | 1213 | 8.5% | @isabellapmayer (241.6K) | 2025-08-10 | Photo (8 img) | non | n/d | #acne #acnejourney #skinjourney #adultacne | https://www.tiktok.com/@isabellapmayer/photo/7537060844580965654 |
| 30 | 488.9K | 63.0K | 342 | 722 | 8069 | 14.8% | @ellaclearskin (591) | 2026-07-27 | Vidéo 5s | non | n/d | the puffin acne app saveeed me. #clearskin #acnetips #acnetreatment #healthyskintips | https://www.tiktok.com/@ellaclearskin/video/7667327392385355021 |
| 31 | 417.3K | 39.9K | 178 | 578 | 2179 | 10.3% | @plurielmedia (1.4M) | 2026-02-17 | Vidéo 172s | non | fra-FR | Océane souffre d’acné. Elle nous raconte son parcours contre la | https://www.tiktok.com/@plurielmedia/video/7607903545056251139 |
| 32 | 413.5K | 22.8K | 203 | 843 | 6903 | 7.4% | @doristenara (258.1K) | 2021-11-24 | Vidéo 15s | non | n/d | À prendre avant l’ovulation et avant le début des règles | https://www.tiktok.com/@doristenara/video/7034271960179723525 |
| 33 | 413.2K | 13.8K | 97 | 1420 | 10.2K | 6.2% | @skincarebysamy (1.1M) | 2024-07-15 | Vidéo 27s | non | fra-FR | ⚠️ ACNÉ DANS LE DOS ET SUR LE TORSE : | https://www.tiktok.com/@skincarebysamy/video/7391917959201049888 |
| 34 | 406.2K | 31.8K | 3348 | 381 | 1844 | 9.2% | @celeste111555 (212.9K) | 2026-05-30 | Vidéo 23s | non | n/d | je m’affiche tellment mais celles qui s’en sont sorties comment | https://www.tiktok.com/@celeste111555/video/7645760032977521952 |
| 35 | 387.5K | 18.3K | 91 | 813 | 11.1K | 7.8% | @lifewithmils (363.7K) | 2026-01-25 | Vidéo 56s | non | eng-US | how to STOP PRE-period BREAKOUTS!🩸 1️⃣ dandelion tea 2️⃣ castor | https://www.tiktok.com/@lifewithmils/video/7599392455837977877 |
| 36 | 296.3K | 22.1K | 141 | 931 | 11.3K | 11.6% | @almasch_ (22.2K) | 2026-01-02 | Vidéo 102s | non | fra-FR | Évidemment chaque peaux est différente, et les produits sont juste | https://www.tiktok.com/@almasch_/video/7590733807192378646 |
| 37 | 296.1K | 22.2K | 94 | 403 | 1498 | 8.2% | @kiki.13521 (44.8K) | 2026-01-24 | Vidéo 13s | non | n/d | thanks to the @AcneTrack App 🤞🏽❤️ #clearskin #acnegirl #acnefighter #AcnetrackApp | https://www.tiktok.com/@kiki.13521/video/7598925439729503510 |
| 38 | 293.8K | 13.0K | 80 | 1059 | 1046 | 5.2% | @mvp_macrae (50.4K) | 2024-07-18 | Vidéo 7s | non | eng-US | Does this happen to anyone else #acne #acneskin #hormonalacne #period | https://www.tiktok.com/@mvp_macrae/video/7393033121223970078 |
| 39 | 291.9K | 25.8K | 339 | 1996 | 14.4K | 14.6% | @nuniverse__ (36.1K) | 2026-06-29 | Vidéo 51s | non | fra-FR | La méthode de ma mère pour calmer l’acné 🇰🇷 Quand | https://www.tiktok.com/@nuniverse__/video/7656916200198278432 |
| 40 | 284.8K | 614 | 40 | 81 | 234 | 0.3% | @mochi_skin.app (378) | 2026-07-24 | Vidéo 34s | oui | fra-FR | Si toi aussi tu en a marre d’acheter des produits | https://www.tiktok.com/@mochi_skin.app/video/7666034979381546272 |
| 41 | 274.3K | 4118 | 149 | 332 | 1838 | 2.3% | @dr.prasanthi (80.4K) | 2023-05-26 | Vidéo 168s | non | fra-FR | How to manage post pill acne? How do you stop | https://www.tiktok.com/@dr.prasanthi/video/7237425763761294600 |
| 42 | 266.5K | 5871 | 318 | 269 | 2057 | 3.2% | @leazlook (163.1K) | 2024-12-11 | Vidéo 107s | non | fra-FR | ma routine naturelle pour l’acné féminin ❤️‍🩹 #acneadulte #acné #acnéhormonal | https://www.tiktok.com/@leazlook/video/7447218196161039638 |
| 43 | 261.6K | 6892 | 117 | 594 | 6964 | 5.6% | @skinglowbyp (1257) | 2026-03-30 | Photo (7 img) | non | n/d | J’ai essayé tous les produits anti acné et ça n’a | https://www.tiktok.com/@skinglowbyp/photo/7623100146267491606 |
| 44 | 231.0K | 3565 | 40 | 922 | 1141 | 2.5% | @skinwithlisa (11.7K) | 2026-04-21 | Vidéo 7s | non | n/d | 1️⃣ Skincare alone won’t fix your skin. If anyone tells | https://www.tiktok.com/@skinwithlisa/video/7631155310366854421 |
| 45 | 228.5K | 8943 | 35 | 281 | 7949 | 7.5% | @louisefcd (94.9K) | 2025-10-29 | Vidéo 112s | oui | fra-FR | Ma routine hyper simple qui m’a rendu la peau PARFAITE | https://www.tiktok.com/@louisefcd/video/7566690528700484886 |
| 46 | 221.2K | 14.5K | 35 | 43 | 836 | 7.0% | @skincarebysamy (1.1M) | 2023-10-17 | Vidéo 29s | non | fra-FR | ✅ Pour cette routine anti-acné très simple je mets un | https://www.tiktok.com/@skincarebysamy/video/7290958203851001120 |
| 47 | 214.8K | 3666 | 172 | 123 | 625 | 2.1% | @laviniarusanda (493.3K) | 2024-07-18 | Vidéo 169s | non | eng-US | Replying to @brookealexandrah day 1 of arazlo! Gonna document the | https://www.tiktok.com/@laviniarusanda/video/7393046199034465542 |
| 48 | 185.0K | 15.2K | 77 | 136 | 261 | 8.5% | @oceanepedrosa_ (91.9K) | 2026-09-17 | Vidéo 30s | non | fra-FR | Dites moi que je pas la seule❤️‍🩹 #acneprone #acneproneskin #acnefighter | https://www.tiktok.com/@oceanepedrosa_/video/7686533237509803297 |
| 49 | 177.3K | 6611 | 21 | 50 | 550 | 4.1% | @___oraane (875.0K) | 2024-06-16 | Vidéo 65s | oui | fra-FR | @Koru-your acne coach, l’application qui va t’aider à embellir ta | https://www.tiktok.com/@___oraane/video/7381099647244225825 |
| 50 | 164.6K | 15.4K | 206 | 229 | 676 | 10.0% | @nora_journey (12.8K) | 2025-01-03 | Vidéo 38s | non | n/d | Toujours en projet clear skin 2025…..💀 Je bloque les com | https://www.tiktok.com/@nora_journey/video/7455663294360210710 |
| 51 | 161.2K | 2927 | 70 | 175 | 297 | 2.2% | @ericanic0le (335.4K) | 2023-01-21 | Vidéo 61s | non | eng-US | In my experience, going on birth control was one of | https://www.tiktok.com/@ericanic0le/video/7191154979082767662 |
| 52 | 154.1K | 18.2K | 172 | 420 | 339 | 12.4% | @marieaimee013 (7032) | 2026-09-24 | Vidéo 8s | non | n/d | Et chaque mois en plus💔#fypシ゚viralシ #jeveuxpasserdanstespourtoi #periode | https://www.tiktok.com/@marieaimee013/video/7689143632875588882 |
| 53 | 144.8K | 13.4K | 88 | 94 | 2798 | 11.3% | @oceanepedrosa_ (91.9K) | 2026-07-29 | Vidéo 143s | non | fra-FR | Si demain j’ai une grosse rechute d’acné c’est la routine | https://www.tiktok.com/@oceanepedrosa_/video/7667979148509351201 |
| 54 | 143.4K | 7508 | 46 | 231 | 3462 | 7.8% | @lolatagliaferroo (55.4K) | 2025-04-18 | Vidéo 142s | non | fra-FR | pov j’ai un bouton qui m’est sorti dans la nuit👁️ | https://www.tiktok.com/@lolatagliaferroo/video/7494602172278050070 |
| 55 | 133.5K | 4117 | 351 | 387 | 2079 | 5.2% | @laulevy (361.5K) | 2025-07-29 | Vidéo 246s | non | fra-FR | Réponse à @Mel2411 SOPK : mon expérience après 3 mois | https://www.tiktok.com/@laulevy/video/7532536183356771606 |
| 56 | 132.3K | 9804 | 47 | 633 | 5973 | 12.4% | @glowup.withjuju1 (289.8K) | 2025-08-31 | Photo (7 img) | non | n/d | #astucetiktok #foryoupage #tik_tok #videoviral #fyp | https://www.tiktok.com/@glowup.withjuju1/photo/7544849731772517637 |
| 57 | 114.7K | 4817 | 89 | 560 | 2626 | 7.1% | @celialetteri (4628) | 2026-03-17 | Vidéo 81s | non | fra-FR | #acné #acnetips #sopk #acneadulte #syndromedesovairespolykystiques | https://www.tiktok.com/@celialetteri/video/7618266469335305494 |
| 58 | 109.3K | 5145 | 52 | 190 | 1258 | 6.1% | @rojii.ely (632.2K) | 2026-04-18 | Vidéo 65s | non | fra-FR | Des petits complexes qui arrivent à gâcher la confiance en | https://www.tiktok.com/@rojii.ely/video/7630191339900112150 |
| 59 | 102.1K | 6442 | 54 | 97 | 2419 | 8.8% | @oceanepedrosa_ (91.9K) | 2026-07-20 | Vidéo 69s | non | fra-FR | Réponse à @Kl Beauty Routine skincare du matin pour ma | https://www.tiktok.com/@oceanepedrosa_/video/7664646494439460129 |
| 60 | 101.1K | 8038 | 53 | 249 | 735 | 9.0% | @mayly_lb (3690) | 2026-09-13 | Vidéo 7s | non | n/d | et c’est ok girly | https://www.tiktok.com/@mayly_lb/video/7685126361014357280 |
| 61 | 97.0K | 6034 | 41 | 465 | 4374 | 11.3% | @doristenara (258.1K) | 2026-09-03 | Vidéo 40s | non | fra-FR | 3 mois pour ce beau résultat 🥹 après une première | https://www.tiktok.com/@doristenara/video/7681350485692960032 |
| 62 | 96.6K | 3616 | 78 | 34 | 2086 | 6.0% | @almasch_ (22.2K) | 2024-02-27 | Photo (8 img) | non | n/d | Et oui ta peau a besoin d’etre hydratée et non | https://www.tiktok.com/@almasch_/photo/7340344115965562145 |
| 63 | 90.5K | 1233 | 21 | 64 | 329 | 1.8% | @morganepaul_naturopathe (1847) | 2024-08-16 | Vidéo 14s | non | fra-FR | Acné avant les règles ? Ton ovulation n'est pas optimale | https://www.tiktok.com/@morganepaul_naturopathe/video/7403664540405157153 |
| 64 | 89.6K | 3273 | 44 | 305 | 1495 | 5.7% | @skincarebysamy (1.1M) | 2025-05-24 | Vidéo 54s | non | fra-FR | ✅🧪 RÈGLES ET BOUTONS, VOICI COMMENT CA FONCTIONNE ! lpubIiciteI | https://www.tiktok.com/@skincarebysamy/video/7508105916164607254 |
| 65 | 88.7K | 3515 | 79 | 122 | 3587 | 8.2% | @francesca.skincare (35.7K) | 2026-05-11 | Vidéo 49s | non | fra-FR | ⭐️ Je vous mets toutes les refs dans la description: | https://www.tiktok.com/@francesca.skincare/video/7638658649929354518 |
| 66 | 85.6K | 4607 | 31 | 319 | 2294 | 8.5% | @myssyjym (922.7K) | 2026-03-20 | Vidéo 100s | non | fra-FR | publicité @Ducray / l’acné hormonale c’est délicat mais pas impossible | https://www.tiktok.com/@myssyjym/video/7619419067622968598 |
| 67 | 81.1K | 1703 | 14 | 1 | 108 | 2.3% | @leazlook (163.1K) | 2026-09-15 | Vidéo 87s | non | fra-FR | à 32 ans, j’apprends enfin à prendre soin de ma | https://www.tiktok.com/@leazlook/video/7685806725718347041 |
| 68 | 79.1K | 2182 | 273 | 188 | 107 | 3.5% | @emmsskin (7384) | 2026-08-06 | Vidéo 16s | non | n/d | This has taken so much to post so please be | https://www.tiktok.com/@emmsskin/video/7670908913012739360 |
| 69 | 78.5K | 2920 | 77 | 149 | 1266 | 5.6% | @emturian (142.9K) | 2026-01-02 | Vidéo 71s | non | fra-FR | L’actif le plus prometteur contre l’acné hormonale ? 👀 Un | https://www.tiktok.com/@emturian/video/7590726317583158550 |
| 70 | 76.0K | 3594 | 38 | 77 | 801 | 5.9% | @lola_lp_ (8397) | 2026-01-22 | Vidéo 89s | non | fra-FR | ✨Les causes de l’acné hormonale✨ ➡️ Abonne toi si tu | https://www.tiktok.com/@lola_lp_/video/7598147339034971414 |
| 71 | 71.8K | 5237 | 147 | 88 | 242 | 8.0% | @elo.mzr (241.0K) | 2026-08-20 | Vidéo 104s | non | fra-FR | J’arrive pas à m’en débarrasser c’est un enfer | https://www.tiktok.com/@elo.mzr/video/7676124722442046752 |
| 72 | 62.8K | 2784 | 38 | 58 | 1704 | 7.3% | @francesca.skincare (35.7K) | 2026-05-21 | Vidéo 58s | non | fra-FR | Mes produits préférés acné safe en parapharmacie partie 1 🤍 | https://www.tiktok.com/@francesca.skincare/video/7642374408232783126 |
| 73 | 49.7K | 447 | 3 | 13 | 56 | 1.0% | @sarah.hym (368) | 2026-05-06 | Photo (7 img) | non | n/d | #acne #pourtoi #skincare #glowup | https://www.tiktok.com/@sarah.hym/photo/7636855895653092630 |
| 74 | 47.3K | 1259 | 92 | 159 | 1204 | 5.7% | @dr_bernabeauty (19.6K) | 2026-07-03 | Vidéo 78s | non | fra-FR | Les patientes et patients adultes avec acné! Allez consulter vous | https://www.tiktok.com/@dr_bernabeauty/video/7658351126256897312 |
| 75 | 45.3K | 453 | 41 | 25 | 125 | 1.4% | @clearskinfrance (6432) | 2026-03-31 | Photo (7 img) | non | n/d | L’acné est une affection cutanée extrêmement fréquente qui touche principalement | https://www.tiktok.com/@clearskinfrance/photo/7623445196386209047 |
| 76 | 43.2K | 1261 | 18 | 84 | 283 | 3.8% | @sarahpalmyra (1.2M) | 2023-06-30 | Vidéo 54s | non | eng-US | Can AI give you better skin? #CTilburypartner I learned about | https://www.tiktok.com/@sarahpalmyra/video/7250555370513468718 |
| 77 | 39.1K | 1015 | 30 | 18 | 512 | 4.0% | @lauu.mn15 (4139) | 2026-03-20 | Photo (2 img) | non | n/d | surtout la crème curacnyl #acné #acnéhormonal #acnetips #skincare #acnesolution @Eau | https://www.tiktok.com/@lauu.mn15/photo/7619316933233544470 |
| 78 | 35.2K | 878 | 7 | 61 | 598 | 4.4% | @sparklesandskin (133.3K) | 2025-11-20 | Vidéo 21s | non | eng-US | Top drugstore ✨acne treatments✨ at @Boots UK @The INKEY List | https://www.tiktok.com/@sparklesandskin/video/7574786041152851203 |
| 79 | 32.8K | 964 | 9 | 16 | 771 | 5.4% | @elisa_mthx (1308) | 2026-08-14 | Photo (8 img) | non | n/d | #skincare #acne #routine | https://www.tiktok.com/@elisa_mthx/photo/7673899619063057696 |
| 80 | 30.4K | 1383 | 49 | 23 | 354 | 6.0% | @francesca.skincare (35.7K) | 2026-03-04 | Vidéo 38s | non | fra-FR | ma peau est 10x mieux depuis que je me lave | https://www.tiktok.com/@francesca.skincare/video/7613450444047748374 |
| 81 | 28.8K | 328 | 29 | 17 | 37 | 1.4% | @itsamxnda (6572) | 2025-01-08 | Photo (7 img) | non | n/d | Il me reste des tâches et de temps en temps | https://www.tiktok.com/@itsamxnda/photo/7457506963275025687 |
| 82 | 27.6K | 858 | 16 | 63 | 565 | 5.4% | @lfvrmorgane (56.1K) | 2024-11-06 | Vidéo 67s | non | fra-FR | Pourquoi tu as des boutons selon les phases de ton | https://www.tiktok.com/@lfvrmorgane/video/7434275236075375905 |
| 83 | 24.2K | 1113 | 175 | 33 | 109 | 5.9% | @reb.szw (7752) | 2025-09-17 | Vidéo 166s | non | fra-FR | Je ne filme plus à cause de mon acné ? | https://www.tiktok.com/@reb.szw/video/7551055476453182722 |
| 84 | 23.5K | 46 | 6 | 5 | 26 | 0.4% | @mochi_skin.app (378) | 2026-09-20 | Vidéo 20s | oui | fra-FR | L’app pour enfin venir à bout de tes problèmes de | https://www.tiktok.com/@mochi_skin.app/video/7687626986293923105 |
| 85 | 23.2K | 545 | 17 | 43 | 56 | 2.8% | @nafikne (15.5K) | 2024-09-23 | Vidéo 34s | non | fra-FR | et j’ai la gerbe aussi 😋 #regle #periodsbelike #periodsproblem #regles | https://www.tiktok.com/@nafikne/video/7417745858462108960 |
| 86 | 21.2K | 425 | 3 | 130 | 494 | 5.0% | @pharmaciegaresevran (60.7K) | 2026-04-27 | Vidéo 33s | non | fra-FR | Les boutons qui apparaissent avant les règles… puis les marques | https://www.tiktok.com/@pharmaciegaresevran/video/7633519730036329761 |
| 87 | 16.8K | 314 | 33 | 4 | 73 | 2.5% | @myestytessa (25.0K) | 2025-10-13 | Vidéo 278s | non | eng-US | Replying to @bigfukinplayer hope this helps 🤎 #acnespecialist #closedcomedones #accutane | https://www.tiktok.com/@myestytessa/video/7560850549625670967 |
| 88 | 15.9K | 543 | 9 | 57 | 227 | 5.3% | @amoudaxtiktok (643.3K) | 2026-03-06 | Vidéo 44s | non | fra-FR | Les boutons hormonaux ne sont pas “aléatoires”. Ils suivent une | https://www.tiktok.com/@amoudaxtiktok/video/7614208303295499537 |
| 89 | 12.9K | 247 | 6 | 1 | 4 | 2.0% | @thatkaitysmith (296.6K) | 2026-07-08 | Vidéo 29s | non | eng-US | For some people acne makes them feel the need to | https://www.tiktok.com/@thatkaitysmith/video/7659960100102114591 |
| 90 | 11.3K | 1021 | 14 | 86 | 65 | 10.5% | @kiki.13521 (44.8K) | 2026-09-28 | Vidéo 16s | non | eng-US | Zweifel immernoch lowkey #acne #acnegirl #glowup #clearskin #acnetrack | https://www.tiktok.com/@kiki.13521/video/7690658459372637473 |
| 91 | 10.4K | 755 | 18 | 103 | 113 | 9.5% | @socup.fr (67.8K) | 2026-07-02 | Vidéo 55s | oui | fra-FR | Non, les boutons ne sont pas forcément liés à un | https://www.tiktok.com/@socup.fr/video/7658013336075799841 |
| 92 | 10.3K | 110 | 8 | 15 | 70 | 2.0% | @equilibrist.lab (11.1K) | 2026-03-16 | Vidéo 32s | non | fra-FR | Des boutons qui reviennent chaque mois avant vos règles ? | https://www.tiktok.com/@equilibrist.lab/video/7617879335046810882 |
| 93 | 9865 | 1326 | 25 | 21 | 195 | 15.9% | @elodievan (1572) | 2026-08-26 | Vidéo 85s | non | fra-FR | jour 2/21 : l’acné à 25 ans m’a fait me | https://www.tiktok.com/@elodievan/video/7678348243566169377 |
| 94 | 9539 | 417 | 4 | 12 | 31 | 4.9% | @eva.prea (22.4K) | 2026-03-10 | Vidéo 62s | non | fra-FR | On va tester les pink croissant de chez @Ouity_fr pour | https://www.tiktok.com/@eva.prea/video/7615687979167911190 |
| 95 | 9252 | 318 | 22 | 4 | 25 | 4.0% | @lenaa6390 (1038) | 2026-07-24 | Vidéo 5s | non | n/d | j’en avais besoin 🌞✨ | https://www.tiktok.com/@lenaa6390/video/7666108350974807329 |
| 96 | 9161 | 217 | 7 | 2 | 81 | 3.4% | @louannestoppr (174) | 2025-07-27 | Vidéo 6s | non | n/d | @STOPPR / Stop Sugar App #stoppr #glassskine | https://www.tiktok.com/@louannestoppr/video/7531809180747943190 |
| 97 | 8468 | 488 | 4 | 3 | 9 | 6.0% | @jzozzy (34.3K) | 2026-09-24 | Vidéo 6s | non | n/d | Gotta love hormonal acne!! (Somebody sedate me) #acneskin #hormoneimbalance #acne | https://www.tiktok.com/@jzozzy/video/7689190144162778398 |
| 98 | 7529 | 185 | 4 | 6 | 50 | 3.3% | @justinchungalt (25.1K) | 2026-06-18 | Vidéo 15s | non | n/d | features of my @AcneScore App | https://www.tiktok.com/@justinchungalt/video/7652844957249588511 |
| 99 | 7105 | 354 | 8 | 15 | 19 | 5.6% | @beautycrew.test (10.2K) | 2025-11-14 | Vidéo 14s | oui | fra-FR | Collaboration commerciale – merci @ducray 💙 J’ai testé le sérum | https://www.tiktok.com/@beautycrew.test/video/7572664639436131606 |
| 100 | 6410 | 313 | 2 | 13 | 210 | 8.4% | @adrianaxng (1233) | 2026-08-12 | Photo (9 img) | non | n/d | Ma routine spéciale acné hormonale 🫧🧴 #acnehormonale #skincareroutine | https://www.tiktok.com/@adrianaxng/photo/7673178779404995873 |
| 101 | 6072 | 383 | 6 | 16 | 90 | 8.2% | @femi_glow.ci (31.4K) | 2026-05-22 | Vidéo 98s | non | fra-FR | Boutons avant les règles : ce lien avec tes hormones | https://www.tiktok.com/@femi_glow.ci/video/7642807320660987154 |
| 102 | 5545 | 605 | 7 | 2 | 15 | 11.3% | @jasminnfit (1059) | 2026-09-08 | Vidéo 8s | non | n/d | Thank you AcneX app ❤️ #acne #healing #viral #confident #fyp | https://www.tiktok.com/@jasminnfit/video/7683175525208132886 |
| 103 | 3767 | 89 | 8 | 1 | 8 | 2.8% | @clearskinfrance (6432) | 2026-04-14 | Vidéo 12s | non | n/d | Merci @AcneTrack App pour ma peau lisse ! #acne #acneproneskin | https://www.tiktok.com/@clearskinfrance/video/7628546639430454550 |
| 104 | 2982 | 314 | 1 | 9 | 21 | 11.6% | @skincarebyines (39) | 2026-08-02 | Vidéo 10s | non | n/d | C’est tellement agaçant quand tu sais pas quoi faire, heureusement | https://www.tiktok.com/@skincarebyines/video/7669350098551426336 |
| 105 | 2349 | 77 | 5 | 1 | 6 | 3.8% | @lenaa6390 (1038) | 2026-08-25 | Vidéo 6s | non | n/d | si je l’ai fait tu peux aussi le faire ☺️🤍 | https://www.tiktok.com/@lenaa6390/video/7677981521269034272 |
| 106 | 1887 | 93 | 7 | 5 | 13 | 6.3% | @crownderm (30.2K) | 2026-03-30 | Vidéo 103s | non | eng-US | I’ve been treating acne for 16 years. I’m the one | https://www.tiktok.com/@crownderm/video/7623143899128696086 |
| 107 | 1734 | 64 | 2 | 1 | 14 | 4.7% | @olim.acnetrack (105) | 2026-03-29 | Vidéo 51s | non | fra-FR | Tu connais pas ? 🤓 #acné #conseil #peau #application | https://www.tiktok.com/@olim.acnetrack/video/7622794952157826326 |
| 108 | 1351 | 137 | 46 | 2 | 5 | 14.1% | @minilucette (9436) | 2026-09-30 | Vidéo 15s | non | n/d | Plaisir d’offrir joie de recevoir #acneskin #adultacne | https://www.tiktok.com/@minilucette/video/7691196547526069536 |
| 109 | 1235 | 38 | 5 | 2 | 3 | 3.9% | @alouche.7 (84.2K) | 2026-09-20 | Vidéo 12s | non | n/d | geill #fy #acnetrack @AcneTrack App | https://www.tiktok.com/@alouche.7/video/7687592616665419040 |
| 110 | 1208 | 62 | 7 | 0 | 2 | 5.9% | @jennifer_blt (6387) | 2026-08-24 | Vidéo 22s | non | fra-FR | Je sais plus quoi faire… #acneskin #acnegirl #acneadulte #boutons | https://www.tiktok.com/@jennifer_blt/video/7677487058004217121 |
| 111 | 1099 | 108 | 0 | 0 | 9 | 10.6% | @skincarebyines (39) | 2026-08-13 | Vidéo 9s | non | n/d | Quand elle m’a parlé de cette app au début je | https://www.tiktok.com/@skincarebyines/video/7673533493573422369 |
| 112 | 876 | 45 | 5 | 1 | 6 | 6.5% | @marineecnt (27.2K) | 2026-09-23 | Vidéo 168s | non | fra-FR | L’acné chez l’adulte, la solution qui m’a aidée cet été | https://www.tiktok.com/@marineecnt/video/7688816974670859552 |
| 113 | 872 | 53 | 0 | 0 | 0 | 6.1% | @lisa.hamilton922 (28) | 2026-08-24 | Vidéo 14s | non | n/d | Quand j’ai découvert qu’on pouvait analyser sa routine avec cette | https://www.tiktok.com/@lisa.hamilton922/video/7677533001361804577 |
| 114 | 841 | 134 | 0 | 0 | 1 | 16.1% | @linaskincare__ (378) | 2026-04-05 | Vidéo 14s | non | n/d | Depuis que j’utilise cette app ma peau a complètement changé | https://www.tiktok.com/@linaskincare__/video/7625290977917373719 |
| 115 | 826 | 55 | 10 | 7 | 12 | 10.2% | @mochi_skin.app (378) | 2026-07-14 | Vidéo 25s | non | n/d | On m’a dit qu’il y avait déjà trop d’app de | https://www.tiktok.com/@mochi_skin.app/video/7662411121302752544 |
| 116 | 805 | 105 | 7 | 1 | 1 | 14.2% | @romy_cmbt (3247) | 2026-09-20 | Vidéo 9s | non | n/d | 🙏😔#acne#regles #pourtoii #ilovebeingawoman | https://www.tiktok.com/@romy_cmbt/video/7687706792587021600 |
| 117 | 461 | 13 | 0 | 0 | 6 | 4.1% | @claire3264 (67) | 2026-09-11 | Photo (9 img) | non | n/d | L’app, c’est Skinely pour les intéressées 🤍 Elle analyse ta | https://www.tiktok.com/@claire3264/photo/7684379344189312288 |
| 118 | 351 | 15 | 1 | 0 | 0 | 4.6% | @skincarebyines (39) | 2026-09-05 | Vidéo 13s | non | n/d | Recherche Beautydecoded dans les stores et arrête de te faire | https://www.tiktok.com/@skincarebyines/video/7682072829424045344 |

### Inferences
- Hypothèse : pour Nacre, les formats « vécu daté » (update de peau, semaine X, réponse à commentaire) sont alignés avec le produit (selfie hebdo, plan 12 semaines) ET avec les formats qui performent en FR ; ils évitent l'avant/après-promesse.
- Hypothèse : les vidéos > 60 s ont une médiane plus haute dans l'échantillon (corrélation, pas causalité ; biais : les créateurs établis font des vidéos longues).
- Les très fortes vues avec ER < 1 % (Ducray, MochiSkin, certains posts isAd) indiquent de la diffusion payée : ne pas les prendre comme preuve qu'un format marche organiquement.
- Le taux de favoris (saves) est le meilleur indicateur d'intention dans l'échantillon FR (1,15 % médian, jusqu'à 6,4 % pour @skincarebysamy) ; les formats « liste à enregistrer » sont ceux qui le maximisent.
- Les carrousels photo avant/après de micro-comptes (368 à 2 285 abonnés) qui atteignent 1-3,7 M vues ressemblent au schéma « comptes thématiques » des apps (voir §6) ; leur lien avec une app n'est pas prouvé (texte des slides non collecté).

### Gaps
- Texte à l'écran des 3 premières secondes et texte des slides photo : non collecté (pas d'OCR) — seul l'audio ASR est disponible.
- Aucune métrique post par post Instagram (Reels/carrousels acné) : pages Instagram fermées sans connexion.
- Échantillon non aléatoire (issu de requêtes de recherche + web) : les médianes ne sont pas des benchmarks de marché.
- Durée de visionnage / rétention : non publiques.

## 2. Quelles accroches (3 premières secondes) reviennent dans les vidéos acné les plus vues ?

### Takeaway
Les accroches gagnantes combinent presque toujours **un ciblage par symptôme ou par âge** (« Si t'as… », « J'ai 28 ans et… »), **une preuve visuelle immédiate** (« ma peau il y a 3 jours / aujourd'hui ») ou **un contre-pied** (« l'acné hormonale ça n'existe pas », « packaging moche = efficace »). Le registre « chaque mois c'est pareil » est déjà approprié par Ducray en France.

### Cited Findings

Accroches réelles (audio ASR des 5 premières secondes, ≤ 15 mots, sauf mention « légende ») — vues au 2026-10-01 :

| # | Accroche (citation courte) | Pattern | Créateur | Vues / autres | Source |
|---|---|---|---|---|---|
| 1 | « Get ready with me. Even though I'm having the worst acne flare up again » | GRWM malgré la poussée | @erinnoelleh (EN) | 18,7 M ; 62,6 K favoris | [TikTok](https://www.tiktok.com/@erinnoelleh/video/7498015564615437599) |
| 2 | (légende) « They told me to cleanse my skin, and I did it using the AcneTrack app » | Mème + app | @kiki.13521 (EN) | 10,8 M | [TikTok](https://www.tiktok.com/@kiki.13521/video/7627904891175832864) |
| 3 | (légende) « Before I started Accutane » | Avant traitement | @courtneyjones5252 (EN) | 10,2 M (2023) | [TikTok](https://www.tiktok.com/@courtneyjones5252/video/7296915573307378977) |
| 4 | « rappelle-toi : bouton sur la joue, change ta [taie] d'oreiller » | Liste-mémo | @myssyjym (FR) | 7,7 M ; 254,9 K favoris | [TikTok](https://www.tiktok.com/@myssyjym/video/7616408279551462678) |
| 5 | (légende) « As long as I have my azelaic acid, I'm not scared of pre-period breakouts » | Produit + cycle (isAd) | @heylina2484 (EN) | 5,5 M | [TikTok](https://www.tiktok.com/@heylina2484/video/7645343692257070344) |
| 6 | (légende) « Et vous pensez que c'est impossible ? » | Défi + avant/après photo | @lana.hpny | 3,7 M | [TikTok](https://www.tiktok.com/@lana.hpny/photo/7620160093228715286) |
| 7 | « toi aussi t'as une poussée d'acné juste avant tes règles ? j'ai la solution » | Question cycle (isAd Ducray) | @maelle.ugc (FR) | 3,3 M | [TikTok](https://www.tiktok.com/@maelle.ugc/video/7521430392935664918) |
| 8 | « Tous les mois c'est pareil, je fais des poussées de boutons avant mes règles » | Récurrence mensuelle (isAd Ducray) | @thecleanjunky (FR) | 3,0 M | [TikTok](https://www.tiktok.com/@thecleanjunky/video/7615305310303014166) |
| 9 | « Ça c'était ma peau il y a 3 jours et ça c'est aujourd'hui » | Avant/maintenant (isAd Ducray) | @_kayyh (FR) | 2,9 M | [TikTok](https://www.tiktok.com/@_kayyh/video/7614223938238909729) |
| 10 | (légende) « tête de oim dans 3 mois j'ai plus rien » | Projection / pari | @alexandre.lln_ (FR) | 1,6 M ; ER 9,5 % | [TikTok](https://www.tiktok.com/@alexandre.lln_/video/7612718502503271702) |
| 11 | « let me tell you how I cured my hormonal acne » | « Comment j'ai… » (isAd) | @chiii._sommm (EN) | 1,6 M | [TikTok](https://www.tiktok.com/@chiii._sommm/video/7628646180724968711) |
| 12 | (légende) « Envoi « Skin » en DM pour avoir le nom de la crème » | Mot-clé DM | @clearskinfrance (FR) | 1,3 M ; 14,4 K favoris | [TikTok](https://www.tiktok.com/@clearskinfrance/video/7623120066569145622) |
| 13 | « Si t'as de l'acné sur ces parties du visage… c'est pas au hasard » | « Si t'as… » | @askcalvin_ (FR) | 1,0 M | [TikTok](https://www.tiktok.com/@askcalvin_/video/7552675674654280982) |
| 14 | « Skincare routine I use to clear my acne in six months » → réaction derm | Duo d'expert | @dermarkologist (EN) | 936,5 K | [TikTok](https://www.tiktok.com/@dermarkologist/video/7348039310555335982) |
| 15 | « plus le packaging est moche, plus le produit fonctionne, c'est ma théorie » | Théorie contre-intuitive | @skincarebysamy (FR) | 877 K ; 55,8 K favoris | [TikTok](https://www.tiktok.com/@skincarebysamy/video/7650181872038841632) |
| 16 | « My skin used to look like this. Now it looks like this. » | Avant/maintenant | @erinnoelleh (EN) | 699,4 K | [TikTok](https://www.tiktok.com/@erinnoelleh/video/7680002379323919647) |
| 17 | « si t'as entre 13 et 18 ans, viens je te montre ta skincare » | Ciblage par âge | @nuniverse__ (FR) | 698,8 K ; ER 19,2 % | [TikTok](https://www.tiktok.com/@nuniverse__/video/7663242067157552417) |
| 18 | « si tu utilises de la crème solaire tous les jours… cette étude » | Étude / révélation | @askcalvin_ (FR) | 615,3 K | [TikTok](https://www.tiktok.com/@askcalvin_/video/7663572684718050593) |
| 19 | « 24 ans et tu es encore comme ça » (cite les commentaires) | Âge + update | @oceanepedrosa_ (FR) | 614,1 K ; ER 11,1 % | [TikTok](https://www.tiktok.com/@oceanepedrosa_/video/7689148085674577185) |
| 20 | « 1 produit qui a aidé beaucoup de mes clientes en consultation » | Autorité praticienne | @elsbellusskincare (francophone) | 586,8 K | [TikTok](https://www.tiktok.com/@elsbellusskincare/video/7408608295004556576) |
| 21 | « C'est pas normal que j'ai encore de l'acné à 23 ans » | Âge + injustice | @plurielmedia (FR) | 417,3 K | [TikTok](https://www.tiktok.com/@plurielmedia/video/7607903545056251139) |
| 22 | (légende) « celles qui s'en sont sorties comment ??? je vous en supplie » | Demande d'aide | @celeste111555 (FR) | 406,2 K ; 3 348 comm. | [TikTok](https://www.tiktok.com/@celeste111555/video/7645760032977521952) |
| 23 | « If you break out like this the week before your period… » | « Si tu… » + cycle | @lifewithmils (EN) | 387,5 K | [TikTok](https://www.tiktok.com/@lifewithmils/video/7599392455837977877) |
| 24 | « Il y a 1 an, ma peau ressemblait à ça, aujourd'hui… » | Journal daté | @almasch_ (FR) | 296,3 K | [TikTok](https://www.tiktok.com/@almasch_/video/7590733807192378646) |
| 25 | « Why? » (légende « Does this happen to anyone else ») | Question relatable | @mvp_macrae (EN) | 293,8 K | [TikTok](https://www.tiktok.com/@mvp_macrae/video/7393033121223970078) |
| 26 | « t'as tout essayé contre les boutons mais rien ne marche ? moi aussi » | Empathie + méthode < 10 € | @nuniverse__ (FR) | 291,9 K | [TikTok](https://www.tiktok.com/@nuniverse__/video/7656916200198278432) |
| 27 | « j'ai développé l'appli de mes rêves… plus de 1000 utilisateurs » | Fondatrice d'app (isAd) | @mochi_skin.app (FR) | 284,8 K ; ER 0,3 % | [TikTok](https://www.tiktok.com/@mochi_skin.app/video/7666034979381546272) |
| 28 | « j'ai 30 ans, j'ai de l'acné et je reviens de chez le dermato » | Âge + frustration | @leazlook (FR) | 266,5 K | [TikTok](https://www.tiktok.com/@leazlook/video/7447218196161039638) |
| 29 | « ma routine skincare pour passer d'une peau pleine de boutons à une peau nickel » | Transformation (isAd) | @louisefcd (FR) | 228,5 K | [TikTok](https://www.tiktok.com/@louisefcd/video/7566690528700484886) |
| 30 | « cette fille a de l'acné sévère et je réagis à sa routine » | Réaction | @skincarebysamy (FR) | 221,2 K | [TikTok](https://www.tiktok.com/@skincarebysamy/video/7290958203851001120) |
| 31 | « j'ai ma 1ère visite d'appart et je me sens pas crédible… à cause de mon acné » | Scène de vie + vulnérabilité | @oceanepedrosa_ (FR) | 185 K | [TikTok](https://www.tiktok.com/@oceanepedrosa_/video/7686533237509803297) |
| 32 | « birth control is just a band aid when it comes to acne » | Contre-pied pilule | @ericanic0le (EN) | 161,2 K | [TikTok](https://www.tiktok.com/@ericanic0le/video/7191154979082767662) |
| 33 | « qu'est-ce que je ferais si demain j'avais une énorme [poussée] d'acné » | Scénario « si demain » | @oceanepedrosa_ (FR) | 144,8 K | [TikTok](https://www.tiktok.com/@oceanepedrosa_/video/7667979148509351201) |
| 34 | « Je vous dévoile mes produits miraculeux contre l'acné » (légende « pov j'ai un bouton… ») | GRWM + POV | @lolatagliaferroo (FR) | 143,4 K | [TikTok](https://www.tiktok.com/@lolatagliaferroo/video/7494602172278050070) |
| 35 | « Je prends la spironolactone depuis trois mois pour… mon SOPK » | Story-time traitement | @laulevy (FR) | 133,5 K | [TikTok](https://www.tiktok.com/@laulevy/video/7532536183356771606) |
| 36 | « l'acné hormonale ça n'existe pas » | Mythe / contre-pied | @celialetteri (FR) | 114,7 K (4,6 K abonnés) | [TikTok](https://www.tiktok.com/@celialetteri/video/7618266469335305494) |
| 37 | « je pleurais tous les soirs, j'avais plus aucune confiance en moi » | Vulnérabilité | @rojii.ely (FR) | 109,3 K | [TikTok](https://www.tiktok.com/@rojii.ely/video/7630191339900112150) |
| 38 | « si ta peau ressemble à ça, arrête d'acheter de nouveaux produits skincare » | Anti-achat / causes | @doristenara (FR) | 97 K | [TikTok](https://www.tiktok.com/@doristenara/video/7681350485692960032) |
| 39 | « Tu as de l'acné avant tes règles ? Ça veut dire que ton ovulation n'est pas optimale » | Diagnostic (allégation non validée) | @morganepaul_naturopathe (FR) | 90,5 K (1,8 K abonnés) | [TikTok](https://www.tiktok.com/@morganepaul_naturopathe/video/7403664540405157153) |
| 40 | « Si t'as des boutons inflammatoires sur le bas du visage… c'est sûrement hormonal » | « Si t'as… » zone (Ducray) | @skincarebysamy (FR) | 89,6 K | [TikTok](https://www.tiktok.com/@skincarebysamy/video/7508105916164607254) |
| 41 | « skincare routine du soir si t'as la peau acnéique… acné pendant 5 ans » | Routine + preuve perso | @francesca.skincare (FR) | 88,7 K | [TikTok](https://www.tiktok.com/@francesca.skincare/video/7638658649929354518) |
| 42 | « j'ai 32 ans, j'ai de l'acné et on m'a toujours proposé des médicaments » | Âge + rejet des traitements (Sisley) | @leazlook (FR) | 81,1 K | [TikTok](https://www.tiktok.com/@leazlook/video/7685806725718347041) |
| 43 | « Si je devais choisir 1 seul actif pour l'acné hormonale à 30 ans » | Choix unique | @emturian (FR) | 78,5 K | [TikTok](https://www.tiktok.com/@emturian/video/7590726317583158550) |
| 44 | « j'ai 28 ans et avoir de l'acné à 28 ans, franchement je vais trop mal » | Âge + émotion | @elo.mzr (FR) | 71,8 K | [TikTok](https://www.tiktok.com/@elo.mzr/video/7676124722442046752) |
| 45 | « je te montre mes produits acné safe préférés en parapharmacie, enregistre » | Sélection + CTA favoris | @francesca.skincare (FR) | 62,8 K | [TikTok](https://www.tiktok.com/@francesca.skincare/video/7642374408232783126) |
| 46 | « Je me lave pas le visage le matin et ça a eu l'air de choquer » | Contre-pied | @francesca.skincare (FR) | 30,4 K | [TikTok](https://www.tiktok.com/@francesca.skincare/video/7613450444047748374) |
| 47 | « Tu te demandes pourquoi t'as des boutons à certaines phases de ton cycle ? » | Question cycle | @lfvrmorgane (FR) | 27,6 K | [TikTok](https://www.tiktok.com/@lfvrmorgane/video/7434275236075375905) |
| 48 | « ça fait plusieurs jours que j'ai pas tourné… en ce moment je déteste mon visage » | Vulnérabilité | @reb.szw (FR) | 24,2 K | [TikTok](https://www.tiktok.com/@reb.szw/video/7551055476453182722) |
| 49 | « I've been prescribing acne treatments for 16 years… I'm the one with the breakout » | Aveu d'expert | @crownderm (EN) | **1 887 seulement** | [TikTok](https://www.tiktok.com/@crownderm/video/7623143899128696086) |
| 50 | « Can AI give you better skin? » | IA / analyse de peau (partenariat Charlotte Tilbury) | @sarahpalmyra (EN) | 43,2 K | [TikTok](https://www.tiktok.com/@sarahpalmyra/video/7250555370513468718) |

Patterns récurrents observés dans ces accroches (comptage sur le tableau ci-dessus, non exclusif) :
- « Si t'as / If you… [symptôme, zone, âge] » : #13, 17, 23, 38, 40, 41 (+ #39, 47 en question).
- Âge + aveu (« j'ai 23/24/28/30/32 ans et de l'acné ») : #19, 21, 28, 42, 44 — exclusivement FR dans l'échantillon, très aligné avec l'avatar 18-35.
- Preuve visuelle immédiate (« il y a X / aujourd'hui », « used to look like this ») : #9, 16, 24, 29, (6 en photo).
- Récurrence mensuelle / cycle : #5, 7, 8, 23, 25, 39, 47 — en FR, les 3 plus vues sont payées par Ducray.
- Contre-pied / théorie : #15, 32, 36, 38, 46.
- Vulnérabilité / scène de vie : #22, 31, 37, 48.
- Format « liste à enregistrer » : #4, 45.

**Formule d'accroche documentée côté apps (international)** : le format slideshow « [une autre personne] + [conflit ou doute] → je lui ai montré [l'IA] → elle a changé d'avis » a fait 234 K, 167 K et 147 K vues, quand des accroches descriptives (« See your room in 12+ styles… ») plafonnaient à ~900 vues. — [Postiz, 16 avril 2026](https://postiz.com/blog/ai-agent-tiktok-views-postiz-api)
- Exemples d'accroches slideshow citées pour les apps : « 5 things I wish I knew before… », « 3 mistakes I kept making… », « 3 signs your routine is not working », « Which one would you choose? ». — [Indie Hackers, 17 juillet 2026](https://www.indiehackers.com/post/i-had-no-idea-tiktok-slideshows-could-get-apps-to-1000s-in-mrr-05ed74d49e)

### Inferences
- Hypothèse : l'accroche « âge + aveu » (« j'ai 29 ans et j'ai encore de l'acné ») est le levier FR le plus spécifique à l'avatar Nacre et le moins capté par les marques (aucune publication isAd dans ce pattern ; une seule collaboration de marque, Sisley, chez @leazlook).
- Hypothèse : « boutons avant les règles » reste un excellent déclencheur, mais en France il est associé à Ducray Keracnyl ; Nacre devrait l'aborder par l'angle « noter / observer » (suivi facultatif) plutôt que « solution produit ».
- Une bonne accroche ne suffit pas sans distribution : #49 (aveu d'un dermatologue) n'a fait que 1 887 vues.
- Les accroches « diagnostic » (#39, cartographie #4) performent mais portent des allégations non validées — à ne pas reproduire telles quelles (cohérent avec le statut non-dispositif médical de Nacre).

### Gaps
- Le texte à l'écran (souvent l'accroche principale sur TikTok) n'est pas capturé ; certaines vidéos (#2, #3, #22) sont musicales sans voix.
- Pas de données de rétention à 3 s par accroche (non publiques).

## 3. Tendances 2025-2026 skincare TikTok/IG : saturé vs montant

### Takeaway
Montent : **acné adulte et acné hormonale** (recherche mondiale), **apps acné / analyse de peau**, **patchs anti-boutons** (pic mondial fin septembre 2026), **glass skin** en France, **barrière cutanée**, et le **minimalisme / anti-surconsommation** comme état d'esprit. Retombent en France : **slugging**, **skin cycling** et **cycle syncing** (volumes quasi nuls en FR) ; la requête « acné pilule » chute fortement en FR. Les experts annoncent la fin des « hacks TikTok à nom accrocheur » et des routines en 10 étapes.

### Cited Findings

**Google Trends (collecte 2026-10-01, hebdo 5 ans ; « 12 derniers mois » = oct. 2025-sept. 2026 vs « 12 mois précédents » ; valeurs relatives au lot)**
- France, lot « tendances skincare » : « patch bouton » 57,2 → 60,9 (+6 %, pic 24-30 août 2025 = 100) ; « glass skin » 6,1 → 24,2 (+299 %, pic 15-21 fév. 2026) ; « slugging » 1,7 (2021-22) → 0,2 → 0,0 ; « skin cycling » 0,0 → 0,9 ; « cycle syncing » ~0. — [Google Trends FR](https://trends.google.com/trends/explore?geo=FR&date=today%205-y&q=skin%20cycling,slugging,patch%20bouton,cycle%20syncing,glass%20skin)
- France, lot « causes & apps » : « acné pilule » 32,0 (2021-22) → 14,0 → 3,9 (−72 % sur un an) ; « application skincare » 0,0 → 10,5 (pic 18-24 janv. 2026 = 71) ; « analyse de peau » 12,2 → 17,2 (+41 %) ; « acné règles » et « acné stress » ≈ 0. — [Google Trends FR](https://trends.google.com/trends/explore?geo=FR&date=today%205-y&q=acn%C3%A9%20pilule,acn%C3%A9%20stress,acn%C3%A9%20r%C3%A8gles,application%20skincare,analyse%20de%20peau)
- Monde, lot « tendances » : « hormonal acne » 43,0 → 53,0 (+23 %, pic 10-16 mai 2026) ; « pimple patch » 59,6 → 75,5 (+27 %, pic semaine du 27 sept. 2026 = 100) ; « skin cycling » 4,0 → 14,1 (+255 %, pic avr. 2026) ; « slugging » 12,7 → 13,5 (pic juil. 2023) ; « cycle syncing » 3,5 → 3,4. — [Google Trends Monde](https://trends.google.com/trends/explore?date=today%205-y&q=hormonal%20acne,skin%20cycling,slugging,cycle%20syncing,pimple%20patch)
- Monde, lot « acné & apps » : « adult acne » 5,2 → 18,7 (+259 %, pic 17-23 mai 2026) ; « hormonal acne » 30,2 → 37,1 (+23 %) ; « acne app » 8,5 → 38,8 (+358 %, pic 31 mai-6 juin 2026 = 100) ; « skin analysis app » 1,8 → 6,0 ; « rate my skin » 2,0 → 5,7. — [Google Trends Monde](https://trends.google.com/trends/explore?date=today%205-y&q=adult%20acne,hormonal%20acne,acne%20app,skin%20analysis%20app,rate%20my%20skin)

**Hashtags TikTok associés (cumul mondial, 2026-10-01 ; détail §4)**
- #glassskin 2,17 M publications / 43,2 Md vues ; #skinbarrier 860 K / 18,2 Md ; #pimplepatch 297 K / 12,6 Md ; #acnepatch 228 K / 5,9 Md ; #deinfluencing 112 K / 4,0 Md ; #projectpan 200,5 K / 1,9 Md ; #underconsumptioncore 15,3 K / 417 M ; #skinimalism 9,7 K / 234 M ; #skincycling 41,2 K / 1,4 Md ; #slugging 15,1 K / 1,9 Md ; #cyclesyncing 115 K / 1,6 Md ; #ratemyskin 145 / 1,2 M ; #aiskinanalysis 991 / 5,6 M ; #skinanalysis 27,1 K / 278 M ; #dupes 266 K / 8,0 Md ; #yuka 149 K / 10,3 Md. — [TikTok #glassskin](https://www.tiktok.com/tag/glassskin) ; [#skinbarrier](https://www.tiktok.com/tag/skinbarrier) ; [#deinfluencing](https://www.tiktok.com/tag/deinfluencing)

**Avis d'experts / presse**
- Beauty Independent (12 janv. 2026) : skinimalism « n'est plus une tendance, c'est un état d'esprit » (Erica Choi, Superegg) ; l'IA d'analyse de peau et les LLM comme « nouveaux influenceurs » montent ; « skin cycling, slugging, buffering et chaque hack TikTok au nom accrocheur vont continuer de chuter » (Stephanie Sprayregen, Mumuk) ; fin annoncée de la routine en 10 étapes ; l'influence passe « de la portée large à la profondeur » ; les ventes K-beauty US +37,2 % à 2 Md $ (NielsenIQ, 52 semaines au 9 août 2025). — [Beauty Independent](https://www.beautyindependent.com/?p=181177)
- Contradiction : Google Trends mondial montre « skin cycling » en hausse sur 12 mois (+255 %, depuis une base faible), tandis que les experts le disent en déclin ; en France il reste quasi nul. — [Google Trends Monde](https://trends.google.com/trends/explore?date=today%205-y&q=hormonal%20acne,skin%20cycling,slugging,cycle%20syncing,pimple%20patch) ; [Beauty Independent](https://www.beautyindependent.com/?p=181177)
- Deinfluencing : mouvement né sur TikTok qui incite à ne pas acheter les produits survendus ; distinction « deinfluencing » (acheter mieux/moins cher) vs « underconsumption core » (utiliser ce qu'on a). Une étude 2026 sur le marketing des fêtes note −14 points d'usage des hauls/unboxings entre 2025 et 2026. — [Substack C. Srivastava](https://chaanisrivastava.substack.com/p/deinfluencing-and-underconsumption) ; [L'ADN](https://www.ladn.eu/actualite/deinfluencing-tendance-anti-consumerisme-tiktok-lutte-surconsommation/) (données issues de l'extrait de recherche, page non lue en entier)
- Cycle syncing (2022) : #CycleSyncing 125 M de tags, #SkinCycling 131 M ; recherches skin cycling +1 000 % YoY et cycle syncing +153 % à l'époque ; campagne TikTok Rael ≈ 11 M vues. — [Glossy, 26 oct. 2022](https://www.glossy.co/beauty/is-cycle-syncing-wellnesss-next-frontier/)
- Le cycle syncing reste scientifiquement non démontré (recherche clinique « non concluante »). — [Clue (FR)](https://helloclue.com/fr/articles/partenariats/la-verite-sur-la-synchronisation-des-cycles-et-l-exercice-physique) ; [Slate](https://www.slate.fr/story/247892/synchronisation-menstruelle-amelioration-performances-sportives-regles)
- Acné-positivité : Starface (patchs) a bâti sa notoriété sur TikTok ; en 2020, ses vidéos avec Charli D'Amelio faisaient 19-34 M vues et la cofondatrice disait n'avoir jamais payé d'influenceurs ; la campagne #myskinandme de Massage Envy cumulait 5,7 Md de vues. — [Glossy, 24 avril 2020](https://www.glossy.co/beauty/tiktok-influencers-help-brands-reach-acne-positive-gen-z)
- Rapport Spate « French beauty trends to watch on TikTok » (oct. 2025, 900 Md de signaux de recherche, 150 M de posts) : chiffres derrière téléchargement, non consultés. — [Spate](https://www.spate.nyc/reports/french-beauty-trends-to-watch-on-tiktok)

### Inferences
- **Saturé (hypothèse)** : « boutons avant les règles → sérum » (campagne Ducray Keracnyl multi-créateurs en FR), face mapping, avant/après Roaccutane, pimple popping (énorme mais hors marque), routines « produits miracles ».
- **Montant (hypothèse)** : acné adulte (recherche +259 % mondial), apps acné et analyse de peau (+358 % mondial ; « application skincare » apparaît en FR en 2026), minimalisme / « arrête d'acheter » (cohérent avec la promesse Nacre « produits choisis selon budget »), barrière cutanée.
- Le terrain « cycle » est plus porteur en TikTok qu'en recherche Google FR (requêtes « acné règles », « cycle syncing » quasi nulles en FR) → l'aborder via des formats vécus, pas via du SEO.
- La chute de « acné pilule » en Google FR (−72 %) contraste avec la place du thème « arrêt de pilule » dans les témoignages TikTok (ex. @elo.mzr) : la conversation se serait déplacée vers les réseaux (hypothèse non vérifiée).

### Gaps
- Lot Google Trends FR « acné adulte / acné hormonale / boutons menton / roaccutane / routine acné » : bloqué (HTTP 429), non collecté.
- TikTok Creative Center redirige désormais vers « TikTok One Creative Suite » avec connexion : aucune donnée de tendance 7/30/120 jours, ni filtre France.
- Pas de mesure des filtres IA « rate my skin » sur TikTok/IG (les hashtags sont très petits : #ratemyskin 145 publications).

## 4. Volumes de hashtags

### Takeaway
Les hashtags acné **en français sont minuscules** comparés aux équivalents anglais (#acneadulte : 849 publications / 8,2 M vues vs #hormonalacne : 167 K / 5,6 Md). Les créatrices FR étiquettent massivement en anglais (#acneproneskin, #acnefighter, #hormonalacne). Les compteurs sont cumulés mondiaux, non filtrables par pays.

### Cited Findings
- #acne : 4 904 769 publications / 208,8 Md vues (2026-10-01). Une source de 2025 citait « plus de 3 M de posts et 129 Md de vues » (mesure antérieure non datée précisément). — [TikTok #acne](https://www.tiktok.com/tag/acne) ; [Dermatology Times, 2025](https://www.dermatologytimes.com/view/acne-and-tiktok-what-do-dermatologists-need-to-know-)
- #FrenchPharmacy était cité à 81,8 M vues et #Frenchskincare à 100,9 M (mai 2023) ; au 2026-10-01, #frenchpharmacy = 25 246 publications / 948,7 M vues. — [Corq, 22 mai 2023](https://corq.studio/insights/french-pharmacy-content-has-found-a-new-audience-on-tiktok-and-these-influencers-are-leading-the-conversation/) ; [TikTok #frenchpharmacy](https://www.tiktok.com/tag/frenchpharmacy)
- Tableau complet (endpoint public challenge/detail, 2026-10-01, cumul mondial) — [pages TikTok `tiktok.com/tag/<hashtag>`](https://www.tiktok.com/tag/acneadulte) :

| Groupe | Hashtag | Publications (cumul) | Vues (cumul) | Vues / publication |
|---|---|---|---|---|
| Acné — FR | #acné | 120 490 | 4.5 Md | 37.5 K |
| Acné — FR | #acneadulte | 849 | 8.2 M | 9.7 K |
| Acné — FR | #acnéadulte | 631 | 3.6 M | 5.7 K |
| Acné — FR | #acnefemme | 28 | 255.3 K | 9.1 K |
| Acné — FR | #acnehormonale | 2 566 | 72.7 M | 28.3 K |
| Acné — FR | #acnéhormonale | 1 894 | 28.9 M | 15.3 K |
| Acné — FR | #acnehormonal | 38 006 | 1.7 Md | 45.3 K |
| Acné — FR | #acnéhormonal | 5 168 | 113.6 M | 22.0 K |
| Acné — FR | #boutons | 30 484 | 3.0 Md | 99.9 K |
| Acné — FR | #bouton | 37 145 | 3.2 Md | 85.7 K |
| Acné — FR | #boutonsdacné | 1 488 | 49.5 M | 33.3 K |
| Acné — FR | #peauacnéique | 1 653 | 18.8 M | 11.4 K |
| Acné — FR | #routineacné | 381 | 11.1 M | 29.1 K |
| Acné — FR | #solutionacne | 365 | 3.6 M | 9.7 K |
| Acné — FR | #astuceacne | 101 | 2.5 M | 24.5 K |
| Acné — FR | #skincareacné | 93 | 3.2 M | 34.5 K |
| Acné — FR | #conseilskincare | 4 376 | 102.6 M | 23.5 K |
| Acné — FR | #roaccutane | 11 048 | 744.2 M | 67.4 K |
| Acné — FR | #isotretinoine | 165 | 4.8 M | 28.9 K |
| Acné — FR | #pilule | 11 290 | 730.4 M | 64.7 K |
| Acné — FR | #arretpilule | 683 | 43.6 M | 63.9 K |
| Acné — FR | #sopk | 65 172 | 1.5 Md | 23.1 K |
| Acné — FR | #acnementon | non trouvé | non trouvé | — |
| Acné — EN/global | #acne | 4 904 769 | 208.8 Md | 42.6 K |
| Acné — EN/global | #adultacne | 38 199 | 883.2 M | 23.1 K |
| Acné — EN/global | #acnejourney | 207 479 | 10.6 Md | 50.9 K |
| Acné — EN/global | #hormonalacne | 167 374 | 5.6 Md | 33.4 K |
| Acné — EN/global | #hormonalacnetips | 1 106 | 39.8 M | 36.0 K |
| Acné — EN/global | #chinacne | 1 072 | 118.2 M | 110.2 K |
| Acné — EN/global | #jawlineacne | 1 077 | 46.4 M | 43.1 K |
| Acné — EN/global | #acneproneskin | 895 184 | 25.5 Md | 28.5 K |
| Acné — EN/global | #acnefighter | 933 096 | 25.8 Md | 27.7 K |
| Acné — EN/global | #acnetips | 142 102 | 5.0 Md | 35.5 K |
| Acné — EN/global | #acneskincare | 363 782 | 10.0 Md | 27.4 K |
| Acné — EN/global | #acnetreatment | 1 724 458 | 48.5 Md | 28.1 K |
| Acné — EN/global | #acnesolution | 105 869 | 3.1 Md | 29.4 K |
| Acné — EN/global | #acnescars | 266 946 | 12.2 Md | 45.7 K |
| Acné — EN/global | #cysticacne | 51 379 | 4.6 Md | 89.2 K |
| Acné — EN/global | #accutane | 115 559 | 5.1 Md | 43.9 K |
| Acné — EN/global | #accutanejourney | 38 272 | 1.8 Md | 47.1 K |
| Acné — EN/global | #spironolactone | 7 671 | 327.8 M | 42.7 K |
| Acné — EN/global | #postpillacne | 1 955 | 71.6 M | 36.6 K |
| Acné — EN/global | #pcos | 1 771 938 | 31.3 Md | 17.7 K |
| Acné — EN/global | #periodacne | 1 102 | 23.3 M | 21.1 K |
| Acné — EN/global | #acnetransformation | 15 641 | 1.1 Md | 72.2 K |
| Acné — EN/global | #acneupdate | 973 | 32.7 M | 33.6 K |
| Acné — EN/global | #acneclearing | 2 418 | 65.4 M | 27.0 K |
| Acné — EN/global | #acnecommunity | 11 508 | 603.9 M | 52.5 K |
| Acné — EN/global | #acneawareness | 11 845 | 620.5 M | 52.4 K |
| Acné — EN/global | #acnegirl | 4 494 | 154.7 M | 34.4 K |
| Acné — EN/global | #pimplepopping | 161 497 | 29.8 Md | 184.8 K |
| Positivité / format | #acnepositivity | 50 780 | 3.6 Md | 71.0 K |
| Positivité / format | #acnepositive | 2 671 | 210.3 M | 78.7 K |
| Positivité / format | #skinpositivity | 25 962 | 1.4 Md | 54.2 K |
| Positivité / format | #realskin | 72 091 | 2.0 Md | 28.2 K |
| Positivité / format | #nomakeup | 1 958 548 | 11.5 Md | 5.9 K |
| Positivité / format | #grwm | 25 072 597 | 569.3 Md | 22.7 K |
| Positivité / format | #grwmacne | 152 | 4.8 M | 31.5 K |
| Positivité / format | #skindiary | 952 | 2.3 M | 2.4 K |
| Positivité / format | #skinjourney | 66 983 | 1.5 Md | 22.7 K |
| Positivité / format | #skinupdate | 14 258 | 328.7 M | 23.1 K |
| Positivité / format | #skintransformation | 126 032 | 3.1 Md | 24.2 K |
| Positivité / format | #glowup | 33 983 549 | 367.1 Md | 10.8 K |
| Positivité / format | #clearskin | 984 844 | 25.0 Md | 25.4 K |
| Positivité / format | #ratemyskin | non trouvé | non trouvé | — |
| Positivité / format | #aiskinanalysis | 991 | 5.6 M | 5.7 K |
| Positivité / format | #skinanalysis | 27 146 | 278.3 M | 10.3 K |
| Positivité / format | #acneapp | 34 | 173.4 K | 5.1 K |
| Positivité / format | #skincareapp | 1 891 | 88.8 M | 46.9 K |
| Skincare général / tendances | #skincare | 60 882 369 | 986.8 Md | 16.2 K |
| Skincare général / tendances | #skincareroutine | 18 974 306 | 251.4 Md | 13.3 K |
| Skincare général / tendances | #skincaretips | 6 904 095 | 122.4 Md | 17.7 K |
| Skincare général / tendances | #skintok | 1 713 489 | 60.9 Md | 35.5 K |
| Skincare général / tendances | #skincarefrance | 13 382 | 259.5 M | 19.4 K |
| Skincare général / tendances | #frenchpharmacy | 25 246 | 948.7 M | 37.6 K |
| Skincare général / tendances | #pharmacie | 115 537 | 3.5 Md | 30.2 K |
| Skincare général / tendances | #parapharmacie | 93 208 | 1.2 Md | 12.4 K |
| Skincare général / tendances | #skinbarrier | 860 248 | 18.2 Md | 21.1 K |
| Skincare général / tendances | #barrierecutanee | 1 324 | 66.0 M | 49.8 K |
| Skincare général / tendances | #glassskin | 2 168 737 | 43.2 Md | 19.9 K |
| Skincare général / tendances | #skincycling | 41 151 | 1.4 Md | 33.4 K |
| Skincare général / tendances | #slugging | 15 104 | 1.9 Md | 127.5 K |
| Skincare général / tendances | #skinimalism | 9 678 | 234.3 M | 24.2 K |
| Skincare général / tendances | #skincareminimaliste | 407 | 814.8 K | 2.0 K |
| Skincare général / tendances | #routineminimaliste | 772 | 1.8 M | 2.4 K |
| Skincare général / tendances | #deinfluencing | 112 023 | 4.0 Md | 35.8 K |
| Skincare général / tendances | #projectpan | 200 503 | 1.9 Md | 9.6 K |
| Skincare général / tendances | #underconsumptioncore | 15 269 | 417.2 M | 27.3 K |
| Skincare général / tendances | #dupes | 266 117 | 8.0 Md | 30.0 K |
| Skincare général / tendances | #antigaspi | 26 067 | 830.7 M | 31.9 K |
| Skincare général / tendances | #yuka | 148 875 | 10.3 Md | 69.3 K |
| Skincare général / tendances | #pimplepatch | 297 121 | 12.6 Md | 42.5 K |
| Skincare général / tendances | #acnepatch | 227 990 | 5.9 Md | 26.0 K |
| Skincare général / tendances | #maskne | 13 705 | 268.0 M | 19.6 K |
| Cycle / hormones | #cyclesyncing | 115 433 | 1.6 Md | 14.0 K |
| Cycle / hormones | #cyclemenstruel | 13 113 | 539.5 M | 41.1 K |
| Cycle / hormones | #cyclefeminin | 5 087 | 87.6 M | 17.2 K |
| Cycle / hormones | #regles | 39 211 | 1.7 Md | 43.3 K |
| Cycle / hormones | #règles | 11 941 | 495.2 M | 41.5 K |
| Cycle / hormones | #spm | 434 571 | 8.2 Md | 18.9 K |
| Cycle / hormones | #syndromeprémenstruel | 1 120 | 14.6 M | 13.0 K |
| Cycle / hormones | #hormones | 549 534 | 10.1 Md | 18.5 K |
| Cycle / hormones | #déséquilibrehormonal | 334 | 5.4 M | 16.1 K |
| Cycle / hormones | #endometriose | 195 169 | 3.5 Md | 17.7 K |
| Marques | #ducray | 7 284 | 484.0 M | 66.4 K |
| Marques | #keracnyl | 681 | 105.2 M | 154.4 K |
| Marques | #effaclar | 61 103 | 9.2 Md | 150.2 K |
| Marques | #larocheposay | 671 059 | 29.0 Md | 43.1 K |
| Marques | #cerave | 784 439 | 32.9 Md | 41.9 K |

### Inferences
- Vues par publication (proxy très grossier de la « demande » par contenu) : #acneadulte ≈ 9,7 K, #acnéhormonale ≈ 15,3 K, #hormonalacne ≈ 33,4 K, #acnejourney ≈ 50,9 K, #acnepositivity ≈ 71 K. Les hashtags anglais restent plus « porteurs » même pour du contenu FR (hypothèse).
- #skindiary (952 posts) et #acneupdate (973) sont quasiment vierges : opportunité de « posséder » un label FR type « point peau » / « semaine X » (hypothèse ; le hashtag n'est pas un levier majeur de distribution sur TikTok en 2026).
- Les hashtags de marque montrent l'avance de LRP/CeraVe (#larocheposay 29,0 Md vues ; #cerave 32,9 Md) vs Ducray (484 M) — Ducray compense par des créateurs payés.

### Gaps
- Volumes France seulement, tendance 30/120 jours, rang de tendance : non disponibles (Creative Center/TikTok One sous connexion).
- Volumes de hashtags Instagram : non obtenus (pages de tags Instagram fermées sans connexion).

## 5. Instagram vs TikTok : benchmarks par format (beauté)

### Takeaway
Sur Instagram, les **carrousels** gardent le meilleur taux d'engagement et, chez Socialinsider, même plus de vues que les Reels pour les comptes de marque ; les Reels gardent la meilleure portée chez Buffer. Sur TikTok, la vidéo reste devant le mode photo en moyenne, mais les carrousels photo de micro-comptes peuvent exploser (cas acné observés). La beauté a des taux d'engagement parmi les plus bas, mais TikTok y reste le canal le plus fort en vues.

### Cited Findings
- Socialinsider (publié 20 fév. 2026 ; 35 M de posts, 447 613 pages, année 2025) — taux d'engagement Instagram : carrousels 0,55 % (2025) vs Reels 0,52 % vs images 0,37 % ; T1 2026 : 0,52 / 0,50 / 0,35 % ; T2 2026 : 0,50 / 0,48 / 0,33 %. Engagement moyen 0,48 % (−24 % sur un an). Vues moyennes par taille de compte : 10-50 K abonnés → carrousels 4 275 vs Reels 2 460 ; 50-100 K → 11 597 vs 6 095. Favoris (50-100 K) : carrousels 35 vs Reels 22. Fréquence 2025 : 8 Reels, 5 carrousels, 7 images / mois. Pas de découpage beauté. — [Socialinsider](https://www.socialinsider.io/blog/instagram-benchmarks/)
- Buffer (19 mars 2026 ; 45 M+ posts) — Instagram, taux d'engagement médian rapporté à la portée : carrousels 6,9 %, images 4,4 %, Reels 3,3 % ; les Reels ont 1,36× la portée des carrousels et 2,25× celle des images. TikTok : vidéo 3,39 % vs carrousels/photos 1,92 % (+77 % pour la vidéo). — [Buffer](https://buffer.com/resources/data-best-content-format-social-media/)
- Contradiction : un guide TTCalculator (T3 2025-T1 2026) affirme que les carrousels TikTok font +15 à 35 % d'engagement vs vidéo pour les comptes < 100 K (6,8 % vs 5,2 %) ; source peu établie. — [TTCalculator](https://ttcalculator.net/guides/growth/tiktok-photo-carousel-engagement/) ; contredit par [Buffer](https://buffer.com/resources/data-best-content-format-social-media/)
- Dash Social, beauté (juil.-déc. 2025) : engagement TikTok 2,8 % (vs 3,6 % avant), Instagram 2,1 % par vues (vs 2,9 %) ; vues moyennes/post TikTok 229 K, Instagram 171 K, YouTube 145 K ; rétention TikTok 23 % ; les meilleurs comptes beauté publient 8×/semaine sur TikTok et 5×/semaine sur Instagram ; « les Reels sont le premier levier de portée » sur Instagram. — [Dash Social](https://www.dashsocial.com/social-media-benchmarks/beauty-industry)
- Rival IQ 2026 : « Beauty & Retail » ont l'engagement le plus faible de toutes les plateformes (données 2025, publié 5 mars 2026) ; un résumé secondaire cite un engagement Instagram médian de 0,14 % par post pour Health & Beauty (chiffre non retrouvé dans la page lue). — [Quid / Rival IQ](https://www.quid.com/knowledge-hub/resource-library/blog/2026-social-media-industry-benchmark-report) ; [Apaya (secondaire)](https://apaya.com/blog/social-media-benchmarks-beauty)
- IQFluence 2026 : TikTok ~4,5 % d'engagement ; les carrousels image y « tirent près de 2 % ». — [IQFluence](https://iqfluence.io/public/blog/social-media-benchmarks)
- Échantillon acné (§1) : TikTok photo n=14, médiane 73,2 K vues vs vidéo 105,7 K ; mais 3 des 5 meilleurs ratios vues/abonnés (et 5 des 11 premiers) sont des carrousels photo de micro-comptes (jusqu'à 4 243×). — [@lana.hpny](https://www.tiktok.com/@lana.hpny/photo/7620160093228715286) ; [@sarah.hym](https://www.tiktok.com/@sarah.hym/photo/7624844858896796950)
- Comptes FR d'autorité plus gros sur Instagram que sur TikTok : @thecleanjunky 146 K IG vs 22,5 K TikTok ; @emturian 323 K IG vs 142,9 K TikTok ; à l'inverse @myssyjym 317 K IG vs 922,7 K TikTok et @skincarebysamy 472 K IG vs 1,1 M TikTok. — [Instagram @thecleanjunky](https://www.instagram.com/thecleanjunky/) ; [TikTok @thecleanjunky](https://www.tiktok.com/@thecleanjunky) ; [Instagram @myssyjym](https://www.instagram.com/myssyjym/) ; [TikTok @myssyjym](https://www.tiktok.com/@myssyjym)

### Inferences
- Hypothèse de répartition : TikTok = découverte (vécu, accroches, slideshows) ; Instagram = carrousels éducatifs « à enregistrer » + preuve sociale + conversion via lien/DM ; Reels IG = recyclage des meilleurs TikTok pour la portée.
- Les chimistes/éducateurs FR (Carole Ballerini, Émeline Cousturian) ont leur base principale sur Instagram : partenariats « carrousel éducatif » plus naturels là-bas.
- Les benchmarks divergent selon la définition de l'engagement (par abonné, par portée, par vue) : ne comparer que des chiffres de même méthode.

### Gaps
- Aucun benchmark carrousel vs Reel spécifique « skincare » ou « acné » trouvé.
- Pas de données post par post sur les Reels/carrousels Instagram des créateurs acné FR.

## 6. Playbooks organiques des apps à abonnement (TikTok/IG, 2024-2026)

### Takeaway
Les apps grand public qui croissent en organique combinent : **(1) réseaux de créateurs/micro-comptes payés au post ou au CPM**, **(2) plusieurs comptes de marque « thématiques » / faceless (slideshows produits en série)**, **(3) formats natifs où l'app apparaît dans une histoire** plutôt qu'en démo, et **(4) un mécanisme partageable** (score, capture). Dans l'acné, AcneTrack, Thea et Puffin passent déjà par des comptes « ambassadeurs » à très faible audience qui atteignent 0,5-10,8 M vues.

### Cited Findings

**Cal AI (calories, IA)**
- 300+ partenariats influenceurs en 18 mois, n°1 Santé & Forme sur l'App Store, 50 M$+ d'ARR ; repère initial de **10 installations pour 1 000 vues** ; CPM payé 0,50-3,00 $ ; « une vidéo ≈ 1 000 $ » (≈ prix de 30 vidéos UGC) ; jusqu'à 20 influenceurs embarqués par semaine (contrats automatisés, canal Slack par créateur, briefs modèles) ; formats « what I eat in a day », snacks, transformations ; vidéos à 43 M, 56 M et 73 M vues organiques ; critères : vues (pas abonnés), qualité des commentaires, audience « culte ». — [FunnelFox, 24 avril 2026](https://blog.funnelfox.com/cal-ai-influencer-marketing/)
- 12+ comptes TikTok de marque lancés en janvier 2025 (carrousels, vidéos faceless recyclées, originaux) ; un carrousel à 25 K vues et 941 favoris ; 15 M+ téléchargements ; 1,5 M$ de MRR au moment de cette poussée multi-comptes ; 30 M$+ de revenu annuel fin 2025 ; chaîne de production : images Pinterest → modèles Figma → légendes avec calories, « des dizaines de carrousels en une heure ». — [8x.social, 30 mars 2026](https://www.8x.social/en/blog/cal-ai-multi-account)
- Les chiffres de revenu diffèrent selon les dates (1,1 M$/mois à 8 mois ; 30 M$+ annuel fin 2025 ; 50 M$+ ARR en 2026) — séries temporelles différentes, non contradictoires en soi. — [The Dock](https://thedock.beehiiv.com/p/making-1-1m-mo-from-an-ai-app-organically-at-17-years-old) ; [FunnelFox](https://blog.funnelfox.com/cal-ai-influencer-marketing/)

**Umax (looksmaxxing, score de visage)**
- ~500 K$ de revenus mensuels d'abonnement (non vérifié par Fortune), 7 M+ téléchargements, 3,99 $/semaine, score hebdomadaire sur 100 ; croissance via TikTok où les utilisateurs partagent leurs captures de score Umax dans leurs vidéos → plus d'1 Md d'impressions ; le fondateur : « les réseaux sociaux sont le plus grand canal publicitaire ». — [Fortune, 1er juillet 2024](https://www.fortune.com/2024/07/01/looksmaxxing-apps-rate-teen-boys-faces-mental-health)

**Bible Chat**
- Compte TikTok @biblechatapp : 167,5 K abonnés, 8,2 M likes ; bio « used by over 25M » (2026-10-01). — [TikTok @biblechatapp](https://www.tiktok.com/@biblechatapp)
- Appfigures (avril 2025, extrait de recherche ; page 403) : deux comptes (@biblechatapp, @ilovebiblechat) à 105 M vues cumulées, une vidéo de Noël à 69 M vues ; 1,5 M téléchargements en mars 2025 — mais le compte ne postait plus depuis des mois : la hausse est attribuée au SEO et à Apple Search Ads (~2 000 mots-clés US). — [Appfigures](https://appfigures.com/resources/insights/20250418/5-this-is-how-to-drive-demand-for-the-oldest-book-in-the-world)

**Apps période / santé féminine**
- Flo : TikTok présenté comme « le canal au plus fort potentiel de croissance et de découverte » ; contenu optimisé pour la recherche sociale ; pipeline de créateurs UGC ; relecture médicale et juridique. — [Offre d'emploi Flo (Greenhouse)](https://job-boards.greenhouse.io/flohealth/jobs/7686592003)
- Campagne TikTok Flo menée par l'agence House of Marketers (chiffres de l'agence) : 10,5 M+ vues, 200 K+ engagements ; trois profils de créateurs : professionnels de santé, créatrices « relatable », leaders de communauté. — [8x.social](https://www.8x.social/en/blog/scale-authenticity)
- Stardust (suivi des règles) aurait atteint 1 M d'utilisateurs en organique (extrait de recherche, sans détail). — [Substack L. Feygin](https://leahfeygin.substack.com/p/the-dos-and-donts-of-femtech)
- Clue : aucun chiffre organique TikTok trouvé ; @helloclue sur TikTok renvoie un compte vide (2026-10-01). — [TikTok @helloclue](https://www.tiktok.com/@helloclue)

**Starface (patchs acné, marque DTC — pas une app mais référence acné)**
- TikTok @starface : 3,2 M abonnés, 45,7 M likes ; Instagram 656 K (2026-10-01). — [TikTok @starface](https://www.tiktok.com/@starface) ; [Instagram @starface](https://www.instagram.com/starface/)
- Soirées « kickback » de créateurs : 17,2 M d'impressions et +200 % d'abonnés (extrait de recherche, Shorty Awards). — [Shorty Awards](https://shortyawards.com/5th-socialgood/big-yellow)

**Slideshows / multi-comptes / AI-UGC (apps diverses)**
- 10 formats slideshow identifiés pour les apps (conseils/erreurs, émotion → révélation, classements, checklists problème-solution, choix interactifs, transformations, mèmes, audio, récits chronologiques, actualités) ; les 5 meilleurs posts « choix interactif » ont fait 221,5 M vues ; « l'app apparaît comme une partie de l'histoire » ; commentaires et favoris > vues comme signal d'intention. — [Indie Hackers, 17 juillet 2026](https://www.indiehackers.com/post/i-had-no-idea-tiktok-slideshows-could-get-apps-to-1000s-in-mrr-05ed74d49e)
- Larry (agent IA de slideshows) : 6 slides 1024×1536, ≤ 5 hashtags, ~60 s d'intervention humaine/post ; 500 K+ vues la 1re semaine, 108 abonnés payants, 588 $ de MRR, ~0,50 $/post. — [Postiz, 16 avril 2026](https://postiz.com/blog/ai-agent-tiktok-views-postiz-api)
- Crushon AI : 50+ comptes TikTok, 3 vidéos/compte/jour (comparatifs générés par IA) → 300 K$ de MRR ; Dippy AI : 60+ comptes, ~100 vidéos/jour, 60 M vues en 3 mois, 15 K$ MRR (contre-exemple : beaucoup de vues, peu de revenu). — [Indie Hackers, 12 déc. 2024](https://www.indiehackers.com/post/50-tiktok-accounts-ai-200-000-mrr-for-mobile-app-bd8f6f48ac)
- Couple Joy (faceless slideshow) : 2 M+ vues, 60 K+ likes, 200+ vidéos. — [Playkit, 2 juillet 2025](https://playkit.substack.com/p/couple-joy-faceless-slideshow-growth)
- Réseau Playkit de 200 micro-créateurs : 600 M+ vues organiques, 3,6 M téléchargements (chiffres auto-déclarés). — [Playkit, 15 oct. 2025](https://playkit.beehiiv.com/p/inside-playkit-s-200-creator-army-and-how-to-replicate-it)
- Rémunération UGC citée : ~30 $/vidéo ou ~1 000 $/mois pour une publication quotidienne sur comptes neufs ; modèle hybride ~250 $/mois + 0,30 $ CPM ; 30-250 $ par vidéo UGC en moyenne (sources secondaires peu établies). — [ClaudeSkills / ASO skills](https://claudeskills.info/zh/skills/Eronred/aso-skills/creator-ugc-marketing/) ; [Influencer Hero](https://www.influencer-hero.com/de/blogs/ugc-influencer-rates)

**Apps acné observées dans l'échantillon (2026-10-01)**
- AcneTrack : compte officiel TikTok 8 abonnés (« Search Acnetrack on the App Store ») mais vidéos de comptes tiers à 10,8 M et 296,1 K vues (@kiki.13521, compte secondaire) ; @askcalvin_ (162 K) la cite dans 2 vidéos à 1,0 M et 615 K vues ; compte « témoignage » dédié @olim.acnetrack (105 abonnés). — [TikTok @acnetrack](https://www.tiktok.com/@acnetrack) ; [@kiki.13521](https://www.tiktok.com/@kiki.13521/video/7627904891175832864) ; [@olim.acnetrack](https://www.tiktok.com/@olim.acnetrack)
- Thea : @alyssaskincarequeen (bio « thea ambassador », 2 349 abonnés) → 533,1 K vues. Puffin : @ellaclearskin (591 abonnés, bio dédiée à l'app) → 488,9 K vues. — [Thea](https://www.tiktok.com/@alyssaskincarequeen/video/7634036334503496990) ; [Puffin](https://www.tiktok.com/@ellaclearskin/video/7667327392385355021)
- MochiSkin (FR, fondatrice « Marie ») : compte 378 abonnés, bio « +3k utilisateurs » ; vidéo fondatrice 284,8 K vues mais `isAd` et ER 0,3 % ; deux autres vidéos à 23,5 K et 826 vues ; Instagram 30 abonnés. — [TikTok @mochi_skin.app](https://www.tiktok.com/@mochi_skin.app) ; [vidéo](https://www.tiktok.com/@mochi_skin.app/video/7666034979381546272)
- Koru (« acne coach ») : collaboration rémunérée avec @___oraane (875 K abonnés) → 177,3 K vues (isAd). Skinely : @claire3264 → 461 vues. — [Koru](https://www.tiktok.com/@___oraane/video/7381099647244225825) ; [Skinely](https://www.tiktok.com/@claire3264/photo/7684379344189312288)
- Concurrence indirecte FR : @askcalvin_ (« Miho », 162 K) renvoie vers son propre « Miho skincare programme » (mihoskin.com) ; @clearskinfrance (6,4 K) fonctionne en funnel « mot-clé en DM » (beacons.ai/acneboy) ; @louisefcd (94,9 K) renvoie vers l'app Solaia (« Perds du poids en désinflammant ton corps »). — [TikTok @askcalvin_](https://www.tiktok.com/@askcalvin_) ; [Solaia](https://solaia.app/diagnostic)
- Ducray (marque) : compte TikTok de marque 22,3 K abonnés seulement, mais campagne Keracnyl portée par ≥ 8 créateurs FR (§1). — [TikTok @ducray](https://www.tiktok.com/@ducray)

### Inferences
- Hypothèse « playbook Nacre pré-lancement » : (a) 2-4 comptes thématiques FR faceless (slideshows « acné adulte », « routine pharmacie par budget », « carnet de cycle ») ; (b) 5-15 micro-créatrices témoignage payées au post + bonus CPM ; (c) la fondatrice/l'équipe en « build in public » ; (d) un artefact partageable (carte « Semaine X » du suivi hebdo) — inspiré d'Umax, sans score de « beauté » ni promesse.
- Le repère Cal AI (10 installs / 1 000 vues) concerne une app virale US de calories : ne pas le transposer tel quel à une app acné FR payante (7,99 €/mois) ; à mesurer.
- Les comptes « ambassadeurs » acné (AcneTrack/Thea/Puffin) prouvent que des micro-comptes peuvent générer des centaines de milliers de vues dans la niche, mais rien ne dit combien d'installations en résultent.
- Risque : les formats « ambassadeur » non signalés peuvent poser un problème de transparence publicitaire (en France, mention de collaboration commerciale obligatoire) — à vérifier avec l'axe réglementation.

### Gaps
- Aucun chiffre d'installations, de conversion ou de revenu pour AcneTrack, Thea, Puffin, MochiSkin, Skinely, TroveSkin, BeautyDecoded.
- Pas de chiffres organiques publics pour Flo/Clue au-delà des affirmations d'agence.
- Tarifs des micro-créatrices FR (par vidéo, CPM) : non trouvés pour la France.
- Recherche web plafonnée (quota de recherches de la session atteint) : pas d'étude de cas supplémentaire sur l'AI-UGC, le « founder-led content » ou les Trial Reels Instagram.

## 7. Créateurs français pertinents (autorité vs témoignage)

### Takeaway
Les « autorités » FR les plus fortes en acné (Myriam @myssyjym, Samy, Amoudax, Carole Ballerini @thecleanjunky) **travaillent déjà avec Ducray sur l'acné cyclique** ; Dermato Drey (dermatologue, 187 K TikTok / 126 K IG) est l'autorité médicale la plus visible sans lien Ducray observé. Côté témoignage, Océane Pedrosa (SOPK, 24 ans, 91,9 K) est la plus alignée avec l'avatar et la plus engageante (ER 8,5-11,3 %).

### Cited Findings

Abonnés au 2026-10-01 (TikTok via page profil ; Instagram via balise publique). « Engagement typique » = ER par vue des vidéos de l'échantillon (1 à 4 vidéos ; indicatif).

**A. Autorités / expertes (à qualifier : diplôme non vérifié par nous)**

| Créateur | Statut déclaré | TikTok | Instagram | Vidéos de l'échantillon (vues, ER) | Liens marques observés | Source |
|---|---|---|---|---|---|---|
| Dermato Drey | Dermatologue ; livre « Faire la paix avec sa peau » | @dermatodrey 186,9 K abonnés, 1,4 M likes, 202 vidéos | @dermato_drey 126 K | non collectées | aucun observé | [TikTok](https://www.tiktok.com/@dermatodrey) ; [Instagram](https://www.instagram.com/dermato_drey/) |
| Docteur_skin (Dr Dima Haidar selon une source secondaire) | Dermatologue | compte quasi vide (184) | @docteur_skin 106 K | — | — | [Instagram](https://www.instagram.com/docteur_skin/) |
| Carole Ballerini | Chimiste cosmétique ; newsletter theskinletter.fr | @thecleanjunky 22,5 K | @thecleanjunky 146 K | Ducray Keracnyl 3,0 M (isAd, ER 0,2 %) | **Ducray** | [TikTok](https://www.tiktok.com/@thecleanjunky) ; [Instagram](https://www.instagram.com/thecleanjunky/) |
| Myriam Ben Souilem | « a travaillé dans le secteur pharmaceutique » ; autrice d'un livre sur l'acné | @myssyjym 922,7 K, 27,2 M likes | 317 K | 7,7 M (ER 11,1 %) ; Ducray 85,6 K (ER 8,5 %) | **Ducray** (publicité) ; fondatrice de @Sérotonine | [TikTok](https://www.tiktok.com/@myssyjym) ; [Instagram](https://www.instagram.com/myssyjym/) ; [Gens d'Internet](https://gensdinternet.fr/?p=28483) |
| Amoudax | Biochimiste / chimiste cosmétique (selon sources secondaires) | @amoudaxtiktok 643,3 K | @amoudax 248 K | Ducray 15,9 K (ER 5,3 %) | **Ducray** | [TikTok](https://www.tiktok.com/@amoudaxtiktok) ; [Instagram](https://www.instagram.com/amoudax/) |
| Samy | « Skin expert » auto-déclaré (skincare & longévité) | @skincarebysamy 1,1 M, 20,3 M likes | 472 K | 877 K (ER 14,3 %) ; 413,2 K ; 221,2 K ; Ducray 89,6 K | **Ducray** (publicité) | [TikTok](https://www.tiktok.com/@skincarebysamy) ; [Instagram](https://www.instagram.com/skincarebysamy/) |
| Émeline Cousturian | « On décode les cosmétiques » (dupes clean) — pas de diplôme affiché | @emturian 142,9 K | @emturian 323 K | 78,5 K (ER 5,6 %) | agence Baghera | [TikTok](https://www.tiktok.com/@emturian) ; [Instagram](https://www.instagram.com/emturian/) |
| Dr Bernadette Ibrahim | Médecin esthétique (Bruxelles / Marseille) | @dr_bernabeauty 19,6 K | 30 K | 47,3 K (ER 5,7 %) — « consultez » | — | [TikTok](https://www.tiktok.com/@dr_bernabeauty) |
| Pharmacie Gare Sevran | Compte d'officine | 60,7 K | — | Ducray 21,2 K | **Ducray** | [TikTok](https://www.tiktok.com/@pharmaciegaresevran) |
| Doris Tenara | Esthéticienne & naturopathe (Paris 11) — pas professionnelle de santé | @doristenara 258,1 K | — | 97 K (ER 11,3 %) ; 413,5 K (2021) | compléments cités (Santarel) | [TikTok](https://www.tiktok.com/@doristenara) |
| Morgane Lefèvre | Naturopathe santé féminine (SOPK, hormones) — pas professionnelle de santé | @lfvrmorgane 56,1 K | 13 K | 27,6 K (ER 5,4 %) | — | [TikTok](https://www.tiktok.com/@lfvrmorgane) ; [Instagram](https://www.instagram.com/lfvrmorgane/) |

**B. Témoignages / créatrices « vécu »**

| Créatrice | Profil | TikTok | Instagram | Vidéos de l'échantillon (vues, ER) | Ton / liens | Source |
|---|---|---|---|---|---|---|
| Océane Pedrosa | 24 ans, SOPK, acné adulte, arrêt de pilule | @oceanepedrosa_ 91,9 K, 9,1 M likes | @oceanepedrosa 28 K | 614,1 K (11,1 %) ; 185 K (8,5 %) ; 144,8 K (11,3 %) ; 102,1 K (8,8 %) ; interview Pluriel 417,3 K | Vulnérable, routine, réponses aux commentaires | [TikTok](https://www.tiktok.com/@oceanepedrosa_) |
| Elo | 28 ans, acné depuis arrêt pilule 2023 ; duo Rislo & Elo | @elo.mzr 241 K | IG perso : elmzr (non vérifié) | 71,8 K (8,0 %) | Agence Must Have | [TikTok](https://www.tiktok.com/@elo.mzr) |
| Céleste | Skincare & boucles, fait de l'UGC | @celeste111555 212,9 K, 24 M likes | 17 K | 406,2 K (9,2 % ; 3 348 comm.) | Demande d'aide, communauté | [TikTok](https://www.tiktok.com/@celeste111555) |
| Léa Z | 30-32 ans, acné adulte ; mode & confiance | @leazlook 163,1 K | non retrouvé | 266,5 K (3,2 %) ; Sisley 81,1 K | **Sisley** | [TikTok](https://www.tiktok.com/@leazlook) |
| Laurène Lévy | SOPK, spironolactone ; bien-être au travail | @laulevy 361,5 K | 158 K | 133,5 K (5,2 %) | Sujet médical (prudence) | [TikTok](https://www.tiktok.com/@laulevy) ; [Instagram](https://www.instagram.com/laulevy/) |
| Rojii | Confiance, maquillage | @rojii.ely 632,2 K | — | 109,3 K (6,1 %) | Agence Promoinflu | [TikTok](https://www.tiktok.com/@rojii.ely) |
| Kay | Beauté / cycle | @_kayyh 373,5 K | — | Ducray 2,9 M (isAd) | **Ducray** ; Migos Media | [TikTok](https://www.tiktok.com/@_kayyh) |
| Francesca | Ex-acné 5 ans, parapharmacie & K-beauty | @francesca.skincare 35,7 K, 4,5 M likes | 5,5 K | 88,7 K (8,2 %) ; 62,8 K (7,3 %) ; 30,4 K (6,0 %) | Agence Grapper | [TikTok](https://www.tiktok.com/@francesca.skincare) |
| Nora | « certified acne girly », 15 ans d'acné | @nora_journey 12,8 K | — | 164,6 K (10,0 %) | Lassitude, anti-Roaccutane | [TikTok](https://www.tiktok.com/@nora_journey) |
| Lola | Explications acné hormonale ; portfolio UGC | @lola_lp_ 8,4 K | — | 76 K (5,9 %) | UGC | [TikTok](https://www.tiktok.com/@lola_lp_) |
| nuniverse | Coréenne en France, K-beauty | @nuniverse__ 36,1 K | — | 698,8 K (19,2 %) ; 291,9 K (14,6 %) | Pédagogique, chaleureux | [TikTok](https://www.tiktok.com/@nuniverse__) |
| Pluriel (média) | Interviews témoignages | @plurielmedia 1,4 M | — | 417,3 K (10,3 %) | Format interview | [TikTok](https://www.tiktok.com/@plurielmedia) |

- Louise Aubéry (@mybetterself) a porté une campagne sur la précarité menstruelle : 1 M+ likes, 5 000 commentaires, 10 M de personnes exposées (abonnés non récupérés). — [Kolsquare](https://www.kolsquare.com/fr/blog/1month1influenceforgood-une-campagne-inspirante-fait-couler-beaucoup-dencre)
- Favikon (fév. 2026) liste aussi parmi les « top skincare France » : Aïda Kihal (acné-positivité), Laurent @skincafeine (auteur, « Mon Beauty Coach », 30 K IG), Alim (acné), Manel Moumni ; handles TikTok de cette liste non retrouvés tels quels (vérification nécessaire). — [Favikon](https://www.favikon.com/fr/blog/top-skincare-influencers-france) ; [Instagram @skincafeine](https://www.instagram.com/skincafeine/)
- Créateurs à écarter ou à risque pour la cible FR : @elsbellusskincare (1 M TikTok, cosmétologue, francophone — pays non vérifié) et @mireilleskincare1 (927,7 K, « lutte contre la dépigmentation ») ont des audiences probablement hors France métropolitaine. — [TikTok @elsbellusskincare](https://www.tiktok.com/@elsbellusskincare) ; [TikTok @mireilleskincare1](https://www.tiktok.com/@mireilleskincare1)

### Inferences
- Shortlist proposée (hypothèse, à valider par devis et vérification de diplôme) : **autorité** → Dermato Drey (médecin, livre acné, pas de lien Ducray vu), Carole Ballerini (chimiste, base IG forte, mais déjà Ducray) ; **témoignage** → Océane Pedrosa, Elo, Céleste, Léa Z, Francesca, Nora (micro), Lola (micro, profil UGC).
- Éviter de bâtir l'autorité Nacre sur des naturopathes / allégations hormonales non validées (Morgane Lefèvre, Doris Tenara, nutri-thérapeute) : incompatibles avec un positionnement « pas de diagnostic, pas de promesse ».
- La quasi-totalité des « grosses » autorités FR acné étant liées à Ducray sur l'acné cyclique, une exclusivité concurrente est probable (hypothèse : clauses à vérifier).
- Les micro-créatrices témoignage (8-40 K) ont des ER de 6-10 % et des audiences 18-30 ans : meilleur rapport coût/crédibilité pour une waitlist (hypothèse).

### Gaps
- Diplômes / numéros RPPS non vérifiés (Dermato Drey, Docteur_skin) ; statut exact de Myriam (« secteur pharmaceutique », pas « pharmacienne »).
- Aucun pharmacien·ne créateur·rice FR de taille significative identifié individuellement (seulement des comptes d'officine) — recherche web plafonnée.
- Tarifs, taux d'engagement Instagram, données démographiques d'audience (part France, âge) : non disponibles sans outil payant.
- Comptes Instagram non retrouvés : @leazlook, @louisefcd, @mybetterself (aucune balise publique renvoyée).
