import secrets
import json
import os
from colorama import init, Fore, Back, Style
from datetime import datetime

# Initialize colorama for Windows CMD
init()

# Initialize player stats
player = {
    "score": 0,
    "health": 100,
    "max_health": 200,
    "artifacts": 0,
    "healing_potion": 0,
    "score_charm": 0,
    "artifact_key": 0,
    "relics": 0,
    "player_strength": secrets.randbelow(10) + 5,  # Cryptographically secure (5-15)
    "level": 1,
    "xp": 0,
    "xp_needed": 50
}

# Define companions
companions = [
    "DrysOG", "Baked", "Akihimura", "Brandon", "SS", "CatzBrownout", "Spvcestep",
    "LeafChicken", "Slink", "Toady", "Crabman", "DarkSkitZo", "toqer", "KenshinGM",
    "CEnnis91", "XoraLoyal", "alfalfa1", "Paramount", "JohnnyTest", "cuddly",
    "Jgunishka", "Moosehead", "Shinfuji", "Agent21iXi", "Firo", "Suprafast", "BadassBampy"
]

# Initialize companion stats
companion_stats = {name: {
    "health": secrets.randbelow(50) + 50,  # 50-100
    "strength": secrets.randbelow(10) + 5,  # 5-15
    "luck": secrets.randbelow(10) + 1  # 1-10
} for name in companions}

# Track fallen companions
fallen_companions = []

# Current companion
current_companion = {
    "name": "",
    "health": 0,
    "strength": 0,
    "luck": 0
}

# Global variables
relic_active = False
stat_changes = ""
last_ascii_used = None  # Track the last used ASCII art index

# List of unique ASCII art designs (labyrinth-themed, no house-like structures)
ascii_art_list = [
    # Start screen (rune circle)
    """
   *~~~*
  *     * 
 *  ***  * 
  *     * 
   *~~~*
""",
    # Path 1 (dark tunnel - swirling shadows)
    """
   ~~~~~
  ~     ~
 ~  ***  ~
  ~     ~
   ~~~~~
""",
    # Path 2 (torchlit tunnel - flame pattern)
    """
   ^^^^
  ^  *  ^
 ^  ***  ^
  ^  *  ^
   ^^^^
""",
    # Path 3 (hidden stairs - jagged steps)
    """
   /////
  /     /
 /  ***  /
  /     /
   /////
""",
    # Path 4 (crystal cavern - sparkling shards)
    """
   ****
  *  *  *
 *  ***  *
  *  *  *
   ****
""",
    # Inventory (sacred artifact)
    """
   +++++
  + *** +
 +  ***  +
  + *** +
   +++++
""",
    # Death/Victory (ancient orb)
    """
   oooo
  o     o
 o  ***  o
  o     o
   oooo
""",
    # Quit (fading glyph)
    """
   ====
  =  *  =
 =  ***  =
  =  *  =
   ====
"""
]

# Function to get random ASCII art, ensuring it's different from the last one
def get_random_ascii():
    global last_ascii_used
    available_indices = [i for i in range(len(ascii_art_list)) if i != last_ascii_used]
    if not available_indices:
        available_indices = list(range(len(ascii_art_list)))  # Fallback if only one art exists
    new_index = secrets.choice(available_indices)
    last_ascii_used = new_index
    return ascii_art_list[new_index]

# Save game to file
def save_game():
    global player, companion_stats, current_companion, fallen_companions, stat_changes
    game_state = {
        "player": {k: int(v) if isinstance(v, (int, float)) else v for k, v in player.items()},
        "companion_stats": {
            name: {k: int(v) if isinstance(v, (int, float)) else v for k, v in stats.items()}
            for name, stats in companion_stats.items()
        },
        "current_companion": {k: int(v) if isinstance(v, (int, float)) else v for k, v in current_companion.items()},
        "fallen_companions": fallen_companions
    }
    try:
        if os.path.exists("SaveGame.txt"):
            if os.path.exists("SaveGame.bak"):
                os.remove("SaveGame.bak")
            os.rename("SaveGame.txt", "SaveGame.bak")
        with open("SaveGame.txt", "w") as f:
            json.dump(game_state, f, indent=2)
        print(Fore.YELLOW + "Your saga is saved!" + Style.RESET_ALL)
        stat_changes = "Saga saved"
    except Exception as e:
        if os.path.exists("SaveGame.bak"):
            os.rename("SaveGame.bak", "SaveGame.txt")
            print(Fore.YELLOW + f"Failed to save saga, restored from backup... Error: {str(e)}" + Style.RESET_ALL)
            stat_changes = f"Failed to save saga, restored from backup: {str(e)}"
        else:
            print(Fore.YELLOW + f"Failed to save saga, no backup available... Error: {str(e)}" + Style.RESET_ALL)
            stat_changes = f"Failed to save saga, no backup available: {str(e)}"
        with open("GameLog.txt", "a") as f:
            f.write(f"{datetime.now().strftime('%m/%d/%Y %H:%M')} - Save failed: {str(e)}\n")
    return stat_changes

# Load game from file
def load_game():
    global player, companion_stats, current_companion, fallen_companions, stat_changes
    if not os.path.exists("SaveGame.txt"):
        print(Fore.YELLOW + "No saved saga found..." + Style.RESET_ALL)
        stat_changes = "No saved saga found"
        return
    try:
        with open("SaveGame.txt", "r") as f:
            game_state = json.load(f)
        
        default_player = {
            "score": 0, "health": 100, "max_health": 200, "artifacts": 0,
            "healing_potion": 0, "score_charm": 0, "artifact_key": 0, "relics": 0,
            "player_strength": secrets.randbelow(10) + 5, "level": 1, "xp": 0, "xp_needed": 50
        }
        for key in default_player:
            if key in game_state.get("player", {}):
                player[key] = int(game_state["player"][key]) if key in [
                    "score", "health", "max_health", "artifacts", "healing_potion",
                    "score_charm", "artifact_key", "relics", "player_strength", "level", "xp", "xp_needed"
                ] else game_state["player"][key]
            else:
                player[key] = default_player[key]
        
        companion_stats.clear()
        companion_stats.update({
            name: {"health": secrets.randbelow(50) + 50, "strength": secrets.randbelow(10) + 5, "luck": secrets.randbelow(10) + 1}
            for name in companions
        })
        for name, stats in game_state.get("companion_stats", {}).items():
            if name in companion_stats:
                companion_stats[name]["health"] = int(stats.get("health", companion_stats[name]["health"]))
                companion_stats[name]["strength"] = int(stats.get("strength", companion_stats[name]["strength"]))
                companion_stats[name]["luck"] = int(stats.get("luck", companion_stats[name]["luck"]))
        
        current_companion_data = game_state.get("current_companion", {})
        current_companion["name"] = current_companion_data.get("name", "")
        if current_companion["name"] in companion_stats:
            current_companion["health"] = int(current_companion_data.get("health", companion_stats[current_companion["name"]]["health"]))
            current_companion["strength"] = int(current_companion_data.get("strength", companion_stats[current_companion["name"]]["strength"]))
            current_companion["luck"] = int(current_companion_data.get("luck", companion_stats[current_companion["name"]]["luck"]))
            companion_stats[current_companion["name"]]["health"] = current_companion["health"]
        else:
            new_companion_name = companions[secrets.randbelow(len(companions))]
            current_companion.update({
                "name": new_companion_name,
                "health": companion_stats[new_companion_name]["health"],
                "strength": companion_stats[new_companion_name]["strength"],
                "luck": companion_stats[new_companion_name]["luck"]
            })
            companion_stats[new_companion_name]["health"] = current_companion["health"]
        
        fallen_companions.clear()
        fallen_companions.extend(game_state.get("fallen_companions", []))
        
        print(Fore.YELLOW + "The runes restore your journey!" + Style.RESET_ALL)
        stat_changes = "Saga restored"
    except Exception as e:
        print(Fore.YELLOW + f"Failed to load saga... Error: {str(e)}" + Style.RESET_ALL)
        stat_changes = f"Failed to load saga: {str(e)}"
        with open("GameLog.txt", "a") as f:
            f.write(f"{datetime.now().strftime('%m/%d/%Y %H:%M')} - Save failed: {str(e)}\n")
    return stat_changes

# Cryptographically secure D5+D5 roll
def roll_dice():
    die1 = secrets.randbelow(5) + 1
    die2 = secrets.randbelow(5) + 1
    outcome = (die1 - 1) * 5 + die2
    luck_modifier = current_companion["luck"] - 5 if current_companion["name"] else 0
    adjusted_grid = max(1, min(25, outcome + luck_modifier))
    return die1, die2, outcome, adjusted_grid

# Level check
def level_check(xp_change):
    global player, stat_changes
    player["xp"] += xp_change
    if player["xp"] >= player["xp_needed"] and player["level"] < 1000:
        player["level"] += 1
        player["max_health"] += 10
        if player["max_health"] > 100000:
            player["max_health"] = 100000
        player["health"] += 5
        levelup_health_change = 5
        player["xp"] -= player["xp_needed"]
        if player["xp"] > 1000000:
            player["xp"] = 1000000
        player["xp_needed"] = player["level"] * 50
        if player["xp_needed"] > 1000000:
            player["xp_needed"] = 1000000
        if player["healing_potion"] < 3:
            player["healing_potion"] += 1
            stat_changes = f"Level {player['level']} reached, Max Health +10, Health +5, Potions +1"
        else:
            stat_changes = f"Level {player['level']} reached, Max Health +10, Health +5"
        return levelup_health_change
    elif player["level"] >= 1000:
        stat_changes = "Max Level 1000 reached, no further leveling"
    return 0

# Check if outcome is positive
def is_positive_outcome(changes):
    return (changes.get("player_health", 0) >= 0 and
            changes.get("comp_health", 0) >= 0 and
            (changes.get("artifacts", 0) > 0 or
             changes.get("healing_potion", 0) > 0 or
             changes.get("score_charm", 0) > 0 or
             changes.get("artifact_key", 0) > 0 or
             changes.get("relics", 0) > 0 or
             changes.get("score", 0) > 0))

# Path outcomes
def path_outcomes(path, adjusted_grid):
    global player, current_companion, stat_changes, relic_active
    outcomes = {
        1: {
            1: ("A shimmering idol glints in the shadows", {"score": 8 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            2: ("Spiked arrows shoot from hidden slits", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            3: ("An enchanted stone pulses with energy", {"score": 6 + player["level"], "artifacts": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            4: ("A venomous scorpion stings", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            5: ("A blessed potion lies in the dust", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            6: ("Poisonous gas seeps from the walls", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            7: ("Ancient roots mend your wounds", {"score": 3 + player["level"], "xp": 5, "player_health": 4, "comp_health": 4}),
            8: ("A chasm trap triggers", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            9: ("A cryptic mural unveils wisdom", {"score": 4 + player["level"], "artifacts": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            10: ("Phantom shades assault", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            11: ("A glowing gem hums softly", {"score": 6 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            12: ("A cursed trap springs", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            13: ("A sacred key gleams in the dark", {"score": 5 + player["level"], "artifact_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            14: ("A spectral guardian strikes", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            15: ("An ancient altar restores vitality", {"score": 3 + player["level"], "healing_potion": 1, "xp": 5, "player_health": 4, "comp_health": 4}),
            16: ("A collapsing wall crushes", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            17: ("A mystic glyph grants insight", {"score": 4 + player["level"], "artifacts": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            18: ("A hidden blade trap triggers", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            19: ("A radiant orb pulses with power", {"score": 6 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            20: ("A venomous mist engulfs you", {"score": 3 + player["level"], "xp": 5, "player_health": -15 + player["player_strength"], "comp_health": -15 + current_companion["strength"]}),
            21: ("A sacred relic shines faintly", {"score": 5 + player["level"], "relics": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            22: ("A swarm of shadow bats attacks", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            23: ("A hidden cache yields a charm", {"score": 5 + player["level"], "score_charm": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            24: ("A cursed idol drains vitality", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            25: ("An enchanted shrine restores power", {"score": 5 + player["level"], "xp": 8, "player_health": 4, "comp_health": 4})
        },
        2: {
            1: ("A radiant sigil flares with light", {"score": 8 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            2: ("Slippery rocks cause a fall", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            3: ("A holy amulet glows brightly", {"score": 6 + player["level"], "artifacts": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            4: ("Thorny tendrils lash out", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            5: ("A sudden flame jet scorches", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            6: ("An unstable floor collapses", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            7: ("Healing balm restores vitality", {"score": 3 + player["level"], "healing_potion": 1, "xp": 5, "player_health": 4, "comp_health": 4}),
            8: ("The ground crumbles", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            9: ("Etched runes share their knowledge", {"score": 4 + player["level"], "artifacts": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            10: ("A desert wraith attacks", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            11: ("A mystic shrine restores power", {"score": 6 + player["level"], "xp": 10, "player_health": 4, "comp_health": 4}),
            12: ("A cursed trap triggers", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            13: ("A sacred key gleams in the torchlight", {"score": 5 + player["level"], "artifact_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            14: ("A spectral beast lunges", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            15: ("A hidden potion shines faintly", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            16: ("A collapsing ceiling traps you", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            17: ("A mystic glyph restores vitality", {"score": 4 + player["level"], "xp": 6, "player_health": 4, "comp_health": 4}),
            18: ("A hidden spike trap springs", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            19: ("A radiant orb grants wisdom", {"score": 6 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            20: ("A sacred relic pulses with power", {"score": 5 + player["level"], "relics": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            21: ("A shadow assassin strikes", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            22: ("A cursed flame erupts", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            23: ("A hidden cache yields a charm", {"score": 5 + player["level"], "score_charm": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            24: ("A mystic trap drains energy", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            25: ("An enchanted shrine restores power", {"score": 5 + player["level"], "xp": 8, "player_health": 4, "comp_health": 4})
        },
        3: {
            1: ("A dawn gem radiates warmth", {"score": 8 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            2: ("A steep tumble grazes", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            3: ("A sacred slab of Anubis is revealed", {"score": 6 + player["level"], "artifacts": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            4: ("A stumble on jagged steps", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            5: ("A blessed elixir lies in the rubble", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            6: ("A hidden spike pit triggers", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            7: ("Ancient etchings bestow insight", {"score": 3 + player["level"], "xp": 5, "player_health": 4, "comp_health": 4}),
            8: ("A swarm of bats overwhelms", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            9: ("A mystic key gleams in the dust", {"score": 4 + player["level"], "artifact_key": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            10: ("Falling debris strikes", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            11: ("A glowing shrine restores power", {"score": 6 + player["level"], "xp": 10, "player_health": 4, "comp_health": 4}),
            12: ("A cursed trap springs", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            13: ("A sacred charm shines faintly", {"score": 5 + player["level"], "score_charm": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            14: ("A spectral guardian attacks", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            15: ("A hidden altar restores vitality", {"score": 3 + player["level"], "healing_potion": 1, "xp": 5, "player_health": 4, "comp_health": 4}),
            16: ("A collapsing stair crushes", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            17: ("A radiant orb pulses with power", {"score": 6 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            18: ("A hidden blade trap triggers", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            19: ("A sacred relic glows softly", {"score": 5 + player["level"], "relics": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            20: ("A venomous mist engulfs you", {"score": 3 + player["level"], "xp": 5, "player_health": -15 + player["player_strength"], "comp_health": -15 + current_companion["strength"]}),
            21: ("A hidden cache yields a potion", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            22: ("A shadow assassin strikes", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            23: ("A mystic glyph grants wisdom", {"score": 4 + player["level"], "artifacts": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            24: ("A cursed idol drains vitality", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            25: ("An enchanted shrine restores power", {"score": 5 + player["level"], "xp": 8, "player_health": 4, "comp_health": 4})
        },
        4: {
            1: ("A luminous jewel dazzles the eye", {"score": 8 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            2: ("Sharp crystals pierce", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            3: ("A glowing sphere hums with magic", {"score": 6 + player["level"], "artifacts": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            4: ("A crystal hawk dives", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            5: ("A radiant potion shines in a crevice", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            6: ("A crystal shard trap springs", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            7: ("A mystic shrine restores vitality", {"score": 3 + player["level"], "xp": 5, "player_health": 4, "comp_health": 4}),
            8: ("A crystalline trap triggers", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            9: ("A crystal prism grants foresight", {"score": 4 + player["level"], "artifacts": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            10: ("A sacred key sparkles in the glow", {"score": 5 + player["level"], "artifact_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            11: ("A glowing shrine restores power", {"score": 6 + player["level"], "xp": 10, "player_health": 4, "comp_health": 4}),
            12: ("A cursed trap springs", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            13: ("A sacred charm glows softly", {"score": 5 + player["level"], "score_charm": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            14: ("A spectral beast lunges", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            15: ("A hidden potion shines faintly", {"score": 3 + player["level"], "healing_potion": 1, "xp": 5, "player_health": 4, "comp_health": 4}),
            16: ("A collapsing crystal wall crushes", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            17: ("A radiant orb grants wisdom", {"score": 6 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            18: ("A hidden blade trap triggers", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            19: ("A sacred relic pulses with power", {"score": 5 + player["level"], "relics": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            20: ("A shadow assassin strikes", {"score": 3 + player["level"], "xp": 5, "player_health": -15 + player["player_strength"], "comp_health": -15 + current_companion["strength"]}),
            21: ("A hidden cache yields a potion", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            22: ("A cursed flame erupts", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            23: ("A mystic glyph grants wisdom", {"score": 4 + player["level"], "artifacts": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            24: ("A mystic trap drains energy", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            25: ("An enchanted shrine restores power", {"score": 5 + player["level"], "xp": 8, "player_health": 4, "comp_health": 4})
        }
    }
    result, changes = outcomes[path][adjusted_grid]
    was_fallen = current_companion["name"] in fallen_companions
    if was_fallen and is_positive_outcome(changes):
        changes["comp_health"] += 10
        if current_companion["name"] in fallen_companions:
            fallen_companions.remove(current_companion["name"])
    return result, changes

# Inventory menu
def inventory():
    global player, current_companion, stat_changes, relic_active
    while True:
        os.system("cls")
        print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.YELLOW + "OGENS CLAX NEXUS - D5+D5" + Style.RESET_ALL)
        print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.YELLOW + get_random_ascii() + Style.RESET_ALL)
        print(Fore.YELLOW + "\nSACRED ITEMS..." + Style.RESET_ALL)
        print(Fore.YELLOW + f"\nHealing Potion ({player['healing_potion']}): Restores vitality..." + Style.RESET_ALL)
        print(Fore.YELLOW + f"Score Charm ({player['score_charm']}): Grants wisdom..." + Style.RESET_ALL)
        print(Fore.YELLOW + f"Artifact Key ({player['artifact_key']}): Unlocks secrets..." + Style.RESET_ALL)
        print(Fore.YELLOW + f"Relic ({player['relics']}): Doubles score gains for the next event..." + Style.RESET_ALL)
        print(Fore.YELLOW + "\nUSE AN ITEM..." + Style.RESET_ALL)
        print(Fore.YELLOW + "1. Healing Potion (+25 health)" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Score Charm (+20 score)" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Artifact Key (+4 artifacts)" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Relic (Double score next event)" + Style.RESET_ALL)
        print(Fore.YELLOW + "5. Return" + Style.RESET_ALL)
        inv_choice = input(Fore.YELLOW + "\nSelect an item (1-5): " + Style.RESET_ALL).strip()
        if inv_choice not in ["1", "2", "3", "4", "5"]:
            stat_changes = "Invalid choice"
            print(Fore.YELLOW + "\nINVALID CHOICE..." + Style.RESET_ALL)
            print(Fore.YELLOW + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
            print(Fore.YELLOW + "\nPress Enter to try again..." + Style.RESET_ALL)
            input()
            continue
        if inv_choice == "1":
            if player["healing_potion"] > 0:
                pre_player_health = player["health"]
                pre_comp_health = current_companion["health"] if current_companion["name"] else 0
                player["health"] += 25
                player["healing_potion"] -= 1
                if player["health"] > player["max_health"]:
                    player["health"] = player["max_health"]
                    stat_changes = f"Health capped at {player['max_health']}, Potions -1"
                else:
                    stat_changes = "Health +25, Potions -1"
                if current_companion["name"]:
                    current_companion["health"] = min(100, current_companion["health"] + 20)
                    companion_stats[current_companion["name"]]["health"] = current_companion["health"]
                    if current_companion["name"] in fallen_companions and current_companion["health"] > 0:
                        fallen_companions.remove(current_companion["name"])
                    stat_changes += f", {current_companion['name']}'s Health +20, Total Damage: Player [{pre_player_health} -> {player['health']}], Companion [{pre_comp_health} -> {current_companion['health']}]"
                else:
                    stat_changes += f", Total Damage: Player [{pre_player_health} -> {player['health']}]"
                print(Fore.YELLOW + "\nHealing Potion used - Vitality restored..." + Style.RESET_ALL)
            else:
                stat_changes = "No Healing Potions remain"
                print(Fore.YELLOW + "\nNo Healing Potions remain..." + Style.RESET_ALL)
        elif inv_choice == "2":
            if player["score_charm"] > 0:
                player["score"] += 20
                player["score_charm"] -= 1
                stat_changes = "Score +20, Charms -1"
                print(Fore.YELLOW + "\nScore Charm used - Wisdom gained..." + Style.RESET_ALL)
            else:
                stat_changes = "No Score Charms remain"
                print(Fore.YELLOW + "\nNo Score Charms remain..." + Style.RESET_ALL)
        elif inv_choice == "3":
            if player["artifact_key"] > 0:
                player["artifacts"] += 4
                player["artifact_key"] -= 1
                stat_changes = "Artifacts +4, Keys -1"
                print(Fore.YELLOW + "\nArtifact Key used - Secrets unlocked..." + Style.RESET_ALL)
            else:
                stat_changes = "No Artifact Keys remain"
                print(Fore.YELLOW + "\nNo Artifact Keys remain..." + Style.RESET_ALL)
        elif inv_choice == "4":
            if player["relics"] > 0:
                player["relics"] -= 1
                relic_active = True
                stat_changes = "Relic used - Score doubled for next event, Relics -1"
                print(Fore.YELLOW + "\nRelic used - Next event's score gains will be doubled..." + Style.RESET_ALL)
            else:
                stat_changes = "No Relics remain"
                print(Fore.YELLOW + "\nNo Relics remain..." + Style.RESET_ALL)
        elif inv_choice == "5":
            return
        print(Fore.YELLOW + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
        print(Fore.YELLOW + "\nPress Enter to return..." + Style.RESET_ALL)
        input()

# Main game loop
def main():
    global player, current_companion, stat_changes, relic_active, fallen_companions
    companion_name = companions[secrets.randbelow(len(companions))]
    current_companion.update({
        "name": companion_name,
        "health": companion_stats[companion_name]["health"],
        "strength": companion_stats[companion_name]["strength"],
        "luck": companion_stats[companion_name]["luck"]
    })
    companion_stats[companion_name]["health"] = current_companion["health"]

    os.system("cls")
    print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
    print(Fore.YELLOW + "OGENS CLAX NEXUS - D5+D5" + Style.RESET_ALL)
    print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
    print(Fore.YELLOW + get_random_ascii() + Style.RESET_ALL)
    print(Fore.YELLOW + "OGENS CLAX NEXUS" + Style.RESET_ALL)
    print(Fore.YELLOW + "ENTER THE LABYRINTH" + Style.RESET_ALL)
    print(Fore.YELLOW + f"\nCompanion: {current_companion['name']} joins you in the labyrinth..." + Style.RESET_ALL)
    print(Fore.YELLOW + "\n\n        Press Enter to go into" + Style.RESET_ALL)
    print(Fore.YELLOW + "    OG3Ns Cl4X Nexus Labyrinth..." + Style.RESET_ALL)
    input()

    while True:
        os.system("cls")
        score_change = 0
        player_health_change = 0
        comp_health_change = 0
        artifact_change = 0
        potion_change = 0
        charm_change = 0
        key_change = 0
        relic_change = 0
        xp_change = 0
        levelup_health_change = 0
        show_health_change = False
        pre_player_health = player["health"]
        pre_comp_health = current_companion["health"] if current_companion["name"] else 0
        post_player_health = pre_player_health
        post_comp_health = pre_comp_health

        print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.YELLOW + "OGENS CLAX NEXUS - D5+D5" + Style.RESET_ALL)
        print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.YELLOW + "\nEXPLORING THE ANCIENT LABYRINTH..." + Style.RESET_ALL)
        print(Fore.YELLOW + f"\nStrength: {player['player_strength']}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Level: {player['level']} (XP: {player['xp']}/{player['xp_needed']})" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Health: {player['health']}  Score: {player['score']}  Artifacts: {player['artifacts']}  Relics: {player['relics']}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Progress: Score {player['score']}/6000 Artifacts {player['artifacts']}/300 Relics {player['relics']}/50" + Style.RESET_ALL)
        if current_companion["name"]:
            print(Fore.YELLOW + f"\nCompanion: {current_companion['name']} (Health: {current_companion['health']}, Strength: {current_companion['strength']}, Luck: {current_companion['luck']})" + Style.RESET_ALL)
        if stat_changes:
            print(Fore.YELLOW + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
        print(Fore.YELLOW + "\n    1 2" + Style.RESET_ALL)
        print(Fore.YELLOW + "   ( o )" + Style.RESET_ALL)
        print(Fore.YELLOW + "    3 4" + Style.RESET_ALL)
        print(Fore.YELLOW + "    ORB" + Style.RESET_ALL)
        print(Fore.YELLOW + "\nCHOOSE YOUR PATH..." + Style.RESET_ALL)
        print(Fore.YELLOW + "Path 1 - Left Tunnel (dark and narrow)" + Style.RESET_ALL)
        print(Fore.YELLOW + "Path 2 - Right Tunnel (lit by torches)" + Style.RESET_ALL)
        print(Fore.YELLOW + "Path 3 - Hidden Stairs (ancient and crumbling)" + Style.RESET_ALL)
        print(Fore.YELLOW + "Path 4 - Crystal Cavern (glowing faintly)" + Style.RESET_ALL)
        print(Fore.YELLOW + "Path 5 - Inventory" + Style.RESET_ALL)
        print(Fore.YELLOW + "Path 6 - Character List" + Style.RESET_ALL)
        print(Fore.YELLOW + "Path 7 - Save Game" + Style.RESET_ALL)
        print(Fore.YELLOW + "Path 8 - Load Game" + Style.RESET_ALL)
        print(Fore.YELLOW + "Path 9 - Quit" + Style.RESET_ALL)
        choice = input(Fore.YELLOW + "\nEnter path (1-9): " + Style.RESET_ALL).strip()

        stat_changes = ""

        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            stat_changes = "Invalid path selected"
            print(Fore.YELLOW + "\nINVALID PATH SELECTED..." + Style.RESET_ALL)
            print(Fore.YELLOW + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
            print(Fore.YELLOW + "\nPress Enter to try again..." + Style.RESET_ALL)
            input()
            continue

        if choice in ["1", "2", "3", "4"]:
            path = int(choice)
            path_messages = {
                1: "TRAVERSING THE LEFT TUNNEL...",
                2: "TRAVERSING THE RIGHT TUNNEL...",
                3: "CLIMBING THE HIDDEN STAIRS...",
                4: "ENTERING THE CRYSTAL CAVERN..."
            }
            os.system("cls")
            print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.YELLOW + "OGENS CLAX NEXUS - D5+D5" + Style.RESET_ALL)
            print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.YELLOW + f"\n{path_messages[path]}" + Style.RESET_ALL)
            print(Fore.YELLOW + get_random_ascii() + Style.RESET_ALL)
            companion_name = companions[secrets.randbelow(len(companions))]
            was_fallen = companion_name in fallen_companions
            pre_comp_health = companion_stats[companion_name]["health"]
            current_companion.update({
                "name": companion_name,
                "health": companion_stats[companion_name]["health"],
                "strength": companion_stats[companion_name]["strength"],
                "luck": companion_stats[companion_name]["luck"]
            })
            companion_stats[companion_name]["health"] = current_companion["health"]
            print(Fore.YELLOW + f"{current_companion['name']} {'(Fallen) ' if was_fallen else ''}joins you for this journey..." + Style.RESET_ALL)
            die1, die2, outcome, adjusted_grid = roll_dice()
            print(Fore.YELLOW + "Rolling for the path's challenge..." + Style.RESET_ALL)
            print(Fore.YELLOW + f"Die 1 (D5): {die1} + Die 2 (D5): {die2} = Outcome {outcome} (Adjusted by Luck: {adjusted_grid})" + Style.RESET_ALL)
            result, changes = path_outcomes(path, adjusted_grid)
            revive_message = ""
            if was_fallen and is_positive_outcome(changes):
                revive_message = f"{current_companion['name']} is revived with +10 health!"
            relic_message = ""
            score_change = changes.get("score", 0)
            if relic_active:
                if score_change == 0:
                    score_change = 5
                    relic_message = "Relic grants +5 score"
                else:
                    score_change *= 2
                    relic_message = "Relic doubled score gain"
                relic_active = False
            player["score"] = min(10000000, max(0, player["score"] + score_change))
            player_health_change = changes.get("player_health", 0)
            comp_health_change = changes.get("comp_health", 0)
            player["artifacts"] += changes.get("artifacts", 0)
            player["healing_potion"] += changes.get("healing_potion", 0)
            player["score_charm"] += changes.get("score_charm", 0)
            player["artifact_key"] += changes.get("artifact_key", 0)
            player["relics"] += changes.get("relics", 0)
            xp_change = changes.get("xp", 0)
            if current_companion["name"]:
                current_companion["health"] = max(0, min(100, current_companion["health"] + comp_health_change))
                companion_stats[current_companion["name"]]["health"] = current_companion["health"]
            player["health"] += player_health_change
            post_player_health = player["health"]
            post_comp_health = current_companion["health"] if current_companion["name"] else 0
            levelup_health_change = level_check(xp_change)
            if player["health"] > player["max_health"]:
                stat_changes = f"Health capped at {player['max_health']}"
                player["health"] = player["max_health"]
                post_player_health = player["health"]
            stat_changes_list = []
            if score_change != 0:
                stat_changes_list.append(f"Score {'+' if score_change > 0 else ''}{score_change}")
            if relic_message:
                stat_changes_list.append(relic_message)
            if revive_message:
                stat_changes_list.append(revive_message)
            if player_health_change != 0 or levelup_health_change != 0:
                total_health_change = player_health_change + levelup_health_change
                stat_changes_list.append(f"Health {'+' if total_health_change > 0 else ''}{total_health_change}")
                show_health_change = True
            if show_health_change:
                stat_changes_list.append(f"Total Damage: Player [{pre_player_health} -> {post_player_health}]" + (f", Companion [{pre_comp_health} -> {post_comp_health}]" if current_companion["name"] else ""))
            if changes.get("artifacts", 0) != 0:
                stat_changes_list.append(f"Artifacts {'+' if changes['artifacts'] > 0 else ''}{changes['artifacts']}")
            if changes.get("healing_potion", 0) != 0:
                stat_changes_list.append(f"Potions {'+' if changes['healing_potion'] > 0 else ''}{changes['healing_potion']}")
            if changes.get("score_charm", 0) != 0:
                stat_changes_list.append(f"Charms {'+' if changes['score_charm'] > 0 else ''}{changes['score_charm']}")
            if changes.get("artifact_key", 0) != 0:
                stat_changes_list.append(f"Keys {'+' if changes['artifact_key'] > 0 else ''}{changes['artifact_key']}")
            if changes.get("relics", 0) != 0:
                stat_changes_list.append(f"Relics {'+' if changes['relics'] > 0 else ''}{changes['relics']}")
            if xp_change != 0:
                stat_changes_list.append(f"XP +{xp_change}")
            if comp_health_change != 0 and current_companion["name"]:
                stat_changes_list.append(f"{current_companion['name']}'s Health {'+' if comp_health_change > 0 else ''}{comp_health_change}")
            stat_changes = ", ".join(stat_changes_list) if stat_changes_list else stat_changes
            if current_companion["health"] <= 0 and current_companion["name"]:
                if current_companion["name"] not in fallen_companions:
                    fallen_companions.append(current_companion["name"])
                stat_changes = f"{stat_changes}, {current_companion['name']} has fallen..." if stat_changes else f"{current_companion['name']} has fallen..."
                print(Fore.YELLOW + f"\n{current_companion['name']} has fallen in the labyrinth..." + Style.RESET_ALL)
            print(Fore.YELLOW + f"\n{current_companion['name']} - {result}" + Style.RESET_ALL)
            if stat_changes:
                print(Fore.YELLOW + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
            print(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
            input()
        elif choice == "5":
            inventory()
        elif choice == "6":
            os.system("cls")
            print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.YELLOW + "OGENS CLAX NEXUS - D5+D5" + Style.RESET_ALL)
            print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.YELLOW + "\nANCIENT COMPANIONS..." + Style.RESET_ALL)
            for name in companions:
                status = "(Fallen)" if name in fallen_companions else ""
                print(Fore.YELLOW + f"{name} {status} - Health: {companion_stats[name]['health']}, Strength: {companion_stats[name]['strength']}, Luck: {companion_stats[name]['luck']}" + Style.RESET_ALL)
            print(Fore.YELLOW + "\nPress Enter to return..." + Style.RESET_ALL)
            stat_changes = "Viewed companion list"
            input()
        elif choice == "7":
            stat_changes = save_game()
            print(Fore.YELLOW + "\nPress Enter to return..." + Style.RESET_ALL)
            input()
        elif choice == "8":
            stat_changes = load_game()
            print(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)
            input()
        elif choice == "9":
            os.system("cls")
            print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.YELLOW + "OGENS CLAX NEXUS - D5+D5" + Style.RESET_ALL)
            print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.YELLOW + get_random_ascii() + Style.RESET_ALL)
            print(Fore.YELLOW + "\nLEAVING THE LABYRINTH Goodbye Traveler..." + Style.RESET_ALL)
            print(Fore.YELLOW + f"\nFinal Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Health: {player['health']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Artifacts: {player['artifacts']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Relics: {player['relics']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Level: {player['level']}" + Style.RESET_ALL)
            now = datetime.now()
            print(Fore.YELLOW + f"\nDate: {now.strftime('%m/%d/%Y')}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Time: {now.strftime('%H:%M')}" + Style.RESET_ALL)
            with open("GameLog.txt", "a") as f:
                f.write(f"{now.strftime('%m/%d/%Y %H:%M')} - Quit - Score: {player['score']}, Health: {player['health']}, Artifacts: {player['artifacts']}, Relics: {player['relics']}, Level: {player['level']}\n")
            print(Fore.YELLOW + "\nPress Enter to end..." + Style.RESET_ALL)
            input()
            break
        if player["health"] <= 0:
            os.system("cls")
            print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.YELLOW + "OGENS CLAX NEXUS - D5+D5" + Style.RESET_ALL)
            print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.YELLOW + get_random_ascii() + Style.RESET_ALL)
            print(Fore.YELLOW + "\nTHE LABYRINTH CLAIMS YOU U Fail..." + Style.RESET_ALL)
            print(Fore.YELLOW + f"\nFinal Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Health: {player['health']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Artifacts: {player['artifacts']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Relics: {player['relics']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Level: {player['level']}" + Style.RESET_ALL)
            now = datetime.now()
            print(Fore.YELLOW + f"\nDate: {now.strftime('%m/%d/%Y')}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Time: {now.strftime('%H:%M')}" + Style.RESET_ALL)
            with open("GameLog.txt", "a") as f:
                f.write(f"{now.strftime('%m/%d/%Y %H:%M')} - Loss - Score: {player['score']}, Health: {player['health']}, Artifacts: {player['artifacts']}, Relics: {player['relics']}, Level: {player['level']}\n")
            print(Fore.YELLOW + "\nPress Enter to end..." + Style.RESET_ALL)
            input()
            break
        if player["score"] >= 6000 and player["artifacts"] >= 300 and player["relics"] >= 50:
            os.system("cls")
            print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.YELLOW + "OGENS CLAX NEXUS - D5+D5" + Style.RESET_ALL)
            print(Fore.YELLOW + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.YELLOW + get_random_ascii() + Style.RESET_ALL)
            print(Fore.YELLOW + "\nVICTORY OVER THE LABYRINTH U Win..." + Style.RESET_ALL)
            print(Fore.YELLOW + f"\nFinal Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Health: {player['health']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Artifacts: {player['artifacts']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Relics: {player['relics']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Level: {player['level']}" + Style.RESET_ALL)
            now = datetime.now()
            print(Fore.YELLOW + f"\nDate: {now.strftime('%m/%d/%Y')}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Time: {now.strftime('%H:%M')}" + Style.RESET_ALL)
            with open("GameLog.txt", "a") as f:
                f.write(f"{now.strftime('%m/%d/%Y %H:%M')} - Win - Score: {player['score']}, Health: {player['health']}, Artifacts: {player['artifacts']}, Relics: {player['relics']}, Level: {player['level']}\n")
            print(Fore.YELLOW + "\nPress Enter to end..." + Style.RESET_ALL)
            input()
            break

if __name__ == "__main__":
    main()