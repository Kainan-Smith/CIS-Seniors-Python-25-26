'''
File: fitnessTracker.py
Author: Kainan Smith
Class: CIS Seniors
Date: 9/23/25

Inputs needed:

'''
print(15 // 12)
print("Welcome to your personalized fitness tracker!")
# Collect inputs)
name = input("What is your name? ")
age = str(input("What is your age? "))
weight = float(input("What is your weight in pounds? "))
height = int(input("What is your height in inches? "))

# Feet and Inches conversion
feet = height // 12
inches = height % 12
specificHeight = "(" + str(feet) + "feet,", inches, "inches)"

exerciseHours = float(input("How any hours do you exercise per week? "))
mainGoal = input("What is your main fitness goal? ")

print("=" * 50)
print("       Fitness report for", name)
print("=" * 50)

print("\n")

# Pre-equation Information
print("Personal Information:")
print("Name:", name)
print("Age:", age, "years old")
print("Weight:", weight, "lbs")
print("Height:", height, "inches", specificHeight)

print("\n")

# Equations
bmi = (weight / (height ** 2)) * 703
exerciseMinutes = (exerciseHours * 60) / 7
weeklyCalories = exerciseHours * 300

# Post-equation Information
print("Fitness Metrics:")
print("BMI:", bmi)
print("Weekly Exercise:", exerciseHours)
print("Daily Exercise:", exerciseMinutes)
print("Setimated Weekly Calories Burned:", weeklyCalories)

print("\n")

print("Fitness Goal:", mainGoal)

print("\n")

print("Keep up the great work with your fitness journey!")