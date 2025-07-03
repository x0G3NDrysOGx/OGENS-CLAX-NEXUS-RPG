# OGENS FANTASY NEXUS RPG - D5+D10

**A Terminal-Based Adventure of Chance & Lore**

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## Overview

**Game Type**: Text-based RPG | Windows Command Line | RNG D5+D10  
**Author**: Developed by Cody L Morgan  
**Version**: 9.0  

Welcome to **OGENS FANTASY NEXUS RPG - D5+D10**, a captivating command-line RPG set in a mystic realm of ancient magic and perilous quests. Navigate treacherous paths, collect sacred runes and arcane crystals, and conquer the Nexus by surviving traps, recruiting companions, and leveling up. Each playthrough is unique, driven by randomized characters and branching events determined by dice rolls. In D5+D10, a five-sided die (1–5) and a ten-sided die (0–9) are rolled, mapping to outcomes 1–50 for each path. A companion’s luck adjusts the outcome, creating dynamic challenges and rewards.

---

## Starting Stats

- HEALTH:        100 (Max: 200)
- SCORE:         0
- LEVEL:         1
- XP to Level 2: 50
- RUNES:         0
- ARCANE CRYSTALS: 0
- ITEMS:         None initially
- COMPANIONS:    One selected randomly from a roster of 27
- PLAYER STRENGTH: 5–15, 5 is Nightmare mode


Each companion has:
- **HEALTH**: 50–100
- **STRENGTH**: 5–15
- **LUCK**: 1–10
- **CLASS**: Randomly assigned (e.g., Barbarian, Cleric, Mage, Sorcerer, Archer, Thief, Paladin, Warrior, Necromancer)

---

## Path Choices

On each turn, choose from nine options:
- **Ancient Crypts**: Gain Score, Runes, XP, Player Health, Companion Health
- **Enchanted Forest**: Gain Score, Runes, Magic Scroll, Arcane Crystals, XP, Player Health, Companion Health
- **Mystic Ruins**: Gain Score, Runes, Healing Potion, Mystic Key, XP, Player Health, Companion Health
- **Shadow Realm**: Gain Score, Runes, Healing Potion, Mystic Key, Arcane Crystals, XP, Player Health, Companion Health
- **Items**: Use Healing Potion (+25 player health, +20 companion health), Magic Scroll (+20 score), Mystic Key (+4 runes), Arcane Crystal (double score or +5 score for next event)
- **Character List**: View companion stats (Health, Strength, Luck, Class)
- **Save Game**: Save progress to a file
- **Load Game**: Load previously saved progress
- **Quit**: Exit with final stats displayed

---

## Dice & Modifiers

Events are based on a D5+D10 roll mapped to 1–50 outcomes with a Luck Modifier:
- D5: 1–5, D10: 0–9
- Outcome = (D5-1)*10 + D10
- LuckMod = Companion Luck - 5
- AdjustedRoll = Outcome + LuckMod (clamped to 1–50)




Outcomes depend on the Adjusted Roll:
- **Low rolls (e.g., 2, 7, 10, 12, 15)**: Damage (-5 to -7 player health, -5 to -7 companion health, adjusted by strength), minimal XP (1)
- **Mid rolls (e.g., 11, 13, 19, 22, 23)**: Items (Potions in Paths 3 and 4, Scrolls in Path 2, Crystals in Paths 2 and 4, Keys in Paths 3 and 4), moderate XP (6–8)
- **High rolls (e.g., 1, 6, 16, 21, 24)**: Runes, score boosts (4–8+level), health gains (+4 player, +4 companion), high XP (8–10), Crystals (Paths 2 and 4), Keys (Paths 3 and 4)

---

## Companion System

The following companions can join you in the mystic realm:
- DrysOG
- Baked
- Akihimura
- Brandon
- SS
- CatzBrownout
- Spvcestep
- LeafChicken
- Slink
- Toady
- Crabman
- DarkSkitZo
- toqer
- KenshinGM
- CEnnis91
- XoraLoyal
- alfalfa1
- Paramount
- JohnnyTest
- cuddly
- Jgunishka
- Moosehead
- Shinfuji
- Agent21iXi
- Firo
- Suprafast
- BadassBampy

Companions influence:
- **Luck**: Adjusts dice rolls via LuckMod
- **Strength**: Reduces companion damage taken
- **Health**: Determines companion survival
- **Class**: Provides unique bonuses:
  - **Barbarian**: +5 damage boost, +2 damage reduction
  - **Cleric**: +10 healing boost
  - **Mage**: +5 magic boost
  - **Sorcerer**: +5 magic boost, -2 damage taken
  - **Archer**: +5 ranged boost
  - **Thief**: +2 luck, +5 score
  - **Paladin**: +5 defense, +5 healing
  - **Warrior**: +5 damage, +2 defense
  - **Necromancer**: +5 necrotic boost, -2 damage taken

If a companion’s health reaches 0, they fall but can be revived by positive outcomes (e.g., gaining items or health).

---

## Leveling & XP

**XP** is earned each turn:
- Successful events (e.g., runes, crystals, potions, keys, health gains): 6–10 XP
- Failed events (e.g., damage taken): 1 XP

**Leveling up**:
- Increases max health (+10), health (+5), and score gains (via level-based bonuses)
- XP requirement: Level * 50 (e.g., 50 for Level 2, 100 for Level 3)

---

## Items

Items are found through events:
- **Healing Potions**: Restores +25 player health (max 200 + level*10), +20 companion health (max 100). Found in **Ancient Crypts** (e.g., adjusted roll 4: "You evade undead patrols, finding a Healing Potion in a dusty alcove"), **Mystic Ruins** (e.g., adjusted roll 19: "You harness ruin magic, gaining a Healing Potion"), **Shadow Realm** (e.g., adjusted roll 27: "You calm a shadow spirit, gaining a Healing Potion").
- **Magic Scrolls**: Grants +20 score when used. Found in **Enchanted Forest** (e.g., adjusted roll 13: "You trade with elven scouts, gaining a Magic Scroll"), **Shadow Realm** (e.g., adjusted roll 23: "You earn a shadow’s blessing, gaining a Magic Scroll").
- **Mystic Keys**: Grants +4 runes when used. Found in **Mystic Ruins** (e.g., adjusted roll 11: "You persuade a ruin sage, earning a Mystic Key"), **Shadow Realm** (e.g., adjusted roll 22: "You defeat a shadow beast, claiming a Mystic Key").
- **Arcane Crystals**: Doubles score for the next event; grants +5 score if no score gain. Found in **Enchanted Forest** (e.g., adjusted roll 6: "You slay a forest troll, seizing an Arcane Crystal"), **Shadow Realm** (e.g., adjusted roll 30: "You vanquish a shadow demon, claiming an Arcane Crystal").
- **Runes**: Found in **Ancient Crypts** (e.g., adjusted roll 1: "You slip past skeletal sentinels, uncovering a glowing Sacred Rune"), **Enchanted Forest** (e.g., adjusted roll 1: "You sneak past glowing sprites, discovering a Sacred Rune"), **Mystic Ruins** (e.g., adjusted roll 16: "You dispel a ruin ward, revealing a Sacred Rune"), **Shadow Realm** (e.g., adjusted roll 24: "You unlock a dark rune, finding a Sacred Rune").

Use items via the Items menu (Path 5).

---

## Win Condition

Win by achieving:
- 6,000+ Score
- 300+ Runes
- 50+ Arcane Crystals

Game ends with a victory screen showing final stats (Score, Health, Runes, Arcane Crystals, Level, Date, Time).

---

## Technical Info

- **Platform**: Windows CMD
- **Language**: Python Script (.EXE)
- **RNG Method**: D5+D5 rolls (D2: 1–5, D5: 1-5) mapped to 1–6 with Luck Modifier
- **Color Output**: Yes (yellow on black via color command)
- **Save/Load**: Text file (SaveGame.txt) with backup (SaveGame.bak)
- **Logging**: GameLog.txt records quit, loss, and win events with timestamps
- **Compatibility**: Windows 10/11 Command Prompt (codepage 1252 for ANSI support)

---

## Downloads
- [OGENS FANTASY NEXUS RPG v10 m/w Python](https://www.mediafire.com/file/xt1wa5xotmlyhee/OGENS_FANTASY_NEXUS_RPG_v10.zip/file)
- [OGENS Spin off Games m/w Python](https://www.mediafire.com/file/0atfln0isot2wmk/OGENS_Spin_Off_Games%252C_Python.zip/file)
- [DrysOGs Batch File Vault](https://ogensvideogameresearch.weebly.com/batch-files.html)

## Installation

1. Clone the repository: `git clone https://github.com/x0G3NDrysOGx/OGENS-CLAX-NEXUS-RPG.git`.
2. Or download zips from MediaFire (see Downloads).
3. Double click `OGENS CL4X NEXUS RPG.exe` to run the game.

## Contributing

Contributing
Got ideas? Submit bug reports, feature suggestions, or pull requests via GitHub Issues.

Special thanks to our dedicated beta tester: LeafChicken, whose feedback helped shape the Nexus!

## License

This project is licensed under the [MIT License](https://github.com/x0G3NDrysOGx/OGENS-CLAX-NEXUS-RPG/blob/main/LICENSE), allowing free use, modification, and distribution, including commercial purposes, as long as the license is included.

## Warning

> The Nexus is alive. Its will is unpredictable.  
> No path is safe. No victory is permanent.  
> Every step is fate.  
> Choose your path. Roll your destiny. Survive the Nexus.
