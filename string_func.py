#strings and their functions 1/2/2023

str = input('Enter a string: \n')
print("\n")
print(f"capitalised : {str.capitalize()}")
print(f"casefold :  {str.casefold()}")
print(f"count a in the string: ",str.count("a"))

print(f"capitalised : {str.capitalize()}")
print(f"Title case :{str.title()}")
if str.endswith("h"):
    print("True")

print(str.center(5,"-"))
print("\n")
