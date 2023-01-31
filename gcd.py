
a = int(input("Enter an integer : "))
b = int(input("Enter an integer: "))


if n>m:
    min = m
else:
    min = n

while (i<min):
    if(n%i == 0 and m%i == 0):
        gcd = i

print(f"{i} is the gcd of {a} and {b}")

