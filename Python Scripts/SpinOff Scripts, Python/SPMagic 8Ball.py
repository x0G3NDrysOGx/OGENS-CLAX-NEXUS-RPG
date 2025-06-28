import random
from colorama import init, Fore, Style

# Initialize colorama for colored output (autoreset for consistency)
init(autoreset=True)

# Define follow-up phrases (30 total)
followup = [
    "You better believe it, dude.",
    "Don't be a dumbass.",
    "Cartman approves.",
    "Even Kenny agrees.",
    "Blame Canada!",
    "Chef would say that's smooth.",
    "Stan's probably crying about it.",
    "Deal with it, mkay?",
    "Well, that escalated quickly.",
    "That's what she said.",
    "Respect my authoritah!",
    "I'm super cereal.",
    "You killed Kenny!",
    "No way, I'm not a Jew!",
    "I'm not your buddy, guy.",
    "ManBearPig's gonna get ya.",
    "That's the stupidest thing I've ever heard.",
    "You're gonna get a bad time.",
    "I'm out, peace!",
    "That's totally Satan's style.",
    "Oh my God, they did WHAT?!",
    "Screw you guys, I'm going home.",
    "I learned something today...",
    "Drugs are bad, mkay.",
    "I'm not fat, I'm big-boned.",
    "Dude, sweet!",
    "This is America, dude.",
    "No, kitty, this is my pot pie!",
    "Totally lame, dude!",
    "You're totally grounded, mister."
]

# Define South Park phrases (100 total)
phrases = [
    "Oh my God, they did WHAT?!",
    "Respect my authoritah!",
    "You bastards!",
    "Screw you guys, I'm going home.",
    "I learned something today...",
    "Drugs are bad, mkay.",
    "I'm super cereal.",
    "That's not how you park a car!",
    "It's a conspiracy!",
    "You killed Kenny!",
    "Oh, hamburgers.",
    "I'm not fat, I'm big-boned.",
    "Dude, sweet!",
    "This is America, dude.",
    "No, kitty, this is my pot pie!",
    "That's the stupidest thing I've ever heard.",
    "Oh, you're just jealous 'cause you're fat.",
    "I'm going down to South Park to get some cheese.",
    "You don't have to be a little bitch about it.",
    "Maybe you're just a little bit retarded.",
    "Timmy! Timmah!",
    "Kick the baby!",
    "Sweet, dude, score!",
    "I'm not your buddy, guy.",
    "He's not my friend, friend.",
    "Derp derp derp!",
    "Aw, weak!",
    "Member berries say no way.",
    "I'm scared, you guys.",
    "That's so gay, dude.",
    "M'kay, that's a bad idea.",
    "I broke the dam!",
    "Beefcake! BEEFCAKE!",
    "It's all about the chewbular.",
    "Butters, you're grounded!",
    "Stan, you're such a turd.",
    "Don't touch my sweet method!",
    "It's coming right for us!",
    "Whoa, major boobage.",
    "You're breaking my balls here.",
    "I'm so stoked, dude!",
    "Tch, whatever, hippie.",
    "You're a towel!",
    "No way, I'm not a Jew!",
    "Oh, Jesus Christ!",
    "This is totally ninja.",
    "Go ahead and suck it.",
    "ManBearPig's gonna get ya.",
    "I'm not a ginger, damn it!",
    "That's ignorant, dude.",
    "Casa Bonita, hell yeah!",
    "I'm getting too old for this.",
    "Aw, hamburgers!",
    "You're such a fatass.",
    "Don't be such a Clyde.",
    "It's a trap, you guys!",
    "I'm so confused right now.",
    "Just give me my Xbox!",
    "That's totally PC, bro.",
    "I need about tree fiddy.",
    "No, I'm serious, you guys.",
    "This is some bullcrap.",
    "Aw, you're so lame.",
    "I'm gonna make love to ya.",
    "That's a sticky situation.",
    "You've got no cred, dude.",
    "I'm not even joking.",
    "South Park's gone to hell.",
    "Don't mess with my junk!",
    "Nice try, Canada.",
    "You're gonna have a bad time.",
    "I'm not fat, I'm festive!",
    "That's super messed up.",
    "I'm a bad kitty!",
    "Oh, the tears of unfathomable sadness!",
    "You're totally grounded, mister.",
    "I'm not your pal, buddy.",
    "This is complete BS!",
    "Who farted? Oh, it's you.",
    "I'm gonna go watch porn.",
    "That's a negative, ghost rider.",
    "You're so freaking poor.",
    "I'm gonna kick your ass!",
    "It's like, whatever, dude.",
    "That's some redneck logic.",
    "I'm too sexy for this crap.",
    "You're a dirty little liar.",
    "This is my happy place.",
    "Don't harsh my mellow.",
    "I'm just a little crippled kid!",
    "That's so not cool, dude.",
    "I'm gonna barf!",
    "You're such a Butters.",
    "It's all PC principal's fault.",
    "I'm out, peace!",
    "That's totally Satan's style.",
    "You're screwing up my chi.",
    "I'm not buying your crap.",
    "This is why we can't have nice things.",
    "I'm not falling for that again."
]

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

def roll_dice_followup(sides):
    # Rejection sampling for follow-up roll (0-based)
    tries = 0
    max_range = 32766
    while tries < 20:
        temp = random.randint(0, max_range)
        tries += 1
        if temp < max_range // sides * sides:
            result = temp % sides  # 0-based for follow-up
            return result
    print(f"Warning: Unable to generate valid d{sides} roll after 20 attempts. Using default 0.")
    return 0

def main():
    while True:
        # Clear console (Windows-compatible)
        print("\033c", end="")

        print(f"{Fore.RED}============================={Style.RESET_ALL}")
        print(f"{Fore.RED}   SPMagic 8 Ball{Style.RESET_ALL}")
        print(f"{Fore.RED}============================={Style.RESET_ALL}")
        print()

        print(f"{Fore.RED}Ask your question (or type exit to quit):{Style.RESET_ALL}")
        question = input().strip()

        if question.lower() == "exit":
            break
        if not question:
            print(f"{Fore.RED}Please enter a question!{Style.RESET_ALL}")
            print()
            continue

        print()
        print(f"{Fore.RED}Shaking Magic 8 Ball...{Style.RESET_ALL}")
        import time
        time.sleep(2)

        # Roll for main phrase (1-100)
        d5 = roll_dice(5)
        d10 = roll_dice(10)
        flip = roll_dice(2) - 1  # 0 or 1
        rand = ((d5 - 1) * 10 + d10) + (flip * 50) - 1

        # Roll for follow-up (optional)
        follow_flip = roll_dice(2) - 1  # 0 or 1
        follow = None

        if follow_flip == 1:
            d6 = roll_dice_followup(6)
            d5_follow = roll_dice_followup(5)
            froll = d6 * 5 + d5_follow
            follow = followup[froll]

        print()
        print(f"{Fore.RED}Your question was:{Style.RESET_ALL}")
        print(question)
        print()
        print(f"{Fore.RED}Magic 8 Ball says:{Style.RESET_ALL}")
        print(f"{Fore.RED}-------------------{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{phrases[rand]}{Style.RESET_ALL}")
        if follow:
            print(f"{Fore.GREEN}{follow}{Style.RESET_ALL}")
        print()
        input(f"{Fore.RED}Press Enter to continue...{Style.RESET_ALL}")

    print()
    print(f"{Fore.RED}Thanks for playing the South Park Magic 8 Ball!{Style.RESET_ALL}")
    input(f"{Fore.RED}Press Enter to exit...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()