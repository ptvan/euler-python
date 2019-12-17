# Project Euler problem 021
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b,
# then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

# more or less a port of the euler021.R, keep using the fact that the first amicable number is 220
# using a set instead of a list since there are no duplicate numbers

import math

amicable_numbers = set()


def sum_divisors(n):
    total = 1
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            total += i
            y = n // i
            if y > i:
                total += y
    return total


for i in range(220, 10000):
    sd = sum_divisors(i)
    for j in range(i + 1, 10000):
        if sd == j and sum_divisors(j) == i:
            amicable_numbers.update([i, j])


print(sum(amicable_numbers))

