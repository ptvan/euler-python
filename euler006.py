# Project Euler problem 006
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

seq = range(1,100)

sum_of_squares = sum(i**2 for i in seq)
square_of_sums = sum(seq)**2

print(sum_of_squares - square_of_sums)