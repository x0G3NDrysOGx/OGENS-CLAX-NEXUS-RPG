# OGENS CLAX NEXUS - D2+D5/D2+D3 v5 & v6 str

**A Terminal-Based Adventure of Chance & Lore**

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

**Game Type**: Text-based RPG | Windows Command Line | RNG D6  
**Author**: Developed by [Cody L Morgan]  
**Version**: 6.0  

---

## Overview

Welcome to **OGENS CLAX NEXUS - D2+D5**, a minimalist yet rich command-line RPG set in a mysterious underground realm. Brave shifting paths, collect arcane artifacts and relics, and rise through the Nexus by surviving traps, recruiting companions, and leveling up. Each playthrough is unique thanks to randomized characters, D2+D3 rolls (mapped to 1–6/1-10 outcomes), and branching events.

---

## Starting Stats

- **Health**: 100 (Max: 200)
- **Score**: 0
- **Level**: 1
- **XP to Level 2**: 50
- **Artifacts**: 0
- **Relics**: 0
- **Items**: None initially
- **Companions**: One selected randomly from a roster of 25

Each companion has:
- **Health**: 50–100
- **Strength**: 5–15
- **Luck**: 1–10

---

## Path Choices

On each turn, choose from nine options:

- **Left Tunnel**: Gain Score, Artifacts, XP, Player Health, Companion Health
- **Right Tunnel**: Gain Score, Artifacts, Score Charm, Relics, XP, Player Health, Companion Health
- **Hidden Stairs**: Gain Score, Artifacts, Healing Potion, Artifact Key, XP, Player Health, Companion Health
- **Crystal Cavern**: Gain Score, Artifacts, Healing Potion, Artifact Key, Relics, XP, Player Health, Companion Health
- **Items**: Use Healing Potion (+25 player health, +20 companion health), Score Charm (+20 score), Artifact Key (+4 artifacts), Relic (double score or +5 score for next event)
- **Character List**: View companion stats (Health, Strength, Luck)
- **Save Game**: Save progress to a file
- **Load Game**: Load previously saved progress
- **Quit**: Exit with final stats displayed

---

## Dice & Modifiers

Events are based on a D2+D3 roll mapped to 1–6 outcomes with a Luck Modifier:
- **D2**: 1–2, **D3**: 1–3
- **Outcome** = (D2-1)*3 + D3
- **LuckMod** = Companion Luck - 5
- **AdjustedRoll** = Outcome + LuckMod (clamped to 1–6)

**Outcomes** depend on the Adjusted Roll:
- **Low rolls (2, 3, 4)**: Damage (-10 to -17+Strength player health, -10 to -17+Strength companion health), minimal XP (0–1)
- **Mid rolls (5)**: Items (Potions in Paths 3 and 4, Charms in Path 2, Relics in Paths 2 and 4), moderate XP (5)
- **High rolls (1, 6)**: Artifacts, score boosts (6–8+level), health gains (+2 player, +2 companion), high XP (5–10), Relics (Paths 2 and 4), Keys (Paths 3 and 4)

---

## Companion System

The following companions can join you in the ancient labyrinth:

- DrysOG
- Baked
- Akihimura
- Brandon
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
- CuddlyWolf
- Jgunishka
- Moosehead
- Shinfuji
- Agent21iXi
- Firo
- Suprafast
- BadassBampy

**Companions influence**:
- **Luck**: Adjusts dice rolls via LuckMod
- **Strength**: Reduces companion damage taken
- **Health**: Determines companion survival

If a companion’s health reaches 0, they fall, and a new companion is randomly selected on the next turn.

---

## Leveling & XP

**XP** is earned each turn:
- Successful events (e.g., artifacts, relics, potions, keys, health gains): 5–10 XP
- Failed events (e.g., damage taken): 0–1 XP

**Leveling up**:
- Increases max health (+10), health (+3), and score gains (via level-based bonuses)
- Grants a Healing Potion if current count is <3
- XP requirement: Level * 50 (e.g., 50 for Level 2, 100 for Level 3)

---

## Items

Items are found through events or leveling up:

- **Healing Potions**: +25 player health (max 200+level*10), +20 companion health (max 100). Found in Hidden Stairs, Crystal Cavern, or via level-up.
- **Score Charms**: +20 score. Found in Right Tunnel.
- **Artifact Keys**: +4 artifacts. Found in Hidden Stairs, Crystal Cavern.
- **Relics**: Doubles score for the next event; grants +5 score if no score gain. Found in Right Tunnel, Crystal Cavern.

Use items via the Items menu (Path 5).

---

## Win Condition

Win by achieving:
- **6,000+ Score**
- **250+ Artifacts**
- **50+ Relics**

Game ends with a victory screen showing final stats (Score, Health, Artifacts, Relics, Level, Date, Time).

---

## Technical Info

- **Platform**: Windows CMD
- **Language**: Batch Script (.BAT)
- **RNG Method**: D2+D3 rolls (D2: 1–2, D3: 1–3) mapped to 1–6 with Luck Modifier
- **Color Output**: Yes (yellow on black via color command)
- **Save/Load**: Text file (SaveGame.txt) with backup (SaveGame.bak)
- **Logging**: GameLog.txt records quit, loss, and win events with timestamps
- **Compatibility**: Windows 10/11 Command Prompt (codepage 1252 for ANSI support)

---

## Downloads

- [OGENS CLAX NEXUS RPG v5 & v6 str](https://www.mediafire.com/file/s9st1lnrxxdv1yx/OGENS_CL4X_NEXUS_RPG_v5_%2526_v6_Str.zip/file)
- [DrysOGs Batch File Vault](https://ogensvideogameresearch.weebly.com/batch-files.html)

## Installation

1. Clone the repository: `git clone https://github.com/[YourUsername]/OGENS-CLAX-NEXUS-RPG.git`.
2. Or download zips from MediaFire (see Downloads).
3. Run `scripts/main.bat` in a Windows command prompt.
4. Customize scripts or images in `/images` to shape your adventure.

## Contributing

Got ideas? Submit bug reports, feature suggestions, or pull requests via GitHub Issues. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the [MIT License](LICENSE.txt), allowing free use, modification, and distribution, including commercial purposes, as long as the license is included.

## Warning

> The Nexus is alive. Its will is unpredictable.  
> No path is safe. No victory is permanent.  
> Every step is fate.  
> Choose your path. Roll your destiny. Survive the Nexus.
