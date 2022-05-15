# https://projecteuler.net/problem=36
# Completed 5/13/2022

sum = 0

# Finds if string is palindrome, returns True if true.
def isPalindrome(string):
    if string == string[::-1]:
        return True
    return False

for num in range(1000000):
    # Checks if base 10 and base 2 are both palindrome
    if isPalindrome(str(num)) and isPalindrome(str(bin(num))[2:]):
        sum += num

print(sum)