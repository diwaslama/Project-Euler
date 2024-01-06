# Largest Prime Factor
#  Find the largets prime factor of: 600851475143

def largest_prime_factor(n):
    a = 1

    while n % 2 == 0:
        a = 2
        n //= 2

    p = 3
    while n != 1:
        while n % p == 0:
            a = p
            n //= p
        p += 2

    return a

answer = largest_prime_factor(600851475143)
print(answer)