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
    "nano_medpack": 0,
    "data_shard": 0,
    "crypto_key": 0,
    "quantum_mod": 0,
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
quantum_mod_active = False
stat_changes = ""

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
        print(Fore.GREEN + "Your data is uploaded to the grid!" + Style.RESET_ALL)
        stat_changes = "Data uploaded to the grid"
    except Exception as e:
        if os.path.exists("SaveGame.bak"):
            os.rename("SaveGame.bak", "SaveGame.txt")
            print(Fore.GREEN + f"Failed to upload data, restored from backup... Error: {str(e)}" + Style.RESET_ALL)
            stat_changes = f"Failed to upload data, restored from backup: {str(e)}"
        else:
            print(Fore.GREEN + f"Failed to upload data, no backup available... Error: {str(e)}" + Style.RESET_ALL)
            stat_changes = f"Failed to upload data, no backup available: {str(e)}"
        with open("GameLog.txt", "a") as f:
            f.write(f"{datetime.now().strftime('%m/%d/%Y %H:%M')} - Save failed: {str(e)}\n")
    return stat_changes

# Load game from file
def load_game():
    global player, companion_stats, current_companion, fallen_companions, stat_changes
    if not os.path.exists("SaveGame.txt"):
        print(Fore.GREEN + "No saved data found..." + Style.RESET_ALL)
        stat_changes = "No saved data found"
        return
    try:
        with open("SaveGame.txt", "r") as f:
            game_state = json.load(f)
        
        default_player = {
            "score": 0, "health": 100, "max_health": 200, "artifacts": 0,
            "nano_medpack": 0, "data_shard": 0, "crypto_key": 0, "quantum_mod": 0,
            "player_strength": secrets.randbelow(10) + 5, "level": 1, "xp": 0, "xp_needed": 50
        }
        for key in default_player:
            if key in game_state.get("player", {}):
                player[key] = int(game_state["player"][key]) if key in [
                    "score", "health", "max_health", "artifacts", "nano_medpack",
                    "data_shard", "crypto_key", "quantum_mod", "player_strength", "level", "xp", "xp_needed"
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
        
        print(Fore.GREEN + "The grid restores your data!" + Style.RESET_ALL)
        stat_changes = "Data restored from the grid"
    except Exception as e:
        print(Fore.GREEN + f"Failed to load data... Error: {str(e)}" + Style.RESET_ALL)
        stat_changes = f"Failed to load data: {str(e)}"
        with open("GameLog.txt", "a") as f:
            f.write(f"{datetime.now().strftime('%m/%d/%Y %H:%M')} - Load failed: {str(e)}\n")
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
        if player["nano_medpack"] < 3:
            player["nano_medpack"] += 1
            stat_changes = f"Level {player['level']} reached, Max Health +10, Health +5, Nano-Medpacks +1"
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
             changes.get("nano_medpack", 0) > 0 or
             changes.get("data_shard", 0) > 0 or
             changes.get("crypto_key", 0) > 0 or
             changes.get("quantum_mod", 0) > 0 or
             changes.get("score", 0) > 0))

# Path outcomes
def path_outcomes(path, adjusted_grid):
    global player, current_companion, stat_changes, quantum_mod_active
    outcomes = {
        1: {
            1: ("Stealth Success: You bypass security drones, snagging a Data Core", {"score": 8 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            2: ("Stealth Betrayal: Your fixer sells you out, security closes in", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            3: ("Stealth Trap: Motion sensors trigger turrets", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            4: ("Stealth Chaos: You slip through, but knock over a server rack", {"score": 3 + player["level"], "xp": 5, "comp_health": -5 + current_companion["strength"], "player_health": -5 + player["player_strength"]}),
            5: ("Stealth Success: You evade patrols, gain a Nano-Medpack", {"score": 5 + player["level"], "nano_medpack": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            6: ("Combat Success: You blast through guards, find a Quantum Mod", {"score": 7 + player["level"], "artifacts": 1, "quantum_mod": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            7: ("Combat Betrayal: Your hired muscle turns on you", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            8: ("Combat Trap: Explosive mines detonate", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            9: ("Combat Success: You clear the vault, snag a Data Core", {"score": 4 + player["level"], "artifacts": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            10: ("Combat Escalation: Reinforcements swarm the vault", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            11: ("Social Success: You bribe a guard, gain a Data Core", {"score": 6 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            12: ("Social Betrayal: The guard rats you out to the corp", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            13: ("Social Success: You charm a tech, gain a Crypto Key", {"score": 5 + player["level"], "crypto_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            14: ("Social Success: You negotiate access, gain a Data Shard", {"score": 3 + player["level"], "data_shard": 1, "xp": 5, "player_health": 4, "comp_health": 4}),
            15: ("Social Escalation: Your talk draws corpo enforcers", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            16: ("Hacking Success: You crack the mainframe, find a Nano-Medpack", {"score": 8 + player["level"], "nano_medpack": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            17: ("Hacking Betrayal: Your ICEbreaker backdoors you", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            18: ("Hacking Trap: Black ICE fries your rig", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            19: ("Hacking Success: You salvage data from a crashed system", {"score": 4 + player["level"], "artifacts": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            20: ("Hacking Escalation: Your breach alerts the netrunners", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            21: ("Intimidation Success: You scare off guards, snag a Crypto Key", {"score": 5 + player["level"], "crypto_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            22: ("Intimidation Betrayal: Your threats backfire, guards attack", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            23: ("Intimidation Success: You bully a tech, gain a Quantum Mod", {"score": 5 + player["level"], "quantum_mod": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            24: ("Intimidation Success: You clear the vault, gain a Data Core", {"score": 6 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            25: ("Intimidation Trap: Your show of force triggers drones", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]})
        },
        2: {
            1: ("Stealth Betrayal: Your contact snitches to the gang", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            2: ("Stealth Trap: You trip a laser grid", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            3: ("Stealth Success: You slip through the market, snag a Data Shard", {"score": 4 + player["level"], "data_shard": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            4: ("Stealth Escalation: Your presence draws a gang hit squad", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            5: ("Combat Betrayal: Your ally switches sides mid-fight", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            6: ("Combat Trap: A hidden turret opens fire", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            7: ("Combat Success: You clear the market, gain a Data Core", {"score": 6 + player["level"], "artifacts": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            8: ("Combat Escalation: The fight draws rival gangs", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            9: ("Social Betrayal: The vendor tips off the gang", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            10: ("Social Trap: Your deal triggers a sting operation", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            11: ("Social Success: You charm a dealer, gain a Nano-Medpack", {"score": 5 + player["level"], "nano_medpack": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            12: ("Social Escalation: Your deal draws corpo spies", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            13: ("Hacking Betrayal: Your netrunner ally sells your code", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            14: ("Hacking Success: You hack a vendor’s rig, gain a Data Core", {"score": 8 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            15: ("Hacking Success: You crack a terminal, gain a Nano-Medpack", {"score": 6 + player["level"], "nano_medpack": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            16: ("Hacking Success: You salvage data, gain a Data Shard", {"score": 4 + player["level"], "data_shard": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            17: ("Intimidation Success: You strong-arm a deal, gain a Crypto Key", {"score": 5 + player["level"], "crypto_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            18: ("Intimidation Success: You clear the market, gain a Quantum Mod", {"score": 5 + player["level"], "quantum_mod": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            19: ("Intimidation Success: You intimidate a vendor, gain a Data Core", {"score": 6 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            20: ("Stealth Success: You slip past sentries, snag a Data Core", {"score": 8 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            21: ("Combat Success: You clear out gangers, find a Quantum Mod", {"score": 7 + player["level"], "artifacts": 1, "quantum_mod": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            22: ("Social Success: You barter for a Crypto Key", {"score": 5 + player["level"], "crypto_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            23: ("Hacking Success: You breach a node, gain a Crypto Key", {"score": 5 + player["level"], "crypto_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            24: ("Hacking Trap: A virus fries your deck", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            25: ("Hacking Escalation: Your breach pulls in net vigilantes", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]})
        },
        3: {
            1: ("Stealth Success: You sneak past execs, grab a Data Core", {"score": 8 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            2: ("Stealth Betrayal: Your insider tips off security", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            3: ("Stealth Trap: Biometric scanners lock you in", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            4: ("Stealth Success: You evade drones, gain a Data Shard", {"score": 3 + player["level"], "data_shard": 1, "xp": 5, "player_health": 4, "comp_health": 4}),
            5: ("Stealth Success: You bypass security, gain a Nano-Medpack", {"score": 5 + player["level"], "nano_medpack": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            6: ("Combat Success: You overpower security, find a Quantum Mod", {"score": 7 + player["level"], "artifacts": 1, "quantum_mod": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            7: ("Combat Betrayal: Your merc ally double-crosses you", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            8: ("Combat Trap: Automated turrets shred you", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            9: ("Combat Success: You clear the floor, gain a Data Core", {"score": 4 + player["level"], "artifacts": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            10: ("Combat Escalation: Elite enforcers swarm the floor", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            11: ("Social Success: You charm an exec, gain a Nano-Medpack", {"score": 6 + player["level"], "nano_medpack": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            12: ("Social Betrayal: The exec sets you up", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            13: ("Social Success: You bribe a guard, gain a Crypto Key", {"score": 5 + player["level"], "crypto_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            14: ("Social Success: You negotiate access, gain a Data Core", {"score": 6 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            15: ("Social Escalation: Your talk pulls in corpo hitmen", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            16: ("Hacking Success: You breach the spire’s net, grab a Data Core", {"score": 8 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            17: ("Hacking Betrayal: Your code is sold to a rival corp", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            18: ("Hacking Trap: A firewall fries your neural link", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            19: ("Hacking Success: You salvage data, gain a Quantum Mod", {"score": 4 + player["level"], "quantum_mod": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            20: ("Hacking Escalation: Your breach draws net enforcers", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            21: ("Intimidation Success: You bully a guard, gain a Data Shard", {"score": 5 + player["level"], "data_shard": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            22: ("Intimidation Betrayal: The guard calls for backup", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            23: ("Intimidation Success: You scare an exec, gain a Crypto Key", {"score": 5 + player["level"], "crypto_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            24: ("Intimidation Success: You clear the floor, gain a Data Core", {"score": 6 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            25: ("Intimidation Trap: Your threats trigger a gas trap", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]})
        },
        4: {
            1: ("Stealth Betrayal: Your avatar is sold out by a netrunner", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            2: ("Stealth Trap: A data trap zaps your avatar", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            3: ("Stealth Success: You bypass a firewall, gain a Data Shard", {"score": 4 + player["level"], "data_shard": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            4: ("Stealth Escalation: Your hack pulls in virtual enforcers", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            5: ("Combat Betrayal: Your co-hacker turns on you", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            6: ("Combat Trap: A kill-switch fries your link", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            7: ("Combat Success: You stabilize the grid, gain a Data Core", {"score": 6 + player["level"], "artifacts": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            8: ("Combat Escalation: Rogue AIs swarm your avatar", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            9: ("Social Betrayal: The sysadmin rats you out", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            10: ("Social Trap: Your ruse triggers a data lock", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            11: ("Social Success: You bluff a node operator, gain a Crypto Key", {"score": 5 + player["level"], "crypto_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            12: ("Social Escalation: Your talk draws net vigilantes", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]}),
            13: ("Hacking Betrayal: Your code is stolen by a rival", {"comp_health": -17 + current_companion["strength"], "xp": 1, "player_health": -17 + player["player_strength"]}),
            14: ("Hacking Success: You crack a secure node, find a Nano-Medpack", {"score": 8 + player["level"], "nano_medpack": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            15: ("Hacking Success: You breach a node, gain a Data Core", {"score": 6 + player["level"], "artifacts": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            16: ("Hacking Success: You salvage data, gain a Data Shard", {"score": 4 + player["level"], "data_shard": 1, "xp": 6, "player_health": 4, "comp_health": 4}),
            17: ("Intimidation Success: You scare off a netrunner, gain a Crypto Key", {"score": 5 + player["level"], "crypto_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            18: ("Intimidation Success: You clear the grid, gain a Quantum Mod", {"score": 5 + player["level"], "quantum_mod": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            19: ("Intimidation Success: You bully a node, gain a Data Core", {"score": 6 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            20: ("Stealth Success: You ghost through the net, snag a Data Core", {"score": 8 + player["level"], "artifacts": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            21: ("Combat Success: You shred ICE, find a Quantum Mod", {"score": 7 + player["level"], "artifacts": 1, "quantum_mod": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            22: ("Social Success: You bluff a sysadmin, gain a Data Shard", {"score": 6 + player["level"], "data_shard": 1, "xp": 10, "player_health": 4, "comp_health": 4}),
            23: ("Hacking Success: You crack a node, gain a Crypto Key", {"score": 5 + player["level"], "crypto_key": 1, "xp": 8, "player_health": 4, "comp_health": 4}),
            24: ("Hacking Trap: Black ICE zaps your neural link", {"comp_health": -15 + current_companion["strength"], "xp": 1, "player_health": -15 + player["player_strength"]}),
            25: ("Hacking Escalation: Your breach pulls in AI hunters", {"comp_health": -20 + current_companion["strength"], "xp": 1, "player_health": -20 + player["player_strength"]})
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
    global player, current_companion, stat_changes, quantum_mod_active
    while True:
        os.system("cls")
        print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.GREEN + "OGENS NEON NEXUS - D5+D5" + Style.RESET_ALL)
        print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.GREEN + "\n   //===\\\\" + Style.RESET_ALL)
        print(Fore.GREEN + "  // *** \\\\" + Style.RESET_ALL)
        print(Fore.GREEN + " //_______\\\\" + Style.RESET_ALL)
        print(Fore.GREEN + " |  ***  |" + Style.RESET_ALL)
        print(Fore.GREEN + " |_______|" + Style.RESET_ALL)
        print(Fore.GREEN + "\nGEAR CACHE..." + Style.RESET_ALL)
        print(Fore.GREEN + f"\nNano-Medpack ({player['nano_medpack']}): Restores vitality..." + Style.RESET_ALL)
        print(Fore.GREEN + f"Data Shard ({player['data_shard']}): Boosts cred..." + Style.RESET_ALL)
        print(Fore.GREEN + f"Crypto Key ({player['crypto_key']}): Unlocks data cores..." + Style.RESET_ALL)
        print(Fore.GREEN + f"Quantum Mod ({player['quantum_mod']}): Doubles score gains for the next event..." + Style.RESET_ALL)
        print(Fore.GREEN + "\nUSE AN ITEM..." + Style.RESET_ALL)
        print(Fore.GREEN + "1. Nano-Medpack (+25 health)" + Style.RESET_ALL)
        print(Fore.GREEN + "2. Data Shard (+20 score)" + Style.RESET_ALL)
        print(Fore.GREEN + "3. Crypto Key (+4 data cores)" + Style.RESET_ALL)
        print(Fore.GREEN + "4. Quantum Mod (Double score next event)" + Style.RESET_ALL)
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
            if player["nano_medpack"] > 0:
                pre_player_health = player["health"]
                pre_comp_health = current_companion["health"] if current_companion["name"] else 0
                player["health"] += 25
                player["nano_medpack"] -= 1
                if player["health"] > player["max_health"]:
                    player["health"] = player["max_health"]
                    stat_changes = f"Health capped at {player['max_health']}, Nano-Medpacks -1"
                else:
                    stat_changes = "Health +25, Nano-Medpacks -1"
                if current_companion["name"]:
                    current_companion["health"] = min(100, current_companion["health"] + 20)
                    companion_stats[current_companion["name"]]["health"] = current_companion["health"]
                    if current_companion["name"] in fallen_companions and current_companion["health"] > 0:
                        fallen_companions.remove(current_companion["name"])
                    stat_changes += f", {current_companion['name']}'s Health +20, Total Damage: Player [{pre_player_health} -> {player['health']}], Companion [{pre_comp_health} -> {current_companion['health']}]"
                else:
                    stat_changes += f", Total Damage: Player [{pre_player_health} -> {player['health']}]"
                print(Fore.GREEN + "\nNano-Medpack used - Vitality restored..." + Style.RESET_ALL)
            else:
                stat_changes = "No Nano-Medpacks remain"
                print(Fore.GREEN + "\nNo Nano-Medpacks remain..." + Style.RESET_ALL)
        elif inv_choice == "2":
            if player["data_shard"] > 0:
                player["score"] += 20
                player["data_shard"] -= 1
                stat_changes = "Score +20, Data Shards -1"
                print(Fore.GREEN + "\nData Shard used - Cred gained..." + Style.RESET_ALL)
            else:
                stat_changes = "No Data Shards remain"
                print(Fore.GREEN + "\nNo Data Shards remain..." + Style.RESET_ALL)
        elif inv_choice == "3":
            if player["crypto_key"] > 0:
                player["artifacts"] += 4
                player["crypto_key"] -= 1
                stat_changes = "Data Cores +4, Crypto Keys -1"
                print(Fore.GREEN + "\nCrypto Key used - Data cores unlocked..." + Style.RESET_ALL)
            else:
                stat_changes = "No Crypto Keys remain"
                print(Fore.GREEN + "\nNo Crypto Keys remain..." + Style.RESET_ALL)
        elif inv_choice == "4":
            if player["quantum_mod"] > 0:
                player["quantum_mod"] -= 1
                quantum_mod_active = True
                stat_changes = "Quantum Mod used - Score doubled for next event, Quantum Mods -1"
                print(Fore.GREEN + "\nQuantum Mod used - Next event's score gains will be doubled..." + Style.RESET_ALL)
            else:
                stat_changes = "No Quantum Mods remain"
                print(Fore.GREEN + "\nNo Quantum Mods remain..." + Style.RESET_ALL)
        elif inv_choice == "5":
            return
        print(Fore.GREEN + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
        print(Fore.GREEN + "\nPress Enter to return..." + Style.RESET_ALL)
        input()

# Main game loop
def main():
    global player, current_companion, stat_changes, quantum_mod_active, fallen_companions
    companion_name = companions[secrets.randbelow(len(companions))]
    current_companion.update({
        "name": companion_name,
        "health": companion_stats[companion_name]["health"],
        "strength": companion_stats[companion_name]["strength"],
        "luck": companion_stats[companion_name]["luck"]
    })
    companion_stats[companion_name]["health"] = current_companion["health"]

    os.system("cls")
    print(Fore.GREEN + """
   //===\\
  //     \\
 //_______\\
 |  ***  | NEON NEXUS
 |  ***  | SURVIVE THE UNDERWORLD
 |_______| 
    """ + Style.RESET_ALL)
    print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
    print(Fore.GREEN + "OGENS NEON NEXUS - D5+D5" + Style.RESET_ALL)
    print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
    print(Fore.GREEN + f"\nCompanion: {current_companion['name']} joins you in the underworld..." + Style.RESET_ALL)
    print(Fore.GREEN + "\n\n        Press Enter to hack in" + Style.RESET_ALL)
    print(Fore.GREEN + "    Neon Nexus Underworld..." + Style.RESET_ALL)
    input()

    while True:
        os.system("cls")
        score_change = 0
        player_health_change = 0
        comp_health_change = 0
        artifact_change = 0
        medpack_change = 0
        shard_change = 0
        key_change = 0
        mod_change = 0
        xp_change = 0
        levelup_health_change = 0
        show_health_change = False
        pre_player_health = player["health"]
        pre_comp_health = current_companion["health"] if current_companion["name"] else 0
        post_player_health = pre_player_health
        post_comp_health = pre_comp_health

        print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.GREEN + "OGENS NEON NEXUS - D5+D5" + Style.RESET_ALL)
        print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
        print(Fore.GREEN + "\nNAVIGATING THE NEON UNDERWORLD..." + Style.RESET_ALL)
        print(Fore.GREEN + f"\nStrength: {player['player_strength']}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Level: {player['level']} (XP: {player['xp']}/{player['xp_needed']})" + Style.RESET_ALL)
        print(Fore.GREEN + f"Health: {player['health']}  Score: {player['score']}  Data Cores: {player['artifacts']}  Quantum Mods: {player['quantum_mod']}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Progress: Score {player['score']}/6000 Data Cores {player['artifacts']}/300 Quantum Mods {player['quantum_mod']}/50" + Style.RESET_ALL)
        if current_companion["name"]:
            print(Fore.GREEN + f"\nCompanion: {current_companion['name']} (Health: {current_companion['health']}, Strength: {current_companion['strength']}, Luck: {current_companion['luck']})" + Style.RESET_ALL)
        if stat_changes:
            print(Fore.GREEN + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
        print(Fore.GREEN + "\n    1 2" + Style.RESET_ALL)
        print(Fore.GREEN + "   ( o )" + Style.RESET_ALL)
        print(Fore.GREEN + "    3 4" + Style.RESET_ALL)
        print(Fore.GREEN + "    NET" + Style.RESET_ALL)
        print(Fore.GREEN + "\nCHOOSE YOUR PATH..." + Style.RESET_ALL)
        print(Fore.GREEN + "Path 1 - Data Vaults (fortified server hub)" + Style.RESET_ALL)
        print(Fore.GREEN + "Path 2 - Neon Slums (gang-run black market)" + Style.RESET_ALL)
        print(Fore.GREEN + "Path 3 - Corporate Spire (megacorp skyscraper)" + Style.RESET_ALL)
        print(Fore.GREEN + "Path 4 - Darknet Grid (virtual reality network)" + Style.RESET_ALL)
        print(Fore.GREEN + "Path 5 - Inventory" + Style.RESET_ALL)
        print(Fore.GREEN + "Path 6 - Contact List" + Style.RESET_ALL)
        print(Fore.GREEN + "Path 7 - Save Game" + Style.RESET_ALL)
        print(Fore.GREEN + "Path 8 - Load Game" + Style.RESET_ALL)
        print(Fore.GREEN + "Path 9 - Quit" + Style.RESET_ALL)
        choice = input(Fore.GREEN + "\nEnter path (1-9): " + Style.RESET_ALL).strip()

        stat_changes = ""

        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            stat_changes = "Invalid path selected"
            print(Fore.GREEN + "\nINVALID PATH SELECTED..." + Style.RESET_ALL)
            print(Fore.GREEN + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
            print(Fore.GREEN + "\nPress Enter to try again..." + Style.RESET_ALL)
            input()
            continue

        if choice in ["1", "2", "3", "4"]:
            path = int(choice)
            path_displays = {
                1: """
   //===\\
   | *** |
   | *** |
   \\===//
""",
                2: """
   ------
   | *  |
   | *  |
   ------
""",
                3: """
   ||||
   |   |
   |   |
   ||||
""",
                4: """
   ~~~~~
   | ^ |
   | ^ |
   ~~~~~
"""
            }
            os.system("cls")
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + "OGENS NEON NEXUS - D5+D5" + Style.RESET_ALL)
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + f"\n{'INFILTRATING THE DATA VAULTS...' if path == 1 else 'NAVIGATING THE NEON SLUMS...' if path == 2 else 'ASCENDING THE CORPORATE SPIRE...' if path == 3 else 'HACKING INTO THE DARKNET GRID...'}" + Style.RESET_ALL)
            print(Fore.GREEN + path_displays[path] + Style.RESET_ALL)
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
            print(Fore.GREEN + f"{current_companion['name']} {'(Flatlined) ' if was_fallen else ''}joins you for this run..." + Style.RESET_ALL)
            die1, die2, outcome, adjusted_grid = roll_dice()
            print(Fore.GREEN + "Rolling for the path's challenge..." + Style.RESET_ALL)
            print(Fore.GREEN + f"Die 1 (D5): {die1} + Die 2 (D5): {die2} = Outcome {outcome} (Adjusted by Luck: {adjusted_grid})" + Style.RESET_ALL)
            result, changes = path_outcomes(path, adjusted_grid)
            revive_message = ""
            if was_fallen and is_positive_outcome(changes):
                revive_message = f"{current_companion['name']} is revived with +10 health!"
            quantum_mod_message = ""
            score_change = changes.get("score", 0)
            if quantum_mod_active:
                if score_change == 0:
                    score_change = 5
                    quantum_mod_message = "Quantum Mod grants +5 score"
                else:
                    score_change *= 2
                    quantum_mod_message = "Quantum Mod doubled score gain"
                quantum_mod_active = False
            player["score"] = min(10000000, max(0, player["score"] + score_change))
            player_health_change = changes.get("player_health", 0)
            comp_health_change = changes.get("comp_health", 0)
            player["artifacts"] += changes.get("artifacts", 0)
            player["nano_medpack"] += changes.get("nano_medpack", 0)
            player["data_shard"] += changes.get("data_shard", 0)
            player["crypto_key"] += changes.get("crypto_key", 0)
            player["quantum_mod"] += changes.get("quantum_mod", 0)
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
            if quantum_mod_message:
                stat_changes_list.append(quantum_mod_message)
            if revive_message:
                stat_changes_list.append(revive_message)
            if player_health_change != 0 or levelup_health_change != 0:
                total_health_change = player_health_change + levelup_health_change
                stat_changes_list.append(f"Health {'+' if total_health_change > 0 else ''}{total_health_change}")
                show_health_change = True
            if show_health_change:
                stat_changes_list.append(f"Total Damage: Player [{pre_player_health} -> {post_player_health}]" + (f", Companion [{pre_comp_health} -> {post_comp_health}]" if current_companion["name"] else ""))
            if changes.get("artifacts", 0) != 0:
                stat_changes_list.append(f"Data Cores {'+' if changes['artifacts'] > 0 else ''}{changes['artifacts']}")
            if changes.get("nano_medpack", 0) != 0:
                stat_changes_list.append(f"Nano-Medpacks {'+' if changes['nano_medpack'] > 0 else ''}{changes['nano_medpack']}")
            if changes.get("data_shard", 0) != 0:
                stat_changes_list.append(f"Data Shards {'+' if changes['data_shard'] > 0 else ''}{changes['data_shard']}")
            if changes.get("crypto_key", 0) != 0:
                stat_changes_list.append(f"Crypto Keys {'+' if changes['crypto_key'] > 0 else ''}{changes['crypto_key']}")
            if changes.get("quantum_mod", 0) != 0:
                stat_changes_list.append(f"Quantum Mods {'+' if changes['quantum_mod'] > 0 else ''}{changes['quantum_mod']}")
            if xp_change != 0:
                stat_changes_list.append(f"XP +{xp_change}")
            if comp_health_change != 0 and current_companion["name"]:
                stat_changes_list.append(f"{current_companion['name']}'s Health {'+' if comp_health_change > 0 else ''}{comp_health_change}")
            stat_changes = ", ".join(stat_changes_list) if stat_changes_list else stat_changes
            if current_companion["health"] <= 0 and current_companion["name"]:
                if current_companion["name"] not in fallen_companions:
                    fallen_companions.append(current_companion["name"])
                stat_changes = f"{stat_changes}, {current_companion['name']} has been flatlined..." if stat_changes else f"{current_companion['name']} has been flatlined..."
                print(Fore.GREEN + f"\n{current_companion['name']} has been flatlined in the underworld..." + Style.RESET_ALL)
            print(Fore.GREEN + f"\n{current_companion['name']} - {result}" + Style.RESET_ALL)
            if stat_changes:
                print(Fore.GREEN + f"\nChanges: {stat_changes}" + Style.RESET_ALL)
            print(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)
            input()
        elif choice == "5":
            inventory()
        elif choice == "6":
            os.system("cls")
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + "OGENS NEON NEXUS - D5+D5" + Style.RESET_ALL)
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + "\nUNDERWORLD CONTACTS..." + Style.RESET_ALL)
            for name in companions:
                status = "(Flatlined)" if name in fallen_companions else ""
                print(Fore.GREEN + f"{name} {status} - Health: {companion_stats[name]['health']}, Strength: {companion_stats[name]['strength']}, Luck: {companion_stats[name]['luck']}" + Style.RESET_ALL)
            print(Fore.GREEN + "\nPress Enter to return..." + Style.RESET_ALL)
            stat_changes = "Viewed contact list"
            input()
        elif choice == "7":
            stat_changes = save_game()
            print(Fore.GREEN + "\nPress Enter to return..." + Style.RESET_ALL)
            input()
        elif choice == "8":
            stat_changes = load_game()
            print(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)
            input()
        elif choice == "9":
            os.system("cls")
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + "OGENS NEON NEXUS - D5+D5" + Style.RESET_ALL)
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + "\nHACKING OUT OF THE UNDERWORLD..." + Style.RESET_ALL)
            print(Fore.GREEN + f"\nFinal Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Health: {player['health']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Data Cores: {player['artifacts']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Quantum Mods: {player['quantum_mod']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Level: {player['level']}" + Style.RESET_ALL)
            now = datetime.now()
            print(Fore.GREEN + f"\nDate: {now.strftime('%m/%d/%Y')}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Time: {now.strftime('%H:%M')}" + Style.RESET_ALL)
            with open("GameLog.txt", "a") as f:
                f.write(f"{now.strftime('%m/%d/%Y %H:%M')} - Quit\n")
            print(Fore.GREEN + "\nPress Enter to end..." + Style.RESET_ALL)
            input()
            break
        if player["health"] <= 0:
            os.system("cls")
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + "OGENS NEON NEXUS - D5+D5" + Style.RESET_ALL)
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + "\n   //===\\\\" + Style.RESET_ALL)
            print(Fore.GREEN + "  // RIP \\\\" + Style.RESET_ALL)
            print(Fore.GREEN + " //_______\\\\" + Style.RESET_ALL)
            print(Fore.GREEN + " |  ***  |" + Style.RESET_ALL)
            print(Fore.GREEN + " |_______|" + Style.RESET_ALL)
            print(Fore.GREEN + "\nTHE UNDERWORLD FLATLINES YOU..." + Style.RESET_ALL)
            print(Fore.GREEN + f"\nFinal Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Health: {player['health']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Data Cores: {player['artifacts']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Quantum Mods: {player['quantum_mod']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Level: {player['level']}" + Style.RESET_ALL)
            now = datetime.now()
            print(Fore.GREEN + f"\nDate: {now.strftime('%m/%d/%Y')}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Time: {now.strftime('%H:%M')}" + Style.RESET_ALL)
            with open("GameLog.txt", "a") as f:
                f.write(f"{now.strftime('%m/%d/%Y %H:%M')} - Loss\n")
            print(Fore.GREEN + "\nPress Enter to end..." + Style.RESET_ALL)
            input()
            break
        if player["score"] >= 6000 and player["artifacts"] >= 300 and player["quantum_mod"] >= 50:
            os.system("cls")
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + "OGENS NEON NEXUS - D5+D5" + Style.RESET_ALL)
            print(Fore.GREEN + "--------------------------------------" + Style.RESET_ALL)
            print(Fore.GREEN + "\n   //***\\\\" + Style.RESET_ALL)
            print(Fore.GREEN + "  // *** \\\\" + Style.RESET_ALL)
            print(Fore.GREEN + " //_______\\\\" + Style.RESET_ALL)
            print(Fore.GREEN + " |  WIN  |" + Style.RESET_ALL)
            print(Fore.GREEN + " |_______|" + Style.RESET_ALL)
            print(Fore.GREEN + "\nYOU CONQUER THE UNDERWORLD..." + Style.RESET_ALL)
            print(Fore.GREEN + f"\nFinal Score: {player['score']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Health: {player['health']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Data Cores: {player['artifacts']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Quantum Mods: {player['quantum_mod']}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Final Level: {player['level']}" + Style.RESET_ALL)
            now = datetime.now()
            print(Fore.GREEN + f"\nDate: {now.strftime('%m/%d/%Y')}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Time: {now.strftime('%H:%M')}" + Style.RESET_ALL)
            with open("GameLog.txt", "a") as f:
                f.write(f"{now.strftime('%m/%d/%Y %H:%M')} - Win\n")
            print(Fore.GREEN + "\nPress Enter to end..." + Style.RESET_ALL)
            input()
            break

if __name__ == "__main__":
    main()