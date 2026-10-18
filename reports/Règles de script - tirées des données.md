# Règles de script, tirées des données (16/10/2026)

## Les données

- **225 vidéos courtes transcrites mot à mot**, avec leurs statistiques : 193 virales (de 300 k à 136 M de vues) et 32 « témoins ». Un témoin est une vidéo du même compte qui a fait moins de 10 % de ses vues habituelles.
- **Environ 95 comptes, 4 langues :** anglais, français, espagnol et portugais.
- **4 niches :**
  - santé et alimentation ;
  - peau et acné ;
  - vulgarisation en français ;
  - méthodes d'écriture, avec des études de rétention : TikTok 9,2 M de vues, Paddy Galloway 5 400 Shorts, 10 000 TikToks scientifiques, 3 931 TED Talks.

Les fichiers bruts sont dans `reports/data scripts viraux/` : `*.jsonl` pour les transcriptions, `metrics.csv` pour les mesures, `frameworks.md` pour les méthodes sourcées.

## Ce que disent les chiffres

| | Vidéos virales | Plus de 5 M de vues | Témoins | Notre T01 v1 |
|---|---|---|---|---|
| Durée médiane | 58 s | 48 s | 58 s | 61 s |
| Mots | 168 | 132 | 168 | 207 |
| Débit | 180 mots/min | 169 | 193 | 204 |
| Début de la parole | 0,1 s | 0,1 s | 0,1 s | 0,2 s |
| Accroche « si tu… / quand tu… » | 14 % | 15 % | 3 % | non |
| Accroche en question | 15 % | 13 % | 25 % | oui |
| Appel à s'abonner | 15 % | 4 % | 9 % | non |

**En français, les vidéos virales font 70 s, 225 mots et 200 mots/min, toutes en « tu ».**

### Ce que ça montre

- **Les vidéos virales ne parlent pas plus vite que les ratées.** En anglais, elles parlent même plus lentement (162 contre 178 mots/min). Le dynamisme vient de l'écriture et de l'image, pas du débit.
- **Les plus grosses sont les plus courtes et les plus denses :** 48 s et 132 mots. T01 v1 avait trop de mots pour ce qu'elle racontait.
- **« Si tu… » bat la question.** Les témoins ratés ouvrent deux fois plus souvent sur une question.

## Les 12 règles qu'on applique

1. **On parle dès 0 s, et la première phrase répète la promesse du titre.**
   - « If you stopped eating sugar for two weeks, this is what would happen. » (15,8 M)
   - « Si ton urine fait de la mousse, écoute bien ceci. » (819 k)
2. **La phrase d'ouverture est l'une de ces trois choses :**
   - un « si tu… » ;
   - un symptôme que tu peux vérifier sur toi, avec l'image qui le montre : « Est-ce que vous avez déjà eu la paupière qui tremble comme ça ? » (9,8 M) ;
   - une correction de ce que tu crois : « Ce ne sont pas des points noirs » (11 M) ; « Le meilleur anti-inflammatoire, ce n'est pas le gingembre, ni le curcuma, ni même l'ail » (8 M).
   - Les témoins ratés ouvrent sur une généralité, comme « Le sport booste le système immunitaire » (3,8 k).
3. **Une seule chaîne de causes, qui monte en intensité.** Pas une liste de faits séparés.
   - Zack D. Films (9,8 M) : « Au début, des fourmis… Mais au bout de 3 heures… Après 6 heures… ».
   - Chaque phrase est un événement physique dans ton corps, relié au suivant par « donc », « parce que » ou « mais ».
4. **Chaque étape promet un gain à l'avatar.**
   - Dr Berg (15,8 M) : « Tu vas… tu vas… ».
   - La peur seule fait moins bien : les mots de peur font baisser le taux de clic. Une menace doit toujours être suivie d'une solution faisable (méta-analyse sur 27 372 personnes).
   - Même compte, même format : « arrêter le sucre 2 semaines » fait 5,9 M, « boire du Coca tous les jours » fait 2 000.
5. **Une relance toutes les 8 à 12 s,** en « mais » ou par une question qui arrive avec sa réponse : « Et les fruits ? Innocents. »
6. **Des phrases de 8 à 12 mots en moyenne, en alternant des très courtes et des longues.**
7. **Zéro jargon,** même expliqué, parce qu'il gêne la compréhension (étude sur 650 personnes).
   - « Un petit bouchon invisible » plutôt que « microcomédon ».
   - Le mot savant peut apparaître en étiquette à l'écran.
8. **Des chiffres qu'on voit :** des durées et des quantités, avec une seule source nommée, qui sert d'ancre de confiance.
9. **Une image nouvelle toutes les 3 à 5 s,** qui montre le mot prononcé : environ 12 plans par minute, l'optimum mesuré sur 10 000 TikToks scientifiques.
10. **Aucune image figée :** tout bouge jusqu'à la coupe.
11. **La phrase la plus forte en dernier, puis on coupe net.** Pas d'abonnement ni de teaser.
    - Seules 4 % des vidéos à plus de 5 M de vues ont un appel à s'abonner.
    - Les témoins ratés finissent souvent sur une vente.
12. **Un débit autour de 185 à 200 mots/min en français, et une musique qui pousse** (120 BPM ou plus) tout en restant grave.
    - Une musique rapide rend les démentis d'experts plus persuasifs.

## À tester plus tard sur nos comptes (pas de données solides)

- **Le personnage qui parle à la première personne.**
  - Il cartonne en français sur des sujets dégoûtants : 5,8 M, 3,1 M, 2,9 M, 2,4 M.
  - Il fait un flop sur des sujets neutres : 8 k.
  - Exemple de départ : « Je suis le caséum, je vis au fond de ta gorge… ».
- **Le rythme des relances.**
- **Le coût réel d'un appel à s'abonner.**
