num = 0
while num >= 0:
    num = int(input("Enter an integer (negative to quit): "))

    if num >= 0:
        print("Depicted graphically:")
        for i in range(num):
            print("*", end=" ")
        print("\n")

print("Goodbye")