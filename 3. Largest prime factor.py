# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Solution: 6857

from math import ceil, sqrt


def isPrime(n):
    if n == 2:
        return True
    for i in [2]+list(range(3, ceil(sqrt(n)), 2)):
        if not n % i:
            return False
    return n >= 2


def getPrimesUpto(n):
    primes = [p for p in range(1, n) if isPrime(p)]
    return primes


def largestPrimeFactor(n, primes):
    for p in reversed(primes):
        if n % p == 0:
            return p


def main():
    n = 600851475143
    primes = getPrimesUpto(n)
    print(largestPrimeFactor(n, primes))


if __name__ == '__main__':
    main()
