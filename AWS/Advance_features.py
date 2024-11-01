from os import system
import math


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

# #Calculate area of major objects
# def circleArea():
#     while True:
#         try:
#             pi = 3.142
#             radius = int(input("Enter the radius: \n"))
#             return pi * radius * radius
#         except ValueError:
#             print("You have not entered a valid number for length or breadth")
# def ValidateUserEntry():
#     while True:
#         try:
#             length = float(input("Enter the length: \n"))
#             breadth = float(input("Enter the breadth: \n"))
#             return breadth*length
#         except ValueError:
#             print("You have not entered a valid number for length or breadth")
# def Squareside():
#     while True:
#         try:
#             side = float(input("Enter the side: \n"))
#             return side
#         except ValueError:
#             print("You have not entered a valid number")
# # def calculateArea():
# def calculateArea():
#     selected_shape = input("Enter the shape you want to calculate the area for (square, rectangle, circle): \n")
#     while selected_shape not in ["square", "rectangle", "circle"]:
#         selected_shape = input("Enter the shape you want to calculate the area for: \n")
#
#     if selected_shape == "square":
#         print(f"The area of the square is {math.pow(Squareside(),2)}")
#     elif selected_shape == "rectangle":
#         print(f"The area of the rectangle is {ValidateUserEntry()}")
#     elif selected_shape == "circle":
#         print(f"The area of the circle is {circleArea()}")
#     else:
#         print("You have not entered the right shape")
#     return "Your shape is " + selected_shape
#
# print(calculateArea())

# Create a File
password=input("Enter your secret super password: ")
file=open("secret.txt", "w")
file.write(password)
file.close()

# Read a File



