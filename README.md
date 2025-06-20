# No-Vig EV Betting Calculator

This script is a command-line tool designed to help sports bettors evaluate the **expected value (EV)** of bets across different bookmakers using **fair odds** derived from a no-vig (zero-margin) probability model. It supports both **2-way** and **3-way** markets and identifies +EV opportunities.

---

## Features

- Supports 2-way and 3-way betting markets (e.g., win/loss, win/draw/loss)
- Calculates **no-vig probabilities** from best available market odds
- Computes **expected value (EV)** of bets from various bookmakers
- Highlights +EV bets to identify potentially profitable opportunities

---

## How It Works

1. **Market Type Selection**  
   The user selects whether the betting market is a 2-way or 3-way market.

2. **Input Fair Odds**  
   The user inputs the best available odds from any bookmaker for each possible outcome.  
   These odds are used to calculate **fair probabilities** by removing the bookmaker margin using the `no_vig_probs()` function.

3. **Input Bookmaker Odds**  
   The user enters odds from various bookmakers for each outcome.  
   The script compares these to the fair probabilities to compute the **expected value** for each bet using the `expected_value()` function.

4. **Result Output**  
   The script outputs a summary indicating which outcomes and bookmakers offer +EV opportunities.

---

## Functions

### `no_vig_probs(odds)`

Calculates implied probabilities from odds and normalizes them to remove the bookmaker's vig (margin).

```python
def no_vig_probs(odds):
    invs = [1 / o for o in odds]
    total = sum(invs)
    return [inv / total for inv in invs]
```

### `expected_value(prob, odds)`

Calculates the expected value (EV) of a bet based on the fair win probability and the bookmaker’s offered odds.

```python
def expected_value(prob, odds):
    return (prob * (odds - 1)) - (1 - prob)
```

---

## Usage

Run the script in a terminal:

```bash
python betting_ev_calculator.py
```

Example flow:
- Choose 2-way or 3-way market
- Enter the best available odds (used to calculate fair probabilities)
- Enter odds from individual bookmakers
- Review results showing +EV opportunities

---

## Notes

- The script assumes **decimal odds** format.
- Input validation is basic; all odds should be positive floats.
- This is a command-line interface tool and does not save input or output data.

---

## License

This project is licensed under the MIT License. Use at your own discretion.
