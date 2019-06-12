# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Product from n to m 
def productFrom(n,m):
    product = 1
    for i in range(n,m):
        product *= i
    return product

# Checks if n is divisable by d
def isDivBy(n,d):
    return n%d == 0

# Checks if n is div by 1,2,...,d
def isDivFrom(n,d):
    divs = {True}
    for i in range(2,d+1):
        if isDivBy(n,i):
            divs.add(True)
        else:
            divs.add(False)
    return all(divs)


def main():
    i = 0
    while True:
    #for i in range(0,int(productFrom(1,10)/2),8):
        if isDivFrom(i,10) and i>0:
            print(i)
            break
        i += 10

# ANS: 232792560
main()