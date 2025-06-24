@echo off
chcp 1252 >nul
setlocal EnableDelayedExpansion

color 0a
title NEON NEXUS - D5+D5

rem TITLE SCREEN
cls
echo.
echo   //===\\
echo  //     \\
echo //_______\\
echo ^|  ***  ^| NEON NEXUS
echo ^|  ***  ^| SURVIVE THE UNDERWORLD
echo ^|_______^| 
echo.
echo --------------------------------------
echo OGens NEON NEXUS - D5+D5
echo --------------------------------------
echo.
echo.
echo        Press Enter to hack in
echo    Neon Nexus Underworld...
echo.
pause >nul

rem Initialize player stats
set /a score=0
set /a health=100
set /a max_health=200
set /a artifacts=0
set /a nano_medpack=0
set /a data_shard=0
set /a crypto_key=0
set /a quantum_mod=0
set /a player_strength=(%random% %% 10) + 5
set "stat_changes="
set "character="
set "quantum_mod_active="

rem Leveling system initialization
set /a level=1
set /a xp=0
set /a xp_needed=50

rem Define companions (unchanged)
set "companions=DrysOG Baked Akihimura Brandon SS CatzBrownout Spvcestep LeafChicken Slink Toady Crabman DarkSkitZo toqer KenshinGM CEnnis91 XoraLoyal alfalfa1 Paramount JohnnyTest cuddly Jgunishka Moosehead Shinfuji Agent21iXi Firo Suprafast BadassBampy"

rem Initialize companion stats
for %%a in (!companions!) do (
    call :set_random_stats %%a
)
goto :after_stat_init

:set_random_stats
set /a "%1_health=(%random% %% 50) + 50"
set /a "%1_strength=(%random% %% 10) + 5"
set /a "%1_luck=(%random% %% 10) + 1"
exit /b

:after_stat_init

:loop
cls
rem Reset temporary variables
set "choice="
set "result="
set /a score_change=0
set /a player_health_change=0
set /a comp_health_change=0
set /a artifact_change=0
set /a medpack_change=0
set /a shard_change=0
set /a key_change=0
set /a mod_change=0
set /a xp_change=0
set /a levelup_health_change=0
set /a display_player_health_change=0
set /a show_health_change=0
set "stat_changes_temp="
set "comp_health_change="
set "leveled_up="
set /a pre_player_health=0
set /a pre_comp_health=0
set /a post_player_health=0
set /a post_comp_health=0

echo --------------------------------------
echo OGENS NEON NEXUS - D5+D5
echo --------------------------------------
echo.
echo NAVIGATING THE NEON UNDERWORLD...
echo.
echo Strength: !player_strength!
echo Level: !level! (XP: !xp!/!xp_needed!)
echo Health: !health!  Score: !score!  Data Cores: !artifacts!  Quantum Mods: !quantum_mod!
echo Progress: Score !score!/6000 Data Cores !artifacts!/300 Quantum Mods !quantum_mod!/50
echo.
if defined character if "!character!" neq "" (
    echo Companion: !character! (Health: !%character%_health!, Strength: !%character%_strength!, Luck: !%character%_luck!)
    echo.
)
if defined stat_changes (
    echo Changes: !stat_changes!
)
echo    1 2
echo   ( o )
echo    3 4
echo    NET
echo.
echo CHOOSE YOUR PATH...
echo Path 1 - Data Vaults (fortified server hub)
echo Path 2 - Neon Slums (gang-run black market)
echo Path 3 - Corporate Spire (megacorp skyscraper)
echo Path 4 - Undernet Grid (virtual reality network)
echo Path 5 - Inventory
echo Path 6 - Contact List
echo Path 7 - Save Game
echo Path 8 - Load Game
echo Path 9 - Quit
echo.
set /p choice=Enter path (1-9): 
set "choice=%choice: =%"
echo !choice!| findstr /r "^[1-9]$" >nul
if errorlevel 1 (
    echo.
    echo INVALID PATH SELECTED...
    set "stat_changes=Invalid path selected"
    echo Press any key to try again...
    pause >nul
    goto loop
)

if "!choice!"=="1" goto path1
if "!choice!"=="2" goto path2
if "!choice!"=="3" goto path3
if "!choice!"=="4" goto path4
if "!choice!"=="5" goto inventory
if "!choice!"=="6" goto characters
if "!choice!"=="7" goto save
if "!choice!"=="8" goto load
if "!choice!"=="9" goto quit

:path1
echo.
echo INFILTRATING THE DATA VAULTS...
echo.
echo   //===\\
echo   ^| *** ^|
echo   ^| *** ^|
echo   \\===//
echo.
goto event

:path2
echo.
echo NAVIGATING THE NEON SLUMS...
echo.
echo   ------
echo   ^| *  ^|
echo   ^| *  ^|
echo   ------
echo.
goto event

:path3
echo.
echo ASCENDING THE CORPORATE SPIRE...
echo.
echo   ^|^|^|^|
echo   ^| ^ ^ ^|
echo   ^| ^ ^ ^|
echo   ^|^|^|^|
echo.
goto event

:path4
echo.
echo JACKING INTO THE UNDERNET GRID...
echo.
echo   ~~~~~
echo   ^| ^^ ^|
echo   ^| ^^ ^|
echo   ~~~~~
echo.
goto event

:event
set "leveled_up="
set "comp_health_change="
rem Pick a random character
set /a companion_count=0
for %%a in (!companions!) do set /a companion_count+=1
set /a char_index=(%random% %% !companion_count!) + 1
set count=1
for %%a in (!companions!) do (
    if !count! equ !char_index! (
        set "character=%%a"
    )
    set /a count+=1
)

rem Roll D5+D5, map to 5x5 grid (25 outcomes)
set /a d5_1=(%random% %% 5) + 1
set /a d5_2=(%random% %% 5) + 1
set /a grid_outcome=((!d5_1!-1)*5) + !d5_2!
set /a luck_modifier=0
if defined character if "!character!" neq "" if defined %character%_luck (
    set /a luck_modifier=!%character%_luck! - 5
)
set /a adjusted_grid=!grid_outcome! + !luck_modifier!
if !adjusted_grid! lss 1 set /a adjusted_grid=1
if !adjusted_grid! gtr 25 set /a adjusted_grid=25

echo Rolling for the path's challenge...
echo Die 1 (D5): !d5_1! + Die 2 (D5): !d5_2! = Outcome !grid_outcome! (Adjusted by Luck: !adjusted_grid!)
echo.

rem Get companion strength
set /a char_strength=5
if defined character if "!character!" neq "" if defined %character%_strength (
    set /a char_strength=!%character%_strength!
)

rem Capture health before changes
set /a pre_player_health=!health!
set /a pre_comp_health=0
if defined character if "!character!" neq "" if defined %character%_health (
    set /a pre_comp_health=!%character%_health!
)

rem Path outcomes (defined in separate grids below)
if "!choice!"=="1" call :path1_outcomes !adjusted_grid!
if "!choice!"=="2" call :path2_outcomes !adjusted_grid!
if "!choice!"=="3" call :path3_outcomes !adjusted_grid!
if "!choice!"=="4" call :path4_outcomes !adjusted_grid!

rem Apply quantum mod effect
if defined quantum_mod_active if "!quantum_mod_active!"=="1" (
    if !score_change! equ 0 (
        set /a score_change=5
        set "stat_changes_temp=Quantum Mod grants +5 score"
    ) else (
        set /a score_change*=2
        set "stat_changes_temp=Quantum Mod doubled score gain"
    )
    set "quantum_mod_active="
)

rem Update stats
set /a score+=!score_change!
if !score! gtr 10000000 (
    set /a score=10000000
    set "stat_changes_temp=Score capped at 10000000"
)
if !score! lss 0 set /a score=0
set /a health+=!player_health_change!
set /a artifacts+=!artifact_change!
set /a nano_medpack+=!medpack_change!
set /a data_shard+=!shard_change!
set /a crypto_key+=!key_change!
set /a quantum_mod+=!mod_change!
set /a xp+=!xp_change!
if !xp! gtr 1000000 (
    set /a xp=1000000
    if defined stat_changes_temp (
        set "stat_changes_temp=!stat_changes_temp!, XP capped at 1000000" 
    ) else (
        set "stat_changes_temp=XP capped at 1000000"
    )
)
if defined character if "!character!" neq "" if defined %character%_health (
    set /a !character!_health+=!comp_health_change!
    if !%character%_health! gtr 100 set /a !character!_health=100
    if !%character%_health! lss 0 set /a !character!_health=0
    set /a post_comp_health=!%character%_health!
    if !comp_health_change! neq 0 (
        if !comp_health_change! gtr 0 (
            set "comp_health_change=!character!'s Health +!comp_health_change!"
        ) else (
            set "comp_health_change=!character!'s Health !comp_health_change!"
        )
    )
)
set /a post_player_health=!health!
call :level_check
if !health! gtr !max_health! (
    set /a health=!max_health!
    if defined stat_changes_temp (
        set "stat_changes_temp=!stat_changes_temp!, Health capped at !max_health!"
    ) else (
        set "stat_changes_temp=Health capped at !max_health!"
    )
)
if !health! leq 0 goto gameover
if !score! geq 6000 if !artifacts! geq 300 if !quantum_mod! geq 50 goto youwin

rem Check companion's health
if defined character if "!character!" neq "" if defined %character%_health (
    set /a char_health=!%character%_health!
    if !char_health! leq 0 (
        if defined stat_changes_temp (
            set "stat_changes_temp=!stat_changes_temp!, !character! has been flatlined..."
        ) else (
            set "stat_changes_temp=!character! has been flatlined..."
        )
        echo !character! has been flatlined in the underworld...
        echo.
        set "character="
    )
)

rem Build stat changes
set "stat_changes=!stat_changes_temp!"
if !score_change! neq 0 (
    if defined stat_changes (
        set "stat_changes=!stat_changes!, Score !score_change!"
    ) else (
        set "stat_changes=Score !score_change!"
    )
)
if !show_health_change! equ 1 (
    set /a total_health_change=!display_player_health_change! + !levelup_health_change!
    if !total_health_change! neq 0 (
        if !total_health_change! gtr 0 (
            set "player_health_display=Health +!total_health_change!"
        ) else (
            set "player_health_display=Health !total_health_change!"
        )
        if defined stat_changes (
            set "stat_changes=!stat_changes!, !player_health_display!"
        ) else (
            set "stat_changes=!player_health_display!"
        )
    )
    if defined character if "!character!" neq "" (
        if !pre_comp_health! neq !post_comp_health! (
            if defined stat_changes (
                set "stat_changes=!stat_changes!, Total Damage: Player [!pre_player_health! -> !post_player_health!], Companion [!pre_comp_health! -> !post_comp_health!]"
            ) else (
                set "stat_changes=Total Damage: Player [!pre_player_health! -> !post_player_health!], Companion [!pre_comp_health! -> !post_comp_health!]"
            )
        ) else (
            if defined stat_changes (
                set "stat_changes=!stat_changes!, Total Damage: Player [!pre_player_health! -> !post_player_health!]"
            ) else (
                set "stat_changes=Total Damage: Player [!pre_player_health! -> !post_player_health!]"
            )
        )
    ) else (
        if defined stat_changes (
            set "stat_changes=!stat_changes!, Total Damage: Player [!pre_player_health! -> !post_player_health!]"
        ) else (
            set "stat_changes=Total Damage: Player [!pre_player_health! -> !post_player_health!]"
        )
    )
)
if !artifact_change! neq 0 (
    if defined stat_changes (
        set "stat_changes=!stat_changes!, Data Cores !artifact_change!"
    ) else (
        set "stat_changes=Data Cores !artifact_change!"
    )
)
if !medpack_change! neq 0 (
    if defined stat_changes (
        set "stat_changes=!stat_changes!, Nano-Medpacks !medpack_change!"
    ) else (
        set "stat_changes=Nano-Medpacks !medpack_change!"
    )
)
if !shard_change! neq 0 (
    if defined stat_changes (
        set "stat_changes=!stat_changes!, Data Shards !shard_change!"
    ) else (
        set "stat_changes=Data Shards !shard_change!"
    )
)
if !key_change! neq 0 (
    if defined stat_changes (
        set "stat_changes=!stat_changes!, Crypto Keys !key_change!"
    ) else (
        set "stat_changes=Crypto Keys !key_change!"
    )
)
if !mod_change! neq 0 (
    if defined stat_changes (
        set "stat_changes=!stat_changes!, Quantum Mods !mod_change!"
    ) else (
        set "stat_changes=Quantum Mods !mod_change!"
    )
)
if !xp_change! neq 0 (
    if defined stat_changes (
        set "stat_changes=!stat_changes!, XP +!xp_change!"
    ) else (
        set "stat_changes=XP +!xp_change!"
    )
)
if defined comp_health_change if "!comp_health_change!" neq "" (
    if defined stat_changes (
        set "stat_changes=!stat_changes!, !comp_health_change!"
    ) else (
        set "stat_changes=!comp_health_change!"
    )
)

echo !character! - !result!
echo.
if defined stat_changes (
    echo Changes: !stat_changes!
    echo.
)

echo Press any key to continue...
pause >nul
goto loop

:path1_outcomes
set /a outcome=%1
if !outcome! == 1 (set "result=Stealth Success: You bypass security drones, snagging a Data Core" & set /a score_change=8 + !level! & set /a artifact_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 2 (set "result=Stealth Betrayal: Your fixer sells you out, security closes in" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 3 (set "result=Stealth Trap: Motion sensors trigger turrets" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 4 (set "result=Stealth Chaos: You slip through, but knock over a server rack" & set /a score_change=3 + !level! & set /a xp_change=5 & set /a comp_health_change=-5 + !char_strength! & set /a player_health_change=-5 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 5 (set "result=Stealth Success: You evade patrols, gain a Nano-Medpack" & set /a score_change=5 + !level! & set /a medpack_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 6 (set "result=Combat Success: You blast through guards, find a Quantum Mod" & set /a score_change=7 + !level! & set /a artifact_change=1 & set /a mod_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 7 (set "result=Combat Betrayal: Your hired muscle turns on you" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 8 (set "result=Combat Trap: Explosive mines detonate" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 9 (set "result=Combat Success: You clear the vault, snag a Data Core" & set /a score_change=4 + !level! & set /a artifact_change=1 & set /a xp_change=6 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 10 (set "result=Combat Escalation: Reinforcements swarm the vault" & set /a comp_health_change=-20 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-20 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 11 (set "result=Social Success: You bribe a guard, gain a Data Core" & set /a score_change=6 + !level! & set /a artifact_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 12 (set "result=Social Betrayal: The guard rats you out to the corp" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 13 (set "result=Social Success: You charm a tech, gain a Crypto Key" & set /a score_change=5 + !level! & set /a key_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 14 (set "result=Social Success: You negotiate access, gain a Data Shard" & set /a score_change=3 + !level! & set /a shard_change=1 & set /a xp_change=5 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 15 (set "result=Social Escalation: Your talk draws corpo enforcers" & set /a comp_health_change=-20 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-20 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 16 (set "result=Hacking Success: You crack the mainframe, find a Nano-Medpack" & set /a score_change=8 + !level! & set /a medpack_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 17 (set "result=Hacking Betrayal: Your ICEbreaker backdoors you" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 18 (set "result=Hacking Trap: Black ICE fries your rig" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 19 (set "result=Hacking Success: You salvage data from a crashed system" & set /a score_change=4 + !level! & set /a artifact_change=1 & set /a xp_change=6 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 20 (set "result=Hacking Escalation: Your breach alerts the netrunners" & set /a comp_health_change=-20 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-20 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 21 (set "result=Intimidation Success: You scare off guards, snag a Crypto Key" & set /a score_change=5 + !level! & set /a key_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 22 (set "result=Intimidation Betrayal: Your threats backfire, guards attack" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 23 (set "result=Intimidation Success: You bully a tech, gain a Quantum Mod" & set /a score_change=5 + !level! & set /a mod_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 24 (set "result=Intimidation Success: You clear the vault, gain a Data Core" & set /a score_change=6 + !level! & set /a artifact_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 25 (set "result=Intimidation Trap: Your show of force triggers drones" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
exit /b

:path2_outcomes
set /a outcome=%1
if !outcome! == 1 (set "result=Stealth Betrayal: Your contact snitches to the gang" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 2 (set "result=Stealth Trap: You trip a laser grid" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 3 (set "result=Stealth Success: You slip through the market, snag a Data Shard" & set /a score_change=4 + !level! & set /a shard_change=1 & set /a xp_change=6 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 4 (set "result=Stealth Escalation: Your presence draws a gang hit squad" & set /a comp_health_change=-20 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-20 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 5 (set "result=Combat Betrayal: Your ally switches sides mid-fight" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 6 (set "result=Combat Trap: A hidden turret opens fire" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 7 (set "result=Combat Success: You clear the market, gain a Data Core" & set /a score_change=6 + !level! & set /a artifact_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 8 (set "result=Combat Escalation: The fight draws rival gangs" & set /a comp_health_change=-20 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-20 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 9 (set "result=Social Betrayal: The vendor tips off the gang" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 10 (set "result=Social Trap: Your deal triggers a sting operation" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 11 (set "result=Social Success: You charm a dealer, gain a Nano-Medpack" & set /a score_change=5 + !level! & set /a medpack_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 12 (set "result=Social Escalation: Your deal draws corpo spies" & set /a comp_health_change=-20 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-20 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 13 (set "result=Hacking Betrayal: Your netrunner ally sells your code" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 14 (set "result=Hacking Success: You hack a vendor’s rig, gain a Data Core" & set /a score_change=8 + !level! & set /a artifact_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 15 (set "result=Hacking Success: You crack a terminal, gain a Nano-Medpack" & set /a score_change=6 + !level! & set /a medpack_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 16 (set "result=Hacking Success: You salvage data, gain a Data Shard" & set /a score_change=4 + !level! & set /a shard_change=1 & set /a xp_change=6 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 17 (set "result=Intimidation Success: You strong-arm a deal, gain a Crypto Key" & set /a score_change=5 + !level! & set /a key_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 18 (set "result=Intimidation Success: You clear the market, gain a Quantum Mod" & set /a score_change=5 + !level! & set /a mod_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 19 (set "result=Intimidation Success: You intimidate a vendor, gain a Data Core" & set /a score_change=6 + !level! & set /a artifact_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 20 (set "result=Stealth Success: You slip past sentries, snag a Data Core" & set /a score_change=8 + !level! & set /a artifact_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 21 (set "result=Combat Success: You clear out gangers, find a Quantum Mod" & set /a score_change=7 + !level! & set /a artifact_change=1 & set /a mod_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 22 (set "result=Social Success: You barter for a Crypto Key" & set /a score_change=5 + !level! & set /a key_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 23 (set "result=Hacking Success: You breach a node, gain a Crypto Key" & set /a score_change=5 + !level! & set /a key_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 24 (set "result=Hacking Trap: A virus fries your deck" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 25 (set "result=Hacking Escalation: Your breach pulls in net vigilantes" & set /a comp_health_change=-20 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-20 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
exit /b

:path3_outcomes
set /a outcome=%1
if !outcome! == 1 (set "result=Stealth Success: You sneak past execs, grab a Data Core" & set /a score_change=8 + !level! & set /a artifact_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 2 (set "result=Stealth Betrayal: Your insider tips off security" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 3 (set "result=Stealth Trap: Biometric scanners lock you in" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 4 (set "result=Stealth Success: You evade drones, gain a Data Shard" & set /a score_change=3 + !level! & set /a shard_change=1 & set /a xp_change=5 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 5 (set "result=Stealth Success: You bypass security, gain a Nano-Medpack" & set /a score_change=5 + !level! & set /a medpack_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 6 (set "result=Combat Success: You overpower security, find a Quantum Mod" & set /a score_change=7 + !level! & set /a artifact_change=1 & set /a mod_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 7 (set "result=Combat Betrayal: Your merc ally double-crosses you" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 8 (set "result=Combat Trap: Automated turrets shred you" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 9 (set "result=Combat Success: You clear the floor, gain a Data Core" & set /a score_change=4 + !level! & set /a artifact_change=1 & set /a xp_change=6 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 10 (set "result=Combat Escalation: Elite enforcers swarm the floor" & set /a comp_health_change=-20 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-20 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 11 (set "result=Social Success: You charm an exec, gain a Nano-Medpack" & set /a score_change=6 + !level! & set /a medpack_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 12 (set "result=Social Betrayal: The exec sets you up" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 13 (set "result=Social Success: You bribe a guard, gain a Crypto Key" & set /a score_change=5 + !level! & set /a key_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 14 (set "result=Social Success: You negotiate access, gain a Data Core" & set /a score_change=6 + !level! & set /a artifact_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 15 (set "result=Social Escalation: Your talk pulls in corpo hitmen" & set /a comp_health_change=-20 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-20 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 16 (set "result=Hacking Success: You breach the spire’s net, grab a Data Core" & set /a score_change=8 + !level! & set /a artifact_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 17 (set "result=Hacking Betrayal: Your code is sold to a rival corp" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 18 (set "result=Hacking Trap: A firewall fries your neural link" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 19 (set "result=Hacking Success: You salvage data, gain a Quantum Mod" & set /a score_change=4 + !level! & set /a mod_change=1 & set /a xp_change=6 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 20 (set "result=Hacking Escalation: Your breach draws net enforcers" & set /a comp_health_change=-20 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-20 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 21 (set "result=Intimidation Success: You bully a guard, gain a Data Shard" & set /a score_change=5 + !level! & set /a shard_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 22 (set "result=Intimidation Betrayal: The guard calls for backup" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 23 (set "result=Intimidation Success: You scare an exec, gain a Crypto Key" & set /a score_change=5 + !level! & set /a key_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 24 (set "result=Intimidation Success: You clear the floor, gain a Data Core" & set /a score_change=6 + !level! & set /a artifact_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 25 (set "result=Intimidation Trap: Your threats trigger a gas trap" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
exit /b

:path4_outcomes
set /a outcome=%1
if !outcome! == 1 (set "result=Stealth Betrayal: Your avatar is sold out by a netrunner" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 2 (set "result=Stealth Trap: A data trap zaps your avatar" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 3 (set "result=Stealth Success: You bypass a firewall, gain a Data Shard" & set /a score_change=4 + !level! & set /a shard_change=1 & set /a xp_change=6 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 4 (set "result=Stealth Escalation: Your hack pulls in virtual enforcers" & set /a comp_health_change=-20 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-20 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 5 (set "result=Combat Betrayal: Your co-hacker turns on you" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 6 (set "result=Combat Trap: A kill-switch fries your link" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 7 (set "result=Combat Success: You stabilize the grid, gain a Data Core" & set /a score_change=6 + !level! & set /a artifact_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 8 (set "result=Combat Escalation: Rogue AIs swarm your avatar" & set /a comp_health_change=-20 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-20 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 9 (set "result=Social Betrayal: The sysadmin rats you out" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 10 (set "result=Social Trap: Your ruse triggers a data lock" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 11 (set "result=Social Success: You bluff a node operator, gain a Crypto Key" & set /a score_change=5 + !level! & set /a key_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 12 (set "result=Social Escalation: Your talk draws net vigilantes" & set /a comp_health_change=-20 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-20 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 13 (set "result=Hacking Betrayal: Your code is stolen by a rival" & set /a comp_health_change=-17 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-17 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 14 (set "result=Hacking Success: You crack a secure node, find a Nano-Medpack" & set /a score_change=8 + !level! & set /a medpack_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 15 (set "result=Hacking Success: You breach a node, gain a Data Core" & set /a score_change=6 + !level! & set /a artifact_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 16 (set "result=Hacking Success: You salvage data, gain a Data Shard" & set /a score_change=4 + !level! & set /a shard_change=1 & set /a xp_change=6 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 17 (set "result=Intimidation Success: You scare off a netrunner, gain a Crypto Key" & set /a score_change=5 + !level! & set /a key_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 18 (set "result=Intimidation Success: You clear the grid, gain a Quantum Mod" & set /a score_change=5 + !level! & set /a mod_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 19 (set "result=Intimidation Success: You bully a node, gain a Data Core" & set /a score_change=6 + !level! & set /a artifact_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 20 (set "result=Stealth Success: You ghost through the net, snag a Data Core" & set /a score_change=8 + !level! & set /a artifact_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 21 (set "result=Combat Success: You shred ICE, find a Quantum Mod" & set /a score_change=7 + !level! & set /a artifact_change=1 & set /a mod_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 22 (set "result=Social Success: You bluff a sysadmin, gain a Data Shard" & set /a score_change=6 + !level! & set /a shard_change=1 & set /a xp_change=10 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 23 (set "result=Hacking Success: You crack a node, gain a Crypto Key" & set /a score_change=5 + !level! & set /a key_change=1 & set /a xp_change=8 & set /a comp_health_change=4 & set /a player_health_change=4 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 24 (set "result=Hacking Trap: Black ICE zaps your neural link" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-15 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
if !outcome! == 25 (set "result=Hacking Escalation: Your breach pulls in AI hunters" & set /a comp_health_change=-20 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-20 + !player_strength! & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
exit /b

:level_check
if defined leveled_up exit /b
if !xp! geq !xp_needed! (
    if !level! geq 1000 (
        set "stat_changes=Max Level 1000 reached, no further leveling"
        exit /b
    )
    set /a level+=1
    set /a max_health+=10
    if !max_health! gtr 100000 set /a max_health=100000
    set /a health+=5
    set /a levelup_health_change=5
    set /a xp-=!xp_needed!
    if !xp! gtr 1000000 set /a xp=1000000
    set /a xp_needed=!level! * 50
    if !xp_needed! gtr 1000000 set /a xp_needed=1000000
    if !nano_medpack! lss 3 (
        set /a nano_medpack+=1
        if defined stat_changes (
            set "stat_changes=!stat_changes!, Level !level! reached, Max Health +10, Health +5, Nano-Medpacks +1"
        ) else (
            set "stat_changes=Level !level! reached, Max Health +10, Health +5, Nano-Medpacks +1"
        )
    ) else (
        if defined stat_changes (
            set "stat_changes=!stat_changes!, Level !level! reached, Max Health +10, Health +5"
        ) else (
            set "stat_changes=Level !level! reached, Max Health +10, Health +5"
        )
    )
    set "leveled_up=1"
)
exit /b

:characters
cls
echo --------------------------------------
echo OGENS NEON NEXUS - D5+D5
echo --------------------------------------
echo.
echo UNDERWORLD CONTACTS...
echo.
for %%a in (!companions!) do (
    echo %%a - Health: !%%a_health!, Strength: !%%a_strength!, Luck: !%%a_luck!
)
echo.
echo Press any key to return...
pause >nul
goto loop

:inventory
cls
echo --------------------------------------
echo OGENS NEON NEXUS - D5+D5
echo --------------------------------------
echo.
echo   //===\\
echo  // *** \\
echo //_______\\
echo ^|  ***  ^|
echo ^|_______^| 
echo.
echo GEAR CACHE...
echo.
echo Nano-Medpack (!nano_medpack!): Restores vitality...
echo Data Shard (!data_shard!): Boosts cred...
echo Crypto Key (!crypto_key!): Unlocks data cores...
echo Quantum Mod (!quantum_mod!): Doubles score gains for the next event...
echo.
echo USE AN ITEM...
echo 1. Nano-Medpack (+25 health)
echo 2. Data Shard (+20 score)
echo 3. Crypto Key (+4 data cores)
echo 4. Quantum Mod (Double score next event)
echo 5. Return
echo.
set /p inv_choice=Select an item (1-5): 
set "inv_choice=%inv_choice: =%"
echo !inv_choice!| findstr /r "^[1-5]$" >nul
if errorlevel 1 (
    echo.
    echo INVALID CHOICE...
    set "stat_changes=Invalid choice"
    echo.
    echo Changes: !stat_changes!
    echo.
    echo Press any key to try again...
    pause >nul
    goto inventory
)

if "!inv_choice!"=="1" (
    if !nano_medpack! gtr 0 (
        set /a pre_player_health=!health!
        set /a pre_comp_health=0
        if defined character if "!character!" neq "" if defined %character%_health (
            set /a pre_comp_health=!%character%_health!
        )
        set /a health+=25
        set /a nano_medpack-=1
        if !health! gtr !max_health! (
            set /a health=!max_health!
            set "stat_changes=Health capped at !max_health!, Nano-Medpacks -1"
        ) else (
            set "stat_changes=Health +25, Nano-Medpacks -1"
        )
        set /a post_player_health=!health!
        set /a post_comp_health=0
        if defined character if "!character!" neq "" if defined %character%_health (
            set /a !character!_health+=20
            if !%character%_health! gtr 100 set /a !character!_health=100
            set /a post_comp_health=!%character%_health!
            set "stat_changes=!stat_changes!, !character!'s Health +20, Total Damage: Player [!pre_player_health! -> !post_player_health!], Companion [!pre_comp_health! -> !post_comp_health!]"
        ) else (
            set "stat_changes=!stat_changes!, Total Damage: Player [!pre_player_health! -> !post_player_health!]"
        )
        echo.
        echo Nano-Medpack used - Vitality restored...
    ) else (
        echo.
        echo No Nano-Medpacks remain...
        set "stat_changes=No Nano-Medpacks remain"
    )
    echo.
    if defined stat_changes (
        echo Changes: !stat_changes!
        echo.
    )
    echo Press any key to return...
    pause >nul
    goto loop
)
if "!inv_choice!"=="2" (
    if !data_shard! gtr 0 (
        set /a score+=20
        set /a data_shard-=1
        set "stat_changes=Score +20, Data Shards -1"
        echo.
        echo Data Shard used - Cred gained...
    ) else (
        echo.
        echo No Data Shards remain...
        set "stat_changes=No Data Shards remain"
    )
    echo.
    if defined stat_changes (
        echo Changes: !stat_changes!
        echo.
    )
    echo Press any key to return...
    pause >nul
    goto loop
)
if "!inv_choice!"=="3" (
    if !crypto_key! gtr 0 (
        set /a artifacts+=4
        set /a crypto_key-=1
        set "stat_changes=Data Cores +4, Crypto Keys -1"
        echo.
        echo Crypto Key used - Data cores unlocked...
    ) else (
        echo.
        echo No Crypto Keys remain...
        set "stat_changes=No Crypto Keys remain"
    )
    echo.
    if defined stat_changes (
        echo Changes: !stat_changes!
        echo.
    )
    echo Press any key to return...
    pause >nul
    goto loop
)
if "!inv_choice!"=="4" (
    if !quantum_mod! gtr 0 (
        set /a quantum_mod-=1
        set "quantum_mod_active=1"
        set "stat_changes=Quantum Mod used - Score doubled for next event, Quantum Mods -1"
        echo.
        echo Quantum Mod used - Next event's score gains will be doubled...
    ) else (
        echo.
        echo No Quantum Mods remain...
        set "stat_changes=No Quantum Mods remain"
    )
    echo.
    if defined stat_changes (
        echo Changes: !stat_changes!
        echo.
    )
    echo Press any key to return...
    pause >nul
    goto loop
)
if "!inv_choice!"=="5" (
    goto loop
)

:save
cls
echo --------------------------------------
echo OGENS NEON NEXUS - D5+D5
echo --------------------------------------
echo.
echo UPLOADING YOUR DATA TO THE GRID...
echo.
if not defined score set /a score=0
if not defined health set /a health=100
if not defined max_health set /a max_health=200
if not defined artifacts set /a artifacts=0
if not defined nano_medpack set /a nano_medpack=0
if not defined data_shard set /a data_shard=0
if not defined crypto_key set /a crypto_key=0
if not defined quantum_mod set /a quantum_mod=0
if not defined level set /a level=1
if not defined xp set /a xp=0
if not defined xp_needed set /a xp_needed=50
if not defined character set "character="
if not defined player_strength set /a player_strength=(%random% %% 10) + 5
for %%a in (!companions!) do (
    if not defined %%a_health call :set_random_stats %%a
)
set "save_success=0"
set /a retry_count=0
:save_retry
if exist SaveGame.txt copy SaveGame.txt SaveGame.bak >nul
(
    echo score=!score!
    echo health=!health!
    echo max_health=!max_health!
    echo artifacts=!artifacts!
    echo nano_medpack=!nano_medpack!
    echo data_shard=!data_shard!
    echo crypto_key=!crypto_key!
    echo quantum_mod=!quantum_mod!
    echo level=!level!
    echo xp=!xp!
    echo xp_needed=!xp_needed!
    echo character=!character!
    echo player_strength=!player_strength!
    for %%a in (!companions!) do (
        echo %%a_health=!%%a_health!
        echo %%a_strength=!%%a_strength!
        echo %%a_luck=!%%a_luck!
    )
) >SaveGame.txt 2>nul
if exist SaveGame.txt (
    for %%F in (SaveGame.txt) do if %%~zF gtr 0 (
        findstr /c:"score=" /c:"health=" /c:"max_health=" /c:"artifacts=" /c:"level=" SaveGame.txt >nul
        if not errorlevel 1 (
            set "save_success=1"
        )
    )
)
if !save_success! equ 0 (
    if !retry_count! lss 2 (
        set /a retry_count+=1
        timeout /t 1 /nobreak >nul
        goto save_retry
    ) else (
        if exist SaveGame.bak (
            copy SaveGame.bak SaveGame.txt >nul
            echo Failed to upload data, restored from backup...
        ) else (
            echo Failed to upload data, no backup available...
        )
        for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
        set "formatted_date=%dt:~4,2%/%dt:~6,2%/%dt:~0,4%"
        set "formatted_time=%dt:~8,2%:%dt:~10,2%"
        echo !formatted_date! !formatted_time! - Save failed: File missing or corrupted>>GameLog.txt 2>nul
    )
) else (
    echo Your data is uploaded to the grid!
)
echo.
echo Press any key to return...
pause >nul
goto loop

:load
cls
echo --------------------------------------
echo OGENS NEON NEXUS - D5+D5
echo --------------------------------------
echo.
if not exist SaveGame.txt (
    echo No saved data found...
    echo.
    echo Press any key to return...
    pause >nul
    goto loop
)
echo DOWNLOADING YOUR DATA FROM THE GRID...
echo.
for /f "tokens=1,2 delims==" %%a in (SaveGame.txt) do (
    set "%%a=%%b"
)
if not defined score set /a score=0
if not defined health set /a health=100
if not defined max_health set /a max_health=200
if not defined artifacts set /a artifacts=0
if not defined nano_medpack set /a nano_medpack=0
if not defined data_shard set /a data_shard=0
if not defined crypto_key set /a crypto_key=0
if not defined quantum_mod set /a quantum_mod=0
if not defined level set /a level=1
if not defined xp set /a xp=0
if not defined xp_needed set /a xp_needed=50
if not defined character set "character="
if not defined player_strength set /a player_strength=(%random% %% 10) + 5
for %%a in (!companions!) do (
    if not defined %%a_health call :set_random_stats %%a
)
echo The grid restores your data!
echo.
echo Press any key to continue...
pause >nul
goto loop

:quit
cls
echo --------------------------------------
echo OGENS NEON NEXUS - D5+D5
echo --------------------------------------
echo.
echo HACKING OUT OF THE UNDERWORLD...
echo.
echo Final Score: !score!
echo Final Health: !health!
echo Final Data Cores: !artifacts!
echo Final Quantum Mods: !quantum_mod!
echo Final Level: !level!
echo.
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "formatted_date=%dt:~4,2%/%dt:~6,2%/%dt:~0,4%"
set "formatted_time=%dt:~8,2%:%dt:~10,2%"
echo Date: !formatted_date!
echo Time: !formatted_time!
echo.
echo !formatted_date! !formatted_time! - Quit>>GameLog.txt 2>nul
echo Press any key to end...
pause >nul
exit /b

:gameover
cls
echo --------------------------------------
echo OGENS NEON NEXUS - D5+D5
echo --------------------------------------
echo.
echo   //===\\
echo  // RIP \\
echo //_______\\
echo ^|  ***  ^|
echo ^|_______^| 
echo.
echo THE UNDERWORLD FLATLINES YOU...
echo.
echo Final Score: !score!
echo Final Health: !health!
echo Final Data Cores: !artifacts!
echo Final Quantum Mods: !quantum_mod!
echo Final Level: !level!
echo.
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "formatted_date=%dt:~4,2%/%dt:~6,2%/%dt:~0,4%"
set "formatted_time=%dt:~8,2%:%dt:~10,2%"
echo Date: !formatted_date!
echo Time: !formatted_time!
echo.
echo !formatted_date! !formatted_time! - Loss>>GameLog.txt 2>nul
echo Press any key to end...
pause >nul
exit /b

:youwin
cls
echo --------------------------------------
echo OGENS NEON NEXUS - D5+D5
echo --------------------------------------
echo.
echo   //***\\
echo  // *** \\
echo //_______\\
echo ^|  WIN  ^|
echo ^|_______^| 
echo.
echo YOU CONQUER THE UNDERWORLD...
echo.
echo Final Score: !score!
echo Final Health: !health!
echo Final Data Cores: !artifacts!
echo Final Quantum Mods: !quantum_mod!
echo Final Level: !level!
echo.
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "formatted_date=%dt:~4,2%/%dt:~6,2%/%dt:~0,4%"
set "formatted_time=%dt:~8,2%:%dt:~10,2%"
echo Date: !formatted_date!
echo Time: !formatted_time!
echo.
echo !formatted_date! !formatted_time! - Win>>GameLog.txt 2>nul
echo Press any key to end...
pause >nul
exit /b