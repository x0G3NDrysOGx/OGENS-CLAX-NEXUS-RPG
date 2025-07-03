# How to Play OGENS FANTASY NEXUS RPG

Welcome to **OGENS FANTASY NEXUS RPG**, a captivating text-based adventure game crafted by Developer Cody L Morgan. Embark on an epic journey through four mystical realms—Ancient Crypts, Enchanted Forest, Mystic Ruins, and Shadow Realm—to conquer the Mystic Realm. Your mission is to achieve a score of 6000, collect 300 runes, and gather 50 arcane crystals. This guide will help you navigate the game and master its mechanics.

---

## **Getting Started**
1. **Launch the Game**:
   - Ensure you have Python 3.x installed along with the required libraries: `secrets`, `json`, `os`, and `colorama`.
   - Run the script `main.py` in your terminal or command prompt:
     ```
     python main.py
     ```
   - The game begins with a fantasy-themed ASCII art and a randomly assigned companion joining your quest.

2. **Understand Your Stats**:
   - **Health**: Starts at 100 (max 200, increases with levels).
   - **Score**: Tracks your progress (target: 6000).
   - **Runes**: Collectible items (target: 300).
   - **Arcane Crystals**: Special items (target: 50).
   - **Player Strength**: Randomly set between 5 and 15, affecting combat outcomes.
   - **Level and XP**: Begin at level 1 with 0 XP (level up at 50 XP per level, capped at 1000).
   - **Items**: Healing Potions, Magic Scrolls, Mystic Keys, and Arcane Crystals.

3. **Choose a Companion**:
   - A random companion (e.g., DrysOG, Baked) joins you at the start, with stats like health (50-100), strength (5-15), luck (1-10), and a class (e.g., Barbarian, Enchanter).
   - Companions can fall in battle but may revive with positive outcomes.

---

## **Gameplay Basics**
1. **Navigation Menu**:
   - After the intro, you’ll see the main menu displaying your stats and options:
     - **1**: Ancient Crypts
     - **2**: Enchanted Forest
     - **3**: Mystic Ruins
     - **4**: Shadow Realm
     - **5**: Inventory
     - **6**: Companions List
     - **7**: Save Game
     - **8**: Load Game
     - **9**: Exit
   - Type the number of your choice and press Enter.

2. **Rolling the Dice**:
   - Each path involves a dice roll using a D5 (1-5) and D10 (1-10), combined and adjusted by your companion’s luck (1-10), resulting in an outcome between 1 and 50.
   - The outcome determines the event you encounter (e.g., treasure, combat).

3. **Exploring Paths**:
   - Select a path to face randomized events. Outcomes can yield rewards (e.g., runes, potions) or challenges (e.g., health loss).
   - Your player strength and companion class modifiers influence the severity of health changes.

4. **Using Items**:
   - Access the inventory (option 5) to use items:
     - **1**: Healing Potion (+25 health for player, +20 for companion, class-boosted).
     - **2**: Magic Scroll (+20 score, class-boosted).
     - **3**: Mystic Key (+4 runes, class-boosted).
     - **4**: Arcane Crystal (doubles next score gain or +5 score if no gain).
     - **5**: Return to menu.

5. **Managing Companions**:
   - View the companions list (option 6) to see their stats and status (active or fallen).
   - A new companion is randomly selected for each path event.

6. **Saving and Loading**:
   - **Save** (option 7): Saves progress to `SaveGame.txt` with a backup (`SaveGame.bak`).
   - **Load** (option 8): Restores progress from `SaveGame.txt` if available.
   - Game events (win, loss, quit) are logged to `GameLog.txt`.

7. **Win and Loss Conditions**:
   - **Win**: Achieve 6000 score, 300 runes, and 50 arcane crystals.
   - **Loss**: Your health drops to 0 or below.

---

## **Tips for Success**
- **Leverage Companions**: Choose paths where your companion’s class provides a boost (e.g., Alchemist for potion effects).
- **Manage Health**: Use Healing Potions strategically to avoid defeat.
- **Collect Wisely**: Prioritize Arcane Crystals for score multipliers and runes for progress.
- **Save Often**: Regularly save your game to avoid losing progress.

---

## **Developer Notes**
This game was created by Cody L Morgan as a passion project to blend fantasy storytelling with procedural gameplay. Enjoy the adventure, and feel free to provide feedback or suggestions!

---

Enjoy conquering the **OGENS FANTASY NEXUS RPG**!