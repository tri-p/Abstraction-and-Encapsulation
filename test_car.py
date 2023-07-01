from car import Car

# ===== start =====
print("\n" + "\033[93m=" * 80 + "\n")
car = Car(1993, "Chevrolet")
car.show()

# accelerate
print("\n" + "\033[93m=" * 80 + "\n")
print("\n\033[95m\x1B[3m\033[1mThe car is accelerating...\033[0m")
car.accelerate()
car.show()

# brake
print("\n" + "\033[93m=" * 80 + "\n")
print("\n\033[95m\x1B[3m\033[1mThe car is braking...\033[0m")
car.brake()
car.show()
print("\n" + "\033[93m=" * 80 + "\n")