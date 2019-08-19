# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Solution: 6857

from time import time
from math import sqrt


def largestPrimeFactor(n):
    while True:
        p = smallestPrimeFactor(n)
        if p >= n:
            return n
        else:
            n = int(n/p)


def smallestPrimeFactor(n):
    for i in range(2, 1+int(sqrt(n))):
        if not n % i:
            return i
    return n

# Since every number, n has a prime factorization, we can repeatedly divide n by prime
# factors (from smallest to largest) and thus the last factor will be the largest factor


def main():
    n = 600851475143
    start = time()
    x = largestPrimeFactor(n)
    end = time()

    print("runtime: {0}s\nsolution: {1}".format(end-start, x))


if __name__ == '__main__':
    main()
