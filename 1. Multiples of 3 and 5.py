# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

# Solution: 233168

import time

def sumMultiples(multiples):
    return sum(multiples)

def getMultiples(multipleX, multipleY, belowN):
    return [n for n in range(belowN) if not (n % multipleX and n % multipleY)]

def main():
    start = time.time()
    x = sumMultiples(getMultiples(3, 5, 1000))
    end = time.time()
    print("runtime: {0}s\nsolution: {1}".format(end-start, x))

if __name__ == '__main__':
    main()
