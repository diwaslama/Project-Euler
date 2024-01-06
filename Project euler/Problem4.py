#  Largest Palindrome Product
#  Find the largest palindrome made from the product of two 3-digit numbers.

def check_palindrome(num):
    return str(num) == str(num)[::-1]

def largest_palindrome_product():
    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if check_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome

answer = largest_palindrome_product()
print(answer)