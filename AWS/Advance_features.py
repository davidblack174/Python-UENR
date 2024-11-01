from os import system
import logging



#Flow Control
# answer = input("Do you want to continue? \n")
# while answer != "no":
#     answer = input("Do you want to continue? \n")
#     if answer == "yes":
#         print("You have chosen to continue")
#     elif answer == "no":
#         print("You have chosen to stop")
#     else:
#         print("You have not entered a valid answer")

#try catch exception
# try:
#     numbers = int(input("Type your number? \n")).is_integer()
#     if numbers:
#         print("You have entered a number")
# except:
#     print("You have not entered a number")


# # User define Functions
# def checkValue():
#     # User input Validation
#     value = input("Enter a digit: ").isdigit()
#     if value == True:
#         print("You entered a digit")
#     else:
#         print("You did not enter the correct value")
#
#
# print(checkValue())

# # Built-in Functions
# print(system("cd /")) #run the command in the terminal
# print(logging.info("This is a log message")) #log message
# print(logging.error("This is an error message")) #error message
# print(logging.warning("This is a warning message")) #warning message

#Calculate area of major objects
# def calculateArea():
def calculateArea():
    #Calculate the area of a square
    selected_shape = input("Enter the shape you want to calculate the area for either one of the following shape (square, rectangle, circle): \n")
    while selected_shape != "square" and selected_shape != "rectangle" and selected_shape != "circle":
        selected_shape = input("Enter the shape you want to calculate the area for: \n")
    if selected_shape == "square":
        square = Squareside() * Squareside()
        print(f"The area of the square is {square}")
    elif selected_shape == "rectangle":
        length = int(input("Enter the length: \n"))
        breadth = int(input("Enter the breadth: \n"))
        rectangle = length * breadth
        print(f"The area of the rectangle is {rectangle}")
    elif selected_shape == "circle":
        pi = 3.142
        radius = int(input("Enter the radius: \n"))
        circle = pi * radius * radius
        print(f"The area of the circle is {circle}")
    else:
        print("You have not enter the right number")


def Squareside():
    side = int(input("Enter the side: \n")).is_integer()
    while side != True:
        side=int(input("Enter the side: \n")).is_integer()
        if side == False:
            print("You have not entered a wrong number")



print(calculateArea())

