n = int(input())

def sum(n):
    if (n==0):
        return 1
    else:
        return n + sum(n-1)
  
v =sum(n)
print(v)


def fact(n):
    if (n==0):
        return 1
    else:
        return n * fact(n-1)
  
u =fact(n)
print(u)

def gcd(a, b):
    if a%b == 0
        return b
    else:
        return gcd(b, a%b)
    
r = gcd(a, b)
