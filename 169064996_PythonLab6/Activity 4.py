class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.__model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.__model}, Year: {self.year}")

    def __update_model(self, new_model):
        self.__model = new_model

    def __str__(self):
        return f"{self.year} {self.make} {self.__model}"
