# Sum Square Difference
# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum

n = 100

# Sum of the squares of the first n natural numbers
sum_of_squares = n * (n + 1) * (2 * n + 1) / 6

# Square of the sum of the first n natural numbers
square_of_sum = (n * (n + 1) / 2) ** 2

answer = square_of_sum - sum_of_squares

print(int(answer))
