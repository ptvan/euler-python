# Project Euler problem 024
# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# brute force version using itertools
import numpy as np
from itertools import permutations

digit = ''.join(list(permutations('0123456789', 10))[999999])
print(digit)


# smarter version ported from euler024.R

def lex(seq, n):
    seq = np.array(seq)
    n = int(n)
    length = len(seq)
    vec = np.zeros(length, dtype="int")
    for i in range(0, length-1):
        if n == 0:
            vec[i] = seq[len(seq)-1]
        else:
            tmp = np.prod(range(1, length - i))
            div = int((n-1) / tmp)
            vec[i] = seq[div]
            n = n % tmp
            seq = seq[seq != vec[i]]

    return vec

lex(range(0,10),1e6)