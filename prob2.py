# https://projecteuler.net/problem=2
# Completed 12/24/2021

def isEven(num):
  if num % 2 == 0:
    return True
  return False

fibseq = [1, 2]
while fibseq[-2] + fibseq[-1] <= 4000000:
  fibseq.append(fibseq[-2] + fibseq[-1])
  
filtered = list(filter(isEven, fibseq))

print(sum(filtered))