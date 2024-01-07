# https://projecteuler.net/problem=44
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

def pentagonal(i):
    return i*(3*i -1)/2

current = 2
found = False
while found == False:
    for i in range(current - 1, 0, -1):
        if isPentagonal(pentagonal(current) - pentagonal(i)) and isPentagonal(pentagonal(current) + pentagonal(i)):
            print(pentagonal(current) - pentagonal(i))
            found = True
    current += 1