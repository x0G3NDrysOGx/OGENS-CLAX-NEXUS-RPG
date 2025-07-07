from colorama import init, Fore, Style
init(autoreset=True, convert=True, strip=False, wrap=True)  # Robust initialization for Windows compatibility
import os
import secrets
import json
from datetime import datetime
import platform

# Define companion classes with unique effects
companion_classes = [
    "CyberSmith", "NetRunner", "Enforcer", "TechWiz", "StreetSam", "Decker", "SynthMage",
    "CyberMonk", "NanoDoc", "ShadowOp", "Hacker", "NeonBard", "ChromeLord", "DataShaman",
    "GearTinker", "BioHacker", "Assassin", "CodeWizard", "UrbanHunter", "GridPriest",
    "WarTech", "AugEnchanter", "NetInquisitor", "CryptoCaster"
]

# Define companion class modifiers
companion_class_modifiers = {
    "CyberSmith": {"damage_boost": 2, "damage_reduction": 2},
    "NetRunner": {"hacking_boost": 3},
    "Enforcer": {"damage_reduction": 3},
    "TechWiz": {"tech_boost": 2},
    "StreetSam": {"damage_boost": 2},
    "Decker": {"score_boost": 2},
    "SynthMage": {"hacking_boost": 2, "damage_reduction": 2, "damage_boost": 2},
    "CyberMonk": {"score_boost": 2},
    "NanoDoc": {"healing_boost": 3},
    "ShadowOp": {"crypto_boost": 2},
    "Hacker": {"score_boost": 2},
    "NeonBard": {"score_boost": 2},
    "ChromeLord": {"damage_boost": 2},
    "DataShaman": {"hacking_boost": 3},
    "GearTinker": {"nano_boost": 2},
    "BioHacker": {"healing_boost": 2},
    "Assassin": {"score_boost": 2},
    "CodeWizard": {"advanced_tech_boost": 2},
    "UrbanHunter": {"score_boost": 2},
    "GridPriest": {"healing_boost": 3},
    "WarTech": {"score_boost": 2},
    "AugEnchanter": {"tech_boost": 2},
    "NetInquisitor": {"crypto_boost": 2},
    "CryptoCaster": {"crypto_boost": 2}
}

# Initialize player stats
player = {
    "score": 0,
    "health": 100,
    "max_health": 200,
    "crypto_chips": 0,
    "nano_patch": 0,
    "data_drive": 0,
    "neon_key": 0,
    "quantum_core": 0,
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

# Track deactivated companions
deactivated_companions = []

# Current companion
current_companion = {
    "name": "",
    "health": 0,
    "strength": 0,
    "luck": 0,
    "class": ""
}

# Global variables
quantum_core_active = False
stat_changes = ""
last_ascii_used = None
last_path_chosen = None

# List of available colorama colors
COLORS = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
]

# Cyberpunk-themed ASCII art with 8 unique pieces
ascii_art_list = [
    """
    ╔══════[⚡]══════╗
    ║ ⚙ * | * * | * ⇓ ║
    ║ * * | *⌁* | * * ║
    ║ ↯ * | * * | * ⚡ ║
    ║ * * | * * | * * ║
    ╚══════[⚡]══════╝
    """,
    """
    ╔══════[⇓]══════╗
    ║ ⇓ * | * * | * ~ ║
    ║ * * | *⚡* | * * ║
    ║ ⚙ * | * * | * ↯ ║
    ║ * * | * * | * * ║
    ╚══════[⇓]══════╝
    """,
    """
    ╔═════[⚡⇓]═════╗
    ║ ~ * | * * | * ⚙ ║
    ║ * * | *⌁* | * * ║
    ║ ↯ * | * * | * ⇓ ║
    ║ * * | * * | * * ║
    ╚═════[⚡⇓]═════╝
    """,
    """
    ╔══════[⚙]══════╗
    ║ ⚙ * | * * | * ↯ ║
    ║ * * | *⚡* | * * ║
    ║ ⇓ * | * * | * ~ ║
    ║ * * | * * | * * ║
    ╚══════[⚙]══════╝
    """,
    """
    ╔═════[⇓⚡]═════╗
    ║ ↯ * | * * | * ⇓ ║
    ║ * * | *⌁* | * * ║
    ║ ~ * | * * | * ⚙ ║
    ║ * * | * * | * * ║
    ╚═════[⇓⚡]═════╝
    """,
    """
    ╔══════[⚡]══════╗
    ║ ⇓ * | * * | * ⚙ ║
    ║ * * | *⚡* | * * ║
    ║ ↯ * | * * | * ~ ║
    ║ * * | * * | * * ║
    ╚══════[⚡]══════╝
    """,
    """
    ╔══════[⚙]══════╗
    ║ ~ * | * * | * ↯ ║
    ║ * * | *⌁* | * * ║
    ║ ⚙ * | * * | * ⇓ ║
    ║ * * | * * | * * ║
    ╚══════[⚙]══════╝
    """,
    """
    ╔═════[⚡⇓]═════╗
    ║ ⚙ * | * * | * ~ ║
    ║ * * | *⚡* | * * ║
    ║ ⇓ * | * * | * ↯ ║
    ║ * * | * * | * * ║
    ╚═════[⚡⇓]═════╝
    """
]

def clear_console():
    """Clear the console in a cross-platform way."""
    try:
        os.system("cls" if platform.system() == "Windows" else "clear")
    except Exception as e:
        print(Fore.GREEN + f"Failed to clear console: {str(e)}" + Style.RESET_ALL)

from colorama import Fore, Style

def get_path_dial():
    """Generate a cyberpunk-themed ASCII neon grid with cyan structure and numbers, highlighting the last chosen path in green."""
    dial_lines = [
        "     ≣≣≣≣≣     ",
        "   |  ⚡ 1 ⚡    ",
        "≣≣≣==≣≣≣==≣≣≣",
        "| 4 ⚡  ⚡ 2 | ",
        "≣≣≣==≣≣≣==≣≣≣",
        "   |  ⚡ 3 ⚡    ",
        "     ≣≣≣≣≣     "
    ]
    colored_dial = []
    for line in dial_lines:
        new_line = line
        for i in range(1, 5):
            path_num = str(i)
            if path_num in line:
                try:
                    if last_path_chosen is not None and path_num == last_path_chosen:
                        new_line = new_line.replace(path_num, f"{Fore.RED}{path_num}{Style.RESET_ALL}")
                    else:
                        new_line = new_line.replace(path_num, f"{Fore.CYAN}{path_num}{Style.RESET_ALL}")
                except:
                    new_line = new_line.replace(path_num, path_num)
        try:
            colored_line = f"{Fore.CYAN}{new_line}{Style.RESET_ALL}"
        except:
            colored_line = new_line
        colored_dial.append(colored_line)
    return "\n".join(colored_dial)

def get_random_ascii():
    """Return a random ASCII art piece with a random color."""
    global last_ascii_used
    available_indices = [i for i in range(len(ascii_art_list)) if i != last_ascii_used]
    if not available_indices:
        available_indices = list(range(len(ascii_art_list)))
    new_index = secrets.choice(available_indices)
    last_ascii_used = new_index
    ascii_art = ascii_art_list[new_index]
    color = COLORS[new_index % len(COLORS)]
    try:
        colored_ascii = f"{color}{ascii_art}{Style.RESET_ALL}"
    except:
        colored_ascii = ascii_art
    return colored_ascii

def log_event(event_message):
    """Log significant game events to GameLog.txt."""
    if event_message not in ["Game won", "Game lost", "Game quit"]:
        return
    try:
        with open("GameLog.txt", "a") as f:
            timestamp = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
            player_stats = (
                f"Score={player['score']}, "
                f"Crypto Chips={player['crypto_chips']}, "
                f"Quantum Cores={player['quantum_core']}, "
                f"Level={player['level']}, "
                f"Health={player['health']}/{player['max_health']}, "
                f"Strength={player['player_strength']}"
            )
            f.write(f"{timestamp} - {event_message} - {player_stats}\n")
    except Exception as e:
        print(Fore.GREEN + f"Failed to log event: {str(e)}" + Style.RESET_ALL)

def save_game():
    """Save game state to SaveGame.txt with backup."""
    global player, companion_stats, current_companion, deactivated_companions, stat_changes
    game_state = {
        "player": {k: int(v) if isinstance(v, (int, float)) else v for k, v in player.items()},
        "companion_stats": {
            name: {k: int(v) if isinstance(v, (int, float)) else v for k, v in stats.items()}
            for name, stats in companion_stats.items()
        },
        "current_companion": {k: int(v) if isinstance(v, (int, float)) else v for k, v in current_companion.items()},
        "deactivated_companions": deactivated_companions
    }
    try:
        if os.path.exists("SaveGame.txt"):
            if os.path.exists("SaveGame.bak"):
                os.remove("SaveGame.bak")
            os.rename("SaveGame.txt", "SaveGame.bak")
        with open("SaveGame.txt", "w") as f:
            json.dump(game_state, f, indent=2)
        stat_changes = "Data backed up to the grid"
        print(Fore.GREEN + "Your data is backed up to the grid!" + Style.RESET_ALL)
    except Exception as e:
        if os.path.exists("SaveGame.bak"):
            os.rename("SaveGame.bak", "SaveGame.txt")
            stat_changes = f"Failed to back up data, restored from backup: {str(e)}"
            print(Fore.GREEN + f"Failed to back up data, restored from backup... Error: {str(e)}" + Style.RESET_ALL)
        else:
            stat_changes = f"Failed to back up data, no backup available: {str(e)}"
            print(Fore.GREEN + f"Failed to back up data, no backup available... Error: {str(e)}" + Style.RESET_ALL)
    return stat_changes

def load_game():
    """Load game state from SaveGame.txt."""
    global player, companion_stats, current_companion, deactivated_companions, stat_changes
    if not os.path.exists("SaveGame.txt"):
        stat_changes = "No data found on the grid"
        print(Fore.GREEN + "No data found on the grid..." + Style.RESET_ALL)
        return
    try:
        with open("SaveGame.txt", "r") as f:
            game_state = json.load(f)
        
        default_player = {
            "score": 0, "health": 100, "max_health": 200, "crypto_chips": 0,
            "nano_patch": 0, "data_drive": 0, "neon_key": 0, "quantum_core": 0,
            "player_strength": secrets.randbelow(10) + 5, "level": 1, "xp": 0, "xp_needed": 50
        }
        for key in default_player:
            if key in game_state.get("player", {}):
                player[key] = int(game_state["player"][key]) if key in [
                    "score", "health", "max_health", "crypto_chips", "nano_patch",
                    "data_drive", "neon_key", "quantum_core", "player_strength", "level", "xp", "xp_needed"
                ] else game_state["player"][key]
            else:
                player[key] = default_player[key]
        
        companion_stats.clear()
        companion_stats.update({
            name: {
                "health": max(0, min(secrets.randbelow(50) + 50, 100)),
                "strength": secrets.randbelow(10) + 5,
                "luck": secrets.randbelow(10) + 1,
                "class": secrets.choice(companion_classes)
            } for name in companions
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
            # Check if companion is deactivated and assign a new one
            if current_companion["health"] <= 0 or current_companion["name"] in deactivated_companions:
                if current_companion["name"] not in deactivated_companions:
                    deactivated_companions.append(current_companion["name"])
                available_companions = [name for name in companions if name not in deactivated_companions]
                if available_companions:
                    new_companion_name = secrets.choice(available_companions)
                    current_companion.update({
                        "name": new_companion_name,
                        "health": max(0, min(companion_stats[new_companion_name]["health"], 100)),
                        "strength": companion_stats[new_companion_name]["strength"],
                        "luck": companion_stats[new_companion_name]["luck"],
                        "class": companion_stats[new_companion_name]["class"]
                    })
                    companion_stats[new_companion_name]["health"] = current_companion["health"]
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
        
        deactivated_companions.clear()
        deactivated_companions.extend(game_state.get("deactivated_companions", []))
        
        stat_changes = "Data restored from the grid"
        print(Fore.GREEN + "The grid restores your data!" + Style.RESET_ALL)
    except Exception as e:
        stat_changes = f"Failed to load data: {str(e)}"
        print(Fore.GREEN + f"Failed to load data... Error: {str(e)}" + Style.RESET_ALL)
    return stat_changes

def roll_dice():
    """Roll two D10s and calculate outcome with luck modifier."""
    die1 = secrets.randbelow(10) + 1  # D10 (1-10)
    die2 = secrets.randbelow(10) + 1  # D10 (1-10)
    outcome = die1 + die2 - 1  # Range: 1-19
    luck_modifier = current_companion["luck"] - 5 if current_companion["name"] else 0
    adjusted_outcome = max(1, min(100, outcome + luck_modifier))  # Cap at 1-100
    return die1, die2, outcome, adjusted_outcome

def level_check(xp_change):
    """Check for level-up and update player stats."""
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
    """Determine if an outcome is positive."""
    return (changes.get("player_health", 0) >= 0 and
            changes.get("comp_health", 0) >= 0 and
            (changes.get("crypto_chips", 0) > 0 or
             changes.get("data_drive", 0) > 0 or
             changes.get("neon_key", 0) > 0 or
             changes.get("quantum_core", 0) > 0 or
             changes.get("score", 0) > 0))

def path_outcomes(path, adjusted_outcome):
    global player, current_companion, stat_changes, quantum_core_active
    outcomes_neon_underdistrict = {
    1: ("You hack a street terminal, snagging a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    2: ("A rogue AI triggers a neural spike", {"comp_health": -6, "xp": 1, "player_health": -6}),
    3: ("A gang ambush catches you in a dark alley", {"comp_health": -5, "xp": 1, "player_health": -5}),
    4: ("You slip past drones, finding a Nano Patch in a stash", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    5: ("Your hack fails, alerting street sentinels", {"score": 3 + player["level"], "xp": 5, "comp_health": -2, "player_health": -2}),
    6: ("You fry a rival gang’s server, snagging a Quantum Core", {"score": 7 + player["level"], "crypto_chips": 1, "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    7: ("A glitchy implant shorts out your ally", {"comp_health": -6, "xp": 1, "player_health": -6}),
    8: ("A rigged trap zaps you in the underdistrict", {"comp_health": -5, "xp": 1, "player_health": -5}),
    9: ("You clear a gang hideout, securing a Crypto Chip", {"score": 4 + player["level"], "crypto_chips": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    10: ("A cyberhound pack overwhelms you", {"comp_health": -7, "xp": 1, "player_health": -7}),
    11: ("You bribe a street fixer, earning a Neon Key", {"score": 6 + player["level"], "neon_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    12: ("A double-crossing fixer sets you up", {"comp_health": -6, "xp": 1, "player_health": -6}),
    13: ("You trade with a netrunner, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    14: ("Your deal angers a street gang", {"comp_health": -5, "xp": 1, "player_health": -5}),
    15: ("A drone swarm locks onto you", {"comp_health": -2, "xp": 1, "player_health": -2}),
    16: ("You bypass a firewall, uncovering a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    17: ("Your hack backfires, frying your gear", {"comp_health": -6, "xp": 1, "player_health": -6}),
    18: ("A rigged terminal shocks you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    19: ("You tap a hidden node, gaining a Nano Patch", {"score": 4 + player["level"], "nano_patch": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    20: ("A virus infects your neural link", {"comp_health": -7, "xp": 1, "player_health": -7}),
    21: ("You raid a black-market cache, securing a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    22: ("You take down a gang enforcer, claiming a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    23: ("You broker a deal with a fixer, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    24: ("You unlock a hidden server, finding a Crypto Chip", {"score": 6 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    25: ("A laser trap fries your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    26: ("A hacked ally turns on you", {"comp_health": -6, "xp": 1, "player_health": -6}),
    27: ("You stabilize a rogue AI, gaining a Nano Patch", {"score": 6 + player["level"], "nano_patch": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    28: ("A viral spike drains your implants", {"comp_health": -5, "xp": 1, "player_health": -5}),
    29: ("You bypass gang security, securing a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    30: ("You fry a rival decker, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    31: ("A street rat sells you out", {"comp_health": -6, "xp": 1, "player_health": -6}),
    32: ("You hack a neon grid, uncovering a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    33: ("Your signal draws a drone swarm", {"comp_health": -7, "xp": 1, "player_health": -7}),
    34: ("A collapsing rig traps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    35: ("You gain a fixer’s trust, earning a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    36: ("Your hack triggers a corporate trace", {"comp_health": -6, "xp": 1, "player_health": -6}),
    37: ("You find a hidden crypto node in the underdistrict", {"score": 6 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    38: ("You take down a street drone, gaining a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    39: ("Your actions provoke a gang war", {"comp_health": -5, "xp": 1, "player_health": -5}),
    40: ("You override a security grid, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    41: ("A trap exposes you to corporate mercs", {"comp_health": -6, "xp": 1, "player_health": -6}),
    42: ("A swarm of micro-drones attacks", {"comp_health": -7, "xp": 1, "player_health": -7}),
    43: ("You barter with a shadow dealer, earning a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    44: ("A neural spike overloads your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    45: ("You slip through neon shadows, finding a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    46: ("You take down a cyber-thug, securing a Neon Key", {"score": 6 + player["level"], "neon_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    47: ("A rogue signal fries your implants", {"comp_health": -6, "xp": 1, "player_health": -6}),
    48: ("You unlock a hidden cache, gaining a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    49: ("A rigged datastream traps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    50: ("You defeat a gang netrunner, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    51: ("You hack a black-market node, gaining a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    52: ("A viral worm corrupts your systems", {"comp_health": -6, "xp": 1, "player_health": -6}),
    53: ("A street gang corners you in a neon alley", {"comp_health": -5, "xp": 1, "player_health": -5}),
    54: ("You dodge a patrol bot, finding a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    55: ("Your signal jams, alerting a gang", {"score": 3 + player["level"], "xp": 5, "comp_health": -2, "player_health": -2}),
    56: ("You crash a rival’s server, snagging a Neon Key", {"score": 6 + player["level"], "neon_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    57: ("A glitch fries your ally’s neural link", {"comp_health": -6, "xp": 1, "player_health": -6}),
    58: ("A rigged holo-trap zaps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    59: ("You raid a gang stash, securing a Nano Patch", {"score": 4 + player["level"], "nano_patch": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    60: ("A cyber-assassin strikes from the shadows", {"comp_health": -7, "xp": 1, "player_health": -7}),
    61: ("You hack a smuggler’s cache, earning a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    62: ("A rogue decker hacks your implants", {"comp_health": -6, "xp": 1, "player_health": -6}),
    63: ("You trade with a street vendor, gaining a Crypto Chip", {"score": 5 + player["level"], "crypto_chips": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    64: ("Your deal goes sour, sparking a fight", {"comp_health": -5, "xp": 1, "player_health": -5}),
    65: ("A glitch swarm overwhelms your defenses", {"comp_health": -2, "xp": 1, "player_health": -2}),
    66: ("You slice through a gang’s firewall, finding a Data Drive", {"score": 8 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    67: ("Your hack triggers a digital trap", {"comp_health": -6, "xp": 1, "player_health": -6}),
    68: ("A rigged node spikes your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    69: ("You tap a hidden datastream, gaining a Neon Key", {"score": 4 + player["level"], "neon_key": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    70: ("A viral payload crashes your implants", {"comp_health": -7, "xp": 1, "player_health": -7}),
    71: ("You raid a gang server, securing a Crypto Chip", {"score": 7 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    72: ("You defeat a street samurai, claiming a Quantum Core", {"score": 5 + player["level"], "quantum_core": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    73: ("You broker a deal with a smuggler, gaining a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    74: ("You unlock a neon vault, finding a Data Drive", {"score": 6 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    75: ("A laser grid traps you in an alley", {"comp_health": -5, "xp": 1, "player_health": -5}),
    76: ("A hacked drone attacks you", {"comp_health": -6, "xp": 1, "player_health": -6}),
    77: ("You stabilize a glitched node, gaining a Crypto Chip", {"score": 6 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    78: ("A viral spike shorts your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    79: ("You bypass a gang trap, securing a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    80: ("You fry a rival’s rig, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    81: ("A fixer betrays you to a gang", {"comp_health": -6, "xp": 1, "player_health": -6}),
    82: ("You hack a hidden terminal, uncovering a Data Drive", {"score": 8 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    83: ("Your signal draws a bounty hunter", {"comp_health": -7, "xp": 1, "player_health": -7}),
    84: ("A collapsing neon sign traps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    85: ("You gain a smuggler’s trust, earning a Crypto Chip", {"score": 5 + player["level"], "crypto_chips": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    86: ("Your hack triggers a street lockdown", {"comp_health": -6, "xp": 1, "player_health": -6}),
    87: ("You find a hidden neon cache, securing a Nano Patch", {"score": 6 + player["level"], "nano_patch": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    88: ("You take down a gang bot, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    89: ("Your actions spark a gang ambush", {"comp_health": -5, "xp": 1, "player_health": -5}),
    90: ("You override a street grid, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    91: ("A trap exposes you to street drones", {"comp_health": -6, "xp": 1, "player_health": -6}),
    92: ("A swarm of gang enforcers attacks", {"comp_health": -7, "xp": 1, "player_health": -7}),
    93: ("You barter with a neon trader, earning a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    94: ("A neural spike fries your rig", {"comp_health": -5, "xp": 1, "player_health": -5}),
    95: ("You slip through a gang’s net, finding a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    96: ("You defeat a cyber-fixer, securing a Data Drive", {"score": 6 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    97: ("A rogue AI curses your systems", {"comp_health": -6, "xp": 1, "player_health": -6}),
    98: ("You unlock a neon server, gaining a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    99: ("A rigged node traps you in a datastream", {"comp_health": -5, "xp": 1, "player_health": -5}),
    100: ("You defeat a street boss, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4})
}

    outcomes_corporate_skyspire = {
    1: ("You infiltrate a corp server, snagging a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    2: ("A security AI locks you in a digital trap", {"comp_health": -6, "xp": 1, "player_health": -6}),
    3: ("A laser grid slices through your defenses", {"comp_health": -5, "xp": 1, "player_health": -5}),
    4: ("You bypass corp drones, finding a Nano Patch in a vault", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    5: ("Your intrusion triggers a lockdown", {"score": 3 + player["level"], "xp": 5, "comp_health": -2, "player_health": -2}),
    6: ("You fry a corp mainframe, seizing a Quantum Core", {"score": 7 + player["level"], "crypto_chips": 1, "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    7: ("Your ally’s implant is hacked by corp security", {"comp_health": -6, "xp": 1, "player_health": -6}),
    8: ("A turret catches you in the skyspire", {"comp_health": -5, "xp": 1, "player_health": -5}),
    9: ("You clear a corp lab, securing a Crypto Chip", {"score": 4 + player["level"], "crypto_chips": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    10: ("Corporate enforcers overwhelm you", {"comp_health": -7, "xp": 1, "player_health": -7}),
    11: ("You bribe a corp insider, earning a Neon Key", {"score": 6 + player["level"], "neon_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    12: ("An insider betrays you to security", {"comp_health": -6, "xp": 1, "player_health": -6}),
    13: ("You trade with a rogue exec, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    14: ("Your deal provokes a corp hit squad", {"comp_health": -5, "xp": 1, "player_health": -5}),
    15: ("A drone swarm targets you in the skyspire", {"comp_health": -2, "xp": 1, "player_health": -2}),
    16: ("You slice a corporate firewall, uncovering a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    17: ("Your hack triggers a security surge", {"comp_health": -6, "xp": 1, "player_health": -6}),
    18: ("A rigged terminal fries your rig", {"comp_health": -5, "xp": 1, "player_health": -5}),
    19: ("You tap a hidden server, gaining a Nano Patch", {"score": 4 + player["level"], "nano_patch": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    20: ("A corporate virus infects your systems", {"comp_health": -7, "xp": 1, "player_health": -7}),
    21: ("You raid a corp vault, securing a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    22: ("You take down a corp guard, claiming a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    23: ("You broker a deal with a rogue AI, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    24: ("You unlock a secure server, finding a Crypto Chip", {"score": 6 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    25: ("A laser trap burns your circuits", {"comp_health": -5, "xp": 1, "player_health": -5}),
    26: ("A hacked ally sabotages your hack", {"comp_health": -6, "xp": 1, "player_health": -6}),
    27: ("You stabilize a glitched server, gaining a Nano Patch", {"score": 6 + player["level"], "nano_patch": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    28: ("A security spike drains your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    29: ("You bypass corp security, securing a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    30: ("You fry a corp netrunner, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    31: ("A corp mole sells you out", {"comp_health": -6, "xp": 1, "player_health": -6}),
    32: ("You hack a skyspire node, uncovering a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    33: ("Your signal draws a security swarm", {"comp_health": -7, "xp": 1, "player_health": -7}),
    34: ("A collapsing platform traps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    35: ("You gain an exec’s trust, earning a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    36: ("Your hack triggers a corporate lockdown", {"comp_health": -6, "xp": 1, "player_health": -6}),
    37: ("You find a hidden corp cache, securing a Nano Patch", {"score": 6 + player["level"], "nano_patch": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    38: ("You take down a corp drone, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    39: ("Your actions spark a security alert", {"comp_health": -5, "xp": 1, "player_health": -5}),
    40: ("You override a corp grid, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    41: ("A trap exposes you to corp enforcers", {"comp_health": -6, "xp": 1, "player_health": -6}),
    42: ("A swarm of security bots attacks", {"comp_health": -7, "xp": 1, "player_health": -7}),
    43: ("You barter with a rogue exec, earning a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    44: ("A neural spike fries your rig", {"comp_health": -5, "xp": 1, "player_health": -5}),
    45: ("You slip through a corp network, finding a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    46: ("You defeat a corp sentinel, securing a Data Drive", {"score": 6 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    47: ("A security AI curses your systems", {"comp_health": -6, "xp": 1, "player_health": -6}),
    48: ("You unlock a corp vault, gaining a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    49: ("A rigged node traps you in a datastream", {"comp_health": -5, "xp": 1, "player_health": -5}),
    50: ("You defeat a corp netrunner, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    51: ("You hack a secure terminal, gaining a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    52: ("A viral worm corrupts your implants", {"comp_health": -6, "xp": 1, "player_health": -6}),
    53: ("A corp turret locks onto you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    54: ("You dodge a security bot, finding a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    55: ("Your signal jams, alerting guards", {"score": 3 + player["level"], "xp": 5, "comp_health": -2, "player_health": -2}),
    56: ("You crash a corp server, snagging a Neon Key", {"score": 6 + player["level"], "neon_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    57: ("A glitch fries your ally’s systems", {"comp_health": -6, "xp": 1, "player_health": -6}),
    58: ("A rigged holo-trap zaps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    59: ("You raid a corp lab, securing a Nano Patch", {"score": 4 + player["level"], "nano_patch": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    60: ("A cyber-assassin strikes from the shadows", {"comp_health": -7, "xp": 1, "player_health": -7}),
    61: ("You hack a corp cache, earning a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    62: ("A rogue AI hacks your implants", {"comp_health": -6, "xp": 1, "player_health": -6}),
    63: ("You trade with a corp defector, gaining a Crypto Chip", {"score": 5 + player["level"], "crypto_chips": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    64: ("Your deal sparks a corp ambush", {"comp_health": -5, "xp": 1, "player_health": -5}),
    65: ("A glitch swarm overwhelms your defenses", {"comp_health": -2, "xp": 1, "player_health": -2}),
    66: ("You slice through a corp firewall, finding a Data Drive", {"score": 8 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    67: ("Your hack triggers a digital surge", {"comp_health": -6, "xp": 1, "player_health": -6}),
    68: ("A rigged node spikes your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    69: ("You tap a hidden datastream, gaining a Neon Key", {"score": 4 + player["level"], "neon_key": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    70: ("A viral payload crashes your implants", {"comp_health": -7, "xp": 1, "player_health": -7}),
    71: ("You raid a corp server, securing a Crypto Chip", {"score": 7 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    72: ("You defeat a corp enforcer, claiming a Quantum Core", {"score": 5 + player["level"], "quantum_core": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    73: ("You broker a deal with a rogue AI, gaining a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    74: ("You unlock a secure vault, finding a Data Drive", {"score": 6 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    75: ("A laser grid traps you in the skyspire", {"comp_health": -5, "xp": 1, "player_health": -5}),
    76: ("A hacked drone attacks you", {"comp_health": -6, "xp": 1, "player_health": -6}),
    77: ("You stabilize a glitched node, gaining a Crypto Chip", {"score": 6 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    78: ("A viral spike shorts your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    79: ("You bypass a corp trap, securing a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    80: ("You fry a corp rig, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    81: ("A corp defector betrays you", {"comp_health": -6, "xp": 1, "player_health": -6}),
    82: ("You hack a hidden terminal, uncovering a Data Drive", {"score": 8 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    83: ("Your signal draws a bounty hunter", {"comp_health": -7, "xp": 1, "player_health": -7}),
    84: ("A collapsing platform traps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    85: ("You gain a defector’s trust, earning a Crypto Chip", {"score": 5 + player["level"], "crypto_chips": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    86: ("Your hack triggers a skyspire lockdown", {"comp_health": -6, "xp": 1, "player_health": -6}),
    87: ("You find a hidden corp cache, securing a Nano Patch", {"score": 6 + player["level"], "nano_patch": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    88: ("You take down a corp bot, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    89: ("Your actions spark a corp alert", {"comp_health": -5, "xp": 1, "player_health": -5}),
    90: ("You override a skyspire grid, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    91: ("A trap exposes you to corp drones", {"comp_health": -6, "xp": 1, "player_health": -6}),
    92: ("A swarm of corp enforcers attacks", {"comp_health": -7, "xp": 1, "player_health": -7}),
    93: ("You barter with a corp insider, earning a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    94: ("A neural spike fries your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    95: ("You slip through a corp net, finding a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    96: ("You defeat a corp operative, securing a Data Drive", {"score": 6 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    97: ("A corp AI curses your systems", {"comp_health": -6, "xp": 1, "player_health": -6}),
    98: ("You unlock a corp server, gaining a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    99: ("A rigged node traps you in a datastream", {"comp_health": -5, "xp": 1, "player_health": -5}),
    100: ("You defeat a corp boss, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4})
}

    outcomes_data_vault = {
    1: ("You bypass vault sentinels, uncovering a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    2: ("A security trap locks you in a digital cage", {"comp_health": -6, "xp": 1, "player_health": -6}),
    3: ("A data spike fries your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    4: ("You evade vault drones, finding a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    5: ("Your hack disturbs the vault’s AI", {"score": 3 + player["level"], "xp": 5, "comp_health": -2, "player_health": -2}),
    6: ("You fry a vault server, claiming a Quantum Core", {"score": 7 + player["level"], "crypto_chips": 1, "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    7: ("Your ally’s implant is corrupted by vault security", {"comp_health": -6, "xp": 1, "player_health": -6}),
    8: ("A laser trap zaps you in the vault", {"comp_health": -5, "xp": 1, "player_health": -5}),
    9: ("You clear a vault node, securing a Crypto Chip", {"score": 4 + player["level"], "crypto_chips": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    10: ("Vault sentinels overwhelm you", {"comp_health": -7, "xp": 1, "player_health": -7}),
    11: ("You bribe a vault tech, earning a Neon Key", {"score": 6 + player["level"], "neon_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    12: ("A tech betrays you to the vault AI", {"comp_health": -6, "xp": 1, "player_health": -6}),
    13: ("You trade with a rogue decker, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    14: ("Your deal angers vault security", {"comp_health": -5, "xp": 1, "player_health": -5}),
    15: ("A drone swarm locks onto you", {"comp_health": -2, "xp": 1, "player_health": -2}),
    16: ("You slice a vault firewall, uncovering a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    17: ("Your hack triggers a data surge", {"comp_health": -6, "xp": 1, "player_health": -6}),
    18: ("A rigged node fries your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    19: ("You tap a hidden datastream, gaining a Nano Patch", {"score": 4 + player["level"], "nano_patch": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    20: ("A vault virus infects your implants", {"comp_health": -7, "xp": 1, "player_health": -7}),
    21: ("You raid a vault cache, securing a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    22: ("You take down a vault drone, claiming a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    23: ("You broker a deal with a vault AI, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    24: ("You unlock a secure node, finding a Crypto Chip", {"score": 6 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    25: ("A laser trap burns your circuits", {"comp_health": -5, "xp": 1, "player_health": -5}),
    26: ("A hacked ally sabotages your hack", {"comp_health": -6, "xp": 1, "player_health": -6}),
    27: ("You stabilize a vault node, gaining a Nano Patch", {"score": 6 + player["level"], "nano_patch": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    28: ("A security spike drains your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    29: ("You bypass vault security, securing a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    30: ("You fry a vault netrunner, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    31: ("A vault tech sells you out", {"comp_health": -6, "xp": 1, "player_health": -6}),
    32: ("You hack a vault node, uncovering a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    33: ("Your signal draws a security swarm", {"comp_health": -7, "xp": 1, "player_health": -7}),
    34: ("A collapsing vault traps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    35: ("You gain a decker’s trust, earning a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    36: ("Your hack triggers a vault lockdown", {"comp_health": -6, "xp": 1, "player_health": -6}),
    37: ("You find a hidden vault cache, securing a Nano Patch", {"score": 6 + player["level"], "nano_patch": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    38: ("You take down a vault drone, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    39: ("Your actions spark a security alert", {"comp_health": -5, "xp": 1, "player_health": -5}),
    40: ("You override a vault grid, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    41: ("A trap exposes you to vault sentinels", {"comp_health": -6, "xp": 1, "player_health": -6}),
    42: ("A swarm of vault drones attacks", {"comp_health": -7, "xp": 1, "player_health": -7}),
    43: ("You barter with a vault tech, earning a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    44: ("A data spike fries your rig", {"comp_health": -5, "xp": 1, "player_health": -5}),
    45: ("You slip through a vault network, finding a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    46: ("You defeat a vault sentinel, securing a Data Drive", {"score": 6 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    47: ("A vault AI curses your systems", {"comp_health": -6, "xp": 1, "player_health": -6}),
    48: ("You unlock a vault server, gaining a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    49: ("A rigged node traps you in a datastream", {"comp_health": -5, "xp": 1, "player_health": -5}),
    50: ("You defeat a vault overseer, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    51: ("You hack a secure vault node, gaining a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    52: ("A viral worm corrupts your implants", {"comp_health": -6, "xp": 1, "player_health": -6}),
    53: ("A vault turret locks onto you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    54: ("You dodge a security bot, finding a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    55: ("Your signal jams, alerting guards", {"score": 3 + player["level"], "xp": 5, "comp_health": -2, "player_health": -2}),
    56: ("You crash a vault server, snagging a Neon Key", {"score": 6 + player["level"], "neon_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    57: ("A glitch fries your ally’s systems", {"comp_health": -6, "xp": 1, "player_health": -6}),
    58: ("A rigged holo-trap zaps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    59: ("You raid a vault cache, securing a Nano Patch", {"score": 4 + player["level"], "nano_patch": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    60: ("A cyber-assassin strikes from the shadows", {"comp_health": -7, "xp": 1, "player_health": -7}),
    61: ("You hack a vault archive, earning a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    62: ("A rogue AI hacks your implants", {"comp_health": -6, "xp": 1, "player_health": -6}),
    63: ("You trade with a vault defector, gaining a Crypto Chip", {"score": 5 + player["level"], "crypto_chips": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    64: ("Your deal sparks a vault ambush", {"comp_health": -5, "xp": 1, "player_health": -5}),
    65: ("A glitch swarm overwhelms your defenses", {"comp_health": -2, "xp": 1, "player_health": -2}),
    66: ("You slice through a vault firewall, finding a Data Drive", {"score": 8 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    67: ("Your hack triggers a digital surge", {"comp_health": -6, "xp": 1, "player_health": -6}),
    68: ("A rigged node spikes your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    69: ("You tap a hidden datastream, gaining a Neon Key", {"score": 4 + player["level"], "neon_key": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    70: ("A viral payload crashes your implants", {"comp_health": -7, "xp": 1, "player_health": -7}),
    71: ("You raid a vault server, securing a Crypto Chip", {"score": 7 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    72: ("You defeat a vault enforcer, claiming a Quantum Core", {"score": 5 + player["level"], "quantum_core": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    73: ("You broker a deal with a rogue AI, gaining a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    74: ("You unlock a secure vault, finding a Data Drive", {"score": 6 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    75: ("A laser grid traps you in the vault", {"comp_health": -5, "xp": 1, "player_health": -5}),
    76: ("A hacked drone attacks you", {"comp_health": -6, "xp": 1, "player_health": -6}),
    77: ("You stabilize a glitched node, gaining a Crypto Chip", {"score": 6 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    78: ("A viral spike shorts your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    79: ("You bypass a vault trap, securing a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    80: ("You fry a vault rig, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    81: ("A vault defector betrays you", {"comp_health": -6, "xp": 1, "player_health": -6}),
    82: ("You hack a hidden terminal, uncovering a Data Drive", {"score": 8 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    83: ("Your signal draws a bounty hunter", {"comp_health": -7, "xp": 1, "player_health": -7}),
    84: ("A collapsing vault traps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    85: ("You gain a defector’s trust, earning a Crypto Chip", {"score": 5 + player["level"], "crypto_chips": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    86: ("Your hack triggers a vault lockdown", {"comp_health": -6, "xp": 1, "player_health": -6}),
    87: ("You find a hidden vault cache, securing a Nano Patch", {"score": 6 + player["level"], "nano_patch": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    88: ("You take down a vault bot, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    89: ("Your actions spark a vault alert", {"comp_health": -5, "xp": 1, "player_health": -5}),
    90: ("You override a vault grid, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    91: ("A trap exposes you to vault drones", {"comp_health": -6, "xp": 1, "player_health": -6}),
    92: ("A swarm of vault enforcers attacks", {"comp_health": -7, "xp": 1, "player_health": -7}),
    93: ("You barter with a vault insider, earning a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    94: ("A data spike fries your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    95: ("You slip through a vault net, finding a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    96: ("You defeat a vault operative, securing a Data Drive", {"score": 6 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    97: ("A vault AI curses your systems", {"comp_health": -6, "xp": 1, "player_health": -6}),
    98: ("You unlock a vault server, gaining a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    99: ("A rigged node traps you in a datastream", {"comp_health": -5, "xp": 1, "player_health": -5}),
    100: ("You defeat a vault boss, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4})
}

    outcomes_grid_wastelands = {
    1: ("You scavenge a ruined grid, finding a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    2: ("A rogue signal fries your systems", {"comp_health": -6, "xp": 1, "player_health": -6}),
    3: ("A glitch trap zaps you in the wastelands", {"comp_health": -5, "xp": 1, "player_health": -5}),
    4: ("You evade scavenger drones, finding a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    5: ("Your hack disturbs a rogue AI", {"score": 3 + player["level"], "xp": 5, "comp_health": -2, "player_health": -2}),
    6: ("You fry a wasteland server, claiming a Quantum Core", {"score": 7 + player["level"], "crypto_chips": 1, "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    7: ("Your ally’s implant is corrupted by a glitch", {"comp_health": -6, "xp": 1, "player_health": -6}),
    8: ("A rigged node shocks you in the wastelands", {"comp_health": -5, "xp": 1, "player_health": -5}),
    9: ("You clear a scavenger camp, securing a Crypto Chip", {"score": 4 + player["level"], "crypto_chips": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    10: ("A scavenger horde overwhelms you", {"comp_health": -7, "xp": 1, "player_health": -7}),
    11: ("You bribe a wasteland nomad, earning a Neon Key", {"score": 6 + player["level"], "neon_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    12: ("A nomad betrays you to scavengers", {"comp_health": -6, "xp": 1, "player_health": -6}),
    13: ("You trade with a rogue decker, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    14: ("Your deal angers wasteland raiders", {"comp_health": -5, "xp": 1, "player_health": -5}),
    15: ("A drone swarm locks onto you", {"comp_health": -2, "xp": 1, "player_health": -2}),
    16: ("You slice a wasteland firewall, uncovering a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    17: ("Your hack triggers a grid surge", {"comp_health": -6, "xp": 1, "player_health": -6}),
    18: ("A rigged node fries your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    19: ("You tap a hidden datastream, gaining a Nano Patch", {"score": 4 + player["level"], "nano_patch": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    20: ("A wasteland virus infects your implants", {"comp_health": -7, "xp": 1, "player_health": -7}),
    21: ("You raid a scavenger cache, securing a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    22: ("You take down a scavenger drone, claiming a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    23: ("You broker a deal with a wasteland AI, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    24: ("You unlock a ruined server, finding a Crypto Chip", {"score": 6 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    25: ("A laser trap burns your circuits", {"comp_health": -5, "xp": 1, "player_health": -5}),
    26: ("A hacked ally sabotages your hack", {"comp_health": -6, "xp": 1, "player_health": -6}),
    27: ("You stabilize a glitched node, gaining a Nano Patch", {"score": 6 + player["level"], "nano_patch": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    28: ("A glitch spike drains your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    29: ("You bypass scavenger traps, securing a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    30: ("You fry a scavenger netrunner, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    31: ("A scavenger sells you out", {"comp_health": -6, "xp": 1, "player_health": -6}),
    32: ("You hack a wasteland node, uncovering a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    33: ("Your signal draws a scavenger swarm", {"comp_health": -7, "xp": 1, "player_health": -7}),
    34: ("A collapsing rig traps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    35: ("You gain a nomad’s trust, earning a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    36: ("Your hack triggers a wasteland lockdown", {"comp_health": -6, "xp": 1, "player_health": -6}),
    37: ("You find a hidden wasteland cache, securing a Nano Patch", {"score": 6 + player["level"], "nano_patch": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    38: ("You take down a wasteland drone, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    39: ("Your actions spark a scavenger alert", {"comp_health": -5, "xp": 1, "player_health": -5}),
    40: ("You override a wasteland grid, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    41: ("A trap exposes you to wasteland drones", {"comp_health": -6, "xp": 1, "player_health": -6}),
    42: ("A swarm of scavenger bots attacks", {"comp_health": -7, "xp": 1, "player_health": -7}),
    43: ("You barter with a wasteland trader, earning a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    44: ("A glitch spike fries your rig", {"comp_health": -5, "xp": 1, "player_health": -5}),
    45: ("You slip through a wasteland net, finding a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    46: ("You defeat a wasteland raider, securing a Data Drive", {"score": 6 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    47: ("A wasteland AI curses your systems", {"comp_health": -6, "xp": 1, "player_health": -6}),
    48: ("You unlock a wasteland server, gaining a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    49: ("A rigged node traps you in a datastream", {"comp_health": -5, "xp": 1, "player_health": -5}),
    50: ("You defeat a wasteland warlord, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    51: ("You hack a ruined terminal, gaining a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    52: ("A viral worm corrupts your implants", {"comp_health": -6, "xp": 1, "player_health": -6}),
    53: ("A wasteland turret locks onto you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    54: ("You dodge a scavenger bot, finding a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    55: ("Your signal jams, alerting raiders", {"score": 3 + player["level"], "xp": 5, "comp_health": -2, "player_health": -2}),
    56: ("You crash a wasteland server, snagging a Neon Key", {"score": 6 + player["level"], "neon_key": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    57: ("A glitch fries your ally’s systems", {"comp_health": -6, "xp": 1, "player_health": -6}),
    58: ("A rigged holo-trap zaps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    59: ("You raid a scavenger cache, securing a Nano Patch", {"score": 4 + player["level"], "nano_patch": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    60: ("A cyber-assassin strikes from the shadows", {"comp_health": -7, "xp": 1, "player_health": -7}),
    61: ("You hack a wasteland archive, earning a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    62: ("A rogue AI hacks your implants", {"comp_health": -6, "xp": 1, "player_health": -6}),
    63: ("You trade with a wasteland defector, gaining a Crypto Chip", {"score": 5 + player["level"], "crypto_chips": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    64: ("Your deal sparks a scavenger ambush", {"comp_health": -5, "xp": 1, "player_health": -5}),
    65: ("A glitch swarm overwhelms your defenses", {"comp_health": -2, "xp": 1, "player_health": -2}),
    66: ("You slice through a wasteland firewall, finding a Data Drive", {"score": 8 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    67: ("Your hack triggers a grid surge", {"comp_health": -6, "xp": 1, "player_health": -6}),
    68: ("A rigged node spikes your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    69: ("You tap a hidden datastream, gaining a Neon Key", {"score": 4 + player["level"], "neon_key": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
    70: ("A viral payload crashes your implants", {"comp_health": -7, "xp": 1, "player_health": -7}),
    71: ("You raid a wasteland server, securing a Crypto Chip", {"score": 7 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    72: ("You defeat a wasteland enforcer, claiming a Quantum Core", {"score": 5 + player["level"], "quantum_core": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    73: ("You broker a deal with a wasteland AI, gaining a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    74: ("You unlock a secure wasteland vault, finding a Data Drive", {"score": 6 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    75: ("A laser grid traps you in the wastelands", {"comp_health": -5, "xp": 1, "player_health": -5}),
    76: ("A hacked drone attacks you", {"comp_health": -6, "xp": 1, "player_health": -6}),
    77: ("You stabilize a glitched node, gaining a Crypto Chip", {"score": 6 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    78: ("A viral spike shorts your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    79: ("You bypass a wasteland trap, securing a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    80: ("You fry a wasteland rig, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    81: ("A wasteland defector betrays you", {"comp_health": -6, "xp": 1, "player_health": -6}),
    82: ("You hack a hidden terminal, uncovering a Data Drive", {"score": 8 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    83: ("Your signal draws a bounty hunter", {"comp_health": -7, "xp": 1, "player_health": -7}),
    84: ("A collapsing rig traps you", {"comp_health": -5, "xp": 1, "player_health": -5}),
    85: ("You gain a nomad’s trust, earning a Crypto Chip", {"score": 5 + player["level"], "crypto_chips": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    86: ("Your hack triggers a wasteland lockdown", {"comp_health": -6, "xp": 1, "player_health": -6}),
    87: ("You find a hidden wasteland cache, securing a Nano Patch", {"score": 6 + player["level"], "nano_patch": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    88: ("You take down a wasteland bot, gaining a Data Drive", {"score": 5 + player["level"], "data_drive": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    89: ("Your actions spark a scavenger alert", {"comp_health": -5, "xp": 1, "player_health": -5}),
    90: ("You override a wasteland grid, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    91: ("A trap exposes you to wasteland drones", {"comp_health": -6, "xp": 1, "player_health": -6}),
    92: ("A swarm of scavenger enforcers attacks", {"comp_health": -7, "xp": 1, "player_health": -7}),
    93: ("You barter with a wasteland trader, earning a Neon Key", {"score": 5 + player["level"], "neon_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    94: ("A glitch spike fries your systems", {"comp_health": -5, "xp": 1, "player_health": -5}),
    95: ("You slip through a wasteland net, finding a Crypto Chip", {"score": 8 + player["level"], "crypto_chips": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    96: ("You defeat a wasteland operative, securing a Data Drive", {"score": 6 + player["level"], "data_drive": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
    97: ("A wasteland AI curses your systems", {"comp_health": -6, "xp": 1, "player_health": -6}),
    98: ("You unlock a wasteland server, gaining a Nano Patch", {"score": 5 + player["level"], "nano_patch": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
    99: ("A rigged node traps you in a datastream", {"comp_health": -5, "xp": 1, "player_health": -5}),
    100: ("You defeat a wasteland boss, claiming a Quantum Core", {"score": 7 + player["level"], "quantum_core": 1, "xp": 10, "player_health": 4, "comp_health": 4})
}

    # Map path to outcomes dictionary
    outcomes_dict = {
        1: outcomes_neon_underdistrict,
        2: outcomes_corporate_skyspire,
        3: outcomes_data_vault,
        4: outcomes_grid_wastelands
    }
    outcomes = outcomes_dict.get(int(path), outcomes_neon_underdistrict)  # Default to Neon Underdistrict
    result, changes = outcomes.get(adjusted_outcome, ("No outcome defined for this path", {}))

    was_deactivated = current_companion["name"] in deactivated_companions

    # Apply player strength scaling for negative health changes
    strength_modifier = 1.5 - (player["player_strength"] / 15)  # Maps strength 5 -> 1.1667, 15 -> 0.5
    if "player_health" in changes and changes["player_health"] < 0:
        scaled_damage = round(changes["player_health"] * strength_modifier)
        changes["player_health"] = max(scaled_damage, -5)  # Cap max damage at -5
    if "comp_health" in changes and changes["comp_health"] < 0:
        scaled_damage = round(changes["comp_health"] * strength_modifier)
        changes["comp_health"] = max(scaled_damage, -5)  # Cap max damage at -5

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
        if "crypto_chips" in changes and changes["crypto_chips"] > 0:
            changes["crypto_chips"] += class_mod.get("crypto_boost", 0)
        if "nano_patch" in changes and changes["nano_patch"] > 0:
            changes["nano_patch"] += class_mod.get("nano_boost", 0)
        if "data_drive" in changes and changes["data_drive"] > 0:
            changes["data_drive"] += class_mod.get("hacking_boost", 0) + class_mod.get("advanced_tech_boost", 0)
        if "neon_key" in changes and changes["neon_key"] > 0:
            changes["neon_key"] += class_mod.get("tech_boost", 0)
        if "quantum_core" in changes and changes["quantum_core"] > 0:
            changes["quantum_core"] += class_mod.get("crypto_boost", 0)

    # Ensure health changes are capped
    changes["player_health"] = max(changes.get("player_health", 0), -100)
    changes["comp_health"] = max(changes.get("comp_health", 0), -100)

    # Cap companion health at 0-100 after applying changes
    if current_companion["name"]:
        current_companion["health"] = max(0, min(current_companion["health"] + changes.get("comp_health", 0), 100))
        companion_stats[current_companion["name"]]["health"] = current_companion["health"]
    else:
        changes["comp_health"] = 0  # No companion health change if no companion

    # Handle deactivated companion revival on positive outcomes
    if was_deactivated and is_positive_outcome(changes):
        changes["comp_health"] += 10  # +10 revival bonus plus +4 from outcome
        current_companion["health"] = max(0, min(current_companion["health"] + 10, 100))  # Cap at 0-100
        companion_stats[current_companion["name"]]["health"] = current_companion["health"]
        if current_companion["name"] in deactivated_companions:
            deactivated_companions.remove(current_companion["name"])
    
    return result, changes

def inventory():
    """Display and manage player's inventory."""
    global player, current_companion, stat_changes, quantum_core_active
    while True:
        clear_console()
        print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.GREEN + "NEON GRID RUNNER - D10+D10" + Style.RESET_ALL)
        print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.GREEN + get_random_ascii() + Style.RESET_ALL)
        print(Fore.GREEN + "\nDATA VAULT..." + Style.RESET_ALL)
        print(Fore.RED + f"Nano Patch ({player['nano_patch']}): Restores vitality..." + Style.RESET_ALL)
        print(Fore.YELLOW + f"Data Drive ({player['data_drive']}): Boosts credits..." + Style.RESET_ALL)
        print(Fore.CYAN + f"Neon Key ({player['neon_key']}): Unlocks crypto chips..." + Style.RESET_ALL)
        print(Fore.BLUE + f"Quantum Core ({player['quantum_core']}): Doubles score gains for the next event..." + Style.RESET_ALL)
        print(Fore.GREEN + "\nUSE AN ITEM..." + Style.RESET_ALL)
        print(Fore.GREEN + "1. Nano Patch (+25 player health, +20 companion health)" + Style.RESET_ALL)
        print(Fore.GREEN + "2. Data Drive (+20 score)" + Style.RESET_ALL)
        print(Fore.GREEN + "3. Neon Key (+4 crypto chips)" + Style.RESET_ALL)
        print(Fore.GREEN + "4. Quantum Core (Double score next event)" + Style.RESET_ALL)
        print(Fore.GREEN + "5. Return" + Style.RESET_ALL)
        inv_choice = input(Fore.GREEN + "\nSelect an item (1-5): " + Style.RESET_ALL).strip()
        if inv_choice not in ["1", "2", "3", "4", "5"]:
            stat_changes = "Invalid choice"
            print(Fore.GREEN + "\nINVALID CHOICE..." + Style.RESET_ALL)
            print(Fore.GREEN + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
            print(Fore.GREEN + "\nPress Enter to try again..." + Style.RESET_ALL)
            input()
            continue
        if inv_choice == "1":
            if player["nano_patch"] > 0:
                pre_player_health = player["health"]
                pre_comp_health = current_companion["health"] if current_companion["name"] else 0
                healing_boost = companion_class_modifiers.get(current_companion["class"], {}).get("healing_boost", 0)
                player["health"] = min(player["health"] + 25 + healing_boost, player["max_health"])
                if current_companion["name"]:
                    current_companion["health"] = max(0, min(current_companion["health"] + 20 + healing_boost, 100))
                    companion_stats[current_companion["name"]]["health"] = current_companion["health"]
                    if current_companion["health"] > 0 and current_companion["name"] in deactivated_companions:
                        deactivated_companions.remove(current_companion["name"])
                player["nano_patch"] -= 1
                if player["nano_patch"] < 0:
                    player["nano_patch"] = 0
                stat_changes = f"Health +{25 + healing_boost}, Companion Health +{20 + healing_boost}, Nano Patches -1"
                stat_changes += f", Total: Player [{pre_player_health} -> {player['health']}]"
                if current_companion["name"]:
                    stat_changes += f", Companion [{pre_comp_health} -> {current_companion['health']}]"
                print(Fore.GREEN + "\nNano Patch used - Vitality restored..." + Style.RESET_ALL)
            else:
                stat_changes = "No Nano Patches remain"
                print(Fore.GREEN + "\nNo Nano Patches remain..." + Style.RESET_ALL)
        elif inv_choice == "2":
            if player["data_drive"] > 0:
                score_boost = companion_class_modifiers.get(current_companion["class"], {}).get("score_boost", 0)
                player["score"] += 20 + score_boost
                player["data_drive"] -= 1
                stat_changes = f"Score +{20 + score_boost}, Data Drives -1"
                print(Fore.GREEN + "\nData Drive used - Credits gained..." + Style.RESET_ALL)
            else:
                stat_changes = "No Data Drives remain"
                print(Fore.GREEN + "\nNo Data Drives remain..." + Style.RESET_ALL)
        elif inv_choice == "3":
            if player["neon_key"] > 0:
                crypto_boost = companion_class_modifiers.get(current_companion["class"], {}).get("crypto_boost", 0)
                player["crypto_chips"] += 4 + crypto_boost
                player["neon_key"] -= 1
                stat_changes = f"Crypto Chips +{4 + crypto_boost}, Neon Keys -1"
                print(Fore.GREEN + "\nNeon Key used - Crypto chips unlocked..." + Style.RESET_ALL)
            else:
                stat_changes = "No Neon Keys remain"
                print(Fore.GREEN + "\nNo Neon Keys remain..." + Style.RESET_ALL)
        elif inv_choice == "4":
            if player["quantum_core"] > 0:
                player["quantum_core"] -= 1
                quantum_core_active = True
                stat_changes = "Quantum Core used - Score doubled for next event, Quantum Cores -1"
                print(Fore.GREEN + "\nQuantum Core used - Next event's score gains will be doubled..." + Style.RESET_ALL)
            else:
                stat_changes = "No Quantum Cores remain"
                print(Fore.GREEN + "\nNo Quantum Cores remain..." + Style.RESET_ALL)
        elif inv_choice == "5":
            return
        print(Fore.GREEN + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
        print(Fore.GREEN + "\nPress Enter to return..." + Style.RESET_ALL)
        input()

def companions_menu():
    """Display companions and their status."""
    global stat_changes
    clear_console()
    print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
    print(Fore.GREEN + "NEON GRID RUNNER - D10+D10" + Style.RESET_ALL)
    print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
    print(Fore.GREEN + get_random_ascii() + Style.RESET_ALL)
    print(Fore.GREEN + "\nCOMPANIONS LIST..." + Style.RESET_ALL)
    for name in companions:
        status = "(Deactivated)" if name in deactivated_companions else ""
        print(Fore.GREEN + f"{name} {status} - Class: {Fore.GREEN}{companion_stats[name]['class']}{Style.RESET_ALL}, Health: {Fore.RED}{companion_stats[name]['health']}{Style.RESET_ALL}, Strength: {Fore.WHITE}{companion_stats[name]['strength']}{Style.RESET_ALL}, Luck: {Fore.YELLOW}{companion_stats[name]['luck']}{Style.RESET_ALL}" + Style.RESET_ALL)
    print(Fore.GREEN + f"\nCurrent Companion: {current_companion['name']} ({current_companion['class']})" + Style.RESET_ALL)
    print(Fore.GREEN + "\nPress Enter to return..." + Style.RESET_ALL)
    stat_changes = "Viewed companions list"
    input()

def main():
    """Main game loop."""
    global player, current_companion, stat_changes, quantum_core_active, deactivated_companions, last_path_chosen, companion_stats
    # Reset all global states
    player.update({
        "score": 0,
        "health": 100,
        "max_health": 200,
        "crypto_chips": 0,
        "nano_patch": 0,
        "data_drive": 0,
        "neon_key": 0,
        "quantum_core": 0,
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
    deactivated_companions.clear()
    quantum_core_active = False
    stat_changes = ""
    last_path_chosen = None

    # Reinitialize companion stats
    companion_stats.clear()
    companion_stats.update({
        name: {
            "health": max(0, min(secrets.randbelow(50) + 50, 100)),
            "strength": secrets.randbelow(10) + 5,
            "luck": secrets.randbelow(10) + 1,
            "class": secrets.choice(companion_classes)
        } for name in companions
    })

    # Assign a new random companion at start
    companion_name = secrets.choice(companions)
    current_companion.update({
        "name": companion_name,
        "health": max(0, min(companion_stats[companion_name]["health"], 100)),
        "strength": companion_stats[companion_name]["strength"],
        "luck": companion_stats[companion_name]["luck"],
        "class": companion_stats[companion_name]["class"]
    })
    companion_stats[companion_name]["health"] = current_companion["health"]

    clear_console()
    print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
    print(Fore.GREEN + "NEON GRID RUNNER - D10+D10" + Style.RESET_ALL)
    print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
    print(Fore.GREEN + get_random_ascii() + Style.RESET_ALL)
    print(Fore.GREEN + "NEON GRID RUNNER" + Style.RESET_ALL)
    print(Fore.GREEN + "CONQUER THE CYBER GRID" + Style.RESET_ALL)
    print(Fore.GREEN + f"\nCompanion: {Fore.GREEN}{current_companion['name']} ({current_companion['class']}) joins you in the grid..." + Style.RESET_ALL)
    print(Fore.GREEN + "\n\n        Press Enter to Hack in" + Style.RESET_ALL)
    print(Fore.GREEN + "    Cyber Grid Nexus..." + Style.RESET_ALL)
    input()

    while True:
        clear_console()
        # Initialize display variables only when needed
        show_health_change = False
        pre_player_health = player["health"]
        pre_comp_health = current_companion["health"] if current_companion["name"] else 0

        print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.GREEN + "NEON GRID RUNNER - D10+D10" + Style.RESET_ALL)
        print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.GREEN + get_random_ascii() + Style.RESET_ALL)
        print(Fore.GREEN + "\nNAVIGATING THE CYBER GRID..." + Style.RESET_ALL)
        print(Fore.WHITE + f"Strength: {player['player_strength']}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Level: {player['level']} (XP: {player['xp']}/{player['xp_needed']})" + Style.RESET_ALL)
        print(Fore.RED + f"Health: {player['health']}" + Style.RESET_ALL + Fore.YELLOW + f"  Score: {player['score']}" + Style.RESET_ALL + Fore.CYAN + f"  Crypto Chips: {player['crypto_chips']}" + Style.RESET_ALL + Fore.BLUE + f"  Quantum Cores: {player['quantum_core']}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Progress: Score {player['score']}/6000 Crypto Chips {player['crypto_chips']}/300 Quantum Cores {player['quantum_core']}/50" + Style.RESET_ALL)
        if current_companion["name"]:
            print(Fore.GREEN + f"\nCompanion: {Fore.GREEN}{current_companion['name']} ({current_companion['class']}{Style.RESET_ALL}) (Health: {Fore.RED}{current_companion['health']}{Style.RESET_ALL}, Strength: {Fore.WHITE}{current_companion['strength']}{Style.RESET_ALL}, Luck: {Fore.YELLOW}{current_companion['luck']}{Style.RESET_ALL})" + Style.RESET_ALL)
        if stat_changes:
            print(Fore.GREEN + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
        print(Fore.GREEN + "\nPath Chosen:" + Style.RESET_ALL)
        print(get_path_dial())

        # Check win condition
        if player["score"] >= 6000 and player["crypto_chips"] >= 300 and player["quantum_core"] >= 50:
            clear_console()
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + "NEON GRID RUNNER - VICTORY" + Style.RESET_ALL)
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + get_random_ascii() + Style.RESET_ALL)
            print(Fore.GREEN + "\nVICTORY! YOU HAVE CONQUERED THE CYBER GRID!" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Final Crypto Chips: {player['crypto_chips']}" + Style.RESET_ALL)
            print(Fore.BLUE + f"Final Quantum Cores: {player['quantum_core']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Level: {player['level']}" + Style.RESET_ALL)
            print(Fore.RED + f"Final Health: {player['health']}/{player['max_health']}" + Style.RESET_ALL)
            print(Fore.WHITE + f"Final Strength: {player['player_strength']}" + Style.RESET_ALL)
            print(Fore.GREEN + "\nYour legend will echo through the grid..." + Style.RESET_ALL)
            print(Fore.GREEN + "\nPress Enter to exit..." + Style.RESET_ALL)
            log_event("Game won")
            input()
            break

        # Check loss condition
        if player["health"] <= 0:
            clear_console()
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + "NEON GRID RUNNER - DEFEAT" + Style.RESET_ALL)
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + get_random_ascii() + Style.RESET_ALL)
            print(Fore.RED + "\nDEFEAT! The Cyber Grid has fried your neural link..." + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Final Crypto Chips: {player['crypto_chips']}" + Style.RESET_ALL)
            print(Fore.BLUE + f"Final Quantum Cores: {player['quantum_core']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Level: {player['level']}" + Style.RESET_ALL)
            print(Fore.RED + f"Final Health: {player['health']}/{player['max_health']}" + Style.RESET_ALL)
            print(Fore.WHITE + f"Final Strength: {player['player_strength']}" + Style.RESET_ALL)
            print(Fore.GREEN + "\nYour run ends here..." + Style.RESET_ALL)
            print(Fore.GREEN + "\nPress Enter to exit..." + Style.RESET_ALL)
            log_event("Game lost")
            input()
            break

        print(Fore.GREEN + "\nCHOOSE YOUR PATH..." + Style.RESET_ALL)
        print(Fore.GREEN + "1. Neon Underdistrict" + Style.RESET_ALL)
        print(Fore.GREEN + "2. Corporate Skyspire" + Style.RESET_ALL)
        print(Fore.GREEN + "3. Data Vault" + Style.RESET_ALL)
        print(Fore.GREEN + "4. Grid Wastelands" + Style.RESET_ALL)
        print(Fore.GREEN + "5. Inventory" + Style.RESET_ALL)
        print(Fore.GREEN + "6. Companions" + Style.RESET_ALL)
        print(Fore.GREEN + "7. Save Game" + Style.RESET_ALL)
        print(Fore.GREEN + "8. Load Game" + Style.RESET_ALL)
        print(Fore.GREEN + "9. Exit" + Style.RESET_ALL)
        choice = input(Fore.GREEN + "\nSelect a path (1-9): " + Style.RESET_ALL).strip()

        if choice in ["1", "2", "3", "4"]:
            try:
                last_path_chosen = choice
                pre_player_health = player["health"]
                pre_comp_health = current_companion["health"] if current_companion["name"] else 0

                # Select a random companion, including deactivated ones
                companion_name = secrets.choice(companions)  # Include all companions, even deactivated
                current_companion.update({
                    "name": companion_name,
                    "health": max(0, min(companion_stats[companion_name]["health"], 100)),
                    "strength": companion_stats[companion_name]["strength"],
                    "luck": companion_stats[companion_name]["luck"],
                    "class": companion_stats[companion_name]["class"]
                })
                companion_stats[companion_name]["health"] = current_companion["health"]
                pre_comp_health = current_companion["health"]

                die1, die2, outcome, adjusted_outcome = roll_dice()
                result, changes = path_outcomes(int(choice), adjusted_outcome)
                was_deactivated = current_companion["name"] in deactivated_companions if current_companion["name"] else False
                if current_companion["name"]:
                    print(Fore.GREEN + f"\n{current_companion['name']} ({current_companion['class']}{Style.RESET_ALL}) {'(Deactivated) ' if was_deactivated else ''}joins you for this run..." + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + "\nNo companion joins you for this run..." + Style.RESET_ALL)
                print(Fore.GREEN + f"\nDice Roll: D10={die1}, D10={die2}, Outcome={outcome}, Adjusted={adjusted_outcome}" + Style.RESET_ALL)
                print(Fore.GREEN + f"\nResult: {result}" + Style.RESET_ALL)

                # Apply quantum core effect
                quantum_core_message = ""
                if quantum_core_active and "score" in changes and changes["score"] > 0:
                    changes["score"] *= 2
                    quantum_core_message = "Score doubled by Quantum Core"
                    quantum_core_active = False
                elif quantum_core_active and ("score" not in changes or changes["score"] <= 0):
                    changes["score"] = changes.get("score", 0) + 5
                    quantum_core_message = "No score gain, +5 score from Quantum Core"
                    quantum_core_active = False

                # Apply changes
                score_change = changes.get("score", 0)
                player["score"] = max(0, player["score"] + score_change)
                player_health_change = changes.get("player_health", 0)
                player["health"] = max(0, min(player["health"] + player_health_change, player["max_health"]))
                comp_health_change = changes.get("comp_health", 0) if current_companion["name"] else 0
                revival_health_change = 0
                if was_deactivated and is_positive_outcome(changes) and current_companion["name"]:
                    revival_health_change = 10  # Track revival bonus separately
                if current_companion["name"]:
                    current_companion["health"] = max(0, min(current_companion["health"] + comp_health_change, 100))
                    companion_stats[current_companion["name"]]["health"] = current_companion["health"]
                    if current_companion["health"] <= 0 and current_companion["name"] not in deactivated_companions:
                        deactivated_companions.append(current_companion["name"])
                crypto_change = changes.get("crypto_chips", 0)
                player["crypto_chips"] = max(0, player["crypto_chips"] + crypto_change)
                drive_change = changes.get("data_drive", 0)
                player["data_drive"] = max(0, player["data_drive"] + drive_change)
                core_change = changes.get("quantum_core", 0)
                player["quantum_core"] = max(0, player["quantum_core"] + core_change)
                patch_change = changes.get("nano_patch", 0)
                player["nano_patch"] = max(0, player["nano_patch"] + patch_change)
                key_change = changes.get("neon_key", 0)
                player["neon_key"] = max(0, player["neon_key"] + key_change)
                xp_change = changes.get("xp", 0)
                levelup_health_change = level_check(xp_change)
                post_player_health = player["health"]
                post_comp_health = current_companion["health"] if current_companion["name"] else 0

                # Build stat changes message with colors
                stat_changes_list = []
                if score_change != 0:
                    stat_changes_list.append(Fore.YELLOW + f"Score {'+' if score_change > 0 else ''}{score_change}" + Style.RESET_ALL)
                if quantum_core_message:
                    stat_changes_list.append(Fore.BLUE + quantum_core_message + Style.RESET_ALL)
                if was_deactivated and is_positive_outcome(changes) and current_companion["name"]:
                    stat_changes_list.append(Fore.GREEN + f"{current_companion['name']} revived with +10 health" + Style.RESET_ALL)
                if player_health_change != 0 or levelup_health_change != 0 or comp_health_change != 0:
                    total_health_change = player_health_change + levelup_health_change
                    stat_changes_list.append(Fore.RED + f"Health {'+' if total_health_change > 0 else ''}{total_health_change}" + Style.RESET_ALL)
                    show_health_change = True
                if show_health_change or player_health_change != 0 or comp_health_change != 0:
                    health_display = f"Total: Player [{pre_player_health} -> {post_player_health}]"
                    if current_companion["name"]:
                        health_display += f", Companion [{pre_comp_health} -> {post_comp_health}]"
                    stat_changes_list.append(Fore.RED + health_display + Style.RESET_ALL)
                if crypto_change != 0:
                    stat_changes_list.append(Fore.CYAN + f"Crypto Chips {'+' if crypto_change > 0 else ''}{crypto_change}" + Style.RESET_ALL)
                if drive_change != 0:
                    stat_changes_list.append(Fore.YELLOW + f"Data Drives {'+' if drive_change > 0 else ''}{drive_change}" + Style.RESET_ALL)
                if core_change != 0:
                    stat_changes_list.append(Fore.BLUE + f"Quantum Cores {'+' if core_change > 0 else ''}{core_change}" + Style.RESET_ALL)
                if patch_change != 0:
                    stat_changes_list.append(Fore.RED + f"Nano Patches {'+' if patch_change > 0 else ''}{patch_change}" + Style.RESET_ALL)
                if key_change != 0:
                    stat_changes_list.append(Fore.CYAN + f"Neon Keys {'+' if key_change > 0 else ''}{key_change}" + Style.RESET_ALL)
                if xp_change != 0:
                    stat_changes_list.append(Fore.GREEN + f"XP +{xp_change}" + Style.RESET_ALL)
                if comp_health_change != 0 and current_companion["name"] and not (was_deactivated and is_positive_outcome(changes)):
                    stat_changes_list.append(Fore.RED + f"{current_companion['name']}'s Health {'+' if comp_health_change > 0 else ''}{comp_health_change}" + Style.RESET_ALL)
                stat_changes = ", ".join(stat_changes_list) if stat_changes_list else "No changes"

                print(Fore.GREEN + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
                print(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)
                input()
            except Exception as e:
                stat_changes = f"Error in path selection: {str(e)}"
                print(Fore.RED + f"Error in path selection: {str(e)}" + Style.RESET_ALL)
                print(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)
                input()
        elif choice == "5":
            inventory()
        elif choice == "6":
            companions_menu()
        elif choice == "7":
            save_game()
            print(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)
            input()
        elif choice == "8":
            load_game()
            print(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)
            input()
        elif choice == "9":
            clear_console()
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + "NEON GRID RUNNER - EXIT" + Style.RESET_ALL)
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + get_random_ascii() + Style.RESET_ALL)
            print(Fore.GREEN + "\nLogging out of the Cyber Grid..." + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Final Crypto Chips: {player['crypto_chips']}" + Style.RESET_ALL)
            print(Fore.BLUE + f"Final Quantum Cores: {player['quantum_core']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Level: {player['level']}" + Style.RESET_ALL)
            print(Fore.RED + f"Final Health: {player['health']}/{player['max_health']}" + Style.RESET_ALL)
            print(Fore.WHITE + f"Final Strength: {player['player_strength']}" + Style.RESET_ALL)
            print(Fore.GREEN + "\nPress Enter to exit..." + Style.RESET_ALL)
            log_event("Game quit")
            input()
            break
        else:
            stat_changes = "Invalid choice"
            print(Fore.GREEN + "\nINVALID CHOICE..." + Style.RESET_ALL)
            print(Fore.GREEN + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
            print(Fore.GREEN + "\nPress Enter to try again..." + Style.RESET_ALL)
            input()

if __name__ == "__main__":
    main()