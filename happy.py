contestant = int(input("Enter a number: "))

my_x = 1
lit  = []
lit2 = []
strc1 = str(contestant)

for i in range(len(strc1)):
    lit.append(strc1[i])

    for i in range(0, len(lit)):
        x = int(lit[i])**2
        lit2.append(x)
        lit2.remove(9)


print(lit)
print(lit2)
