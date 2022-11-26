# https://projecteuler.net/problem=17
# Completed 1/19/2022

count = 0

singles = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

for i in range(1, 1000):
  
  if i > 99:
    count += len(singles[int(str(i)[0])]) + len("hundred")
    if int(str(i)[1:3]) == 0:
      continue
    elif int(str(i)[1:3]) < 20:
      count += len("and") + len(singles[int(str(i)[1:3])])
    else:
      count += len("and") + len(tens[int(str(i)[1])]) + len(singles[int(str(i)[2])])
  
  else:
    if i < 20:
      count += len(singles[i])
    else:
      count += len(tens[int(str(i)[0])]) + len(singles[int(str(i)[1])])
      
count += len("onethousand")

print(count)