class Car:
    def __init__(self, make, model, year):
        self.make = make
        self._model = model  # Private attribute
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self._model}, Year: {self.year}")

    def __update_model(self, new_model):
        self._model = new_model
