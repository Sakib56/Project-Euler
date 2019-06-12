# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

def EuclidPrimes(n):
    primes = [2]
    nth = 2
    num = 3
    while num <= n:
        isDiv = {True}
        for p in primes:
            if not (num % p):
                isDiv.add(False)
                break
        if all(isDiv):
            primes.append(num)
            # print("{}: {}".format(nth, num))
            nth += 1
        num += 2
    return primes

def summation(primes):
    return sum(primes)


n = 1000000
primes = EuclidPrimes(n)
print(primes)
print(summation(primes))