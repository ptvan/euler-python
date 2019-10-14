# Project Euler problem 005
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from functools import reduce
from math import gcd

# first we create a function to calculate the least common multiple of 2 numbers
# using the known relationship between lcm and greatest common divisor
def lcm(a, b):
    return a*b // gcd(a,b)

# then again noting from the lcm definition, lcm(a, b, c) == lcm(lcm(a,b),c)
# we use reduce
print(reduce(lcm, range(1,20+1)))




