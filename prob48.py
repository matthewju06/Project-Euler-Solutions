# https://projecteuler.net/problem=48
# Completed 3/29/2022

num = 0

# Adding to the series
current = 1
while(current <= 1000):
    num += current ** current
    current += 1

# Converting final integer to string to use substring and get last 10 digits
print(str(num)[len(str(num)) - 10 : len(str(num))])