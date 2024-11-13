import random

# Generating random scores for 100 people
scores = [random.randint(0, 100) for _ in range(100)]

# Finding the highest score and corresponding person (index)
best_score = max(scores)
best_person = scores.index(best_score) + 1  # Adding 1 to match person number

print(f"Person {best_person} scored the best with a score of {best_score}.")