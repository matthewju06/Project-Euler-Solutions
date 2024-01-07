# https://projecteuler.net/problem=37
# Completed 1/6/2024

import math

def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2,math.ceil(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

sum = 0
count = 0
current = 11
while count < 11:
    currentStr = str(current)
    lenCurrent = len(currentStr)
    primeTF = True
    for i in range(lenCurrent):
        if not isPrime(int(currentStr[:i+1])) or not isPrime(int(currentStr[i:])):
            primeTF = False
    if primeTF:
        sum += current
        count += 1
    current += 1

print(sum)