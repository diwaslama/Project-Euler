# Even Fibonacci Numbers
# By considering the terms in the Fibonacci sequence 
# whose values do not exceed four million,
# find the sum of the even-valued terms

def sum_of_even_fibonacci(limit):
    a = 1
    b = 2
    total_sum = 0

    while b <= limit:
        if b % 2 == 0:
            total_sum += b
        a, b = b, a + b

    return total_sum

answer = sum_of_even_fibonacci(4000000)
print(answer)