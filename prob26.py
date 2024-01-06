# https://projecteuler.net/problem=26
# Completed 1/4/2024

def fracToDec(den):
    res = ""
    mp = {}
    rem = 1 % num
 
    # Keep finding remainder until either
    # remainder becomes 0 or repeats
    while ((rem != 0) and (rem not in mp)):
 
        # Store this remainder
        mp[rem] = len(res)
 
        # Multiply remainder with 10
        rem = rem * 10
 
        # Append rem / denr to result
        res_part = rem // num
        res += str(res_part)
 
        # Update remainder
        rem = rem % num
 
    if (rem == 0):
        return 0
    else:
        return res[mp[rem]:]

largest = 0
largestNum = 0

for num in range (2,1000):
    if len(str(fracToDec(num))) > largest:
        largest = len(str(fracToDec(num)))
        largestNum = num

print(largestNum)