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
print(f"the strings wiht he followong values in it: {str.find}")

string1 = input("Enter a string to operate some of the functions: ")

print(f" Check for numberical spaces in a string {string1.isspace}") ## boolean operator on a string

pan_number = input("Enter a string: ")

# def is_Valid_pan_alpha(pan_number):
#     pan_number.isalpha and pan_number.isupper
  

# def check_pan():
#     if pan_number.length == 10 and is_Valid_pan_alpha(pan_number) and pan_number[5:8].isnum == "True":
       

def check_pan(pan_number):
    if pan_number.isupper =="True" and pan_number.length == 10 and pan_number[0:4].isalpha == "True" and pan_number[5:8].isnum == "True" and pan_number[10].isalpha == "True":
        print("Pan Card number is a valid one ")
    else:
        print("Invalid PAN card number")
       
