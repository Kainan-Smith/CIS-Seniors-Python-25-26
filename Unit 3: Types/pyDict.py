'''
Student Grade Book Manager

Program: pyDict.py
Author: Kainan Smith
Date: 11/04/2025

- Student ID: "512345"
- Grade Level: 12
- Email: "emma.r@school.edu"
- Math Grade: 95
- English Grade: 88
- Science Grade: 92
- Homework Completed: True

Tasks:
1. Create a dictionary called student1 with all the information above
2. Print the entire dictionary
3. Print just Emma's email address
4. Print just Emmaa's math grade
'''

# Part 1: Create your dictionary here
student1 = {
    "name": "Emma Rodriguez",
    "studentID": "512345",
    "grade": 12,
    "eMail": "emma.r@school.edu",
    "mathGrade": 95,
    "englishGrade": 88,
    "scienceGrade": 92,
    "homework": True
}

# Print the entire dictionary
print("Complete Student Record")
print(student1)

# Print specific values
print("\nStudent E-Mail:", student1["eMail"])
print("Math Grade:", student1["mathGrade"])

# Part 2
# Modify Emma's homework status
student1["homework"] = False

# Update her English Grade
student1["englishGrade"] = 91

# Add a history grade
student1["historyGrade"] = 89

# Add clubs information
student1["clubs"] = ["Debate Team", "Math Club"]

# Print the updated dictionary
print("\nUpdated Student Record:")
print(student1)

# Part 3: Create a function to calculate average grade
# Python function structure: def funcName(arguments)
def calculateAverage(student):
    # Get all the grades
    math = student["mathGrade"]
    english = student["englishGrade"]
    science = student["scienceGrade"]
    history = student["historyGrade"]

    # Calculate average
    total = math + english + science + history
    average = total / 4

    # Return the average
    return average

# Test your function
# Function call:
average = calculateAverage(student1)
print(f"\n{student1["name"]}'s average grade: {average:.2f}")


# Part 4: Using Dictionary Methods
# 1. Print all keys
print("\nAll keys in the dictionary:")
print(student1.keys())

# 2. Print all values
print("\nAll values in the dictionary:")
print(student1.values())

# 3. Print all key:value pairs
print("\nAll the key:value pairs:")
print(student1.items())

# 4. Safely get phone number (doesn't exist)
phone = student1.get("phoneNumber")
print("\nPhone Number:", phone)


# 5. Create new student and use update()
student2 = {
    "name": "Marcus Chen",
    "studentID": "512345" ,
}

# Use .update() to add these fields all at once:
student2.update({"grade": 11, "mathGrade": 87, "englishGrade": 90, "scienceGrade": 85})


print("\nNew Student Record:")
print(f"{student2["name"]}:")
print(f"Student ID: {student2["studentID"]}")
print(f"Grade Level: {student2["grade"]}")
print(f"Math Grade: {student2["mathGrade"]}")
print(f"English Grade: {student2["englishGrade"]}")
print(f"Science Grade: {student2["scienceGrade"]}")