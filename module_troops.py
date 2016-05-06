from header_common import *
from header_items import *
from header_troops import *
from header_skills import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id
#  2) Toop name (string)
#  3) Plural troop name (string)
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene and entry
#   5.1) Scene (only applicable to heroes)
#   5.2) Entry point using the entry() function: for example, entry(15)
#  6) Reserved (int). Put constant "reserved" or 0
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
####################################################################################################################

def wp(x):
  return wp_one_handed(x)|wp_two_handed(x)|wp_polearm(x)|wp_archery(x)|wp_crossbow(x)|wp_throwing(x)

def wpe(m,a,c,t):
  return wp_one_handed(m)|wp_two_handed(m)|wp_polearm(m)|wp_archery(a)|wp_crossbow(c)|wp_throwing(t)

def wpex(o,w,p,a,c,t):
  return wp_one_handed(o)|wp_two_handed(w)|wp_polearm(p)|wp_archery(a)|wp_crossbow(c)|wp_throwing(t)

def wp_melee(x):
  return wp_one_handed(x + 20)|wp_two_handed(x)|wp_polearm(x + 10)

reserved = 0
no_scene = 0

default_face_1 = 0x0000000400000001124000000020000000000000001c00800000000000000000
default_face_2 = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield

# troops have 30 charisma and 10 weapon master to stop the game engine from adding random skill levels
pw_attr = cha_30|level(1)
knows_pw = knows_weapon_master_10

troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,0, [],
   str_15|agi_15|int_4|cha_4,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all,0,0,0, [],
   str_14, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all,0,0,0, [],
   str_14, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,0,[],0,0,0,0],
####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  
  #Basic Tier
  ["peasant","Peasant","a peasant",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_old_coarse_tunic","itm_ragged_shirt","itm_woolen_hose"],
   str_9|agi_11|pw_attr,wpex(50,30,30,0,0,30),knows_pw|knows_power_strike_1|knows_athletics_2|knows_labouring_2|knows_tailoring_1|knows_riding_1,default_face_1,default_face_2],
  ["peasant_female","Peasant","a peasant",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_dress","itm_blue_dress","itm_peasant_dress","itm_woolen_dress","itm_ripped_woolen_hose","itm_woolen_hose","itm_blue_hose"],
   str_9|agi_11|pw_attr,wpex(50,30,30,0,0,30),knows_pw|knows_power_strike_1|knows_athletics_2|knows_labouring_2|knows_tailoring_1|knows_riding_1,default_face_1,default_face_2],
  ["serf","Serf","a serf",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_heraldic_coarse_tunic","itm_woolen_hose"],
   str_8|agi_10|pw_attr,wpex(50,30,30,0,0,50),knows_pw|knows_power_strike_1|knows_athletics_2|knows_labouring_5|knows_engineer_1|knows_tailoring_1|knows_herding_3|knows_riding_1,default_face_1,default_face_2],
  ["serf_female","Serf","a serf",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_heraldic_blue_dress","itm_heraldic_peasant_dress","itm_ripped_woolen_hose","itm_woolen_hose","itm_blue_hose"],
   str_8|agi_10|pw_attr,wpex(50,30,30,0,0,50),knows_pw|knows_power_strike_1|knows_athletics_2|knows_labouring_5|knows_engineer_1|knows_tailoring_1|knows_herding_3|knows_riding_1,default_face_1,default_face_2],
  ["beggar","Beggar","a beggar",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_ragged_shirt","itm_tattered_wrapping_boots"],
   str_11|agi_13|pw_attr,wpex(60,40,60,10,40,60),knows_pw|knows_ironflesh_1|knows_power_strike_1|knows_athletics_5|knows_riding_1|knows_looting_2|knows_labouring_2,default_face_1,default_face_2],
  ["ministrel","Minstrel","a minstrel",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_old_tabard","itm_woolen_hose"],
   str_10|agi_12|pw_attr,wpex(50,30,30,0,0,80),knows_pw|knows_musician_3|knows_athletics_5|knows_riding_3,default_face_1,default_face_2],
  ["huntsman","Huntsman","a huntsman",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_ragged_woolen_cap","itm_old_coarse_tunic","itm_crude_bow","itm_bent_arrows","itm_woolen_hose"],
   str_11|agi_13|pw_attr,wpex(70,35,60,120,100,50),knows_pw|knows_ironflesh_2|knows_power_strike_1|knows_power_draw_3|knows_athletics_3|knows_riding_1|knows_labouring_1|knows_herding_3,default_face_1,default_face_2],
  ["alchemist","Alchemist","a alchemist",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_black_robe","itm_woolen_hose"],
   str_9|agi_12|pw_attr,wpex(70,30,30,20,20,20),knows_pw|knows_athletics_3|knows_riding_3|knows_alchemy_3|knows_wound_treatment_1|knows_labouring_1,default_face_1,default_face_2],
  ["healer","Healer","a healer",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_old_linen_tunic","itm_woolen_hose"],
   str_8|agi_9|pw_attr,wpex(70,10,20,0,0,5),knows_pw|knows_athletics_1|knows_riding_1|knows_wound_treatment_2|knows_alchemy_1|knows_labouring_1|knows_tailoring_2,default_face_1,default_face_2],
  ["monk","Monk","a monk",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_friar_sandals","itm_friar_robe","itm_brown_hood"],
   str_8|agi_9|pw_attr,wpex(25,10,80,0,0,30),knows_pw|knows_athletics_1|knows_riding_1|knows_wound_treatment_1|knows_engineer_1|knows_labouring_5|knows_tailoring_1|knows_herding_2,default_face_1,default_face_2],
  ["militia","Militia","a militia",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_ragged_woolen_cap","itm_heraldic_coarse_tunic","itm_woolen_hose"],
   str_13|agi_12|pw_attr,wpex(90,40,80,10,40,50),knows_pw|knows_ironflesh_2|knows_power_strike_2|knows_athletics_2|knows_riding_1|knows_labouring_1|knows_herding_2|knows_wage_1,default_face_1,default_face_2],
  ["footman","Footman","a footman",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_arming_cap","itm_heraldic_shirt","itm_tattered_wrapping_boots"],
   str_15|agi_14|pw_attr,wpex(100,100,130,10,45,80),knows_pw|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_shield_1|knows_athletics_5|knows_riding_2|knows_sailing_3|knows_wage_1,default_face_1,default_face_2],
  ["archer","Archer","an archer",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_tattered_headcloth","itm_heraldic_shirt","itm_tattered_wrapping_boots"],
   str_14|agi_14|pw_attr,wpex(90,60,70,125,50,50),knows_pw|knows_ironflesh_4|knows_power_strike_3|knows_power_draw_4|knows_athletics_4|knows_riding_2|knows_sailing_3|knows_wage_1,default_face_1,default_face_2],
  ["crossbowman","Crossbowman","a crossbowman",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_ragged_woolen_cap","itm_heraldic_shirt","itm_tattered_wrapping_boots"],
   str_14|agi_14|pw_attr,wpex(90,60,60,50,125,50),knows_pw|knows_ironflesh_3|knows_power_strike_2|knows_athletics_4|knows_riding_2|knows_sailing_3|knows_wage_1,default_face_1,default_face_2],
  ["lancer","Lancer","a lancer",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_arming_cap","itm_heraldic_shirt","itm_tattered_wrapping_boots"],
   str_14|agi_14|pw_attr,wpex(90,60,120,10,30,80),knows_pw|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_athletics_1|knows_riding_6|knows_wage_1,default_face_1,default_face_2],
  ["man_at_arms","Man at Arms","a man at arms",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_arming_cap","itm_tabard","itm_old_hide_boots"],
   str_15|agi_15|pw_attr,wpex(105,120,110,20,50,30),knows_pw|knows_ironflesh_4|knows_power_strike_4|knows_shield_1|knows_athletics_2|knows_riding_4|knows_wage_1,default_face_1,default_face_2],
  ["sergeant","Sergeant","a sergeant",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_arming_cap","itm_tabard","itm_old_hide_boots"],
   str_15|agi_15|pw_attr,wpex(110,125,110,20,60,40),knows_pw|knows_ironflesh_5|knows_power_strike_4|knows_shield_2|knows_athletics_5|knows_riding_2|knows_wage_1,default_face_1,default_face_2],
  ["engineer","Engineer","an engineer",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_tattered_headcloth","itm_tabard","itm_old_hide_boots","itm_tattered_wrapping_boots",],
   str_10|agi_12|pw_attr,wpex(90,50,60,30,65,50),knows_pw|knows_ironflesh_2|knows_power_strike_2|knows_athletics_2|knows_engineer_2|knows_siege_1|knows_riding_2|knows_looting_1|knows_sailing_4|knows_wage_1,default_face_1,default_face_2],
  ["sailor","Sailor","a sailor",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_ragged_woolen_cap","itm_old_hide_boots"],
   str_14|agi_12|pw_attr,wpex(95,70,80,30,40,70),knows_pw|knows_ironflesh_3|knows_power_strike_3|knows_athletics_2|knows_sailing_9|knows_riding_1|knows_wage_1,default_face_1,default_face_2],
  ["blacksmith","Blacksmith","a Blacksmith",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_ragged_leather_apron","itm_old_hide_boots"],
   str_14|agi_12|pw_attr,wpex(90,55,70,30,70,50),knows_pw|knows_ironflesh_3|knows_power_strike_4|knows_athletics_1|knows_engineer_7|knows_tailoring_5|knows_riding_2|knows_looting_2|knows_sailing_4,default_face_1,default_face_2],
  ["armoursmith","Armourer","a armourer",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_ragged_leather_apron","itm_old_hide_boots"],
   str_14|agi_12|pw_attr,wpex(90,55,70,30,70,50),knows_pw|knows_ironflesh_3|knows_power_strike_4|knows_athletics_1|knows_engineer_5|knows_tailoring_7|knows_riding_2|knows_looting_2|knows_sailing_4,default_face_1,default_face_2],
  ["doctor","Doctor","a doctor",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_black_robe","itm_black_hood","itm_ripped_woolen_hose"],
   str_10|agi_10|pw_attr,wpex(70,40,50,10,20,30),knows_pw|knows_athletics_2|knows_power_strike_2|knows_wound_treatment_5|knows_alchemy_2|knows_riding_2,default_face_1,default_face_2],
  ["traveler","Traveler","a traveler",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_old_coarse_tunic","itm_old_hide_boots",],
   str_11|agi_13|pw_attr,wpex(70,40,90,10,40,60),knows_pw|knows_ironflesh_1|knows_power_strike_2|knows_athletics_5|knows_sailing_7|knows_riding_3|knows_labouring_1|knows_tailoring_2,default_face_1,default_face_2],
  ["herdsman","Herdsman","a herdsman",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_old_coarse_tunic","itm_ragged_shirt","itm_tattered_wrapping_boots","itm_herding_crook"],
   str_10|agi_14|pw_attr,wpex(50,35,40,0,10,40),knows_pw|knows_power_strike_1|knows_athletics_5|knows_labouring_2|knows_riding_3|knows_herding_5,default_face_1,default_face_2],
  ["merchant","Merchant","a merchant",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_rich_outfit","itm_ripped_woolen_hose",],
   str_12|agi_13|pw_attr,wpex(50,40,50,10,20,60),knows_pw|knows_ironflesh_1|knows_power_strike_1|knows_athletics_5|knows_sailing_7|knows_riding_6|knows_trade_2|knows_labouring_1|knows_herding_1,default_face_1,default_face_2],
  
  #Mercenary Tier
  ["mercenary_crossbowman","Mercenary Crossbowman","a mercenary crossbowman",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_ragged_woolen_cap","itm_old_coarse_tunic","itm_old_tabard","itm_tattered_wrapping_boots"],
   str_14|agi_14|pw_attr,wpex(60,70,70,50,125,50),knows_pw|knows_ironflesh_3|knows_power_strike_2|knows_athletics_4|knows_riding_2|knows_sailing_3,default_face_1,default_face_2],
  ["mercenary_cavalry","Mercenary Cavalry","a mercenary cavalry",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_ragged_woolen_cap","itm_old_coarse_tunic","itm_tattered_wrapping_boots"],
   str_14|agi_14|pw_attr,wpex(90,60,120,10,30,80),knows_pw|knows_ironflesh_3|knows_power_strike_3|knows_athletics_1|knows_riding_6,default_face_1,default_face_2],
  ["mercenary_hired_blade","Hired Blade","a hired blade",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_ragged_woolen_cap","itm_old_coarse_tunic","itm_old_tabard","itm_tattered_wrapping_boots"],
   str_15|agi_14|pw_attr,wpex(90,110,110,10,35,80),knows_pw|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_shield_1|knows_athletics_5|knows_riding_2|knows_sailing_3,default_face_1,default_face_2],
  ["mercenary_sword_sister","Sword Sister","a sword sister",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_ragged_woolen_cap","itm_old_coarse_tunic","itm_old_tabard","itm_tattered_wrapping_boots"],
   str_15|agi_14|pw_attr,wpex(90,110,110,10,35,80),knows_pw|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_shield_1|knows_athletics_5|knows_riding_2|knows_sailing_3,default_face_1,default_face_2],
   
  ["mercenary_end","playable_troops_end","playable_troops_end",0,0,0,0,[],0,0,0,0,0],
  
  ##Cultural Tier
  #Swadia
  ["knight","Knight","a knight",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_arming_cap","itm_tabard","itm_old_hide_boots"],
   str_15|agi_15|pw_attr,wpex(105,120,125,20,50,30),knows_pw|knows_ironflesh_4|knows_power_strike_5|knows_shield_2|knows_athletics_2|knows_riding_5|knows_wage_1,default_face_1,default_face_2],
   
  #Rhodok
  ["sharpshooter","Sharpshooter","a sharpshooter",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_ragged_woolen_cap","itm_heraldic_shirt","itm_tattered_wrapping_boots"],
   str_14|agi_14|pw_attr,wpex(90,60,60,50,140,50),knows_pw|knows_ironflesh_3|knows_power_strike_3|knows_shield_1|knows_athletics_4|knows_riding_2|knows_sailing_3|knows_wage_1,default_face_1,default_face_2],
    
  #Nord
  ["huscarl","Huscarl","a huscarl",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_arming_cap","itm_tabard","itm_old_hide_boots"],
   str_17|agi_14|pw_attr,wpex(125,120,125,20,60,80),knows_pw|knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_power_throw_1|knows_athletics_5|knows_riding_2|knows_wage_1,default_face_1,default_face_2],
  ["shieldmaiden","Shield Maiden","a shield maiden",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_arming_cap","itm_tabard","itm_old_hide_boots"],
   str_17|agi_14|pw_attr,wpex(125,120,125,20,60,80),knows_pw|knows_ironflesh_5|knows_power_strike_5|knows_shield_3|knows_power_throw_1|knows_athletics_5|knows_riding_2|knows_wage_1,default_face_1,default_face_2],
  
  #Sarranid
  ["mamaluke","Mamaluke","a mamaluke",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_arming_cap","itm_tabard","itm_old_hide_boots"],
   str_15|agi_16|pw_attr,wpex(120,105,110,20,50,30),knows_pw|knows_ironflesh_3|knows_power_strike_4|knows_shield_1|knows_athletics_3|knows_riding_7|knows_wage_1,default_face_1,default_face_2],
  ["slave","Slave","a slave",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_tattered_wrapping_boots"],
   str_14|agi_15|pw_attr,wpex(90,100,130,10,45,80),knows_pw|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_shield_1|knows_athletics_5|knows_riding_2|knows_sailing_3|knows_labouring_2,default_face_1,default_face_2],
  
  #Vaegir
  ["marksman","Marksman","an marksman",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_tattered_headcloth","itm_heraldic_shirt","itm_tattered_wrapping_boots"],
   str_14|agi_14|pw_attr,wpex(90,60,70,145,50,50),knows_pw|knows_ironflesh_4|knows_power_strike_3|knows_power_draw_5|knows_athletics_4|knows_riding_2|knows_sailing_3|knows_wage_1,default_face_1,default_face_2],
    
  #Khergit
  ["horse_archer","Horse Archer","a horse archer",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_stained_felt_hat_b","itm_tattered_headcloth","itm_heraldic_shirt","itm_tattered_wrapping_boots"],
   str_14|agi_14|pw_attr,wpex(90,60,60,130,30,50),knows_pw|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_horse_archery_2|knows_athletics_1|knows_riding_6|knows_wage_1,default_face_1,default_face_2],
  
  #Multiple Cultures
  ["guard","Guard","a guard",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_arming_cap","itm_tabard","itm_old_hide_boots"],
   str_15|agi_18|pw_attr,wpex(125,110,110,20,60,40),knows_pw|knows_ironflesh_4|knows_power_strike_4|knows_shield_2|knows_athletics_5|knows_riding_2|knows_wage_1,default_face_1,default_face_2],
  
  #Townwatch
  ["watchman","Watchman","a watchman",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_arming_cap","itm_heraldic_shirt","itm_tattered_wrapping_boots"],
   str_15|agi_14|pw_attr,wpex(115,130,100,10,45,80),knows_pw|knows_ironflesh_4|knows_power_strike_4|knows_shield_1|knows_athletics_4|knows_riding_3|knows_sailing_3|knows_wage_1,default_face_1,default_face_2],
  ["ranger","Ranger","an ranger",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_arming_cap","itm_heraldic_shirt","itm_tattered_wrapping_boots"],
   str_14|agi_15|pw_attr,wpex(95,60,60,125,50,50),knows_pw|knows_ironflesh_4|knows_power_strike_3|knows_power_draw_4|knows_athletics_5|knows_riding_2|knows_sailing_3|knows_wage_1,default_face_1,default_face_2],

  #Outlaw Tier
  ["ruffian","Ruffian","a ruffian",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_nomad_vest","itm_nomad_armor","itm_rawhide_coat","itm_old_hide_boots","itm_club","itm_spiked_club"],
   str_14|agi_12|pw_attr,wpex(90,75,80,10,20,80),knows_pw|knows_ironflesh_4|knows_power_strike_4|knows_athletics_3|knows_riding_1|knows_looting_2|knows_labouring_2,default_face_1,default_face_2],
  ["brigand","Brigand","a brigand",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_nomad_vest","itm_nomad_armor","itm_rawhide_coat","itm_old_hide_boots","itm_club"],
   str_12|agi_14|pw_attr,wpex(85,40,70,100,60,70),knows_pw|knows_ironflesh_3|knows_power_strike_2|knows_power_draw_3|knows_athletics_4|knows_riding_1|knows_looting_6,default_face_1,default_face_2],
  ["hashashin","Hashashin","a hashashin",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_archers_vest","itm_turban","itm_old_hide_boots","itm_blunt_falchion"],
   str_13|agi_15|pw_attr,wpex(125,70,110,100,100,80),knows_pw|knows_power_strike_4|knows_power_draw_2|knows_power_throw_1|knows_athletics_6|knows_riding_2|knows_looting_6,default_face_1,default_face_2],
  ["sea_raider","Sea Raider","a sea raider",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_nomad_vest","itm_nomad_armor","itm_rawhide_coat","itm_old_hide_boots","itm_club","itm_old_shield"],
   str_15|agi_12|pw_attr,wpex(100,75,95,10,20,80),knows_pw|knows_ironflesh_4|knows_power_strike_4|knows_athletics_3|knows_shield_1|knows_riding_1|knows_sailing_4|knows_engineer_1,default_face_1,default_face_2],
  ["thief","Thief","a thief",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_tunic_with_green_cape","itm_tattered_wrapping_boots","itm_common_hood","itm_old_knife","itm_club"],
   str_12|agi_15|pw_attr,wpex(100,40,60,10,80,60),knows_pw|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_athletics_5|knows_riding_2|knows_looting_8,default_face_1,default_face_2],
  ["raider","Raider","a raider",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_nomad_vest","itm_tattered_wrapping_boots","itm_club","itm_bent_lance"],
   str_13|agi_14|pw_attr,wpex(90,60,110,10,30,80),knows_pw|knows_ironflesh_3|knows_power_strike_3|knows_athletics_2|knows_riding_4|knows_looting_2,default_face_1,default_face_2],
  ["cultist","Cultist","a cultist",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_red_robe","itm_red_hood","itm_club"],
   str_12|agi_13|pw_attr,wpex(90,10,100,0,0,30),knows_pw|knows_athletics_1|knows_riding_1|knows_wound_treatment_1|knows_alchemy_2|knows_engineer_2|knows_labouring_5|knows_tailoring_1|knows_herding_2,default_face_1,default_face_2],
  
  ["saved_troops_end","saved_troops_end","saved_troops_end",0,0,0,0,[],0,0,0,0,0],
  
  #Second Tier
  ["marshal","Marshal","the marshal",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_tabard","itm_old_hide_boots"],
   str_16|agi_15|pw_attr,wpex(110,125,120,80,100,50),knows_pw|knows_ironflesh_6|knows_power_strike_5|knows_power_draw_2|knows_shield_2|knows_siege_1|knows_athletics_3|knows_riding_4|knows_wage_1,default_face_1,default_face_2],
  ["steward","Steward","the steward",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_rich_outfit","itm_courtly_outfit","itm_nobleman_outfit","itm_ripped_woolen_hose","itm_woolen_hose"],
   str_14|agi_15|pw_attr,wpex(100,80,80,50,80,50),knows_pw|knows_ironflesh_4|knows_power_strike_3|knows_athletics_5|knows_riding_4|knows_sailing_5|knows_trade_1|knows_labouring_3|knows_engineer_2|knows_tailoring_2|knows_wage_1,default_face_1,default_face_2],
  
  #Third Tier
  ["lord","Lord","the lord",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_old_tabard","itm_rich_outfit","itm_courtly_outfit","itm_nobleman_outfit","itm_ripped_woolen_hose","itm_old_hide_boots","itm_worn_sword"],
   str_16|agi_15|pw_attr,wpex(115,115,115,50,70,50),knows_pw|knows_leadership_1|knows_ironflesh_6|knows_power_strike_4|knows_shield_2|knows_athletics_2|knows_riding_5,default_face_1,default_face_2],
  ["lady","Lady","the lady",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_lady_dress_ruby","itm_lady_dress_green","itm_lady_dress_blue","itm_court_dress","itm_red_dress","itm_ripped_woolen_hose","itm_woolen_hose","itm_blue_hose","itm_wimple_a","itm_wimple_b","itm_barbette","itm_worn_sword"],
   str_16|agi_15|pw_attr,wpex(115,115,115,50,70,50),knows_pw|knows_leadership_1|knows_ironflesh_6|knows_power_strike_4|knows_shield_2|knows_athletics_2|knows_riding_5,default_face_1,default_face_2],
  ["doge","Doge","the doge",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_rich_outfit","itm_courtly_outfit","itm_nobleman_outfit","itm_ripped_woolen_hose","itm_woolen_hose","itm_worn_sword"],
   str_14|agi_16|pw_attr,wpex(110,80,80,50,100,50),knows_pw|knows_leadership_1|knows_ironflesh_4|knows_power_strike_3|knows_shield_1|knows_athletics_5|knows_riding_7|knows_sailing_7|knows_trade_3|knows_labouring_3|knows_engineer_1|knows_tailoring_2|knows_alchemy_1,default_face_1,default_face_2],
  ["captain","Captain","the captain",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_tabard","itm_old_hide_boots","itm_worn_sword","itm_crude_bolts","itm_flimsy_crossbow"],
   str_16|agi_15|pw_attr,wpex(110,125,120,80,100,50),knows_pw|knows_leadership_1|knows_ironflesh_6|knows_power_strike_5|knows_power_draw_2|knows_shield_2|knows_athletics_3|knows_riding_4|knows_sailing_3,default_face_1,default_face_2],
  ["grandmaster","Grandmaster","the grandmaster",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_tabard","itm_old_hide_boots","itm_worn_sword"],
   str_16|agi_15|pw_attr,wpex(125,125,110,30,60,50),knows_pw|knows_leadership_1|knows_ironflesh_6|knows_power_strike_6|knows_shield_3|knows_athletics_3|knows_riding_4|knows_sailing_3,default_face_1,default_face_2],
  ["bishop","Bishop","the bishop",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_priest_robe","itm_priest_leggings","itm_priest_coif"],
   str_16|agi_14|pw_attr,wpex(60,70,115,50,20,50),knows_pw|knows_leadership_1|knows_ironflesh_8|knows_power_strike_2|knows_athletics_2|knows_wound_treatment_5|knows_riding_5,default_face_1,default_face_2],
  ["warchief","Warchief","the warchief",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_nomad_vest","itm_nomad_armor","itm_fur_hat","itm_old_hide_boots","itm_falchion","itm_crude_bolts","itm_flimsy_crossbow"],
   str_15|agi_16|pw_attr,wpex(110,110,90,90,70,40),knows_pw|knows_leadership_1|knows_ironflesh_5|knows_power_strike_4|knows_power_draw_2|knows_athletics_4|knows_looting_6|knows_riding_1|knows_sailing_4|knows_labouring_2,default_face_1,default_face_2],

  #Final Tier
  ["king","King","the king",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_old_tabard","itm_rich_outfit","itm_courtly_outfit","itm_nobleman_outfit","itm_ripped_woolen_hose","itm_old_hide_boots","itm_worn_sword"],
   str_16|agi_15|pw_attr,wpex(115,115,115,50,70,50),knows_pw|knows_leadership_1|knows_ironflesh_6|knows_power_strike_4|knows_shield_2|knows_athletics_2|knows_riding_5,default_face_1,default_face_2],
  ["queen","Queen","the queen",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_lady_dress_ruby","itm_lady_dress_green","itm_lady_dress_blue","itm_court_dress","itm_red_dress","itm_brown_dress","itm_green_dress","itm_sarranid_lady_dress","itm_sarranid_lady_dress_b","itm_ripped_woolen_hose","itm_woolen_hose","itm_blue_hose","itm_wimple_a","itm_wimple_b","itm_barbette","itm_worn_sword"],
   str_16|agi_15|pw_attr,wpex(115,115,115,50,70,50),knows_pw|knows_leadership_1|knows_ironflesh_6|knows_power_strike_4|knows_shield_2|knows_athletics_2|knows_riding_5,default_face_1,default_face_2],
  ["archbishop","Archbishop","the archbishop",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_priest_robe","itm_priest_leggings","itm_bishop_mitre"],
   str_16|agi_14|pw_attr,wpex(60,70,115,50,20,50),knows_pw|knows_leadership_1|knows_ironflesh_8|knows_power_strike_2|knows_athletics_2|knows_wound_treatment_5|knows_riding_5,default_face_1,default_face_2],
  ["patrician","Patrician","the patrician",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_rich_outfit","itm_courtly_outfit","itm_nobleman_outfit","itm_ripped_woolen_hose","itm_woolen_hose","itm_worn_sword"],
   str_14|agi_16|pw_attr,wpex(110,80,80,50,100,50),knows_pw|knows_leadership_1|knows_ironflesh_4|knows_power_strike_3|knows_shield_1|knows_athletics_5|knows_riding_7|knows_sailing_7|knows_trade_3|knows_labouring_3|knows_engineer_1|knows_tailoring_2,default_face_1,default_face_2],
  ["commander","Commander","the commander",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_tabard","itm_old_hide_boots","itm_worn_sword","itm_crude_bolts","itm_flimsy_crossbow"],
   str_16|agi_15|pw_attr,wpex(110,125,120,80,100,50),knows_pw|knows_leadership_1|knows_ironflesh_6|knows_power_strike_5|knows_power_draw_2|knows_shield_2|knows_athletics_3|knows_riding_4|knows_sailing_3,default_face_1,default_face_2],
  ["warlord","Warlord","the warlord",tf_mounted|tf_guarantee_all,0,0,"fac_commoners",
   ["itm_nomad_vest","itm_nomad_armor","itm_fur_hat","itm_old_hide_boots","itm_one_handed_battle_axe_a","itm_crude_bolts","itm_flimsy_crossbow"],
   str_15|agi_16|pw_attr,wpex(110,110,90,90,70,40),knows_pw|knows_leadership_1|knows_ironflesh_4|knows_power_strike_4|knows_power_draw_2|knows_athletics_4|knows_looting_6|knows_riding_1|knows_sailing_4|knows_labouring_2|knows_herding_1,default_face_1,default_face_2],
  
  #Rebel Tier
  ["rebel","Rebel","a rebel",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_ragged_woolen_cap","itm_stained_felt_hat_b","itm_tattered_headcloth","itm_heraldic_coarse_tunic","itm_old_tabard","itm_tattered_wrapping_boots","itm_old_hide_boots","itm_chipped_falchion","itm_rusty_sword","itm_crude_spear","itm_old_shield","itm_flimsy_crossbow","itm_crude_bolts"],
   str_14|agi_14|pw_attr,wpex(90,70,80,30,75,70),knows_pw|knows_ironflesh_3|knows_power_strike_3|knows_athletics_3|knows_riding_2|knows_engineer_1|knows_sailing_3|knows_tailoring_1,default_face_1,default_face_2],
  
  #Admin Tier
  ["godlike_hero","Admin","a admin",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_red_shirt","itm_linen_tunic","itm_woolen_hose","itm_invisible_sword","itm_invisible_bow","itm_invisible_arrows"],
   str_30|agi_30|pw_attr,wpex(300,300,300,300,300,300),knows_pw|knows_ironflesh_10|knows_power_strike_10|knows_power_draw_10|knows_power_throw_10|knows_shield_10|knows_athletics_10|knows_riding_10|knows_engineer_10|knows_siege_10|knows_wound_treatment_10|knows_looting_10|knows_labouring_10|knows_sailing_10|knows_tailoring_10|knows_herding_10|knows_trade_10|knows_musician_10|knows_alchemy_10,default_face_1,default_face_2],
  ["event_hero","Hero","a hero",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_red_shirt","itm_linen_tunic","itm_woolen_hose","itm_invisible_sword","itm_invisible_bow","itm_invisible_arrows"],
   str_30|agi_30|pw_attr,wpex(300,300,300,300,300,300),knows_pw|knows_ironflesh_10|knows_power_strike_10|knows_power_draw_10|knows_power_throw_10|knows_shield_10|knows_athletics_10|knows_riding_10|knows_engineer_10|knows_siege_10|knows_wound_treatment_10|knows_looting_10|knows_labouring_10|knows_sailing_10|knows_tailoring_10|knows_herding_10|knows_trade_10|knows_musician_10|knows_alchemy_10,default_face_1,default_face_2],
  ["guide","Guide","a guide",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_fur_hat","itm_sarranid_cloth_robe_b","itm_tattered_wrapping_boots","itm_worn_sword"],
   str_15|agi_15|pw_attr,wpex(125,110,90,10,40,60),knows_pw|knows_ironflesh_5|knows_power_strike_2|knows_athletics_7|knows_musician_3|knows_sailing_7|knows_riding_7|knows_labouring_2|knows_herding_2|knows_tailoring_2|knows_engineer_2|knows_wound_treatment_4|knows_alchemy_1,default_face_1,default_face_2],
    
  #Decap Troop
  ["decaptroop"," "," ",tf_guarantee_all,0,0,"fac_commoners",
   ["itm_invisible_head","itm_invisible_body","itm_invisible_foot","itm_invisible_hand"],
   str_5|agi_5|pw_attr,wpex(0,0,0,0,0,0),knows_pw,default_face_1,default_face_2],
  
  ["playable_troops_end","playable_troops_end","playable_troops_end",0,0,0,0,[],0,0,0,0,0],
  
  ##NPCS Start
  
  ["test_race","Footman","a footman",tf_guarantee_all|tf_giant_male,0,0,"fac_commoners",
   [],
   str_15|agi_14|pw_attr,wpex(100,100,130,10,45,80),knows_pw|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_shield_1|knows_athletics_5|knows_riding_2|knows_sailing_3,default_face_1,default_face_2],
  
  ##NPCS END

  ["inactive_players_array","inactive_players_array","inactive_players_array",0,0,0,0,[],0,0,0,0,0],
  ["mission_data","mission_data","mission_data",0,0,0,0,[],0,0,0,0,0],
  ["banner_background_color_array","banner_background_color_array","banner_background_color_array",0,0,0,0,[],0,0,0,0,0],
  ["temp_array","temp_array","temp_array",0,0,0,0,[],0,0,0,0,0],
  ["last_chat_message","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_0","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_1","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_2","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_3","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_4","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_5","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_6","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_7","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_8","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_9","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_10","-","-",0,0,0,0,[],0,0,0,0,0],
  ["chat_overlay_ring_buffer_end","-","-",0,0,0,0,[],0,0,0,0,0],
  ["ship_array","ship_array","ship_array",0,0,0,0,[],0,0,0,0,0],
  ["cart_array","cart_array","cart_array",0,0,0,0,[],0,0,0,0,0],
  ["removed_scene_props","removed_scene_props","removed_scene_props",0,0,0,0,[],0,0,0,0,0],
  ["animation_menu_strings","animation_menu_strings","animation_menu_strings",0,0,0,0,[],0,0,0,0,0],
  ["animation_durations","animation_durations","animation_durations",0,0,0,0,[],0,0,0,0,0],
]
