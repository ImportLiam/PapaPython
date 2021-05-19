import math

#addition function
def add (num1, num2):
    return num1 + num2

#subtraction function
def subtract (num1, num2):
    return num1 - num2

#multiplication function
def multiply (num1, num2):
    return num1 * num2

#division function
def divide (num1, num2):
    return num1 / num2

#square function
def square (num1):
    return num1 * num1
    
 #menu
select = int(input("Select Options from 1, 2, 3, 4, 5 :"))

number_1 = int(input("Enter Your First number: "))
number_2 = int(input("Enter Your Second number: "))

if select == 1:
    print (number_1, "+", number_2, "=", add(number_1, number_2))
elif select == 2:
    print(number_1. "-", number_2, "=", subtract(number_1, number_2))