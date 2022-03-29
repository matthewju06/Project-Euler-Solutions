# https://projecteuler.net/problem=25
# Completed 3/29/2022

# Starting with first 2 numbers to start fib sequence
fibSequence = [0,1]

# Adding to fibSequence until latest value is 1000 digits
while(len(str(fibSequence[len(fibSequence) -1])) < 1000):
    fibSequence.append(fibSequence[len(fibSequence) -1] + fibSequence[len(fibSequence) -2])

print(len(fibSequence) -1)