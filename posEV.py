def no_vig_probs(odds):
    invs = [1 / o for o in odds]
    total = sum(invs)
    return [inv / total for inv in invs]

def expected_value(prob, odds):
    return (prob * (odds - 1)) - (1 - prob)

# Choose market type
while True:
    market_type = input("Is this a 2-way or 3-way market? (enter 2 or 3): ").strip()
    if market_type in ['2', '3']:
        market_type = int(market_type)
        break
    else:
        print("Please enter 2 or 3.")

labels = ['Outcome 1', 'Outcome 2'] if market_type == 2 else ['Team 1 Win', 'Draw', 'Team 2 Win']

# Input fair odds from best available market (for no-vig calc)
print("\nEnter the best odds from any bookie for each outcome:")
fair_odds = []
for label in labels:
    fair_odds.append(float(input(f"  {label} odds: ")))

fair_probs = no_vig_probs(fair_odds)
print("\nFair Probabilities:")
for label, prob in zip(labels, fair_probs):
    print(f"  {label}: {prob:.2%}")

# Bookie inputs
print("\nNow enter odds from each bookie (type 'done' to finish):")
bookies = {}

while True:
    name = input("\nBookie name (or 'done'): ")
    if name.lower() == 'done':
        break

    odds = []
    for label in labels:
        val = input(f"  {label} odds: ").strip()
        try:
            odds.append(float(val))
        except:
            print("Invalid number. Try again.")
            break
    else:
        if len(odds) == market_type:
            bookies[name] = odds

# Calculate EVs
print("\n🔍 +EV Opportunities:\n")
for bookie, odds in bookies.items():
    evs = [expected_value(p, o) for p, o in zip(fair_probs, odds)]
    if any(ev > 0 for ev in evs):
        print(f"✅ {bookie}:")
        for i, ev in enumerate(evs):
            if ev > 0:
                print(f"  {labels[i]} @ {odds[i]:.2f} (EV: {ev:.2%})")
    else:
        print(f"❌ {bookie}: No +EV bets.")
