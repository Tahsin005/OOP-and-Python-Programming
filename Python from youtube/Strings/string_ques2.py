'''Write a python function that checks if the given string is a palindrome or not'''
def isPalindrome(s):
    clean = (s.replace(" ", "")).lower()
    rev = clean[::-1]
    return rev == clean
    
s = input()
print(isPalindrome(s))