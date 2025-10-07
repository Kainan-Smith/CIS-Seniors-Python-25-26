# Python Variable Name Validator
# Student Name: _______________
# Date: _______________

# List of Python keywords
pythonKeywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
    'while', 'with', 'yield'
]
numbers = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
]

# Display welcome message
print("=== PYTHON VARIABLE NAME VALIDATOR ===")
print("This program checks if your variable name is valid in Python.")
print()

# Get user input
variableName = input("Enter a variable name to validate: ")
varNameChars = list(variableName)


# Your validation code goes here
for item in (varNameChars):
    if variableName == "" or variableName == " ":
        print("Invalid Variable Name.  Identifier cannot be empty.")
    elif varNameChars[0] in numbers:
        print("Invalid Variable Name.  Identifier cannot start with a number.")
        break

# Check each rule and provide appropriate feedback