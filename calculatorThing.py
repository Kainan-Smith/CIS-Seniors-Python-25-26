'''
File: calculatorThing.py
Author: Kainan Smith >:]
Date: 9/24/25

Calculate the amount of listens needed to break even for posting music on spotify with different distributors.
'''

# Set Spotify monetization constant
MIN_PAY_RATE = 0.003
MAX_PAY_RATE = 0.005

# Collect inputs and set variables accordingly
distributor = input("What distributor are you using for your release? (DistroKid or Soundrop) ")
numSongs = int(input("How many original songs are in your release? "))
numCover = int(input("How many cover songs are in your release? "))

# Perform calculations
cost = 0.0
costPerYear = 0.0

if distributor == "DistroKid":
    cost = 24.99
    costPerYear = round((numCover * (0.99 * 12)), 2)
if distributor == "Soundrop":
    cost = round((numSongs * 4.99) + (numCover * 5.99), 2)

minListens = round((cost / MIN_PAY_RATE), 2)
maxListens = round((cost / MAX_PAY_RATE), 2)
minListensPerYear = round((costPerYear / MIN_PAY_RATE))
maxListensPerYear = round((costPerYear / MAX_PAY_RATE))

# Output amount of listens needed to break even
print("\n")


if distributor == "DistroKid":
    print("Your release will require a $" + str(cost) + " license, but this will cover all your releases for a year.")
    if numCover > 0:
        print("Additionally, you will have to pay " + str(costPerYear) + " per year to make up for the price of licensing cover songs.")
    print("Therefore, you will need " + str(round(minListens)) + "-" + str(round(maxListens)) + " listens to break even.")
    if numCover > 0:
        print("With an extra " + str(round(minListensPerYear)) + "-" + str(round(maxListensPerYear)) + " listens per year to account for the cover licensing fee.")


if distributor == "Soundrop":
    print("Your release will cost $" + str(cost) + ".")
    print("Note: Soundrop takes 15% of payment from Spotify.")
    print("Therefore, you will need " + str(round(minListens * 1.15)) + "-" + str(round(maxListens * 1.15)) + " listens to break even.")