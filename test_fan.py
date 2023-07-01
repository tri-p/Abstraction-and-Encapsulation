from fan import Fan

# ===== start =====

# default fan
print("\nDEFAULT FAN")
default_fan = Fan("SLOW", "off", 5, "Blue")
default_fan.show()

# fan 1
print("\nFAN 1")
default_fan.set_speed(3)
default_fan.show()