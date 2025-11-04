# import the random module
import random

# Generate a random floating point number
print(random.random())
print(random.random())
print(random.random())

# Using randrange()
print(random.randrange(5))
print(random.randrange(5))
print(random.randrange(5))
print(random.randrange(5))
print(random.randrange(5))

print()
print("Using a seed.")
random.seed(15) # Generate same sequence of numbers using same seed

# Generate same sequence of random integers between 1 and 10
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))