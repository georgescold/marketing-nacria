"""Account 3 / C (BD, @moceaane format): shared style prompts + one entry per carousel (character, 7 scenes, output folder).

A scene is a prompt, or (prompt, [extra reference scenes]) when another character must match an earlier scene.
"""
STYLE = ("Warm semi-realistic 2D digital comic illustration, like a modern French webtoon or storybook, soft cel shading, cosy warm lighting, "
         "detailed but simple backgrounds. Portrait framing. Full-bleed illustration, no border, no frame. No text, no letters, no numbers, "
         "no speech bubbles, no logos. ")
# The user wants the acne clearly visible on every slide, happy endings included (the message is "ta peau change, pas ta valeur",
# not "her skin got clear"). Each story's "char" varies the acne: zones (jaw/chin, cheeks, forehead, temples, back), kind (red
# bumps, whiteheads, deeper jaw bumps, dark or red post-acne marks) and intensity, and scenes never say "faint marks".
ACNE = ("Her acne is clearly visible at normal viewing distance in every scene, happy scenes included: many distinct inflamed red pimples "
        "and bumps with some redness around them, drawn as round soft-edged spots (never lines or stripes), on the zones described for her. "
        "Not hidden by hair, hands, light or makeup unless the scene says so. ")
SAME = ("Use the reference image for the character and the art style: the SAME woman (same face, same hair, same skin tone, same acne spots "
        "in the same places), drawn in exactly the same warm semi-realistic 2D webtoon illustration style with soft cel shading and warm light. "
        + ACNE + "Portrait framing, her face clearly visible. Full-bleed illustration, no border, no frame. No text, no letters, no numbers, "
        "no speech bubbles, no logos. New scene: ")
STILL = " Her acne is still clearly visible."
PHOTO = ("a calm morning by a window in soft daylight, only three simple skincare products lined up, her phone on a small tripod takes a "
         "photo of her face; she looks focused and calm.")

STORIES = {
 "lea": {
  "folder": "exemple 1",
  "char": ("The main character is a 28-year-old French woman with long dark-brown hair in a loose low bun and warm light skin, with acne on "
           "her chin, jaw and lower cheeks: many raised red pimples, a few with white heads, and some red marks. "),
  "s1": "early morning in her small bathroom, she leans toward a round mirror and touches a new pimple on her chin, worried.",
  "s2": "in an open-plan office she sits at her desk while two colleagues glance at her chin and whisper; she hides her chin behind her hand.",
  "s3": "at night on her sofa she scrolls her phone showing the flawless filtered face of an influencer, the screen glow on her sad face.",
  "s4": "sitting on the bathroom floor surrounded by many skincare bottles and jars, she cries with her head on her knees.",
  "s5": PHOTO,
  "s6": "by the window in soft light, she smiles gently with her chin resting on her hands." + STILL,
  "s7": "she walks out of her building into a sunny Parisian street with a tote bag on her shoulder, bare-faced and smiling." + STILL,
 },
 "mariage": {
  "folder": "exemple 2",
  "char": ("The main character is a 30-year-old Black French woman with deep brown skin and natural curly hair tied in a high puff, with acne "
           "on her jaw and cheeks: many raised bumps with a reddish-purple tint, a few bigger deep ones, and many dark post-acne marks. "),
  "s1": "in her cosy apartment she holds a pale blue bridesmaid dress on a hanger in one hand and a small hand mirror in the other, looking worriedly at the breakout on her jaw.",
  "s2": "she sits at her desk on a video call on her laptop with her smiling, excited sister wearing a bridal veil on screen (a Black woman with deep brown skin); she forces a smile while touching her cheek.",
  "s3": "in a bright pharmacy aisle her arms are overflowing with many skincare boxes and bottles, panicked, a few products falling.",
  "s4": "at night in her bathroom, the sink is covered with ten skincare products, her skin is red and irritated, she leans on the sink, exhausted and close to tears.",
  "s5": PHOTO,
  "s6": ("on the wedding morning in a sunny bedroom, she sits in front of a vanity mirror wearing the pale blue bridesmaid dress from the "
         "first scene, a smiling friend applies light makeup on her cheek with a soft brush, two other bridesmaids in pale blue dresses laugh "
         "in the background; she smiles at her reflection." + STILL),
  "s7": ("Use the reference images: the heroine from the first image wearing the pale blue bridesmaid dress she holds there, and her sister "
         "the bride, who is the SAME woman shown on the laptop screen in the second image (Black woman with deep brown skin, dark hair in an "
         "elegant updo, white veil). Same warm semi-realistic 2D webtoon style, both faces clearly visible, full-bleed, no text. Scene: at the "
         "wedding party in a garden at dusk with string lights, the two sisters laugh and dance hand in hand, a photographer in the "
         "background; joyful. The heroine's acne is still clearly visible.", ["s2"]),
 },
 "pilule": {
  "folder": "exemple 3",
  "char": ("The main character is a 26-year-old French woman with light olive skin and a short wavy chestnut bob, with acne along her "
           "jawline and on her chin: a dense cluster of red pimples and a few deeper swollen bumps. "),
  "s1": "in her bathroom she holds an empty contraceptive pill blister pack and touches the new pimples on her jaw in the mirror, puzzled and worried.",
  "s2": "at a Sunday family lunch around a table, an aunt points at her chin with a concerned face while relatives look; she shrinks in her chair, embarrassed.",
  "s3": "at her desk in front of a laptop showing an online calendar with all days crossed out and a far-away free slot, she sighs, head in her hand.",
  "s4": "at night in bed she scrolls her phone, surrounded by many floating phone screens showing influencers giving contradictory advice, confused and overwhelmed.",
  "s5": "a calm morning at her kitchen table, she taps a small red dot on a calendar in her phone app, three simple skincare products lined up next to her coffee; organised and calm.",
  "s6": "weeks later in a bright dermatologist's office, she shows her phone with a row of small weekly photos to a kind female doctor who listens and smiles; she feels heard." + STILL,
  "s7": "walking home in a golden autumn street, wind in her hair, she smiles, at peace." + STILL,
 },
 "rendezvous": {
  "folder": "exemple 4",
  "char": ("The main character is a 25-year-old French woman with fair freckled skin and long auburn hair, with acne on her chin and both "
           "cheeks: many red pimples, some with white heads, clearly distinct from her freckles. "),
  "s1": "sitting on her bed in a cosy sweater she looks at her phone, a big glowing heart icon floating above it (a dating app match), excited; her other hand touches the pimples on her chin.",
  "s2": "the evening before, at her bathroom mirror she applies thick layers of foundation with a sponge, frowning at her cakey reflection.",
  "s3": "the next day, sitting on her bedroom floor against the bed, she types on her phone to cancel the date, sad and ashamed, the dress she planned to wear lying next to her.",
  "s4": "on a sofa her best friend hugs her warmly and comforts her, a box of tissues and two mugs of tea on the table.",
  "s5": PHOTO,
  "s6": "at a sunny café terrace she arrives with light makeup, a bit nervous but smiling, a kind young man with curly dark hair and a light blue shirt stands up and smiles warmly at her." + STILL,
  "s7": ("Use the two reference images: the SAME red-haired woman (same face, freckles, same acne on chin and cheeks) and the SAME young man "
         "with curly dark hair and a light blue shirt from the second image, same warm semi-realistic 2D webtoon style, both faces clearly "
         "visible, full-bleed, no text. Scene: they sit face to face at a small round table on the sunny café terrace with two coffees, "
         "laughing together; she is relaxed and radiant, her acne still clearly visible, he looks into her eyes.", ["s6"]),
 },
 "visio": {
  "folder": "exemple 5",
  "char": ("The main character is a 27-year-old French woman of North African descent with light brown skin and long curly dark hair, with "
           "acne on her forehead and cheeks: many small red pimples and whiteheads on the forehead and a few bigger red ones on the cheeks. "),
  "s1": "at home at her desk, a video meeting on her laptop shows a grid of colleagues; she sees her own face in a small tile and reaches to switch her camera off, uneasy.",
  "s2": "seen from behind her shoulder in a dim room: the laptop screen shows a grid of smiling colleagues and one black tile; she sits slumped, her face half visible in profile, sad.",
  "s3": "her manager speaks to her on the laptop screen; she answers with her camera off, hugging a cushion, embarrassed.",
  "s4": "late at night in her bathroom she pats thick concealer on her forehead, frustrated, many products around the sink.",
  "s5": PHOTO,
  "s6": "close-up of her face lit by the laptop screen as she takes a deep breath before turning her camera on, eyes closed, a small brave smile." + STILL,
  "s7": "she is on a video call with her camera on, laughing with her colleagues on the laptop screen, confident." + STILL,
 },
 "couple": {
  "folder": "exemple 6",
  "char": ("The main character is a 29-year-old French woman of Vietnamese descent with light skin and straight black shoulder-length hair, "
           "with acne on her chin, jaw and cheeks: several deep red swollen bumps, red pimples and red marks. Medium close-up framing in every scene: "
           "her face is large in the frame so her acne is easy to see. Her arms, neck and body have perfectly clear skin: the acne is only "
           "on her face. "),
  "s1": "at dawn in a cosy bedroom she slips quietly out of bed while her boyfriend (a man with short brown hair) still sleeps, touching her chin.",
  "s2": "in the bathroom at dawn she quickly applies foundation over the pimples on her chin, glancing anxiously at the door.",
  "s3": "back in bed with perfect makeup, she pretends to sleep while her boyfriend wakes up beside her; she looks tense.",
  "s4": "one morning her boyfriend opens the bathroom door and finds her bare-faced; she covers her face with her hands, embarrassed.",
  "s5": "in the bathroom her boyfriend gently takes her hands away from her face and smiles at her tenderly." + STILL,
  "s6": ("a calm morning: she sits by the window in the foreground, facing her phone on a small tripod that takes a photo of her face, "
         "three simple skincare products on the table; behind her, her boyfriend brings her a coffee. She is clearly in the scene." + STILL),
  "s7": ("on a lazy Sunday morning, the two of them (only one man in the picture: her boyfriend) sit side by side in bed, laughing "
         "together over coffee; she is bare-faced and relaxed." + STILL),
 },
 "trente": {
  "folder": "exemple 7",
  "char": ("The main character is a 30-year-old French woman with fair skin and wavy shoulder-length blonde hair, with acne on her jaw and "
           "chin: red pimples, a few with white heads, and red post-acne marks. "),
  "s1": "in her living room she holds an old photo of herself as a teenager with acne next to her face, looking at her reflection in a mirror, sighing.",
  "s2": "at her birthday party in a cosy apartment with friends, plain balloons and a cake, she stands at the edge of the group hiding behind her glass.",
  "s3": "a friend raises a phone for a group selfie and she turns her face away from the camera.",
  "s4": "late at night alone in the kitchen with leftover cake, she reads her phone, tired and discouraged.",
  "s5": PHOTO,
  "s6": "on a sofa a friend shows her own chin pimples and they burst out laughing together, relieved." + STILL,
  "s7": "at a sunny picnic in a park she stands in the middle of a group photo with her friends, laughing." + STILL,
 },
 "plage": {
  "folder": "exemple 8",
  "char": ("The main character is a 26-year-old French woman of mixed heritage with medium brown skin and big curly hair, with acne on her "
           "back, shoulders and upper chest: many red pimples and dark marks, and a few pimples on her jaw. "),
  "s1": "in a shop fitting room she tries on a swimsuit and looks over her shoulder at her back in the mirror, covered in pimples, worried.",
  "s2": "at the beach with friends in swimsuits, she stays sitting under a parasol in a long-sleeved shirt.",
  "s3": "her friends wave at her from the sea to join them; she shakes her head, hugging her knees.",
  "s4": "at night in her bathroom she tries to see her back with a hand mirror in front of the big mirror, frustrated.",
  "s5": "a calm morning in her bedroom, three simple skincare products on the dresser, her phone on a small tripod takes a photo of her shoulders and back in soft daylight; she looks calm.",
  "s6": "weeks later at the beach she takes off her shirt in her swimsuit, a little nervous but smiling; the pimples on her back and shoulders are still clearly visible.",
  "s7": "she runs laughing into the sea with her friends, splashing; the pimples on her back and shoulders are still clearly visible.",
 },
 "soeur": {
  "folder": "exemple 9",
  "char": ("The main character is a 28-year-old French woman with light skin and light-brown hair with bangs, with acne on her forehead and "
           "temples: many small red pimples and whiteheads. Her 15-year-old sister has the same hair colour in a ponytail and acne on her "
           "forehead and cheeks. "),
  "s1": "in her teenage sister's bedroom, the 15-year-old sister cries on her bed, face in her pillow, while the heroine stands at the door, worried.",
  "s2": "the heroine sits on the bed next to her sister, who shows her phone with mean comments under a selfie, tears on her cheeks.",
  "s3": "a memory: the heroine as a teenager years ago, crying alone in a similar bedroom, in a softer sepia tone.",
  "s4": "the heroine lifts her bangs to show her own pimples on her forehead; her sister stops crying, surprised.",
  "s5": "in the bathroom both sisters stand side by side at the sink with three simple skincare products, laughing.",
  "s6": "the two sisters take a photo together by the window with a phone on a small tripod, smiling; both still have clearly visible acne.",
  "s7": "the two sisters walk arm in arm down a sunny street, bare-faced and confident; both still have clearly visible acne.",
 },
 "sport": {
  "folder": "exemple 10",
  "char": ("The main character is a 24-year-old Black French woman with dark skin and long box braids, with acne on her forehead and temples "
           "along the hairline: many raised bumps with a reddish-purple tint and dark marks. "),
  "s1": "at the entrance of a gym she pulls the hood of her hoodie over her head to hide her forehead, people working out in the background.",
  "s2": "in the middle of a group workout class, doing squats among other women in tank tops, she keeps her grey hood up, sweating and uncomfortable.",
  "s3": "in the locker room she wipes sweat from her forehead and looks at her pimples in the mirror, frustrated, a tight headband in her hand.",
  "s4": "at home she sits on her bed in front of a pile of products and headbands, discouraged.",
  "s5": "a calm morning in her bathroom, three simple skincare products and a soft clean headband by the sink, her phone on a small tripod takes a photo of her face; she looks calm.",
  "s6": "at the gym she pulls her hood down and ties her braids back, nervous but determined." + STILL,
  "s7": "in the workout class she laughs with a friend while exercising, sweaty and proud." + STILL,
 },
}
