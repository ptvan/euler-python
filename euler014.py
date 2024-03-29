# Project Euler problem 014
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
#   13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

# this version saved the chains so we don't have to grow a list dynamically

has2 = {}


def collatz(n):
    seq = []
    seq.append(n)
    tmp = n

    while tmp > 1:
        if tmp % 2 == 0:
            tmp = int(tmp / 2)
            if tmp in has2:
                seq += has2[tmp]
                break
            else:
                seq.append(tmp)
        else:
            tmp = 3 * tmp + 1
            if tmp in has2:
                seq += has2[tmp]
                break
            else:
                seq.append(tmp)

    has2[n] = seq
    return len(seq)


num = 0
biggest = 0
for i in range(1000000):
    c = collatz(i)
    if num < c:
        num = c
        biggest = i

print(biggest, "has", num, "elements")
