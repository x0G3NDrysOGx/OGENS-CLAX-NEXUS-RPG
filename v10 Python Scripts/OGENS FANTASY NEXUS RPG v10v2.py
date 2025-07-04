from colorama import init, Fore, Style
init(autoreset=True, convert=True, strip=False, wrap=True)  # Robust initialization for Windows compatibility
import os
import secrets
import json
from datetime import datetime

# Define companion classes with unique effects
companion_classes = [
    "Barbarian", "Cleric", "Knight", "Mage", "Ranger", "Rogue", "Sorcerer", "Paladin",
    "Druid", "Necromancer", "Monk", "Bard", "Warlock", "Shaman", "Alchemist", "Beastmaster",
    "Assassin", "Wizard", "Hunter", "Priest", "Warlord", "Enchanter", "Inquisitor", "Runecaster"
]

# Define companion class modifiers
companion_class_modifiers = {
    "Barbarian": {"damage_boost": 5, "damage_reduction": 2},
    "Cleric": {"healing_boost": 10},
    "Knight": {"damage_reduction": 5},
    "Mage": {"magic_boost": 3},
    "Ranger": {"damage_boost": 3},
    "Rogue": {"score_boost": 5},
    "Sorcerer": {"healing_boost": 5, "damage_reduction": 2, "damage_boost": 2},
    "Paladin": {"healing_boost": 5, "damage_reduction": 3, "damage_boost": 3},
    "Druid": {"nature_boost": 5},
    "Necromancer": {"dark_boost": 5},
    "Monk": {"evasion_boost": 3},
    "Bard": {"social_boost": 5},
    "Warlock": {"curse_boost": 5},
    "Shaman": {"spirit_boost": 5},
    "Alchemist": {"potion_boost": 5},
    "Beastmaster": {"companion_boost": 5},
    "Assassin": {"critical_boost": 5},
    "Wizard": {"advanced_magic_boost": 5},
    "Hunter": {"tracking_boost": 5},
    "Priest": {"protective_boost": 5},
    "Warlord": {"leadership_boost": 5},
    "Enchanter": {"enchantment_boost": 5},
    "Inquisitor": {"detection_boost": 5},
    "Runecaster": {"rune_boost": 5}
}

# Initialize player stats
player = {
    "score": 0,
    "health": 100,
    "max_health": 200,
    "runes": 0,
    "healing_potion": 0,
    "magic_scroll": 0,
    "mystic_key": 0,
    "arcane_crystal": 0,
    "player_strength": secrets.randbelow(10) + 5,  # 5-15
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

# Initialize companion stats with random classes
companion_stats = {name: {
    "health": min(secrets.randbelow(50) + 50, 100),  # 50-100, capped at 100
    "strength": secrets.randbelow(10) + 5,  # 5-15
    "luck": secrets.randbelow(10) + 1,  # 1-10
    "class": secrets.choice(companion_classes)
} for name in companions}

# Track fallen companions
fallen_companions = []

# Current companion
current_companion = {
    "name": "",
    "health": 0,
    "strength": 0,
    "luck": 0,
    "class": ""
}

# Global variables
arcane_crystal_active = False
stat_changes = ""
last_ascii_used = None

# Track the last chosen path
last_path_chosen = None

from colorama import Fore, Style

def get_path_dial():
    """Generate a fantasy-themed ASCII rune circle with yellow structure and numbers, highlighting the last chosen path in green."""
    dial_lines = [
        "     ☽===☾     ",
        "   |  ✦ 1 ✦    ",
        "=+===+=====+=+=",
        "| 4 ✦     ✦ 2  ",
        "=+===+=====+=+=",
        "   |  ✦ 3 ✦    ",
        "     ☽===☾     "
    ]
    colored_dial = []
    for line in dial_lines:
        new_line = line
        # Replace path numbers with colored versions
        for i in range(1, 5):
            path_num = str(i)
            if path_num in line:
                try:
                    if last_path_chosen is not None and path_num == last_path_chosen:
                        new_line = new_line.replace(path_num, f"{Fore.GREEN}{path_num}{Style.RESET_ALL}")
                    else:
                        new_line = new_line.replace(path_num, f"{Fore.YELLOW}{path_num}{Style.RESET_ALL}")
                except:
                    # Fallback to plain text if color rendering fails
                    new_line = new_line.replace(path_num, path_num)
        # Apply yellow to the entire line (including non-number characters)
        try:
            colored_line = f"{Fore.YELLOW}{new_line}{Style.RESET_ALL}"
        except:
            # Fallback to plain text if color rendering fails
            colored_line = new_line
        colored_dial.append(colored_line)
    return "\n".join(colored_dial)

# List of available colorama colors (unchanged)
COLORS = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
]

# New forest-themed ascii_art_list with 8 unique, detailed pieces
ascii_art_list = [
    """
    ╔══════[🌲]══════╗
    ║ 🌿 * | * * | * ♣ ║
    ║ * * | *✨* | * * ║
    ║ ❧ * | * * | * 🌿 ║
    ║ * * | * * | * * ║
    ╚══════[🌲]══════╝
    """,
    """
    ╔══════[🌳]══════╗
    ║ ♣ * | * * | * ~ ║
    ║ * * | *★* | * * ║
    ║ 🌿 * | * * | * ❧ ║
    ║ * * | * * | * * ║
    ╚══════[🌳]══════╝
    """,
    """
    ╔═════[🌲🌲]═════╗
    ║ ~ * | * * | * 🌿 ║
    ║ * * | *♦* | * * ║
    ║ ❧ * | * * | * ♣ ║
    ║ * * | * * | * * ║
    ╚═════[🌲🌲]═════╝
    """,
    """
    ╔══════[🌴]══════╗
    ║ 🌿 * | * * | * ❧ ║
    ║ * * | *☽* | * * ║
    ║ ♣ * | * * | * ~ ║
    ║ * * | * * | * * ║
    ╚══════[🌴]══════╝
    """,
    """
    ╔═════[🌳🌲]═════╗
    ║ ❧ * | * * | * ♣ ║
    ║ * * | *✨* | * * ║
    ║ ~ * | * * | * 🌿 ║
    ║ * * | * * | * * ║
    ╚═════[🌳🌲]═════╝
    """,
    """
    ╔══════[🌲]══════╗
    ║ ♣ * | * * | * 🌿 ║
    ║ * * | *★* | * * ║
    ║ ❧ * | * * | * ~ ║
    ║ * * | * * | * * ║
    ╚══════[🌲]══════╝
    """,
    """
    ╔══════[🌴]══════╗
    ║ ~ * | * * | * ❧ ║
    ║ * * | *♦* | * * ║
    ║ 🌿 * | * * | * ♣ ║
    ║ * * | * * | * * ║
    ╚══════[🌴]══════╝
    """,
    """
    ╔═════[🌲🌳]═════╗
    ║ 🌿 * | * * | * ~ ║
    ║ * * | *☾* | * * ║
    ║ ♣ * | * * | * ❧ ║
    ║ * * | * * | * * ║
    ╚═════[🌲🌳]═════╝
    """
]

def get_random_ascii():
    global last_ascii_used
    available_indices = [i for i in range(len(ascii_art_list)) if i != last_ascii_used]
    if not available_indices:
        available_indices = list(range(len(ascii_art_list)))
    new_index = secrets.choice(available_indices)
    last_ascii_used = new_index
    ascii_art = ascii_art_list[new_index]
    # Apply a color from the COLORS list, cycling through using modulo
    color = COLORS[new_index % len(COLORS)]
    try:
        colored_ascii = f"{color}{ascii_art}{Style.RESET_ALL}"
    except:
        # Fallback to plain text if color rendering fails
        colored_ascii = ascii_art
    return colored_ascii

def log_event(event_message):
    if event_message not in ["Game won", "Game lost", "Game quit"]:
        return
    try:
        with open("GameLog.txt", "a") as f:
            timestamp = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
            player_stats = (
                f"Score={player['score']}, "
                f"Runes={player['runes']}, "
                f"Arcane Crystals={player['arcane_crystal']}, "
                f"Level={player['level']}, "
                f"Health={player['health']}/{player['max_health']}, "
                f"Strength={player['player_strength']}"
            )
            f.write(f"{timestamp} - {event_message} - {player_stats}\n")
    except Exception as e:
        print(Fore.MAGENTA + f"Failed to log event: {str(e)}" + Style.RESET_ALL)

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
        stat_changes = "Progress inscribed in the tomes"
        print(Fore.MAGENTA + "Your progress is inscribed in the ancient tomes!" + Style.RESET_ALL)
    except Exception as e:
        if os.path.exists("SaveGame.bak"):
            os.rename("SaveGame.bak", "SaveGame.txt")
            stat_changes = f"Failed to inscribe progress, restored from backup: {str(e)}"
            print(Fore.MAGENTA + f"Failed to inscribe progress, restored from backup... Error: {str(e)}" + Style.RESET_ALL)
        else:
            stat_changes = f"Failed to inscribe progress, no backup available: {str(e)}"
            print(Fore.MAGENTA + f"Failed to inscribe progress, no backup available... Error: {str(e)}" + Style.RESET_ALL)
    return stat_changes

def load_game():
    global player, companion_stats, current_companion, fallen_companions, stat_changes
    if not os.path.exists("SaveGame.txt"):
        stat_changes = "No tomes found"
        print(Fore.MAGENTA + "No ancient tomes found..." + Style.RESET_ALL)
        return
    try:
        with open("SaveGame.txt", "r") as f:
            game_state = json.load(f)
        
        default_player = {
            "score": 0, "health": 100, "max_health": 200, "runes": 0,
            "healing_potion": 0, "magic_scroll": 0, "mystic_key": 0, "arcane_crystal": 0,
            "player_strength": secrets.randbelow(10) + 5, "level": 1, "xp": 0, "xp_needed": 50
        }
        for key in default_player:
            if key in game_state.get("player", {}):
                player[key] = int(game_state["player"][key]) if key in [
                    "score", "health", "max_health", "runes", "healing_potion",
                    "magic_scroll", "mystic_key", "arcane_crystal", "player_strength", "level", "xp", "xp_needed"
                ] else game_state["player"][key]
            else:
                player[key] = default_player[key]
        
        companion_stats.clear()
        companion_stats.update({
            name: {"health": min(secrets.randbelow(50) + 50, 100), "strength": secrets.randbelow(10) + 5, 
                   "luck": secrets.randbelow(10) + 1, "class": secrets.choice(companion_classes)}
            for name in companions
        })
        for name, stats in game_state.get("companion_stats", {}).items():
            if name in companion_stats:
                companion_stats[name]["health"] = max(0, min(int(stats.get("health", companion_stats[name]["health"])), 100))
                companion_stats[name]["strength"] = int(stats.get("strength", companion_stats[name]["strength"]))
                companion_stats[name]["luck"] = int(stats.get("luck", companion_stats[name]["luck"]))
                companion_stats[name]["class"] = stats.get("class", companion_stats[name]["class"])
        
        current_companion_data = game_state.get("current_companion", {})
        current_companion["name"] = current_companion_data.get("name", "")
        if current_companion["name"] in companion_stats:
            current_companion["health"] = max(0, min(int(current_companion_data.get("health", companion_stats[current_companion["name"]]["health"])), 100))
            current_companion["strength"] = int(current_companion_data.get("strength", companion_stats[current_companion["name"]]["strength"]))
            current_companion["luck"] = int(current_companion_data.get("luck", companion_stats[current_companion["name"]]["luck"]))
            current_companion["class"] = current_companion_data.get("class", companion_stats[current_companion["name"]]["class"])
            companion_stats[current_companion["name"]]["health"] = current_companion["health"]
        else:
            new_companion_name = secrets.choice(companions)
            current_companion.update({
                "name": new_companion_name,
                "health": max(0, min(companion_stats[new_companion_name]["health"], 100)),
                "strength": companion_stats[new_companion_name]["strength"],
                "luck": companion_stats[new_companion_name]["luck"],
                "class": companion_stats[new_companion_name]["class"]
            })
            companion_stats[new_companion_name]["health"] = current_companion["health"]
        
        fallen_companions.clear()
        fallen_companions.extend(game_state.get("fallen_companions", []))
        
        stat_changes = "Progress restored from the tomes"
        print(Fore.MAGENTA + "The ancient tomes restore your progress!" + Style.RESET_ALL)
    except Exception as e:
        stat_changes = f"Failed to load tomes: {str(e)}"
        print(Fore.MAGENTA + f"Failed to load tomes... Error: {str(e)}" + Style.RESET_ALL)
    return stat_changes

def roll_dice():
    die1 = secrets.randbelow(5) + 1  # D5
    die2 = secrets.randbelow(10) + 1  # D10
    outcome = (die1 - 1) * 10 + die2
    luck_modifier = current_companion["luck"] - 5 if current_companion["name"] else 0
    adjusted_outcome = max(1, min(50, outcome + luck_modifier))
    return die1, die2, outcome, adjusted_outcome

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
        stat_changes = f"Level {player['level']} reached, Max Health +10, Health +5"
        return levelup_health_change
    elif player["level"] >= 1000:
        stat_changes = "Max Level 1000 reached, no further leveling"
    return 0

def is_positive_outcome(changes):
    return (changes.get("player_health", 0) >= 0 and
            changes.get("comp_health", 0) >= 0 and
            (changes.get("runes", 0) > 0 or
             changes.get("magic_scroll", 0) > 0 or
             changes.get("mystic_key", 0) > 0 or
             changes.get("arcane_crystal", 0) > 0 or
             changes.get("score", 0) > 0))

def path_outcomes(path, adjusted_outcome):
    global player, current_companion, stat_changes, arcane_crystal_active
    outcomes = {
        1: {  # Ancient Crypts
            1: ("You slip past skeletal sentinels, uncovering a glowing Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            2: ("A treacherous guide leads you into a wraith ambush", {"comp_health": -6, "xp": 1, "player_health": -6}),
            3: ("A cursed rune triggers a collapsing tomb", {"comp_health": -5, "xp": 1, "player_health": -5}),
            4: ("You evade undead patrols, finding a Healing Potion in a dusty alcove", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            5: ("Your stealth falters, disturbing a crypt’s restless spirits", {"score": 3 + player["level"], "xp": 5, "comp_health": -2, "player_health": -2}),
            6: ("You vanquish a horde of zombies, claiming an Arcane Crystal", {"score": 7 + player["level"], "runes": 1, "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            7: ("An ally succumbs to a dark curse in the crypt", {"comp_health": -6, "xp": 1, "player_health": -6}),
            8: ("A spiked trap catches you off guard", {"comp_health": -5, "xp": 1, "player_health": -5}),
            9: ("You clear a crypt chamber, securing a Sacred Rune", {"score": 4 + player["level"], "runes": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            10: ("A lich’s minions overwhelm you in a dark corridor", {"comp_health": -7, "xp": 1, "player_health": -7}),
            11: ("You convince a restless ghost to reveal a Mystic Key", {"score": 6 + player["level"], "mystic_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            12: ("A deceitful spirit curses you with weakness", {"comp_health": -6, "xp": 1, "player_health": -6}),
            13: ("You negotiate with a crypt guardian, earning a Magic Scroll", {"score": 5 + player["level"], "magic_scroll": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            14: ("Your words enrage a spectral warden", {"comp_health": -5, "xp": 1, "player_health": -5}),
            15: ("Angered spirits swarm you in the crypt’s depths", {"comp_health": -2, "xp": 1, "player_health": -2}),
            16: ("You dispel a necrotic ward, revealing a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            17: ("Your spell misfires, unleashing dark energies", {"comp_health": -6, "xp": 1, "player_health": -6}),
            18: ("A trapped rune explodes, wounding you", {"comp_health": -5, "xp": 1, "player_health": -5}),
            19: ("You harness a crypt’s magic, gaining a Healing Potion", {"score": 4 + player["level"], "healing_potion": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            20: ("A dark spell summons shadowy foes", {"comp_health": -7, "xp": 1, "player_health": -7}),
            21: ("You uncover a hidden vault, securing an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            22: ("You defeat a bone golem, claiming a Mystic Key", {"score": 5 + player["level"], "mystic_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            23: ("You appease a crypt spirit, earning a Magic Scroll", {"score": 5 + player["level"], "magic_scroll": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            24: ("You unlock a sealed crypt, finding a Sacred Rune", {"score": 6 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            25: ("A shadow trap snares you in the crypt", {"comp_health": -5, "xp": 1, "player_health": -5}),
            26: ("A possessed ally turns against you", {"comp_health": -6, "xp": 1, "player_health": -6}),
            27: ("You soothe a tormented soul, gaining a Healing Potion", {"score": 6 + player["level"], "healing_potion": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            28: ("A cursed ward saps your vitality", {"comp_health": -5, "xp": 1, "player_health": -5}),
            29: ("You bypass ancient traps, securing a Mystic Key", {"score": 5 + player["level"], "mystic_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            30: ("You slay a crypt wraith, claiming an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            31: ("A ghostly trickster leads you into danger", {"comp_health": -6, "xp": 1, "player_health": -6}),
            32: ("You channel crypt magic, uncovering a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            33: ("Your presence awakens a horde of skeletons", {"comp_health": -7, "xp": 1, "player_health": -7}),
            34: ("A crumbling crypt pins you under rubble", {"comp_health": -5, "xp": 1, "player_health": -5}),
            35: ("You earn a spirit’s trust, gaining a Magic Scroll", {"score": 5 + player["level"], "magic_scroll": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            36: ("Your spell attracts a malevolent force", {"comp_health": -6, "xp": 1, "player_health": -6}),
            37: ("You find a secret rune chamber in the crypt", {"score": 6 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            38: ("You defeat a skeletal beast, gaining a Healing Potion", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            39: ("Your words trigger a vengeful curse", {"comp_health": -5, "xp": 1, "player_health": -5}),
            40: ("You dispel a dark crypt aura, claiming an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            41: ("A hidden trap exposes you to wraiths", {"comp_health": -6, "xp": 1, "player_health": -6}),
            42: ("A swarm of undead engulfs you", {"comp_health": -7, "xp": 1, "player_health": -7}),
            43: ("You barter with a crypt keeper, earning a Mystic Key", {"score": 5 + player["level"], "mystic_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            44: ("A rune’s backlash scorches you", {"comp_health": -5, "xp": 1, "player_health": -5}),
            45: ("You glide through shadows, finding a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            46: ("You fell a dark knight, securing a Mystic Key", {"score": 6 + player["level"], "mystic_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            47: ("A spirit’s wrath curses your soul", {"comp_health": -6, "xp": 1, "player_health": -6}),
            48: ("You unlock a crypt’s ancient seal, gaining a Healing Potion", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            49: ("A magical snare binds you in the crypt", {"comp_health": -5, "xp": 1, "player_health": -5}),
            50: ("You defeat a lich king, claiming an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4})
        },
        2: {  # Enchanted Forest
            1: ("You sneak past glowing sprites, discovering a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            2: ("A sly dryad lures you into a trap", {"comp_health": -6, "xp": 1, "player_health": -6}),
            3: ("Enchanted vines entangle you in the undergrowth", {"comp_health": -5, "xp": 1, "player_health": -5}),
            4: ("You avoid a wolf pack, finding a Healing Potion by a stream", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            5: ("Your footsteps disrupt a sacred grove", {"score": 3 + player["level"], "xp": 5, "comp_health": -2, "player_health": -2}),
            6: ("You slay a forest troll, seizing an Arcane Crystal", {"score": 7 + player["level"], "runes": 1, "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            7: ("Your ally flees, spooked by forest spirits", {"comp_health": -6, "xp": 1, "player_health": -6}),
            8: ("A hidden pit swallows you in the forest", {"comp_health": -5, "xp": 1, "player_health": -5}),
            9: ("You rout a bandit camp, claiming a Sacred Rune", {"score": 4 + player["level"], "runes": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            10: ("A beast pack ambushes you in the woods", {"comp_health": -7, "xp": 1, "player_health": -7}),
            11: ("You befriend a forest druid, earning a Mystic Key", {"score": 6 + player["level"], "mystic_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            12: ("A cunning fairy tricks you into a trap", {"comp_health": -6, "xp": 1, "player_health": -6}),
            13: ("You trade with elven scouts, gaining a Magic Scroll", {"score": 5 + player["level"], "magic_scroll": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            14: ("Your words provoke a wrathful treant", {"comp_health": -5, "xp": 1, "player_health": -5}),
            15: ("A fairy swarm attacks you in the glade", {"comp_health": -2, "xp": 1, "player_health": -2}),
            16: ("You dispel a forest enchantment, finding a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            17: ("Your spell angers woodland spirits", {"comp_health": -6, "xp": 1, "player_health": -6}),
            18: ("A cursed vine saps your strength", {"comp_health": -5, "xp": 1, "player_health": -5}),
            19: ("You tap into forest magic, gaining a Healing Potion", {"score": 4 + player["level"], "healing_potion": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            20: ("A rogue spell awakens feral beasts", {"comp_health": -7, "xp": 1, "player_health": -7}),
            21: ("You discover a hidden glade, securing an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            22: ("You defeat a dire wolf, claiming a Mystic Key", {"score": 5 + player["level"], "mystic_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            23: ("You earn a fairy’s favor, gaining a Magic Scroll", {"score": 5 + player["level"], "magic_scroll": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            24: ("You unlock a mystic tree, finding a Sacred Rune", {"score": 6 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            25: ("A magical snare traps you in the forest", {"comp_health": -5, "xp": 1, "player_health": -5}),
            26: ("A charmed ally betrays you in the woods", {"comp_health": -6, "xp": 1, "player_health": -6}),
            27: ("You pacify a forest spirit, gaining a Healing Potion", {"score": 6 + player["level"], "healing_potion": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            28: ("A cursed root drains your life force", {"comp_health": -5, "xp": 1, "player_health": -5}),
            29: ("You evade forest traps, securing a Mystic Key", {"score": 5 + player["level"], "mystic_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            30: ("You vanquish a forest wyrm, claiming an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            31: ("A deceitful druid leads you astray", {"comp_health": -6, "xp": 1, "player_health": -6}),
            32: ("You harness woodland magic, uncovering a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            33: ("Your noise draws a pack of wild beasts", {"comp_health": -7, "xp": 1, "player_health": -7}),
            34: ("A hidden trap springs underfoot", {"comp_health": -5, "xp": 1, "player_health": -5}),
            35: ("You win an elf’s trust, gaining a Magic Scroll", {"score": 5 + player["level"], "magic_scroll": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            36: ("Your spell provokes dark forest entities", {"comp_health": -6, "xp": 1, "player_health": -6}),
            37: ("You find a sacred rune grove in the forest", {"score": 6 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            38: ("You slay a forest beast, gaining a Healing Potion", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            39: ("Your words incite a spirit’s wrath", {"comp_health": -5, "xp": 1, "player_health": -5}),
            40: ("You dispel a forest ward, claiming an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            41: ("A trap reveals you to forest predators", {"comp_health": -6, "xp": 1, "player_health": -6}),
            42: ("A horde of feral creatures attacks", {"comp_health": -7, "xp": 1, "player_health": -7}),
            43: ("You negotiate with a forest guardian, earning a Mystic Key", {"score": 5 + player["level"], "mystic_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            44: ("A cursed vine lashes out at you", {"comp_health": -5, "xp": 1, "player_health": -5}),
            45: ("You slip through the underbrush, finding a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            46: ("You defeat a treant warrior, securing a Mystic Key", {"score": 6 + player["level"], "mystic_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            47: ("A forest spirit curses you with malaise", {"comp_health": -6, "xp": 1, "player_health": -6}),
            48: ("You unlock a mystic grove, gaining a Healing Potion", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            49: ("A magical net ensnares you in the woods", {"comp_health": -5, "xp": 1, "player_health": -5}),
            50: ("You defeat a forest guardian, claiming an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4})
        },
        3: {  # Mystic Ruins
            1: ("You bypass stone sentinels, uncovering a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            2: ("A hidden trap springs, alerting ruin guardians", {"comp_health": -6, "xp": 1, "player_health": -6}),
            3: ("An ancient rune collapses a chamber", {"comp_health": -5, "xp": 1, "player_health": -5}),
            4: ("You evade ruin patrols, finding a Healing Potion", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            5: ("Your steps disturb sacred ruins", {"score": 3 + player["level"], "xp": 5, "comp_health": -2, "player_health": -2}),
            6: ("You shatter a stone golem, claiming an Arcane Crystal", {"score": 7 + player["level"], "runes": 1, "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            7: ("Your ally is swayed by ruin curses", {"comp_health": -6, "xp": 1, "player_health": -6}),
            8: ("A falling pillar traps you in the ruins", {"comp_health": -5, "xp": 1, "player_health": -5}),
            9: ("You clear a ruin chamber, securing a Sacred Rune", {"score": 4 + player["level"], "runes": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            10: ("A golem horde overwhelms you", {"comp_health": -7, "xp": 1, "player_health": -7}),
            11: ("You persuade a ruin sage, earning a Mystic Key", {"score": 6 + player["level"], "mystic_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            12: ("A sage’s curse weakens you", {"comp_health": -6, "xp": 1, "player_health": -6}),
            13: ("You appease a ruin guardian, gaining a Magic Scroll", {"score": 5 + player["level"], "magic_scroll": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            14: ("Your words anger a ruin spirit", {"comp_health": -5, "xp": 1, "player_health": -5}),
            15: ("Guardians swarm the ruins, attacking you", {"comp_health": -2, "xp": 1, "player_health": -2}),
            16: ("You dispel a ruin ward, revealing a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            17: ("Your spell backfires, summoning ruin foes", {"comp_health": -6, "xp": 1, "player_health": -6}),
            18: ("An exploding rune wounds you", {"comp_health": -5, "xp": 1, "player_health": -5}),
            19: ("You harness ruin magic, gaining a Healing Potion", {"score": 4 + player["level"], "healing_potion": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            20: ("A dark spell awakens ruin guardians", {"comp_health": -7, "xp": 1, "player_health": -7}),
            21: ("You find a hidden ruin vault, securing an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            22: ("You defeat a stone guardian, claiming a Mystic Key", {"score": 5 + player["level"], "mystic_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            23: ("You earn a sage’s blessing, gaining a Magic Scroll", {"score": 5 + player["level"], "magic_scroll": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            24: ("You unlock a sealed ruin, finding a Sacred Rune", {"score": 6 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            25: ("A magical trap ensnares you in the ruins", {"comp_health": -5, "xp": 1, "player_health": -5}),
            26: ("A possessed ally attacks you", {"comp_health": -6, "xp": 1, "player_health": -6}),
            27: ("You calm a ruin spirit, gaining a Healing Potion", {"score": 6 + player["level"], "healing_potion": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            28: ("A cursed ward drains your strength", {"comp_health": -5, "xp": 1, "player_health": -5}),
            29: ("You bypass ruin traps, securing a Mystic Key", {"score": 5 + player["level"], "mystic_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            30: ("You vanquish a ruin golem, claiming an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            31: ("A deceitful sage leads you into peril", {"comp_health": -6, "xp": 1, "player_health": -6}),
            32: ("You channel ruin magic, uncovering a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            33: ("Your presence stirs a guardian horde", {"comp_health": -7, "xp": 1, "player_health": -7}),
            34: ("A collapsing ruin traps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
            35: ("You gain a guardian’s favor, earning a Magic Scroll", {"score": 5 + player["level"], "magic_scroll": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            36: ("Your spell draws dark ruin forces", {"comp_health": -6, "xp": 1, "player_health": -6}),
            37: ("You discover a hidden rune chamber in the ruins", {"score": 6 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            38: ("You slay a ruin beast, gaining a Healing Potion", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            39: ("Your words trigger a ruin curse", {"comp_health": -5, "xp": 1, "player_health": -5}),
            40: ("You dispel a ruin’s dark aura, claiming an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            41: ("A trap exposes you to ruin sentinels", {"comp_health": -6, "xp": 1, "player_health": -6}),
            42: ("A swarm of stone guardians attacks", {"comp_health": -7, "xp": 1, "player_health": -7}),
            43: ("You barter with a ruin keeper, earning a Mystic Key", {"score": 5 + player["level"], "mystic_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            44: ("A rune’s backlash injures you", {"comp_health": -5, "xp": 1, "player_health": -5}),
            45: ("You slip through ruin shadows, finding a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            46: ("You defeat a dark sentinel, securing a Mystic Key", {"score": 6 + player["level"], "mystic_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            47: ("A ruin spirit’s curse saps your vitality", {"comp_health": -6, "xp": 1, "player_health": -6}),
            48: ("You unlock a ruin’s ancient seal, gaining a Healing Potion", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            49: ("A magical snare binds you in the ruins", {"comp_health": -5, "xp": 1, "player_health": -5}),
            50: ("You defeat a ruin lord, claiming an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4})
        },
        4: {  # Shadow Realm
            1: ("You evade shadow wraiths, finding a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            2: ("A shadow betrays you to dark entities", {"comp_health": -6, "xp": 1, "player_health": -6}),
            3: ("A dark rune triggers a spectral trap", {"comp_health": -5, "xp": 1, "player_health": -5}),
            4: ("You slip past demons, finding a Healing Potion", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            5: ("Your presence disturbs a shadow portal", {"score": 3 + player["level"], "xp": 5, "comp_health": -2, "player_health": -2}),
            6: ("You slay a shadow demon, claiming an Arcane Crystal", {"score": 7 + player["level"], "runes": 1, "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            7: ("Your ally is corrupted by shadow magic", {"comp_health": -6, "xp": 1, "player_health": -6}),
            8: ("A shadow trap engulfs you", {"comp_health": -5, "xp": 1, "player_health": -5}),
            9: ("You clear a dark shrine, securing a Sacred Rune", {"score": 4 + player["level"], "runes": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            10: ("A demon horde swarms you", {"comp_health": -7, "xp": 1, "player_health": -7}),
            11: ("You persuade a shadow spirit, earning a Mystic Key", {"score": 6 + player["level"], "mystic_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            12: ("A dark spirit curses you", {"comp_health": -6, "xp": 1, "player_health": -6}),
            13: ("You appease a shadow entity, gaining a Magic Scroll", {"score": 5 + player["level"], "magic_scroll": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            14: ("Your words enrage a shadow demon", {"comp_health": -5, "xp": 1, "player_health": -5}),
            15: ("Shadows swarm you in the realm", {"comp_health": -2, "xp": 1, "player_health": -2}),
            16: ("You dispel a shadow ward, revealing a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            17: ("Your spell backfires, summoning dark foes", {"comp_health": -6, "xp": 1, "player_health": -6}),
            18: ("A dark rune explodes, injuring you", {"comp_health": -5, "xp": 1, "player_health": -5}),
            19: ("You harness shadow magic, gaining a Healing Potion", {"score": 4 + player["level"], "healing_potion": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            20: ("A rogue spell awakens shadow beasts", {"comp_health": -7, "xp": 1, "player_health": -7}),
            21: ("You find a hidden shadow shrine, securing an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            22: ("You defeat a shadow beast, claiming a Mystic Key", {"score": 5 + player["level"], "mystic_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            23: ("You earn a shadow’s blessing, gaining a Magic Scroll", {"score": 5 + player["level"], "magic_scroll": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            24: ("You unlock a dark rune, finding a Sacred Rune", {"score": 6 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            25: ("A shadow snare traps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
            26: ("A possessed ally betrays you", {"comp_health": -6, "xp": 1, "player_health": -6}),
            27: ("You calm a shadow spirit, gaining a Healing Potion", {"score": 6 + player["level"], "healing_potion": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            28: ("A dark ward drains your life", {"comp_health": -5, "xp": 1, "player_health": -5}),
            29: ("You bypass shadow traps, securing a Mystic Key", {"score": 5 + player["level"], "mystic_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            30: ("You vanquish a shadow demon, claiming an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            31: ("A shadow trickster leads you into danger", {"comp_health": -6, "xp": 1, "player_health": -6}),
            32: ("You channel shadow magic, uncovering a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            33: ("Your presence awakens shadow horrors", {"comp_health": -7, "xp": 1, "player_health": -7}),
            34: ("A dark trap springs in the realm", {"comp_health": -5, "xp": 1, "player_health": -5}),
            35: ("You gain a demon’s favor, earning a Magic Scroll", {"score": 5 + player["level"], "magic_scroll": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            36: ("Your spell draws shadow forces", {"comp_health": -6, "xp": 1, "player_health": -6}),
            37: ("You find a hidden rune shrine in the shadows", {"score": 6 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            38: ("You slay a shadow beast, gaining a Healing Potion", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            39: ("Your words trigger a shadow curse", {"comp_health": -5, "xp": 1, "player_health": -5}),
            40: ("You dispel a shadow aura, claiming an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            41: ("A trap reveals you to shadow wraiths", {"comp_health": -6, "xp": 1, "player_health": -6}),
            42: ("A horde of shadow demons attacks", {"comp_health": -7, "xp": 1, "player_health": -7}),
            43: ("You barter with a shadow keeper, earning a Mystic Key", {"score": 5 + player["level"], "mystic_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            44: ("A dark rune’s backlash wounds you", {"comp_health": -5, "xp": 1, "player_health": -5}),
            45: ("You glide through shadows, finding a Sacred Rune", {"score": 8 + player["level"], "runes": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            46: ("You defeat a dark knight, securing a Mystic Key", {"score": 6 + player["level"], "mystic_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            47: ("A shadow spirit curses your soul", {"comp_health": -6, "xp": 1, "player_health": -6}),
            48: ("You unlock a shadow seal, gaining a Healing Potion", {"score": 5 + player["level"], "healing_potion": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            49: ("A magical shadow snare binds you", {"comp_health": -5, "xp": 1, "player_health": -5}),
            50: ("You defeat a shadow lord, claiming an Arcane Crystal", {"score": 7 + player["level"], "arcane_crystal": 1, "xp": 10, "player_health": 4, "comp_health": 4})
        }
    }

    result, changes = outcomes.get(path, {}).get(adjusted_outcome, ("No outcome defined", {}))
    was_fallen = current_companion["name"] in fallen_companions

    # Apply player strength scaling for negative health changes
    strength_modifier = 2.75 - (player["player_strength"] / 7.5)  # Maps strength 5 -> ~2.0833, 15 -> 0.75
    if "player_health" in changes and changes["player_health"] < 0:
        scaled_damage = round(changes["player_health"] * strength_modifier)
        # Ensure minimum damage of -2 at strength 15 for small damages
        changes["player_health"] = max(scaled_damage, -2) if player["player_strength"] >= 15 else scaled_damage
    if "comp_health" in changes and changes["comp_health"] < 0:
        scaled_damage = round(changes["comp_health"] * strength_modifier)
        changes["comp_health"] = max(scaled_damage, -2) if player["player_strength"] >= 15 else scaled_damage

    # Apply companion class modifiers
    if current_companion["name"]:
        companion_class = current_companion["class"]
        class_mod = companion_class_modifiers.get(companion_class, {})
        if "player_health" in changes and changes["player_health"] < 0:
            changes["player_health"] = max(changes["player_health"] + min(class_mod.get("damage_reduction", 0), 2), -15)
        if "comp_health" in changes and changes["comp_health"] < 0:
            changes["comp_health"] = max(changes["comp_health"] + min(class_mod.get("damage_reduction", 0), 2), -15)
        if "player_health" in changes and changes["player_health"] > 0:
            changes["player_health"] += class_mod.get("healing_boost", 0)
            changes["comp_health"] = changes.get("comp_health", 0) + class_mod.get("healing_boost", 0)
        if "score" in changes and changes["score"] > 0:
            changes["score"] += class_mod.get("score_boost", 0)
        if "runes" in changes and changes["runes"] > 0:
            changes["runes"] += class_mod.get("magic_boost", 0) + class_mod.get("advanced_magic_boost", 0)
        if "healing_potion" in changes and changes["healing_potion"] > 0:
            changes["healing_potion"] += class_mod.get("potion_boost", 0)
        if "magic_scroll" in changes and changes["magic_scroll"] > 0:
            changes["magic_scroll"] += class_mod.get("enchantment_boost", 0)
        if "mystic_key" in changes and changes["mystic_key"] > 0:
            changes["mystic_key"] += class_mod.get("rune_boost", 0)
        if "arcane_crystal" in changes and changes["arcane_crystal"] > 0:
            changes["arcane_crystal"] += class_mod.get("dark_boost", 0) + class_mod.get("curse_boost", 0)

    # Ensure health changes are capped
    changes["player_health"] = max(changes.get("player_health", 0), -100)
    changes["comp_health"] = max(changes.get("comp_health", 0), -100)

    # Cap companion health at 0-100 after applying changes
    if current_companion["name"]:
        current_companion["health"] = max(0, min(current_companion["health"] + changes.get("comp_health", 0), 100))
        companion_stats[current_companion["name"]]["health"] = current_companion["health"]
    else:
        changes["comp_health"] = 0  # No companion health change if no companion

    # Handle fallen companion revival on positive outcomes
    if was_fallen and is_positive_outcome(changes):
        changes["comp_health"] += 10  # +10 revival bonus plus +4 from outcome
        current_companion["health"] = max(0, min(current_companion["health"] + 10, 100))  # Cap at 0-100
        companion_stats[current_companion["name"]]["health"] = current_companion["health"]
        if current_companion["name"] in fallen_companions:
            fallen_companions.remove(current_companion["name"])
    
    return result, changes

def inventory():
    global player, current_companion, stat_changes, arcane_crystal_active
    while True:
        os.system("cls")
        print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.MAGENTA + "OGENS FANTASY NEXUS - D5+D10" + Style.RESET_ALL)
        print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.MAGENTA + get_random_ascii() + Style.RESET_ALL)
        print(Fore.MAGENTA + "\nTREASURE VAULT..." + Style.RESET_ALL)
        print(Fore.RED + f"Healing Potion ({player['healing_potion']}): Restores vitality..." + Style.RESET_ALL)
        print(Fore.YELLOW + f"Magic Scroll ({player['magic_scroll']}): Boosts renown..." + Style.RESET_ALL)
        print(Fore.CYAN + f"Mystic Key ({player['mystic_key']}): Unlocks sacred runes..." + Style.RESET_ALL)
        print(Fore.BLUE + f"Arcane Crystal ({player['arcane_crystal']}): Doubles score gains for the next event..." + Style.RESET_ALL)
        print(Fore.MAGENTA + "\nUSE AN ITEM..." + Style.RESET_ALL)
        print(Fore.MAGENTA + "1. Healing Potion (+25 player health, +20 companion health)" + Style.RESET_ALL)
        print(Fore.MAGENTA + "2. Magic Scroll (+20 score)" + Style.RESET_ALL)
        print(Fore.MAGENTA + "3. Mystic Key (+4 runes)" + Style.RESET_ALL)
        print(Fore.MAGENTA + "4. Arcane Crystal (Double score next event)" + Style.RESET_ALL)
        print(Fore.MAGENTA + "5. Return" + Style.RESET_ALL)
        inv_choice = input(Fore.MAGENTA + "\nSelect an item (1-5): " + Style.RESET_ALL).strip()
        if inv_choice not in ["1", "2", "3", "4", "5"]:
            stat_changes = "Invalid choice"
            print(Fore.MAGENTA + "\nINVALID CHOICE..." + Style.RESET_ALL)
            print(Fore.MAGENTA + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nPress Enter to try again..." + Style.RESET_ALL)
            input()
            continue
        if inv_choice == "1":
            if player["healing_potion"] > 0:
                pre_player_health = player["health"]
                pre_comp_health = current_companion["health"] if current_companion["name"] else 0
                healing_boost = companion_class_modifiers.get(current_companion["class"], {}).get("healing_boost", 0)
                player["health"] = min(player["health"] + 25 + healing_boost, player["max_health"])
                if current_companion["name"]:
                    current_companion["health"] = max(0, min(current_companion["health"] + 20 + healing_boost, 100))
                    companion_stats[current_companion["name"]]["health"] = current_companion["health"]
                    if current_companion["health"] > 0 and current_companion["name"] in fallen_companions:
                        fallen_companions.remove(current_companion["name"])
                player["healing_potion"] -= 1
                if player["healing_potion"] < 0:
                    player["healing_potion"] = 0
                stat_changes = f"Health +{25 + healing_boost}, Companion Health +{20 + healing_boost}, Healing Potions -1"
                stat_changes += f", Total: Player [{pre_player_health} -> {player['health']}]"
                if current_companion["name"]:
                    stat_changes += f", Companion [{pre_comp_health} -> {current_companion['health']}]"
                print(Fore.MAGENTA + "\nHealing Potion used - Vitality restored..." + Style.RESET_ALL)
            else:
                stat_changes = "No Healing Potions remain"
                print(Fore.MAGENTA + "\nNo Healing Potions remain..." + Style.RESET_ALL)
        elif inv_choice == "2":
            if player["magic_scroll"] > 0:
                score_boost = companion_class_modifiers.get(current_companion["class"], {}).get("score_boost", 0)
                player["score"] += 20 + score_boost
                player["magic_scroll"] -= 1
                stat_changes = f"Score +{20 + score_boost}, Magic Scrolls -1"
                print(Fore.MAGENTA + "\nMagic Scroll used - Renown gained..." + Style.RESET_ALL)
            else:
                stat_changes = "No Magic Scrolls remain"
                print(Fore.MAGENTA + "\nNo Magic Scrolls remain..." + Style.RESET_ALL)
        elif inv_choice == "3":
            if player["mystic_key"] > 0:
                rune_boost = companion_class_modifiers.get(current_companion["class"], {}).get("rune_boost", 0)
                player["runes"] += 4 + rune_boost
                player["mystic_key"] -= 1
                stat_changes = f"Runes +{4 + rune_boost}, Mystic Keys -1"
                print(Fore.MAGENTA + "\nMystic Key used - Sacred runes unlocked..." + Style.RESET_ALL)
            else:
                stat_changes = "No Mystic Keys remain"
                print(Fore.MAGENTA + "\nNo Mystic Keys remain..." + Style.RESET_ALL)
        elif inv_choice == "4":
            if player["arcane_crystal"] > 0:
                player["arcane_crystal"] -= 1
                arcane_crystal_active = True
                stat_changes = "Arcane Crystal used - Score doubled for next event, Arcane Crystals -1"
                print(Fore.MAGENTA + "\nArcane Crystal used - Next event's score gains will be doubled..." + Style.RESET_ALL)
            else:
                stat_changes = "No Arcane Crystals remain"
                print(Fore.MAGENTA + "\nNo Arcane Crystals remain..." + Style.RESET_ALL)
        elif inv_choice == "5":
            return
        print(Fore.MAGENTA + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
        print(Fore.MAGENTA + "\nPress Enter to return..." + Style.RESET_ALL)
        input()

def companions_menu():
    global stat_changes
    os.system("cls")
    print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
    print(Fore.MAGENTA + "OGENS FANTASY NEXUS - D5+D10" + Style.RESET_ALL)
    print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
    print(Fore.MAGENTA + get_random_ascii() + Style.RESET_ALL)
    print(Fore.MAGENTA + "\nCOMPANIONS LIST..." + Style.RESET_ALL)
    for name in companions:
        status = "(Fallen)" if name in fallen_companions else ""
        print(Fore.MAGENTA + f"{name} {status} - Class: {Fore.MAGENTA}{companion_stats[name]['class']}{Style.RESET_ALL}, Health: {Fore.RED}{companion_stats[name]['health']}{Style.RESET_ALL}, Strength: {Fore.WHITE}{companion_stats[name]['strength']}{Style.RESET_ALL}, Luck: {Fore.YELLOW}{companion_stats[name]['luck']}{Style.RESET_ALL}" + Style.RESET_ALL)
    print(Fore.MAGENTA + f"\nCurrent Companion: {current_companion['name']} ({current_companion['class']})" + Style.RESET_ALL)
    print(Fore.MAGENTA + "\nPress Enter to return..." + Style.RESET_ALL)
    stat_changes = "Viewed companions list"
    input()

def main():
    global player, current_companion, stat_changes, arcane_crystal_active, fallen_companions, last_path_chosen
    # Reset global states to ensure fresh game
    player.update({
        "score": 0,
        "health": 100,
        "max_health": 200,
        "runes": 0,
        "healing_potion": 0,
        "magic_scroll": 0,
        "mystic_key": 0,
        "arcane_crystal": 0,
        "player_strength": secrets.randbelow(10) + 5,
        "level": 1,
        "xp": 0,
        "xp_needed": 50
    })
    current_companion.update({
        "name": "",
        "health": 0,
        "strength": 0,
        "luck": 0,
        "class": ""
    })
    fallen_companions.clear()
    arcane_crystal_active = False
    stat_changes = ""
    last_path_chosen = None  # Reset last chosen path
    
    # Initialize companion stats afresh
    companion_stats.clear()
    companion_stats.update({
        name: {
            "health": max(0, min(secrets.randbelow(50) + 50, 100)),
            "strength": secrets.randbelow(10) + 5,
            "luck": secrets.randbelow(10) + 1,
            "class": secrets.choice(companion_classes)
        } for name in companions
    })

    # Select random companion at start
    companion_name = secrets.choice(companions)
    current_companion.update({
        "name": companion_name,
        "health": max(0, min(companion_stats[companion_name]["health"], 100)),
        "strength": companion_stats[companion_name]["strength"],
        "luck": companion_stats[companion_name]["luck"],
        "class": companion_stats[companion_name]["class"]
    })
    companion_stats[companion_name]["health"] = current_companion["health"]

    os.system("cls")
    print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
    print(Fore.MAGENTA + "OGENS FANTASY NEXUS - D5+D10" + Style.RESET_ALL)
    print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
    print(Fore.MAGENTA + get_random_ascii() + Style.RESET_ALL)
    print(Fore.MAGENTA + "OGENS FANTASY NEXUS" + Style.RESET_ALL)
    print(Fore.MAGENTA + "CONQUER THE MYSTIC REALM" + Style.RESET_ALL)
    print(Fore.MAGENTA + f"\nCompanion: {Fore.MAGENTA}{current_companion['name']} ({current_companion['class']}) joins you in the realm..." + Style.RESET_ALL)
    print(Fore.MAGENTA + "\n\n        Press Enter to embark" + Style.RESET_ALL)
    print(Fore.MAGENTA + "    Fantasy Nexus Realm..." + Style.RESET_ALL)
    input()

    while True:
        os.system("cls")
        # Initialize display variables only when needed
        show_health_change = False
        pre_player_health = player["health"]
        pre_comp_health = current_companion["health"] if current_companion["name"] else 0

        print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.MAGENTA + "OGENS FANTASY NEXUS - D5+D10" + Style.RESET_ALL)
        print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.MAGENTA + get_random_ascii() + Style.RESET_ALL)
        print(Fore.MAGENTA + "\nNAVIGATING THE MYSTIC REALM..." + Style.RESET_ALL)
        print(Fore.WHITE + f"Strength: {player['player_strength']}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Level: {player['level']} (XP: {player['xp']}/{player['xp_needed']})" + Style.RESET_ALL)
        print(Fore.RED + f"Health: {player['health']}" + Style.RESET_ALL + Fore.YELLOW + f"  Score: {player['score']}" + Style.RESET_ALL + Fore.CYAN + f"  Runes: {player['runes']}" + Style.RESET_ALL + Fore.BLUE + f"  Arcane Crystals: {player['arcane_crystal']}" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"Progress: Score {player['score']}/6000 Runes {player['runes']}/300 Arcane Crystals {player['arcane_crystal']}/50" + Style.RESET_ALL)
        if current_companion["name"]:
            print(Fore.MAGENTA + f"\nCompanion: {Fore.MAGENTA}{current_companion['name']} ({current_companion['class']}{Style.RESET_ALL}) (Health: {Fore.RED}{current_companion['health']}{Style.RESET_ALL}, Strength: {Fore.WHITE}{current_companion['strength']}{Style.RESET_ALL}, Luck: {Fore.YELLOW}{current_companion['luck']}{Style.RESET_ALL})" + Style.RESET_ALL)
        if stat_changes:
            print(Fore.MAGENTA + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
        # Display the fantasy-themed dial under Changes
        print(Fore.MAGENTA + "\nPath Chosen:" + Style.RESET_ALL)
        print(get_path_dial())

        # Check win condition
        if player["score"] >= 6000 and player["runes"] >= 300 and player["arcane_crystal"] >= 50:
            os.system("cls")
            print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.MAGENTA + "OGENS FANTASY NEXUS - VICTORY" + Style.RESET_ALL)
            print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.MAGENTA + get_random_ascii() + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nVICTORY! YOU HAVE CONQUERED THE MYSTIC REALM!" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Final Runes: {player['runes']}" + Style.RESET_ALL)
            print(Fore.BLUE + f"Final Arcane Crystals: {player['arcane_crystal']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Level: {player['level']}" + Style.RESET_ALL)
            print(Fore.RED + f"Final Health: {player['health']}/{player['max_health']}" + Style.RESET_ALL)
            print(Fore.WHITE + f"Final Strength: {player['player_strength']}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nYour legend will echo through the ages..." + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nPress Enter to exit..." + Style.RESET_ALL)
            log_event("Game won")
            input()
            break

        # Check loss condition
        if player["health"] <= 0:
            os.system("cls")
            print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.MAGENTA + "OGENS FANTASY NEXUS - DEFEAT" + Style.RESET_ALL)
            print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.MAGENTA + get_random_ascii() + Style.RESET_ALL)
            print(Fore.RED + "\nDEFEAT! The Mystic Realm has claimed you..." + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Final Runes: {player['runes']}" + Style.RESET_ALL)
            print(Fore.BLUE + f"Final Arcane Crystals: {player['arcane_crystal']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Level: {player['level']}" + Style.RESET_ALL)
            print(Fore.RED + f"Final Health: {player['health']}/{player['max_health']}" + Style.RESET_ALL)
            print(Fore.WHITE + f"Final Strength: {player['player_strength']}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nYour journey ends here..." + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nPress Enter to exit..." + Style.RESET_ALL)
            log_event("Game lost")
            input()
            break

        print(Fore.MAGENTA + "\nCHOOSE YOUR PATH..." + Style.RESET_ALL)
        print(Fore.MAGENTA + "1. Ancient Crypts" + Style.RESET_ALL)
        print(Fore.MAGENTA + "2. Enchanted Forest" + Style.RESET_ALL)
        print(Fore.MAGENTA + "3. Mystic Ruins" + Style.RESET_ALL)
        print(Fore.MAGENTA + "4. Shadow Realm" + Style.RESET_ALL)
        print(Fore.MAGENTA + "5. Inventory" + Style.RESET_ALL)
        print(Fore.MAGENTA + "6. Companions" + Style.RESET_ALL)
        print(Fore.MAGENTA + "7. Save Game" + Style.RESET_ALL)
        print(Fore.MAGENTA + "8. Load Game" + Style.RESET_ALL)
        print(Fore.MAGENTA + "9. Exit" + Style.RESET_ALL)
        choice = input(Fore.MAGENTA + "\nSelect a path (1-9): " + Style.RESET_ALL).strip()

        if choice in ["1", "2", "3", "4"]:
            # Update last chosen path
            last_path_chosen = choice
            # Select random companion (including fallen) for path event
            companion_name = secrets.choice(companions)
            current_companion.update({
                "name": companion_name,
                "health": max(0, min(companion_stats[companion_name]["health"], 100)),
                "strength": companion_stats[companion_name]["strength"],
                "luck": companion_stats[companion_name]["luck"],
                "class": companion_stats[companion_name]["class"]
            })
            companion_stats[companion_name]["health"] = current_companion["health"]
            pre_player_health = player["health"]
            pre_comp_health = current_companion["health"] if current_companion["name"] else 0

            die1, die2, outcome, adjusted_outcome = roll_dice()
            result, changes = path_outcomes(int(choice), adjusted_outcome)
            was_fallen = current_companion["name"] in fallen_companions
            print(Fore.MAGENTA + f"\n{current_companion['name']} ({current_companion['class']}{Style.RESET_ALL}) {'(Fallen) ' if was_fallen else ''}joins you for this quest..." + Style.RESET_ALL)
            print(Fore.MAGENTA + f"\nDice Roll: D5={die1}, D10={die2}, Outcome={outcome}, Adjusted={adjusted_outcome}" + Style.RESET_ALL)
            print(Fore.MAGENTA + f"\nResult: {result}" + Style.RESET_ALL)

            # Apply arcane crystal effect
            arcane_crystal_message = ""
            if arcane_crystal_active and "score" in changes and changes["score"] > 0:
                changes["score"] *= 2
                arcane_crystal_message = "Score doubled by Arcane Crystal"
                arcane_crystal_active = False
            elif arcane_crystal_active and ("score" not in changes or changes["score"] <= 0):
                changes["score"] = (changes.get("score", 0) + 5)
                arcane_crystal_message = "No score gain, +5 score from Arcane Crystal"
                arcane_crystal_active = False

            # Apply changes
            score_change = changes.get("score", 0)
            player["score"] += score_change
            if player["score"] < 0:
                player["score"] = 0
            player_health_change = changes.get("player_health", 0)
            player["health"] += player_health_change
            if player["health"] > player["max_health"]:
                player["health"] = player["max_health"]
            if current_companion["name"] and current_companion["health"] <= 0 and current_companion["name"] not in fallen_companions:
                fallen_companions.append(current_companion["name"])
            rune_change = changes.get("runes", 0)
            player["runes"] += rune_change
            scroll_change = changes.get("magic_scroll", 0)
            player["magic_scroll"] += scroll_change
            crystal_change = changes.get("arcane_crystal", 0)
            player["arcane_crystal"] += crystal_change
            potion_change = changes.get("healing_potion", 0)
            player["healing_potion"] += potion_change
            key_change = changes.get("mystic_key", 0)
            player["mystic_key"] += key_change
            xp_change = changes.get("xp", 0)
            levelup_health_change = level_check(xp_change)
            post_player_health = player["health"]
            post_comp_health = current_companion["health"] if current_companion["name"] else 0

            # Compute actual companion health change for reporting
            actual_comp_health_change = post_comp_health - pre_comp_health if current_companion["name"] else 0

            # Build stat changes message with colors
            stat_changes_list = []
            if score_change != 0:
                stat_changes_list.append(Fore.YELLOW + f"Score {'+' if score_change > 0 else ''}{score_change}" + Style.RESET_ALL)
            if arcane_crystal_message:
                stat_changes_list.append(Fore.BLUE + arcane_crystal_message + Style.RESET_ALL)
            if was_fallen and is_positive_outcome(changes):
                stat_changes_list.append(Fore.MAGENTA + f"{current_companion['name']} revived with +14 health" + Style.RESET_ALL)
            if player_health_change != 0 or levelup_health_change != 0:
                total_health_change = player_health_change + levelup_health_change
                stat_changes_list.append(Fore.RED + f"Health {'+' if total_health_change > 0 else ''}{total_health_change}" + Style.RESET_ALL)
                show_health_change = True
            if show_health_change:
                stat_changes_list.append(Fore.RED + f"Total Damage: Player [{pre_player_health} -> {post_player_health}]" + (f", Companion [{pre_comp_health} -> {post_comp_health}]" if current_companion["name"] else "") + Style.RESET_ALL)
            if rune_change != 0:
                stat_changes_list.append(Fore.CYAN + f"Runes {'+' if rune_change > 0 else ''}{rune_change}" + Style.RESET_ALL)
            if scroll_change != 0:
                stat_changes_list.append(Fore.YELLOW + f"Magic Scrolls {'+' if scroll_change > 0 else ''}{scroll_change}" + Style.RESET_ALL)
            if crystal_change != 0:
                stat_changes_list.append(Fore.BLUE + f"Arcane Crystals {'+' if crystal_change > 0 else ''}{crystal_change}" + Style.RESET_ALL)
            if potion_change != 0:
                stat_changes_list.append(Fore.RED + f"Healing Potions {'+' if potion_change > 0 else ''}{potion_change}" + Style.RESET_ALL)
            if key_change != 0:
                stat_changes_list.append(Fore.CYAN + f"Mystic Keys {'+' if key_change > 0 else ''}{key_change}" + Style.RESET_ALL)
            if xp_change != 0:
                stat_changes_list.append(Fore.GREEN + f"XP +{xp_change}" + Style.RESET_ALL)
            if actual_comp_health_change != 0 and current_companion["name"]:
                stat_changes_list.append(Fore.RED + f"{current_companion['name']}'s Health {'+' if actual_comp_health_change > 0 else ''}{actual_comp_health_change}" + Style.RESET_ALL)
            stat_changes = ", ".join(stat_changes_list) if stat_changes_list else "No changes"

            print(Fore.MAGENTA + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nPress Enter to continue..." + Style.RESET_ALL)
            input()

        elif choice == "5":
            inventory()

        elif choice == "6":
            companions_menu()

        elif choice == "7":
            save_game()
            print(Fore.MAGENTA + "\nPress Enter to continue..." + Style.RESET_ALL)
            input()

        elif choice == "8":
            load_game()
            print(Fore.MAGENTA + "\nPress Enter to continue..." + Style.RESET_ALL)
            input()

        elif choice == "9":
            os.system("cls")
            print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.MAGENTA + "OGENS FANTASY NEXUS - EXIT" + Style.RESET_ALL)
            print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.MAGENTA + get_random_ascii() + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nLeaving the Mystic Realm..." + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Final Runes: {player['runes']}" + Style.RESET_ALL)
            print(Fore.BLUE + f"Final Arcane Crystals: {player['arcane_crystal']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Level: {player['level']}" + Style.RESET_ALL)
            print(Fore.RED + f"Final Health: {player['health']}/{player['max_health']}" + Style.RESET_ALL)
            print(Fore.WHITE + f"Final Strength: {player['player_strength']}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nPress Enter to exit..." + Style.RESET_ALL)
            log_event("Game quit")
            input()
            break

        else:
            stat_changes = "Invalid choice"
            print(Fore.MAGENTA + "\nINVALID CHOICE..." + Style.RESET_ALL)
            print(Fore.MAGENTA + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nPress Enter to try again..." + Style.RESET_ALL)
            input()

if __name__ == "__main__":
    main()