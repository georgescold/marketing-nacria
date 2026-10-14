STYLE = ("Photorealistic 3D medical illustration, landscape, in the style of a premium anatomy render. A translucent glassy dark-blue human "
         "{body} seen from the front against a very dark navy background, faint blue outlines of the skeleton and blood vessels, a few soft "
         "light particles. Inside it, in its true anatomical position and LARGE in the frame, {organ}, rendered realistically and glossy in "
         "{color}, with fine red and orange blood vessels, softly glowing from within. The top fifth of the image is dark. Centred, high detail. "
         "No text, no labels, no logo.")
TORSO, PELVIS, HEAD = "neck and torso", "torso down to the pelvis", "head and neck"
Y = {
 "y_ovaires": (PELVIS, "the female reproductive organs: the uterus, the fallopian tubes and the two ovaries", "pink-red"),
 "y_sopk": (PELVIS, "the uterus and two enlarged ovaries covered with many small round fluid-filled cysts", "pink-purple"),
 "y_hormones": (TORSO, "the endocrine glands lit up together: the pituitary gland in the head, the thyroid in the neck and the adrenal glands on top of the kidneys, linked by glowing blue nerve-like lines", "orange and electric blue"),
 "y_surrenales": (TORSO, "the two kidneys with the adrenal glands on top of them glowing bright orange", "purple-blue kidneys and bright orange adrenal glands"),
 "y_pancreas": (TORSO, "the pancreas next to the stomach and duodenum, its insulin-producing islets glowing", "orange"),
 "y_cerveau": (HEAD, "the human brain", "pink-violet with electric blue highlights"),
 "y_sebum": (HEAD, "the face's oil (sebaceous) glands glowing as tiny dots densely concentrated on the nose, the forehead and the chin (T-zone)", "orange"),
 "y_cuir_chevelu": (HEAD, "the scalp's hair follicles and oil glands glowing along the hairline and over the top of the head", "orange"),
}
JOBS = {k: ("4:3", STYLE.format(body=b, organ=o, color=c)) for k, (b, o, c) in Y.items()}
