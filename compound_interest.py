# input values


def compound(principal, rate , time):
    

    # calculate compound interest
    interest = ( principal * (1 + rate/100) ** time ) - principal
    return interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate %: "))
time = int(input("Enter the time period in years: "))

intr = compound(principal, rate , time)

print("The compound interest is:", intr )
