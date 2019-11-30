# Project Euler problem 012
# What is the value of the first triangle number to have over five hundred divisors?

# here we observe that (1) N and N+1 are co-primes, which means that
# the numbers of factors of N*N+1 is just the product of N's number of factors
# and N+1's number of factors
# another case where we use mathematical properties to get at the problem
# in contrast to euler012.R's naive approach

def triangle(n):
    return int((n*(n+1))/2)


def how_many_factors(n):
    return len([x for x in range(1, int(n) + 1) if int(n) % x == 0])


for n in range(1, 1000000):
    if n % 2 == 0:
        cnt = how_many_factors(n / 2) * how_many_factors(n + 1)
    else:
        cnt = how_many_factors(n) * how_many_factors((n + 1) / 2)
    if cnt >= 500:
        print(triangle(n))
        break

