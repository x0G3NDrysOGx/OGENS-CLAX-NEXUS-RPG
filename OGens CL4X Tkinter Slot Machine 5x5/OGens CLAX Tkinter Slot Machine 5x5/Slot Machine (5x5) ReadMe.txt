# Slot Machine Game README (5x5 Version)

## Overview
This is an advanced Python-based slot machine game with a 5x5 grid, featuring 15 paylines, a variety of symbols, and engaging mechanics such as regular spins, free spins, a jackpot, extra credits, and an in-game store. Built using `tkinter` for the GUI and `secrets` for true randomness, the game offers an immersive experience with persistent player data, a leaderboard, and customizable bets. Players can win coins and credits, track stats, and purchase items to enhance gameplay.

## Game Features

### Game Setup
- **Grid**: 5 reels × 5 rows, displaying 25 symbols per spin.
- **Symbols**: 🍒 (Cherry), 🔔 (Bell), 🍋 (Lemon), 7️⃣ (Seven), ⭐ (Star), 💎 (Diamond, also the wild symbol), 🍉 (Watermelon), 🍊 (Orange).
- **Paylines**: 15 predefined paylines (horizontal, vertical, and diagonal) checked for wins.
- **Currency**: 
  - **Coins**: Used for betting and added to the balance when won.
  - **Credits**: Earned from winning paylines and used to purchase items in the store.
- **Persistence**: Player data (balance, jackpot, stats, extra spins, credits) is saved to `slot_machine_save.json`. Leaderboard data is saved to `leaderboard.json`.
- **Randomness**: Uses `secrets` module for cryptographically secure random symbol selection and credit generation.

### Betting and Spinning
- **Bet Adjustment**: Players set bets (1–100 coins) via a text entry or +/- buttons, limited by their balance. The bet can be adjusted without spinning.
- **Regular Spins**: Deduct the bet amount from the balance (unless using an extra spin) and increment the jackpot by 1 coin per bet (`JACKPOT_INCREMENT = 1`).
- **Extra Spins**: Can be used instead of regular spins, costing no coins but not contributing to the jackpot. Purchased via the store or earned through gameplay.
- **Free Spins**: Triggered by five 💎 symbols in the middle row or by purchasing from the store, granting 5 free spins (`FREE_SPINS = 5`). Free spins use the current bet for payouts but do not deduct from the balance.

### Payline Wins
When a payline is hit (i.e., all symbols in a payline are the same or include the wild symbol 💎), the payout is calculated as:  
**Payout = Bet × Multiplier** for the matching symbol.  
The multipliers are defined in the `PAYOUTS` dictionary:  
- 🍒: 2x  
- 🔔: 5x  
- 🍋: 3x  
- 7️⃣: 10x  
- ⭐: 7x  
- 💎: 15x  
- 🍉: 4x  
- 🍊: 3x  

**Example**: If your bet is 10 coins and you hit a payline with 🍒 symbols, you win `10 × 2 = 20 coins` for that payline.  

Multiple paylines can contribute to the total payout if multiple winning combinations are hit in a single spin. This applies to both **regular spins** and **free spins**.

### Extra Credits
For each winning payline, you also receive **random extra credits** (between 1 and 100, generated using `secrets.randbelow(100) + 1`).  
These credits are added to your total credits, which can be used to purchase items in the store (e.g., extra spins, balance boosts).

**Example**: If you hit two paylines in a single spin (e.g., one 🍒 and one ⭐), you might earn 20 coins (🍒: 10 × 2) + 70 coins (⭐: 10 × 7) = 90 coins, plus, for example, 50 credits for the 🍒 payline and 30 credits for the ⭐ payline, totaling 80 credits.

### Free Spins Mode
- **Trigger**: Activated by five 💎 symbols in the middle row (checked via `check_bonus`) or by purchasing "Free Spins Purchase" from the store.
- **Mechanics**: Grants 5 free spins, using the current bet (set before triggering) to calculate payouts. No coins are deducted from the balance.
- **Winnings**: Payouts from paylines and extra credits (1–100 per winning payline) accumulate over the 5 spins. Total coins are added to the balance, and credits are added to the credit balance at the end.
- **Stats**: Each free spin increments the `spins` stat. Winning paylines increment the `wins` stat and add to `total_won` (payouts + extra credits). The `total_bet` stat is not incremented.
- **Limitations**: No additional free spins or jackpot checks occur during free spins.

### Jackpot
- **Base Value**: Starts at 1000 coins (`JACKPOT_BASE = 1000`).
- **Increment**: Increases by 1 coin per bet in regular spins (`JACKPOT_INCREMENT = 1`).
- **Win Condition**: 1-in-1000 chance (`secrets.randbelow(1000) == 0`) for bets of 1–100 coins during regular spins (not free spins or extra spins).
- **Payout**: Awards the entire jackpot, which resets to 1000 coins after a win. The balance is updated, and the win is recorded in stats and the leaderboard.
- **Visuals**: Winning the jackpot highlights all reel symbols in gold.

### In-Game Store
Players can spend credits to purchase items, enhancing gameplay:
- **Extra Spin** (50 credits): Adds 1 extra spin, usable without deducting coins.
- **Balance Boost** (100 credits): Adds 100 coins to the balance.
- **Jackpot Boost** (200 credits): Increases the jackpot by 500 coins.
- **Free Spins Purchase** (250 credits): Triggers 5 free spins immediately.
- **Mechanics**: Select an item from the store listbox and click "Buy Item." The purchase deducts credits and applies the effect. Insufficient credits trigger an error message.

### Stats and Leaderboard
- **Stats Tracking**:
  - **Spins**: Incremented for each regular, extra, or free spin.
  - **Wins**: Incremented for spins with at least one winning payline or a jackpot win.
  - **Total Won**: Sum of all coins and credits won from paylines and jackpots.
  - **Total Bet**: Sum of coins bet in regular spins (not extra or free spins).
  - **Win Rate**: Calculated as `(wins / spins) × 100` (0% if no spins).
- **Leaderboard**: Stores the top 5 high scores (balance) with player names in `leaderboard.json`. Updated on game quit or when the balance reaches zero (game over).
- **Display**: Stats are shown in the GUI, and the leaderboard is accessible via a button, displayed in a pop-up.

### Game Interface
- **GUI**: Built with `tkinter`, featuring a 5x5 grid of reel labels, balance/credits/jackpot/bet/extra spins displays, a bet adjustment entry/buttons, a store listbox, payline/status displays, and buttons for Spin, Quit, Leaderboard, and Reset. The window size is 700x500 pixels.
- **Visual Feedback**:
  - Spins animate with cycling symbols for 10 iterations (100ms delay).
  - Winning paylines highlight in light green; jackpots highlight in gold.
  - Status messages indicate wins (green), losses (red), free spins (blue), or jackpots (purple).
- **Player Name**: Prompted at game start (defaults to "Player" if empty).

### Game Flow
- **Start**: Load saved data or start with 100 coins, 1000-coin jackpot, 0 extra spins, 0 credits, and zeroed stats.
- **Spin**:
  - Regular spins deduct the bet and check for paylines, jackpot, or free spins.
  - Extra spins (if available) deduct no coins.
  - Free spins trigger on five 💎 symbols or store purchase, running 5 spins.
- **Game Over**: Triggered when balance and extra spins reach zero, showing the leaderboard and final stats before quitting.
- **Quit**: Saves balance and leaderboard, showing final stats and leaderboard.
- **Reset**: Deletes save files, resetting balance to 100, jackpot to 1000, and stats/spins/credits to 0.

### Technical Details
- **Dependencies**: `tkinter`, `colorama`, `json`, `os`, `secrets`, `time`.
- **Files**:
  - `slot_machine_save.json`: Stores balance, jackpot, stats, extra spins, credits.
  - `leaderboard.json`: Stores top 5 high scores.
- **Error Handling**: Catches JSON/IO errors for loading/saving, `tkinter` setup issues, and invalid bet inputs (must be 1–100 and not exceed balance).
- **Randomness**: Uses `secrets` for secure random symbol selection, credit generation, and jackpot checks.

## Example Scenario
- **Setup**: Bet set to 10 coins, balance at 100 coins, 0 credits.
- **Regular Spin**:
  - Deducts 10 coins (balance: 90).
  - Hits two paylines (🍒: 10 × 2 = 20 coins, ⭐: 10 × 7 = 70 coins) and earns 50 + 30 = 80 credits.
  - Total: 90 coins + 80 credits added (balance: 180, credits: 80).
  - Jackpot increases by 1 (to 1001).
- **Free Spins** (triggered by five 💎):
  - 5 spins, each checking paylines with 10-coin bet.
  - Spin 1: Hits 🍒 payline (20 coins, 50 credits). Total so far: 20 coins, 50 credits.
  - Spin 2–5: No wins. Final: 20 coins added to balance (now 200), 50 credits added (now 130).
- **Store Purchase**: Spend 100 credits on Balance Boost, adding 100 coins (balance: 300, credits: 30).

This README provides a complete overview of the 5x5 slot machine game, covering payouts, extra credits, and all mechanics for both regular and free spins, ensuring players understand how to play and what to expect from wins.