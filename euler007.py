# Project Euler problem 007
# What is the 10 001st prime number?

import numpy as np

# re-using our function for calculating primes from euler003.py
def primes(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

# using the known property of prime number's upper bound:
# n(ln(n) + ln(ln(n))) > p > n(ln(n) + ln(ln(n−1)))
# we only need to calculate up to n(ln(n) + ln(ln(n)))

ceil = int(np.ceil(n * (np.log(n) + np.log(np.log(n)))))

nums = primes(ceil)

nums[10001]


