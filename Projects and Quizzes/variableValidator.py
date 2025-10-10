# Python Variable Name Validator
# Student Name: _______________
# Date: _______________

# List of Python keywords
pythonKeywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
    'while', 'with', 'yield', 'print'
]
# Display welcome message
print("=== PYTHON VARIABLE NAME VALIDATOR ===")
print("This program checks if your variable name is valid in Python.")
print()

# Check each rule and provide appropriate feedback
while True:
    variableName = input("Enter a variable name to validate: ")
    wrongChar = variableName.isalnum()

    validVar = True
    specialChar = False
    emptyString = False
    startNumber = False
    pyKeyword = False

    if variableName == "":
        emptyString = True
        validVar = False
    else:
        if wrongChar == False:
            specialChar = True
            validVar = False
        if variableName[0].isdigit():
            startNumber = True
            validVar = False
        if variableName in pythonKeywords:
            pyKeyword = True
            validVar = False

    if validVar == False:
        print("Invalid Variable Name.")
        if specialChar == True:
            print("Identifier cannot contain spaces or special characters other than \"_\".")
        if emptyString == True:
            print("Identifier cannot be empty.")
        if startNumber == True:
            print("Identifier cannot start with a number.")
        if pyKeyword == True:
            print("Identifier cannot be the name of a Python Keyword.")
    else:
        print("Valid Variable Name.  Good Job!")