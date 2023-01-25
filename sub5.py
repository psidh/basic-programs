
math = int(input("enter the marks of maths: "))
eng = int(input("enter the marks of english: "))
p = int(input("enter the marks of physics: "))
c = int(input("enter the marks of cehmistry: "))
py = int(input("enter the marks of python: "))
abg = (math+eng+p+c+py)/5
per = avg*100
print(f"The average of the subjects is {avg}")
print(f"The percentage is {per}")

if (90<=per<=100):
  print("Grade A+")
elif (80<=per<=90):
  print("Grade A")
elif (70<=per<=80):
  print("Grade B+")
elif (60<=per<=70):
  print("Grade B")
elif (50<=per<=60):
  print("Grade C")
elif (40<=per<=50):
  print("Grade D")
else:
  print("Grade F")

