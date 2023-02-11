num = int(input("Enter a number: "))


sum = 0


tempo = num
while temp > 0:
   digit = tempo % 10
   sum += digit ** 3
   tempo //= 10


if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

   
   # n armstrong numbers between a given range
number = int(input())

string = str(number)
length = len(string)

for i in range(1, number):

    temp = i
    s=0
    while(i>0):
        rem = i%10
        s = s+ (rem**length)
        i //= 10
    if (temp == s):
        print(temp)
    

