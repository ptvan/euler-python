# Project Euler problem 003
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import numpy as np
import math
num = 600851475143

def primes(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

p = primes(int(num**0.5))

vec = [1]
for i in range(1, len(p)):
    # print(i)
    if (num % i == 0 and i > 1 ):
        if ((np.prod(vec) * i) <= num): 
            vec.append(i)
        
print(np.max(vec))