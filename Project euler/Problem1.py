# Multiples of 3 or 5
# Find the sum of all the multiples of 3 or 5 below 1000.

total_sum = 0

for number in range(1, 1000):
    if number % 3 == 0 or number % 5 == 0:
        total_sum += number

print(total_sum)