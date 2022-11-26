sum = 0

for num in range(1,100000000):
    temp = 0
    for letter in str(num):
        temp += int(letter) ** 5
    
    if temp == num:
        sum += num
        
print(sum)