from fan import Fan

# ===== start =====

# default fan
default_fan = Fan("SLOW", "off", 5, "Blue")
default_fan.show()

# fan 1
print("\n")
default_fan.set_speed(3)
default_fan.show()