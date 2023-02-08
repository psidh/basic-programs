def isPalindrome(s):
#     s1str = str(s)
    return s1str == s1str[::-1]
 
 

s = input("Enter a string: ")
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
