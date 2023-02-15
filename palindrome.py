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

def reverse(n):
    length = len(str(n))
    list = []
    for i in range(length):
        list.append(n%10)
        n = n//10
    palin=''
    for i in range(len(list)):
        palin += str(list[i])
    print(palin)  
    if int(palin) == n:
        print("A Palindrome number")
    else:
        print("Not a Palindrome")  

reverse(n)
    
