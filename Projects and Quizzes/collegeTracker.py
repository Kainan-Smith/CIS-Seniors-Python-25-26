'''
File: collegeTracker.py
Author: Kainan Smith
'''
import math

# Feature 1
print("="*50)
print(" "*3 + "Welcome to your college application tracker.")
print("="*50)

APPLICATION_FEE = 75.00
AVG_ACCEPTANCE_RATE = 55.0
MAX_IDEAL_DISTANCE = 500

studentName = input("What is your name? ")
numSchools = int(input("How many colleges would you like to apply for? "))

school = []
location = []
tuition = []
distance = []
acceptance_rate = []

# Feature 2
for count in range(numSchools):
    school.append(input("School Name: "))
    location.append(input("Location: "))
    tuition.append(int(input("Tuiton Cost: ")))
    distance.append(float(input("Distance from Home (miles): ")))
    acceptance_rate.append(float(input("Acceptance Rate: ")))


# Feature 3
totalCost = numSchools * APPLICATION_FEE
avgTuition = (math.fsum(tuition)) / numSchools
totalDistance = sum(distance)


# Feature 4
print("\nSchool Information:\n")
for count in range(numSchools):
    print(f"{school[count]}, {location[count]}: ")
    print(f"${tuition[count]:,.2f} per year in tuition.")
    print(f"{distance[count]:,.2f} miles from home.")
    print(f"{acceptance_rate[count]:,.2f}% of students get accepted.")
   
    print("\n")


# Feature 5
print(f"The total cost of applying all {numSchools} schools would be {totalCost}.")
print(f"The average tuition of the {numSchools} schools is {avgTuition:,.2f}.")
print(f"To visit every school, you would have to travel {totalDistance} miles.")

