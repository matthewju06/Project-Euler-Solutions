# https://projecteuler.net/problem=9
# Completed 12/29/2021

import math

found = False
c = 333
while not found:
  for b in range(math.ceil(c/2),c):
    for a in range(math.ceil(b/2),b):
      if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
        print(a * b * c)
        found = True
  c += 1