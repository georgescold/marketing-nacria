PHOTO = ("Realistic close-up skin photograph like a dermatology reference picture of real acne, {what}. Warm natural light, soft focus, "
         "real skin texture with visible pores, slightly matte skin, no makeup, natural colours, not glossy, not airbrushed. "
         "Wide landscape framing. No text.")
ORGAN = ("Premium photorealistic 3D medical render, close-up: {organ} fills about 70 percent of the frame width, in its anatomical position, "
         "glossy and slightly translucent, glowing softly from within in {color}, with fine {vessels} blood vessels. Behind it only a faint "
         "dark-blue translucent outline of the body ({body}). Very dark navy background with tiny light particles. The top 15 percent of "
         "the image is dark. No text, no labels, no logo.")
JOBS = {
 "p_menton": ("16:9", PHOTO.format(what="the lower face of a young woman, lips and chin, with three or four red inflamed pimples on the chin")),
 "p_stress": ("16:9", PHOTO.format(what="the cheek of a young woman with a cluster of many small red papules and a few whiteheads, part of her nose and lips visible on the right")),
 "p_machoire": ("16:9", PHOTO.format(what="the jawline and lower cheek of a young woman seen in profile, several small red pimples along the jaw, her lips at the right edge")),
 "p_sucre": ("16:9", PHOTO.format(what="the side of the chin and the jaw of a young woman with olive skin, a cluster of red pimples and small bumps")),
 "p_nez": ("16:9", PHOTO.format(what="an extreme close-up of a young woman's nose (nose tip, nostrils, a bit of the upper lip), ONE single red inflamed pimple on the tip of the nose with a soft red halo, exactly in the centre")),
 "p_sommeil": ("16:9", PHOTO.format(what="the forehead of a young woman with her hairline at the top, a few red pimples in the centre of the forehead")),
 "o_ovaires": ("4:3", ORGAN.format(organ="the uterus with the fallopian tubes and the two ovaries", color="pink-red", vessels="red", body="hips")),
 "o_surrenales": ("4:3", ORGAN.format(organ="the two kidneys with the two adrenal glands on top of them, the adrenal glands glowing bright orange", color="purple-blue for the kidneys and orange for the adrenal glands", vessels="red and orange", body="lower back")),
 "o_hormones": ("4:3", ORGAN.format(organ="the endocrine glands (pituitary gland, thyroid, adrenal glands) linked together by a bright network of glowing blue neurons", color="pink-orange glands and electric blue neurons", vessels="red", body="torso")),
 "o_pancreas": ("4:3", ORGAN.format(organ="the pancreas next to the stomach", color="orange", vessels="red", body="torso")),
 "o_sebum": ("4:3", ORGAN.format(organ="a large magnified human skin pore with its hair follicle and a swollen sebaceous oil gland full of sebum, seen as a realistic anatomical cut-away", color="orange-yellow", vessels="red", body="a face in profile")),
 "o_cerveau": ("4:3", ORGAN.format(organ="the human brain", color="pink-violet with electric blue neurons", vessels="red", body="head")),
}
