
DICT = {}

for i in range(15):
    n = int(input("Enter the key: "))
    m = int(input("Enter the value: "))

    DICT[n] = m

print(DICT)

def rad_eval():
    return(eval(input("Enter the dictionary values: ")))
