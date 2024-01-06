# https://projecteuler.net/problem=33
# Completed 1/6/2024
from fractions import Fraction

numerProduct = 1
denomProduct = 1

for numer in range(10, 100):
    for denom in range(10,100):
        if numer/denom < 1:
            for num in range(2):
                numerStr = str(numer)
                singleNumer = numerStr[num]
                removedNumer = numerStr[:num] + numerStr[num+1:]
                denomStr = str(denom)
                removedDenomIndex = denomStr.find(removedNumer)
                
                if removedDenomIndex != -1 and removedNumer != "0" and singleNumer != "0":
                    singleDenom = denomStr[:removedDenomIndex] + denomStr[removedDenomIndex+1:]
                    if singleDenom != "0" and int(singleNumer) / int(singleDenom) == numer / denom:
                        numerProduct *= numer
                        denomProduct *= denom

print(Fraction(numerProduct,denomProduct).denominator)
