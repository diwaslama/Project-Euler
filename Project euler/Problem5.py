# Smallest Multiple
# Fidn the  the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?

import math

# Prime factors needed: 2, 3, 5, 7, 11, 13, 17, 19
# Calculate the max power of each prime factor within the range 1-20

power_2 = math.floor(math.log(20, 2))
power_3 = math.floor(math.log(20, 3))

answer = (2 ** power_2) * (3 ** power_3) * 5 * 7 * 11 * 13 * 17 * 19

print(answer)
