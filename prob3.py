# https://projecteuler.net/problem=3
# Completed 12/24/2021
import math

def isPrime(num):
  for i in range(2,num):
    if num % i == 0:
      return False
  return True

largest = 0

for i in range(1, math.ceil(math.sqrt(600851475143))):
  if 600851475143 % i == 0: #If i is a factor of 600851475143
    if isPrime(i):
      largest = i
print(largest)
    