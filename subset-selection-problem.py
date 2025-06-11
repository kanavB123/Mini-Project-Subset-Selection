import random

numbers = [-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4]

subset_size = 5
max_attempts = 10000
found_sets = set()

attempts = 0
while attempts < max_attempts:
    sample = tuple(sorted(random.sample(numbers, subset_size)))
    if sum(sample) == 0:
        found_sets.add(sample)
    attempts += 1

result = list(found_sets)

print(f"Total subsets found: {len(result)}")
for r in result[:5]:
    print(r)
