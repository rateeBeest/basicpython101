class Car:
    """Just a simple program that written for cars. Docstring"""

    def __init__(self, make, model, year):
        """Initialize make, model, year"""
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"Driving {self.make} {self.model} {self.year} is now driving")

    def stop_drive(self):
        print(f"Driving {self.make} {self.model} {self.year} is now stopped")


my_Tesla = Car("Tesla", "model 3", year="2023")

print(f"my car made is: {my_Tesla.make}")
print(f"my car model is: {my_Tesla.model}")
print(f"my car year is: {my_Tesla.year}")

my_Tesla.drive()
my_Tesla.stop_drive()
