# Project Euler problem 009
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# NOTE: this is a direct port of euler-r/euler009.R
# Here we exploit the fact that a < b < c
# which in turn means a < (a + b + c) / 3
# and a < b < (a + b + c) / 2

import numpy as np

a = 0
b = 0
c = 0
s = 1000

found = False

for a in range(int(np.floor(s/3))):
    for b in range(a, int(np.floor(s/2)), 1):
        c = s - (a + b)
        if a**2 + b**2 == c**2:
            found = True
            break
    if found:
        break

print(a, "x", b, "x", c, "=", a*b*c)
