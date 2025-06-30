import random
from colorama import init, Fore, Style

# Initialize colorama for colored output (autoreset for consistency)
init(autoreset=True)

# Define rune descriptions (50 total)
rune = {
    1: "ᚠ Fehu – Wealth, beginnings, luck",
    2: "ᚢ Uruz – Strength, health, endurance",
    3: "ᚦ Thurisaz – Protection, conflict, reactive force",
    4: "ᚨ Ansuz – Wisdom, communication, signals",
    5: "ᚱ Raidho – Travel, movement, journey",
    6: "ᚲ Kenaz – Torch, illumination, revelation",
    7: "ᚷ Gebo – Gift, generosity, exchange",
    8: "ᚹ Wunjo – Joy, harmony, success",
    9: "ᚺ Hagalaz – Disruption, storms, tests",
    10: "ᚾ Nauthiz – Need, resistance, constraint",
    11: "ᛁ Isa – Ice, stillness, stagnation",
    12: "ᛃ Jera – Harvest, reward, cycle",
    13: "ᛇ Eiwaz – Defense, transition, death/rebirth",
    14: "ᛈ Perthro – Mystery, chance, secrets",
    15: "ᛉ Algiz – Protection, higher self, sanctuary",
    16: "ᛋ Sowilo – Sun, clarity, victory",
    17: "ᛏ Tiwaz – Honor, justice, leadership",
    18: "ᛒ Berkano – Growth, rebirth, fertility",
    19: "ᛖ Ehwaz – Horse, movement, trust",
    20: "ᛗ Mannaz – Humanity, self, social order",
    21: "ᛚ Laguz – Water, intuition, flow",
    22: "ᛜ Ingwaz – Potential, gestation, inner fire",
    23: "ᛞ Dagaz – Breakthrough, transformation, awakening",
    24: "ᛟ Othala – Ancestry, heritage, inheritance",
    25: "ᛠ Ear – Endings, mortality, descent",
    26: "ᚠ Fehu Rx – Greed, instability, bad fortune",
    27: "ᚢ Uruz Rx – Weakness, sickness, lack of will",
    28: "ᚦ Thurisaz Rx – Danger, impulsiveness, recklessness",
    29: "ᚨ Ansuz Rx – Lies, miscommunication, manipulation",
    30: "ᚱ Raidho Rx – Stuck, delay, lack of direction",
    31: "ᚲ Kenaz Rx – Darkness, confusion, loss of insight",
    32: "ᚷ Gebo Rx – Selfishness, imbalance, strings attached",
    33: "ᚹ Wunjo Rx – Sorrow, discord, broken relationships",
    34: "ᚺ Hagalaz Rx – Chaos, disaster, exposure",
    35: "ᚾ Nauthiz Rx – Suffering, bondage, powerlessness",
    36: "ᛁ Isa Rx – Isolation, emotional block, detachment",
    37: "ᛃ Jera Rx – Bad timing, missed opportunities",
    38: "ᛇ Eiwaz Rx – Stagnation, fear of change",
    39: "ᛈ Perthro Rx – Secrets revealed, bad luck",
    40: "ᛉ Algiz Rx – Vulnerability, deception, danger",
    41: "ᛋ Sowilo Rx – False hope, burnout",
    42: "ᛏ Tiwaz Rx – Injustice, arrogance, poor leadership",
    43: "ᛒ Berkano Rx – Loss, infertility, stagnation",
    44: "ᛖ Ehwaz Rx – Betrayal, mistrust, disconnection",
    45: "ᛗ Mannaz Rx – Alienation, self-deception",
    46: "ᛚ Laguz Rx – Drowning, emotional turmoil",
    47: "ᛜ Ingwaz Rx – Blocked energy, delay",
    48: "ᛞ Dagaz Rx – Resistance to change",
    49: "ᛟ Othala Rx – Stuck in past, family conflict",
    50: "ᛠ Ear Rx – Denial of death, fear of endings"
}

# Define mysterious effects (30 total)
effect = {
    1: "Whispers in the wind - a voice from the void speaks.",
    2: "The candle flickers unnaturally - fire spirits are near.",
    3: "A raven circles above - a message from Odin.",
    4: "You smell pine, though none is near - forest magic stirs.",
    5: "The runes glow faintly - they remember old wars.",
    6: "A drop of blood lands on the stone - fate is watching.",
    7: "Your hands tingle - ancestral power flows through you.",
    8: "Everything goes silent - a moment out of time.",
    9: "A shadow darts past - unseen watchers gather.",
    10: "The rune hums - it likes your question.",
    11: "A second rune appears - a twin message.",
    12: "The wind changes direction - heed reversal.",
    13: "You feel watched - something ancient stirs.",
    14: "A chill enters the room - Hel is near.",
    15: "A spark leaps from the rune - divine attention.",
    16: "Smoke forms a sigil - interpret it quickly.",
    17: "A spider drops on the runes - destiny spins.",
    18: "A sudden clarity vanishes too fast.",
    19: "Stone cracks - truth cannot be ignored.",
    20: "A wolf's howl echoes - Fenrir stirs.",
    21: "The sky darkens - prophecy intensifies.",
    22: "You see a flash of your past - time bleeds.",
    23: "A feather falls - Huginn or Muninn visits.",
    24: "The runes shuffle themselves - they choose.",
    25: "A tear wells in your eye - ancestors speak.",
    26: "Heat rises - Muspelheim touches your world.",
    27: "Cold breathes down your neck - Niflheim's gaze.",
    28: "A buzzing in your ear - Loki laughs.",
    29: "You sense someone behind you - but no one's there.",
    30: "Your reflection blinks - a fate double watches."
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
        print(f"{Fore.YELLOW}       RUNE ORACLE - 2D50{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}================================{Style.RESET_ALL}")
        print()

        print(f"{Fore.YELLOW}Shuffling fate and casting runes...{Style.RESET_ALL}")
        import time
        time.sleep(2)

        # Roll 2D5 for grid index (1-25)
        die1 = roll_dice(5)
        die2 = roll_dice(5)
        grid_index = (die1 - 1) * 5 + die2

        # Coin flip for rune side (0=Heads: 1-25, 1=Tails: 26-50)
        coin_rune = roll_dice(2) - 1  # 0 or 1
        rune_num = grid_index + (coin_rune * 25)

        print(f"{Fore.YELLOW}Die 1 (D5): {die1}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Die 2 (D5): {die2}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Grid Index (1-25): {grid_index}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Coin Flip (Rune Side) (0=Heads,1=Tails): {coin_rune}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}-------------------------------{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Rune Number: {rune_num}{Style.RESET_ALL}")
        print()

        # Get rune meaning
        rune_meaning = rune.get(rune_num, "Error: Rune not found")
        print(f"{Fore.YELLOW}Interpreting the runes...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}-------------------------------{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{rune_meaning}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}-------------------------------{Style.RESET_ALL}")

        # Fate's coin flip
        fate_flip = roll_dice(2) - 1
        fate_str = f"0=Heads - {Fore.BLUE}Good Omen{Style.RESET_ALL}" if fate_flip == 0 else f"1=Tails - {Fore.RED}Bad Omen{Style.RESET_ALL}"
        print()
        print(f"{Fore.YELLOW}Fate's Coin Flip (D2): {fate_str}{Style.RESET_ALL}")

        # Mysterious effect
        d5_effect = roll_dice(5)
        d6 = roll_dice(6)
        sum_effect = d5_effect + d6
        fx = sum_effect * 3 - 5
        if fx < 1:
            fx = 1
        if fx > 30:
            fx = 30

        print()
        print(f"{Fore.YELLOW}Mysterious-Effect Dice (D5,D6): {d5_effect}, {d6}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Effect number selected: {fx}{Style.RESET_ALL}")

        # Get mysterious effect
        effect_meaning = effect.get(fx, "Error: Effect not found")
        print()
        print(f"{Fore.YELLOW}Mysterious Effect:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{effect_meaning}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Style.RESET_ALL}")
        print()

        input(f"{Fore.YELLOW}Press Enter to cast again...{Style.RESET_ALL}")

    print()
    print(f"{Fore.YELLOW}Thanks for casting the runes!{Style.RESET_ALL}")
    input(f"{Fore.YELLOW}Press Enter to exit...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()