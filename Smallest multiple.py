# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def productFrom(n,m):
    product = 1
    for i in range(n,m):
        product *= i
    return product

def isDivBy(n,d):
    return n%d == 0

def isDivFrom(n,d):
    divs = {True}
    for i in range(2,d,):
        if isDivBy(n,i):
            divs.add(True)
        else:
            divs.add(False)
    return all(divs)


def main():
    #for i in range(1,productFrom(2,10)): 
    numsDivByFirstN = []
    for i in range(1,productFrom(2,10)):
        if isDivFrom(i,10):
            numsDivByFirstN.append(i)
    print(numsDivByFirstN[0])

main()