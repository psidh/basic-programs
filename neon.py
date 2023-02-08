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

#new method for calculating the neon number:


num3 = int(input("Enter a number \n"))
sqr2 = num**2 

str = str(sqr2)

inte = []

for i in range(len(str)):
    inte.append(int(str[i]))

print(inte)
num2 = 0
for i in range(len(str)):
    num2 += inte[i]

print(num2)

if (num3 == num2):
    print("Neon Number \n")
else:
    print("Not a Neon Number \n")
