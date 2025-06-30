import random
from colorama import init, Fore, Style

# Initialize colorama for colored output (autoreset for consistency)
init(autoreset=True)

# Define demon descriptions (72 total)
demon = {
    1: "Bael - First king of Hell, grants invisibility.",
    2: "Agares - Master of languages, can cause earthquakes.",
    3: "Vassago - Reveals past and future.",
    4: "Samigina - Teaches liberal arts and speaks of souls.",
    5: "Marbas - Heals or causes illness, reveals secrets.",
    6: "Valefor - Grants cunning and thievery.",
    7: "Amon - Knows past/future, reconciles foes.",
    8: "Barbatos - Understands animal speech and treasures.",
    9: "Paimon - Powerful king, teaches sciences.",
    10: "Buer - Heals, teaches philosophy and herbs.",
    11: "Gusion - Tells all things past, present, and future.",
    12: "Sitri - Causes love and reveals secrets.",
    13: "Beleth - Commands love and lust.",
    14: "Leraje - Causes great battles and wounds.",
    15: "Eligos - Reveals hidden things and war.",
    16: "Zepar - Makes women fall in love.",
    17: "Botis - Reconciles enemies, tells past/future.",
    18: "Bathin - Knows virtues of herbs and gems.",
    19: "Sallos - Instills love between people.",
    20: "Purson - Reveals hidden things and treasures.",
    21: "Marax - Teaches astronomy and herbs.",
    22: "Ipos - Knows thoughts and future.",
    23: "Aim - Spreads fire and teaches cunning.",
    24: "Naberius - Restores lost dignity and eloquence.",
    25: "Glasya-Labolas - Speaks of murder and wars.",
    26: "Bune - Moves corpses and gives riches.",
    27: "Ronove - Teaches rhetoric and languages.",
    28: "Berith - Turns metals into gold, tells truths.",
    29: "Astaroth - Teaches sciences and secrets.",
    30: "Forneus - Teaches rhetoric and languages.",
    31: "Foras - Teaches logic and ethics, finds treasures.",
    32: "Asmoday - Teaches arithmetic and astronomy.",
    33: "Gaap - Transports people, teaches philosophy.",
    34: "Furfur - Causes love and storms.",
    35: "Marchosias - Strong fighter, gives truthful answers.",
    36: "Stolas - Teaches astronomy and knowledge of herbs.",
    37: "Phenex - Poetic demon, sings sweet notes.",
    38: "Halphas - Builds towers and commands legions.",
    39: "Malphas - Builds houses and reveals enemies.",
    40: "Raum - Destroys dignities, steals treasures.",
    41: "Focalor - Controls wind and sea, drowns men.",
    42: "Vepar - Controls waters, causes wounds to fester.",
    43: "Sabnock - Builds fortresses, inflicts wounds.",
    44: "Shax - Steals sight, hearing, and understanding.",
    45: "Vine - Discovers hidden things, creates storms.",
    46: "Bifrons - Teaches science, geometry, and astrology.",
    47: "Uvall - Teaches love and reveals secrets.",
    48: "Haagenti - Turns metals into gold, makes wine.",
    49: "Crocell - Teaches geometry, conjures water.",
    50: "Furcas - Teaches philosophy and astrology.",
    51: "Balam - Knows past/future, gives invisibility.",
    52: "Alloces - Teaches astronomy and commands cavalry.",
    53: "Camio - Answers in burning ashes or voices.",
    54: "Murmur - Teaches philosophy and necromancy.",
    55: "Orobas - Gives true answers of past/future.",
    56: "Gremory - Tells of treasures and love.",
    57: "Ose - Makes men insane and teaches liberal sciences.",
    58: "Amy - Teaches astrology and reveals treasures.",
    59: "Orias - Changes appearance and grants dignities.",
    60: "Vapula - Teaches mechanics and philosophy.",
    61: "Zagan - Turns water into wine and blood into oil.",
    62: "Valac - Reveals treasures, appears as a child with dragon.",
    63: "Andras - Sows discord and causes chaos.",
    64: "Haures - Teaches philosophy and destroys enemies.",
    65: "Andrealphus - Teaches astronomy and geometry.",
    66: "Cimejes - Teaches grammar and logic.",
    67: "Amdusias - Commands music and causes trees to bend.",
    68: "Belial - Grants favors and dignities.",
    69: "Decarabia - Knows virtues of birds and stones.",
    70: "Seere - Brings things to pass quickly.",
    71: "Dantalion - Knows thoughts and influences minds.",
    72: "Andromalius - Returns stolen goods, reveals thieves."
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

        print(f"{Fore.RED}===================================={Style.RESET_ALL}")
        print(f"{Fore.RED}           DEMON DICE - D72{Style.RESET_ALL}")
        print(f"{Fore.RED}===================================={Style.RESET_ALL}")
        print()

        print(f"{Fore.RED}Rolling the Demon Dice...{Style.RESET_ALL}")
        import time
        time.sleep(2)

        # Roll two D6 for base number (1-36)
        d1 = roll_dice(6)
        d2 = roll_dice(6)
        base = (d1 - 1) * 6 + d2

        # Coin flip for upper or lower half (0 or 1)
        half = roll_dice(2) - 1  # 0 or 1
        result = base + (half * 36)

        # Show rolls
        print(f"{Fore.RED}First Roll (D6): {d1}{Style.RESET_ALL}")
        print(f"{Fore.RED}Second Roll (D6): {d2}{Style.RESET_ALL}")
        print(f"{Fore.RED}Demon Number: {result}{Style.RESET_ALL}")
        print(f"{Fore.RED}------------------------------------{Style.RESET_ALL}")

        # Get demon description
        demon_desc = demon.get(result, "Error: Demon not found")
        print()
        print(f"{Fore.RED}Your demon is:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{demon_desc}{Style.RESET_ALL}")
        print()

        input(f"{Fore.RED}Press any key to roll again, or Ctrl+C to exit...{Style.RESET_ALL}")
        # No explicit exit condition; Ctrl+C to terminate

if __name__ == "__main__":
    main()