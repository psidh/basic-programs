def gcd(a, b):
    if a > b:
        r = a % b
        if r == 0:
            return b
        else:
            return gcd(b, a % b)
    else:
        r = a % b 
        if r == 0:
            return a
        else:
            return gcd(a, b % a)

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

print(gcd(a,b ))
