n = int(input("Enter the n size: ")) #. N represents the no. of rows to be printed
print("Pattern\n")
for i in range(n):                   #. This is the first loop which makes the rows
  for j in range(i):                 #. The inner loop has the work of printing across the rows like a matrix
    print("*", end="")               #. The asterick or any other print statement can be used and end="" is used to print adjacent values
  print()                            #. The last statement is used is to bring the cursor to the startin position
  
print("\n Inverted Triangle")        #. The Inverted triangle goes with the same approach
for i in range(n):                   #. The initial loop does the same thing as before
  for j in range(n-1):               #. The second loop makes the decrementation with respect to i
    print("*", end="")               
  print()


