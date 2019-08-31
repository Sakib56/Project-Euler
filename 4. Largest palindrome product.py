# A palindromic number reads the same both ways. The largest palindrome made from the product
#  of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Solution: 906609

from operator import itemgetter
from time import time


def isPalindrome(n):
    stringNum = str(n)
    return stringNum == stringNum[::-1]

# Max 3 digit num has 11 as factor is 11*floor(999/11) -> 11*90
# Min 3 digit num has 11 as factor is 11*ceil(100/11) -> 11*10
# This was an observation that I made


def find3Palindrome():
    threeDigitPalindromic = []
    for i in range(90, 10, -1):
        for j in range(999, 100, -1):
            num1 = 11*i
            num2 = j
            product = num1 * num2
            if isPalindrome(product):
                # tuple (num1, num2, product) -> num1 * num2 = product
                threeDigitPalindromic.append((num1, num2, product))

    return sorted(threeDigitPalindromic, key=itemgetter(2))


def main():
    start = time()
    x = find3Palindrome()
    end = time()

    # for num1, num2, product in palindromic:
    #     print("{0} * {1} = {2}".format(num1, num2, product))

    print("runtime: {0}s\nsolution: {1}".format(end-start, x[-1]))


if __name__ == '__main__':
    main()
