'''
Given a number, % and // can be used to get each digit. for the three-digit number user_val like 927
'''

myDigit = int(input("Enter a 3 digit number: "))

onesDigit = myDigit % 10
tempVal = myDigit // 10

tensDigit = tempVal % 10
tempVal //= 10

hundredsDigit = tempVal % 10

print(hundredsDigit, tensDigit, onesDigit)