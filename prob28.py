# https://projecteuler.net/problem=28
# Completed 5/15/2022

# 0 = up, 1 = right, 2 = down, 3 = left
turn = 1
array = []
x = 500
y = 500

# Creating 1001x1001 2d array
for i in range(1001):
    array.append([])
    for j in range(1001):
        array[i].append("")

# Adding numbers 1-1002001 clockwise
for num in range(1,1002002):
    array[y][x] = num
    if turn == 0:
        if array[y][x+1] == "":
            x += 1
            turn = 1
        else:
            y -= 1
    elif turn == 1:
        if array[y+1][x] == "":
            y += 1
            turn = 2
        else:
            x += 1
    elif turn == 2:
        if array[y][x-1] == "":
            x -= 1
            turn = 3
        else:
            y += 1
    elif turn == 3:
        if array[y-1][x] == "":
            y -= 1
            turn = 0
        else:
            x -= 1

sum = 0
x = 0
y = 0

# Sum of numbers from top left to bottom right diagonal
while x < 1001:
    sum += array[y][x]
    x += 1
    y += 1

x = 1000
y = 0

# Sum of numbers from top right to bottom left diagonal
while x >= 0:
    sum += array[y][x]
    x -= 1
    y += 1
    
print(sum-1)