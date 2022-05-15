# https://projecteuler.net/problem=34
# Completed 5/12/2022

import math

totalSum = 0
for num in range(3,99999):
    sum = 0
    # Converting to string to traverse num
    string = str(num)
    for dig in string:
        sum += math.factorial(int(dig))
    if sum == num:
        totalSum += num

print(totalSum)