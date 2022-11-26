# https://projecteuler.net/problem=4
# Completed 12/29/2021

largest = 0

for i in range (100, 1000):
    for j in range(100, 1000):
        if i * j > largest and i * j == int(str(i * j)[::-1]):
            largest = i * j

print(largest)
    