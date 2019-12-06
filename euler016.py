# Project Euler problem 016
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

# unlike R, Python handles large integers transparently, so this is trivial

print(sum(int(digit) for digit in str(2**1000)))