# https://projecteuler.net/problem=29
# Completed 5/10/2022

arr = []

# Adding a^b for range 2<=a<=100, 2<=b<=100
for a in range(2,101):
    for b in range(2,101):
        arr.append(a ** b)

# Filtering list of duplicates
filteredArr = list(dict.fromkeys(arr))
print(len(filteredArr))