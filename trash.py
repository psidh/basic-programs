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
    
    
    
  
