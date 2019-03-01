# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

# Solution: 233168

def sumMulti(multiples):
    sum = 0
    for n in multiples:
        sum += n
    return sum

def getMulti(multiple_x, multiple_y, below_N):
    multiples = []
    for n in range(below_N):
        if not (n % multiple_x and n % multiple_y):
            multiples.append(n)
    return multiples

def main():
    m = getMulti(3, 5, 1000)
    s = sumMulti(m)
    print(s)

main()
