#
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
    
 #input menu
select = int(input("Select Options from 1-Add., 2-Sub., 3-Mult., 4-Div., 5-Square :"))

number_1 = int(input("Enter Your First number: "))
#after entering your first number, the script will immediately direct you to the following l=menu directly below
number_2 = int(input("Enter Your Second number: "))

if select == 1:
    print (number_1, "+", number_2, "=", add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))

elif select == 3: 
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))

elif select == 5:
    print(number_1, "**", number_1, multiply(number_1, number_1))

else:
        print ("Incorrect Input")
        