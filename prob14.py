# https://projecteuler.net/problem=14
# Completed 1/4/2022

largest = 0
largestCount = 0

for i in range(1, 1_000_000):
    sequenceNum = i
    count = 0
    while sequenceNum != 1:
        if sequenceNum % 2 == 0:
            sequenceNum /= 2
        else:
            sequenceNum = sequenceNum * 3 + 1
        count += 1
    if count > largestCount:
        largestCount = count
        largest = i
        
print(largest)