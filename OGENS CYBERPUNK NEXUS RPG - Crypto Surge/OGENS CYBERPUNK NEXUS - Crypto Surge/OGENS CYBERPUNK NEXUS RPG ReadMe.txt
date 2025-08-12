# OGENS CYBER GRID RUNNER - D10+D10

**A Terminal-Based Adventure of Neon & Code**

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## Overview

**Game Type**: Text-based RPG | Windows Command Line | RNG D10+D10  
**Author**: Developed by Cody L Morgan  
**Version**: 12.0  

Dive into **OGENS CYBER GRID RUNNER - D10+D10**, a thrilling command-line RPG set in a cyberpunk dystopia of neon-lit streets, corporate spires, and digital wastelands. Navigate treacherous paths, collect **credits**, **crypto chips**, and **quantum cores**, and conquer the Cyber Grid by surviving traps, recruiting companions, and leveling up. Each playthrough is unique, driven by randomized companions, classes, and branching events determined by two ten-sided dice (D10+D10) mapped to outcomes 1–100. Companions enhance strategic choices, while the new shop system lets you spend credits to gear up for the challenges ahead.

---

## Starting Stats

- **HEALTH**: 100 (Max: 200)
- **SCORE**: 0
- **LEVEL**: 1
- **XP to Level 2**: 50
- **CREDITS**: 100
- **CRYPTO CHIPS**: 0
- **QUANTUM CORES**: 0
- **ITEMS**: None initially (Nano Patch, Data Drive, Neon Key, Quantum Core, Crypto Surge)
- **COMPANIONS**: One selected randomly from a roster of 27
- **PLAYER STRENGTH**: 5–14 (5 is Nightmare mode)

Each companion has:
- **HEALTH**: 50–100
- **STRENGTH**: 5–14
- **CLASS**: Randomly assigned (e.g., CyberSmith, NetRunner, Enforcer, TechWiz, StreetSam, Decker, SynthMage, CyberMonk, NanoDoc, ShadowOp, Hacker, NeonBard, ChromeLord, DataShaman, GearTinker, BioHacker, Assassin, CodeWizard, UrbanHunter, GridPriest, WarTech, AugEnchanter, NetInquisitor, CryptoCaster)

---

## Path Choices

On each turn, choose from nine options:
- **0. Shop**: Purchase items (Nano Patch, Data Drive, Neon Key, Quantum Core, Crypto Surge) using credits.
- **1. Neon Underdistrict**: Gain Credits, Crypto Chips, Nano Patch, Neon Key, Quantum Core, XP, Player Health, Companion Health.
- **2. Corporate Skyspire**: Gain Credits, Crypto Chips, Nano Patch, Data Drive, Neon Key, Quantum Core, XP, Player Health, Companion Health.
- **3. Data Vault**: Gain Credits, Crypto Chips, Nano Patch, Data Drive, Neon Key, Quantum Core, XP, Player Health, Companion Health.
- **4. Grid Wastelands**: Gain Credits, Crypto Chips, Nano Patch, Data Drive, Neon Key, Quantum Core, XP, Player Health, Companion Health.
- **5. Inventory**: Use Nano Patch (+25 player health, +20 companion health), Data Drive (+20 score), Neon Key (+4 crypto chips), Quantum Core (double score or +5 score for next event), Crypto Surge (double crypto chips for 2 events).
- **6. Companions**: View companion stats (Health, Strength, Class).
- **7. Save Game**: Save progress to `SaveGame.txt`.
- **8. Load Game**: Load progress from `SaveGame.txt`.
- **9. Quit**: Exit with final stats displayed.

---

## Dice & Modifiers

Events are determined by a D10+D10 roll mapped to 1–100 outcomes:
- **Roll Formula**: `(Die1 - 1) * 10 + Die2` (Die1: 1–10, Die2: 1–10)
- **Outcome Range**: 1–100

**Outcome Examples**:
- **Low rolls (e.g., 9, 18, 27, 45)**: Damage (-2 to -9 player/companion health, adjusted by strength/class), minimal XP (1), credit loss (-7 to -50).
- **Mid rolls (e.g., 2, 5, 7, 15, 17)**: Items (Nano Patch, Data Drive, Neon Key, Quantum Core, Crypto Surge), Credits (+10 to +70), moderate XP (8–12).
- **High rolls (e.g., 1, 3, 16, 26, 43)**: High Credits (+25 to +70), Crypto Chips (+1 to +5), score boosts (+10 to +39), health gains (+5 to +14), high XP (10–20).

**Modifiers**:
- **Player Strength**: Reduces player damage taken (e.g., -9 at strength ≤5, -2 at strength ≥15).
- **Companion Strength**: Reduces companion damage taken (similar scaling).
- **Companion Class**: Boosts rewards (e.g., +3 healing for NanoDoc, +2 score for Decker).

---

## Companion System

**Companions** (27 total, randomly assigned):
- DrysOG, Baked, Akihimura, Brandon, SS, CatzBrownout, Spvcestep, LeafChicken, Slink, Toady, Crabman, DarkSkitZo, toqer, KenshinGM, CEnnis91, XoraLoyal, alfalfa1, Paramount, JohnnyTest, cuddly, Jgunishka, Moosehead, Shinfuji, Agent21iXi, Firo, Suprafast, BadassBampy

**Companion Mechanics**:
- **Health**: 50–100; if ≤0, companion is **deactivated** but can be chosen again.
- **Revival**: On positive outcomes (e.g., gaining items, health, or credits), deactivated companions revive with **+10 health** (displayed as, e.g., “DrysOG revived with +10 health”).
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
- **Nano Patch**: ~50–87 credits (+25 player health, +20 companion health when used).
- **Data Drive**: ~75–131 credits (+20 score when used).
- **Neon Key**: ~100–175 credits (+4 crypto chips when used).
- **Quantum Core**: ~150–262 credits (doubles score or +5 score for next event).
- **Crypto Surge** (rare, 10% chance): ~300–525 credits (doubles crypto chips for 2 events).

**Price Variation**: Random modifier (25–75%) adjusts prices each shop visit.

---

## Items

Items are earned via events or purchased in the shop:
- **Nano Patch**: Restores +25 player health (max 200 + level*10), +20 companion health (max 100). Found in **Neon Underdistrict** (e.g., roll 2: “Found a discarded Nano Patch in an alley!”), **Corporate Skyspire** (e.g., roll 2: “Found a Nano Patch in an office!”), **Data Vault** (e.g., roll 2: “Found a Nano Patch in a server!”), **Grid Wastelands** (e.g., roll 2: “Found a Nano Patch in ruins!”).
- **Data Drive**: Grants +20 score. Found in **Corporate Skyspire** (e.g., roll 7: “Snagged a Data Drive from a desk!”), **Data Vault** (e.g., roll 7: “Snagged a Data Drive from a node!”), **Grid Wastelands** (e.g., roll 7: “Found a Data Drive in a wreck!”).
- **Neon Key**: Grants +4 crypto chips. Found in **Neon Underdistrict** (e.g., roll 5: “Scavenged a Neon Key from a hideout!”), **Corporate Skyspire** (e.g., roll 5: “Found a Neon Key in a vault!”), **Data Vault** (e.g., roll 5: “Found a Neon Key in a vault!”), **Grid Wastelands** (e.g., roll 5: “Found a Neon Key in debris!”).
- **Quantum Core**: Doubles score for the next event; grants +5 score if no score gain. Found in **Neon Underdistrict** (e.g., roll 10: “Found a Quantum Core in a dumpster!”), **Corporate Skyspire** (e.g., roll 10: “Found a Quantum Core in a lab!”), **Data Vault** (e.g., roll 10: “Found a Quantum Core in a server!”), **Grid Wastelands** (e.g., roll 10: “Found a Quantum Core in a ruin!”).
- **Crypto Surge**: Doubles crypto chips for 2 events. Found in **Neon Underdistrict** (e.g., roll 50: “Crypto Surge found! (Doubles crypto chips for 2 events)”), **Corporate Skyspire** (e.g., roll 50), **Data Vault** (e.g., roll 50), **Grid Wastelands** (e.g., roll 50).

Use items via the **Inventory** menu (Path 5).

---

## Leveling & XP

**XP** is earned each turn:
- **Positive events** (e.g., credits, crypto chips, items, health gains): 8–20 XP
- **Negative events** (e.g., damage, credit loss): 1 XP

**Leveling up**:
- Increases max health (+10), health (+5), and XP requirement (Level * 50, capped at 1,000,000).
- Max level: 1,000.

---

## Win Condition

Win by achieving:
- **6,000+ Score**
- **300+ Crypto Chips**
- **50+ Quantum Cores**

Victory displays final stats (Score, Health, Crypto Chips, Quantum Cores, Level, Strength, Credits).

---

## Technical Info

- **Platform**: Windows CMD
- **Language**: Python Script (.EXE)
- **RNG Method**: D10+D10 rolls mapped to 1–100
- **Dependencies**: `pygame` (audio), `colorama` (colored output: cyan, yellow, red, green, blue, magenta on black)
- **Save/Load**: `SaveGame.txt` with backup (`SaveGame.bak`)
- **Logging**: `GameLog.txt` records win, loss, quit events with timestamps
- **Audio**: Background music (`sounds/background_music.ogg`) with fallback if missing
- **Compatibility**: Windows 10/11 Command Prompt (codepage 1252 for ANSI support)

---

## Installation

1. Clone the repository: `git clone https://github.com/x0G3NDrysOGx/OGENS-CYBER-GRID-RUNNER.git`.
2. Install dependencies: `pip install pygame colorama`.
3. Ensure `sounds/background_music.ogg` is in the `sounds` folder.
4. Run `OGENS CYBER GRID RUNNER.exe` or `python main.py`.

## Contributing

Submit bug reports, feature suggestions, or pull requests via GitHub Issues. Special thanks to **LeafChicken** for beta testing and shaping the Cyber Grid!

## License

Licensed under the [MIT License](https://github.com/x0G3NDrysOGx/OGENS-CYBER-GRID-RUNNER/blob/main/LICENSE).

## Warning

> The Cyber Grid pulses with danger. Its code is alive.  
> Every roll shapes your fate. Every companion carries a spark.  
> Spend your credits wisely. Revive your allies. Survive the Grid.

---