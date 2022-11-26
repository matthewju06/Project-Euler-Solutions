# https://projecteuler.net/problem=21
# Completed 2/12/2022

import math

def sumDivisors(num):
  divSum = 0
  for i in range(1, math.floor(num/2)+1):
    if num % i == 0:
      divSum += i
  return divSum

sum = 0

for a in range(1, 10000):
  b = sumDivisors(a)
  if a != b and a == sumDivisors(b):
    sum += a
    
print(sum)