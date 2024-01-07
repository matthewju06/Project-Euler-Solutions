# https://projecteuler.net/problem=46
# Completed 1/7/2024

import math

def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

currentSum = 9
found = False
while not found:
    if not isPrime(currentSum):
        found = True
        for possiblePrime in range(2, currentSum - 1):
            if isPrime(possiblePrime):
                tempSum = (currentSum - possiblePrime)/2
                if (math.sqrt(tempSum)).is_integer():
                    found = False
                    break
            
        if found:
            print(currentSum)
    currentSum += 2