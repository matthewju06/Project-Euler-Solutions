# https://projecteuler.net/problem=6
# Completed 12/24/2021

sumofsquares = 0;
for i in range(1, 101):
  sumofsquares += i ** 2 

squareofsums = 5050 ** 2

print(squareofsums - sumofsquares)