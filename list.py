
# ● Program to get the difference between the two lists.

lk = [1, 2, 3, 4, 5]
lo = [6, 5, 4, 3, 2]

for i in range(5):
    if lk[i] not in lo:
        l3 = []
        l3.append(lk[i])
    else:
        pass
print(l3)


list2=[]
def i():
    rows = int(input("Enter thh number of rows: "))
    
    for i in range(rows):
        input_ = input("Enter the row sequence")
        k = input_.split()
        list2.append(k)

i()
print(list2)

list3 = []
for row in l1:
    boy = row.count(0)
    girl = row.count(1)
    list3.append([boy, girl])

for i in range(len(list3)):
    
    print(f"{i+1} Row: boys {list3[i][0]}")
    print(f"{i+1} Row: girls {list3[i][1]}")
