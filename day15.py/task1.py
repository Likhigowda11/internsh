actions = ["Click", "Scroll", "Exit"]

sample_space = []

for first_action in actions:
    for second_action in actions:
        sample_space.append((first_action, second_action))

print("Sample Space (S):")
print(sample_space)
print("Total Outcomes in Sample Space:", len(sample_space))

event_at_least_one_click = []

for outcome in sample_space:
    if "Click" in outcome:
        event_at_least_one_click.append(outcome)

print("\nOutcomes with at least one Click:")
print(event_at_least_one_click)

probability_click = len(event_at_least_one_click) / len(sample_space)

print("\nProbability of at least one Click:", probability_click)

import random

num_trials = 1000
count_sum_7 = 0

for i in range(num_trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    if total == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / num_trials

print("\nExperimental Probability of sum = 7:", experimental_probability)

total_possible = 36
favorable = 6

theoretical_probability = favorable / total_possible

print("Theoretical Probability of sum = 7:", theoretical_probability)