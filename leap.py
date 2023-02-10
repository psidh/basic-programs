def check(year):
  if (year % 100==0 and year%400==0):
    print("The year is leap year.")

  elif(year%4==0):
    print("THe year is leap year.")

  else:
    print("not a leap year")

year = int(input("Enter the year: "))
check(year)
 
# second method


start = int(input())
end = int(input())

for i in range(start , end):
  if (i % 100==0 and i%400==0) or (i%4==0):
    print( i, end=" ")
