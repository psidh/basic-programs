n = int(input("Enter the n size: ")) 
print("Pattern\n")
for i in range(n):
  for j in range(i):
    print("*", end="")
  print()
  
print("\n Inverted Triangle")
for i in range(n):
  for j in range(n-1):
    print("*", end="")
  print()
