def isPalindrome (s):
    return s == s[::-1]

s = "dad"
a = isPalindrome(s)

if (a):
    print("is palndrome")
else:
    print("is not a palndome")