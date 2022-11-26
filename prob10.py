# https://projecteuler.net/problem=10
# Completed 12/31/2021

import math

def is_prime(num):
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

sum = 0
for i in range(2, 2000000):
  if is_prime(i):
    sum += i
    
print(sum)

