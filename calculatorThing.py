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
distributor = input("What distributor are you using for your release? ")

if distributor == "Distrokid" or "distrokid" or "DistroKid":
    distributor = "DistroKid"
if distributor == "Soundrop" or "soundrop" or "Sound drop" or "sound drop" or "Sound Drop" or "Sounddrop" or "sounddrop" or "SoundDrop":
    distributor = "Soundrop"

numSongs = int(input("How many original songs are in your release? "))
numCover = int(input("How many cover songs are in your release? "))

# Perform calculations
cost = 0.0
costPerYear = 0.0

if distributor == "DistroKid":
    cost = 24.99
    costPerYear = numCover * (0.99 * 12)
if distributor == "Soundrop":
    cost = (numSongs * 4.99) + (numCover * 5.99)

minListens = cost / MIN_PAY_RATE
maxListens = cost / MAX_PAY_RATE

if distributor == "Soundrop":
    minListens *= 1.15
    maxListens *= 1.15

minListensPerYear = costPerYear / MIN_PAY_RATE
maxListensPerYear = costPerYear / MAX_PAY_RATE

print("Your release will cost you $" + str(cost))
if distributor == "DistroKid":
    print("Additionally, you will have to pay " + str(costPerYear) + " per year, but you can release as many original songs for free for the next year")

print("Therefore, you will need " + str(minListens) + "-" + str(maxListens) + " listens to break even")
if distributor == "DistroKid":
    print("With an additional " + str(minListensPerYear) + "-" + str(maxListensPerYear) + " listens per year to make up for the cost of uploading covers")