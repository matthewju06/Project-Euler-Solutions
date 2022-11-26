# https://projecteuler.net/problem=22
# Completed 3/28/2022

import math

def isAbundant(num):
    divSum = 0
    for i in range(1, math.floor(num/2)+1):
        if num % i == 0:
            divSum += i
    if divSum > num:
        return True
    return False

def lessThan28124(num):
    return num < 28124

abundants = list(filter(isAbundant, range(28124)))
abundantSums = []
sum = 0;

for i in abundants:
    for j in abundants:
        abundantSums.append(i + j)

abundantSums.sort()
abundantSums = list(dict.fromkeys(abundantSums))
abundantSums = list(filter(lessThan28124, abundantSums))

for i in range(28124):
    if i not in abundantSums:
        sum += i

print(sum)