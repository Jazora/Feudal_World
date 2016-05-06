from header_skins import *
####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################

chin_size = 0
chin_shape = 1
chin_forward = 2
jaw_width = 3
jaw_position = 4
mouth_nose_distance = 5
mouth_width = 6
cheeks = 7
nose_height = 8
nose_width = 9
nose_size = 10
nose_shape = 11
nose_bridge = 12
cheek_bones = 13
eye_width = 14
eye_to_eye_dist = 15
eye_shape = 16
eye_depth = 17
eyelids = 18
eyebrow_position = 19
eyebrow_height = 20
eyebrow_depth = 21
eyebrow_shape = 22
temple_width = 23
face_depth = 24
face_ratio = 25
face_width = 26

comp_less_than = -1
comp_greater_than = 1


skins = [
  ("man", 0, "man_body", "man_calf_l", "m_handL", "male_head",
   [(20,  0,  0.7, -0.6, "Chin Size"),
    (260, 0, -0.6,  1.4, "Chin Shape"),
    (10,  0, -0.5,  0.9, "Chin Forward"),
    (240, 0,  0.9, -0.8, "Jaw Width"),
    (210, 0, -0.5,  1.0, "Jaw Position"),
    (250, 0,  0.8, -1.0, "Mouth-Nose Distance"),
    (200, 0, -0.3,  1.0, "Mouth Width"),
    (50,  0, -1.5,  1.0, "Cheeks"),

    (60,  0, -0.4, 1.35, "Nose Height"),
    (70,  0, -0.6,  0.7, "Nose Width"),
    (80,  0,  1.0, -0.1, "Nose Size"),
    (270, 0, -0.5,  1.0, "Nose Shape"),
    (90,  0, -0.2,  1.4, "Nose Bridge"),

    (100, 0, -0.3,  1.5, "Cheek Bones"),
    (150, 0, -0.2,  3.0, "Eye Width"),
    (110, 0,  1.5, -0.9, "Eye to Eye Dist"),
    (120, 0,  1.9, -1.0, "Eye Shape"),
    (130, 0, -0.5,  1.1, "Eye Depth"),
    (140, 0,  1.0, -1.2, "Eyelids"),

    (160, 0,  1.3, -0.2, "Eyebrow Position"),
    (170, 0, -0.1,  1.9, "Eyebrow Height"),
    (220, 0, -0.1,  0.9, "Eyebrow Depth"),
    (180, 0, -1.1,  1.6, "Eyebrow Shape"),
    (230, 0,  1.2, -0.7, "Temple Width"),

    (30,  0, -0.6,  0.9, "Face Depth"),
    (40,  0,  0.9, -0.6, "Face Ratio"),
    (190, 0,  0.0, 0.95, "Face Width"),

    (280, 0,  0.0,  1.0, "Post-Edit"),
   ],
   ["man_hair_s","man_hair_m","man_hair_n","man_hair_o","man_hair_y10","man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_t","man_hair_y6","man_hair_y3","man_hair_y7","man_hair_y9","man_hair_y11","man_hair_u","man_hair_y","man_hair_y2","man_hair_y4","man_hair_y5","man_hair_y8","courthair","shortcut","shortlayer","shortbob"],
   ["beard_e","beard_d","beard_k","beard_l","beard_i","beard_j","beard_z","beard_m","beard_n","beard_y","beard_p","beard_o","beard_v","beard_f","beard_b","beard_c","beard_t","beard_u","beard_r","beard_s","beard_a","beard_h","beard_g","beard_q"],
   ["hair_blonde","hair_red","hair_brunette","hair_black","hair_white"],
   ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"],
   [
    ("manface_young_2",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
    ("manface_midage",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
    ("manface_young",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("manface_young_3",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
    ("manface_7",0xffc0c8c8,["hair_blonde"],[0xff171313, 0xff007080c]),
    ("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),
    ("manface_african",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),
    ("manface_asian1",0xfff4d5bc,["hair_blonde"],[0xff171313, 0xff007080c]),
    ("manface_asian2",0xfff4d5bc,["hair_blonde"],[0xff171313, 0xff007080c]),
    ("manface_asian3",0xffdca486,["hair_blonde"],[0xff171313, 0xff007080c]),
    ("manface_mideast1",0xffaeb0a6,["hair_blonde"],[0xff171313, 0xff007080c]),
    ("manface_mideast2",0xffd0c8c1,["hair_blonde"],[0xff171313, 0xff007080c]),
    ("manface_mideast3",0xffe0e8e8,["hair_blonde"],[0xff171313, 0xff007080c]),
    ("manface_black1",0xffaf785b,["hair_blonde"],[0xff120808, 0xff007080c]),
    ("manface_black2",0xffaf785b,["hair_blonde"],[0xff120808, 0xff007080c]),
    ("manface_black3",0xffaf785b,["hair_blonde"],[0xff120808, 0xff007080c]),
    ("manface_white1",0xffe0e8e8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
    ("manface_white2",0xffe0e8e8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("manface_white3",0xffe0e8e8,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ],
   [(voice_die,"snd_man_die"),
    (voice_hit,"snd_man_hit"),
    (voice_grunt,"snd_man_grunt"),
    (voice_grunt_long,"snd_man_grunt_long"),
    (voice_yell,"snd_man_yell"),
    (voice_stun,"snd_man_stun"),
    (voice_victory,"snd_man_victory"),
   ],
   "skel_human", 1.0, "psys_game_blood","psys_game_blood_2",
   [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)],
    [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
    [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
    [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
    [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
    [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
    [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
    [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
   ]
  ),

  ("woman", skf_use_morph_key_10, "woman_body", "woman_calf_l", "f_handL", "female_head_new",
   [(230,0,0.7,-0.7, "Chin Size"), 
    (220,0,-0.6,0.6, "Chin Shape"), 
    (10,0,-0.5,0.5, "Chin Forward"),
    (20,0,-0.5,0.6, "Jaw Width"), 
    (40,0,-0.7,0.7, "Jaw Position"),
    (90,0,-1.2,1.2, "Jaw Neck"),
    (50,0,-0.8,0.8, "Cheeks 2"),
    (210,0,-0.5,0.5, "Cheeks 1"),
    (100,0,-0.8,0.8, "Cheek Bones"),
    (270,0,0.8,-0.8, "Mouth-Nose Distance"),
    (30,0,-0.6,1.0, "Mouth Width"),
    (160,0,1.0,-0.7, "Lips Position"),

    (60,0,-0.5,0.5, "Nose Height"),
    (70,0,-0.7,0.7, "Nose Width"),
    (80,0,0.5,-1.0, "Nose Size"),
    (240,0,-0.5,0.5, "Nose Shape"),

    (150,0,-0.8,0.8, "Eye Width"),
    (110,0,0.5,-0.5, "Eye to Eye Dist"),
    (120,0,-0.7,0.8, "Eye Shape"),
    (130,0,-1.0,0.7, "Eye Position"),
    (140,0,-1.0,1.0, "Eyelids"),

    (170,0,-0.7,0.7, "Eyebrow Height"),
    (180,0,-1.0,0.7, "Eyebrow Shape"),
    (260,0,0.8,-0.8, "Temple Width"),

    (200,0,0.7,-0.7, "Face tall-short"),
    (250,0,0.8,-0.8, "Face up-down"),
    (190,0,-0.6,1.0, "Face Width"),

    (280,0,0.0,0.7, "Post-Edit"),
   ],
   ["woman_hair_p","woman_hair_n","woman_hair_o","woman_hair_q","woman_hair_r","woman_hair_t","woman_hair_s","woman_hair_10","woman_hair_11","woman_hair_12","woman_hair_13","woman_hair_14","woman_hair_15","woman_hair_16","woman_hair_17","woman_hair_18","woman_hair_19","woman_hair_22","woman_hair_23"],
   ["acc1","acc2","acc3","acc4","acc5","acc6","acc7","acc8","acc9","acc10","acc11","acc12","acc13","acc14"],
   ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
   [],
   [
     ("womanface_01",0xfff2f9f7,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("womanface_02",0xffeaf7ff,["hair_blonde"],[0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("womanface_03",0xffe4eded,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("womanface_04",0xffd5d3b8,["hair_blonde"],[0xff19100c, 0xff0c0d19, 0xff007080c]),
     ("womanface_05",0xff7e7c85,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("womanface_06",0xffeaf0f5,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("womanface_07",0xfff4ffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("womanface_08",0xfff1f1ff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("womanface_09",0xfff6f7f5,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("womanface_10",0xfff6ffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("womanface_11",0xfffbfaf7,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("womanface_12",0xffeaf7ff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("womanface_13",0xffe1e9f0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("womanface_14",0xffeaf7ff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("womanface_15",0xffeaf7ff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("womanface_16",0xfff9faff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
   ],
   [(voice_die,"snd_woman_die"),
    (voice_hit,"snd_woman_hit"),
    (voice_yell,"snd_woman_yell"),
   ],
   "skel_human", 1.0, "psys_game_blood","psys_game_blood_2",
   
   [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)],
    [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
    [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
    [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
    [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
    [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
    [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
    [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
   ]
  ),
  
  ("giant_male", 0, "invisible", "invisible", "invisible", "invisible", 
    [(0,0,0,0, "Chin Size"),
    (0,0,0,0, "Chin Shape"),
    (0,0,0,0, "Chin Forward"),
    (0,0,0,0, "Jaw Width"),
    (0,0,0,0, "Jaw Position"),
    (0,0,0,0, "Mouth-Nose Distance"),
    (0,0,0,0, "Mouth Width"),
    (0,0,0,0, "Cheeks"),

    (0,0,0,0, "Nose Height"),
    (0,0,0,0, "Nose Width"),
    (0,0,0,0, "Nose Size"),
    (0,0,0,0, "Nose Shape"),
    (0,0,0,0, "Nose Bridge"),

    (0,0,0,0, "Cheek Bones"),
    (0,0,0,0, "Eye Width"),
    (0,0,0,0, "Eye to Eye Dist"),
    (0,0,0,0, "Eye Shape"),
    (0,0,0,0, "Eye Depth"),
    (0,0,0,0, "Eyelids"),

    (0,0,0,0, "Eyebrow Position"),
    (0,0,0,0, "Eyebrow Height"),
    (0,0,0,0, "Eyebrow Depth"),
    (0,0,0,0, "Eyebrow Shape"),
    (0,0,0,0, "Temple Width"),

    (0,0,0,0, "Face Depth"),
    (0,0,0,0, "Face Ratio"),
    (0,0,0,0, "Face Width"),

    (0,0,0,0, "Post-Edit"),
    ],
    [],
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"],
    [
		("barf_skull",0xffffffff,["hair_blonde"],[0xffffffff, 0xffffffff]),
     ],
    [],
    "skel_human", 1.12,
    "psys_game_blood","psys_game_blood_2",
  ),

]

