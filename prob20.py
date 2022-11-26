# https://projecteuler.net/problem=20
# Completed 2/6/2022

n = 1
sum = 0

for i in range(1, 101):
  n *= i

for i in str(n):
  sum += int(i)
  
print(sum)