# Project Euler problem 010
# Find the sum of all the primes below two million.
import numpy as np


def primes(n):
    vec = np.array(list(range(2, n)))
    i = 1
    while vec[i] <= int(np.ceil(np.sqrt(n))):
        vec = vec[np.logical_or(vec % vec[i] != 0, vec == vec[i])]
        i = i + 1
    return vec


print(primes(int(2e6)))


