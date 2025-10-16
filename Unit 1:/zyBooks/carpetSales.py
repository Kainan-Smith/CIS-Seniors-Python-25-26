'''
Step 1: Read from input the carpet price per square foot (float), room width (int) and room length (int).  Calculate the room area in square feet.  Calculate the carpet price based on square feet with an additional 20% for waste.  Output square feet and carpet cost.  Submit forgrading to confirm 1 test passes.
'''
totalSales = 0

# Initialize Constants
TAX_RATE = 0.007
WASTE_PCT = 1.2
LABOR_RATE = 0.05

# Order 1
# Input price per sq foot, room width and room length
price = float(input("Enter price per square foot: "))
width = int(input("Enter the width of the room: "))
length = int(input("Enter the length of the room: "))

# Calculate room square feet
sq_ft = width * length

# Calculate carpet cost including 20% waste
carpet = (sq_ft * WASTE_PCT) * price

# Calculate labor (0.75¢ per sq ft)
labor = sq_ft * LABOR_RATE

# Calculate sales tax (7%)
tax = (carpet + labor) * TAX_RATE

# Calculate total cost
cost = carpet + tax + labor

# Output results
print("Order #1")
print(f"Square Footage: {sq_ft} sq ft.")
print(f"Carpet Cost: ${carpet:.2f}.")
print(f"Labor Cost: ${labor}")
print(f"Tax: ${tax:.2f}")
print(f"Cost: ${cost:.2f}")
totalSales += cost


# Order 2

# Input
print("\nFor Order 2, add the price per sq ft, width, and length all separated be a space.  Ex. 2.45 16 10")
price, width, length = input().split()

price = float(price)
width = int(width)
length - int(length)

# Calculations
sq_feet = width * length
carpet = (sq_ft * price) * WASTE_PCT
labor = sq_ft * LABOR_RATE
tax = (carpet + labor) * TAX_RATE
cost = carpet + labor + tax

print("\nOrder #2")
print(f"Square Footage: {sq_ft} sq ft.")
print(f"Carpet Cost: ${carpet:.2f}.")
print(f"Labor Cost: ${labor}")
print(f"Tax: ${tax:.2f}")
print(f"Cost: ${cost:.2f}")
totalSales += cost

# Order 3
price, width, length = input().split()

price = float(price)
width = int(width)
length - int(length)

# Calculations
sq_feet = width * length
carpet = (sq_ft * price) * WASTE_PCT
labor = sq_ft * LABOR_RATE
tax = (carpet + labor) * TAX_RATE
cost = carpet + labor + tax

print("\nOrder #3")
print(f"Square Footage: {sq_ft} sq ft.")
print(f"Carpet Cost: ${carpet:.2f}.")
print(f"Labor Cost: ${labor}")
print(f"Tax: ${tax:.2f}")
print(f"Cost: ${cost:.2f}")
totalSales += cost


print(f"\nTotal Sales: ${totalSales:.2f}")