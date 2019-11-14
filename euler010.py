# Project Euler problem 010
# Find the sum of all the primes below two million.

# a translation of euler010.R, with adaptations for Python (see notes)
import numpy as np


def primes(n):
    # note 1: python % operator works on 2 numbers
    # or a number and a numpy array, so we use the latter
    vec = np.array(list(range(2, n)))
    i = 1
    while vec[i] <= int(np.ceil(np.sqrt(n))):
        # note 2: similarly, Boolean OR does not work on a list
        # so instead we use numpy's logical_or()
        vec = vec[np.logical_or(vec % vec[i] != 0, vec == vec[i])]
        i = i + 1
    return vec


print(primes(int(2e6)))


