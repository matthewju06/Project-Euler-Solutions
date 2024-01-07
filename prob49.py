# https://projecteuler.net/problem=49
# Completed 1/7/2024

import math

def isPermutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

current = 1001
while current < 10000:
    if isPrime(current):
        for increment in range(1,math.ceil((10000-1001)/2)):
            if isPermutation(current, current + increment) and isPrime(current + increment) and isPermutation(current, current + 2 * increment) and isPrime(current + 2 * increment):
                print(str(current) + str(current + increment) + str(current + 2 * increment))
    current += 2