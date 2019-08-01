# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

# Solution: 233168

def sumMultiples(multiples):
    sum = 0
    for n in multiples:
        sum += n
    return sum

def getMultiples(multipleX, multipleY, belowN):
    multiples = [n for n in range(belowN) if not (n % multipleX and n % multipleY)]
    return multiples

def main():
    m = getMultiples(3, 5, 1000)
    s = sumMultiples(m)
    print(s)

main()
