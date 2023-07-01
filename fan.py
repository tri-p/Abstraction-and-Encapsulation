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

    # setter methods to modify data member