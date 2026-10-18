# Process vidéo « X expliqués en 60 secondes »

Ce process est copié sur @learning.of.theday (analyse : `reports/Analyse learning.of.theday.md`). Il sert pour tous les comptes vidéo. Il a été validé par l'utilisatrice sur E01 à E03 du compte Acné (« Incroyable », « parfait », « c'est exactement ça »).

## Les comptes

| Compte | Remplace | Série | DA | Dossier de sortie |
|---|---|---|---|---|
| `acne` | le compte carrousel « Acné solution » | « Les boutons expliqués », etc. | porcelaine nacrée sur encre prune, Fraunces + DM Sans | `Posts TikTok/compte vidéo/` |
| `organes` | les carrousels Organes (style @factslipv9n) | « Ton visage décodé », etc. | « scanner » : hologramme anatomique bleu, organe lumineux, jaune d'alerte #F6E13C, Open Sans ExtraBold | `Posts TikTok/compte organes/vidéo/` |
| `nutrition` | nouveau compte, personnage Margot (IA, aucun diplôme revendiqué) | « Les aliments accusés », etc. | « food noir et verdict » : photo culinaire sur vert forêt, tampon de preuve, Fraunces Black + DM Sans | `Posts TikTok/compte nutrition/vidéo/` |

Tout est déclaré dans `comptes.py`. Pour chaque compte :
- un plan (`plan.py`, `plan_organes.py`) : 6 chapitres × 8 parties, DA et prompts ;
- un module de miniatures (`miniatures.py`, `miniatures_organes.py`) : héros, couvertures, polices et couleurs du rendu ;
- un module d'épisodes (`episodes.py` avec E01…, `episodes_organes.py` avec O01…).

La voix, l'alignement, la musique, le mix, le pic du CTA et le rendu sont communs.

**Nouveau compte :**
1. Créer `plan_X.py`, `miniatures_X.py` (mêmes noms d'interface que `miniatures_organes.py`) et `episodes_X.py`.
2. L'ajouter à `comptes.ACCOUNTS`.
3. Choisir la photo de profil (emblème du CTA).

## Règles fixes (validées par l'utilisatrice)

- **Durée libre** (15/10) : 1 min comme 1 min 30, c'est le script qui décide. On ne coupe jamais une explication et on n'accélère jamais une voix pour tenir dans 60 s.

- **Budget : 2 $ maximum par vidéo** (en pratique 1,1 à 1,5 $). Les coûts réels se lisent sur l'API usage de fal : `GET https://api.fal.ai/v1/models/usage?endpoint_id=…&expand=time_series`, en sommant `cost`. Les prix affichés mentent : Wan en 1080p revient à environ 1 $ le clip. Annoncer le coût avant un lot payant.
- **Format :**
  - 1 chapitre = 8 parties, la saison = 6 chapitres = 48 vidéos ;
  - 160 à 230 mots, 55 à 70 s ;
  - publication : 1 par jour, le matin.
- **Script :**
  1. Le titre de série est lu (« Les boutons expliqués. Partie 4. La tête blanche. »).
  2. Accroche choc à la 2e personne (mythe ou chiffre).
  3. Mécanisme pas à pas, avec des images simples.
  4. Un chiffre sourcé environ toutes les 10 s.
  5. Une nuance.
  6. Chute en antithèse (« Ce n'est pas X. C'est Y. »).
  7. CTA.
- **Vérité :**
  - les mythes ne servent que d'accroches cassées ;
  - jamais de fausse promesse santé, ni de diagnostic, ni de marque ;
  - un signe médical renvoie vers un médecin.
- **CTA final :** dans l'énergie du reportage, il fait monter l'émotion (pas de boucle).
  - Texte : « Le X, c'est le Nième. Il en reste N. Pour enfin tous les comprendre, abonne-toi. » Il doit contenir « Pour » et « abonne ».
  - Visuel : la grille du chapitre s'allume, puis l'emblème (photo de profil), un badge « + » qui pulse et « Abonne-toi ». Tenue 1,3 s.
  - Son : un riser culmine sur « abonne-toi », un impact tombe avec le « + », la musique monte de 5 dB à partir de « Pour » et reste haute, coupure en fondu de 0,15 s.
- **Voix :**
  - Gemini 3.8 Flash TTS, voix **Despina**, style `reportage_cta` (grave, une seule prise CTA compris) ;
  - `voix.tighten()` ramène les pauses à 0,33 s de médiane ;
  - alignement **local** wav2vec2 FR (gratuit, 15 ms de médiane).
- **Musique :**
  - Lyria 3.5 (0,10 $), brief « documentaire d'investigation » découpé en sections calées sur les lignes (`score(...)`) ;
  - 9,7 dB sous la voix (mesure K-weighted du compte modèle), total −14,4 LUFS en loudnorm deux passes, sans ducking ;
  - les creux sont comblés par le drone `sons/drone_2.mp3` ;
  - si la piste meurt avant la fin, elle est prolongée par une reprise du passage le plus intense.
- **Visuels :**
  - une image de départ par scène (Nano Banana, 0,04 $, 9:16) ;
  - clips Grok Imagine lite (environ 0,033 $/s, 2 à 4 s), caméra fixe (préfixe `MOTION`) ;
  - le clip est accéléré ×1 à ×2 pour que l'action finisse à 90 % de la ligne, puis l'image tient ;
  - le reste bouge en code : lueur qui respire, `fx` « sweep » (lumière rasante) ou « scan » (ligne de scanner, Organes), compteurs, anneau jaune (Organes).
- **Miniature (refaite le 14/10, « pas assez envie de cliquer ») :** structure exacte du modèle, tout dans le carré central (y 420 à 1500) :
  1. titre de série en capitales blanches sur 2 lignes équilibrées ;
  2. pastille « PARTIE N » colorée ;
  3. l'objet ;
  4. le sujet en énormes capitales colorées (sans article) ;
  5. l'accroche en antithèse en blanc dessous (`COVER_HOOK`, sinon la 1re phrase de la chute).
  La même image sert de carte « Partie N » dans la vidéo.
- **Légende :**
  - `TITRE` = « Série · Partie N : Titre » ;
  - `DESCRIPTION` = l'antithèse, puis « Ce que la vidéo n'a pas eu le temps de dire. », puis des paragraphes sourcés (auteur, revue, année), puis 5 hashtags (dont #acneadulte sur Acné).

## Format Nutrition (« Ta peau dans l'assiette », depuis le 15/10)

1. **Ouverture.** Une question directe à laquelle la vidéo répond (« Est-ce que le chocolat donne vraiment des boutons ? »). Elle est dite et écrite en grand sur le plan le plus fort (`open="question"`), sans grille des aliments.
2. **Promesse tenue.** La promesse du hook se referme plus tard dans la vidéo.
3. **Margot.** Elle se présente une fois : « spécialiste de la nutrition cutanée », et elle dit quelles études elle a épluchées, avec une formulation différente à chaque épisode. Pendant ce temps, les études de CET épisode défilent (`montage`), jamais les autres aliments.
4. **Verdict.** Il répond à la question d'ouverture (« Alors, le chocolat donne-t-il des boutons ? Mon verdict : probablement oui. »). Le tampon porte l'affirmation jugée (`verdict=(ligne, "PROBABLE", "probablement", "le chocolat donne des boutons")`).
5. **Voix.** `Erinome:nutri_jeune` (jeune, percutante), avec `fluid=True` : une respiration par phrase, jamais de pause à l'intérieur. Utiliser `produire.ps1 <EP>` (ou `prises.py <EP> 4 <ligne de Margot>`).
   - **Rythme humain**, comme le compte modèle : 190 à 210 mots/min, environ 0,65 s après la question, environ 0,5 s après chaque phrase.
     - Si la prise dépasse 215 mots/min ou si la question d'ouverture s'enchaîne sans respiration, c'est « pas humain » (retour de l'utilisatrice sur N03).
   - **Débit constant** : le même débit du début à la fin, l'énergie passe par l'intonation et non par la vitesse.
     - Gemini variait de 6,2 à 9,4 syllabes/s d'une ligne à l'autre ; l'utilisatrice l'a entendu comme « des accélérations de voix » à chaque changement de plan.
   - **Ne jamais retoucher la voix** (15/10, deux essais ratés).
     - `regulate` posait des silences calibrés, coupait les blancs entre les mots et étirait les phrases : la voix devenait « robotique », « en double », avec « des coupures » et « moins de dynamisme ».
     - `prises.py` passe maintenant chaque prise dans `voix.natural`, qui garde la prise telle quelle et raccourcit seulement les pauses trop longues :
       - elle coupe à l'intérieur du vrai silence, avec des fondus de 20 ms ;
       - les respirations restent ;
       - la question d'ouverture garde au moins 0,6 s ;
       - le volume n'est corrigé que sur une phrase décalée de plus de 3 dB.
     - Le dynamisme et la régularité viennent de la voix elle-même : on demande un débit soutenu, chiffré (« environ 200 mots par minute… ne ralentit jamais »).
     - 4 prises par vidéo ; on garde celle qui est la plus proche du centre de la fourchette `wpm`, la plus régulière d'une ligne à l'autre et la plus vivante (variation de la mélodie de la voix, `voix.expressiveness`).
     - `produire.ps1 <EP> [<EP>…]` enchaîne prises, musique, rendu et copies finales.
   - La clé `wpm` de l'épisode donne une fourchette : (195, 215) par défaut, (190, 210) pour les Organes.

## Format Organes (v3, depuis le 15/10)

1. **Ouverture.** Une question sur la zone (« Des boutons sur le menton, toujours au même endroit ? »), écrite en grand sur la PHOTO du vrai bouton, avec l'anneau blanc (`open="question"`, `miniatures_organes.question_layer`). Pas de titre de série parlé avant.
2. **Le vrai bouton.** Toute ligne qui montre le bouton est une photo macro de peau réelle (`photo=[...]`, `plan_organes.PHOTO`), comme le haut des carrousels. Jamais de boule rouge lumineuse sur l'hologramme. L'hologramme reste pour les organes et les mécanismes.
   - 1 à 3 boutons, jamais symétriques. Mesurer l'anneau sur la photo ; le zoom avance vers lui.
3. **Pas de formule mécanique.** Pas de « Le test : » ni de tournure répétée d'une vidéo à l'autre : les conseils sont dits naturellement.
3 bis. **Aucune allusion à une autre vidéo, aucune boucle ouverte** (tous les comptes). Ce qui est annoncé dans une vidéo y trouve sa réponse.
   - Jamais « je t'explique dans la partie 8 ».
   - Pour ne pas spoiler un autre épisode, on répond en termes généraux (« ce duo peut signaler un déséquilibre hormonal, et ça se traite »).
4. **Voix.** `Despina:reportage_suspense` (débit constant), `fluid=True`, `wpm=200`, `prises.py <EP> 3 1`.

## Produire un épisode (FAL_KEY dans l'environnement)

Toutes les commandes se lancent depuis `outils/video/`. Les fichiers déjà présents sont conservés : on peut relancer une étape sans rien repayer.

1. **Écrire l'épisode** dans le module d'épisodes du compte :
   - `lines` : (texte, prompt de la 1re image ou None, couleurs, compteur) ;
   - `chain` {i: j} : la scène i démarre sur la dernière image de j ;
   - `reuse` {i: (épisode, j, avec_clip)} : la scène vient d'un épisode précédent, gratuitement ;
   - `motion`, `anim`, `fx`, `clip_end`, `music=score(...)`, `caption` ;
   - Organes seulement : `glow`, `keys`, `ring`.
2. Voix, environ 0,05 $ :

   ```bash
   python assets.py <EP> voice Despina:reportage_suspense
   ```

   Quand une phrase doit coller au reste de la prise, par exemple la présentation de Margot, utiliser plutôt l'outil de prises (3 prises ≈ 0,15 $). Il garde la prise où cette ligne a le débit et le volume les plus proches du reste. Ne jamais greffer une phrase régénérée seule : ça s'entend toujours.

   ```bash
   python prises.py <EP> 3 <ligne>
   ```
3. Images de départ, 0,04 $ par image :

   ```bash
   python assets.py <EP> images
   ```

   Les regarder. Pour Organes, mesurer les positions de `ring`.
4. Clips, environ 0,07 à 0,10 $ chacun, dans l'ordre des chaînes :

   ```bash
   python assets.py <EP> anim grok
   ```

   Regarder les dernières images et poser `clip_end` si un clip en fait trop.
5. Musique, 0,10 $, puis copier `music_lyria.mp3` en `music.mp3` :

   ```bash
   python musique.py <EP> lyria
   ```
6. Images de contrôle, puis rendu final :

   ```bash
   python render_video.py <EP> 1 20 40
   python render_video.py <EP>
   ```

   Le rendu produit `video.mp4`, à copier en `<EP court> - <Titre>.mp4`.
7. Miniature : `python miniatures.py C1.4` (ou `miniatures_organes.py`), copiée en `<EP court> - Miniature.jpg`. Créer aussi `<EP court> - Légende.txt` (TITRE + DESCRIPTION).
8. Vérifier le coût réel via l'API usage.

## Sous-titres

- Aucune ponctuation à l'écran (`render_video.bare`) : seuls « ? » et « ! » restent, collés à leur mot.
- Découpe : toujours à la fin d'une phrase. À une virgule ou à deux-points, seulement si le morceau fait déjà 14 caractères ; sinon les énumérations faisaient défiler des mots isolés (« cires ») trop vite pour être lus. Un sous-titre ne finit jamais sur un petit mot (« de », « ce », « tu »…).
- Organes : 3 ou 4 mots par sous-titre, sur une seule ligne (taille 54, `maxlen` 24).

## Pièges connus

- `cv2.imwrite` échoue sur les chemins accentués : enregistrer via PIL.
- transformers importe sklearn, qui plante sur l'ABI numpy : `voix.align_local` neutralise `is_sklearn_available`.
- Le filtre de contenu de fal bloque les doigts qui pressent : utiliser des flèches en argile.
- Grok exagère parfois (boule géante, objet qui se déforme) : préciser le prompt ou couper avec `clip_end`.
- Une scène chaînée hérite des défauts de sa source : rechaîner depuis une image propre.
- Nano Banana Pro peut rendre une image encadrée : ajouter « Full-bleed, no border ».
- Les heredocs avec accents passent en cp1252 sous Windows : écrire les patchs avec l'outil Write.
- Environ 1 clip Grok sur 3 en fait trop à la fin (boule rouge géante, gelée, objet qui change de couleur). Toujours regarder le début, le milieu et la fin de chaque clip :
  - poser `clip_end` ;
  - sinon passer la ligne en image fixe (la retirer de `anim` et mettre le .mp4 de côté) ;
  - sinon rechaîner : supprimer l'image et le clip de la scène suivante, puis relancer `anim`.
  Les images fixes chaînées se recréent gratuitement en relançant `anim` une fois leur .png supprimé.
- Organes : dans le style hologramme, « sang » fait apparaître un cœur. Décrire des objets de labo isolés et interdire tout organe dans le prompt. Mesurer `ring` sur l'image générée (centre des pixels rouges).
- Grok ignore les images de fin et a tendance à « remplir » plutôt qu'à « vider » (N01 : il a versé du lait sur « le lien disparaît »). Pour une action qui doit finir dans un état précis (se vider, disparaître, s'éteindre) :
  1. créer l'image de fin avec `assets.end_frame(png, "changement", png_end)` (0,04 $) ;
  2. animer ce plan avec le moteur `h3`, qui respecte l'image de fin (environ 0,05 $).
- Partie 8 d'un chapitre : le CTA annonce le chapitre suivant (« Le chapitre suivant parle de tes hormones. Pour ne pas le rater, abonne-toi. »).
