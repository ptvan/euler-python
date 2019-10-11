# Project Euler problem 004
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
    rev = str(num)[::-1]
    return rev == str(num)

largest = 0

for i in range(100,999):
    for j in range(100,999):
        if (is_palindrome(i*j) and i*j > largest):
            largest = i*j

print(largest)
