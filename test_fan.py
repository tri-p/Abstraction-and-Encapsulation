from fan import Fan

# ===== start =====

# default fan
print("\n" + "\033[93m=" * 80 + "\n")
print("\n\033[95m\x1B[3m\033[1mDEFAULT FAN\033[0m")
default_fan = Fan("SLOW", "off", 5.0, "Blue")
default_fan.show()

# fan 1
print("\n" + "\033[93m=" * 80 + "\n")
print("\n\033[95m\x1B[3m\033[1mFAN 1\033[0m")
default_fan.set_speed(3)
default_fan.set_on(True)
default_fan.set_radius(10)
default_fan.set_color("Yellow")
default_fan.show()

# fan 2
print("\n" + "\033[93m=" * 80 + "\n")
print("\n\033[95m\x1B[3m\033[1mFAN 2\033[0m")
default_fan.set_speed(2)
default_fan.set_on(False)
default_fan.set_radius(5)
default_fan.set_color("Blue")
default_fan.show()
print("\n" + "\033[93m=" * 80 + "\n")