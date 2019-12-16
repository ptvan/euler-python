# Project Euler problem 020
# Find the sum of the digits in the number 100!

# this is trivial with built-in math functions and list comprehension
# unlike R, Python readily handles large integers

import math

fact = math.factorial(100)
print(sum([int(i) for i in str(fact)]))

