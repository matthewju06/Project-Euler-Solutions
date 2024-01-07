# https://projecteuler.net/problem=45
# Completed 1/7/2024

import math

def isPentagonal(i):
    discriminant = (1/2 ** 2) - (4 * 3/2 * -1*i)
    if discriminant >= 0:
        n = (1/2 - math.sqrt(discriminant)) / (2 * 3/2)
        if n > 0 and n.is_integer():
            return True
        n = (1/2 + math.sqrt(discriminant)) / (2 * 3/2)
        if n > 0 and n.is_integer():
            return True
    return False

def isHexagonal(i):
    discriminant = (1 ** 2) - (4 * 2 * -1*i)
    if discriminant >= 0:
        n = (1 - math.sqrt(discriminant)) / (2 * 2)
        if n > 0 and n.is_integer():
            return True
        n = (1 + math.sqrt(discriminant)) / (2 * 2)
        if n > 0 and n.is_integer():
            return True
    return False

def triangular(i):
    return i*(i + 1)/2

current = 286
while 1 == 1:
    if isHexagonal(triangular(current)) and isPentagonal(triangular(current)):
        print(triangular(current))
        break
    current += 1