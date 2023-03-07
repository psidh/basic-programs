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

n1 = int(input("Enter the number of elemetns in the list 1: "))
n2 = int(input("Enter the number of elemetns in the list 2: "))

for i in range(n1):
    x = int(input())
    l1 = []
    l1.append(x)
for i in range(n2):
    y = int(input())
    l2 = []
    l2.append(y)
    
    

