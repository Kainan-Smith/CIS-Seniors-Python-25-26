'''
Convert a set number of minutes to hours.
'''

minutes = int(input("Enter minutes: "))

hours = minutes // 60
minsRemaining = minutes % 60

print(minutes, "minute(s) is", hours, "hour(s) and", minsRemaining, "minute(s).")