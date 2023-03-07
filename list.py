
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


# #Q4)  list of combinations of 0's  and 1's   -  two dimen array

# # boys = 0
# # girls = 1


list2 = []
def i():
    rows = int(input("Enter the number of rows: "))
    
    for i in range(rows):
        input_ = input("Enter the row sequence: ")
        k = [int(x) for x in input_.split()]
        list2.append(k)
i()
print(list2)

list3 = []

for row in list2:
    boy = row.count(0)
    girl = row.count(1)
    list3.append([boy, girl])

for i, counts in enumerate(list3):
    print(f"Row {i+1}: boys {counts[0]}")
    print(f"Row {i+1}: girls {counts[1]}")





