# OGENS FANTASY NEXUS RPG - D5+D10

**A Terminal-Based Adventure of Strategy & Lore**

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## Overview

**Game Type**: Text-based RPG | Windows Command Line | RNG D5+D10  
**Author**: Developed by Cody L Morgan  
**Version**: 11.0  

Welcome to **OGENS FANTASY NEXUS RPG - D5+D10**, a thrilling command-line RPG set in a mystic realm of ancient crypts, enchanted forests, and shadowy realms. Navigate perilous paths, collect **credits**, **runes**, and **mystic keys**, and conquer the Nexus by surviving traps, recruiting companions, and leveling up. Each playthrough is unique, driven by randomized companions, classes, and branching events determined by a five-sided die (D5) and a ten-sided die (D10), mapped to outcomes 1–50. Companions enhance strategic choices, while the new shop system lets you spend credits to bolster your quest.

---

## Starting Stats

- **HEALTH**: 100 (Max: 200)
- **SCORE**: 0
- **LEVEL**: 1
- **XP to Level 2**: 50
- **CREDITS**: 100
- **RUNES**: 0
- **ITEMS**: None initially (Healing Potion, Magic Scroll, Mystic Key, Rune Pulse)
- **COMPANIONS**: One selected randomly from a roster of 27
- **PLAYER STRENGTH**: 5–14 (5 is Nightmare mode)

Each companion has:
- **HEALTH**: 50–100
- **STRENGTH**: 5–14
- **CLASS**: Randomly assigned (e.g., CyberSmith, NetRunner, Enforcer, TechWiz, StreetSam, Decker, SynthMage, CyberMonk, NanoDoc, ShadowOp, Hacker, NeonBard, ChromeLord, DataShaman, GearTinker, BioHacker, Assassin, CodeWizard, UrbanHunter, GridPriest, WarTech, AugEnchanter, NetInquisitor, CryptoCaster)

---

## Path Choices

On each turn, choose from nine options:
- **0. Shop**: Purchase items (Healing Potion, Magic Scroll, Mystic Key, Rune Pulse) using credits.
- **1. Ancient Crypts**: Gain Credits, Runes, XP, Player Health, Companion Health.
- **2. Enchanted Forest**: Gain Credits, Runes, Magic Scroll, Rune Pulse, XP, Player Health, Companion Health.
- **3. Mystic Ruins**: Gain Credits, Runes, Healing Potion, Mystic Key, XP, Player Health, Companion Health.
- **4. Shadow Realm**: Gain Credits, Runes, Healing Potion, Mystic Key, Rune Pulse, XP, Player Health, Companion Health.
- **5. Items**: Use Healing Potion (+25 player health, +20 companion health), Magic Scroll (+20 score), Mystic Key (+4 runes), Rune Pulse (double runes for 2 events).
- **6. Character List**: View companion stats (Health, Strength, Class).
- **7. Save Game**: Save progress to `SaveGame.txt`.
- **8. Load Game**: Load progress from `SaveGame.txt`.
- **9. Quit**: Exit with final stats displayed.

---

## Dice & Modifiers

Events are determined by a D5+D10 roll mapped to 1–50 outcomes:
- **Roll Formula**: `(D5-1)*10 + D10` (D5: 1–5, D10: 1–10)
- **Outcome Range**: 1–50

**Outcome Examples**:
- **Low rolls (e.g., 9, 18, 27, 45)**: Damage (-2 to -9 player/companion health, adjusted by strength/class), minimal XP (1), credit loss (-7 to -50).
- **Mid rolls (e.g., 2, 5, 7, 15, 17)**: Items (Healing Potion, Magic Scroll, Mystic Key, Rune Pulse), Credits (+10 to +70), moderate XP (8–12).
- **High rolls (e.g., 1, 3, 16, 26, 43)**: High Credits (+25 to +70), Runes (+1 to +5), score boosts (+10 to +39), health gains (+5 to +14), high XP (10–20).

**Modifiers**:
- **Player Strength**: Reduces player damage taken (e.g., -9 at strength ≤5, -2 at strength ≥15).
- **Companion Strength**: Reduces companion damage taken (similar scaling).
- **Companion Class**: Boosts rewards (e.g., +3 healing for NanoDoc, +2 score for Decker).

---

## Companion System

**Companions** (27 total, randomly assigned):
- DrysOG, Baked, Akihimura, Brandon, SS, CatzBrownout, Spvcestep, LeafChicken, Slink, Toady, Crabman, DarkSkitZo, toqer, KenshinGM, CEnnis91, XoraLoyal, alfalfa1, Paramount, JohnnyTest, cuddly, Jgunishka, Moosehead, Shinfuji, Agent21iXi, Firo, Suprafast, BadassBampy

**Companion Mechanics**:
- **Health**: 50–100; if ≤0, companion is **fallen** but can be chosen again.
- **Revival**: On positive outcomes (e.g., gaining items, health, or credits), fallen companions revive with **+10 health** (displayed as, e.g., “DrysOG revived with +10 health”).
- **Strength**: 5–14, reduces damage taken.
- **Class Bonuses**:
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

---

## Shop System

Access the **Shop** (Path 0) to purchase items using **credits**:
- **Healing Potion**: ~50–87 credits (+25 player health, +20 companion health when used).
- **Magic Scroll**: ~75–131 credits (+20 score when used).
- **Mystic Key**: ~100–175 credits (+4 runes when used).
- **Rune Pulse** (rare, 10% chance): ~300–525 credits (doubles runes for 2 events).

**Price Variation**: Random modifier (25–75%) adjusts prices each shop visit.

---

## Items

Items are earned via events or purchased in the shop:
- **Healing Potion**: Restores +25 player health (max 200 + level*10), +20 companion health (max 100). Found in **Mystic Ruins** (e.g., roll 2: “Discovered a Healing Potion in a tomb!”), **Shadow Realm** (e.g., roll 2: “Found a Healing Potion in a dark shrine!”).
- **Magic Scroll**: Grants +20 score. Found in **Enchanted Forest** (e.g., roll 3: “Found a Magic Scroll in an elven grove!”).
- **Mystic Key**: Grants +4 runes. Found in **Mystic Ruins** (e.g., roll 5: “Found a Mystic Key in a ruin!”), **Shadow Realm** (e.g., roll 5: “Claimed a Mystic Key from a shadow vault!”).
- **Rune Pulse**: Doubles runes for 2 events. Found in **Enchanted Forest** (e.g., roll 10: “Found a Rune Pulse in a mystic grove!”), **Shadow Realm** (e.g., roll 10: “Discovered a Rune Pulse in a dark altar!”).
- **Runes**: Found in **Ancient Crypts** (e.g., roll 1: “Avoided a skeleton ambush, found runes!”), **Enchanted Forest** (e.g., roll 1: “Outsmarted forest spirits, gained runes!”), **Mystic Ruins** (e.g., roll 1: “Bypassed a ruin trap, earned runes!”), **Shadow Realm** (e.g., roll 1: “Traded with a shadow wraith, gained runes!”).

Use items via the **Items** menu (Path 5).

---

## Leveling & XP

**XP** is earned each turn:
- **Positive events** (e.g., credits, runes, items, health gains): 8–20 XP
- **Negative events** (e.g., damage, credit loss): 1 XP

**Leveling up**:
- Increases max health (+10), health (+5), and XP requirement (Level * 50, capped at 1,000,000).
- Max level: 1,000.

---

## Win Condition

Win by achieving:
- **6,000+ Score**
- **300+ Runes**
- **50+ Rune Pulses**

Victory displays final stats (Score, Health, Runes, Rune Pulses, Level, Strength, Credits).

---

## Technical Info

- **Platform**: Windows CMD
- **Language**: Python Script (.EXE)
- **RNG Method**: D5+D10 rolls mapped to 1–50
- **Dependencies**: `pygame` (audio), `colorama` (colored output: cyan, yellow, red, green, blue, magenta on black)
- **Save/Load**: `SaveGame.txt` with backup (`SaveGame.bak`)
- **Logging**: `GameLog.txt` records win, loss, quit events with timestamps
- **Audio**: Background music (`sounds/background_music.ogg`) with fallback if missing
- **Compatibility**: Windows 10/11 Command Prompt (codepage 1252 for ANSI support)

---

## Installation

1. Clone the repository: `git clone https://github.com/x0G3NDrysOGx/OGENS-FANTASY-NEXUS-RPG.git`.
2. Install dependencies: `pip install pygame colorama`.
3. Ensure `sounds/background_music.ogg` is in the `sounds` folder.
4. Run `OGENS FANTASY NEXUS RPG.exe` or `python main.py`.

## Contributing

Submit bug reports, feature suggestions, or pull requests via GitHub Issues. Special thanks to **LeafChicken** for beta testing and shaping the Nexus!

## License

Licensed under the [MIT License](https://github.com/x0G3NDrysOGx/OGENS-FANTASY-NEXUS-RPG/blob/main/LICENSE).

## Warning

> The Nexus pulses with ancient magic. Its will is unpredictable.  
> Every roll shapes your fate. Every companion carries a spark.  
> Spend your credits wisely. Revive your allies. Survive the Nexus.

---