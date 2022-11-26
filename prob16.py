# https://projecteuler.net/problem=16
# Completed 1/5/2022

num = 2 ** 1000

sum = 0
for dig in str(num):
    sum += int(dig)

print(sum)