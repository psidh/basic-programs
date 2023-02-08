num = int(input("Enter a number \n"))
sqr = num**2 
sum = 0


while (sqr>0):
    sum =sum + sqr%10
    sqr = sqr//10 # floor division

if (num == sum):
    print(f"{num} is a Neon Number \n")
else:
    print(f"{num} is not a Neon Number \n")
