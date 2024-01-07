# https://projecteuler.net/problem=39
# Completed 1/6/2024

import math
#a^2 + b^2 = c^2
max = 0
highP = 0

for p in range (1000):
    count = 0
    for c in range(3,math.ceil(p/2)):
        for a in range(math.ceil(c/2),c):
            b = p - c - a
            if a ** 2 + b ** 2 == c ** 2:
                count += 1
    if count > max:
        max = count
        highP = p

print(highP)