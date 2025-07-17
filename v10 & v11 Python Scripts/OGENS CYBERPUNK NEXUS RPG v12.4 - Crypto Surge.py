import pygame
from colorama import init, Fore, Style
import os
import secrets
import json
from datetime import datetime
import sys
import platform

# Initialize colorama for Windows compatibility
init(autoreset=True, convert=True, strip=False, wrap=True)

# Handle resource paths for PyInstaller
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Initialize Pygame mixer for audio with fallback
pygame_initialized = False
try:
    pygame.mixer.init()
    pygame_initialized = True
except pygame.error as e:
    print(Fore.RED + f"Failed to initialize audio mixer: {str(e)}. Continuing without audio." + Style.RESET_ALL)

# Define path to background music in the 'sounds' folder
SOUNDS_DIR = "sounds"
BACKGROUND_MUSIC = resource_path(os.path.join(SOUNDS_DIR, "background_music.ogg"))

# Check if music file exists and load/play it with fallback
if pygame_initialized and os.path.exists(BACKGROUND_MUSIC):
    try:
        pygame.mixer.music.load(BACKGROUND_MUSIC)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(Fore.RED + f"Failed to load music: {str(e)}. Continuing without music." + Style.RESET_ALL)
else:
    print(Fore.RED + "Warning: background_music.ogg not found in sounds folder or Pygame not initialized! Continuing without music." + Style.RESET_ALL)

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
    "crypto_surge": 0,
    "crypto_surge_events": 0,
    "player_strength": secrets.randbelow(10) + 5,
    "level": 1,
    "xp": 0,
    "xp_needed": 50,
    "credits": 100
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
    "health": min(secrets.randbelow(50) + 50, 100),
    "strength": secrets.randbelow(10) + 5,
    "class": secrets.choice(companion_classes)
} for name in companions}

# Track deactivated companions
deactivated_companions = []

# Current companion
current_companion = {
    "name": "",
    "health": 0,
    "strength": 0,
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
    ╔══════[🪐]══════╗
    ║ 🌇 * | * * | * ⇓ ║
    ║ * * | *🗽* | * * ║
    ║ ↯ * | * * | * ⚡ ║
    ║ * * | * * | * * ║
    ╚══════[🌐]══════╝
    """,
    """
    ╔══════[📡]══════╗
    ║ ⇓ * | * * | * ~ ║
    ║ * * | *⚡* | * * ║
    ║ 🌞 * | * * | * ↯ ║
    ║ * * | * * | * * ║
    ╚══════[🌎]══════╝
    """,
    """
    ╔═════[🕸️]═════╗
    ║ ~ * | * * | * 🌗 ║
    ║ * * | *🌉* | * * ║
    ║ ↯ * | * * | * ⇓ ║
    ║ * * | * * | * * ║
    ╚═════[🪬]═════╝
    """,
    """
    ╔══════[📡]══════╗
    ║ ⚙ * | * * | * ↯ ║
    ║ * * | *🌃* | * * ║
    ║ ⇓ * | * * | * ~ ║
    ║ * * | * * | * * ║
    ╚══════[🌌]══════╝
    """,
    """
    ╔═════[🧬]═════╗
    ║ ↯ * | * * | * ⇓ ║
    ║ * * | *🌅* | * * ║
    ║ ~ * | * * | * ⚙ ║
    ║ * * | * * | * * ║
    ╚═════[🖲️]═════╝
    """,
    """
    ╔══════[🪙]══════╗
    ║ ⇓ * | * * | * 🤖 ║
    ║ * * | *🛸* | * * ║
    ║ ↯ * | * * | * ~ ║
    ║ * * | * * | * * ║
    ╚══════[⚡]══════╝
    """,
    """
    ╔══════[☄️]══════╗
    ║ ~ * | * * | * ↯ ║
    ║ * * | *🏛️* | * * ║
    ║ 🏍️ * | * * | * ⇓ ║
    ║ * * | * * | * * ║
    ╚══════[🌚]══════╝
    """,
    """
    ╔═════[🪬]═════╗
    ║ 🧮 * | * * | * ~ ║
    ║ * * | *🏙️* | * * ║
    ║ ⇓ * | * * | * ↯ ║
    ║ * * | * * | * * ║
    ╚═════[🕸️]═════╝
    """
]

def clear_console():
    """Clear the console in a cross-platform way."""
    try:
        os.system("cls" if platform.system() == "Windows" else "clear")
    except Exception as e:
        print(Fore.GREEN + f"Failed to clear console: {str(e)}" + Style.RESET_ALL)

from colorama import Fore, Style

def get_path_dial(last_path_chosen):
    """Generate a cyberpunk-themed ASCII neon grid with blue structure, light blue numbers, and the last chosen path in magenta. Emojis remain uncolored."""
    dial_lines = [
        "     ☽≣≣≣≣≣☾     ",
        "   |  ⌁ 1 🌃    ",
        "☽≣≣≣==≣≣≣==≣≣≣☾",
        "| 4 🖥️  📱 2 | ",
        "☽≣≣≣==≣≣≣==≣≣≣☾",
        "   |  ↯ 3 💾    ",
        "     ☽≣≣≣≣≣☾     "
    ]
    colored_dial = []
    for line in dial_lines:
        new_line = line
        for i in range(1, 5):
            path_num = str(i)
            if path_num in line:
                try:
                    if last_path_chosen is not None and path_num == str(last_path_chosen):
                        new_line = new_line.replace(path_num, f"{Fore.MAGENTA}{path_num}{Style.RESET_ALL}")
                    else:
                        new_line = new_line.replace(path_num, f"{Fore.LIGHTCYAN_EX}{path_num}{Style.RESET_ALL}")
                except:
                    new_line = new_line.replace(path_num, path_num)
        try:
            colored_line = f"{Fore.BLUE}{new_line}{Style.RESET_ALL}"
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
        "player": {k: int(v) if isinstance(v, (int, float)) else str(v) for k, v in player.items()},
        "companion_stats": {
            name: {k: int(v) if isinstance(v, (int, float)) else str(v) for k, v in stats.items()}
            for name, stats in companion_stats.items()
        },
        "current_companion": {k: int(v) if isinstance(v, (int, float)) else str(v) for k, v in current_companion.items()},
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
            "crypto_surge": 0, "crypto_surge_events": 0,
            "player_strength": secrets.randbelow(10) + 5, "level": 1, "xp": 0, "xp_needed": 50,
            "credits": 100
        }
        for key in default_player:
            if key in game_state.get("player", {}):
                player[key] = int(game_state["player"][key]) if key in [
                    "score", "health", "max_health", "crypto_chips", "nano_patch",
                    "data_drive", "neon_key", "quantum_core", "crypto_surge",
                    "crypto_surge_events", "player_strength", "level", "xp", "xp_needed", "credits"
                ] else game_state["player"][key]
            else:
                player[key] = default_player[key]
        
        companion_stats.clear()
        companion_stats.update({
            name: {
                "health": max(0, min(secrets.randbelow(50) + 50, 100)),
                "strength": secrets.randbelow(10) + 5,
                "class": secrets.choice(companion_classes)
            } for name in companions
        })
        for name, stats in game_state.get("companion_stats", {}).items():
            if name in companion_stats:
                companion_stats[name]["health"] = max(0, min(int(stats.get("health", companion_stats[name]["health"])), 100))
                companion_stats[name]["strength"] = int(stats.get("strength", companion_stats[name]["strength"]))
                companion_stats[name]["class"] = stats.get("class", companion_stats[name]["class"])
        
        current_companion_data = game_state.get("current_companion", {})
        companion_name = current_companion_data.get("name", "")
        available_companions = [name for name in companions if name not in game_state.get("deactivated_companions", [])]
        
        if companion_name in companion_stats and companion_name not in game_state.get("deactivated_companions", []):
            current_companion.update({
                "name": companion_name,
                "health": max(0, min(int(current_companion_data.get("health", companion_stats[companion_name]["health"])), 100)),
                "strength": int(current_companion_data.get("strength", companion_stats[companion_name]["strength"])),
                "class": current_companion_data.get("class", companion_stats[companion_name]["class"])
            })
            companion_stats[companion_name]["health"] = current_companion["health"]
        else:
            # Select a new valid companion if saved companion is invalid or deactivated
            if not available_companions:
                deactivated_companions.clear()
                available_companions = companions.copy()
                stat_changes = "All companions were deactivated; resetting companion list."
                print(Fore.RED + "Warning: All companions were deactivated. Resetting companion list." + Style.RESET_ALL)
            try:
                companion_name = secrets.choice(available_companions)
                current_companion.update({
                    "name": companion_name,
                    "health": max(0, min(companion_stats[companion_name]["health"], 100)),
                    "strength": companion_stats[companion_name]["strength"],
                    "class": companion_stats[companion_name]["class"]
                })
                companion_stats[companion_name]["health"] = current_companion["health"]
                stat_changes = f"Loaded companion {companion_name} ({current_companion['class']}) assigned."
            except Exception as e:
                stat_changes = f"Error assigning companion: {str(e)}. Starting without companion."
                print(Fore.RED + stat_changes + Style.RESET_ALL)
                current_companion.update({
                    "name": "",
                    "health": 0,
                    "strength": 0,
                    "class": ""
                })
        
        deactivated_companions.clear()
        deactivated_companions.extend(game_state.get("deactivated_companions", []))
        
        stat_changes = "Data restored from the grid"
        print(Fore.GREEN + "The grid restores your data!" + Style.RESET_ALL)
    except Exception as e:
        stat_changes = f"Failed to load data: {str(e)}"
        print(Fore.GREEN + f"Failed to load data... Error: {str(e)}" + Style.RESET_ALL)
    return stat_changes

def roll_dice():
    """Roll two D10s to produce outcomes 1-100 using grid logic: (D10-1)*10 + D10."""
    die1 = secrets.randbelow(10) + 1
    die2 = secrets.randbelow(10) + 1
    outcome = (die1 - 1) * 10 + die2
    return die1, die2, outcome

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
             changes.get("score", 0) > 0 or
             changes.get("credits", 0) > 0))

def path_outcomes(path, outcome):
    global player, current_companion, stat_changes, quantum_core_active
    if not (1 <= outcome <= 100):
        raise ValueError(f"Invalid outcome {outcome}; must be between 1 and 100")

    outcomes_neon_underdistrict = {
        1: ("Evaded a gang patrol, snagged some credits!", {"credits": 30, "xp": 10}),
        2: ("Found a discarded Nano Patch in an alley!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        3: ("Hacked a street sign, boosted your score!", {"score": secrets.randbelow(10) + 10, "xp": 12, "credits": 10}),  # 10-19
        4: ("Traded with a runner, earned crypto chips!", {"crypto_chips": 2, "xp": 10, "credits": 10}),
        5: ("Scavenged a Neon Key from a hideout!", {"neon_key": 1, "xp": 8, "credits": 10}),
        6: ("Dodged a trap, sharpened your skills!", {"xp": 10, "player_health": 2, "credits": 10}),  # Halved from 5
        7: ("Picked up a Data Drive from debris!", {"data_drive": 1, "xp": 8, "credits": 10}),
        8: ("Quick hack paid off with credits!", {"credits": 25, "xp": 10}),
        9: ("Gang scuffle left you bruised!", {"player_health": -5, "comp_health": -5, "xp": 1}),
        10: ("Found a Quantum Core in a dumpster!", {"quantum_core": 1, "xp": 10, "credits": 10}),
        11: ("Struck a deal, gained crypto chips!", {"crypto_chips": 2, "xp": 10, "credits": 10}),
        12: ("Street medkit patched you up!", {"player_health": 5, "comp_health": 5, "xp": 8, "credits": 10}),  # Halved from 10
        13: ("Outran a drone, gained experience!", {"xp": 8, "credits": 10}),
        14: ("Courier job brought in credits!", {"credits": 20, "xp": 10}),
        15: ("Found a hidden Data Drive!", {"data_drive": 1, "xp": 8, "credits": 10}),
        16: ("Hacked a vendor, scored points!", {"score": secrets.randbelow(10) + 10, "xp": 10, "credits": 10}),  # 10-19
        17: ("Unearthed a Neon Key in the shadows!", {"neon_key": 1, "xp": 8, "credits": 10}),
        18: ("Gang ambush caught you off guard!", {"player_health": -6, "comp_health": -6, "xp": 1}),
        19: ("Won a street fight, earned credits!", {"credits": 35, "xp": 10}),
        20: ("Snagged a Nano Patch from a thug!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        21: ("Hacked a node, gained crypto chips!", {"crypto_chips": 3, "xp": 10, "credits": 10}),
        22: ("Found a Data Drive in a crate!", {"data_drive": 1, "xp": 8, "credits": 10}),
        23: ("Slipped past a patrol, gained XP!", {"xp": 12, "credits": 10}),
        24: ("Traded for credits in the market!", {"credits": 40, "xp": 10}),
        25: ("Picked up a Neon Key in the chaos!", {"neon_key": 1, "xp": 8, "credits": 10}),
        26: ("Hacked a terminal, boosted score!", {"score": secrets.randbelow(10) + 15, "xp": 10, "credits": 10}),  # 15-24
        27: ("Gang attack left you battered!", {"player_health": -7, "comp_health": -7, "xp": 1}),
        28: ("Heist paid off with credits!", {"credits": 45, "xp": 10}),
        29: ("Found crypto chips in a stash!", {"crypto_chips": 3, "xp": 10, "credits": 10}),
        30: ("Learned street smarts, gained XP!", {"xp": 15, "credits": 10}),
        31: ("Scavenged a Nano Patch!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        32: ("Traded for a Data Drive!", {"data_drive": 1, "xp": 8, "credits": 10}),
        33: ("Job brought in big credits!", {"credits": 50, "xp": 10}),
        34: ("Found a Neon Key in a dark alley!", {"neon_key": 1, "xp": 8, "credits": 10}),
        35: ("Gang fight took a toll!", {"player_health": -8, "comp_health": -8, "xp": 1}),
        36: ("Hacked a system, scored big!", {"score": secrets.randbelow(10) + 15, "xp": 10, "credits": 10}),  # 15-24
        37: ("Deal netted crypto chips!", {"crypto_chips": 4, "xp": 10, "credits": 10}),
        38: ("Found a Nano Patch in a hideout!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        39: ("Dodged a trap, patched up!", {"player_health": 2, "comp_health": 2, "xp": 8, "credits": 10}),  # Halved from 5
        40: ("Overcame a challenge, gained XP!", {"xp": 18, "credits": 10}),
        41: ("Traded for a stack of credits!", {"credits": 55, "xp": 10}),
        42: ("Scored a Quantum Core in a raid!", {"quantum_core": 1, "xp": 10, "credits": 10}),
        43: ("Hacked a drone, boosted score!", {"score": secrets.randbelow(10) + 20, "xp": 10, "credits": 10}),  # 20-29
        44: ("Found a Neon Key in a dump!", {"neon_key": 1, "xp": 8, "credits": 10}),
        45: ("Gang ambush hit hard!", {"player_health": -9, "comp_health": -9, "xp": 1}),
        46: ("Hacked a system, earned credits!", {"credits": 60, "xp": 10}),
        47: ("Won a fight, gained crypto chips!", {"crypto_chips": 4, "xp": 10, "credits": 10}),
        48: ("Found a Nano Patch in a crate!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        49: ("Dodged a trap, health restored!", {"player_health": 3, "comp_health": 3, "xp": 8, "credits": 10}),  # Halved from 6
        50: ("Crypto Surge found! (Doubles credits for 2 events)", {"crypto_surge": 1, "credits": -10, "xp": 10}),
        51: ("Mugged by street rats!", {"player_health": -10, "comp_health": -10, "xp": 1}),
        52: ("Thief swiped your credits!", {"credits": -12, "xp": 1}),
        53: ("Companion caught in a fight!", {"comp_health": -10, "xp": 1}),
        54: ("Failed hack cost you credits!", {"credits": -7, "xp": 1}),
        55: ("Gang trap hit you hard!", {"player_health": -11, "comp_health": -11, "xp": 1}),
        56: ("Bad deal cost you credits!", {"credits": -15, "xp": 1}),
        57: ("Companion badly hurt!", {"comp_health": -12, "xp": 1}),
        58: ("Grid virus zapped you!", {"player_health": -12, "comp_health": -12, "xp": 1}),
        59: ("Lost crypto chips to a thief!", {"score": 5, "xp": 1}),
        60: ("Ambushed, took a beating!", {"player_health": -13, "comp_health": -13, "xp": 1}),
        61: ("Scammed, lost credits!", {"credits": -17, "xp": 1}),
        62: ("Companion injured in a brawl!", {"comp_health": -13, "xp": 1}),
        63: ("Hack attempt failed spectacularly!", {"player_health": -14, "comp_health": -14, "xp": 1}),
        64: ("Credits stolen in a heist!", {"credits": -20, "xp": 1}),
        65: ("Companion hurt in an ambush!", {"comp_health": -14, "xp": 1}),
        66: ("Grid interference drained vitality!", {"player_health": -15, "comp_health": -15, "xp": 1}),
        67: ("Lost credits in a street fight!", {"credits": -10, "xp": 1}),
        68: ("Gang took your credits!", {"credits": -22, "xp": 1}),
        69: ("Companion severely injured!", {"comp_health": -15, "xp": 1}),
        70: ("Deal gone wrong, lost credits!", {"credits": -25, "xp": 1}),
        71: ("Gang attack hit hard!", {"player_health": -16, "comp_health": -16, "xp": 1}),
        72: ("Trap cost you credits!", {"credits": -12, "xp": 1}),
        73: ("Companion took a bad hit!", {"comp_health": -16, "xp": 1}),
        74: ("Grid virus spread, big damage!", {"player_health": -17, "comp_health": -17, "xp": 1}),
        75: ("Heist wiped out your credits!", {"credits": -27, "xp": 1}),
        76: ("Companion nearly out of action!", {"comp_health": -17, "xp": 1}),
        77: ("Severe gang assault!", {"player_health": -18, "comp_health": -18, "xp": 1}),
        78: ("Lost credits in a scam!", {"credits": -15, "xp": 1}),
        79: ("Companion critically wounded!", {"comp_health": -18, "xp": 1}),
        80: ("Ambush took down companion!", {"comp_health": -19, "xp": 1}),
        81: ("Gang assault crushed you!", {"player_health": -19, "comp_health": -19, "xp": 1}),
        82: ("Fight drained your credits!", {"credits": -30, "xp": 1}),
        83: ("Companion hurt badly!", {"comp_health": -20, "xp": 1}),
        84: ("Grid virus outbreak, heavy damage!", {"player_health": -20, "comp_health": -20, "xp": 1}),
        85: ("Scam cost you credits!", {"credits": -17, "xp": 1}),
        86: ("Companion down for the count!", {"comp_health": -21, "xp": 1}),
        87: ("Major gang attack!", {"player_health": -21, "comp_health": -21, "xp": 1}),
        88: ("Credits completely wiped out!", {"credits": -50, "xp": 1}),
        89: ("Companion in critical failure!", {"comp_health": -22, "xp": 1}),
        90: ("Grid virus surge, severe damage!", {"player_health": -22, "comp_health": -22, "xp": 1}),
        91: ("Gang wipeout, heavy losses!", {"player_health": -23, "comp_health": -23, "xp": 1}),
        92: ("Lost credits and health!", {"credits": -20, "player_health": -24, "comp_health": -24, "xp": 1}),
        93: ("Companion lost, critical injury!", {"comp_health": -24, "player_health": -25, "xp": 1}),
        94: ("Grid collapse, vitality drained!", {"player_health": -26, "comp_health": -26, "xp": 1}),
        95: ("Gang massacre, critical hit!", {"player_health": -27, "comp_health": -25, "xp": 1}),
        96: ("Lost credits in a brutal fight!", {"credits": -25, "player_health": -28, "comp_health": -28, "xp": 1}),
        97: ("Companion gone, severe loss!", {"comp_health": -26, "player_health": -29, "xp": 1}),
        98: ("Grid overload, near fatal!", {"player_health": -30, "comp_health": -30, "xp": 1}),
        99: ("Gang annihilation, critical failure!", {"player_health": -31, "comp_health": -27, "xp": 1}),
        100: ("Total grid failure, heavy credit loss!", {"credits": -25, "player_health": -50, "comp_health": -30, "xp": 1})
    }

    outcomes_corporate_skyspire = {
        1: ("Bypassed security, scored credits!", {"credits": 35, "xp": 10}),
        2: ("Found a Nano Patch in an office!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        3: ("Hacked a corporate terminal, big score!", {"score": secrets.randbelow(10) + 15, "xp": 12, "credits": 10}),  # 15-24
        4: ("Negotiated a deal, gained crypto chips!", {"crypto_chips": 3, "xp": 10, "credits": 10}),
        5: ("Found a Neon Key in a vault!", {"neon_key": 1, "xp": 8, "credits": 10}),
        6: ("Evaded drones, gained vitality!", {"player_health": 3, "comp_health": 3, "xp": 8, "credits": 10}),  # Halved from 6
        7: ("Snagged a Data Drive from a desk!", {"data_drive": 1, "xp": 8, "credits": 10}),
        8: ("Quick hack netted credits!", {"credits": 30, "xp": 10}),
        9: ("Security bot zapped you!", {"player_health": -6, "comp_health": -6, "xp": 1}),
        10: ("Found a Quantum Core in a lab!", {"quantum_core": 1, "xp": 10, "credits": 10}),
        11: ("Deal brought crypto chips!", {"crypto_chips": 2, "xp": 10, "credits": 10}),
        12: ("Corporate medkit restored health!", {"player_health": 6, "comp_health": 6, "xp": 8, "credits": 10}),  # Halved from 12
        13: ("Outsmarted AI, gained XP!", {"xp": 10, "credits": 10}),
        14: ("Job paid off with credits!", {"credits": 25, "xp": 10}),
        15: ("Found a hidden Data Drive!", {"data_drive": 1, "xp": 8, "credits": 10}),
        16: ("Hacked a server, scored points!", {"score": secrets.randbelow(10) + 15, "xp": 10, "credits": 10}),  # 15-24
        17: ("Found a Neon Key in a safe!", {"neon_key": 1, "xp": 8, "credits": 10}),
        18: ("Security lockdown hurt you!", {"player_health": -7, "comp_health": -7, "xp": 1}),
        19: ("Won a corporate deal, got credits!", {"credits": 40, "xp": 10}),
        20: ("Snagged a Nano Patch from a guard!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        21: ("Hacked a system, gained crypto chips!", {"crypto_chips": 3, "xp": 10, "credits": 10}),
        22: ("Found a Data Drive in a lab!", {"data_drive": 1, "xp": 8, "credits": 10}),
        23: ("Evaded a trap, gained XP!", {"xp": 12, "credits": 10}),
        24: ("Traded for credits in a meeting!", {"credits": 45, "xp": 10}),
        25: ("Found a Neon Key in an office!", {"neon_key": 1, "xp": 8, "credits": 10}),
        26: ("Hacked a mainframe, big score!", {"score": secrets.randbelow(10) + 20, "xp": 10, "credits": 10}),  # 20-29
        27: ("Security bots attacked!", {"player_health": -8, "comp_health": -8, "xp": 1}),
        28: ("Corporate job paid well!", {"credits": 50, "xp": 10}),
        29: ("Found crypto chips in a vault!", {"crypto_chips": 4, "xp": 10, "credits": 10}),
        30: ("Learned corporate secrets, gained XP!", {"xp": 15, "credits": 10}),
        31: ("Scavenged a Nano Patch!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        32: ("Traded for a Data Drive!", {"data_drive": 1, "xp": 8, "credits": 10}),
        33: ("Big corporate deal, huge credits!", {"credits": 55, "xp": 10}),
        34: ("Found a Neon Key in a safe!", {"neon_key": 1, "xp": 8, "credits": 10}),
        35: ("Security trap hit hard!", {"player_health": -9, "comp_health": -9, "xp": 1}),
        36: ("Hacked a system, scored big!", {"score": secrets.randbelow(10) + 20, "xp": 10, "credits": 10}),  # 20-29
        37: ("Deal netted crypto chips!", {"crypto_chips": 4, "xp": 10, "credits": 10}),
        38: ("Found a Nano Patch in a lab!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        39: ("Dodged a trap, health restored!", {"player_health": 3, "comp_health": 3, "xp": 8, "credits": 10}),  # Halved from 7
        40: ("Overcame a challenge, gained XP!", {"xp": 18, "credits": 10}),
        41: ("Traded for credits in a boardroom!", {"credits": 60, "xp": 10}),
        42: ("Found a Quantum Core in a safe!", {"quantum_core": 1, "xp": 10, "credits": 10}),
        43: ("Hacked a drone, big score!", {"score": secrets.randbelow(10) + 25, "xp": 10, "credits": 10}),  # 25-34
        44: ("Found a Neon Key in a vault!", {"neon_key": 1, "xp": 8, "credits": 10}),
        45: ("Security system zapped you!", {"player_health": -10, "comp_health": -10, "xp": 1}),
        46: ("Hacked a system, earned credits!", {"credits": 65, "xp": 10}),
        47: ("Won a deal, gained crypto chips!", {"crypto_chips": 5, "xp": 10, "credits": 10}),
        48: ("Found a Nano Patch in a crate!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        49: ("Dodged a trap, health restored!", {"player_health": 4, "comp_health": 4, "xp": 8, "credits": 10}),  # Halved from 8
        50: ("Crypto Surge in a safe! (Doubles credits for 2 events)", {"crypto_surge": 1, "credits": -12, "xp": 10}),
        51: ("Security bots attacked!", {"player_health": -11, "comp_health": -11, "xp": 1}),
        52: ("Lost credits to a corporate scam!", {"credits": -15, "xp": 1}),
        53: ("Companion caught in a trap!", {"comp_health": -12, "xp": 1}),
        54: ("Failed hack cost credits!", {"credits": -10, "xp": 1}),
        55: ("Security lockdown hit hard!", {"player_health": -12, "comp_health": -12, "xp": 1}),
        56: ("Bad deal cost credits!", {"credits": -17, "xp": 1}),
        57: ("Companion badly hurt!", {"comp_health": -13, "xp": 1}),
        58: ("System virus zapped you!", {"player_health": -13, "comp_health": -13, "xp": 1}),
        59: ("Lost crypto chips to a hack!", {"score": 6, "xp": 1}),
        60: ("Ambushed by security!", {"player_health": -14, "comp_health": -14, "xp": 1}),
        61: ("Scammed, lost credits!", {"credits": -20, "xp": 1}),
        62: ("Companion injured in a fight!", {"comp_health": -15, "xp": 1}),
        63: ("Hack failed, took damage!", {"player_health": -15, "comp_health": -15, "xp": 1}),
        64: ("Credits stolen in a heist!", {"credits": -22, "xp": 1}),
        65: ("Companion hurt in a trap!", {"comp_health": -16, "xp": 1}),
        66: ("System surge drained vitality!", {"player_health": -16, "comp_health": -16, "xp": 1}),
        67: ("Lost credits in a deal!", {"credits": -12, "xp": 1}),
        68: ("Security took your credits!", {"credits": -25, "xp": 1}),
        69: ("Companion severely injured!", {"comp_health": -17, "xp": 1}),
        70: ("Deal gone wrong, lost credits!", {"credits": -27, "xp": 1}),
        71: ("Security assault hit hard!", {"player_health": -17, "comp_health": -17, "xp": 1}),
        72: ("Trap cost you credits!", {"credits": -15, "xp": 1}),
        73: ("Companion took a bad hit!", {"comp_health": -18, "xp": 1}),
        74: ("System virus, big damage!", {"player_health": -18, "comp_health": -18, "xp": 1}),
        75: ("Heist wiped out credits!", {"credits": -30, "xp": 1}),
        76: ("Companion nearly out!", {"comp_health": -19, "xp": 1}),
        77: ("Severe security assault!", {"player_health": -19, "comp_health": -19, "xp": 1}),
        78: ("Lost credits in a scam!", {"credits": -17, "xp": 1}),
        79: ("Companion critically wounded!", {"comp_health": -20, "xp": 1}),
        80: ("Security took down companion!", {"comp_health": -21, "xp": 1}),
        81: ("Security crushed you!", {"player_health": -20, "comp_health": -20, "xp": 1}),
        82: ("Fight drained credits!", {"credits": -32, "xp": 1}),
        83: ("Companion hurt badly!", {"comp_health": -22, "xp": 1}),
        84: ("System outage, heavy damage!", {"player_health": -21, "comp_health": -21, "xp": 1}),
        85: ("Scam cost you credits!", {"credits": -20, "xp": 1}),
        86: ("Companion down!", {"comp_health": -23, "xp": 1}),
        87: ("Major security attack!", {"player_health": -22, "comp_health": -22, "xp": 1}),
        88: ("Credits wiped out!", {"credits": -50, "xp": 1}),
        89: ("Companion in critical failure!", {"comp_health": -24, "xp": 1}),
        90: ("System surge, severe damage!", {"player_health": -23, "comp_health": -23, "xp": 1}),
        91: ("Security wipeout!", {"player_health": -24, "comp_health": -24, "xp": 1}),
        92: ("Lost credits and health!", {"credits": -22, "player_health": -25, "comp_health": -25, "xp": 1}),
        93: ("Companion lost!", {"comp_health": -26, "player_health": -26, "xp": 1}),
        94: ("System collapse!", {"player_health": -27, "comp_health": -27, "xp": 1}),
        95: ("Security massacre!", {"player_health": -28, "comp_health": -26, "xp": 1}),
        96: ("Lost credits in a fight!", {"credits": -27, "player_health": -29, "comp_health": -29, "xp": 1}),
        97: ("Companion gone!", {"comp_health": -27, "player_health": -30, "xp": 1}),
        98: ("System overload!", {"player_health": -31, "comp_health": -31, "xp": 1}),
        99: ("Security annihilation!", {"player_health": -32, "comp_health": -28, "xp": 1}),
        100: ("Total system failure!", {"credits": -30, "player_health": -50, "comp_health": -30, "xp": 1})
    }

    outcomes_data_vault = {
        1: ("Bypassed firewall, got credits!", {"credits": 40, "xp": 10}),
        2: ("Found a Nano Patch in a server!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        3: ("Hacked a database, huge score!", {"score": secrets.randbelow(10) + 20, "xp": 12, "credits": 10}),  # 20-29
        4: ("Downloaded crypto chips!", {"crypto_chips": 3, "xp": 10, "credits": 10}),
        5: ("Found a Neon Key in a vault!", {"neon_key": 1, "xp": 8, "credits": 10}),
        6: ("Evaded a virus, gained vitality!", {"player_health": 3, "comp_health": 3, "xp": 8, "credits": 10}),  # Halved from 7
        7: ("Snagged a Data Drive from a node!", {"data_drive": 1, "xp": 8, "credits": 10}),
        8: ("Quick hack netted credits!", {"credits": 35, "xp": 10}),
        9: ("Virus zapped you!", {"player_health": -7, "comp_health": -7, "xp": 1}),
        10: ("Found a Quantum Core in a server!", {"quantum_core": 1, "xp": 10, "credits": 10}),
        11: ("Hacked a node, got crypto chips!", {"crypto_chips": 3, "xp": 10, "credits": 10}),
        12: ("Server medkit restored health!", {"player_health": 7, "comp_health": 7, "xp": 8, "credits": 10}),  # Halved from 14
        13: ("Outsmarted AI, gained XP!", {"xp": 12, "credits": 10}),
        14: ("Job paid off with credits!", {"credits": 30, "xp": 10}),
        15: ("Found a hidden Data Drive!", {"data_drive": 1, "xp": 8, "credits": 10}),
        16: ("Hacked a server, scored points!", {"score": secrets.randbelow(10) + 20, "xp": 10, "credits": 10}),  # 20-29
        17: ("Found a Neon Key in a vault!", {"neon_key": 1, "xp": 8, "credits": 10}),
        18: ("Firewall hit you hard!", {"player_health": -8, "comp_health": -8, "xp": 1}),
        19: ("Won a data heist, got credits!", {"credits": 45, "xp": 10}),
        20: ("Snagged a Nano Patch from a node!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        21: ("Hacked a system, gained crypto chips!", {"crypto_chips": 4, "xp": 10, "credits": 10}),
        22: ("Found a Data Drive in a server!", {"data_drive": 1, "xp": 8, "credits": 10}),
        23: ("Evaded a virus, gained XP!", {"xp": 14, "credits": 10}),
        24: ("Traded for credits in a node!", {"credits": 50, "xp": 10}),
        25: ("Found a Neon Key in a vault!", {"neon_key": 1, "xp": 8, "credits": 10}),
        26: ("Hacked a mainframe, big score!", {"score": secrets.randbelow(10) + 25, "xp": 10, "credits": 10}),  # 25-34
        27: ("Virus attack hit hard!", {"player_health": -9, "comp_health": -9, "xp": 1}),
        28: ("Data heist paid well!", {"credits": 55, "xp": 10}),
        29: ("Found crypto chips in a node!", {"crypto_chips": 4, "xp": 10, "credits": 10}),
        30: ("Learned data secrets, gained XP!", {"xp": 16, "credits": 10}),
        31: ("Scavenged a Nano Patch!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        32: ("Traded for a Data Drive!", {"data_drive": 1, "xp": 8, "credits": 10}),
        33: ("Big data deal, huge credits!", {"credits": 60, "xp": 10}),
        34: ("Found a Neon Key in a server!", {"neon_key": 1, "xp": 8, "credits": 10}),
        35: ("Firewall trap hit hard!", {"player_health": -10, "comp_health": -10, "xp": 1}),
        36: ("Hacked a system, scored big!", {"score": secrets.randbelow(10) + 25, "xp": 10, "credits": 10}),  # 25-34
        37: ("Deal netted crypto chips!", {"crypto_chips": 5, "xp": 10, "credits": 10}),
        38: ("Found a Nano Patch in a node!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        39: ("Dodged a virus, health restored!", {"player_health": 4, "comp_health": 4, "xp": 8, "credits": 10}),  # Halved from 9
        40: ("Overcame a challenge, gained XP!", {"xp": 20, "credits": 10}),
        41: ("Traded for credits in a vault!", {"credits": 65, "xp": 10}),
        42: ("Found a Quantum Core in a vault!", {"quantum_core": 1, "xp": 10, "credits": 10}),
        43: ("Hacked a drone, big score!", {"score": secrets.randbelow(10) + 30, "xp": 10, "credits": 10}),  # 30-39
        44: ("Found a Neon Key in a server!", {"neon_key": 1, "xp": 8, "credits": 10}),
        45: ("Virus surge hit hard!", {"player_health": -11, "comp_health": -11, "xp": 1}),
        46: ("Hacked a system, earned credits!", {"credits": 70, "xp": 10}),
        47: ("Won a heist, gained crypto chips!", {"crypto_chips": 5, "xp": 10, "credits": 10}),
        48: ("Found a Nano Patch in a crate!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        49: ("Dodged a trap, health restored!", {"player_health": 5, "comp_health": 5, "xp": 8, "credits": 10}),  # Halved from 10
        50: ("Crypto Surge found! (Doubles credits for 2 events)", {"crypto_surge": 1, "credits": -15, "xp": 10}),
        51: ("Virus attack hit hard!", {"player_health": -12, "comp_health": -12, "xp": 1}),
        52: ("Lost credits to a hack!", {"credits": -17, "xp": 1}),
        53: ("Companion caught in a virus!", {"comp_health": -13, "xp": 1}),
        54: ("Failed hack cost credits!", {"credits": -12, "xp": 1}),
        55: ("Firewall hit you hard!", {"player_health": -13, "comp_health": -13, "xp": 1}),
        56: ("Bad deal cost credits!", {"credits": -20, "xp": 1}),
        57: ("Companion badly hurt!", {"comp_health": -14, "xp": 1}),
        58: ("System virus zapped you!", {"player_health": -14, "comp_health": -14, "xp": 1}),
        59: ("Lost crypto chips to a hack!", {"score": 7, "xp": 1}),
        60: ("Ambushed by security!", {"player_health": -15, "comp_health": -15, "xp": 1}),
        61: ("Scammed, lost credits!", {"credits": -22, "xp": 1}),
        62: ("Companion injured in a trap!", {"comp_health": -16, "xp": 1}),
        63: ("Hack failed, took damage!", {"player_health": -16, "comp_health": -16, "xp": 1}),
        64: ("Credits stolen in a heist!", {"credits": -25, "xp": 1}),
        65: ("Companion hurt in a virus!", {"comp_health": -17, "xp": 1}),
        66: ("System surge drained vitality!", {"player_health": -17, "comp_health": -17, "xp": 1}),
        67: ("Lost credits in a deal!", {"credits": -15, "xp": 1}),
        68: ("Security took your credits!", {"credits": -27, "xp": 1}),
        69: ("Companion severely injured!", {"comp_health": -18, "xp": 1}),
        70: ("Deal gone wrong, lost credits!", {"credits": -30, "xp": 1}),
        71: ("Security assault hit hard!", {"player_health": -18, "comp_health": -18, "xp": 1}),
        72: ("Trap cost you credits!", {"credits": -17, "xp": 1}),
        73: ("Companion took a bad hit!", {"comp_health": -19, "xp": 1}),
        74: ("System virus, big damage!", {"player_health": -19, "comp_health": -19, "xp": 1}),
        75: ("Heist wiped out credits!", {"credits": -32, "xp": 1}),
        76: ("Companion nearly out!", {"comp_health": -20, "xp": 1}),
        77: ("Severe security assault!", {"player_health": -20, "comp_health": -20, "xp": 1}),
        78: ("Lost credits in a scam!", {"credits": -20, "xp": 1}),
        79: ("Companion critically wounded!", {"comp_health": -21, "xp": 1}),
        80: ("Security took down companion!", {"comp_health": -22, "xp": 1}),
        81: ("Security crushed you!", {"player_health": -21, "comp_health": -21, "xp": 1}),
        82: ("Fight drained credits!", {"credits": -35, "xp": 1}),
        83: ("Companion hurt badly!", {"comp_health": -23, "xp": 1}),
        84: ("System outage, heavy damage!", {"player_health": -22, "comp_health": -22, "xp": 1}),
        85: ("Scam cost you credits!", {"credits": -22, "xp": 1}),
        86: ("Companion down!", {"comp_health": -24, "xp": 1}),
        87: ("Major security attack!", {"player_health": -23, "comp_health": -23, "xp": 1}),
        88: ("Credits wiped out!", {"credits": -50, "xp": 1}),
        89: ("Companion in critical failure!", {"comp_health": -25, "xp": 1}),
        90: ("System surge, severe damage!", {"player_health": -24, "comp_health": -24, "xp": 1}),
        91: ("Security wipeout!", {"player_health": -25, "comp_health": -25, "xp": 1}),
        92: ("Lost credits and health!", {"credits": -25, "player_health": -26, "comp_health": -26, "xp": 1}),
        93: ("Companion lost!", {"comp_health": -27, "player_health": -27, "xp": 1}),
        94: ("System collapse!", {"player_health": -28, "comp_health": -28, "xp": 1}),
        95: ("Security massacre!", {"player_health": -29, "comp_health": -27, "xp": 1}),
        96: ("Lost credits in a fight!", {"credits": -30, "player_health": -30, "comp_health": -30, "xp": 1}),
        97: ("Companion gone!", {"comp_health": -28, "player_health": -31, "xp": 1}),
        98: ("System overload!", {"player_health": -32, "comp_health": -32, "xp": 1}),
        99: ("Security annihilation!", {"player_health": -33, "comp_health": -29, "xp": 1}),
        100: ("Total system failure!", {"credits": -35, "player_health": -50, "comp_health": -30, "xp": 1})
    }

    outcomes_grid_wastelands = {
        1: ("Scavenged credits from wreckage!", {"credits": 25, "xp": 10}),
        2: ("Found a Nano Patch in ruins!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        3: ("Hacked a drone, scored points!", {"score": secrets.randbelow(10) + 10, "xp": 12, "credits": 10}),  # 10-19
        4: ("Traded scrap for crypto chips!", {"crypto_chips": 2, "xp": 10, "credits": 10}),
        5: ("Found a Neon Key in debris!", {"neon_key": 1, "xp": 8, "credits": 10}),
        6: ("Survived a storm, gained vitality!", {"player_health": 2, "comp_health": 2, "xp": 8, "credits": 10}),  # Halved from 5
        7: ("Found a Data Drive in a wreck!", {"data_drive": 1, "xp": 8, "credits": 10}),
        8: ("Quick hack netted credits!", {"credits": 20, "xp": 10}),
        9: ("Mutant attack hit you!", {"player_health": -5, "comp_health": -5, "xp": 1}),
        10: ("Found a Quantum Core in a ruin!", {"quantum_core": 1, "xp": 10, "credits": 10}),
        11: ("Deal brought crypto chips!", {"crypto_chips": 1, "xp": 10, "credits": 10}),
        12: ("Found a medkit in the wastes!", {"player_health": 5, "comp_health": 5, "xp": 8, "credits": 10}),  # Halved from 10
        13: ("Outran a drone, gained XP!", {"xp": 8, "credits": 10}),
        14: ("Scavenged credits from a wreck!", {"credits": 15, "xp": 10}),
        15: ("Found a hidden Data Drive!", {"data_drive": 1, "xp": 8, "credits": 10}),
        16: ("Hacked a terminal, scored points!", {"score": secrets.randbelow(10) + 10, "xp": 10, "credits": 10}),  # 10-19
        17: ("Found a Neon Key in a ruin!", {"neon_key": 1, "xp": 8, "credits": 10}),
        18: ("Mutant ambush hit hard!", {"player_health": -6, "comp_health": -6, "xp": 1}),
        19: ("Won a fight, got credits!", {"credits": 30, "xp": 10}),
        20: ("Snagged a Nano Patch from a scavenger!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        21: ("Hacked a node, gained crypto chips!", {"crypto_chips": 2, "xp": 10, "credits": 10}),
        22: ("Found a Data Drive in debris!", {"data_drive": 1, "xp": 8, "credits": 10}),
        23: ("Evaded a trap, gained XP!", {"xp": 10, "credits": 10}),
        24: ("Traded for credits in the wastes!", {"credits": 35, "xp": 10}),
        25: ("Found a Neon Key in a wreck!", {"neon_key": 1, "xp": 8, "credits": 10}),
        26: ("Hacked a system, scored big!", {"score": secrets.randbelow(10) + 15, "xp": 10, "credits": 10}),  # 15-24
        27: ("Mutant attack hit hard!", {"player_health": -7, "comp_health": -7, "xp": 1}),
        28: ("Scavenged credits from a ruin!", {"credits": 40, "xp": 10}),
        29: ("Found crypto chips in a stash!", {"crypto_chips": 3, "xp": 10, "credits": 10}),
        30: ("Learned wasteland skills, gained XP!", {"xp": 12, "credits": 10}),
        31: ("Scavenged a Nano Patch!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        32: ("Traded for a Data Drive!", {"data_drive": 1, "xp": 8, "credits": 10}),
        33: ("Big trade, huge credits!", {"credits": 45, "xp": 10}),
        34: ("Found a Neon Key in a ruin!", {"neon_key": 1, "xp": 8, "credits": 10}),
        35: ("Mutant trap hit hard!", {"player_health": -8, "comp_health": -8, "xp": 1}),
        36: ("Hacked a system, scored big!", {"score": secrets.randbelow(10) + 15, "xp": 10, "credits": 10}),  # 15-24
        37: ("Deal netted crypto chips!", {"crypto_chips": 3, "xp": 10, "credits": 10}),
        38: ("Found a Nano Patch in a wreck!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        39: ("Dodged a trap, health restored!", {"player_health": 3, "comp_health": 3, "xp": 8, "credits": 10}),  # Halved from 6
        40: ("Overcame a challenge, gained XP!", {"xp": 15, "credits": 10}),
        41: ("Traded for credits in a ruin!", {"credits": 50, "xp": 10}),
        42: ("Found a Quantum Core in a wreck!", {"quantum_core": 1, "xp": 10, "credits": 10}),
        43: ("Hacked a drone, big score!", {"score": secrets.randbelow(10) + 20, "xp": 10, "credits": 10}),  # 20-29
        44: ("Found a Neon Key in a ruin!", {"neon_key": 1, "xp": 8, "credits": 10}),
        45: ("Mutant ambush hit hard!", {"player_health": -9, "comp_health": -9, "xp": 1}),
        46: ("Hacked a system, earned credits!", {"credits": 55, "xp": 10}),
        47: ("Won a fight, gained crypto chips!", {"crypto_chips": 4, "xp": 10, "credits": 10}),
        48: ("Found a Nano Patch in a crate!", {"nano_patch": 1, "xp": 8, "credits": 10}),
        49: ("Dodged a trap, health restored!", {"player_health": 3, "comp_health": 3, "xp": 8, "credits": 10}),  # Halved from 7
        50: ("Crypto Surge found! (Doubles credits for 2 events)", {"crypto_surge": 1, "credits": -7, "xp": 10}),
        51: ("Mutant attack hit hard!", {"player_health": -10, "comp_health": -10, "xp": 1}),
        52: ("Lost credits to a scavenger!", {"credits": -12, "xp": 1}),
        53: ("Companion caught in a trap!", {"comp_health": -11, "xp": 1}),
        54: ("Failed hack cost credits!", {"credits": -10, "xp": 1}),
        55: ("Mutant trap hit hard!", {"player_health": -11, "comp_health": -11, "xp": 1}),
        56: ("Bad deal cost credits!", {"credits": -15, "xp": 1}),
        57: ("Companion badly hurt!", {"comp_health": -12, "xp": 1}),
        58: ("Wasteland virus zapped you!", {"player_health": -12, "comp_health": -12, "xp": 1}),
        59: ("Lost crypto chips to a thief!", {"score": 5, "xp": 1}),
        60: ("Ambushed by mutants!", {"player_health": -13, "comp_health": -13, "xp": 1}),
        61: ("Scammed, lost credits!", {"credits": -17, "xp": 1}),
        62: ("Companion injured in a fight!", {"comp_health": -14, "xp": 1}),
        63: ("Hack failed, took damage!", {"player_health": -14, "comp_health": -14, "xp": 1}),
        64: ("Credits stolen in a heist!", {"credits": -20, "xp": 1}),
        65: ("Companion hurt in a trap!", {"comp_health": -15, "xp": 1}),
        66: ("Wasteland surge drained vitality!", {"player_health": -15, "comp_health": -15, "xp": 1}),
        67: ("Lost credits in a deal!", {"credits": -12, "xp": 1}),
        68: ("Scavengers took your credits!", {"credits": -22, "xp": 1}),
        69: ("Companion severely injured!", {"comp_health": -16, "xp": 1}),
        70: ("Deal gone wrong, lost credits!", {"credits": -25, "xp": 1}),
        71: ("Mutant assault hit hard!", {"player_health": -16, "comp_health": -16, "xp": 1}),
        72: ("Trap cost you credits!", {"credits": -15, "xp": 1}),
        73: ("Companion took a bad hit!", {"comp_health": -17, "xp": 1}),
        74: ("Wasteland virus, big damage!", {"player_health": -17, "comp_health": -17, "xp": 1}),
        75: ("Heist wiped out credits!", {"credits": -27, "xp": 1}),
        76: ("Companion nearly out!", {"comp_health": -18, "xp": 1}),
        77: ("Severe mutant assault!", {"player_health": -18, "comp_health": -18, "xp": 1}),
        78: ("Lost credits in a scam!", {"credits": -17, "xp": 1}),
        79: ("Companion critically wounded!", {"comp_health": -19, "xp": 1}),
        80: ("Mutants took down companion!", {"comp_health": -20, "xp": 1}),
        81: ("Mutant assault crushed you!", {"player_health": -19, "comp_health": -19, "xp": 1}),
        82: ("Fight drained credits!", {"credits": -30, "xp": 1}),
        83: ("Companion hurt badly!", {"comp_health": -21, "xp": 1}),
        84: ("Wasteland outage, heavy damage!", {"player_health": -20, "comp_health": -20, "xp": 1}),
        85: ("Scam cost you credits!", {"credits": -20, "xp": 1}),
        86: ("Companion down!", {"comp_health": -22, "xp": 1}),
        87: ("Major mutant attack!", {"player_health": -21, "comp_health": -21, "xp": 1}),
        88: ("Credits wiped out!", {"credits": -50, "xp": 1}),
        89: ("Companion in critical failure!", {"comp_health": -23, "xp": 1}),
        90: ("Wasteland surge, severe damage!", {"player_health": -22, "comp_health": -22, "xp": 1}),
        91: ("Mutant wipeout!", {"player_health": -23, "comp_health": -23, "xp": 1}),
        92: ("Lost credits and health!", {"credits": -22, "player_health": -24, "comp_health": -24, "xp": 1}),
        93: ("Companion lost!", {"comp_health": -25, "player_health": -25, "xp": 1}),
        94: ("Wasteland collapse!", {"player_health": -26, "comp_health": -26, "xp": 1}),
        95: ("Mutant massacre!", {"player_health": -27, "comp_health": -25, "xp": 1}),
        96: ("Lost credits in a fight!", {"credits": -25, "player_health": -28, "comp_health": -28, "xp": 1}),
        97: ("Companion gone!", {"comp_health": -26, "player_health": -29, "xp": 1}),
        98: ("Wasteland overload!", {"player_health": -30, "comp_health": -30, "xp": 1}),
        99: ("Mutant annihilation!", {"player_health": -31, "comp_health": -27, "xp": 1}),
        100: ("Total wasteland failure!", {"credits": -25, "player_health": -50, "comp_health": -30, "xp": 1})
    }

    outcomes_dict = {
        1: outcomes_neon_underdistrict,
        2: outcomes_corporate_skyspire,
        3: outcomes_data_vault,
        4: outcomes_grid_wastelands
    }
    outcomes = outcomes_dict.get(int(path), outcomes_neon_underdistrict)  # Default to Neon Underdistrict
    result, changes = outcomes.get(outcome, ("No outcome defined for this path", {}))

    was_deactivated = current_companion["name"] in deactivated_companions

    # Crypto Surge effect if active
    crypto_surge_message = ""
    if player["crypto_surge_events"] > 0 and "credits" in changes and changes["credits"] > 0:
        changes["credits"] *= 2
        player["crypto_surge_events"] -= 1
        crypto_surge_message = f"Credits doubled by Crypto Surge ({player['crypto_surge_events']} events left)"
    elif player["crypto_surge_events"] > 0:
        crypto_surge_message = f"Crypto Surge active ({player['crypto_surge_events']} events left)"

    # Apply player strength scaling for negative health changes
    strength_modifier = 2.1 - (player["player_strength"] / 17.5)
    if "player_health" in changes and changes["player_health"] < 0:
        scaled_damage = round(changes["player_health"] * strength_modifier)
        if player["player_strength"] <= 5:
            changes["player_health"] = max(scaled_damage, -9)
        elif player["player_strength"] <= 9:
            changes["player_health"] = max(scaled_damage, -7)
        elif player["player_strength"] == 10:
            changes["player_health"] = max(scaled_damage, -6)
        elif player["player_strength"] <= 14:
            changes["player_health"] = max(scaled_damage, -4)
        else:
            changes["player_health"] = max(scaled_damage, -2)

    # Apply companion strength scaling for negative health changes
    if "comp_health" in changes and changes["comp_health"] < 0:
        comp_strength = current_companion["strength"]
        comp_strength_modifier = 2.1 - (comp_strength / 17.5)
        scaled_comp_damage = round(changes["comp_health"] * comp_strength_modifier)
        if comp_strength <= 5:
            changes["comp_health"] = max(scaled_comp_damage, -9)
        elif comp_strength <= 9:
            changes["comp_health"] = max(scaled_comp_damage, -7)
        elif comp_strength == 10:
            changes["comp_health"] = max(scaled_comp_damage, -6)
        elif comp_strength <= 14:
            changes["comp_health"] = max(scaled_comp_damage, -4)
        else:
            changes["comp_health"] = max(scaled_comp_damage, -2)

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
        changes["comp_health"] = 0

    # Handle deactivated companion revival on positive outcomes
    if was_deactivated and is_positive_outcome(changes):
        changes["comp_health"] += 10
        current_companion["health"] = max(0, min(current_companion["health"] + 10, 100))
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
        print(Fore.MAGENTA + f"Crypto Surge ({player['crypto_surge']}): Doubles credits for next 2 events..." + Style.RESET_ALL)
        print(Fore.GREEN + "\nUSE AN ITEM..." + Style.RESET_ALL)
        print(Fore.GREEN + "1. Nano Patch (+25 player health, +20 companion health)" + Style.RESET_ALL)
        print(Fore.GREEN + "2. Data Drive (+20 score)" + Style.RESET_ALL)
        print(Fore.GREEN + "3. Neon Key (+4 crypto chips)" + Style.RESET_ALL)
        print(Fore.GREEN + "4. Quantum Core (Double score next event)" + Style.RESET_ALL)
        print(Fore.GREEN + "5. Crypto Surge (Double credits for next 2 events)" + Style.RESET_ALL)
        print(Fore.GREEN + "6. Return" + Style.RESET_ALL)
        inv_choice = input(Fore.GREEN + "\nSelect an item (1-6): " + Style.RESET_ALL).strip()
        if not inv_choice or inv_choice not in ["1", "2", "3", "4", "5", "6"]:
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
            if player["crypto_surge"] > 0:
                player["crypto_surge_events"] = 2
                player["crypto_surge"] -= 1
                stat_changes = "Crypto Surge used - Credits will double for next 2 events, Crypto Surges -1"
                print(Fore.GREEN + "\nCrypto Surge used - Next 2 events' credit gains will be doubled..." + Style.RESET_ALL)
            else:
                stat_changes = "No Crypto Surges remain"
                print(Fore.GREEN + "\nNo Crypto Surges remain..." + Style.RESET_ALL)
        elif inv_choice == "6":
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
        print(Fore.GREEN + f"{name} {status} - Class: {Fore.GREEN}{companion_stats[name]['class']}{Style.RESET_ALL}, Health: {Fore.RED}{companion_stats[name]['health']}{Style.RESET_ALL}, Strength: {Fore.WHITE}{companion_stats[name]['strength']}{Style.RESET_ALL}" + Style.RESET_ALL)
    print(Fore.GREEN + f"\nCurrent Companion: {current_companion['name']} ({current_companion['class']})" + Style.RESET_ALL)
    print(Fore.GREEN + "\nPress Enter to return..." + Style.RESET_ALL)
    stat_changes = "Viewed companions list"
    input()

def shop():
    global player, stat_changes
    while True:
        clear_console()
        print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.GREEN + "NEON GRID RUNNER - SHOP" + Style.RESET_ALL)
        print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.GREEN + get_random_ascii() + Style.RESET_ALL)
        shop_items = {
            "nano_patch": 50,
            "data_drive": 75,
            "neon_key": 100,
            "quantum_core": 150
        }
        rare_item = "crypto_surge" if secrets.randbelow(10) == 0 else None
        if rare_item:
            shop_items[rare_item] = 300
        # Store prices for each item to ensure consistency
        item_prices = {}
        for item, base_price in shop_items.items():
            price_modifier = (secrets.randbelow(50) + 25) / 100
            item_prices[item] = int(base_price * (1 + price_modifier))
        print(Fore.GREEN + "\nSHOP TERMINAL..." + Style.RESET_ALL)
        print(Fore.GREEN + f"Credits: {player['credits']}" + Style.RESET_ALL)
        for item, current_price in item_prices.items():
            item_name = item.replace('_', ' ').title()
            if item == "crypto_surge":
                print(Fore.GREEN + f"{item_name} (Doubles credits for 2 events) - Price: {current_price} credits" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"{item_name} - Price: {current_price} credits" + Style.RESET_ALL)
        print(Fore.GREEN + "\nPURCHASE AN ITEM..." + Style.RESET_ALL)
        for i, item in enumerate(shop_items.keys(), 1):
            print(Fore.GREEN + f"{i}. {item.replace('_', ' ').title()}" + Style.RESET_ALL)
        print(Fore.GREEN + f"{len(shop_items) + 1}. Return" + Style.RESET_ALL)
        choice = input(Fore.GREEN + "\nSelect an item (1-" + str(len(shop_items) + 1) + "): " + Style.RESET_ALL).strip()
        if not choice or not choice.isdigit() or int(choice) not in range(1, len(shop_items) + 2):
            stat_changes = "Invalid choice"
            print(Fore.GREEN + "\nINVALID CHOICE..." + Style.RESET_ALL)
            print(Fore.GREEN + "\nPress Enter to try again..." + Style.RESET_ALL)
            input()
            continue
        if int(choice) == len(shop_items) + 1:
            return
        selected_item = list(shop_items.keys())[int(choice) - 1]
        current_price = item_prices[selected_item]  # Use the stored price
        if player["credits"] >= current_price:
            player["credits"] -= current_price
            if selected_item == "crypto_surge":
                player["crypto_surge"] = player.get("crypto_surge", 0) + 1
                stat_changes = f"Purchased Crypto Surge for {current_price} credits"
            else:
                player[selected_item] += 1
                stat_changes = f"Purchased {selected_item.replace('_', ' ').title()} for {current_price} credits"
            print(Fore.GREEN + f"\n{stat_changes}..." + Style.RESET_ALL)
        else:
            stat_changes = "Insufficient credits"
            print(Fore.GREEN + "\nInsufficient credits..." + Style.RESET_ALL)
        print(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)
        input()

def main():
    """Main game loop."""
    global player, current_companion, stat_changes, quantum_core_active, deactivated_companions, companion_stats, last_path_chosen
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
        "crypto_surge": 0,
        "crypto_surge_events": 0,
        "player_strength": secrets.randbelow(10) + 5,
        "level": 1,
        "xp": 0,
        "xp_needed": 50,
        "credits": 100
    })
    current_companion.update({
        "name": "",
        "health": 0,
        "strength": 0,
        "class": ""
    })
    deactivated_companions.clear()
    quantum_core_active = False
    stat_changes = ""
    last_path_chosen = None  # Initialize global variable

    # Reinitialize companion stats
    companion_stats.clear()
    companion_stats.update({
        name: {
            "health": max(0, min(secrets.randbelow(50) + 50, 100)),
            "strength": secrets.randbelow(10) + 5,
            "class": secrets.choice(companion_classes)
        } for name in companions
    })

    # Assign a new random companion at start
    available_companions = [name for name in companions if name not in deactivated_companions]
    if not available_companions:
        deactivated_companions.clear()
        available_companions = companions.copy()
        stat_changes = "All companions were deactivated; resetting companion list."
        print(Fore.RED + "Warning: All companions were deactivated. Resetting companion list." + Style.RESET_ALL)

    try:
        companion_name = secrets.choice(available_companions)
        current_companion.update({
            "name": companion_name,
            "health": max(0, min(companion_stats[companion_name]["health"], 100)),
            "strength": companion_stats[companion_name]["strength"],
            "class": companion_stats[companion_name]["class"]
        })
        companion_stats[companion_name]["health"] = current_companion["health"]
        stat_changes = f"Companion {companion_name} ({current_companion['class']}) assigned."
    except Exception as e:
        stat_changes = f"Error assigning companion: {str(e)}. Starting without companion."
        print(Fore.RED + stat_changes + Style.RESET_ALL)
        current_companion.update({
            "name": "",
            "health": 0,
            "strength": 0,
            "class": ""
        })

    clear_console()
    print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
    print(Fore.GREEN + "NEON GRID RUNNER - D10+D10" + Style.RESET_ALL)
    print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
    print(Fore.GREEN + get_random_ascii() + Style.RESET_ALL)
    print(Fore.GREEN + "NEON GRID RUNNER" + Style.RESET_ALL)
    print(Fore.GREEN + "CONQUER THE CYBER GRID" + Style.RESET_ALL)
    if current_companion["name"]:
        print(Fore.GREEN + f"\nCompanion: {Fore.GREEN}{current_companion['name']} ({current_companion['class']}) joins you in the grid..." + Style.RESET_ALL)
    else:
        print(Fore.RED + "\nNo companion available. Proceeding solo..." + Style.RESET_ALL)
    print(Fore.GREEN + "\n\n        Press Enter to Hack in" + Style.RESET_ALL)
    print(Fore.GREEN + "    Cyber Grid Nexus..." + Style.RESET_ALL)
    input()

    while True:
        clear_console()
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
        print(Fore.RED + f"Health: {player['health']}" + Style.RESET_ALL + Fore.YELLOW + f"  Score: {player['score']}" + Style.RESET_ALL + Fore.CYAN + f"  Crypto Chips: {player['crypto_chips']}" + Style.RESET_ALL + Fore.BLUE + f"  Quantum Cores: {player['quantum_core']}" + Style.RESET_ALL + Fore.MAGENTA + f"  Credits: {player['credits']}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Progress: Score {player['score']}/6000 Crypto Chips {player['crypto_chips']}/300 Quantum Cores {player['quantum_core']}/50" + Style.RESET_ALL)
        if current_companion["name"]:
            print(Fore.GREEN + f"\nCompanion: {Fore.GREEN}{current_companion['name']} ({current_companion['class']}{Style.RESET_ALL}) (Health: {Fore.RED}{current_companion['health']}{Style.RESET_ALL}, Strength: {Fore.WHITE}{current_companion['strength']}{Style.RESET_ALL})" + Style.RESET_ALL)
        if stat_changes:
            print(Fore.GREEN + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
        if player["crypto_surge_events"] > 0:
            print(Fore.MAGENTA + f"Crypto Surge active: Crypto Chips will double for {player['crypto_surge_events']} more event(s)" + Style.RESET_ALL)
        print(Fore.GREEN + "\nPath Chosen:" + Style.RESET_ALL)
        print(get_path_dial(last_path_chosen))

        # Check win/loss conditions (unchanged from original)
        if player["score"] >= 6000 and player["crypto_chips"] >= 300 and player["quantum_core"] >= 50:
            if pygame_initialized:
                pygame.mixer.music.stop()
                pygame.quit()
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

        if player["health"] <= 0:
            if pygame_initialized:
                pygame.mixer.music.stop()
                pygame.quit()
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
        print(Fore.GREEN + "0. Shop" + Style.RESET_ALL)
        print(Fore.GREEN + "1. Neon Underdistrict" + Style.RESET_ALL)
        print(Fore.GREEN + "2. Corporate Skyspire" + Style.RESET_ALL)
        print(Fore.GREEN + "3. Data Vault" + Style.RESET_ALL)
        print(Fore.GREEN + "4. Grid Wastelands" + Style.RESET_ALL)
        print(Fore.GREEN + "5. Inventory" + Style.RESET_ALL)
        print(Fore.GREEN + "6. Companions" + Style.RESET_ALL)
        print(Fore.GREEN + "7. Save Game" + Style.RESET_ALL)
        print(Fore.GREEN + "8. Load Game" + Style.RESET_ALL)
        print(Fore.GREEN + "9. Exit" + Style.RESET_ALL)
        choice = input(Fore.GREEN + "\nSelect a path (0-9): " + Style.RESET_ALL).strip()

        if choice == "0":
            shop()
        elif choice in ["1", "2", "3", "4"]:
            try:
                last_path_chosen = choice  # Update global variable
                pre_player_health = player["health"]
                pre_comp_health = current_companion["health"] if current_companion["name"] else 0

                # Select a new random companion
                available_companions = companions.copy()
                if not available_companions:
                    stat_changes = "No companions available. Proceeding without companion."
                    print(Fore.RED + stat_changes + Style.RESET_ALL)
                    current_companion.update({
                        "name": "",
                        "health": 0,
                        "strength": 0,
                        "class": ""
                    })
                    pre_comp_health = 0
                else:
                    try:
                        companion_name = secrets.choice(available_companions)
                        current_companion.update({
                            "name": companion_name,
                            "health": max(0, min(companion_stats[companion_name]["health"], 100)),
                            "strength": companion_stats[companion_name]["strength"],
                            "class": companion_stats[companion_name]["class"]
                        })
                        companion_stats[companion_name]["health"] = current_companion["health"]
                        pre_comp_health = current_companion["health"]
                    except Exception as e:
                        stat_changes = f"Error assigning companion: {str(e)}. Proceeding without companion."
                        print(Fore.RED + stat_changes + Style.RESET_ALL)
                        current_companion.update({
                            "name": "",
                            "health": 0,
                            "strength": 0,
                            "class": ""
                        })
                        pre_comp_health = 0

                die1, die2, outcome = roll_dice()
                result, changes = path_outcomes(int(choice), outcome)
                was_deactivated = current_companion["name"] in deactivated_companions if current_companion["name"] else False
                if current_companion["name"]:
                    print(Fore.GREEN + f"\n{current_companion['name']} ({current_companion['class']}{Style.RESET_ALL}) {'(Deactivated) ' if was_deactivated else ''}joins you for this run..." + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + "\nNo companion joins you for this run..." + Style.RESET_ALL)
                print(Fore.GREEN + f"\nDice Roll: D10={die1}, D10={die2}, Outcome={outcome}" + Style.RESET_ALL)
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
                credits_change = changes.get("credits", 0)
                player["credits"] = max(0, player["credits"] + credits_change)
                revival_health_change = 0
                if was_deactivated and is_positive_outcome(changes) and current_companion["name"]:
                    revival_health_change = 10
                if current_companion["name"] and current_companion["health"] <= 0 and current_companion["name"] not in deactivated_companions:
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
                crypto_surge_change = changes.get("crypto_surge", 0)
                player["crypto_surge"] = max(0, player["crypto_surge"] + crypto_surge_change)
                xp_change = changes.get("xp", 0)
                levelup_health_change = level_check(xp_change)
                post_player_health = player["health"]
                post_comp_health = current_companion["health"] if current_companion["name"] else 0

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
                if credits_change != 0:
                    stat_changes_list.append(Fore.MAGENTA + f"Credits {'+' if credits_change > 0 else ''}{credits_change}" + Style.RESET_ALL)
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
                if crypto_surge_change != 0:
                    stat_changes_list.append(Fore.MAGENTA + f"Crypto Surges {'+' if crypto_surge_change > 0 else ''}{crypto_surge_change}" + Style.RESET_ALL)
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
            if pygame_initialized:
                pygame.mixer.music.stop()
                pygame.quit()
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