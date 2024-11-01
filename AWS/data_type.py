from Advance_features import calculateArea as ca

#Composion of data type
#int, float, str, bool, NoneType, list, dict
# def make(x, y, z, a):
#     #declare a variable
#     print(x)
#     print(y)
#     print(type(int(z)))
#     print(type(z))
#     print(int(z) + y)
#     a = True
#     print(a)
#     print(x<y)
# make(5, 5.0, "5", True)

# #List   0  1 2  3  4
# list = [1, 2, 3, 4, 5]
# #Indexing
# print(list[0])
# print(list[3])
# #Slicing
# print(type(list[0:3])) #1, 2, 3

# #function
# def checkValue():
#     # User input Validation
#     value = input("Enter a digit: ")
#     if value.isdigit():
#         print("You entered a digit")
#     elif value.isalpha():
#         print("You entered a letter, instead of a digit")
#     elif value.isalnum():
#         print("You entered a letter and a digit")
#     elif value.isdecimal():
#         print("You entered a decimal number instead of a digit")
#     else:
#         print("You did not enter the correct value")
#
# checkValue()

''''# #Loops
list = [1, 2, 3, 4, 5]
index = [0, 1, 2, 3, 4]
index1=[1,"a", 3, 4, 5]
print(type(index))
print(type(index1))

#For loop
for i,p,k in zip(list, index, index1):
    #loop through the list and append the index to it
    print(f"The index {p} is {i} and another value {k}")
'''
# # while loop (pre-condition)
# x = input("Enter an exit statement: ")
# while x != "exit":  #not equal to exit
#     x = input("Enter an exit statement: ")
#     print("You have not entered the exit statement")

# print(type(5)) #int
# print(type(5.0)) #float
# print(type("5")) #str
# print(type(True)) #bool
# print(type(None)) #NoneType
# print(type([])) #list
# print(type({})) #dict

#dictionary data type
# dictionary={"name":"John", "age":25, "school":"UENR"}
# print(dictionary["name"])
# print(dictionary["age"])
# print(dictionary["school"])
# print(dictionary.update({"name":"Kwame","department":"IT"}))
# print(dictionary["name"])
# print(dictionary.keys())
# print(dictionary.values())

print(ca)
exit()
