def fact(n):
    fact = 1
    for i in range(1, n):
        fact *= n
    return fact

n = int(input("Enter the number to calculate the factorial: "))
print(f"The factorial of {n} is equal to {fact(n)}")
