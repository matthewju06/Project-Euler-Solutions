from itertools import permutations

# Finds permutations in order
def lexicographical_permutation(num):
    perm = sorted(''.join(chars) for chars in permutations(num))
    i = 1
    for x in perm:
        # Going until the millionth permutation
        if i == 1000000:
            print(x)
        i += 1

num ='0123456789'
lexicographical_permutation(num)