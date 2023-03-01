list= [
    [1, 2, 1],
    [2, 3, 0],
    [2, 4, 1],
]

def even(n):
    if n%2 == 0:
        return True
count = 0
for i in range(len(list)):
    for j in range(2):
        if even((list[i][0]) - (list[i][1]))  and list[i][2] == 0:
            print("True")
            break
        elif even((list[i][0]) - (list[i][1])) == False and list[i][2] == 1:
            print("True")
            break
        else:
            print("False")
            break
    break

    # for universal converage the below code can be used
    # max_list =[]
# list1 = []
# length = int(input("Enter the number of lists you want to enter: "))
# for i in range(length):
#     for j in range(3):
#         start = int(input("Enter start value: "))
#         end = int (input("Enter end value: "))
#         binary  = int(input("Enter the outcome: "))
#         list1.append(start)
#         list1.append(end)
#         list1.append(binary)
#         max_list.append(list1)
