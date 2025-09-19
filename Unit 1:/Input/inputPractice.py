'''
File: inputPractice.py
Author: Kainan Smith
Class: CIS Seniors
Date: 9/19/2025

Ask:
First Name
Last Name
Favorite Color
First Number
Second Number
Favorite TV Show
Favorite Movie
Favorite Song
Favorite Food

- Write out a paragraph outlining the user data using variables. Using the First
  and Second Numbers, create 3 separate math equations, and print out the values
  from the expressions.
'''

firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
favColor = input("What is your favorite color? ")
num1 = input("Select the first number: ")
num2 = input("Select the second number: ")
favShow = input("What is your favorite show? ")
favMovie = input("What is your favorite movie? ")
favSong = input("What is your favorite song? ")
favFood = input("What is your favorite food? ")

print("My name is", firstName, lastName + ", my favorite color is", favColor + ".  My favorite show is", favShow + ", my favorite movie is", favMovie + ", my favorite song is", favSong + ", and my favorite food is", favFood + ".")

equation1 = int(num1) + int(num2)
equation2 = int(num1) - int(num2)
equation3 = int(num1) * int(num2)

print(str(num1), "+", str(num2), "=", equation1)
print(str(num1), "-", str(num2), "=", equation1)
print(str(num1), "x", str(num2), "=", equation1)