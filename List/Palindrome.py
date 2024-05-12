# To check if a string is a palindrome without using built-in functions

s = "malayalam"

def is_palindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True
    
print(is_palindrome(s))


def palindrome_check(s):
    return s == s[::-1]
    
print(palindrome_check(s))

