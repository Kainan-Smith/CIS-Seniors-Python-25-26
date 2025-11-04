'''
Python has a module called random.  It needs to be imported to use it.
'''

import random
for roll in range(10):
    print(random.randint(1, 6), end=" ")

# Second example
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
count = 0

while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    else:
        print("You winner !!")
        print(count, "guesses")
        break