from pet import Pet

# ===== start =====
print("\n" + "\033[93m=" * 80 + "\n")
pet = Pet()

# prompt the user for information
pet.set_name()
pet.set_animal_type()
pet.set_age()

# display the pet information
print("\n" + "\033[93m=" * 80 + "\n")
print("\033[95m\x1B[3m\033[1mPET'S INFORMATION\033[0m")
pet.show()
print("\n" + "\033[93m=" * 80 + "\n")