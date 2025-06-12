==================================================
               OGENS CLAX NEXUS - D2+D5
      A Terminal-Based Adventure of Chance & Lore
GAME TYPE:
  Text-based RPG | Windows Command Line | RNG D6
AUTHOR:
  Developed by [Cody L Morgan]
VERSION:
  6.0
==================================================
>> OVERVIEW:
Welcome to OGENS CLAX NEXUS - D2+D5, a minimalist yet rich 
command-line RPG set in a mysterious underground realm. 
Brave shifting paths, collect arcane artifacts and relics, 
and rise through the Nexus by surviving traps, recruiting 
companions, and leveling up.
Each playthrough is unique thanks to randomized characters, 
D2+D3 rolls (mapped to 1–6 outcomes), and branching events.
==================================================
>> STARTING STATS:
HEALTH:        100 (Max: 200)
SCORE:         0
LEVEL:         1
XP to Level 2: 50
ARTIFACTS:     0
RELICS:        0
ITEMS:         None initially
COMPANIONS:    One selected randomly from a roster of 25
Each companion has:
  HEALTH:     50–100
  STRENGTH:   5–15
  LUCK:       1–10
==================================================
>> PATH CHOICES:
On each turn, choose from nine options:
LEFT TUNNEL
  Score, Artifacts, XP, Player Health, Companion Health

RIGHT TUNNEL
  Score, Artifacts, Score Charm, Relics, XP, Player Health, Companion Health

HIDDEN STAIRS
  Score, Artifacts, Healing Potion, Artifact Key, XP, Player Health, Companion Health

CRYSTAL CAVERN
  Score, Artifacts, Healing Potion, Artifact Key, Relics, XP, Player Health, Companion Health

ITEMS
  Use Healing Potion (+25 player health, +20 companion health), Score Charm (+20 score), Artifact Key (+4 artifacts), Relic (double score or +5 score for next event)

CHARACTER LIST
  View companion stats (Health, Strength, Luck)

SAVE GAME
  Save current progress to a file

LOAD GAME
  Load previously saved progress

QUIT
  Exit the game with final stats displayed
==================================================
>> DICE & MODIFIERS:
Events are based on a D2+D3 roll mapped to 1–6 outcomes with Luck Modifier:
  D2: 1–2, D3: 1–3
  Outcome = (D2-1)*3 + D3
  LuckMod = Companion Luck - 5
  AdjustedRoll = Outcome + LuckMod (clamped to 1–6)
Outcomes depend on the Adjusted Roll:
  Low rolls (e.g., 2, 3, 4): Damage (-10 to -17+Strength player health, -10 to -17+Strength companion health), minimal XP (0–1)
  Mid rolls (e.g., 5): Items (Potions in Paths 3 and 4, Charms in Path 2, Relics in Paths 2 and 4), moderate XP (5)
  High rolls (e.g., 1, 6): Artifacts, score boosts (6–8+level), health gains (+2 player, +2 companion), high XP (5–10), Relics (Paths 2 and 4), Keys (Paths 3 and 4)
==================================================
>> COMPANION SYSTEM:
OGENS CLAX NEXUS - Companion Characters
The following companions can join you during your adventure in the ancient labyrinth:
  DrysOG  
  Baked 
  Akihimura 
  Brandon
  Spvcestep  
  LeafChicken  
  Slink  
  Toady  
  Crabman  
  DarkSkitZo  
  toqer  
  KenshinGM  
  CEnnis91  
  XoraLoyal  
  alfalfa1  
  Paramount  
  JohnnyTest  
  CuddlyWolf  
  Jgunishka  
  Moosehead  
  Shinfuji  
  Agent21iXi  
  Firo  
  Suprafast  
  BadassBampy  
Companions influence:
  Luck: Adjusts dice rolls via LuckMod
  Strength: Reduces companion damage taken
  Health: Determines companion survival
If a companion's health reaches 0, they fall, and a new companion is selected randomly on the next turn.
==================================================
>> LEVELING & XP:
XP is earned each turn:
  Successful events (e.g., artifacts, relics, potions, keys, health gains): 5–10 XP
  Failed events (e.g., damage taken): 0–1 XP
Leveling up:
  Increases max health (+10), health (+3), and score gains (via level-based bonuses)
  Grants a Healing Potion if current count is <3
  XP requirement: Level * 50 (e.g., 50 for Level 2, 100 for Level 3)
==================================================
>> ITEMS:
Items are found through events or leveling up and include:
  Healing Potions: +25 player health (max 200+level*10), +20 companion health (max 100). Found in Hidden Stairs and Crystal Cavern events or via level-up.
  Score Charms:    +20 score. Found in Right Tunnel events.
  Artifact Keys:   +4 artifacts. Found in Hidden Stairs and Crystal Cavern events.
  Relics:         Doubles score for the next event; grants +5 score if no score gain. Found in Right Tunnel and Crystal Cavern events.
Items are used via the Items menu (Path 5).
==================================================
>> WIN CONDITION:
Win by achieving:
  6,000+ Score
  250+ Artifacts
  50+ Relics
Game ends with a victory screen showing final stats (Score, Health, Artifacts, Relics, Level, Date, Time).
==================================================
>> TECHNICAL INFO:
Platform:     Windows CMD
Language:     Batch Script (.BAT)
RNG Method:   D2+D3 rolls (D2: 1–2, D3: 1–3) mapped to 1–6 with Luck Modifier
Color Output: Yes (via color command, yellow on black)
Save/Load:    Text file (SaveGame.txt) with backup (SaveGame.bak)
Logging:      GameLog.txt records quit, loss, and win events with timestamps
Compatibility: Windows 10/11 Command Prompt (codepage 1252 for ANSI support)
==================================================
>> WARNING:
The Nexus is alive. Its will is unpredictable.
No path is safe. No victory is permanent.
Every step is fate.
Choose your path.
Roll your destiny.
Survive the Nexus.
==================================================
