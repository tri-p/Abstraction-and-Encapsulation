from car import Car

# ===== start =====
print("\n")
car = Car(1993, "Chevrolet")
car.show()

# accelerate
print("\n")
print("=" * 80)
print("\nThe car is accelerating...")
car.accelerate()
car.show()
print("\n")

# brake
print("=" * 80)
print("\nThe car is braking...")
car.brake()
car.show()