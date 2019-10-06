
# Project Euler problem 002:
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

def fib(upper):
    a, b = 1,1
    total = 0
    while a < upper:
        if a % 2 == 0:
            total += a
        a, b = b, a+b
    return total

print(fib(4E6))