# https://projecteuler.net/problem=15
# Completed 1/30/2022

array = []

for i in range(21):
    array.append([])
    for j in range(21):
        if i == 20 or j == 20:
            array[i].append(1)
        else:
            array[i].append(None)

array[20][20] = 0

for i in range(19, -1, -1):
    for j in range(19, -1, -1):
        array[i][j] = array[i+1][j] + array[i][j+1]

print(array[0][0])