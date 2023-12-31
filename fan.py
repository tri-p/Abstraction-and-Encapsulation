# PABUNA, KATRINA B. 
# BSCPE 1-4

# create class
class Fan:
    # init method
    def __init__(self, speed, on, radius, color):
        # private members
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    # def show
    def show(self):
        print("\033[92m\033[1mSpeed:\033[0m", self.__speed,
              "\n\033[92m\033[1mThe fan is\033[0m", self.__on,
              "\n\033[92m\033[1mRadius:\033[0m", self.__radius,
              "\n\033[92m\033[1mColor:\033[0m", self.__color)

    # getter methods
    def get_speed(self):
        return self.__speed

    def get_on(self):
        return self.__on
    
    def get_radius(self):
        return self.__radius
    
    def get_color(self):
        return self.__color

    # setter methods to modify data member
    # condition to allow data modification with rules
    def set_speed(self, number):
        try:
            constant = ""
            if number == 1:
                constant = "SLOW"
            elif number == 2:
                constant = "MEDIUM"
            elif number == 3:
                constant = "FAST"
            else:
                constant = print("The number", number, "is invalid.")
            self.__speed = constant
        except ValueError():
            print("Error.")
        return self.__speed
    
    def set_on(self, on):
        if on is True:
            fan = "on"
        else:
            fan = "off"
        self.__on = fan
        return self.__on
    
    def set_radius(self, number):
        try:
            self.__radius = float(number)
        except ValueError():
            print("Error.")
        return self.__radius
    
    def set_color(self, color):
        self.__color = color
        return self.__color