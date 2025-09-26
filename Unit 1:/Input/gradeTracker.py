'''
File: gradeTracker.py
Author: Kainan Smith >:]
Class: CIS Seniors
Date: 9/26/25
'''

print("=" * 40)
print("Welcome to your grade tracker!")
print("=" * 40)

# Collect inputs
studentCount = input(int("How many students are you tracking? "))
studentName = []
studentGrade = []
totalGrades = 0

print("Please enter student information:")

for count in (0, studentCount):
    sName = input("Student Name: ")
    studentName.append(sName)
    sGrade = int(input("Student Grade: "))
    studentGrade.append(sGrade)
    totalGrades += sGrade

# Calculations
print("Total of Student Grades: " + str(totalGrades))
