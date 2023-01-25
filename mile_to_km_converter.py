
cond = input("Enter from what you want to convert mtokm or kmtomi : ")

if (cond=="mtokm"):
  m = int(input("Enter the number of miles: "))
  print(f"{m} miles is equal to {m * 1.6}")
elif (cond=="kmtom"):
  m = int(input("Enter the number of kilometres: "))
  print(f"{km} miles is equal to {km / 1.6}")
else: 
  print("Sorry you have not given the apt input to the system.")
