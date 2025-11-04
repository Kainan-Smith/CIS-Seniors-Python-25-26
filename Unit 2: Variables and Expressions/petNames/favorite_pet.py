# A script favorite_pet.py that imports and uses the pet_names module

import pet_names # imports the pet_names module

print("My favorite pet is", pet_names.petName1, "-")
print("I remember when he weighed only", pet_names.petWeight1, "pounds.")
print("I love", pet_names.petName2, "too, of course.")

if __name__ == "__main__":
    print("This is the __main__ code from favorite_pet.py")