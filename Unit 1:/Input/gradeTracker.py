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
studentCount = int(input("How many students are you tracking? "))
studentName = []
studentGrade = []
totalGrades = 0
numPassing = 0
lowestScore = 100
highestScore = 0
studentLetterGrade = []
numA = 0
numB = 0
numC = 0
numD = 0
numF = 0

print("Please enter student information:")

print("\n")


for count in range(studentCount):
    sName = input("Student Name: ")
    studentName.append(sName)
    sGrade = int(input("Student Grade: "))
    studentGrade.append(sGrade)
    if sGrade >= 70:
        numPassing += 1
    totalGrades += sGrade
    if sGrade < lowestScore:
        lowestScore = sGrade
    elif sGrade > highestScore:
        highestScore = sGrade

    if sGrade >= 90:
        studentLetterGrade.append("A")
        numA += 1
    elif 80 <= sGrade < 90:
        studentLetterGrade.append("B")
        numB += 1
    elif 70 <= sGrade < 80:
        studentLetterGrade.append("C")
        numC += 1
    elif 60 <= sGrade < 70:
        studentLetterGrade.append("D")
        numD += 1
    elif sGrade < 60:
        studentLetterGrade.append("F")
        numF += 1
    

# Calculations
gradeAverage = totalGrades / studentCount

print("\n")

# Output
print("Number of Studends:", studentCount)
print("Total of Student Grades:", totalGrades)
print("Average:", gradeAverage)
print("Highest Score:", highestScore)
print("Lowest Score:", lowestScore)
print("Amount of passing students: " + str(numPassing) + "/" + str(studentCount))
print("Pass Rate: " + str(round(((numPassing / studentCount) * 100), 2)) + "%")

print("\n")

print("A Grades (>90):", numA)
print("B Grades (80-89):", numB)
print("C Grades (70-79):", numC)
print("D Grades (60-69):", numD)
print("F Grades (<59):", numF)