# https://projecteuler.net/problem=1
# Completed 12/29/2021

sum = 0

for num in range(1000):
  if num % 3 == 0 or num % 5 == 0:
    sum += num

print(sum)