# https://projecteuler.net/problem=32
# Completed 

def containedOnce(single, total):
    return str(total).count(str(single)) == 1

sumArr = []

for num in range (123456789,987654321):
    status = True
    for i in range (1,10):
        if containedOnce(i, num):
            continue
        else:
            status = False
    if not status:
        continue
    
    numStr = str(num)
    for j in range(1,4):
        for k in range(1,4):
            if int(numStr[0:j]) * int(numStr[j:j+k]) == int(numStr[j+k:]):
                print(numStr[0:j] + " * " + numStr[j:j+k] + " = " + numStr[j+k:])
                if sumArr.count(numStr[j+k:]) == 0:
                    sumArr.append(numStr[j+k:])

sum = 0
for i in range(len(sumArr)):
    sum += int(sumArr[i])
print(sum)