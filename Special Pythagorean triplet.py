# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

# def getPythagoreanTriplet(GeneralFibSeq):
#     triplets = set()
#     for i in range(len(GeneralFibSeq)-3):
#         hn = GeneralFibSeq[i]
#         hn1 = GeneralFibSeq[i+1]
#         hn2 = GeneralFibSeq[i+2]
#         hn3 = GeneralFibSeq[i+3]
#         triplets.add((2*hn1*hn2,  hn*hn3,  2*hn1*hn2+hn*hn))
#     return triplets

# def fib(n,initSeq):
#     fibSeq = initSeq    
#     if n <= 1:
#         return fibSeq[:n]
#     else:
#         for i in range(2, n):
#             fibSeq.append(fibSeq[i-1]+fibSeq[i-2])
#     return fibSeq

# def verify(triplet):
#     aa = triplet[0]*triplet[0]
#     bb = triplet[1]*triplet[1]
#     cc = triplet[2]*triplet[2]
#     return aa + bb == cc

# def slowMain():
#     generatedTriplets = []
#     n = 1000
#     for i in range(9):
#         for j in range(9):
#             firstNFibs = fib(n,[i,j])
#             for trip in getPythagoreanTriplet(firstNFibs):
#                 generatedTriplets.append(trip)
#     generatedTriplets = list(set(generatedTriplets))

#     for trip in generatedTriplets:
#         a = trip[0]
#         b = trip[1]
#         c = trip[2]
#         if a+b+c == 52:
#             print(trip)

def pythagoreanSumEquals(n):
    pythagoreanSum = 0
    b = 2
    while pythagoreanSum != n:
        for a in range(1,b):
            for b in range(1,n):
                c = math.sqrt(a*a+b*b)
                if a+b+c == n:
                    pythagoreanSum = n
                    return (a, b, int(c))

def main(): 
    specialTriplet = pythagoreanSumEquals(1000)
    print(specialTriplet, specialTriplet[0]*specialTriplet[1]*specialTriplet[2])

main()