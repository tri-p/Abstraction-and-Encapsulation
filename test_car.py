from car import Car

# ===== start =====
print("\n")
car = Car(1993, "Chevrolet")
car.show()

# accelerate
print("=" * 80)
print("\nThe car is accelerating...")
car.accelerate()
car.show()

# brake
print("=" * 80)
print("\nThe car is braking...")
car.brake()
car.show()