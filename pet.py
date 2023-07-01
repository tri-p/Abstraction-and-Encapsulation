# PABUNA, KATRINA B. 
# BSCPE 1-4

# create class
class Pet():
    # init method
    def __init__(self):
        # private members
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    # def show
    def show(self):
        print("Name of the pet:", self.__name,
              "\nAnimal type of the pet:", self.__animal_type,
              "\nAge of pet:", self.__age)

    # getter methods

    # setter methods