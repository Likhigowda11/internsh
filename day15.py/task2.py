
P_heads = 1/2
P_six = 1/6
P_heads_and_six = P_heads * P_six

print("Independent Event Probability (Heads AND 6):", P_heads_and_six)

total_marbles = 10
red_marbles = 5

P_first_red = red_marbles / total_marbles

total_marbles_after = total_marbles - 1
red_marbles_after = red_marbles - 1

P_second_red_given_first = red_marbles_after / total_marbles_after

P_both_red = P_first_red * P_second_red_given_first

print("Dependent Event Probability (Both Red):", P_both_red)

print("\nWhy did denominator change?")
print("Because total marbles reduced from 10 to 9 after first pick.")
print("The second probability depends on the first event.")

print("TASK 2: Independent vs Dependent Events\n")

print("Independent Case:")
print("P(Heads) = 1/2")
print("P(6 on die) = 1/6")
print("Since independent:")
print("P(Heads AND 6) = (1/2) × (1/6) = 1/12\n")

print("Dependent Case (Without Replacement):")
print("Bag: 5 Red, 5 Blue (Total = 10)")
print("P(First Red) = 5/10")
print("After removing one Red:")
print("Remaining Red = 4")
print("Remaining Total = 9")
print("P(Second Red | First Red) = 4/9")
print("P(Both Red) = (5/10) × (4/9) = 2/9\n")

print("Reflection:")
print("Denominator changed because total marbles reduced from 10 to 9.")
print("Second event depends on first event.\n")

print("NLP Connection:")
print("Next word probability depends on previous word.")
print('Example: P("Francisco" | "San")')