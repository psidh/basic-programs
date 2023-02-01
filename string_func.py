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

print(str.center(45, "y"))
print("\n")

print(f"check for alphanumberic: {str.isalnum()}")
print(f"check for decimals: {str.isdecimal()}")
print(f"check for alphabet: {str.isalpha()}")
print(f"check for ascii characters: {str.isascii()}")
print(f"check for digits: {str.isdigit()}")
print(f"identifiers: {str.isidentifier()}")
print(f"title rules followed: {str.istitle()}")
