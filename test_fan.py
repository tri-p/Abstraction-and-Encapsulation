from fan import Fan

# ===== start =====

# default fan
print("\nDEFAULT FAN")
default_fan = Fan("SLOW", "off", 5.0, "Blue")
default_fan.show()

# fan 1
print("\nFAN 1")
default_fan.set_speed(3)
default_fan.set_on(True)
default_fan.set_radius(10)
default_fan.set_color("Yellow")
default_fan.show()

# fan 2
print("\nFAN 2")
default_fan.set_speed(2)
default_fan.set_on(False)
default_fan.set_radius(5)
default_fan.set_color("Blue")
default_fan.show()