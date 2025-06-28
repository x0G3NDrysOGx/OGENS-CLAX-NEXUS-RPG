# OGENS CLAX & NEON NEXUS - D5+D5 v8 str ASCII

**A Terminal-Based Adventure of Chance & Lore**

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

**Game Type**: Text-based RPG | Windows Command Line | RNG D5+D5
 
**Author**: Developed by [Cody L Morgan]  
**Version**: 8.0  

---

## Overview

Welcome to **OGENS CLAX & NEON NEXUS - D5+D5**, a minimalist yet rich command-line RPG set in a mysterious underground realm. Brave shifting paths, collect arcane artifacts and relics, and rise through the Nexus by surviving traps, recruiting companions, and leveling up. Each playthrough is unique thanks to randomized characters and branching events driven by dice rolls. In D5+D5, a Five-sided die (1–5) and a Five-sided die (1–5) are rolled, mapping to a 5x5 grid for outcomes 1–25 for each path. A companion’s luck adjusts the outcome, creating dynamic challenges and rewards.

---

## Starting Stats

- **Health**: 100 (Max: 200)
- **Score**: 0
- **Level**: 1
- **XP to Level 2**: 50
- **Artifacts**: 0
- **Relics**: 0
- **Items**: None initially
- **Companions**: One selected randomly from a roster of 27
- PLAYER STRENGTH: 5–15, 5 is Nightmare mode

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

D2+D3:
- **Healing Potions**: Restores +25 player health (max 200 + level*10), +20 companion health (max 100). Found in **Left Tunnel** (adjusted grid 2: "A mystic vial gleams in the dust"), **Hidden Stairs** (adjusted grid 2: "A blessed elixir lies in the rubble"), **Crystal Cavern** (adjusted grid 2: "A radiant potion and talisman shine in a crevice"), or via **level-up** (if potions < 3).
- **Score Charms**: Grants +20 score when used. Found in **Right Tunnel** (adjusted grid 2: "A faint talisman sparkles softly"), **Crystal Cavern** (adjusted grid 2: "A radiant potion and talisman shine in a crevice").
- **Artifact Keys**: Grants +4 artifacts when used. Found in **Crystal Cavern** (adjusted grid 6: "A sacred key sparkles in the glow").
- **Relics**: Doubles score for the next event; grants +5 score if no score gain. Found in **Right Tunnel** (adjusted grid 3: "An urn discloses a shimmering relic"), **Crystal Cavern** (adjusted grid 3: "A shimmering relic pulses with power").
- **Artifacts**: Found in **Left Tunnel** (adjusted grid 5: "An enchanted stone pulses with energy", adjusted grid 6: "A shimmering idol glints in the shadows").

D2+D5:
- **Healing Potions**: Restores +25 player health (max 200 + level*10), +20 companion health (max 100). Found in **Hidden Stairs** (adjusted grid 5: "A blessed elixir lies in the rubble"), **Crystal Cavern** (adjusted grid 5: "A radiant potion shines in a crevice"), or via **level-up** (if potions < 3).
- **Score Charms**: Grants +20 score when used. Found in **Left Tunnel** (adjusted grid 9: "A cryptic mural unveils its wisdom and a score charm"), **Crystal Cavern** (adjusted grid 9: "A crystal prism grants foresight and a score charm").
- **Artifact Keys**: Grants +4 artifacts when used. Found in **Hidden Stairs** (adjusted grid 10: "A mystic key gleams in the dust"), **Crystal Cavern** (adjusted grid 10: "A sacred key sparkles in the glow").
- **Relics**: Doubles score for the next event; grants +5 score if no score gain. Found in **Right Tunnel** (adjusted grid 1: "A radiant sigil flares with light", adjusted grid 3: "A holy amulet glows brightly"), **Crystal Cavern** (adjusted grid 1: "A luminous jewel dazzles the eye", adjusted grid 3: "A glowing sphere hums with magic").
- **Artifacts**: Found in **Left Tunnel** (adjusted grid 1: "A shimmering idol glints in the shadows", adjusted grid 3: "An enchanted stone pulses with energy", adjusted grid 7: "Ancient roots mend your wounds and reveal an artifact"), **Right Tunnel** (adjusted grid 1: "A radiant sigil flares with light", adjusted grid 3: "A holy amulet glows brightly", adjusted grid 9: "Etched runes share their knowledge"), **Hidden Stairs** (adjusted grid 1: "A dawn gem radiates warmth", adjusted grid 3: "A sacred slab of Anubis is revealed", adjusted grid 7: "A hidden alcove offers refuge", adjusted grid 9: "Ancient etchings bestow insight"), **Crystal Cavern** (adjusted grid 1: "A luminous jewel dazzles the eye", adjusted grid 3: "A glowing sphere hums with magic", adjusted grid 7: "Crystal mist rejuvenates you and reveals an artifact", adjusted grid 9: "A crystal prism grants foresight and a score charm").

Use items via the Items menu (Path 5).

---

## Win Condition

Win by achieving:
- **6,000+ Score**
- **300+ Artifacts**
- **50+ Relics**

Game ends with a victory screen showing final stats (Score, Health, Artifacts, Relics, Level, Date, Time).

---

## Technical Info

- **Platform**: Windows CMD
- **Language**: Batch Script (.BAT)
- **RNG Method**: D5+D5 rolls (D2: 1–5, D5: 1-5) mapped to 1–6 with Luck Modifier
- **Color Output**: Yes (yellow on black via color command)
- **Save/Load**: Text file (SaveGame.txt) with backup (SaveGame.bak)
- **Logging**: GameLog.txt records quit, loss, and win events with timestamps
- **Compatibility**: Windows 10/11 Command Prompt (codepage 1252 for ANSI support)

---

## Downloads
- [OGENS CLAX NEXUS RPG v8 str ASCII bat](https://www.mediafire.com/file/5p9d98eg8r80s4h/OGENS_CL4X_NEXUS_RPG_D5%252BD5_v8_str.zip/file)
- [OGENS NEON NEXUS RPG v8 str ASCII bat](https://www.mediafire.com/file/817o0dwfwd5edbs/OGENS_NEON_NEXUS_RPG_D5%252BD5_v8_str.zip/file)
- [OGENS CLAX & NEON NEXUS RPG m/w Python](https://www.mediafire.com/file/i10hni39p3c96rl/OG3NS_CL4X_%2526_N30N_NEXUS_RPG%252C_Python.zip/file)
- [OGENS Spin off Games m/w Python](https://www.mediafire.com/file/0atfln0isot2wmk/OGENS_Spin_Off_Games%252C_Python.zip/file)
- [DrysOGs Batch File Vault](https://ogensvideogameresearch.weebly.com/batch-files.html)

## Installation

1. Clone the repository: `git clone https://github.com/[YourUsername]/OGENS-CLAX-NEXUS-RPG.git`.
2. Or download zips from MediaFire (see Downloads).
3. Double click `OGENS CL4X NEXUS RPG.bat` to run the game.
4. Customize scripts like Char list to shape your adventure.

## Contributing

Got ideas? Submit bug reports, feature suggestions, or pull requests via GitHub Issues. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the [MIT License](LICENSE.txt), allowing free use, modification, and distribution, including commercial purposes, as long as the license is included.

## Warning

> The Nexus is alive. Its will is unpredictable.  
> No path is safe. No victory is permanent.  
> Every step is fate.  
> Choose your path. Roll your destiny. Survive the Nexus.
