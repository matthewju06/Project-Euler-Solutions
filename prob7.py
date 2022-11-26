# https://projecteuler.net/problem=7
# Completed 12/25/2021

def isPrime(num):
  for i in range(2,num):
    if num % i == 0:
      return False
  return True

count = 0
current = 2

while count != 10001:
    if isPrime(current):
        count += 1
    current += 1

print(current - 1)