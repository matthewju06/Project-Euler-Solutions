# https://projecteuler.net/problem=19
# Completed 3/20/2022

def daysInMonth():
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        return 28

count = 0;
weekday = 2

for year in range(1900, 2001):
    for month in range(1,13):
        for day in range(1, daysInMonth()+1):
            if day == 1 and weekday == 1 and year > 1900:
                count += 1
            if weekday < 7:
                weekday +=1
            else:
                weekday = 1
                
print(count)