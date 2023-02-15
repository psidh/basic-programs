def isPalindrome(s):
#     s1str = str(s)
    return s1str == s1str[::-1]
 
 

s = input("Enter a string: ")
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
    
n = int(input())

n = int(input())

num = int(input())

def reverse(n):
    length = len(str(n))
    strsrc = ""
    
    for i in range(length):
        strsrc+=str(n%10)
        n = n//10
    palin= ""

    for i in range(len(strsrc)):
        palin += str(strsrc[i])
    print(palin)  
 
    if (palin) == str(num):
        print("A Palindrome number")

    else:
        print("Not a Palindrome")  

reverse(num)
    
