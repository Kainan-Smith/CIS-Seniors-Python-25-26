'''
File: quizScorer.py
Author: Kainan Smith >:]
Class: CIS Seniors
Date: 9/25/25
'''

# Get Inputs
name = input("What is your name? ")
numQuestions = int(input("How many questions was the quiz? "))
if numQuestions < 5:
    print("no it wasnt")
    exit()

print("Scoring", name + "'s quiz with", numQuestions, "questions.")

studentAnswerList = []
correctAnswerList = []
numCorrect = 0

print("Enter student's answers (1 for True, 0 for False):")

for count in range(1, numQuestions + 1):
    sAnswer = int(input("Question " + str(count) + ": "))
    studentAnswerList.append(sAnswer)

print("Enter correct answers (1 for True, 0 for False):")

for count in range(1, numQuestions + 1):
    cAnswer = int(input("Question " + str(count) + ": "))
    correctAnswerList.append(cAnswer)

for count in range(0, numQuestions):
    if studentAnswerList[count] == correctAnswerList[count]:
        numCorrect += 1

quizPercentage = round((numCorrect / numQuestions) * 100)

# Output results
print(name + " got " + str(numCorrect) + " out of " + str(numQuestions) + " questions correct.  Which gives them a score of " + str(quizPercentage) + "%.")

if quizPercentage < 70:
    print("Unfortunately, " + name + " failed their quiz...")
else:
    print(name + " passed their quiz!  Conglomeration!!!")