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
        print("Speed:", self.__speed,
              "\nThe fan is", self.__on,
              "\nRadius:", self.__radius,
              "\nColor:", self.__color)

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