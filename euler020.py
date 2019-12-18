# Project Euler problem 020
# Find the sum of the digits in the number 100!

# unlike R, Python readily handles large integers
# so this is trivial with built-in math functions and list comprehension

import math

fact = math.factorial(100)
print(sum([int(i) for i in str(fact)]))

