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

# Initialize Pygame mixer for audio
try:
    pygame.mixer.init()
except pygame.error as e:
    print(Fore.RED + f"Failed to initialize audio mixer: {str(e)}" + Style.RESET_ALL)

# Define path to background music in the 'sounds' folder
SOUNDS_DIR = "sounds"
BACKGROUND_MUSIC = resource_path(os.path.join(SOUNDS_DIR, "background_music.ogg"))

# Check if music file exists and load/play it
if os.path.exists(BACKGROUND_MUSIC):
    try:
        pygame.mixer.music.load(BACKGROUND_MUSIC)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(Fore.RED + f"Failed to load music: {str(e)}" + Style.RESET_ALL)
else:
    print(Fore.RED + "Warning: background_music.ogg not found in sounds folder!" + Style.RESET_ALL)

# Define companion classes with unique effects
companion_classes = [
    "Barbarian", "Cleric", "Knight", "Mage", "Ranger", "Rogue", "Sorcerer", "Paladin",
    "Druid", "Necromancer", "Monk", "Bard", "Warlock", "Shaman", "Alchemist", "Beastmaster",
    "Assassin", "Wizard", "Hunter", "Priest", "Warlord", "Enchanter", "Inquisitor", "Runecaster"
]

# Define companion class modifiers
companion_class_modifiers = {
    "Barbarian": {"damage_boost": 2, "damage_reduction": 2},
    "Cleric": {"healing_boost": 3},
    "Knight": {"damage_reduction": 3},
    "Mage": {"magic_boost": 2},
    "Ranger": {"damage_boost": 2},
    "Rogue": {"score_boost": 2},
    "Sorcerer": {"healing_boost": 2, "damage_reduction": 2, "damage_boost": 2},
    "Paladin": {"healing_boost": 2, "damage_reduction": 2, "damage_boost": 2},
    "Druid": {"rune_boost": 2},
    "Necromancer": {"dark_boost": 2},
    "Monk": {"score_boost": 2},
    "Bard": {"score_boost": 2},
    "Warlock": {"curse_boost": 2},
    "Shaman": {"healing_boost": 3},
    "Alchemist": {"potion_boost": 2},
    "Beastmaster": {"healing_boost": 2},
    "Assassin": {"score_boost": 2},
    "Wizard": {"advanced_magic_boost": 2},
    "Hunter": {"score_boost": 2},
    "Priest": {"healing_boost": 3},
    "Warlord": {"score_boost": 2},
    "Enchanter": {"enchantment_boost": 2},
    "Inquisitor": {"rune_boost": 2},
    "Runecaster": {"rune_boost": 2}
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
    "rune_pulse": 0,
    "player_strength": secrets.randbelow(10) + 5,
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
    "health": min(secrets.randbelow(50) + 50, 100),
    "strength": secrets.randbelow(10) + 5,
    "class": secrets.choice(companion_classes)
} for name in companions}

# Track fallen companions
fallen_companions = []

# Current companion
current_companion = {
    "name": "",
    "health": 0,
    "strength": 0,
    "class": ""
}

# Global variables
arcane_crystal_active = False
rune_pulse_events = 0
stat_changes = ""
last_ascii_used = None
last_path_chosen = None

def get_path_dial():
    """Generate a fantasy-themed ASCII rune circle with yellow structure, cyan numbers, and the last chosen path in green."""
    dial_lines = [
        "     ☽===☾     ",
        "   |  ❧ 1 🏰    ",
        "☽=+===+=====+=+☾",
        "| 4 🧙‍♂️   📜 2 | ",
        "☽=+===+=====+=+☾",
        "   |  ✦ 3 ⚔️    ",
        "     ☽===☾     "
    ]
    colored_dial = []
    for line in dial_lines:
        new_line = line
        for i in range(1, 5):
            path_num = str(i)
            if path_num in line:
                try:
                    if last_path_chosen is not None and path_num == last_path_chosen:
                        new_line = new_line.replace(path_num, f"{Fore.GREEN}{path_num}{Style.RESET_ALL}")
                    else:
                        new_line = new_line.replace(path_num, f"{Fore.CYAN}{path_num}{Style.RESET_ALL}")
                except:
                    new_line = new_line.replace(path_num, path_num)
        try:
            colored_line = f"{Fore.YELLOW}{new_line}{Style.RESET_ALL}"
        except:
            colored_line = new_line
        colored_dial.append(colored_line)
    return "\n".join(colored_dial)

# List of available colorama colors
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
    ╔══════[🗝️]══════╗
    ║ 🌿 * | * * | * ♣ ║
    ║ * * | *🪷* | * * ║
    ║ ❧ * | * * | * 🌿 ║
    ║ * * | * * | * * ║
    ╚══════[🌲]══════╝
    """,
    """
    ╔══════[🪶]══════╗
    ║ ♣ * | * * | * 🪻 ║
    ║ * * | *🐉* | * * ║
    ║ 🌿 * | * * | * ❧ ║
    ║ * * | * * | * * ║
    ╚══════[🌳]══════╝
    """,
    """
    ╔═════[🌳🦇]═════╗
    ║ 🪴 * | * * | * 🌿 ║
    ║ * * | *🦚* | * * ║
    ║ ❧ * | * * | * ♣ ║
    ║ * * | * * | * * ║
    ╚═════[🦉🌲]═════╝
    """,
    """
    ╔══════[🔮]══════╗
    ║ 🌿 * | * * | * ❧ ║
    ║ * * | *🧜‍♀️* | * * ║
    ║ ♣ * | * * | * 🧝‍♀️ ║
    ║ * * | * * | * * ║
    ╚══════[🌴]══════╝
    """,
    """
    ╔═════[🐍🌲]═════╗
    ║ ❧ * | * * | * ♣ ║
    ║ * * | *📿* | * * ║
    ║ 🧚‍♀️ * | * * | * 🌿 ║
    ║ * * | * * | * * ║
    ╚═════[🌳🦎]═════╝
    """,
    """
    ╔══════[🌲]══════╗
    ║ ♣ * | * * | * 🌿 ║
    ║ * * | *⚗️* | * * ║
    ║ ❧ * | * * | * 🗡️ ║
    ║ * * | * * | * * ║
    ╚══════[👑]══════╝
    """,
    """
    ╔══════[🔔]══════╗
    ║ 🫅 * | * * | * ❧ ║
    ║ * * | *🕯️* | * * ║
    ║ 🌿 * | * * | * ♣ ║
    ║ * * | * * | * * ║
    ╚══════[🌴]══════╝
    """,
    """
    ╔═════[🌲🦜]═════╗
    ║ 🌿 * | * * | * 🪸 ║
    ║ * * | *🪄* | * * ║
    ║ 🪦 * | * * | * ❧ ║
    ║ * * | * * | * * ║
    ╚═════[🦢🌳]═════╝
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
    color = COLORS[new_index % len(COLORS)]
    try:
        colored_ascii = f"{color}{ascii_art}{Style.RESET_ALL}"
    except:
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
                f"Rune Pulses={player['rune_pulse']}, "
                f"Level={player['level']}, "
                f"Health={player['health']}/{player['max_health']}, "
                f"Strength={player['player_strength']}"
            )
            f.write(f"{timestamp} - {event_message} - {player_stats}\n")
    except Exception as e:
        print(Fore.MAGENTA + f"Failed to log event: {str(e)}" + Style.RESET_ALL)

def save_game():
    global player, companion_stats, current_companion, fallen_companions, stat_changes, rune_pulse_events
    game_state = {
        "player": {k: int(v) if isinstance(v, (int, float)) else v for k, v in player.items()},
        "companion_stats": {
            name: {k: int(v) if isinstance(v, (int, float)) else v for k, v in stats.items()}
            for name, stats in companion_stats.items()
        },
        "current_companion": {k: int(v) if isinstance(v, (int, float)) else v for k, v in current_companion.items()},
        "fallen_companions": fallen_companions,
        "rune_pulse_events": rune_pulse_events
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
    global player, companion_stats, current_companion, fallen_companions, stat_changes, rune_pulse_events
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
            "rune_pulse": 0, "player_strength": secrets.randbelow(10) + 5, "level": 1, "xp": 0, "xp_needed": 50
        }
        for key in default_player:
            if key in game_state.get("player", {}):
                player[key] = int(game_state["player"][key]) if key in [
                    "score", "health", "max_health", "runes", "healing_potion",
                    "magic_scroll", "mystic_key", "arcane_crystal", "rune_pulse",
                    "player_strength", "level", "xp", "xp_needed"
                ] else game_state["player"][key]
            else:
                player[key] = default_player[key]
        
        companion_stats.clear()
        companion_stats.update({
            name: {"health": min(secrets.randbelow(50) + 50, 100), "strength": secrets.randbelow(10) + 5, 
                   "class": secrets.choice(companion_classes)}
            for name in companions
        })
        for name, stats in game_state.get("companion_stats", {}).items():
            if name in companion_stats:
                companion_stats[name]["health"] = max(0, min(int(stats.get("health", companion_stats[name]["health"])), 100))
                companion_stats[name]["strength"] = int(stats.get("strength", companion_stats[name]["strength"]))
                companion_stats[name]["class"] = stats.get("class", companion_stats[name]["class"])
        
        current_companion_data = game_state.get("current_companion", {})
        current_companion["name"] = current_companion_data.get("name", "")
        if current_companion["name"] in companion_stats:
            current_companion["health"] = max(0, min(int(current_companion_data.get("health", companion_stats[current_companion["name"]]["health"])), 100))
            current_companion["strength"] = int(current_companion_data.get("strength", companion_stats[current_companion["name"]]["strength"]))
            current_companion["class"] = current_companion_data.get("class", companion_stats[current_companion["name"]]["class"])
            companion_stats[current_companion["name"]]["health"] = current_companion["health"]
        else:
            available_companions = [name for name in companions if name not in fallen_companions]
            new_companion_name = secrets.choice(available_companions) if available_companions else secrets.choice(companions)
            current_companion.update({
                "name": new_companion_name,
                "health": max(0, min(companion_stats[new_companion_name]["health"], 100)),
                "strength": companion_stats[new_companion_name]["strength"],
                "class": companion_stats[new_companion_name]["class"]
            })
            companion_stats[new_companion_name]["health"] = current_companion["health"]
        
        fallen_companions.clear()
        fallen_companions.extend(game_state.get("fallen_companions", []))
        rune_pulse_events = game_state.get("rune_pulse_events", 0)
        
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
    return die1, die2, outcome, outcome

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
    if not isinstance(changes, dict):
        return False
    try:
        return (changes.get("player_health", 0) >= 0 and
                changes.get("comp_health", 0) >= 0 and
                (changes.get("player_health", 0) > 0 or
                 changes.get("comp_health", 0) > 0 or
                 changes.get("runes", 0) > 0 or
                 changes.get("magic_scroll", 0) > 0 or
                 changes.get("mystic_key", 0) > 0 or
                 changes.get("arcane_crystal", 0) > 0 or
                 changes.get("rune_pulse", 0) > 0 or
                 changes.get("score", 0) > 0))
    except Exception:
        return False

def shop():
    global player, stat_changes
    while True:
        os.system("cls")
        print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.MAGENTA + "OGENS FANTASY NEXUS - D5+D10" + Style.RESET_ALL)
        print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.MAGENTA + get_random_ascii() + Style.RESET_ALL)
        print(Fore.MAGENTA + "\nMYSTIC BAZAAR..." + Style.RESET_ALL)
        print(Fore.CYAN + f"Runes: {player['runes']}" + Style.RESET_ALL)
        price_modifier = secrets.randbelow(51) / 100 + 0.25  # 0.25 to 0.75
        items = [
            f"Healing Potion - Price: {int(50 * (1 + price_modifier))} runes",
            f"Magic Scroll - Price: {int(75 * (1 + price_modifier))} runes",
            f"Mystic Key - Price: {int(100 * (1 + price_modifier))} runes",
            f"Arcane Crystal - Price: {int(125 * (1 + price_modifier))} runes"
        ]
        if secrets.randbelow(10) == 0:  # 10% chance for rare item
            items.append(f"Rune Pulse - Price: {int(150 * (1 + price_modifier))} runes")
        print(Fore.MAGENTA + "\nAvailable Items:" + Style.RESET_ALL)
        for i, item in enumerate(items, 1):
            print(Fore.MAGENTA + f"{i}. {item}" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"{len(items) + 1}. Return" + Style.RESET_ALL)
        shop_choice = input(Fore.MAGENTA + f"\nSelect an item (1-{len(items) + 1}): " + Style.RESET_ALL).strip()
        if shop_choice == str(len(items) + 1):
            return
        if shop_choice not in [str(i) for i in range(1, len(items) + 2)]:
            stat_changes = "Invalid choice"
            print(Fore.MAGENTA + "\nINVALID CHOICE..." + Style.RESET_ALL)
            print(Fore.MAGENTA + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nPress Enter to try again..." + Style.RESET_ALL)
            input()
            continue
        item_index = int(shop_choice) - 1
        if item_index >= len(items):
            stat_changes = "Invalid choice"
            print(Fore.MAGENTA + "\nINVALID CHOICE..." + Style.RESET_ALL)
            print(Fore.MAGENTA + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nPress Enter to try again..." + Style.RESET_ALL)
            input()
            continue
        item_name = items[item_index].split(" - ")[0]
        price = int(items[item_index].split("Price: ")[1].split(" ")[0])
        if player["runes"] < price:
            stat_changes = "Not enough runes"
            print(Fore.MAGENTA + "\nNot enough runes..." + Style.RESET_ALL)
            print(Fore.MAGENTA + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nPress Enter to try again..." + Style.RESET_ALL)
            input()
            continue
        player["runes"] -= price
        if item_name == "Healing Potion":
            player["healing_potion"] += 1
            stat_changes = f"Healing Potion +1, Runes -{price}"
        elif item_name == "Magic Scroll":
            player["magic_scroll"] += 1
            stat_changes = f"Magic Scroll +1, Runes -{price}"
        elif item_name == "Mystic Key":
            player["mystic_key"] += 1
            stat_changes = f"Mystic Key +1, Runes -{price}"
        elif item_name == "Arcane Crystal":
            player["arcane_crystal"] += 1
            stat_changes = f"Arcane Crystal +1, Runes -{price}"
        elif item_name == "Rune Pulse":
            player["rune_pulse"] += 1
            stat_changes = f"Rune Pulse +1, Runes -{price}"
        print(Fore.MAGENTA + f"\nPurchased {item_name}!" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
        print(Fore.MAGENTA + "\nPress Enter to continue..." + Style.RESET_ALL)
        input()

def path_outcomes(path, outcome):
    global player, current_companion, stat_changes, arcane_crystal_active, rune_pulse_events
    
    if not (1 <= outcome <= 50):
        raise ValueError(f"Invalid outcome {outcome}; must be between 1 and 50")

    outcomes_ancient_crypts = {
        1: ("Avoided a skeleton ambush, found runes!", {"runes": 20, "xp": 8}),
        2: ("Discovered a Healing Potion in a tomb!", {"healing_potion": 1, "xp": 6}),
        3: ("Deciphered a crypt rune, gained renown!", {"score": secrets.randbelow(10) + 10, "xp": 10}),
        4: ("Traded with a shade, earned runes!", {"runes": 25, "xp": 8}),
        5: ("Found a Mystic Key in a sarcophagus!", {"mystic_key": 1, "xp": 6}),
        6: ("Dodged a trap, vitality restored!", {"player_health": 3, "comp_health": 3, "xp": 6}),
        7: ("Recovered a Magic Scroll from a crypt!", {"magic_scroll": 1, "xp": 6}),
        8: ("Chanted a spell, gained runes!", {"runes": 15, "xp": 8}),
        9: ("Cursed trap drained your vitality!", {"player_health": -5, "comp_health": -5, "xp": 3}),
        10: ("Found an Arcane Crystal in a vault!", {"arcane_crystal": 1, "xp": 8}),
        11: ("Bargained with a ghost, gained runes!", {"runes": 20, "xp": 8}),
        12: ("Ancient elixir healed wounds!", {"player_health": 5, "comp_health": 5, "xp": 6}),
        13: ("Outwitted a wraith, gained wisdom!", {"xp": 10}),
        14: ("Looted runes from a crypt!", {"runes": 25, "xp": 8}),
        15: ("Found a Magic Scroll in a chest!", {"magic_scroll": 1, "xp": 6}),
        16: ("Chanted runes, boosted renown!", {"score": secrets.randbelow(10) + 15, "xp": 8}),
        17: ("Unearthed a Mystic Key in the dust!", {"mystic_key": 1, "xp": 6}),
        18: ("Skeleton ambush struck hard!", {"player_health": -6, "comp_health": -6, "xp": 3}),
        19: ("Defeated a wight, gained runes!", {"runes": 30, "xp": 8}),
        20: ("Snagged a Healing Potion from a shrine!", {"healing_potion": 1, "xp": 6}),
        21: ("Crypt collapse, injured!", {"player_health": -7, "comp_health": -7, "xp": 3}),
        22: ("Poisoned air sapped strength!", {"player_health": -8, "comp_health": -8, "xp": 3}),
        23: ("Cursed relic drained vitality!", {"player_health": -9, "comp_health": -9, "xp": 3}),
        24: ("Trapped by spectral chains!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        25: ("Wraith’s curse struck deep!", {"player_health": -11, "comp_health": -11, "xp": 3}),
        26: ("Mastered a rune, big renown!", {"score": secrets.randbelow(10) + 15, "xp": 8}),
        27: ("Cursed blade struck you!", {"player_health": -7, "comp_health": -7, "xp": 3}),
        28: ("Looted a crypt, gained runes!", {"runes": 40, "xp": 8}),
        29: ("Found runes in a hidden vault!", {"runes": 30, "xp": 8}),
        30: ("Learned ancient lore, gained wisdom!", {"xp": 12}),
        31: ("Phantom strike hit hard!", {"player_health": -12, "comp_health": -12, "xp": 3}),
        32: ("Ancient trap sprung!", {"player_health": -8, "comp_health": -8, "xp": 3}),
        33: ("Major rune haul from a crypt!", {"runes": 45, "xp": 8}),
        34: ("Found a Mystic Key in a vault!", {"mystic_key": 1, "xp": 6}),
        35: ("Cursed trap hit hard!", {"player_health": -8, "comp_health": -8, "xp": 3}),
        36: ("Chanted a powerful spell, big renown!", {"score": secrets.randbelow(10) + 20, "xp": 8}),
        37: ("Traded with a lich, gained runes!", {"runes": 35, "xp": 8}),
        38: ("Spectral surge drained you!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        39: ("Dodged a spectral trap, healed!", {"player_health": 3, "comp_health": 3, "xp": 6}),
        40: ("Overcame a guardian, gained wisdom!", {"xp": 15}),
        41: ("Ghoul attack wounded you!", {"player_health": -11, "comp_health": -11, "xp": 3}),
        42: ("Found an Arcane Crystal in a crypt!", {"arcane_crystal": 1, "xp": 8}),
        43: ("Crumbling tomb trapped you!", {"player_health": -9, "comp_health": -9, "xp": 3}),
        44: ("Found a Mystic Key in a shrine!", {"mystic_key": 1, "xp": 6}),
        45: ("Wraith attack drained you!", {"player_health": -9, "comp_health": -9, "xp": 3}),
        46: ("Chanted runes, earned runes!", {"runes": 55, "xp": 8}),
        47: ("Defeated a specter, gained runes!", {"runes": 40, "xp": 8}),
        48: ("Dark energy surge hit hard!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        49: ("Dodged a curse, vitality restored!", {"player_health": 4, "comp_health": 4, "xp": 6}),
        50: ("Rune Pulse found! (Doubles runes for 2 events)", {"rune_pulse": 1, "xp": 8})
    }

    outcomes_enchanted_forest = {
        1: ("Evaded a dire wolf, found runes!", {"runes": 25, "xp": 8}),
        2: ("Found a Healing Potion under a tree!", {"healing_potion": 1, "xp": 6}),
        3: ("Charmed a sprite, gained renown!", {"score": secrets.randbelow(10) + 15, "xp": 10}),
        4: ("Traded with a dryad, earned runes!", {"runes": 30, "xp": 8}),
        5: ("Found a Mystic Key in a glade!", {"mystic_key": 1, "xp": 6}),
        6: ("Healed by forest magic!", {"player_health": 3, "comp_health": 3, "xp": 6}),
        7: ("Found a Magic Scroll in a hollow!", {"magic_scroll": 1, "xp": 6}),
        8: ("Gained runes from a fairy!", {"runes": 20, "xp": 8}),
        9: ("Entangled by vines, hurt!", {"player_health": -6, "comp_health": -6, "xp": 3}),
        10: ("Found an Arcane Crystal in a spring!", {"arcane_crystal": 1, "xp": 8}),
        11: ("Befriended a fae, gained runes!", {"runes": 25, "xp": 8}),
        12: ("Forest spring healed you!", {"player_health": 6, "comp_health": 6, "xp": 6}),
        13: ("Outran a beast, gained wisdom!", {"xp": 10}),
        14: ("Traded with elves, earned runes!", {"runes": 30, "xp": 8}),
        15: ("Found a Magic Scroll in a grove!", {"magic_scroll": 1, "xp": 6}),
        16: ("Charmed a spirit, big renown!", {"score": secrets.randbelow(10) + 15, "xp": 8}),
        17: ("Found a Mystic Key in a tree!", {"mystic_key": 1, "xp": 6}),
        18: ("Beast attack struck hard!", {"player_health": -7, "comp_health": -7, "xp": 3}),
        19: ("Defeated a troll, gained runes!", {"runes": 35, "xp": 8}),
        20: ("Found a Healing Potion in a glade!", {"healing_potion": 1, "xp": 6}),
        21: ("Poisoned thorns struck you!", {"player_health": -8, "comp_health": -8, "xp": 3}),
        22: ("Fell into a hidden pit!", {"player_health": -9, "comp_health": -9, "xp": 3}),
        23: ("Dire beast clawed you!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        24: ("Enchanted vines ensnared you!", {"player_health": -11, "comp_health": -11, "xp": 3}),
        25: ("Cursed fog drained vitality!", {"player_health": -12, "comp_health": -12, "xp": 3}),
        26: ("Mastered forest magic, big renown!", {"score": secrets.randbelow(10) + 20, "xp": 8}),
        27: ("Wild boar charged you!", {"player_health": -7, "comp_health": -7, "xp": 3}),
        28: ("Found runes in a fairy ring!", {"runes": 45, "xp": 8}),
        29: ("Gained runes from a druid!", {"runes": 35, "xp": 8}),
        30: ("Learned forest lore, gained wisdom!", {"xp": 12}),
        31: ("Treant’s wrath hit hard!", {"player_health": -8, "comp_health": -8, "xp": 3}),
        32: ("Poisoned spores weakened you!", {"player_health": -9, "comp_health": -9, "xp": 3}),
        33: ("Major rune haul from a glade!", {"runes": 50, "xp": 8}),
        34: ("Found a Mystic Key in a hollow!", {"mystic_key": 1, "xp": 6}),
        35: ("Beast trap hit hard!", {"player_health": -9, "comp_health": -9, "xp": 3}),
        36: ("Charmed a spirit, huge renown!", {"score": secrets.randbelow(10) + 20, "xp": 8}),
        37: ("Traded with a nymph, gained runes!", {"runes": 40, "xp": 8}),
        38: ("Fae trick drained you!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        39: ("Dodged a trap, healed!", {"player_health": 4, "comp_health": 4, "xp": 6}),
        40: ("Overcame a beast, gained wisdom!", {"xp": 15}),
        41: ("Wolf pack ambushed you!", {"player_health": -11, "comp_health": -11, "xp": 3}),
        42: ("Found an Arcane Crystal in a glade!", {"arcane_crystal": 1, "xp": 8}),
        43: ("Enchanted briars struck you!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        44: ("Found a Mystic Key in a grove!", {"mystic_key": 1, "xp": 6}),
        45: ("Dire beast attacked!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        46: ("Learned forest magic, earned runes!", {"runes": 60, "xp": 8}),
        47: ("Defeated a wyrm, gained runes!", {"runes": 45, "xp": 8}),
        48: ("Toxic sap burned you!", {"player_health": -12, "comp_health": -12, "xp": 3}),
        49: ("Dodged a curse, vitality restored!", {"player_health": 4, "comp_health": 4, "xp": 6}),
        50: ("Rune Pulse found! (Doubles runes for 2 events)", {"rune_pulse": 1, "xp": 8})
    }

    outcomes_mystic_ruins = {
        1: ("Bypassed a golem, found runes!", {"runes": 30, "xp": 8}),
        2: ("Found a Healing Potion in ruins!", {"healing_potion": 1, "xp": 6}),
        3: ("Deciphered a rune, big renown!", {"score": secrets.randbelow(10) + 20, "xp": 10}),
        4: ("Traded with a spirit, earned runes!", {"runes": 35, "xp": 8}),
        5: ("Found a Mystic Key in a ruin!", {"mystic_key": 1, "xp": 6}),
        6: ("Healed by ancient magic!", {"player_health": 4, "comp_health": 4, "xp": 6}),
        7: ("Found a Magic Scroll in a ruin!", {"magic_scroll": 1, "xp": 6}),
        8: ("Chanted runes, gained runes!", {"runes": 25, "xp": 8}),
        9: ("Rune trap drained you!", {"player_health": -7, "comp_health": -7, "xp": 3}),
        10: ("Found an Arcane Crystal in a vault!", {"arcane_crystal": 1, "xp": 8}),
        11: ("Bargained with a shade, gained runes!", {"runes": 30, "xp": 8}),
        12: ("Ancient shrine healed you!", {"player_health": 7, "comp_health": 7, "xp": 6}),
        13: ("Outwitted a guardian, gained wisdom!", {"xp": 10}),
        14: ("Looted runes from ruins!", {"runes": 35, "xp": 8}),
        15: ("Found a Magic Scroll in a vault!", {"magic_scroll": 1, "xp": 6}),
        16: ("Mastered a rune, big renown!", {"score": secrets.randbelow(10) + 20, "xp": 8}),
        17: ("Found a Mystic Key in a ruin!", {"mystic_key": 1, "xp": 6}),
        18: ("Golem attack struck hard!", {"player_health": -8, "comp_health": -8, "xp": 3}),
        19: ("Defeated a sentinel, gained runes!", {"runes": 40, "xp": 8}),
        20: ("Found a Healing Potion in a shrine!", {"healing_potion": 1, "xp": 6}),
        21: ("Collapsing ruin injured you!", {"player_health": -9, "comp_health": -9, "xp": 3}),
        22: ("Rune surge burned you!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        23: ("Guardian trap crushed you!", {"player_health": -11, "comp_health": -11, "xp": 3}),
        24: ("Cursed stone drained vitality!", {"player_health": -12, "comp_health": -12, "xp": 3}),
        25: ("Ancient ward struck you!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        26: ("Chanted a spell, huge renown!", {"score": secrets.randbelow(10) + 25, "xp": 8}),
        27: ("Rune trap hit hard!", {"player_health": -9, "comp_health": -9, "xp": 3}),
        28: ("Looted a vault, gained runes!", {"runes": 50, "xp": 8}),
        29: ("Found runes in a hidden chamber!", {"runes": 40, "xp": 8}),
        30: ("Learned ancient secrets, gained wisdom!", {"xp": 12}),
        31: ("Golem’s fist smashed you!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        32: ("Falling debris hit hard!", {"player_health": -8, "comp_health": -8, "xp": 3}),
        33: ("Major rune haul from a vault!", {"runes": 55, "xp": 8}),
        34: ("Found a Mystic Key in a chamber!", {"mystic_key": 1, "xp": 6}),
        35: ("Guardian trap hit hard!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        36: ("Mastered a spell, huge renown!", {"score": secrets.randbelow(10) + 25, "xp": 8}),
        37: ("Traded with a spirit, gained runes!", {"runes": 45, "xp": 8}),
        38: ("Arcane backlash drained you!", {"player_health": -11, "comp_health": -11, "xp": 3}),
        39: ("Dodged a rune trap, healed!", {"player_health": 4, "comp_health": 4, "xp": 6}),
        40: ("Overcame a guardian, gained wisdom!", {"xp": 15}),
        41: ("Sentinel’s strike wounded you!", {"player_health": -12, "comp_health": -12, "xp": 3}),
        42: ("Found an Arcane Crystal in a ruin!", {"arcane_crystal": 1, "xp": 8}),
        43: ("Cursed rune exploded!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        44: ("Found a Mystic Key in a vault!", {"mystic_key": 1, "xp": 6}),
        45: ("Rune surge drained you!", {"player_health": -11, "comp_health": -11, "xp": 3}),
        46: ("Mastered ruin magic, earned runes!", {"runes": 65, "xp": 8}),
        47: ("Defeated a golem, gained runes!", {"runes": 50, "xp": 8}),
        48: ("Ancient trap sprung on you!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        49: ("Dodged a trap, vitality restored!", {"player_health": 4, "comp_health": 4, "xp": 6}),
        50: ("Rune Pulse found! (Doubles runes for 2 events)", {"rune_pulse": 1, "xp": 8})
    }

    outcomes_shadow_realm = {
        1: ("Evaded a shadow beast, found runes!", {"runes": 20, "xp": 8}),
        2: ("Found a Healing Potion in the dark!", {"healing_potion": 1, "xp": 6}),
        3: ("Banished a shade, gained renown!", {"score": secrets.randbelow(10) + 10, "xp": 10}),
        4: ("Traded with a wraith, earned runes!", {"runes": 25, "xp": 8}),
        5: ("Found a Mystic Key in the shadows!", {"mystic_key": 1, "xp": 6}),
        6: ("Survived a dark surge, healed!", {"player_health": 3, "comp_health": 3, "xp": 6}),
        7: ("Found a Magic Scroll in a void!", {"magic_scroll": 1, "xp": 6}),
        8: ("Chanted runes, gained runes!", {"runes": 15, "xp": 8}),
        9: ("Shadow trap drained you!", {"player_health": -5, "comp_health": -5, "xp": 3}),
        10: ("Found an Arcane Crystal in the dark!", {"arcane_crystal": 1, "xp": 8}),
        11: ("Bargained with a demon, gained runes!", {"runes": 20, "xp": 8}),
        12: ("Dark shrine healed you!", {"player_health": 5, "comp_health": 5, "xp": 6}),
        13: ("Outwitted a shadow, gained wisdom!", {"xp": 10}),
        14: ("Looted runes from a void!", {"runes": 25, "xp": 8}),
        15: ("Found a Magic Scroll in a shrine!", {"magic_scroll": 1, "xp": 6}),
        16: ("Banished a spirit, big renown!", {"score": secrets.randbelow(10) + 15, "xp": 8}),
        17: ("Found a Mystic Key in a void!", {"mystic_key": 1, "xp": 6}),
        18: ("Shadow beast struck hard!", {"player_health": -6, "comp_health": -6, "xp": 3}),
        19: ("Defeated a demon, gained runes!", {"runes": 30, "xp": 8}),
        20: ("Found a Healing Potion in a shrine!", {"healing_potion": 1, "xp": 6}),
        21: ("Dark surge hit hard!", {"player_health": -7, "comp_health": -7, "xp": 3}),
        22: ("Shadow tendrils ensnared you!", {"player_health": -8, "comp_health": -8, "xp": 3}),
        23: ("Cursed void drained vitality!", {"player_health": -9, "comp_health": -9, "xp": 3}),
        24: ("Demon’s claw struck you!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        25: ("Nightmare’s gaze weakened you!", {"player_health": -11, "comp_health": -11, "xp": 3}),
        26: ("Mastered dark magic, big renown!", {"score": secrets.randbelow(10) + 15, "xp": 8}),
        27: ("Shadow surge hit hard!", {"player_health": -7, "comp_health": -7, "xp": 3}),
        28: ("Looted a void, gained runes!", {"runes": 40, "xp": 8}),
        29: ("Found runes in a dark shrine!", {"runes": 30, "xp": 8}),
        30: ("Learned shadow lore, gained wisdom!", {"xp": 12}),
        31: ("Phantom strike drained you!", {"player_health": -8, "comp_health": -8, "xp": 3}),
        32: ("Dark miasma poisoned you!", {"player_health": -9, "comp_health": -9, "xp": 3}),
        33: ("Major rune haul from a void!", {"runes": 45, "xp": 8}),
        34: ("Found a Mystic Key in a shrine!", {"mystic_key": 1, "xp": 6}),
        35: ("Shadow trap hit hard!", {"player_health": -8, "comp_health": -8, "xp": 3}),
        36: ("Banished a demon, huge renown!", {"score": secrets.randbelow(10) + 20, "xp": 8}),
        37: ("Traded with a wraith, gained runes!", {"runes": 35, "xp": 8}),
        38: ("Void energy burned you!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        39: ("Dodged a dark trap, healed!", {"player_health": 3, "comp_health": 3, "xp": 6}),
        40: ("Overcame a shadow, gained wisdom!", {"xp": 15}),
        41: ("Shadow beast clawed you!", {"player_health": -11, "comp_health": -11, "xp": 3}),
        42: ("Found an Arcane Crystal in a void!", {"arcane_crystal": 1, "xp": 8}),
        43: ("Dark curse struck you!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        44: ("Found a Mystic Key in a shrine!", {"mystic_key": 1, "xp": 6}),
        45: ("Shadow beast drained you!", {"player_health": -9, "comp_health": -9, "xp": 3}),
        46: ("Learned dark magic, earned runes!", {"runes": 55, "xp": 8}),
        47: ("Defeated a nightmare, gained runes!", {"runes": 40, "xp": 8}),
        48: ("Cursed shadow attacked!", {"player_health": -10, "comp_health": -10, "xp": 3}),
        49: ("Dodged a curse, vitality restored!", {"player_health": 4, "comp_health": 4, "xp": 6}),
        50: ("Rune Pulse found! (Doubles runes for 2 events)", {"rune_pulse": 1, "xp": 8})
    }

    outcomes_dict = {
        1: outcomes_ancient_crypts,
        2: outcomes_enchanted_forest,
        3: outcomes_mystic_ruins,
        4: outcomes_shadow_realm
    }
    
    outcomes = outcomes_dict.get(int(path), outcomes_ancient_crypts)
    result, changes = outcomes.get(outcome, ("No outcome defined for this path", {}))

    # Apply Rune Pulse effect
    if rune_pulse_events > 0 and "runes" in changes and changes["runes"] > 0:
        changes["runes"] *= 2
        rune_pulse_events -= 1
        changes["rune_pulse_message"] = f"Runes doubled by Rune Pulse ({rune_pulse_events} events left)"
    elif rune_pulse_events > 0 and ("runes" not in changes or changes["runes"] <= 0):
        changes["runes"] = changes.get("runes", 0) + 2
        rune_pulse_events -= 1
        changes["rune_pulse_message"] = f"No rune gain, +2 runes from Rune Pulse ({rune_pulse_events} events left)"

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
        if "rune_pulse" in changes and changes["rune_pulse"] > 0:
            changes["rune_pulse"] += class_mod.get("rune_boost", 0)

    # Ensure health changes are capped
    changes["player_health"] = max(changes.get("player_health", 0), -100)
    changes["comp_health"] = max(changes.get("comp_health", 0), -100)

    # Cap companion health at 0-100 after applying changes
    if current_companion["name"]:
        current_companion["health"] = max(0, min(current_companion["health"] + changes.get("comp_health", 0), 100))
        companion_stats[current_companion["name"]]["health"] = current_companion["health"]
    else:
        changes["comp_health"] = 0

    # Handle fallen companion revival on positive outcomes
    was_fallen = current_companion["name"] in fallen_companions
    if was_fallen and is_positive_outcome(changes):
        changes["comp_health"] += 10
        current_companion["health"] = max(0, min(current_companion["health"] + 10, 100))
        companion_stats[current_companion["name"]]["health"] = current_companion["health"]
        if current_companion["name"] in fallen_companions:
            fallen_companions.remove(current_companion["name"])
            changes["revival_message"] = f"{current_companion['name']} revived with +10 health"

    return result, changes

def inventory():
    global player, current_companion, stat_changes, arcane_crystal_active, rune_pulse_events
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
        print(Fore.CYAN + f"Rune Pulse ({player['rune_pulse']}): Doubles rune gains for the next two events..." + Style.RESET_ALL)
        print(Fore.MAGENTA + "\nUSE AN ITEM..." + Style.RESET_ALL)
        print(Fore.MAGENTA + "1. Healing Potion (+25 player health, +20 companion health)" + Style.RESET_ALL)
        print(Fore.MAGENTA + "2. Magic Scroll (+20 score)" + Style.RESET_ALL)
        print(Fore.MAGENTA + "3. Mystic Key (+4 runes)" + Style.RESET_ALL)
        print(Fore.MAGENTA + "4. Arcane Crystal (Double score next event)" + Style.RESET_ALL)
        print(Fore.MAGENTA + "5. Rune Pulse (Double runes for two events)" + Style.RESET_ALL)
        print(Fore.MAGENTA + "6. Return" + Style.RESET_ALL)
        inv_choice = input(Fore.MAGENTA + "\nSelect an item (1-6): " + Style.RESET_ALL).strip()
        if inv_choice not in ["1", "2", "3", "4", "5", "6"]:
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
            if player["rune_pulse"] > 0:
                player["rune_pulse"] -= 1
                rune_pulse_events = 2
                stat_changes = "Rune Pulse used - Runes doubled for next two events, Rune Pulses -1"
                print(Fore.MAGENTA + "\nRune Pulse used - Next two events' rune gains will be doubled..." + Style.RESET_ALL)
            else:
                stat_changes = "No Rune Pulses remain"
                print(Fore.MAGENTA + "\nNo Rune Pulses remain..." + Style.RESET_ALL)
        elif inv_choice == "6":
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
        print(Fore.MAGENTA + f"{name} {status} - Class: {Fore.MAGENTA}{companion_stats[name]['class']}{Style.RESET_ALL}, Health: {Fore.RED}{companion_stats[name]['health']}{Style.RESET_ALL}, Strength: {Fore.WHITE}{companion_stats[name]['strength']}{Style.RESET_ALL}" + Style.RESET_ALL)
    print(Fore.MAGENTA + f"\nCurrent Companion: {current_companion['name']} ({current_companion['class']})" + Style.RESET_ALL)
    print(Fore.MAGENTA + "\nPress Enter to return..." + Style.RESET_ALL)
    stat_changes = "Viewed companions list"
    input()

def main():
    global player, current_companion, stat_changes, arcane_crystal_active, rune_pulse_events, fallen_companions, last_path_chosen
    player.update({
        "score": 0,
        "health": 100,
        "max_health": 200,
        "runes": 0,
        "healing_potion": 0,
        "magic_scroll": 0,
        "mystic_key": 0,
        "arcane_crystal": 0,
        "rune_pulse": 0,
        "player_strength": secrets.randbelow(10) + 5,
        "level": 1,
        "xp": 0,
        "xp_needed": 50
    })
    current_companion.update({
        "name": "",
        "health": 0,
        "strength": 0,
        "class": ""
    })
    fallen_companions.clear()
    arcane_crystal_active = False
    rune_pulse_events = 0
    stat_changes = ""
    last_path_chosen = None
    
    companion_stats.clear()
    companion_stats.update({
        name: {
            "health": max(0, min(secrets.randbelow(50) + 50, 100)),
            "strength": secrets.randbelow(10) + 5,
            "class": secrets.choice(companion_classes)
        } for name in companions
    })

    companion_name = secrets.choice(companions)
    current_companion.update({
        "name": companion_name,
        "health": max(0, min(companion_stats[companion_name]["health"], 100)),
        "strength": companion_stats[companion_name]["strength"],
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
        print(Fore.RED + f"Health: {player['health']}" + Style.RESET_ALL + Fore.YELLOW + f"  Score: {player['score']}" + Style.RESET_ALL + Fore.CYAN + f"  Runes: {player['runes']}" + Style.RESET_ALL + Fore.BLUE + f"  Arcane Crystals: {player['arcane_crystal']}" + Style.RESET_ALL + Fore.CYAN + f"  Rune Pulses: {player['rune_pulse']}" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"Progress: Score {player['score']}/6000 Runes {player['runes']}/300 Arcane Crystals {player['arcane_crystal']}/50" + Style.RESET_ALL)
        if current_companion["name"]:
            print(Fore.MAGENTA + f"\nCompanion: {Fore.MAGENTA}{current_companion['name']} ({current_companion['class']}{Style.RESET_ALL}) (Health: {Fore.RED}{current_companion['health']}{Style.RESET_ALL}, Strength: {Fore.WHITE}{current_companion['strength']}{Style.RESET_ALL})" + Style.RESET_ALL)
        if stat_changes:
            print(Fore.MAGENTA + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
        print(Fore.MAGENTA + "\nPath Chosen:" + Style.RESET_ALL)
        print(get_path_dial())

        if player["score"] >= 6000 and player["runes"] >= 300 and player["arcane_crystal"] >= 50:
            pygame.mixer.music.stop()
            os.system("cls")
            print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.MAGENTA + "OGENS FANTASY NEXUS - VICTORY" + Style.RESET_ALL)
            print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.MAGENTA + get_random_ascii() + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nVICTORY! YOU HAVE CONQUERED THE MYSTIC REALM!" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Final Runes: {player['runes']}" + Style.RESET_ALL)
            print(Fore.BLUE + f"Final Arcane Crystals: {player['arcane_crystal']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Final Rune Pulses: {player['rune_pulse']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Level: {player['level']}" + Style.RESET_ALL)
            print(Fore.RED + f"Final Health: {player['health']}/{player['max_health']}" + Style.RESET_ALL)
            print(Fore.WHITE + f"Final Strength: {player['player_strength']}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nYour legend will echo through the ages..." + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nPress Enter to exit..." + Style.RESET_ALL)
            log_event("Game won")
            input()
            pygame.quit()
            break

        if player["health"] <= 0:
            pygame.mixer.music.stop()
            os.system("cls")
            print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.MAGENTA + "OGENS FANTASY NEXUS - DEFEAT" + Style.RESET_ALL)
            print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.MAGENTA + get_random_ascii() + Style.RESET_ALL)
            print(Fore.RED + "\nDEFEAT! The Mystic Realm has claimed you..." + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Final Runes: {player['runes']}" + Style.RESET_ALL)
            print(Fore.BLUE + f"Final Arcane Crystals: {player['arcane_crystal']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Final Rune Pulses: {player['rune_pulse']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Level: {player['level']}" + Style.RESET_ALL)
            print(Fore.RED + f"Final Health: {player['health']}/{player['max_health']}" + Style.RESET_ALL)
            print(Fore.WHITE + f"Final Strength: {player['player_strength']}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nYour journey ends here..." + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nPress Enter to exit..." + Style.RESET_ALL)
            log_event("Game lost")
            input()
            pygame.quit()
            break

        print(Fore.MAGENTA + "\nCHOOSE YOUR PATH..." + Style.RESET_ALL)
        print(Fore.MAGENTA + "0. Mystic Bazaar" + Style.RESET_ALL)
        print(Fore.MAGENTA + "1. Ancient Crypts" + Style.RESET_ALL)
        print(Fore.MAGENTA + "2. Enchanted Forest" + Style.RESET_ALL)
        print(Fore.MAGENTA + "3. Mystic Ruins" + Style.RESET_ALL)
        print(Fore.MAGENTA + "4. Shadow Realm" + Style.RESET_ALL)
        print(Fore.MAGENTA + "5. Inventory" + Style.RESET_ALL)
        print(Fore.MAGENTA + "6. Companions" + Style.RESET_ALL)
        print(Fore.MAGENTA + "7. Save Game" + Style.RESET_ALL)
        print(Fore.MAGENTA + "8. Load Game" + Style.RESET_ALL)
        print(Fore.MAGENTA + "9. Exit" + Style.RESET_ALL)
        choice = input(Fore.MAGENTA + "\nSelect a path (0-9): " + Style.RESET_ALL).strip()

        if choice in ["1", "2", "3", "4"]:
            last_path_chosen = choice
            companion_name = secrets.choice(companions)
            current_companion.update({
                "name": companion_name,
                "health": max(0, min(companion_stats[companion_name]["health"], 100)),
                "strength": companion_stats[companion_name]["strength"],
                "class": companion_stats[companion_name]["class"]
            })
            companion_stats[companion_name]["health"] = current_companion["health"]
            pre_player_health = player["health"]
            pre_comp_health = current_companion["health"] if current_companion["name"] else 0

            die1, die2, outcome, _ = roll_dice()
            result, changes = path_outcomes(int(choice), outcome)
            was_fallen = current_companion["name"] in fallen_companions
            print(Fore.MAGENTA + f"\n{current_companion['name']} ({current_companion['class']}{Style.RESET_ALL}) {'(Fallen) ' if was_fallen else ''}joins you for this quest..." + Style.RESET_ALL)
            print(Fore.MAGENTA + f"\nDice Roll: D5={die1}, D10={die2}, Outcome={outcome}" + Style.RESET_ALL)
            print(Fore.MAGENTA + f"\nResult: {result}" + Style.RESET_ALL)

            arcane_crystal_message = ""
            if arcane_crystal_active and "score" in changes and changes["score"] > 0:
                changes["score"] *= 2
                arcane_crystal_message = "Score doubled by Arcane Crystal"
                arcane_crystal_active = False
            elif arcane_crystal_active and ("score" not in changes or changes["score"] <= 0):
                changes["score"] = (changes.get("score", 0) + 5)
                arcane_crystal_message = "No score gain, +5 score from Arcane Crystal"
                arcane_crystal_active = False

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
            pulse_change = changes.get("rune_pulse", 0)
            player["rune_pulse"] += pulse_change
            potion_change = changes.get("healing_potion", 0)
            player["healing_potion"] += potion_change
            key_change = changes.get("mystic_key", 0)
            player["mystic_key"] += key_change
            xp_change = changes.get("xp", 0)
            levelup_health_change = level_check(xp_change)
            post_player_health = player["health"]
            post_comp_health = current_companion["health"] if current_companion["name"] else 0

            actual_comp_health_change = post_comp_health - pre_comp_health if current_companion["name"] else 0

            stat_changes_list = []
            if score_change != 0:
                stat_changes_list.append(Fore.YELLOW + f"Score {'+' if score_change > 0 else ''}{score_change}" + Style.RESET_ALL)
            if arcane_crystal_message:
                stat_changes_list.append(Fore.BLUE + arcane_crystal_message + Style.RESET_ALL)
            if changes.get("rune_pulse_message"):
                stat_changes_list.append(Fore.CYAN + changes["rune_pulse_message"] + Style.RESET_ALL)
            if was_fallen and is_positive_outcome(changes):
                stat_changes_list.append(Fore.MAGENTA + f"{current_companion['name']} revived with +10 health" + Style.RESET_ALL)
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
            if pulse_change != 0:
                stat_changes_list.append(Fore.CYAN + f"Rune Pulses {'+' if pulse_change > 0 else ''}{pulse_change}" + Style.RESET_ALL)
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

        elif choice == "0":
            shop()
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
            pygame.mixer.music.stop()
            os.system("cls")
            print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.MAGENTA + "OGENS FANTASY NEXUS - EXIT" + Style.RESET_ALL)
            print(Fore.MAGENTA + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.MAGENTA + get_random_ascii() + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nLeaving the Mystic Realm..." + Style.RESET_ALL)
            print(Fore.YELLOW + f"Final Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Final Runes: {player['runes']}" + Style.RESET_ALL)
            print(Fore.BLUE + f"Final Arcane Crystals: {player['arcane_crystal']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"Final Rune Pulses: {player['rune_pulse']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Level: {player['level']}" + Style.RESET_ALL)
            print(Fore.RED + f"Final Health: {player['health']}/{player['max_health']}" + Style.RESET_ALL)
            print(Fore.WHITE + f"Final Strength: {player['player_strength']}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nPress Enter to exit..." + Style.RESET_ALL)
            log_event("Game quit")
            input()
            pygame.quit()
            break
        else:
            stat_changes = "Invalid choice"
            print(Fore.MAGENTA + "\nINVALID CHOICE..." + Style.RESET_ALL)
            print(Fore.MAGENTA + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "\nPress Enter to try again..." + Style.RESET_ALL)
            input()

if __name__ == "__main__":
    main()