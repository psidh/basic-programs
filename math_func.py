from math import *

constant_pi = pi

number = int(input("Enter a number:  "))

print(f"The sin value of the given input is {sin(number)}")

print(f"The cos value pof the given input is {cos(number)}")

print(f"The cos value pof the given input is {tan(number)}")

print(f"Exponential of {number} is {mt.exp(number)}")

print(f"natural logarithm of {number} is {mt.log(number)}")

print(f"logarithm of {number} is {mt.log10(number)}")


var_1 = int(input("Enter first number: "))
var_2 = int(input("Enter second number: "))




print(f"the expression is {3*(mt.pow(var_1,2))} + {mt.sqrt(mt.pow(var_1, 2)+ mt.pow(var_2, 2))} + {mt.exp(mt.log(var_1))}")
