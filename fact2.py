
def factorial(x):

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))



num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print(f"The factorial of {num} is {result}")