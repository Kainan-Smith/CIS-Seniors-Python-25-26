'''
File Name: variables.py
Author: Kainan Smith
Date: 9/17/2025

Practicing variable basics
'''

# This is a single line comment
# Variables can hold all data types
myInt = 25
myFloat = 6.28
myString = "Yaba goobie !!"
myBool = True

print("My name is:", myString)

myAge = myInt

print("My age is:", myAge)
print("I do not want to be", myInt + myAge)     #50

print(myFloat)      #6.28
myFloat = 12.20     #reassigned the variable
print(myFloat)      #12.20

print("\n\n\n")

print("My Ticket App")
print("--------------")

ticketTotal = 43.50
processFee = 2.95
venueFee =  3.95

print("\nMy Subtotal is:")
print("----------------")
print("$", ticketTotal + processFee + venueFee)