#starting
#20th feb -- the 19th feb was too good :)
num = int(input("Enter a number: "))
def arms(num):
  sum = 0
  tempo = num
  while tempo > 0:
    digit = tempo % 10
    sum += digit ** (len(str(num)))
    tempo //= 10
  if num == sum:
    return num,"is an Armstrong number"
  else:
    return num,"is not an Armstrong number"  
ans = arms(num)
print(ans)
 
def fact(num):
    fact = 0
    if num == 1:
      return 1
    for i in range(1, num -1):
        fact *= i
    return fact
