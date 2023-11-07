from my_package.module1 import Vehicle

class Bicycle:
    def __init__(self, make, model, year, color, type):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.type = type


    def ride(self):
        return f"Riding the {self.color} {self.year} {self.make} {self.model} {self.type}."
    

