# Project Euler problem 025 :
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


import numpy as np

# brute force since modern computers are fast:
a = 1
b = 1
c = a + b
n = 2

while len(str(c)) < 1000:
    n = n + 1
    c = a + b
    a = b
    b = c

print(n)

# More elegantly, we note that Fibonacci sequence converges via Binet's formula
# (https://en.wikipedia.org/wiki/Fibonacci_number#Relation_to_the_golden_ratio)
# specifically phi^n / sqrt(5) where phi ~ 1.6180
# since we want 1000 digits, set (phi^n / sqrt(5)) = 999 and solve
phi = 1.6180
n = int(np.floor((np.log(10)*999 + np.log(5)/2)/np.log(phi)))
print(n)