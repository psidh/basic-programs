(X, Y, Z ) = (1, 2, 3)

print(X)
print(Y)

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
list1 = list(tuple1)

print(list1)
list1[3]  = "4"
list1.append(67)
list1.remove(3)
list1.pop()
for i in range(len(list1)):
    list1.append(i)

print(tuple1)
 
print(tuple1.count(2))
