# https://projecteuler.net/problem=30
# Completed 9/8/2023

sum = 0

for num in range(2,1000000):
    tempSum = 0
    for digit in str(num):
        tempSum += int(digit) ** 5
    if num == tempSum:
        sum += tempSum
print(sum)