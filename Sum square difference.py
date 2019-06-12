# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first 
# 3025 - 385 = 2640

# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

def sumSquared(n):
    m = n*(n+1)/2
    return m*m

def squaredSum(n):
    squaredSum = 0
    for i in range(n+1):
        squaredSum += i*i
    return squaredSum

def main():
    n = 1000000000
    sum_squared = sumSquared(n) # (1+...+n)^2
    squared_sum = squaredSum(n) # 1^2+...+n^2
    difference = sum_squared - squared_sum
    print("The differnce between the sum of squares {} numbers is\n{} - {} = {}".format(n, sum_squared, squared_sum, difference))

main()