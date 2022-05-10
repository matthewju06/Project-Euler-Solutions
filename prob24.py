from itertools import permutations

def lexicographical_permutation(num):
    perm = sorted(''.join(chars) for chars in permutations(num))
    i = 1
    for x in perm:
        if i == 1000000:
            print(x)
        i += 1
        
num ='0123456789'
lexicographical_permutation(num)