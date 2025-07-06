# OGENS CYBER GRID RUNNER - D10+D10

**A Terminal-Based Adventure of Neon & Code**

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## Overview

**Game Type**: Text-based RPG | Windows Command Line | RNG D10+D10  
**Author**: Developed by Cody L Morgan  
**Version**: 11.0  

Welcome to **OGENS CYBER GRID RUNNER - D10+D10**, a gripping command-line RPG set in a cyberpunk dystopia of neon-lit streets and digital battlegrounds. Navigate treacherous paths, collect crypto chips and quantum cores, and conquer the Cyber Grid by surviving traps, recruiting companions, and leveling up. Each playthrough is unique, driven by randomized companions, classes, and branching events determined by dice rolls. In D10+D10, two ten-sided dice (1–10) are rolled, mapping to outcomes 1–100 for each path, with a companion’s luck adjusting the outcome for dynamic challenges and rewards.

---

## Starting Stats

- **HEALTH**: 100 (Max: 200)
- **SCORE**: 0
- **LEVEL**: 1
- **XP to Level 2**: 50
- **CRYPTO CHIPS**: 0
- **QUANTUM CORES**: 0
- **ITEMS**: None initially (Nano Patch, Data Drive, Neon Key, Quantum Core)
- **COMPANIONS**: One selected randomly from a roster of 27
- **PLAYER STRENGTH**: 5–15 (5 is Nightmare mode)

Each companion has:
- **HEALTH**: 50–100
- **STRENGTH**: 5–15
- **LUCK**: 1–10
- **CLASS**: Randomly assigned (e.g., CyberSmith, NetRunner, Enforcer, TechWiz, StreetSam, Decker, SynthMage, CyberMonk, NanoDoc, ShadowOp, Hacker, NeonBard, ChromeLord, DataShaman, GearTinker, BioHacker, Assassin, CodeWizard, UrbanHunter, GridPriest, WarTech, AugEnchanter, NetInquisitor, CryptoCaster)

---

## Path Choices

On each turn, choose from nine options:
- **Neon Underdistrict**: Gain Score, Crypto Chips, Nano Patch, Neon Key, Quantum Core, XP, Player Health, Companion Health
- **Corporate Skyspire**: Gain Score, Crypto Chips, Nano Patch, Data Drive, Neon Key, Quantum Core, XP, Player Health, Companion Health
- **Data Vault**: Gain Score, Crypto Chips, Nano Patch, Data Drive, Neon Key, Quantum Core, XP, Player Health, Companion Health
- **Grid Wastelands**: Gain Score, Crypto Chips, Nano Patch, Data Drive, Neon Key, Quantum Core, XP, Player Health, Companion Health
- **Inventory**: Use Nano Patch (+25 player health, +20 companion health), Data Drive (+20 score), Neon Key (+4 crypto chips), Quantum Core (double score or +5 score for next event)
- **Companions**: View companion stats (Health, Strength, Luck, Class)
- **Save Game**: Save progress to a file
- **Load Game**: Load previously saved progress
- **Quit**: Exit with final stats displayed

---

## Dice & Modifiers

Events are based on a D10+D10 roll mapped to 1–100 outcomes with a Luck Modifier:
- D10: 1–10, D10: 1–10
- Outcome = Die1 + Die2 - 1
- LuckMod = Companion Luck - 5
- AdjustedRoll = Outcome + LuckMod (clamped to 1–100)

Outcomes depend on the Adjusted Roll:
- **Low rolls (e.g., 2, 7, 10, 12, 15)**: Damage (-5 to -7 player health, -5 to -7 companion health, adjusted by strength), minimal XP (1)
- **Mid rolls (e.g., 11, 13, 19, 22, 23)**: Items (Nano Patches in Paths 1, 3, 4; Data Drives in Paths 2, 3, 4; Neon Keys in Paths 1, 3, 4; Quantum Cores in Paths 1, 2, 3, 4), moderate XP (6–8)
- **High rolls (e.g., 1, 6, 16, 21, 24)**: Crypto Chips, score boosts (4–8+level), health gains (+4 player, +4 companion), high XP (8–10), Quantum Cores (Paths 1, 2, 3, 4), Neon Keys (Paths 1, 3, 4)

---

## Companion System

The following companions can join you in the Cyber Grid:
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
  - **CyberSmith**: +2 damage boost, +2 damage reduction
  - **NetRunner**: +3 hacking boost
  - **Enforcer**: +3 damage reduction
  - **TechWiz**: +2 tech boost
  - **StreetSam**: +2 damage boost
  - **Decker**: +2 score boost
  - **SynthMage**: +2 hacking boost, +2 damage reduction, +2 damage boost
  - **CyberMonk**: +2 score boost
  - **NanoDoc**: +3 healing boost
  - **ShadowOp**: +2 crypto boost
  - **Hacker**: +2 score boost
  - **NeonBard**: +2 score boost
  - **ChromeLord**: +2 damage boost
  - **DataShaman**: +3 hacking boost
  - **GearTinker**: +2 nano boost
  - **BioHacker**: +2 healing boost
  - **Assassin**: +2 score boost
  - **CodeWizard**: +2 advanced tech boost
  - **UrbanHunter**: +2 score boost
  - **GridPriest**: +3 healing boost
  - **WarTech**: +2 score boost
  - **AugEnchanter**: +2 tech boost
  - **NetInquisitor**: +2 crypto boost
  - **CryptoCaster**: +2 crypto boost

If a companion’s health reaches 0, they are deactivated but can be revived by positive outcomes (e.g., gaining items or health).

---

## Leveling & XP

**XP** is earned each turn:
- Successful events (e.g., crypto chips, quantum cores, nano patches, neon keys, health gains): 6–10 XP
- Failed events (e.g., damage taken): 1 XP

**Leveling up**:
- Increases max health (+10), health (+5), and score gains (via level-based bonuses)
- XP requirement: Level * 50 (e.g., 50 for Level 2, 100 for Level 3)

---

## Items

Items are found through events:
- **Nano Patches**: Restores +25 player health (max 200 + level*10), +20 companion health (max 100). Found in **Neon Underdistrict** (e.g., adjusted roll 4: "You slip past drones, finding a Nano Patch in a stash"), **Data Vault** (e.g., adjusted roll 19: "You tap a hidden datastream, gaining a Nano Patch"), **Grid Wastelands** (e.g., adjusted roll 27: "You stabilize a glitched node, gaining a Nano Patch").
- **Data Drives**: Grants +20 score when used. Found in **Corporate Skyspire** (e.g., adjusted roll 13: "You trade with a rogue exec, gaining a Data Drive"), **Data Vault** (e.g., adjusted roll 23: "You broker a deal with a vault AI, gaining a Data Drive"), **Grid Wastelands** (e.g., adjusted roll 35: "You gain a nomad’s trust, earning a Data Drive").
- **Neon Keys**: Grants +4 crypto chips when used. Found in **Neon Underdistrict** (e.g., adjusted roll 11: "You bribe a street fixer, earning a Neon Key"), **Data Vault** (e.g., adjusted roll 22: "You take down a vault drone, claiming a Neon Key"), **Grid Wastelands** (e.g., adjusted roll 29: "You bypass scavenger traps, securing a Neon Key").
- **Quantum Cores**: Doubles score for the next event; grants +5 score if no score gain. Found in **Neon Underdistrict** (e.g., adjusted roll 6: "You fry a rival gang’s server, snagging a Quantum Core"), **Corporate Skyspire** (e.g., adjusted roll 21: "You raid a corp vault, securing a Quantum Core"), **Data Vault** (e.g., adjusted roll 30: "You fry a vault netrunner, claiming a Quantum Core"), **Grid Wastelands** (e.g., adjusted roll 40: "You override a wasteland grid, claiming a Quantum Core").
- **Crypto Chips**: Found in **Neon Underdistrict** (e.g., adjusted roll 1: "You hack a street terminal, snagging a Crypto Chip"), **Corporate Skyspire** (e.g., adjusted roll 16: "You slice a corporate firewall, uncovering a Crypto Chip"), **Data Vault** (e.g., adjusted roll 45: "You slip through a vault network, finding a Crypto Chip"), **Grid Wastelands** (e.g., adjusted roll 51: "You hack a ruined terminal, gaining a Crypto Chip").

Use items via the Inventory menu (Path 5).

---

## Win Condition

Win by achieving:
- 6,000+ Score
- 300+ Crypto Chips
- 50+ Quantum Cores

Game ends with a victory screen showing final stats (Score, Health, Crypto Chips, Quantum Cores, Level, Strength).

---

## Technical Info

- **Platform**: Windows CMD
- **Language**: Python Script (.EXE)
- **RNG Method**: D10+D10 rolls (D10: 1–10, D10: 1–10) mapped to 1–100 with Luck Modifier
- **Color Output**: Yes (via colorama with cyan, yellow, red, green, blue, magenta on black)
- **Save/Load**: Text file (SaveGame.txt) with backup (SaveGame.bak)
- **Logging**: GameLog.txt records quit, loss, and win events with timestamps
- **Compatibility**: Windows 10/11 Command Prompt (codepage 1252 for ANSI support)

---

## Installation

1. Clone the repository: `git clone https://github.com/x0G3NDrysOGx/OGENS-CYBER-GRID-RUNNER.git`.
2. Or download zips from MediaFire (see Downloads).
3. Double click `OGENS CYBER GRID RUNNER.exe` to run the game.

## Contributing

Got ideas? Submit bug reports, feature suggestions, or pull requests via GitHub Issues.

Special thanks to our dedicated beta tester: LeafChicken, whose feedback helped shape the Cyber Grid!

## License

This project is licensed under the [MIT License](https://github.com/x0G3NDrysOGx/OGENS-CYBER-GRID-RUNNER/blob/main/LICENSE), allowing free use, modification, and distribution, including commercial purposes, as long as the license is included.

## Warning

> The Cyber Grid is alive. Its code is unpredictable.  
> No path is safe. No victory is permanent.  
> Every step is fate.  
> Choose your path. Roll your destiny. Survive the Grid.