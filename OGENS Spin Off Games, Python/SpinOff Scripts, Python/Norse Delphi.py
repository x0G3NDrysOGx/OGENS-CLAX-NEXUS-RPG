import random
from colorama import init, Fore, Style

# Initialize colorama for colored output (green text, autoreset for consistency)
init(autoreset=True)

# Define gods/goddesses/giants (1-80)
gods = {
    1: "Odin - Allfather, wisdom-seeker, wanderer",
    2: "Frigg - Queen of Asgard, seer of fates",
    3: "Thor - Thunderer, protector of Midgard",
    4: "Loki - Trickster, shapeshifter, chaos-bearer",
    5: "Freya - Vanir goddess of love, war, and seidr",
    6: "Freyr - Lord of peace and prosperity",
    7: "Heimdall - Guardian of Bifrost, all-seeing",
    8: "Tyr - One-handed god of law and sacrifice",
    9: "Baldr - God of light, purity, and beauty",
    10: "Njord - God of sea, wind, and wealth",
    11: "Skadi - Goddess of winter, hunting, and bow",
    12: "Bragi - God of poetry and eloquence",
    13: "Idunn - Keeper of apples, youth-giver",
    14: "Hel - Mistress of the underworld",
    15: "Vidar - Silent god, avenger of Odin",
    16: "Vali - God of vengeance and renewal",
    17: "Forseti - God of justice and reconciliation",
    18: "Hodr - Blind god, accidental slayer",
    19: "Ullr - God of archery and skiing",
    20: "Eir - Goddess of healing and mercy",
    21: "Jormungandr - Midgard serpent, world encircler",
    22: "Fenrir - Giant wolf, destined to break chains",
    23: "Surtr - Fire giant, destroyer at Ragnarok",
    24: "Ymir - Primordial giant, ancestor of giants",
    25: "Angrboda - Giantess, mother of monsters",
    26: "Skoll - Wolf chasing the sun",
    27: "Hati - Wolf chasing the moon",
    28: "Nidhogg - Dragon gnawing roots of Yggdrasil",
    29: "Ran - Sea goddess who captures drowned sailors",
    30: "Aegir - God of ocean storms",
    31: "Modi - Son of Thor, god of courage",
    32: "Magni - Son of Thor, god of strength",
    33: "Bestla - Giantess, grandmother of Odin",
    34: "Baldur's Horse - Symbolic companion",
    35: "Hrimthursar - Frost giants, ancient foes",
    36: "Surtur - Fire giant king of Muspelheim",
    37: "Alfheim Elves - Light elves of the heavens",
    38: "Svartalfar - Dark elves, skilled smiths",
    39: "Dwarves - Masters of craft and runes",
    40: "Jotnar - Giants, forces of chaos and nature",
    41: "Gefjon - Goddess of fertility and ploughing",
    42: "Hlin - Protector of those fated to die",
    43: "Kvasir - God of inspiration and wisdom",
    44: "Meili - Thor's lesser-known brother",
    45: "Mimir - Guardian of wisdom and memory",
    46: "Nanna - Wife of Baldr, goddess of joy",
    47: "Sigyn - Loyal wife of Loki",
    48: "Snotra - Goddess of wisdom and prudence",
    49: "Syn - Guardian of doors and defensive oath",
    50: "Thor's goats - Tanngrisnir and Tanngnjostr",
    51: "Vili - Brother of Odin, god of will",
    52: "Ve - Brother of Odin, god of the world",
    53: "Yggdrasil - World tree, axis of cosmos",
    54: "Alvis - A dwarf with vast knowledge",
    55: "Buri - First god, ancestor of Aesir",
    56: "Dellingr - God of dawn",
    57: "Eitri - Dwarf smith, creator of Mjolnir",
    58: "Fensalir - Home of goddess Frigg",
    59: "Gullveig - Mysterious sorceress, linked to Vanir",
    60: "Hoemir - God of silence and thought",
    61: "Brynhildr - Valkyrie, shieldmaiden and chooser of slain",
    62: "Hildr - Valkyrie, fierce battle maiden",
    63: "Gunnr - Valkyrie, war goddess",
    64: "Rota - Valkyrie, known for fate-deciding",
    65: "Sigrun - Valkyrie, victorious rune-bearer",
    66: "Skogul - Valkyrie, warrior spirit",
    67: "Thrud - Valkyrie, daughter of Thor",
    68: "Ullr - God of archery, hunting, skiing",
    69: "Valkyries - Choosers of the slain",
    70: "Vedrfolnir - Eagle perched atop Yggdrasil",
    71: "Vindalf - God of the wind",
    72: "Var - Goddess of promises and agreements",
    73: "Vili - God of will and desire",
    74: "Volsung - Legendary hero ancestor",
    75: "Ymir - Primordial frost giant",
    76: "Aegir - God of the sea and brewing",
    77: "Ondur - Spirit or soul",
    78: "Jord - Earth goddess and mother of Thor",
    79: "Helblindi - Brother of Loki",
    80: "Nari/Narfi - Son of Loki, bound in punishment"
}

# Define elves/dwarves/spirits (1-30)
eds = {
    1: "Alf (Elf) - Light and swift spirit",
    2: "Dvalin (Dwarf) - Master smith and craftsman",
    3: "Tomte (Spirit) - Household guardian",
    4: "Svartalf (Dark Elf) - Skilled in magic",
    5: "Glasir (Elf) - Gleaming guardian",
    6: "Fjalar (Dwarf) - Cunning and clever",
    7: "Huldra (Spirit) - Forest enchantress",
    8: "Nisse (Spirit) - Protective household sprite",
    9: "Elr (Elf) - Wise forest dweller",
    10: "Dain (Dwarf) - Steadfast and loyal",
    11: "Skadi (Giantess) - Winter huntress",
    12: "Ljosalfar (Light Elf) - Radiant beings",
    13: "Bergrisar (Mountain Giants) - Powerful and strong",
    14: "Vaettir (Spirits) - Nature guardians",
    15: "Ask (Elf) - First man in myth",
    16: "Embla (Elf) - First woman in myth",
    17: "Hamingja (Spirit) - Fortune and luck",
    18: "Skogtroll (Spirit) - Forest troll",
    19: "Dvergr (Dwarf) - Earth dwellers",
    20: "Myling (Spirit) - Ghost child",
    21: "Fossegrim (Spirit) - Water spirit musician",
    22: "Jotunn (Giant) - Ancient force of chaos",
    23: "Huldrefolk (Spirit) - Hidden folk",
    24: "Skjaldmeyjar (Valkyrie) - Shieldmaidens",
    25: "Draugr (Spirit) - Undead warrior",
    26: "Valkyrie (Spirit) - Choosers of slain",
    27: "Alviss (Dwarf) - All-wise smith",
    28: "Ranva (Spirit) - Misty guardian of lakes",
    29: "Eikinskjaldi (Giant) - Mountain dweller with icy breath",
    30: "Fylgja (Spirit) - Ancestral guardian spirit"
}

# Define Norns/fates (1-3)
norns = {
    1: "Urd - Past, fate that has already happened",
    2: "Verdandi - Present, ongoing fate",
    3: "Skuld - Future, fate yet to come"
}

def roll_dice(sides):
    # Rejection sampling for fair roll
    tries = 0
    max_range = 32766  # Approx half of 65535 (max random value)
    while tries < 20:
        temp = random.randint(0, max_range)
        tries += 1
        if temp < max_range // sides * sides:  # Ensure fair distribution
            result = temp % sides + 1
            return result
    print(f"Warning: Unable to generate valid d{sides} roll after 20 attempts. Using default 1.")
    return 1

def main():
    while True:
        # Clear console (Windows-compatible)
        print("\033c", end="")

        print(f"{Fore.YELLOW}================================{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}       NORSE DELPHI - D80 D30{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}================================{Style.RESET_ALL}")
        print()

        print(f"{Fore.YELLOW}Consulting the ancient powers...{Style.RESET_ALL}")
        import time
        time.sleep(2)  # Simulate delay

        # Roll for Major God/Goddess or Giant (1-80)
        d8 = roll_dice(8)
        d5 = roll_dice(5)
        coin = roll_dice(2) - 1  # 0 or 1
        god_num = (d8 - 1) * 5 + d5
        if coin == 1:
            god_num += 40

        print(f"{Fore.YELLOW}Rolling for Major God/Goddess or Giant...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Die 1 (D8): {d8}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Die 2 (D5): {d5}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Coin flip: {coin} = {'Heads' if coin == 0 else 'Tails'}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Result number (1-80): {god_num}{Style.RESET_ALL}")
        god = gods.get(god_num, "Unknown Entity")
        print(f"{Fore.GREEN}-------------------------------{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{god}{Style.RESET_ALL}")
        print()

        # Roll for Elves, Dwarves, or Spirits (1-30)
        ed_die1 = roll_dice(5)
        ed_die2 = roll_dice(3)
        coin = roll_dice(2) - 1  # 0 or 1
        eds_value = (ed_die1 - 1) * 3 + ed_die2  # Renamed to avoid conflict
        if coin == 1:
            eds_value += 15

        print(f"{Fore.YELLOW}Rolling for Elves, Dwarves, or Spirits:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Die 1 (D5): {ed_die1}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Die 2 (D3): {ed_die2}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Coin flip: {coin} = {'Heads' if coin == 0 else 'Tails'}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Result number (1-30): {eds_value}{Style.RESET_ALL}")
        eds_name = eds.get(eds_value, "Unknown Spirit")  # Fixed: Use eds dictionary with eds_value as key
        print(f"{Fore.GREEN}-------------------------------{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{eds_name}{Style.RESET_ALL}")
        print()

        # Roll for Norn or Fate (1-3)
        norns_die = roll_dice(3)
        norn = norns.get(norns_die, "Unknown Norn")

        print(f"{Fore.YELLOW}Rolling for Norn or Fate...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Result number (1-3): {norns_die}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}-------------------------------{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{norn}{Style.RESET_ALL}")
        print()

        input(f"{Fore.YELLOW}Press Enter to consult again...{Style.RESET_ALL}")
        # No need for goto, loop handled by while True

if __name__ == "__main__":
    main()