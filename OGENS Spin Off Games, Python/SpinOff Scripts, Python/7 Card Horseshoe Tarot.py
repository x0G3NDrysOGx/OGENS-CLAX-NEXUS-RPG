import random
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()

# Define tarot cards (78 total: Major + Minor Arcana)
cards = {
    0: ("The Fool", "New beginnings, innocence, adventure", "Recklessness, fear of change"),
    1: ("The Magician", "Manifestation, resourcefulness", "Manipulation, poor planning"),
    2: ("The High Priestess", "Intuition, mystery", "Secrets, repressed feelings"),
    3: ("The Empress", "Abundance, nurturing", "Dependence, creative block"),
    4: ("The Emperor", "Authority, structure", "Control, rigidity"),
    5: ("The Hierophant", "Tradition, spirituality", "Rebellion, nonconformity"),
    6: ("The Lovers", "Love, harmony", "Disharmony, imbalance"),
    7: ("The Chariot", "Willpower, determination", "Lack of control, aggression"),
    8: ("Strength", "Courage, inner strength", "Self-doubt, weakness"),
    9: ("The Hermit", "Soul-searching, introspection", "Isolation, loneliness"),
    10: ("Wheel of Fortune", "Good luck, cycles", "Bad luck, resistance to change"),
    11: ("Justice", "Fairness, truth", "Dishonesty, unfairness"),
    12: ("The Hanged Man", "Surrender, new perspective", "Stagnation, delay"),
    13: ("Death", "Transformation, endings", "Resistance to change, fear of loss"),
    14: ("Temperance", "Balance, moderation", "Imbalance, excess"),
    15: ("The Devil", "Addiction, materialism", "Freedom, detachment"),
    16: ("The Tower", "Sudden change, upheaval", "Fear of change, avoidance"),
    17: ("The Star", "Hope, inspiration", "Lack of faith, despair"),
    18: ("The Moon", "Illusion, intuition", "Confusion, fear"),
    19: ("The Sun", "Joy, success", "Temporary setbacks, lack of clarity"),
    20: ("Judgement", "Awakening, renewal", "Self-doubt, refusal to change"),
    21: ("The World", "Completion, fulfillment", "Incompletion, lack of closure"),
    22: ("Ace of Wands", "Inspiration, new opportunities", "Lack of direction, delays"),
    23: ("Two of Wands", "Planning, decisions", "Fear of change, indecision"),
    24: ("Three of Wands", "Expansion, foresight", "Obstacles, delays"),
    25: ("Four of Wands", "Celebration, harmony", "Tension, lack of support"),
    26: ("Five of Wands", "Conflict, competition", "Avoiding conflict, resolution"),
    27: ("Six of Wands", "Victory, recognition", "Ego, lack of recognition"),
    28: ("Seven of Wands", "Defense, perseverance", "Giving up, overwhelm"),
    29: ("Eight of Wands", "Speed, progress", "Delays, frustration"),
    30: ("Nine of Wands", "Resilience, persistence", "Exhaustion, doubt"),
    31: ("Ten of Wands", "Burden, responsibility", "Overwhelm, delegation"),
    32: ("Page of Wands", "Enthusiasm, exploration", "Lack of direction, impulsiveness"),
    33: ("Knight of Wands", "Adventure, passion", "Recklessness, haste"),
    34: ("Queen of Wands", "Confidence, warmth", "Jealousy, insecurity"),
    35: ("King of Wands", "Leadership, vision", "Domineering, impulsiveness"),
    36: ("Ace of Cups", "Love, new emotions", "Blocked emotions, emptiness"),
    37: ("Two of Cups", "Partnership, unity", "Disharmony, separation"),
    38: ("Three of Cups", "Friendship, celebration", "Overindulgence, isolation"),
    39: ("Four of Cups", "Apathy, contemplation", "New opportunities, awareness"),
    40: ("Five of Cups", "Loss, regret", "Acceptance, moving on"),
    41: ("Six of Cups", "Nostalgia, reunion", "Stuck in past, naivety"),
    42: ("Seven of Cups", "Choices, fantasy", "Clarity, decision-making"),
    43: ("Eight of Cups", "Walking away, transition", "Fear of change, stagnation"),
    44: ("Nine of Cups", "Contentment, wishes fulfilled", "Dissatisfaction, greed"),
    45: ("Ten of Cups", "Happiness, family", "Conflict, disconnection"),
    46: ("Page of Cups", "Creativity, intuition", "Emotional immaturity, insecurity"),
    47: ("Knight of Cups", "Romance, charm", "Moodiness, unrealistic"),
    48: ("Queen of Cups", "Compassion, intuition", "Emotional insecurity, co-dependency"),
    49: ("King of Cups", "Emotional balance, wisdom", "Manipulation, moodiness"),
    50: ("Ace of Swords", "Clarity, breakthrough", "Confusion, miscommunication"),
    51: ("Two of Swords", "Indecision, stalemate", "Clarity, difficult choices"),
    52: ("Three of Swords", "Heartbreak, sorrow", "Healing, forgiveness"),
    53: ("Four of Swords", "Rest, contemplation", "Burnout, restlessness"),
    54: ("Five of Swords", "Conflict, betrayal", "Reconciliation, regret"),
    55: ("Six of Swords", "Transition, moving on", "Resistance to change, stagnation"),
    56: ("Seven of Swords", "Deception, strategy", "Coming clean, guilt"),
    57: ("Eight of Swords", "Restriction, powerlessness", "Freedom, self-empowerment"),
    58: ("Nine of Swords", "Anxiety, despair", "Hope, recovery"),
    59: ("Ten of Swords", "Betrayal, rock bottom", "Recovery, new beginnings"),
    60: ("Page of Swords", "Curiosity, new ideas", "Gossip, impulsiveness"),
    61: ("Knight of Swords", "Ambition, action", "Recklessness, aggression"),
    62: ("Queen of Swords", "Clarity, independence", "Coldness, cruelty"),
    63: ("King of Swords", "Authority, logic", "Manipulation, tyranny"),
    64: ("Ace of Pentacles", "Prosperity, new opportunities", "Missed opportunities, greed"),
    65: ("Two of Pentacles", "Balance, adaptability", "Disorganization, overwhelm"),
    66: ("Three of Pentacles", "Teamwork, skill", "Lack of collaboration, mediocrity"),
    67: ("Four of Pentacles", "Security, control", "Greed, insecurity"),
    68: ("Five of Pentacles", "Poverty, insecurity", "Recovery, charity"),
    69: ("Six of Pentacles", "Generosity, sharing", "Selfishness, debt"),
    70: ("Seven of Pentacles", "Patience, investment", "Lack of progress, impatience"),
    71: ("Eight of Pentacles", "Skill, hard work", "Laziness, lack of focus"),
    72: ("Nine of Pentacles", "Abundance, independence", "Financial dependence, overindulgence"),
    73: ("Ten of Pentacles", "Legacy, wealth", "Financial loss, family disputes"),
    74: ("Page of Pentacles", "Ambition, learning", "Lack of focus, procrastination"),
    75: ("Knight of Pentacles", "Hard work, responsibility", "Laziness, stagnation"),
    76: ("Queen of Pentacles", "Nurturing, practicality", "Financial insecurity, neglect"),
    77: ("King of Pentacles", "Wealth, stability", "Greed, stubbornness")
}

def roll_dice():
    # Simulate fair d6 and d13 rolls
    d6 = random.randint(1, 6)
    d13 = random.randint(1, 13)
    # Calculate card index
    card_idx = (d6 - 1) * 13 + (d13 - 1)
    # Simulate coin flip (0 for upright, 1 for reversed)
    flip = random.randint(0, 1)
    return card_idx, flip

def show_card(position, card_idx, flip):
    label = {
        1: "Past",
        2: "Present",
        3: "Near Future",
        4: "Core Issue",
        5: "External Influences",
        6: "Hopes/Fears",
        7: "Outcome"
    }[position]
    
    name, upright, reversed = cards[card_idx]
    orientation = "Upright" if flip == 0 else "Reversed"
    meaning = upright if flip == 0 else reversed
    
    print(f"{Fore.GREEN}{label}:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{name} ({orientation}): {meaning}{Style.RESET_ALL}")
    print()

def main():
    while True:
        # Clear console (works on Windows, use os-specific clear for cross-platform)
        print("\033c", end="")  # Clear console (Windows-compatible)
        
        print(f"{Fore.YELLOW}====================================={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}   7-Card Horseshoe Tarot Spread{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}====================================={Style.RESET_ALL}")
        print()
        
        question = input(f"{Fore.YELLOW}Please enter your question (or type 'exit' to quit):\n{Style.RESET_ALL}")
        if not question:
            question = "Unspecified question"
        if question.lower() == "exit":
            break
        
        print()
        print(f"{Fore.YELLOW}You asked: {question}{Style.RESET_ALL}")
        print()
        print(f"{Fore.YELLOW}Shuffling the cards...{Style.RESET_ALL}")
        import time
        time.sleep(2)  # Simulate shuffling delay
        
        # Pick 7 unique cards
        picked_cards = []
        for _ in range(7):
            tries = 0
            while tries < 20:
                card_idx, flip = roll_dice()
                if card_idx not in picked_cards:
                    picked_cards.append((card_idx, flip))
                    break
                tries += 1
            else:
                print(f"Error picking card {_ + 1}. Exiting.")
                return
        
        print(f"{Fore.YELLOW}Your Seven-Card Horseshoe Reading:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}---------------------------------{Style.RESET_ALL}")
        for i, (card_idx, flip) in enumerate(picked_cards, 1):
            show_card(i, card_idx, flip)
        print(f"{Fore.YELLOW}---------------------------------{Style.RESET_ALL}")
        
        print(f"{Fore.YELLOW}Reflect on these messages as they relate to your question.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}The cards have spoken, but your path is yours to walk.{Style.RESET_ALL}")
        print()
        
        cont = input(f"{Fore.YELLOW}Would you like another reading? (y/n): {Style.RESET_ALL}")
        if cont.lower() != "y":
            break
    
    print()
    print(f"{Fore.YELLOW}Thank you for consulting the Tarot. May your path be clear.{Style.RESET_ALL}")
    input(f"{Fore.YELLOW}Press Enter to exit...{Style.RESET_ALL}")  # Mimics pause

if __name__ == "__main__":
    main()