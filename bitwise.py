# PROGRAM 1: FLOOR DIVISION AND EXPONENT

a = int(input())    # VARIABLE SET 1
b = int(input())

print(a//b)  #FLOOR DIV
print(a**b)  #EXPONENT

# PROGRAM 2: BITWISE OPERATORS

c = int(input())    # VARIABLE SET 2
d = int(input())

print(c|d)  #BITWISE OR
print(c&d)  #BITWISE AND
print(~c)   #BITWISE NEGATION
print(c ^ d) #BITWISE XOR

#PROGRAM 3: LEFT SHIFT AND RIGHT SHIFT

e = int(input())    # VARIABLE SET 1
f = int(input())

print(e>>1)
print(f<<3)

#PROGRAM 4: REVISION


cond = input("Enter from what you want to convert mtokm or kmtomi : ")

if (cond=="mtokm"):
  m = int(input("Enter the number of miles: "))
  print(f"{m} miles is equal to {m * 1.6}")
elif (cond=="kmtom"):
  m = int(input("Enter the number of kilometres: "))
  print(f"{km} miles is equal to {km / 1.6}")
else: 
  print("Sorry you have not given the apt input to the system.")
