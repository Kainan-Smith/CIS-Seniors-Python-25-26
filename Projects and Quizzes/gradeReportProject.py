'''
File: gradeReportProject.py
Author: Kainan Smith >:]
Date: 11/4/2025
'''
# Challenge: Complete Grade Book System

# Create a list of student dictionaries
def averageFunc(student):
    total = student["math"] + student["english"] + student["science"] + student["history"]
    avg = total / 4
    return avg

grade_book = [
    {"name": "Emma Rodriguez", "idNumber": "512345", "math": 95, "english": 91, "science": 92, "history": 89},
    {"name": "Marcus Chen", "idNumber": "512346", "math": 87, "english": 90, "science": 85, "history": 88},
    {"name": "Sophia Patel", "idNumber": "512347", "math": 98, "english": 96, "science": 94, "history": 97}
]

grade_book[0]["average"] = averageFunc(grade_book[0])
grade_book[1]["average"] = averageFunc(grade_book[1])
grade_book[2]["average"] = averageFunc(grade_book[2])

def print_class_report(students):
    """Prints a formatted report for all students"""
    for item in grade_book:
        count = 0
        print(grade_book[count]["name"])
        count += 1
    pass

def find_top_student(students):
    """Returns the student with the highest average"""
    # Your code here
    pass

def count_honor_students(students):
    """Counts students with average >= 90"""
    # Your code here
    pass

# Test your functions
print_class_report(grade_book)
top_student = find_top_student(grade_book)
honor_count = count_honor_students(grade_book)