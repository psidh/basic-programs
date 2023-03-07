
#Q2) read two lists - sort individualy - -> merge the lists and display  
#_______________________________________________________

l1 = [5, 4, 3]
l2 = [4, 7, 2]

# sort l1
for i in range(len(l1)):
    for j in range(len(l1)-1):
        if l1[j] > l1[j+1]:
            l1[j], l1[j+1] = l1[j+1], l1[j]

# sort l2
for i in range(len(l2)):
    for j in range(len(l2)-1):
        if l2[j] > l2[j+1]:
            l2[j], l2[j+1] = l2[j+1], l2[j]

# merge and display
l3 = l1 + l2
print(l3)

# Q3) read a sentence into a string and sort the words in a sentence in ascending order of the length of the words 
#_________________________________________________________

strsrc = input("Enter a sentence: ")

lst = strsrc.split()
 
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if len(lst[j]) > len(lst[j+1]):
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)

