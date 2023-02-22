num = int(input())
name = input()
marks = []
for i in range(5):
  marks.append(input("Enter the marks: "))

print(f"The marks of the subjects are; ")  
for i in range(5):
  print(marks[i])
print(f"the average of the marks are {sum(marks)/5}")  
print(f"The percentage of {name} is {(sum(marks)/5)*100}")
