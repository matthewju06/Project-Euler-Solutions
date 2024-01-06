# https://projecteuler.net/problem=27
# Completed 5/16/2023

import math

def isPrime(num):
    if num >= 0:
        for i in range(2, math.floor(math.sqrt(num)) + 1):
            if (num % i) == 0:
                return False
        return True
    return False

largestCoef = 0
longestN = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while(isPrime(pow(n, 2) + a*n + b)):
            n+=1
        if(n > longestN):
            longestN = n
            largestCoef = a * b

print(largestCoef)