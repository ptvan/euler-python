# Project Euler problem 023
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n
# and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed
# as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import numpy as np

def divisors(n):
    divs = set(x for tup in ([i, n // i]
                             for i in range(1, int(n ** 0.5) + 1) if n % i == 0) for x in tup)
    divs.discard(n)
    return divs

abundant = []
limit = 28123
for i in range(1, limit+1):
    if sum(divisors(i)) > i:
        abundant.append(i)

length = len(abundant)

sums = np.empty([length, length], dtype=int)

for i in range(0, length):
    for j in range(0, length):
        sums[i, j] = abundant[i] + abundant[j]

sums = np.unique(sums)
sums = sums[sums <= limit]

print(sum(list(range(1,limit+1))) - sum(sums))
