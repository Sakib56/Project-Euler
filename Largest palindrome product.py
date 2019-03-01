#A palindromic number reads the same both ways. The largest palindrome made from the product
#  of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from operator import itemgetter

def isPalindrome(n):
    stringNum = str(n)
    return stringNum == stringNum[::-1]

# Max 3 digit num with 11 as factor is 11*floor(999/11) -> 11*90
# Min 3 digit num with 11 as factor is 11*ceil(100/11) -> 11*10

def find3Palindrome():
    threeDigitPalindromic = []
    for i in range(90,10,-1):
        for j in range(999,100,-1):
            num1 = 11*i
            num2 = j
            product = num1 * num2
            if isPalindrome(product):
                threeDigitPalindromic.append((num1,num2,product))
    return sorted(threeDigitPalindromic, key=itemgetter(2), reverse=True)

def main():
    palindromic = find3Palindrome()
    for i in range(10):
        print("{0} * {1} = {2}".format(palindromic[i][0], palindromic[i][1], palindromic[i][2]))
    
main()
