'''
File: pyQuiz1.py
Author: Kainan Smith
Class: CIS Seniors
Date: 10/1/25
'''

# Question 1
print("Question 1:")

for count in range(1, 6):
    print(count + 1)

print("\n")
# Question 2
print("Question 2:")

for count in range(3, 9):
    print(count)

print("\n")
# Question 3
print("Question 3:")

for count in range(0, 11, 2):
    print(count)

print("\n")
# Question 4
print("Question 4:")

for count in range(10, 0, -1):
    print(count)

print("\n")
# Question 5
print("Question 5:")

for count in range(1, 6):
    print("5 x", count, "=", (5 * count))

print("\n")
# Question 6
print("Question 6:")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

print("\n")
# Question 7
print("Question 7:")

for count in range(1, 11):
    if count % 2 == 0:
        print("Even")
    else:
        print("Odd")

print("\n")
# Question 8
print("Question 8:")

for count in range(20, -1, -5):
    print("Countdown", count)

print("\n")
# Question 9
print("Question 9:")

for count in range(1, 7):
    if count < 4:
        print("Number", count, "is Small")
    else:
        print("Number", count, "is Large")

print("\n")
# Question 10
print("Question 10:")

number = int(input("Enter a number: "))

for count in range(1, number + 1, 2):
    if count < 5:
        print("Low:", count)
    else:
        print("High:", count)

print("\n")
# Bonus Question
print("Bonus Question:")

for count in range(15, -1, -3):
    if count > 0:
        print(count)
    else:
        print("Blastoff!")