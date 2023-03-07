# list1 = [1, 2, 3, 4, 5]

# if len(list1) % 2 != 0:
#     list2 = list1[:-1]  # create a copy of list1 without the last element
#     for i in range(len(list2)):
#         if i % 2 == 0:
#             list2[i+1], list2[i] = list2[i], list2[i+1]
    
#     list2.append(list1[-1])  # add back the last element

#     print(list2)
# else:
#     print("List length must be odd for this operation.")

# #________________________________________________________________


# string1 = input()
# last_letter = string1[-1]
# lst = list(string1)

# for letter in string1:
#    if string1.count(letter) > 1:
#         first_index = string1.find(letter) # Find the first occurrence
#         second_index = string1.find(letter, first_index+1) # Find the second occurrence starting from the index of the first occurrence

#         lst[second_index] = "$"
#         lst[-1] = last_letter

# modified = ''.join(lst)

# print(modified)

#__________________________________________________________________

# lst = [-2, -3, 1, -5, 2, -3]
# list2 = []
# for i in range(len(lst)):
#     if lst[i] > 0 and lst[i+1] > 0:
        
#         list2.append(lst[i])
#         list2.append(lst[i+1])
#     else:
#         pass
        
# print(list2)



#__________________________________________________________________


#CONSTANT = 3816547290


#Q1) read two lists - sort individualy - -> merge the lists and display  
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


# Q2 MErge the two lists and the sort the the "merged list"

l1 = []
l2 = []

for i in range(5):
    x1 = int(input())
    l1.append(x1)
for i in range(5):
    x2 = int(input())
    l2.append(x1)


l3 = l1 + l2

for i in range(len(l3)):
    for j in range(len(l3)-1):
        if l3[j] > l3[j+1]:
            l3[j], l3[j+1] = l3[j+1], l3[j]



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

