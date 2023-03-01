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
