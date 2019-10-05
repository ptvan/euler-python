# Project Euler problem 001:
# Find the sum of all the multiples of 3 or 5 below 1000.

# We use list comprehension to make things more Pythonic
ans = [x for x in range(1000) if (x % 3 == 0 or x % 5 == 0)]

print(sum(ans))
