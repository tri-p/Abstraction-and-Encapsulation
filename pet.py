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
        print("\033[92m\033[1mName:\033[0m", self.__name,
              "\n\033[92m\033[1mAnimal Type:\033[0m", self.__animal_type,
              "\n\033[92m\033[1mAge:\033[0m", self.__age)

    # getter methods
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    # setter methods
    def set_name(self):
        name = input("\033[92m\033[1mWhat is the pet's name? \033[0m")
        self.__name = name
        return self.__name
    
    def set_animal_type(self):
        animal_type = input("\033[92m\033[1mWhat type of animal is the pet? \033[0m")
        self.__animal_type = animal_type
        return self.__animal_type
    
    def set_age(self):
        age = int(input("\033[92m\033[1mWhat is the pet's age? \033[0m"))
        self.__age = age
        return self.__age