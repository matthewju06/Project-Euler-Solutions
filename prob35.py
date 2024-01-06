# https://projecteuler.net/problem=35
# Completed 1/6/2024
import math

def isPrime(num):
    primeTF = True
    for i in range(2,math.ceil(math.sqrt(num)+1)):
        if num % i == 0:
            primeTF = False
    return primeTF

def isCircPrime(num):
    numStr = str(num)
    primeTF = True
    for i in range(len(numStr)):
        rotatei = numStr[i:] + numStr[:i]
        if not isPrime(int(rotatei)):
            primeTF = False
    return primeTF

count = 0
for num in range(1,1000000):
    if isPrime(num) and isCircPrime(num):
        count+=1
print(count)