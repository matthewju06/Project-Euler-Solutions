# https://projecteuler.net/problem=12
# Completed 1/2/2022

import math

def factorCount(num):
  factors = 0
  for i in range(1, math.ceil(math.sqrt(num))):
    if num % i == 0:
      factors += 2
  return factors

currentTriNum = 1
count = 1
found = False

while found == False:
  if factorCount(currentTriNum) > 500:
    print(currentTriNum)
    found = True
    break
  count += 1
  currentTriNum += count