# https://projecteuler.net/problem=5
# Completed 12/29/2021

def rangeDivisible(num, first, last):
  for i in range(first, last):
    if num % i != 0:
      return False
  return True

num = 0
potential = 20
  
while num == 0:
  if rangeDivisible(potential, 1, 21):
    num = potential
  potential += 1
  
print(num)