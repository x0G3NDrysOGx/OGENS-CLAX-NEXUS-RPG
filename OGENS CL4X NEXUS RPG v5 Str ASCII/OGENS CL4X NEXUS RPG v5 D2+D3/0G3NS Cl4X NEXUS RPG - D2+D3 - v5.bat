@echo off
chcp 1252 >nul
setlocal EnableDelayedExpansion

color 0e
title OGENS CLAX NEXUS - D2+D3

rem TITLE SCREEN
cls
echo.
echo   _____
echo  /_____\
echo /_______\
echo ^|  ***  ^| OGENS CLAX NEXUS
echo ^|  ***  ^| ENTER THE LABYRINTH
echo ^|_______^| 
echo.
echo --------------------------------------
echo OGENS CLAX NEXUS - D2+D3
echo --------------------------------------
echo.
echo.
echo        Press Enter to enter
echo    OGens Clax Nexus Labyrinth...
echo.
pause >nul

rem Initialize player stats
set /a score=0
set /a health=100
set /a max_health=200
set /a artifacts=0
set /a healing_potion=0
set /a ascore_charm=0
set /a artifact_key=0
set /a relics=0
set /a player_strength=(%random% %% 10) + 5
set "stat_changes="
set "character="
set "relic_active="

rem Leveling system initialization
set /a level=1
set /a xp=0
set /a xp_needed=50

rem Define companions
set "companions=DrysOG Baked Akihimura Brandon SS CatzBrownout Spvcestep LeafChicken Slink Toady Crabman DarkSkitZo toqer KenshinGM CEnnis91 XoraLoyal alfalfa1 Paramount JohnnyTest cuddlyWolf Jgunishka Moosehead Shinfuji Agent21iXi Firo Suprafast BadassBampy"

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
set /a potion_change=0
set /a charm_change=0
set /a key_change=0
set /a relic_change=0
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
echo OGENS CLAX NEXUS - D2+D3
echo --------------------------------------
echo.
echo EXPLORING THE ANCIENT LABYRINTH...
echo.
echo Strength: !player_strength!
echo Level: !level! (XP: !xp!/!xp_needed!)
echo Health: !health!  Score: !score!  Artifacts: !artifacts!  Relics: !relics!
echo Progress: Score !score!/6000 Artifacts !artifacts!/250 Relics !relics!/50
echo.
if defined character if "!character!" neq "" (
    echo Companion: !character! (Health: !%character%_health!, Strength: !%character%_strength!, Luck: !%character%_luck!)
    echo.
)
if defined stat_changes (
    echo Changes: !stat_changes!
    echo.
)
echo    1 2
echo   ( o )
echo    3 4
echo    ORB
echo.
echo CHOOSE YOUR PATH...
echo Path 1 - Left Tunnel (dark and narrow)
echo Path 2 - Right Tunnel (lit by torches)
echo Path 3 - Hidden Stairs (ancient and crumbling)
echo Path 4 - Crystal Cavern (glowing faintly)
echo Path 5 - Items
echo Path 6 - Character List
echo Path 7 - Save Game
echo Path 8 - Load Game
echo Path 9 - Quit
echo.
set /p choice=Enter path (1-9): 
set "choice=%choice: =%"

if "!choice!"=="1" goto path1
if "!choice!"=="2" goto path2
if "!choice!"=="3" goto path3
if "!choice!"=="4" goto path4
if "!choice!"=="5" goto inventory
if "!choice!"=="6" goto characters
if "!choice!"=="7" goto save
if "!choice!"=="8" goto load
if "!choice!"=="9" goto quit
echo.
echo INVALID PATH CHOSEN...
set "stat_changes=Invalid path chosen"
echo Press any key to try again...
pause >nul
goto loop

:path1
echo.
echo TRAVERSING THE LEFT TUNNEL...
echo.
echo   /\/\/\
echo   ^|    ^|
echo   ^|    ^|
echo   \/\/\/
echo.
goto event

:path2
echo.
echo TRAVERSING THE RIGHT TUNNEL...
echo.
echo   ------
echo   ^| *  ^|
echo   ^| *  ^|
echo   ------
echo.
goto event

:path3
echo.
echo CLIMBING THE HIDDEN STAIRS...
echo.
echo   =====
echo   ^|   ^|
echo   ^|   ^|
echo   ====
echo.
goto event

:path4
echo.
echo ENTERING THE CRYSTAL CAVERN...
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

rem Roll D2+D3, map to grid outcome (1-6), adjust by Luck
set /a d2=(%random% %% 2) + 1
set /a d3=(%random% %% 3) + 1
set /a grid_outcome=(%d2%-1)*3 + %d3%
set /a luck_modifier=0
if defined character if "!character!" neq "" (
    if defined %character%_luck (
        set /a luck_modifier=!%character%_luck! - 5
    ) else (
        set /a luck_modifier=0
    )
)
set /a adjusted_grid=!grid_outcome! + !luck_modifier!
if !adjusted_grid! lss 1 set /a adjusted_grid=1
if !adjusted_grid! gtr 6 set /a adjusted_grid=6

echo Rolling for the path's challenge...
echo Die 1 (D2): !d2! + Die 2 (D3): !d3! = Outcome !grid_outcome! (Adjusted by Luck: !adjusted_grid!)
echo.

rem Get companion strength
set /a char_strength=5
if defined character if "!character!" neq "" (
    if defined %character%_strength (
        set /a char_strength=!%character%_strength!
    ) else (
        set /a char_strength=5
    )
)

rem Capture health before changes
set /a pre_player_health=!health!
set /a pre_comp_health=0
if defined character if "!character!" neq "" (
    if defined %character%_health (
        set /a pre_comp_health=!%character%_health!
    )
)

rem Path 1: Left Tunnel (Grid: 1-6)
if "!choice!"=="1" (
    if !adjusted_grid! == 1 (set "result=Spiked arrows shoot from hidden slits" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=2 & set /a player_health_change=-9 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 2 (set "result=A mystic vial gleams in the dust" & set /a potion_change=1 & set /a xp_change=6 & set /a comp_health_change=3 & set /a player_health_change=3 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 3 (set "result=A secret passage is uncovered" & set /a score_change=2 + !char_strength! + !level! & set /a xp_change=4 & set /a comp_health_change=2 & set /a player_health_change=0 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 4 (set "result=A shamanic scorpion stings" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=2 & set /a player_health_change=-9 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 5 (set "result=An enchanted stone pulses with energy" & set /a score_change=8 + !level! & set /a artifact_change=1 & set /a xp_change=8 & set /a comp_health_change=5 & set /a player_health_change=3 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 6 (set "result=A shimmering idol glints in the shadows" & set /a score_change=10 + !level! & set /a artifact_change=1 & set /a xp_change=12 & set /a comp_health_change=5 & set /a player_health_change=3 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
)

rem Path 2: Right Tunnel (Grid: 1-6)
if "!choice!"=="2" (
    if !adjusted_grid! == 1 (set "result=Slippery rocks cause a fall" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=1 & set /a player_health_change=-9 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 2 (set "result=A faint talisman sparkles softly" & set /a charm_change=1 & set /a xp_change=6 & set /a comp_health_change=3 & set /a player_health_change=3 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 3 (set "result=An urn discloses a shimmering relic" & set /a score_change=2 + !char_strength! + !level! & set /a relic_change=1 & set /a xp_change=4 & set /a comp_health_change=2 & set /a player_health_change=0 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 4 (set "result=Thorny tendrils lash out" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=2 & set /a player_health_change=-9 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 5 (set "result=A holy amulet glows brightly" & set /a score_change=10 + !level! & set /a artifact_change=1 & set /a xp_change=12 & set /a comp_health_change=5 & set /a player_health_change=3 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 6 (set "result=A radiant sigil flares with light" & set /a score_change=9 + !level! & set /a artifact_change=1 & set /a xp_change=12 & set /a comp_health_change=5 & set /a player_health_change=3 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
)

rem Path 3: Hidden Stairs (Grid: 1-6)
if "!choice!"=="3" (
    if !adjusted_grid! == 1 (set "result=A steep tumble grazes" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=2 & set /a player_health_change=-9 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 2 (set "result=A blessed elixir lies in the rubble" & set /a potion_change=1 & set /a xp_change=6 & set /a comp_health_change=3 & set /a player_health_change=3 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 3 (set "result=Falling pebbles hint at a secret" & set /a score_change=2 + !char_strength! & set /a xp_change=4 & set /a comp_health_change=2 & set /a player_health_change=0 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 4 (set "result=A swarm of bats overwhelms" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=2 & set /a player_health_change=-9 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 5 (set "result=A sacred slab of Anubis is revealed" & set /a score_change=12 + !level! & set /a artifact_change=1 & set /a xp_change=12 & set /a comp_health_change=5 & set /a player_health_change=3 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 6 (set "result=A dawn gem radiates warmth" & set /a score_change=8 + !level! & set /a artifact_change=1 & set /a xp_change=12 & set /a comp_health_change=5 & set /a player_health_change=3 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
)

rem Path 4: Crystal Cavern (Grid: 1-6)
if "!choice!"=="4" (
    if !adjusted_grid! == 1 (set "result=Sharp crystals pierce" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=2 & set /a player_health_change=-9 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 2 (set "result=A radiant potion and talisman shine in a crevice" & set /a potion_change=1 & set /a charm_change=1 & set /a xp_change=6 & set /a comp_health_change=3 & set /a player_health_change=3 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 3 (set "result=A shimmering relic pulses with power" & set /a score_change=3 + !char_strength! + !level! & set /a relic_change=1 & set /a xp_change=4 & set /a comp_health_change=2 & set /a player_health_change=0 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 4 (set "result=A crystal hawk dives" & set /a comp_health_change=-15 + !char_strength! & set /a xp_change=2 & set /a player_health_change=-9 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 5 (set "result=A glowing sphere hums with magic" & set /a score_change=11 + !level! & set /a artifact_change=1 & set /a xp_change=12 & set /a comp_health_change=5 & set /a player_health_change=3 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
    if !adjusted_grid! == 6 (set "result=A sacred key sparkles in the glow" & set /a key_change=1 & set /a xp_change=6 & set /a comp_health_change=5 & set /a player_health_change=3 & set /a display_player_health_change=!player_health_change! & set show_health_change=1)
)

rem Apply relic effect
if defined relic_active if "!relic_active!"=="1" (
    if !score_change! equ 0 (
        set /a score_change=5
        set "stat_changes_temp=Relic grants +5 score"
    ) else (
        set /a score_change*=2
        set "stat_changes_temp=Relic doubled score gain"
    )
    set "relic_active="
)

rem Update stats
set /a score+=!score_change!
if !score! lss 0 set /a score=0
set /a health+=!player_health_change!
if !health! gtr !max_health! (
    set /a health=!max_health!
    echo Health capped at !max_health!...
)
set /a post_player_health=!health!
set /a post_comp_health=0
if defined character if "!character!" neq "" (
    if defined %character%_health (
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
)
set /a artifacts+=!artifact_change!
set /a healing_potion+=!potion_change!
set /a score_charm+=!charm_change!
set /a artifact_key+=!key_change!
set /a relics+=!relic_change!
set /a xp+=!xp_change!
call :level_check
if !health! leq 0 goto gameover
if !score! geq 6000 if !artifacts! geq 250 if !relics! geq 50 goto youwin

rem Check companion's health
if defined character if "!character!" neq "" (
    if defined %character%_health (
        set /a char_health=!%character%_health!
        if !char_health! leq 0 (
            if defined stat_changes (
                set "stat_changes=!stat_changes!, !character! has fallen..."
            ) else (
                set "stat_changes=!character! has fallen..."
            )
            echo !character! has fallen in the labyrinth...
            echo.
            set "character="
        )
    )
)

rem Build stat changes
set "stat_changes_temp="
if !score_change! neq 0 (
    set "stat_changes_temp=Score !score_change!"
)
if !show_health_change! equ 1 (
    set /a total_health_change=!display_player_health_change! + !levelup_health_change!
    if !total_health_change! neq 0 (
        if !total_health_change! gtr 0 (
            set "player_health_display=Health +!total_health_change!"
        ) else (
            set "player_health_display=Health !total_health_change!"
        )
        if defined stat_changes_temp (
            set "stat_changes_temp=!stat_changes_temp!, !player_health_display!"
        ) else (
            set "stat_changes_temp=!player_health_display!"
        )
    )
    rem Add Total Damage
    if defined character if "!character!" neq "" (
        if !pre_comp_health! neq !post_comp_health! (
            if defined stat_changes_temp (
                set "stat_changes_temp=!stat_changes_temp!, Total Damage: Player [!pre_player_health! -> !post_player_health!], Companion [!pre_comp_health! -> !post_comp_health!]"
            ) else (
                set "stat_changes_temp=Total Damage: Player [!pre_player_health! -> !post_player_health!], Companion [!pre_comp_health! -> !post_comp_health!]"
            )
        ) else (
            if defined stat_changes_temp (
                set "stat_changes_temp=!stat_changes_temp!, Total Damage: Player [!pre_player_health! -> !post_player_health!]"
            ) else (
                set "stat_changes_temp=Total Damage: Player [!pre_player_health! -> !post_player_health!]"
            )
        )
    ) else (
        if defined stat_changes_temp (
            set "stat_changes_temp=!stat_changes_temp!, Total Damage: Player [!pre_player_health! -> !post_player_health!]"
        ) else (
            set "stat_changes_temp=Total Damage: Player [!pre_player_health! -> !post_player_health!]"
        )
    )
)
if !artifact_change! neq 0 (
    if defined stat_changes_temp (
        set "stat_changes_temp=!stat_changes_temp!, Artifacts !artifact_change!"
    ) else (
        set "stat_changes_temp=Artifacts !artifact_change!"
    )
)
if !potion_change! neq 0 (
    if defined stat_changes_temp (
        set "stat_changes_temp=!stat_changes_temp!, Potions !potion_change!"
    ) else (
        set "stat_changes_temp=Potions !potion_change!"
    )
)
if !charm_change! neq 0 (
    if defined stat_changes_temp (
        set "stat_changes_temp=!stat_changes_temp!, Charms !charm_change!"
    ) else (
        set "stat_changes_temp=Charms !charm_change!"
    )
)
if !key_change! neq 0 (
    if defined stat_changes_temp (
        set "stat_changes_temp=!stat_changes_temp!, Keys !key_change!"
    ) else (
        set "stat_changes_temp=Keys !key_change!"
    )
)
if !relic_change! neq 0 (
    if defined stat_changes_temp (
        set "stat_changes_temp=!stat_changes_temp!, Relics !relic_change!"
    ) else (
        set "stat_changes_temp=Relics !relic_change!"
    )
)
if !xp_change! neq 0 (
    if defined stat_changes_temp (
        set "stat_changes_temp=!stat_changes_temp!, XP +!xp_change!"
    ) else (
        set "stat_changes_temp=XP +!xp_change!"
    )
)
if defined character if "!character!" neq "" (
    if defined comp_health_change if "!comp_health_change!" neq "" (
        if defined stat_changes_temp (
            set "stat_changes_temp=!stat_changes_temp!, !comp_health_change!"
        ) else (
            set "stat_changes_temp=!comp_health_change!"
        )
    )
)
set "stat_changes=!stat_changes_temp!"

echo !character! - !result!
echo.
if defined stat_changes (
    echo Changes: !stat_changes!
    echo.
)

echo Press any key to continue...
pause >nul
goto loop

:level_check
if defined leveled_up exit /b
if !xp! geq !xp_needed! (
    set /a level+=1
    set /a max_health+=10
    set /a health+=5
    set /a levelup_health_change=5
    if !health! gtr !max_health! set /a health=!max_health!
    set /a xp-=!xp_needed!
    set /a xp_needed=!level! * 50
    if !healing_potion! lss 3 (
        set /a healing_potion+=1
        echo You've reached Level !level!^^! Max Health increased to !max_health!, Health +5, Score gains increased, and you gained a Healing Potion^^!
    ) else (
        echo You've reached Level !level!^^! Max Health increased to !max_health!, Health +5, Score gains increased^^!
    )
    echo.
    set "leveled_up=1"
)
exit /b

:characters
cls
echo --------------------------------------
echo OGENS CLAX NEXUS - D2+D3
echo --------------------------------------
echo.
echo ANCIENT COMPANIONS...
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
echo OGENS CLAX NEXUS - D2+D3
echo --------------------------------------
echo.
echo   _______
echo  /_______\
echo  ^|  ***  ^|
echo  ^|_______^| 
echo.
echo SACRED ITEMS...
echo.
echo Healing Potion (!healing_potion!): Restores vitality...
echo Score Charm (!score_charm!): Grants wisdom...
echo Artifact Key (!artifact_key!): Unlocks secrets...
echo Relic (!relics!): Doubles score gains for the next event...
echo.
echo USE AN ITEM...
echo 1. Healing Potion (+25 health)
echo 2. Score Charm (+20 score)
echo 3. Artifact Key (+4 artifacts)
echo 4. Relic (Double score next event)
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
    if !healing_potion! gtr 0 (
        set /a pre_player_health=!health!
        set /a pre_comp_health=0
        if defined character if "!character!" neq "" (
            if defined %character%_health (
                set /a pre_comp_health=!%character%_health!
            )
        )
        set /a health+=25
        set /a healing_potion-=1
        if !health! gtr !max_health! (
            set /a health=!max_health!
            set "stat_changes=Health capped at !max_health!, Potions -1"
        ) else (
            set "stat_changes=Health +25, Potions -1"
        )
        set /a post_player_health=!health!
        set /a post_comp_health=0
        if defined character if "!character!" neq "" (
            if defined %character%_health (
                set /a !character!_health+=20
                if !%character%_health! gtr 100 set /a !character!_health=100
                set /a post_comp_health=!%character%_health!
                set "stat_changes=!stat_changes!, !character!'s Health +20, Total Damage: Player [!pre_player_health! -> !post_player_health!], Companion [!pre_comp_health! -> !post_comp_health!]"
            ) else (
                set "stat_changes=!stat_changes!, Total Damage: Player [!pre_player_health! -> !post_player_health!]"
            )
        ) else (
            set "stat_changes=!stat_changes!, Total Damage: Player [!pre_player_health! -> !post_player_health!]"
        )
        echo.
        echo Healing Potion used - Vitality restored...
    ) else (
        echo.
        echo No Healing Potions remain...
        set "stat_changes=No Healing Potions remain"
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
    if !score_charm! gtr 0 (
        set /a score+=20
        set /a score_charm-=1
        set "stat_changes=Score +20, Charms -1"
        echo.
        echo Score Charm used - Wisdom gained...
    ) else (
        echo.
        echo No Score Charms remain...
        set "stat_changes=No Score Charms remain"
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
    if !artifact_key! gtr 0 (
        set /a artifacts+=4
        set /a artifact_key-=1
        set "stat_changes=Artifacts +4, Keys -1"
        echo.
        echo Artifact Key used - Secrets unlocked...
    ) else (
        echo.
        echo No Artifact Keys remain...
        set "stat_changes=No Artifact Keys remain"
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
    if !relics! gtr 0 (
        set /a relics-=1
        set "relic_active=1"
        set "stat_changes=Relic used - Score doubled for next event, Relics -1"
        echo.
        echo Relic used - Next event's score gains will be doubled...
    ) else (
        echo.
        echo No Relics remain...
        set "stat_changes=No Relics remain"
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
echo OGENS CLAX NEXUS - D2+D3
echo --------------------------------------
echo.
echo ETCHING YOUR SAGA IN STONE...
echo.
:: Initialize all variables
if not defined score set /a score=0
if not defined health set /a health=100
if not defined max_health set /a max_health=200
if not defined artifacts set /a artifacts=0
if not defined healing_potion set /a healing_potion=0
if not defined score_charm set /a score_charm=0
if not defined artifact_key set /a artifact_key=0
if not defined relics set /a relics=0
if not defined level set /a level=1
if not defined xp set /a xp=0
if not defined xp_needed set /a xp_needed=50
if not defined character set "character="
if not defined player_strength set /a player_strength=(%random% %% 10) + 5
:: Ensure companion stats are initialized
for %%a in (!companions!) do (
    if not defined %%a_health call :set_random_stats %%a
    if not defined %%a_strength call :set_random_stats %%a
    if not defined %%a_luck call :set_random_stats %%a
)
set "save_success=0"
set /a retry_count=0
:save_retry
:: Backup existing save file
if exist SaveGame.txt copy SaveGame.txt SaveGame.bak >nul
(
    echo score=!score!
    echo health=!health!
    echo max_health=!max_health!
    echo artifacts=!artifacts!
    echo healing_potion=!healing_potion!
    echo score_charm=!score_charm!
    echo artifact_key=!artifact_key!
    echo relics=!relics!
    echo level=!level!
    echo xp=!xp!
    echo xp_needed=!xp_needed!
    echo character=!character!
    echo player_strength=!player_strength!
    for %%a in (!companions!) do (
        if defined %%a_health if defined %%a_strength if defined %%a_luck (
            echo %%a_health=!%%a_health!
            echo %%a_strength=!%%a_strength!
            echo %%a_luck=!%%a_luck!
        )
    )
) >SaveGame.txt 2>nul
:: Check if retry is needed
if errorlevel 1 if !retry_count! lss 2 (
    set /a retry_count+=1
    timeout /t 1 /nobreak >nul
    goto save_retry
)
:: Verify the save file
if exist SaveGame.txt (
    for %%F in (SaveGame.txt) do if %%~zF gtr 0 (
        findstr /c:"score=" /c:"health=" /c:"max_health=" /c:"artifacts=" /c:"level=" SaveGame.txt >nul
        if not errorlevel 1 (
            set "save_success=1"
        )
    )
)
if !save_success! equ 1 (
    echo Your saga is saved!
) else (
    echo Failed to save saga... Check GameLog.txt for details.
    echo %date% %time% - Save failed: File missing or corrupted >>GameLog.txt 2>nul
)
echo.
echo Press any key to return...
pause >nul
goto loop

:load
cls
echo --------------------------------------
echo OGENS CLAX NEXUS - D2+D3
echo --------------------------------------
echo.
if not exist SaveGame.txt (
    echo No saved saga found...
    echo.
    echo Press any key to return...
    pause >nul
    goto loop
)
echo RESTORING YOUR JOURNEY...
echo.
for /f "tokens=1,2 delims==" %%a in (SaveGame.txt) do (
    set "%%a=%%b"
)
for %%a in (!companions!) do (
    if not defined %%a_health if not defined %%a_strength if not defined %%a_luck (
        call :set_random_stats %%a
    )
)
if not defined score set /a score=0
if not defined health set /a health=100
if not defined max_health set /a max_health=200
if not defined artifacts set /a artifacts=0
if not defined healing_potion set /a healing_potion=0
if not defined score_charm set /a score_charm=0
if not defined artifact_key set /a artifact_key=0
if not defined relics set /a relics=0
if not defined level set /a level=1
if not defined xp set /a xp=0
if not defined xp_needed set /a xp_needed=50
if not defined character set "character="
if not defined player_strength set /a player_strength=(%random% %% 10) + 5
echo The runes restore your journey!
echo.
echo Press any key to continue...
pause >nul
goto loop

:quit
cls
echo --------------------------------------
echo OGENS CLAX NEXUS - D2+D3
echo --------------------------------------
echo.
echo LEAVING THE LABYRINTH...
echo.
echo Final Score: !score!
echo Final Health: !health!
echo Final Artifacts: !artifacts!
echo Final Relics: !relics!
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
echo OGENS CLAX NEXUS - D2+D3
echo --------------------------------------
echo.
echo   _____
echo  /     \
echo /_______\
echo ^|  RIP ^|
echo.
echo THE LABYRINTH CLAIMS YOU...
echo.
echo Final Score: !score!
echo Final Health: !health!
echo Final Artifacts: !artifacts!
echo Final Relics: !relics!
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
echo OGENS CLAX NEXUS - D2+D3
echo --------------------------------------
echo.
echo   *****
echo   / W \
echo  / === \
echo /_______\
echo.
echo VICTORY OVER THE LABYRINTH...
echo.
echo Final Score: !score!
echo Final Health: !health!
echo Final Artifacts: !artifacts!
echo Final Relics: !relics!
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
