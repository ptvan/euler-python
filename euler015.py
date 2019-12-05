# Project Euler problem 015
# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Recognize that all paths have 40 steps, and we're trying to find all
# possible combinations of 20-step paths. This is a binomial coefficient

# only one is necessary...
import math
import scipy.special

print(int(math.factorial(40) / ((math.factorial(20)*(math.factorial(40-20))))))
print(int(scipy.special.binom(40,20)))