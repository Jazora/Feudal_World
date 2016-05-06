from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from header_items import *
from module_constants import *
import header_debug as dbg
import header_lazy_evaluation as lazy

####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id.
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags.
#  3) Mission-type (int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#  4) Mission description text (string).
#
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) Entry point number: Troops spawned from this spawn record will use this entry.
#    5.2) Spawn flags.
#    5.3) Alter flags: which equipment will be overriden.
#    5.4) AI flags.
#    5.5) Number of troops to spawn.
#    5.6) List of equipment to add to troops spawned from here (maximum 8).
#
#  6) List of triggers (list): Each trigger contains the following fields:
#    6.1) Check interval: How frequently this trigger will be checked. Also used for special triggers listed in header_triggers.py.
#    6.2) Delay interval: Time to wait before applying the consequences of the trigger after its conditions have been evaluated as true.
#    6.3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
#    6.4) Conditions block (list), must be a valid operation block. Every time the trigger is checked, this block will be executed.
#    If the conditions block returns true or is empty, the consequences block will be executed.
#    6.5) Consequences block (list), must be a valid operation block. Executed only if the conditions block succeeded.
####################################################################################################################

spawn_points_0_99 = [
  (0,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (1,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (2,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (3,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (4,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (5,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (6,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (7,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (8,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (9,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (10,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (11,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (12,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (13,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (14,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (15,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (16,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (17,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (18,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (19,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (20,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (21,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (22,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (23,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (24,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (25,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (26,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (27,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (28,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (29,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (30,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (31,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (32,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (33,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (34,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (35,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (36,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (37,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (38,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (39,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (40,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (41,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (42,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (43,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (44,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (45,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (46,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (47,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (48,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (49,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (50,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (51,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (52,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (53,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (54,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (55,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (56,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (57,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (58,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (59,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (60,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (61,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (62,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (63,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (64,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (65,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (66,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (67,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (68,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (69,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (70,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (71,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (72,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (73,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (74,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (75,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (76,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (77,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (78,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (79,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (80,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (81,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (82,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (83,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (84,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (85,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (86,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (87,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (88,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (89,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (90,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (91,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (92,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (93,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (94,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (95,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (96,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (97,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (98,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  (99,mtef_visitor_source,0,aif_start_alarmed,1,[]),
  ]

before_mission_start_setup = (ti_before_mission_start, 0, 0, [], # set up basic mission and scene values
   [(server_set_friendly_fire, 1),
    (server_set_melee_friendly_fire, 1),
    (server_set_friendly_fire_damage_self_ratio, 0),
    (server_set_friendly_fire_damage_friend_ratio, 100),
    (team_set_relation, team_default, team_default, -1),
    (team_set_relation, team_default, team_spawn_invulnerable, 0),
    (team_set_relation, team_spawn_invulnerable, team_default, 0),
    (team_set_relation, team_spawn_invulnerable, team_spawn_invulnerable, 0),
    (call_script, "script_initialize_scene_globals"),
    (call_script, "script_scene_set_day_time"),
    (call_script, "script_scene_setup_factions_castles"),
    (call_script, "script_setup_all_linked_scene_props"),
    #Feudal World
    (call_script, "script_setup_special_attributes"),
    #Feudal World
    (try_begin),
      (multiplayer_is_server),
      (call_script, "script_setup_castle_money_chests"),
    (else_try),
      (call_script, "script_load_profile_options"),
    (try_end),
    ])

after_mission_start_setup = (ti_after_mission_start, 0, 0, [], # spawn and move certain things after most other set up is done
   [(set_spawn_effector_scene_prop_kind, 0, -1),
    (set_spawn_effector_scene_prop_kind, 1, -1),
    (assign, "$g_preset_message_display_enabled", 0),
    (multiplayer_is_server),
    (assign, "$g_next_scene", -1),
    #(call_script, "script_setup_ship_collision_props"),
    (call_script, "script_setup_scene_props_after_mission_start"),
    (init_position, pos1),
    (set_spawn_position, pos1), # spawn a respawn position marker scene prop for each possible player
    (server_get_max_num_players, "$g_spawn_marker_count"),
    (val_add, "$g_spawn_marker_count", 1),
    (try_for_range, ":unused", 0, "$g_spawn_marker_count"),
      (spawn_scene_prop, "spr_code_spawn_marker"),
    (try_end),
    (assign, "$g_spawned_bot_count", 0),
    (call_script, "script_cf_check_name_server"),
    ])

player_joined = (ti_server_player_joined, 0, 0, [], # server: handle connecting players
   [(store_trigger_param_1, ":player_id"),
    (call_script, "script_setup_player_joined", ":player_id"),
    (multiplayer_is_server),
    #(multiplayer_send_message_to_player, ":player_id", server_event_set_skybox),
    (try_begin),
      (eq, "$g_name_server_enabled", 1),
      (call_script, "script_cf_player_load_data_url", ":player_id"),
    (try_end),
    ])

player_exit = (ti_on_player_exit, 0, 0, [], # server: save player values on exit
   [(store_trigger_param_1, ":player_id"),
    (call_script, "script_cf_save_player_exit", ":player_id"),
    (call_script, "script_cf_player_update_pos_url", ":player_id",0),
    ])

agent_spawn = (ti_on_agent_spawn, 0, 0, [], # server and clients: set up new agents after they spawn
   [(store_trigger_param_1, ":agent_id"),
    (call_script, "script_on_agent_spawned", ":agent_id"),
    (multiplayer_is_server),
    (agent_get_player_id,":player_id",":agent_id"),
    (player_is_active, ":player_id"),
    (try_begin),
      (player_slot_eq, ":player_id", slot_player_profile_loaded, 1),
      (call_script, "script_cf_player_get_pos_url", ":player_id"),
      (player_set_slot, ":player_id", slot_player_profile_loaded, 0),
    (try_end),
    (agent_is_human,":agent_id"),
    (call_script, "script_cf_player_update_troop_url", ":player_id"),
    ])

agent_killed = (ti_on_agent_killed_or_wounded, 0, 0, [], # server and clients: handle messages, score, loot, and more after agents die
   [(store_trigger_param_1, ":dead_agent_id"),
    (store_trigger_param_2, ":killer_agent_id"),
    (call_script, "script_client_check_show_respawn_time_counter", ":dead_agent_id"),
    (call_script, "script_apply_consequences_for_agent_death", ":dead_agent_id", ":killer_agent_id"),
    (multiplayer_is_server),
    (call_script, "script_setup_agent_for_respawn", ":dead_agent_id", ":killer_agent_id"),
    (call_script, "script_check_animal_killed", ":dead_agent_id", ":killer_agent_id"),
    (call_script, "script_check_spawn_bots", ":dead_agent_id"),
    ])

agent_hit = (ti_on_agent_hit, 0, 0, [], # server: apply extra scripted effects for special weapons, hitting animals, and when overloaded by armor
   [(store_trigger_param_1, ":attacked_agent_id"),
    (store_trigger_param_2, ":attacker_agent_id"),
    (store_trigger_param_3, ":damage_dealt"),
    (try_begin), # check if damage should bleed through the armor due to unmet requirements
      (agent_slot_ge, ":attacked_agent_id", slot_agent_armor_damage_through, 5),
      (agent_get_slot, ":damage_through_multiplier", ":attacked_agent_id", slot_agent_armor_damage_through),
      (gt, reg0, -1),
      (item_get_slot, ":damage_through", reg0, slot_item_max_raw_damage),
      (val_mul, ":damage_through", ":damage_through_multiplier"),
      (val_div, ":damage_through", 100),
      (gt, ":damage_through", ":damage_dealt"),
      (store_random_in_range, ":damage_through", ":damage_dealt", ":damage_through"),
      (set_trigger_result, ":damage_through"),
    (try_end),
    (try_begin),
      (agent_slot_ge, ":attacked_agent_id", slot_agent_animal_birth_time, 1),
      (call_script, "script_animal_hit", ":attacked_agent_id", ":attacker_agent_id", ":damage_dealt", reg0),
    (try_end),
    (try_begin),
      (is_between, reg0, scripted_items_begin, scripted_items_end),
      (call_script, "script_agent_hit_with_scripted_item", ":attacked_agent_id", ":attacker_agent_id", ":damage_dealt", reg0),
    (try_end),
    (try_begin),# Fist damage
      (neg|gt,reg0,0),
      (agent_get_item_slot, ":hand_item", ":attacker_agent_id", ek_gloves),
      (try_begin),
        (neg|gt,":hand_item",0),#player doesnt have gloves on so dont do damage
        (set_trigger_result, 0),
      (try_end),
    (try_end),
    ])

item_picked_up = (ti_on_item_picked_up, 0, 0, [], # handle agents picking up an item
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":item_id"),
    (store_trigger_param_3, ":instance_id"),
    (call_script, "script_agent_calculate_stat_modifiers_for_item", ":agent_id", ":item_id", 1, 1),
    (multiplayer_is_server),
    (call_script, "script_check_on_item_picked_up", ":agent_id", ":item_id", ":instance_id"),
    ])

item_dropped = (ti_on_item_dropped, 0, 0, [], # handle agents dropping an item
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":item_id"),
    (store_trigger_param_3, ":instance_id"),
    (call_script, "script_agent_calculate_stat_modifiers_for_item", ":agent_id", ":item_id", 0, 1),
    (multiplayer_is_server),
    (call_script, "script_check_on_item_dropped", ":agent_id", ":item_id", ":instance_id", 0),
    ])

item_wielded = (ti_on_item_wielded, 0, 0, [], # handle agents wielding an item
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":item_id"),
    (call_script, "script_agent_calculate_stat_modifiers_for_item", ":agent_id", ":item_id", 1, 1),
    ])

item_unwielded = (ti_on_item_unwielded, 0, 0, [], # handle agents un-wielding an item
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":item_id"),
    (call_script, "script_agent_calculate_stat_modifiers_for_item", ":agent_id", ":item_id", 0, 1),
    ])

agent_mount = (ti_on_agent_mount, 0, 0, [], # server: check speed factor and attached carts when agents mount a horse
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":horse_agent_id"),
    (agent_set_slot, ":horse_agent_id", slot_agent_horse_last_rider, ":agent_id"),
    (agent_set_slot, ":agent_id", slot_agent_last_horse_ridden, ":horse_agent_id"),
    (multiplayer_is_server),
    (call_script, "script_check_agent_horse_speed_factor", ":agent_id", ":horse_agent_id", 0),
    (try_begin),
      (call_script, "script_cf_attach_cart", ":agent_id", -1, ":agent_id"),
    (try_end),
    ])

agent_dismount = (ti_on_agent_dismount, 0, 0, [], # server: make horses stand still after being dismounted from
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":horse_agent_id"),
    (agent_set_slot, ":horse_agent_id", slot_agent_horse_last_rider, ":agent_id"),
    (agent_set_slot, ":agent_id", slot_agent_last_horse_ridden, ":horse_agent_id"),
    (multiplayer_is_server),
    (agent_get_position, pos1, ":horse_agent_id"),
    (agent_set_scripted_destination, ":horse_agent_id", pos1, 0),
    ])

player_check_loop = (0, 0, 0.5, # server: check all players to see if any need agents spawned, also periodically lowering outlaw ratings
   [(multiplayer_is_server),
    (store_mission_timer_a, ":time"),
    (get_max_players, ":max_players"),
    (assign, ":loop_end", ":max_players"),
    (try_for_range, ":player_id", "$g_loop_player_id", ":loop_end"), # continue from the last player id checked
      (player_is_active, ":player_id"),
      (player_get_slot, ":kick_at_time", ":player_id", slot_player_kick_at_time),
      (try_begin), # kick after an interval if rejected by the name server
        (gt, ":kick_at_time", 0),
        (try_begin),
          (ge, ":time", ":kick_at_time"),
          (kick_player, ":player_id"),
        (try_end),
      (else_try),
        (try_begin),
          (this_or_next|player_slot_eq, ":player_id", slot_player_spawn_state, player_spawn_state_dead),
          (player_slot_eq, ":player_id", slot_player_spawn_state, player_spawn_state_invulnerable),
          (call_script, "script_cf_player_check_spawn_agent", ":player_id"),
          (assign, ":loop_end", -1), # if the spawn checks were run, end the loop to give other triggers a chance to run, then immediately continue
          (store_add, "$g_loop_player_id", ":player_id", 1),
        (try_end),
        (try_begin),
          (eq, "$g_loop_player_check_outlaw", 1),
          (player_get_slot, ":outlaw_rating", ":player_id", slot_player_outlaw_rating),
          (try_begin),
            (gt, ":outlaw_rating", 0),
            (val_sub, ":outlaw_rating", 1),
            (player_set_slot, ":player_id", slot_player_outlaw_rating, ":outlaw_rating"),
            (multiplayer_send_3_int_to_player, ":player_id", server_event_player_set_slot, ":player_id", slot_player_outlaw_rating, ":outlaw_rating"),
            (call_script, "script_cf_player_update_troop_url", ":player_id"),
          (try_end),
        (try_end),
      (try_end),
    (try_end),
    (eq, ":loop_end", ":max_players"), # if all players were checked, the trigger will succeed and wait the rearm interval before checking again
    (assign, "$g_loop_player_id", 1), # go back to the start (player id 0 is the server)
    (try_begin), # only decrease outlaw ratings at certain intervals, not every time
      (ge, ":time", "$g_loop_player_check_outlaw_time"),
      (val_add, "$g_loop_player_check_outlaw_time", loop_player_check_outlaw_interval),
      (assign, "$g_loop_player_check_outlaw", 1),
    (else_try),
      (assign, "$g_loop_player_check_outlaw", 0),
    (try_end),
    ], [])

agent_check_loop = (0, 0, 0.5, # server: loop over all agents, doing all common repetitive checks together for each agent, to minimize the penalty of using try_for_agents
   [(multiplayer_is_server),
    (try_begin), # if the loop was not restarted
      (gt, "$g_loop_agent_last_checked", -2),
      (assign, ":agent_id", -1),
      (try_for_agents, ":loop_agent_id"), # find the next agent id greater than the previous checked
        (eq, ":agent_id", -1),
        (gt, ":loop_agent_id", "$g_loop_agent_last_checked"),
        (assign, ":agent_id", ":loop_agent_id"),
      (try_end),
      (try_begin),
        (gt, ":agent_id", -1), # if a next agent id was found
        (assign, "$g_loop_agent_last_checked", ":agent_id"),
        (call_script, "script_check_agent_drowning", ":agent_id"),
        (try_begin),
          (eq, "$g_loop_horse_check", 1),
          (try_begin),
            (neg|agent_is_human, ":agent_id"),
            (call_script, "script_check_remove_lost_horse", ":agent_id"),
          (else_try),
            (call_script, "script_agent_remove_empty_ammo_stacks", ":agent_id"),
          (try_end),
        (try_end),
        (try_begin),
          (eq, "$g_loop_health_check", 1),
          (call_script, "script_check_agent_health", ":agent_id"),
        (try_end),
      (else_try),
        (assign, "$g_loop_agent_last_checked", -2),
      (try_end),
    (else_try), # setting up to restart the loop
      (store_mission_timer_a, ":time"),
      (try_begin),
        (ge, ":time", "$g_loop_agent_check_time"),
        (val_add, "$g_loop_agent_check_time", loop_agent_check_interval),
        (assign, "$g_loop_agent_last_checked", -1), # set to an invalid low agent id to start
        (try_begin),
          (ge, ":time", "$g_loop_horse_check_time"),
          (val_add, "$g_loop_horse_check_time", loop_horse_check_interval),
          (assign, "$g_loop_horse_check", 1),
        (else_try),
          (assign, "$g_loop_horse_check", 0),
        (try_end),
        (try_begin),
          (ge, ":time", "$g_loop_health_check_time"),
          (val_add, "$g_loop_health_check_time", loop_health_check_interval),
          (assign, "$g_loop_health_check", 1),
        (else_try),
          (assign, "$g_loop_health_check", 0),
        (try_end),
      (try_end),
    (try_end),
    (eq, "$g_loop_agent_last_checked", -2), # at the end of the loop, the trigger succeeds to wait the rearm interval before restarting
    ], [])

agent_check_attack_loop = (0, 0, 0.2, [], # server: repeatedly check all agents for attacking with a weapon they can't use - should be kept as simple as possible
   [(multiplayer_is_server),
    (try_for_agents, ":agent_id"),
      (agent_slot_eq, ":agent_id", slot_agent_cannot_attack, 1),
      (agent_get_attack_action, ":action", ":agent_id"),
      (is_between, ":action", 1, 7), # if the agent attack action is anything except "free" or "cancelling attack", unwield the weapon
      (agent_set_wielded_item, ":agent_id", -1),
    (try_end),
    ])

resource_regrow_check = (10, 0, 0, [], # server: call the script to regrow a removed scene prop after the required time
   [(multiplayer_is_server),
    (troop_get_slot, ":resources_count", "trp_removed_scene_props", slot_array_count),
    (gt, ":resources_count", 0),
    (val_add, ":resources_count", slot_array_begin),
    (try_for_range, ":resource_slot", slot_array_begin, ":resources_count"), # loop over all scene props added to the removed list
      (troop_get_slot, ":instance_id", "trp_removed_scene_props", ":resource_slot"),
      (le, ":instance_id", 0),
    (else_try),
      (neg|scene_prop_slot_eq, ":instance_id", slot_scene_prop_state, scene_prop_state_hidden),
      (troop_set_slot, "trp_removed_scene_props", ":resource_slot", -1),
    (else_try),
      (scene_prop_get_slot, ":regen_time", ":instance_id", slot_scene_prop_state_time),
      (store_mission_timer_a, ":time"),
      (ge, ":time", ":regen_time"), # if the regeneration time is passed, remove from the list and call the stored script
      (troop_set_slot, "trp_removed_scene_props", ":resource_slot", -1),
      (scene_prop_get_slot, ":regrow_script", ":instance_id", slot_scene_prop_regrow_script),
      (try_begin),
        (eq, ":regrow_script", 0),
        (call_script, "script_regrow_resource", ":instance_id"),
      (else_try),
        (call_script, ":regrow_script", ":instance_id"),
      (try_end),
    (try_end),
    ])

polls_check = (2, 0, 0, [], # server: regularly check to see if any polls have ended
   [(multiplayer_is_server),
    (call_script, "script_check_polls_ended"),
    ])

game_ended_check = (1, 5, 0, # server: check for game end from victory or an admin scene change
   [(multiplayer_is_server),
    (eq, "$g_game_ended", 0),
    (store_mission_timer_a, ":current_time"),
    (store_mul, ":game_end_time", "$g_game_time_limit", 60),
    (try_begin), # check for the victory condition
      (call_script, "script_cf_victory_condition_met"),
      (assign, ":faction_id", reg0),
      (try_begin), # if only just met, store the time when the game could end
        (le, "$g_victory_condition_time", 0),
        (store_mul, "$g_victory_condition_time", "$g_victory_condition", 60),
        (val_add, "$g_victory_condition_time", ":current_time"),
      (else_try),
        (gt, "$g_victory_condition_time", 0),
        (this_or_next|ge, ":current_time", "$g_victory_condition_time"), # if the victory condition has held for the required time, end the game
        (ge, ":current_time", ":game_end_time"),
        (get_max_players, ":max_players"),
        (try_for_range, ":player_id", 1, ":max_players"),
          (player_is_active, ":player_id"),
          (multiplayer_send_3_int_to_player, ":player_id", server_event_preset_message, "str_s1_reign_supreme", preset_message_faction|preset_message_big|preset_message_log, ":faction_id"),
        (try_end),
        #(assign, "$g_game_ended", 1),# We dont want the game to end when someone owns all the castles
      (try_end),
    (else_try), # reset the victory condition timer
      (assign, "$g_victory_condition_time", 0),
    (try_end),
    (this_or_next|eq, "$g_game_ended", 1),
    (this_or_next|is_between, "$g_next_scene", scenes_begin, scenes_end), # end the mission if an admin changes the scene
    (ge, ":current_time", ":game_end_time"),
    (assign, "$g_game_ended", 1),
    ],
   [(try_begin), # after the delay, start the next mission
      (neg|is_between, "$g_next_game_type", game_type_mission_templates_begin, game_type_mission_templates_end),
      (assign, "$g_next_game_type", game_type_mission_templates_begin),
    (try_end),
    (assign, ":started_manually", 1),
    (try_begin),
      (neg|is_between, "$g_next_scene", scenes_begin, scenes_end),
      (assign, "$g_next_scene", scenes_begin),
      (assign, ":started_manually", 0),
    (try_end),
    #Save Players Data
    (get_max_players, ":max_players"),
    (try_for_range, ":player_id", 1, ":max_players"),
      (player_is_active, ":player_id"),
      (call_script, "script_cf_player_update_pos_url", ":player_id",1),
    (try_end),
    #Save Players Data
    (start_multiplayer_mission, "$g_next_game_type", "$g_next_scene", ":started_manually"),
    (call_script, "script_game_set_multiplayer_mission_end"),
    ])

draw_initial_banners = (0, 0, ti_once, [], # server: calculate and draw all castle banners at mission start
   [(multiplayer_is_server),
    (call_script, "script_redraw_castle_banners", redraw_all_banners, -1),
    ])

fill_chests_starting_inventory = (8, 0, ti_once, [], # server: wait so the pseudo random number generator can get some entropy
   [(multiplayer_is_server),
    (call_script, "script_scene_fill_chests_starting_inventory"),
    ])

fire_place_check = (1, 0, 60, # server: wait 1 second between checks of fire heaps, then 60 seconds after all have been checked
   [(multiplayer_is_server),
    (scene_prop_get_instance, ":instance_id", "spr_pw_fire_wood_heap", "$g_fire_place_instance_no"),
    (call_script, "script_fire_place_burn", ":instance_id"),
    (val_add, "$g_fire_place_instance_no", 1),
    (scene_prop_get_num_instances, ":num_instances", "spr_pw_fire_wood_heap"),
    (try_begin),
      (ge, "$g_fire_place_instance_no", ":num_instances"),
      (assign, "$g_fire_place_instance_no", 0),
    (try_end),
    (eq, "$g_fire_place_instance_no", 0),
    ], [])

fish_school_loop = (0.1, 0, 30, # server: wait 0.1 seconds between checks of fish schools, then 30 seconds after all have been checked
   [(multiplayer_is_server),
    (try_begin),
      (scene_prop_get_instance, ":instance_id", "spr_pw_fish_school", "$g_fish_school_instance_no"),
      (call_script, "script_move_fish_school", ":instance_id"),
      (val_add, "$g_fish_school_instance_no", 1),
    (else_try), # at the loop end, check all nets as well
      (assign, "$g_fish_school_instance_no", 0),
      (call_script, "script_check_fishing_nets"),
    (try_end),
    (eq, "$g_fish_school_instance_no", 0),
    ], [])

herd_leader_movement_loop = (5, 0, 0, [], # server: check all animal herd leaders to see if any are ready to move
   [(multiplayer_is_server),
    (le, "$g_loop_animal_herd_begin", 0), # not currently moving a herd
    (scene_spawned_item_get_num_instances, ":herds_end", "itm_animal_herd_manager"),
    (try_begin),
      (ge, "$g_loop_animal_herd_to_move", ":herds_end"),
      (assign, "$g_loop_animal_herd_to_move", 0),
    (try_end),
    (store_mission_timer_a, ":time"), # loop over next herd managers to check if any are ready to move
    (try_for_range, "$g_loop_animal_herd_to_move", "$g_loop_animal_herd_to_move", ":herds_end"),
      (scene_spawned_item_get_instance, ":herd_manager", "itm_animal_herd_manager", "$g_loop_animal_herd_to_move"),
      (assign, "$g_loop_animal_herd_leader", -1),
      (scene_prop_get_slot, ":adult_item_id", ":herd_manager", slot_animal_herd_manager_adult_item_id),
      (item_get_slot, ":loop_end", ":adult_item_id", slot_item_animal_max_in_herd),
      (try_for_range, ":herd_slot", 0, ":loop_end"), # loop over animals in the herd
        (scene_prop_get_slot, ":herd_agent_id", ":herd_manager", ":herd_slot"),
        (gt, ":herd_agent_id", -1),
        (try_begin),
          (agent_is_active, ":herd_agent_id"),
          (agent_get_item_id, ":herd_item_id", ":herd_agent_id"),
          (agent_slot_eq, ":herd_agent_id", slot_agent_animal_herd_manager, ":herd_manager"),
          (gt, ":herd_item_id", -1),
          (item_slot_eq, ":herd_item_id", slot_item_animal_adult_item_id, ":adult_item_id"),
          (try_begin), # if the leader has been found, set the times for the followers to move
            (neq, "$g_loop_animal_herd_leader", -1),
            (store_random_in_range, ":move_time", 0, 6),
            (val_add, ":move_time", ":time"),
            (agent_set_slot, ":herd_agent_id", slot_agent_animal_move_time, ":move_time"),
          (else_try), # the first valid animal found is the leader: start the movement if the set time is met
            (assign, "$g_loop_animal_herd_leader", ":herd_agent_id"),
            (neg|agent_slot_ge, ":herd_agent_id", slot_agent_animal_move_time, ":time"),
            (assign, ":herds_end", -1), # break out of the herd manager checking loop after the animal loop is finished
            (store_add, "$g_loop_animal_herd_begin", ":herd_slot", 1),
            (store_random_in_range, ":move_time", 5, 31), # set the next move time
            (val_add, ":move_time", ":time"),
            (agent_set_slot, "$g_loop_animal_herd_leader", slot_agent_animal_move_time, ":move_time"),
            (call_script, "script_animal_move", "$g_loop_animal_herd_leader", "$g_loop_animal_herd_leader"), # move the leader
          (else_try), # if the leader movement time is not met, skip to the next herd manager to check
            (assign, ":loop_end", -1),
          (try_end),
        (else_try), # if the animal or agent id is not valid, remove it from the herd manager
          (scene_prop_set_slot, ":herd_manager", ":herd_slot", -1),
          (agent_is_active, ":herd_agent_id"),
          (le, ":herd_item_id", -1),
          (agent_set_slot, ":herd_agent_id", slot_agent_animal_herd_manager, -1),
        (try_end),
      (try_end),
      (try_begin), # if no valid animals are found, remove the herd manager
        (eq, "$g_loop_animal_herd_leader", -1),
        (scene_prop_set_prune_time, ":herd_manager", 1),
      (try_end),
    (try_end),
    ])

herd_follower_movement_loop = (0.5, 0, 0, [], # server: when currently moving a herd, check the follower animals for any ready to move
   [(multiplayer_is_server),
    (gt, "$g_loop_animal_herd_begin", 0), # currently moving a herd
    (try_begin), # if the herd leader and manager are valid
      (agent_is_active, "$g_loop_animal_herd_leader"),
      (scene_spawned_item_get_instance, ":herd_manager", "itm_animal_herd_manager", "$g_loop_animal_herd_to_move"),
      (store_mission_timer_a, ":time"),
      (scene_prop_get_slot, ":adult_item_id", ":herd_manager", slot_animal_herd_manager_adult_item_id),
      (item_get_slot, ":loop_end", ":adult_item_id", slot_item_animal_max_in_herd),
      (assign, ":remaining_to_move", 0),
      (try_for_range, ":herd_slot", "$g_loop_animal_herd_begin", ":loop_end"), # loop over the followers to check if any are ready to move
        (scene_prop_get_slot, ":herd_agent_id", ":herd_manager", ":herd_slot"),
        (agent_is_active, ":herd_agent_id"),
        (agent_get_slot, ":move_time", ":herd_agent_id", slot_agent_animal_move_time),
        (gt, ":move_time", 0),
        (try_begin),
          (ge, ":time", ":move_time"),
          (agent_set_slot, ":herd_agent_id", slot_agent_animal_move_time, 0),
          (call_script, "script_animal_move", ":herd_agent_id", "$g_loop_animal_herd_leader"),
        (else_try),
          (val_add, ":remaining_to_move", 1),
        (try_end),
      (try_end),
      (gt, ":remaining_to_move", 0), # if any followers are still waiting
    (else_try), # otherwise, go back to the herd manager checking loop
      (assign, "$g_loop_animal_herd_begin", 0),
      (val_add, "$g_loop_animal_herd_to_move", 1),
    (try_end),
    ])

herd_animal_count_check = (300, 0, 0, [], # server: periodically update the global count of herd animals - rare conditions seemed to make this value incorrect over time
   [(multiplayer_is_server),
    (assign, "$g_herd_animal_count", 0),
    (try_for_agents, ":agent_id"),
      (agent_slot_ge, ":agent_id", slot_agent_animal_birth_time, 1),
      (val_add, "$g_herd_animal_count", 1),
    (try_end),
    ])

escape_pressed = (ti_escape_pressed, 0, 0, [], # clients: show escape menu
   [(call_script, "script_cf_no_input_presentation_active"),
    (start_presentation, "prsnt_escape_menu"),
    ])

tab_pressed = (ti_tab_pressed, 0, 0, [], # clients: show player stats chart when that control is pressed (not necessarily tab)
   [(call_script, "script_cf_no_input_presentation_active"),
    (neg|is_presentation_active, "prsnt_tabbed_stats_chart"),
    (assign, "$g_stats_chart_opened_manually", 1),
    (start_presentation, "prsnt_tabbed_stats_chart"),
    ])

static_presentations_setup = (ti_battle_window_opened, 0, 0, [], # clients: called after connecting and when returning from the log window (which clears all presentations)
   [(try_begin),
      (eq, "$g_display_agent_labels", 1),
      (start_presentation, "prsnt_display_agent_labels"),
    (try_end),
    (try_begin),
      (eq, "$g_display_chat_overlay", 1),
      (start_presentation, "prsnt_chat_overlay"),
    (try_end),
    (try_begin),
      (gt, "$g_respawn_start_time", 0),
      (start_presentation, "prsnt_respawn_time_counter"),
    (try_end),
    (try_begin),
      (neq, "$g_game_type", "mt_no_money"),
      (start_presentation, "prsnt_gold"),
    (try_end),
    (start_presentation, "prsnt_food_bar"),
    (start_presentation, "prsnt_scene_prop_hit_points_bar"),
    (try_begin), # if an inventory was being accessed before the presentations were cleared, notify the server to stop sending updates
      (gt, "$g_show_inventory_instance_id", 0),
      (assign, "$g_show_inventory_instance_id", 0),
      (multiplayer_send_message_to_server, client_event_transfer_inventory),
    (try_end),
    ])

action_menu_pressed = (0, 0, 0, [], # clients: show action menu while that control is held down
   [(game_key_clicked, gk_action_menu),
    (call_script, "script_cf_no_input_presentation_active"),
    (neg|is_presentation_active, "prsnt_action_menu"),
    (start_presentation, "prsnt_action_menu"),
    ])

target_agent_pressed = (0, 0.3, 0, # clients: allow aiming at other agents or corpses to select them
   [(game_key_is_down, gk_target_agent),
    (call_script, "script_cf_no_input_presentation_active"),
    (multiplayer_get_my_player, ":player_id"),
    (player_is_active, ":player_id"),
    (try_begin), # if shift is down, select live agents while the control is held down
      (this_or_next|key_is_down, key_left_shift),
      (key_is_down, key_right_shift),
      (call_script, "script_select_target_agent"),
      (assign, "$g_targeting_corpses", 0),
    (else_try), # otherwise select corpses, running the loot script when the control is released
      (call_script, "script_select_target_corpse"),
      (assign, "$g_targeting_corpses", 1),
    (try_end),
    ],
   [(eq, "$g_targeting_corpses", 1),
    (neg|game_key_is_down, gk_target_agent),
    (call_script, "script_loot_target_corpse"),
    ])

chat_overlay_toggled = (0, 0, 0, [], # clients: toggle the overlay for local or faction chat
   [(key_clicked, key_f10),
    (call_script, "script_cf_no_input_presentation_active"),
    (try_begin),
      (neg|is_presentation_active, "prsnt_chat_overlay"),
      (assign, "$g_display_chat_overlay", 1),
      (start_presentation, "prsnt_chat_overlay"),
    (else_try),
      (assign, "$g_display_chat_overlay", 0),
    (try_end),
    ])

chat_resend_check = (0.3, 0.3, 0, [(troop_slot_eq, "trp_last_chat_message", slot_last_chat_message_not_recieved, 1)], # clients: try to resend lost chat mesages
   [(troop_slot_eq, "trp_last_chat_message", slot_last_chat_message_not_recieved, 1), # if the server has not confirmed receiving the last chat message for at least 0.3 seconds
    (troop_get_slot, ":event", "trp_last_chat_message", slot_last_chat_message_event_type), # resend the chat type and string
    (try_begin),
      (gt, ":event", net_chat_event_mask),
      (multiplayer_send_int_to_server, client_event_chat_message_type, ":event"),
    (try_end),
    (val_and, ":event", net_chat_event_mask),
    (str_store_troop_name, s0, "trp_last_chat_message"),
    (multiplayer_send_string_to_server, ":event", s0),
    ])

local_chat_pressed = (0, 0.05, 0, [(game_key_clicked, gk_local_chat),(call_script, "script_cf_no_input_presentation_active")], # clients: local chat entry box
   [(assign, "$g_chat_box_string_id", "str_send_message_to_players_nearby"),
    (assign, "$g_chat_box_event_type", chat_event_type_local),
    (start_presentation, "prsnt_chat_box"),
    ])
    
whisper_chat_pressed = (0, 0.05, 0, [(game_key_clicked, gk_local_chat),(key_is_down, key_right_shift),(call_script, "script_cf_no_input_presentation_active")], # clients: local chat entry box
   [(assign, "$g_chat_box_string_id", "str_send_whisper_to_players_nearby"),
    (assign, "$g_chat_box_event_type", chat_event_type_whisper),
    (start_presentation, "prsnt_chat_box"),
    ])

faction_chat_pressed = (0, 0.05, 0, [(game_key_clicked, gk_faction_chat),(call_script, "script_cf_no_input_presentation_active")], # clients: faction chat entry box
   [(multiplayer_get_my_player, ":player_id"),
    (player_get_slot, ":faction_id", ":player_id", slot_player_faction_id),
    (is_between, ":faction_id", warlords_begin, factions_end),
    (str_store_faction_name, s11, ":faction_id"),
    (assign, "$g_chat_box_string_id", "str_send_message_to_the_s11"),
    (assign, "$g_chat_box_event_type", chat_event_type_faction),
    (try_begin),
      (eq,":faction_id",warlords_begin),
      (player_slot_eq, ":player_id", slot_player_is_lord, 1),
      (start_presentation, "prsnt_chat_box"),
    (else_try),
      (neq,":faction_id",warlords_begin),
      (start_presentation, "prsnt_chat_box"),
    (try_end),
    ])

admin_chat_pressed = (0, 0.05, 0, [(game_key_clicked, gk_admin_chat),(call_script, "script_cf_no_input_presentation_active")], # clients: admin chat entry box
   [(try_begin), # for admins, allow sending only to a targeted player
      (multiplayer_get_my_player, ":player_id"),
      (player_is_admin, ":player_id"),
      (assign, "$g_chat_box_player_string_id", "str_send_admin_message_to_s1"),
    (else_try),
      (assign, "$g_chat_box_player_string_id", 0),
    (try_end),
    (assign, "$g_chat_box_string_id", "str_send_admin_message"),
    (assign, "$g_chat_box_event_type", chat_event_type_admin),
    (start_presentation, "prsnt_chat_box"),
    ])

money_bag_pressed = (0, 0, 0, [], # clients: show presentation to drop money bags or interact with money chests
   [(game_key_clicked, gk_money_bag),
    (call_script, "script_cf_no_input_presentation_active"),
    (start_presentation, "prsnt_money_bag"),
    ])

animation_menu_pressed = (0, 0.05, 0, [(game_key_clicked, gk_animation_menu),(call_script, "script_cf_no_input_presentation_active")], # clients: show animation menu
   [(try_begin),
      (eq, "$g_animation_menu_no_mouse_grab", 1),
      (start_presentation, "prsnt_animation_menu_no_mouse_grab"),
    (else_try),
      (start_presentation, "prsnt_animation_menu"),
    (try_end),
    ])

welcome_message = (0, 0, ti_once, [], # clients: show a welcome message when connecting to a server
   [(neg|multiplayer_is_server),
    (call_script, "script_show_welcome_message"),
    ])

turn_windmill_fans = (0, 0, 4.0, [], # clients: make windmill fans in the scene turn visually (not affecting collision detection)
   [(neg|multiplayer_is_server),
    (call_script, "script_cf_turn_windmill_fans", 0),
    ])

ambient_sounds_check = (1, 0, 10, # clients: check for nearby ambient sound emitters to activate
   [(neg|multiplayer_is_server),
    (scene_prop_get_num_instances, ":num_instances", "spr_pw_scene_ambient_sound"),
    (try_begin),
      (ge, "$g_ambient_sound_instance_no", ":num_instances"),
      (assign, "$g_ambient_sound_instance_no", 0),
    (try_end),
    (scene_prop_get_instance, ":instance_id", "spr_pw_scene_ambient_sound", "$g_ambient_sound_instance_no"),
    (val_add, "$g_ambient_sound_instance_no", 1),
    (call_script, "script_cf_play_scene_ambient_sound", ":instance_id"),
    ], [])

music_situation_check = (25, 0, 0, [], # clients: try adjust the music for the current situation
   [(neg|multiplayer_is_server),
    (call_script, "script_music_set_situation"),
    ])

shadow_recalculation = (15, 1, 0, # clients: periodically recalculate environment shadows to fix them for moveable scene props
   [(neg|multiplayer_is_server),
    (eq, "$g_disable_automatic_shadow_recalculation", 0),
    (call_script, "script_cf_client_agent_is_inactive"),
    ],
   [(call_script, "script_cf_client_agent_is_inactive"),
    (rebuild_shadow_map),
    ])
    
handle_wild_animal_spawns = (280, 0, 0, [], # server: handle wild animal spawn zones e.g keeping the population up, var1 = animal type (1=boar,2=deer)
   [(multiplayer_is_server),
    (scene_prop_get_num_instances, ":max_spawns", "spr_wild_animal_spawn_zone"),
    (try_for_range, ":spawns_no", 0, ":max_spawns"),
      (scene_prop_get_instance, ":spawnpoint", "spr_wild_animal_spawn_zone", ":spawns_no"), # Validity check
      (prop_instance_get_position, pos1, ":spawnpoint"),
      (prop_instance_get_variation_id, ":animal_type", ":spawnpoint"),
      
      (try_begin),
        (eq,":animal_type",1),#Boar check
        (assign,":Amount",0),
        (try_for_agents, ":horse_agent_id"),
          (agent_get_item_id, ":horse_item_id", ":horse_agent_id"),
          (eq, ":horse_item_id", "itm_boar"),
          (val_add,":Amount",1),
        (try_end),
        
        # We dont need to check if we can spawn herd animals as we already checked for population
        (eq,":Amount",0),# There is no population so spawn in new animal type
        (call_script, "script_cf_spawn_herd_animal", "itm_boar", -1),
        (call_script, "script_cf_spawn_herd_animal", "itm_boar", -1),
        
      (else_try),
        (eq,":animal_type",2),#Deer
        (assign,":Amount",0),
        (try_for_agents, ":horse_agent_id"),
          (agent_get_item_id, ":horse_item_id", ":horse_agent_id"),
          (eq, ":horse_item_id", "itm_deer"),
          (val_add,":Amount",1),
        (try_end),
        
        # We dont need to check if we can spawn herd animals as we already checked for population
        (eq,":Amount",0),# There is no population so spawn in new animal type
        (call_script, "script_cf_spawn_herd_animal", "itm_deer", -1),
        (call_script, "script_cf_spawn_herd_animal", "itm_deer", -1),

      (try_end),
    (try_end),
    ])
    
remove_empty_ammo = (1, 0, 0, [], # server: handle agents remove empty ammo quivers
   [(multiplayer_is_server),
    (try_for_agents, ":agent_id"),
      (agent_is_active,":agent_id"),
      (agent_is_alive,":agent_id"),
      (try_for_range, ":slot_check", ek_item_0, ek_item_3 + 1),# Check for special ammo type
        (agent_get_item_slot, ":item_id", ":agent_id", ":slot_check"),
        (ge,":item_id",0),
        (item_get_type, ":slot_ammo_type", ":item_id"),
        (this_or_next|eq,":slot_ammo_type",itp_type_thrown),
        (this_or_next|eq,":slot_ammo_type",itp_type_arrows),
        (eq,":slot_ammo_type",itp_type_bolts),
        (agent_get_ammo_for_slot, ":ammo_amount", ":agent_id", ":slot_check"),
        (le,":ammo_amount",0),
        (assign,":quantity",0),
        (try_for_range, ":check_dups", ek_item_0, ek_item_3 + 1),
          (agent_get_item_slot, ":dup_check_id", ":agent_id", ":check_dups"),
          (eq,":dup_check_id",":item_id"),
          (val_add,":quantity",1),
        (try_end),
        (eq,":quantity",1), # Ensure we are not unequiping duplicates due to unequip item being buggy
        (agent_unequip_item, ":agent_id", ":item_id", ":slot_check"),
      (try_end),
    (try_end),
    ])
    
pitch_check = (1, 0, 0, [], # server: handle pitch
   [(multiplayer_is_server),
    (call_script, "script_cf_pitch_tick"),
    ])
    
ladder_collision = (0, 0, 0, [], # server: handle ladder colision
   [(multiplayer_is_server),
    (call_script, "script_cf_ladder_collision"),
    ])

ladder_death = (1, 0, 0, [], # server: handle ladder death
   [(multiplayer_is_server),
    (call_script, "script_cf_ladder_collision_death"),
    (call_script, "script_cf_ladder_death"),
    ])
    
sitting_check = (1, 0, 0, [], # server: handle agents sitting
   [(multiplayer_is_server),
    (try_for_agents, ":agent_id"),
      (agent_is_active,":agent_id"),
      (agent_is_alive,":agent_id"),
      (agent_is_human,":agent_id"),
      (agent_get_slot,":instance",":agent_id",slot_agent_scene_prop_in_use),
      (ge,":instance",0),
      (agent_get_animation, ":anim", ":agent_id", 0),
      (try_begin),
        (this_or_next|eq,":anim","anim_sitting"),
        (this_or_next|eq,":anim","anim_sitting_pillow_male"),
        (eq,":anim","anim_sitting_pillow_female"),
          (try_begin),
            (agent_get_position,pos2,":agent_id"),
            (prop_instance_get_position, pos4, ":instance"),
            (get_distance_between_positions,":dist",pos2,pos4),
            (gt, ":dist", 45),##If moved away from the chair stop the animation
            (call_script, "script_cf_do_custom_anims", ":agent_id", "anim_sitting_finish",0),
            (call_script, "script_cf_do_custom_anims", ":agent_id", "anim_sitting_finish",1),
            (agent_set_slot,":agent_id",slot_agent_scene_prop_in_use,-1),
          (try_end),
      (else_try),
        (eq,":anim","anim_sleep"),
          (agent_get_position,pos2,":agent_id"),
          (prop_instance_get_position, pos4, ":instance"),
          (get_distance_between_positions,":dist",pos2,pos4),
          (agent_get_wielded_item, ":weapon_item_id", ":agent_id", 0),
          (agent_get_wielded_item, ":shield_item_id", ":agent_id", 1),
          (try_begin),
            (gt, ":dist", 100),##If moved away from the bed stop the animation
              (call_script, "script_cf_do_custom_anims", ":agent_id", "anim_pose_finish",0),
              (call_script, "script_cf_do_custom_anims", ":agent_id", "anim_pose_finish",1),
              (agent_set_slot,":agent_id",slot_agent_scene_prop_in_use,-1),
          (else_try),
            (this_or_next|gt,":weapon_item_id",0), # if the player has a weapon or shield then stop sleeping
            (gt,":shield_item_id",0),
              (call_script, "script_cf_do_custom_anims", ":agent_id", "anim_pose_finish",0),
              (call_script, "script_cf_do_custom_anims", ":agent_id", "anim_pose_finish",1),
              (agent_set_slot,":agent_id",slot_agent_scene_prop_in_use,-1),
          (try_end),
      (else_try),##Agent isnt sitting anymore
        (agent_set_slot,":agent_id",slot_agent_scene_prop_in_use,-1),
        (call_script, "script_cf_do_custom_anims", ":agent_id", "anim_pose_finish",0),
        (call_script, "script_cf_do_custom_anims", ":agent_id", "anim_pose_finish",1),
      (try_end),
    (try_end),
    ])
    
pose_check = (1, 0, 0, [], # server: handle agents posing
   [(multiplayer_is_server),
    (try_for_agents, ":agent_id"),
      (agent_is_active,":agent_id"),
      (agent_is_alive,":agent_id"),
      (agent_is_human,":agent_id"),
      (agent_get_slot,":instance",":agent_id",slot_agent_pose_manager),
      (ge,":instance",0),
      (prop_instance_get_scene_prop_kind, ":scene_prop", ":instance"),
      (try_begin),
        (eq,":scene_prop","spr_code_pose_manager"),
        (prop_instance_is_valid, ":instance"),
        (agent_get_slot,":pose_anim",":agent_id",slot_agent_pose_anim),
        (ge,":pose_anim",0),
        (agent_get_animation, ":anim", ":agent_id", 1),
        (try_begin),
          (eq,":anim",":pose_anim"),
            (try_begin),
              (agent_get_position,pos2,":agent_id"),
              (prop_instance_get_position, pos4, ":instance"),
              (get_distance_between_positions,":dist",pos2,pos4),
              (gt, ":dist", 2),##If moved away from the manager stop the animation
              (call_script, "script_cf_do_custom_anims", ":agent_id", "anim_pose_finish",1),
              (agent_set_slot,":agent_id",slot_agent_pose_anim,-1),
              (agent_set_slot,":agent_id",slot_agent_pose_manager,-1),
              (call_script, "script_remove_scene_prop", ":instance","spr_code_pose_manager"),
            (try_end),
        (else_try),##Agent isnt being a poser anymore
          (agent_set_slot,":agent_id",slot_agent_pose_anim,-1),
          (agent_set_slot,":agent_id",slot_agent_pose_manager,-1),
          (call_script, "script_remove_scene_prop", ":instance","spr_code_pose_manager"),
        (try_end),
      (try_end),
    (try_end),
    ])
    
instrument_check = (2, 0, 0, [], # server: handle agents playing instruments
   [(multiplayer_is_server),
    (call_script, "script_cf_check_musical_instrument"),
    ])
    
instrument_killed = (ti_on_agent_killed_or_wounded, 0, 0, [], # handle instruments
   [
    (store_trigger_param_1, ":dead_agent_id"),
    (call_script, "script_client_stop_playing_musical_instrument", ":dead_agent_id"),
    ])

instrument_unwielded = (ti_on_item_unwielded, 0, 0, [], # handle instruments
   [
    (store_trigger_param_1, ":agent_id"),
    (call_script, "script_cf_stop_playing_musical_instrument", ":agent_id"),
    (eq,reg20,1),
    (call_script, "script_client_stop_playing_musical_instrument", ":agent_id"),
    ])
    
instrument_dropped = (ti_on_item_dropped, 0, 0, [], # handle instruments
   [
    (store_trigger_param_1, ":agent_id"),
    (call_script, "script_cf_stop_playing_musical_instrument", ":agent_id"),
    (eq,reg20,1),
    (call_script, "script_client_stop_playing_musical_instrument", ":agent_id"),
    ])
    
market_synch_leave = (ti_on_player_exit, 0, 0, [], # clients: ensure we always had an upto date name for the owner of the prop when leaving the server
   [(store_trigger_param_1, ":player_id"),
    (player_is_active,":player_id"),
    (call_script, "script_cf_player_leave_market",":player_id"),
    ])
    
setup_metalworks = (ti_after_mission_start, 0, 0, [], # server: setup the code props for metalworks
   [(multiplayer_is_server),
    (scene_prop_get_num_instances, ":anvils_amount", "spr_fw_metalworks_anvil"),
    (try_for_range, ":anvil_no", 0, ":anvils_amount"),
      (scene_prop_get_instance, ":anvil_id", "spr_fw_metalworks_anvil", ":anvil_no"), # Validity check
      (prop_instance_is_valid, ":anvil_id"),
      (prop_instance_get_position, pos0, ":anvil_id"),
      (position_set_x, pos0, -5000),
      (position_set_y, pos0, -5000),
      (position_set_z, pos0, -5000),
      (try_for_range, ":metal_types", "spr_code_heated_iron_piece", "spr_code_metalworks_end"), # Make all our metal types for this prop
        (set_spawn_position, pos0),
        (spawn_scene_prop, ":metal_types"),
        (scene_prop_set_slot, reg0, slot_scene_prop_state, scene_prop_state_hidden),
        (scene_prop_set_slot, reg0, slot_scene_prop_linked_scene_prop, ":anvil_id"),
      (try_end),
    (try_end),
    (scene_prop_get_num_instances, ":forge_amount", "spr_fw_metalworks_forge"),
    (try_for_range, ":forge_no", 0, ":forge_amount"),
      (scene_prop_get_instance, ":forge_id", "spr_fw_metalworks_forge", ":forge_no"),
      (prop_instance_is_valid, ":forge_id"),
      (prop_instance_get_position, pos0, ":forge_id"),
      (position_set_x, pos0, -5000),
      (position_set_y, pos0, -5000),
      (position_set_z, pos0, -5000),
      (try_for_range, ":metal_types", "spr_code_iron_piece", "spr_code_metalworks_end"), # Make all our metal types for this prop
        (set_spawn_position, pos0),
        (spawn_scene_prop, ":metal_types"),
        (scene_prop_set_slot, reg0, slot_scene_prop_state, scene_prop_state_hidden),
        (scene_prop_set_slot, reg0, slot_scene_prop_linked_scene_prop, ":forge_id"),
      (try_end),
    (try_end),
    (scene_prop_get_num_instances, ":manak_amount", "spr_fw_mannequin"),
    (try_for_range, ":manak_no", 0, ":manak_amount"),
      (scene_prop_get_instance, ":manak_id", "spr_fw_mannequin", ":manak_no"),
      (prop_instance_is_valid, ":manak_id"),
      (prop_instance_get_position, pos0, ":manak_id"),
      (try_for_range, ":body_parts", "spr_code_mannequin_head", "spr_code_mannequin_end"), # Make all our metal types for this prop
        (set_spawn_position, pos0),
        (spawn_scene_prop, ":body_parts"),
        (scene_prop_set_slot, reg0, slot_scene_prop_linked_scene_prop, ":manak_id"),
      (try_end),
    (try_end),
    ])
    
setup_herbs = (ti_after_mission_start, 0, 0, [], # server: setup the alchemy herbs to spawn near trees
   [(multiplayer_is_server),
    (try_for_range, ":tree_type", "spr_pw_tree_a1", "spr_pw_tree_trunk_a"), # Get all the trees on the map
      (scene_prop_get_num_instances, ":trees_amount", ":tree_type"),
      (try_for_range, ":tree_no", 0, ":trees_amount"),
        (scene_prop_get_instance, ":tree_id", ":tree_type", ":tree_no"), # Validity check
        (prop_instance_is_valid, ":tree_id"),
        (call_script, "script_cf_spawn_random_herb", ":tree_id"),
      (try_end),
    (try_end),
    ])

shackle_dropped = (ti_on_item_dropped, 0, 0, [], # server: handle agents dropping cuffs
   [(multiplayer_is_server),
    (store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":item_id"),
    (store_trigger_param_3, ":instance_id"),
    (agent_is_active,":agent_id"),
    (agent_is_alive,":agent_id"),
    
    (try_begin),
      (eq,":item_id","itm_cuffs"),
        (scene_prop_set_prune_time, ":instance_id", 0),
    (try_end),
    
    (agent_slot_eq,":agent_id",slot_agent_shackled,1),
    (call_script, "script_cf_equip_wield_item", ":agent_id", "itm_cuffs"),
    ])
    
shackle_death = (ti_on_agent_killed_or_wounded, 0, 0, [], # server: handles agents shackled on death
   [(multiplayer_is_server),
    (store_trigger_param_1, ":dead_agent_id"),
    (agent_is_active,":dead_agent_id"),
    (gt,":dead_agent_id",-1),#Check if player left the server
    (agent_set_slot,":dead_agent_id",slot_agent_shackled,0),
    ])
    
shackle_check = (0, 0, 0, [], # server: handle agents un-wielding cuffs # Not used
   [(multiplayer_is_server),
    (try_for_agents, ":agent_id"),
      (agent_is_active,":agent_id"),
      (agent_is_alive,":agent_id"),
      (agent_slot_eq,":agent_id",slot_agent_shackled,1),
      (agent_get_wielded_item,":equiped_item",":agent_id",0),
      (neq,":equiped_item","itm_cuffs"),
      (assign,":HasCuffs",0),
      (try_for_range, ":item_id", ek_item_0, ek_item_3 + 1),#Check for shackles
        (eq,":item_id","itm_cuffs"),
          (assign,":HasCuffs",1),
        (try_begin),
          (ge,":item_id",1),
          (neq,":item_id","itm_cuffs"),
          (assign,":HasCuffs",2),
        (try_end),
      (try_end),
      (try_begin),
        (eq,":HasCuffs",2),#Agent has cuffs but also other items
        (call_script, "script_cf_agent_drop_all_weapons", ":agent_id"),
        (call_script, "script_cf_equip_wield_item", ":agent_id", "itm_cuffs"),
      (else_try),
        (eq,":HasCuffs",1),#Has cuffs but not wielded
        (agent_set_wielded_item, ":agent_id", "itm_cuffs"),
      (else_try),#Dont have any items at all
        (call_script, "script_cf_agent_drop_all_weapons", ":agent_id"),
        (call_script, "script_cf_equip_wield_item", ":agent_id", "itm_cuffs"),
      (try_end),
    (try_end),
    ])
    
shackle_animation = (1, 0, 0, [], # server: handle animation for shackled players
   [(multiplayer_is_server),
    (try_for_agents, ":agent_id"),
      (agent_is_active,":agent_id"),
      (agent_is_alive,":agent_id"),
      (agent_is_human,":agent_id"),
      (agent_get_animation, ":anim", ":agent_id", 1),
      (agent_get_wielded_item,":equiped_item",":agent_id",0),
      
      (try_begin),
        (agent_slot_eq,":agent_id",slot_agent_shackled,1),
        (neq,":anim","anim_arrested"),
        (eq,":equiped_item","itm_cuffs"),
        (call_script, "script_cf_do_custom_anims", ":agent_id", "anim_arrested",1),
      (else_try),
        (agent_slot_eq,":agent_id",slot_agent_shackled,0),
        (eq,":anim","anim_arrested"),
        (call_script, "script_cf_do_custom_anims", ":agent_id", "anim_arrested_finish",1),
      (try_end),
    (try_end),
    ])
   
decap_check = (ti_on_agent_hit, 0, 0, [],
   [(multiplayer_is_server),
    (store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":inflictor_id"),
    (store_trigger_param_3, ":damage"),
    (copy_position, pos2, pos0),
    (agent_is_active,":agent_id"),
    (agent_is_active,":inflictor_id"),
    
    (agent_get_bone_position, pos10, ":agent_id", 5, 0),#debug
    
    (agent_is_human,":agent_id"),
    (agent_is_human,":inflictor_id"),
    
    (agent_get_player_id,":player_id",":agent_id"),
    (player_is_active,":player_id"),
    
    (store_agent_hit_points,":hp",":agent_id",1),
    
    (ge,":damage",":hp"), # did the agent die
    
    (gt,reg0,0), # make sure this person atleast used a weapon
    
    (agent_get_position, pos3, ":agent_id"),
    (get_distance_between_positions, ":distance", pos3, pos2),
    (agent_get_crouch_mode, ":is_crouched", ":agent_id"),
    (agent_get_horse, ":is_mounted", ":agent_id"),
    (try_begin), # is the agent crouched
      (eq,":is_crouched",1),
        (assign,":min_head",100),
        (assign,":max_head",130),
    (else_try), # is the agent mounted
      (ge, ":is_mounted", 0),
        (assign, ":min_head", 240),
        (assign, ":max_head", 270),
    (else_try), # otherwise just standing
      (assign,":min_head",160),
      (assign,":max_head",190),
    (try_end),
    (is_between, ":distance", ":min_head", ":max_head"), # ensure we hit head
    
    (agent_get_action_dir, ":attack_dir", ":inflictor_id"),
    (this_or_next|eq, ":attack_dir", 1),
    (eq, ":attack_dir", 2),
    
    (agent_get_position, pos1, ":agent_id"),
    (set_spawn_position, pos1),
    (spawn_agent,"trp_decaptroop"),
    (player_control_agent, ":player_id", reg0),
    
    (agent_get_item_slot, ":helmet", ":agent_id", ek_head),
    (try_begin),
      (le,":helmet","itm_no_head"),#if the player is wearing no helmet then set the helmet of the decap to invisable otherwise equip the helmet
      (call_script, "script_change_armor", reg0, "itm_no_head"),
    (else_try),
      (call_script, "script_change_armor", reg0, ":helmet"),
    (try_end),
    
    (call_script, "script_change_armor", ":agent_id", "itm_invisible_head"),
    
    (agent_get_position, pos4, reg0),
	  (position_move_z, pos4, ":min_head"),
    (particle_system_burst, "psys_blood_decapitation", pos4, 40), 
    (remove_agent, reg0),
    (player_get_death_count, ":death_count", ":player_id"),
    (val_sub, ":death_count",1),
    (player_set_death_count, ":player_id", ":death_count"),
    ])
 
toggle_walk = (
  0, 0, 0.1, [
  (neg|multiplayer_is_server),
  (neg|is_presentation_active, "prsnt_escape_menu"),
  (neg|is_presentation_active, "prsnt_admin_menu"),
  (neg|is_presentation_active, "prsnt_faction_admin_menu"),
  (neg|is_presentation_active, "prsnt_tabbed_stats_chart"),
  (neg|is_presentation_active, "prsnt_chat_box"),
  (neg|is_presentation_active, "prsnt_money_bag"),
  (neg|is_presentation_active, "prsnt_action_menu"),
  (neg|is_presentation_active, "prsnt_action_menu"),
  (game_key_clicked,gk_zoom),
  ],
  [
    (multiplayer_send_message_to_server, client_event_toggle_walk),
  ])

unofficial_server = (0, 0, 0, [],
   [(multiplayer_is_server),
    (get_max_players, ":max_players"),
    (try_for_range, ":player_id", 1, ":max_players"),
      (player_is_active, ":player_id"),
      (multiplayer_send_2_int_to_player, ":player_id", server_event_player_announce_message, reg0, "str_unofficial_server"),
    (try_end),
    ])

log_player_leave_gold = (ti_on_player_exit, 0, 0, [],
   [(multiplayer_is_server),
    (store_trigger_param_1, ":player_id"),
    
    (player_get_unique_id, reg1, ":player_id"),
    (str_store_player_username,s1,":player_id"),
    (player_get_gold, reg2, ":player_id"),
    (server_add_message_to_log, "str_log_leave_gold"),
    ])
    
log_damage = (ti_on_agent_hit, 0, 0, [],
   [(multiplayer_is_server),
    (store_trigger_param_1, ":hit_agent_id"),
    (store_trigger_param_2, ":attacker_agent_id"),
    (store_trigger_param_3, ":damage"),
    (agent_is_active,":hit_agent_id"),
    (agent_is_human,":hit_agent_id"),
    (agent_get_player_id,":hit_player_id",":hit_agent_id"),
    (player_is_active,":hit_player_id"),
    (agent_is_active,":attacker_agent_id"),
    (try_begin),
      (agent_is_human,":attacker_agent_id"),
      (assign,":valid_attacker_agent_id",":attacker_agent_id"),
    (else_try),
      (agent_get_rider,":attacker_rider_id",":attacker_agent_id"),
      (agent_is_active,":attacker_rider_id"),
      (assign,":valid_attacker_agent_id",":attacker_rider_id"), # ensure the rider is valid
      (agent_get_item_id,reg0, ":attacker_agent_id"),#Get the horse type
    (try_end),
    (agent_is_active,":valid_attacker_agent_id"),
    (agent_get_player_id,":attacker_player_id",":valid_attacker_agent_id"),
    (player_is_active,":attacker_player_id"),
    (player_get_unique_id, reg1, ":hit_player_id"),
    (str_store_player_username,s1,":hit_player_id"),
    (player_get_unique_id, reg2, ":attacker_player_id"),
    (str_store_player_username,s2,":attacker_player_id"),
    (assign,reg3,":damage"),
    (try_begin),
      (gt,reg0,-1),
      (is_between, reg0, all_items_begin, all_items_end),
      (str_store_item_name,s3,reg0),
    (else_try),
      (str_store_string,s3,"@fist/kick"),
    (try_end),
    (server_add_message_to_log, "str_log_damage"),
    ])
  
test_animation = (
  0, 0.5, 0.1, [
  (neg|multiplayer_is_server),
  (game_key_clicked,gk_everyone_hear),
  ],
  [
    (try_begin),
      (call_script,"script_client_get_my_agent"),
      (assign,":agent_id",reg0),
      (agent_is_active,":agent_id"),
      (agent_is_alive,":agent_id"),
      (multiplayer_send_2_int_to_server, client_event_agent_animate, "anim_play_flute"),
    (try_end),
  ])
    
test_height = (ti_on_item_dropped, 0, 0, [],
   [(multiplayer_is_server),
    (store_trigger_param_1, ":agent_id"),
    (agent_get_position, pos1, ":agent_id"),
    (set_spawn_position, pos1),
    (spawn_agent,"trp_test_race"),
    (agent_get_player_id,":player_id",":agent_id"),
    (player_control_agent, ":player_id", reg0),
    (remove_agent, ":agent_id"),
    ])
    
test_special_death = (ti_on_agent_knocked_down, 0, 0, [],
   [(multiplayer_is_server),
    (store_trigger_param_1, ":agent_id"),
    (agent_is_active,":agent_id"),
    (agent_get_player_id,":player_id",":agent_id"),
    (player_is_active,":player_id"),
    (player_get_troop_id, ":troop_id", ":player_id"),
    (try_begin),
      (eq,":troop_id","trp_godlike_hero"),
      (agent_fade_out, ":agent_id"),
    (try_end),
    ])
    
def common_triggers(self):
  return [(ti_before_mission_start, 0, 0, [(assign, "$g_game_type", "mt_" + self)], []),
    before_mission_start_setup,
    after_mission_start_setup,
    
    #unofficial_server,
    
    setup_metalworks,
    setup_herbs,
    
    player_joined,
    player_exit,

    agent_spawn,
    agent_killed,
    agent_hit,

    item_picked_up,
    item_dropped,
    item_wielded,
    item_unwielded,
 
    market_synch_leave,
    
    decap_check,
    
    log_player_leave_gold,
    log_damage,
    
    handle_wild_animal_spawns,
    
    remove_empty_ammo,
    
    pitch_check,
    ladder_collision,
    ladder_death,
    sitting_check,
    pose_check,
    toggle_walk,
    
    shackle_dropped,
    shackle_death,
    shackle_check,
    shackle_animation,
    
    instrument_check,
    instrument_killed,
    instrument_unwielded,
    instrument_dropped,

    agent_mount,
    agent_dismount,

    player_check_loop,
    agent_check_loop,
    agent_check_attack_loop,
    #ship_movement_loop,

    resource_regrow_check,
    polls_check,
    game_ended_check, # Debug testing for bugs for disabling this.
    draw_initial_banners,
    fill_chests_starting_inventory,
    fire_place_check,
    fish_school_loop,
    herd_leader_movement_loop,
    herd_follower_movement_loop,
    herd_animal_count_check,

    escape_pressed,
    tab_pressed,
    static_presentations_setup,
    action_menu_pressed,
    target_agent_pressed,
    chat_overlay_toggled,
    chat_resend_check,
    local_chat_pressed,
    whisper_chat_pressed,
    faction_chat_pressed,
    admin_chat_pressed,
    #ship_control_pressed,
    animation_menu_pressed,

    welcome_message,
    turn_windmill_fans,
    ambient_sounds_check,
    music_situation_check,
    shadow_recalculation,
    ]

mission_templates = [
  ("conquest", mtf_battle_mode, -1, "Conquest.", spawn_points_0_99,
    common_triggers("conquest") + [
    money_bag_pressed,
    ]),

  ("quick_battle", mtf_battle_mode, -1, "Quick battle.", spawn_points_0_99,
    common_triggers("quick_battle") + [
    money_bag_pressed,
    ]),

  ("no_money", mtf_battle_mode, -1, "No money.", spawn_points_0_99,
    common_triggers("no_money")
    ),

  ("feudalism", mtf_battle_mode, -1, "Feudalism.", spawn_points_0_99,
    common_triggers("feudalism") + [
    money_bag_pressed,
    ]),

  ("permanent_death", mtf_battle_mode, -1, "Permanent death.", spawn_points_0_99,
    common_triggers("permanent_death") + [
    money_bag_pressed,
    ]),

  ("edit_scene", 0, -1, "edit_scene", [(0,mtef_visitor_source,0,aif_start_alarmed,1,[])],
   [
    (ti_before_mission_start, 0, 0, [], # set up some basic values for scene editing features
     [(server_set_add_to_game_servers_list, 0),
      (assign, "$g_edit_scene", 1),
      (call_script, "script_scene_set_day_time"),
      (call_script, "script_setup_castle_names"),
      (troop_set_slot, "trp_removed_scene_props", 0),
      (call_script, "script_setup_all_linked_scene_props"),
      ]),

    (ti_after_mission_start, 0, 0, [], # set up more values and perform some scene checks
     [(set_spawn_effector_scene_prop_kind, team_default, -1),
      (team_set_relation, team_default, team_default, -1),
      (call_script, "script_initialize_troop_equipment_slots"),
      (call_script, "script_initialize_item_slots"),
      (try_begin),
        (neg|is_edit_mode_enabled),
        (display_message, "str_error_edit_mode_not_enabled"),
      (try_end),
      (display_message, "str_pw_editor_welcome"),
      (try_begin),
        (prop_instance_is_valid, 0),
        (prop_instance_get_scene_prop_kind, reg0, 0),
        (ge, reg0, "spr_pw_tree_a1"),
        (display_message, "str_error_scene_prop_0_pw"),
      (try_end),
      ]),

    (ti_server_player_joined, 0, 0, [], # spawn an agent to walk or ride around with
     [(store_trigger_param_1, ":player_id"),
      (player_set_team_no, ":player_id", team_default),
      (player_set_troop_id, ":player_id", "trp_player"),
      (entry_point_get_position, pos10, 0),
      (player_spawn_new_agent, ":player_id", 0),
      ]),

    (ti_on_agent_spawn, 0, 0, [], # move new agents near the position of previous ones
     [(store_trigger_param_1, ":agent_id"),
      (neg|agent_is_non_player, ":agent_id"),
      (agent_set_position, ":agent_id", pos10),
      ]),

    (ti_escape_pressed, 0, 0, [], # confirm leaving edit mode
     [(question_box, "str_leave_edit_mode"),
      ]),

    (ti_question_answered, 0, 0, [], # handle the leaving confirmation dialog
     [(store_trigger_param_1, ":answer"),
      (eq, ":answer", 0),
      (finish_mission),
      ]),

    (0, 0, 0, [(key_clicked, key_f1)], # show some basic editing information
     [(call_script, "script_preset_message", "str_pw_editor_info", preset_message_read_object, 0, 0),
      ]),

    (0, 0, 0, [(key_clicked, key_f2)], # list the meanings of scene prop values adjustable in the editor
     [(call_script, "script_preset_message", "str_pw_editor_values_info", preset_message_read_object, 0, 0),
      ]),

    (0, 0, 0, [(key_clicked, key_f3)], # list castle names with the corresponding numbers in the editor
     [(str_clear, s0),
      (store_sub, reg1, castle_names_end, castle_names_begin),
      (try_for_range_backwards, ":castle_name_string_id", castle_names_begin, castle_names_end),
        (val_sub, reg1, 1),
        (str_store_string, s1, ":castle_name_string_id"),
        (str_store_string, s0, "str_castle_names_numbers_format"),
      (try_end),
      (str_store_string, s2, s0),
      (call_script, "script_preset_message", "str_pw_editor_castle_names", preset_message_read_object, 0, 0),
      ]),

    (0, 0, 0, [(key_clicked, key_f12)], # measure distance between the player agent and the first pointer_arrow scene prop
     [(scene_prop_get_instance, ":instance_id", "spr_pointer_arrow", 0),
      (prop_instance_get_position, pos1, ":instance_id"),
      (get_player_agent_no, ":agent_id"),
      (agent_is_active, ":agent_id"),
      (agent_is_alive, ":agent_id"),
      (agent_get_position, pos2, ":agent_id"),
      (get_distance_between_positions, reg1, pos1, pos2),
      (get_sq_distance_between_positions, reg2, pos1, pos2),
      (display_message, "str_distance_reg1_sq_distance_reg2"),
      ]),

    (0, 0, 0, [(key_clicked, key_f11)], # spawn an admin horse for fast movement
     [(get_player_agent_no, ":agent_id"),
      (agent_is_active, ":agent_id"),
      (agent_is_alive, ":agent_id"),
      (agent_get_position, pos1, ":agent_id"),
      (position_move_x, 50),
      (set_spawn_position, pos1),
      (spawn_horse, "itm_admin_horse"),
      (agent_equip_item, ":agent_id", "itm_torch"),
      ]),

    (0, 0, 0, [(key_clicked, key_f10)], # iterate through the positions of all scene props added to the ship collison list
     [(troop_get_slot, ":collision_props_count", "trp_ship_array", slot_ship_array_collision_props_count),
      (try_begin),
        (ge, "$g_test_ship_collision_prop", ":collision_props_count"),
        (assign, "$g_test_ship_collision_prop", 0),
        (entry_point_get_position, pos1, 0),
      (else_try),
        (store_add, ":collision_prop_slot", slot_ship_array_collision_props_begin, "$g_test_ship_collision_prop"),
        (troop_get_slot, ":collision_instance_id", "trp_ship_array", ":collision_prop_slot"),
        (val_add, "$g_test_ship_collision_prop", 1),
        (prop_instance_get_position, pos1, ":collision_instance_id"),
      (try_end),
      (get_player_agent_no, ":agent_id"),
      (agent_is_active, ":agent_id"),
      (agent_is_alive, ":agent_id"),
      (agent_set_position, ":agent_id", pos1),
      ]),

    (0, 0, 0, [(key_clicked, key_f9)], # respawn a new player agent using a random troop
     [(multiplayer_get_my_player, ":player_id"),
      (player_get_agent_id, ":agent_id", ":player_id"),
      (try_begin),
        (agent_is_active, ":agent_id"),
        (agent_is_alive, ":agent_id"),
        (agent_fade_out, ":agent_id"),
        (try_for_range, ":player_equip_slot", slot_player_equip_item_0, slot_player_equip_end),
          (player_set_slot, ":player_id", ":player_equip_slot", 0),
        (try_end),
      (try_end),
      (store_random_in_range, ":troop_id", playable_troops_begin, playable_troops_end),
      (player_set_troop_id, ":player_id", ":troop_id"),
      (call_script, "script_player_add_default_troop_items", ":player_id", ":troop_id"),
      (call_script, "script_get_random_equipment", "itm_linen_tunic", "itm_tribal_warrior_outfit"),
      (player_set_slot, ":player_id", slot_player_equip_body, reg0),
      (call_script, "script_get_random_equipment", "itm_sarranid_boots_a", "itm_khergit_leather_boots"),
      (player_set_slot, ":player_id", slot_player_equip_foot, reg0),
      (call_script, "script_player_add_spawn_items", ":player_id", 1),
      (player_spawn_new_agent, ":player_id", 0),
      (mission_cam_get_position, pos10),
      ]),

    (0, 0, 0, [(key_clicked, key_f8)], # iterate through positions of all scene props that are not correctly linked with the other required props
     [(troop_get_slot, ":unlinked_prop_count", "trp_removed_scene_props", slot_array_count),
      (try_begin),
        (gt, ":unlinked_prop_count", 0),
        (lt, "$g_test_unlinked_prop", ":unlinked_prop_count"),
        (val_add, "$g_test_unlinked_prop", 1),
        (troop_get_slot, ":unlinked_instance_id", "trp_removed_scene_props", "$g_test_unlinked_prop"),
        (prop_instance_is_valid, ":unlinked_instance_id"),
        (assign, reg10, ":unlinked_instance_id"),
        (prop_instance_get_scene_prop_kind, reg11, ":unlinked_instance_id"),
        (prop_instance_get_variation_id_2, reg12, ":unlinked_instance_id"),
        (display_message, "str_error_unlinked_scene_prop"),
      (else_try),
        (assign, ":unlinked_instance_id", -1),
        (ge, "$g_test_unlinked_prop", ":unlinked_prop_count"),
        (assign, "$g_test_unlinked_prop", 0),
        (display_message, "str_no_more_unlinked_scene_props"),
        (prop_instance_is_valid, 0),
        (prop_instance_get_scene_prop_kind, reg0, 0),
        (ge, reg0, "spr_pw_tree_a1"),
        (display_message, "str_error_scene_prop_0_pw"),
        (assign, ":unlinked_instance_id", 0),
      (try_end),
      (try_begin),
        (neq, ":unlinked_instance_id", -1),
        (prop_instance_get_position, pos1, ":unlinked_instance_id"),
        (init_position, pos2),
        (position_get_rotation_around_z, ":rotation", pos1),
        (position_copy_rotation, pos1, pos2),
        (position_rotate_z, pos1, ":rotation"),
        (copy_position, pos2, pos1),
        (position_move_z, pos2, 300, 1),
        (set_spawn_position, pos2),
        (spawn_item, "itm_pointer_arrow", 0, 4),
        (prop_instance_set_position, reg0, pos2),
        (prop_instance_animate_to_position, reg0, pos1, 200),
        (get_player_agent_no, ":agent_id"),
        (agent_is_active, ":agent_id"),
        (agent_is_alive, ":agent_id"),
        (agent_set_position, ":agent_id", pos1),
      (try_end),
      ]),
      
    sitting_check,
    ladder_collision,
    ladder_death,

    ]),
]
