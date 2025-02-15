# car.py
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

#main.py
from car import Car

def compare_car_years(car1, car2):
    # This function returns True if car1 is newer than car2
    return car1.year > car2.year

# Creating two Car instances to compare
car1 = Car("Toyota", "Corolla", 2025)
car2 = Car("Honda", "Civic", 2024)

# Using the comparison function and printing the result
comparison_result = compare_car_years(car1, car2)
print(f"Car1 ({car1}) is newer than Car2 ({car2}): {comparison_result}")


