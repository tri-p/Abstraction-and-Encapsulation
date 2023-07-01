# PABUNA, KATRINA B. 
# BSCPE 1-4

# create class
class Car:
    # init method
    def __init__(self, year_model, make):
        # private members
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0  # default at zero

    # def show
    def show(self):
        print("\nYear Model:", self.__year_model,
              "\nMake:", self.__make,
              "\nSpeed:", self.__speed)

    # methods
    def accelerate(self):
        for i in range(5):
            self.__speed += 5
            print("Current Speed:", self.__speed)
        return self.__speed
    
    def brake(self):
        for i in range(5):
            self.__speed -= 5
            print("Current Speed:", self.__speed)
        return self.__speed