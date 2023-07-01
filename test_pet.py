from pet import Pet

# ===== start =====
print("\n")
pet = Pet()

# prompt the user for information
pet.set_name()
pet.set_animal_type()
pet.set_age()

# display the pet information
print("\n")
print("PET'S INFORMATION")
pet.show()
print("\n")