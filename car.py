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
        print("\n\033[92m\033[1mYear Model: \033[0m" + str(self.__year_model) +
              "\n\033[92m\033[1mMake: \033[0m" + str(self.__make) +
              "\n\033[92m\033[1mSpeed: \033[0m" + str(self.__speed) + "\n")

    # methods
    def accelerate(self):
        for i in range(5):
            self.__speed += 5
            print("\033[96m\033[1mCurrent Speed:", self.__speed)
        return self.__speed
    
    def brake(self):
        for i in range(5):
            self.__speed -= 5
            print("\033[96m\033[1mCurrent Speed:", self.__speed)
        return self.__speed

    # getter method
    def get_speed(self):
        return self.__speed