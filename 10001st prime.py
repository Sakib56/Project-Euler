# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13. What is the 10,001st prime number?
import math

# Returns primes upto n by checking prime divisors existence
def EuclidPrimes(n):
    primes = [2]
    nth = 2
    num = 3
    while nth != n+1:
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

def main():
    primes = EuclidPrimes(10001)
    print(primes[-1])

main()