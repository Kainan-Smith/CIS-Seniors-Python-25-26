'''
Program: approxSquareRoots.py
Author David Wells
Class: CIS Seniors
Date: 10/2/25

Request: Write a program that computes square roots. You will use Python's math module.  Python's math module has a function caled sqrt - math.sqrt() - will only be used at the end to compare your calculation with Python's calculation.

Compute the square root of a number:
1. The input is a number.
2. The outputs are the program's estimate of the square root using Newton's method of successive approximations and Python's own estimate using math.sqrt().
'''

import math

# Receive the input number from the user
x = float(input("Enter a positive number: "))

# Initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0

# Perform the successive approximations
while True:
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        break

# Output the result
print("The program's estimate:", estimate)
print("Python's estimate:     ", math.sqrt(x))