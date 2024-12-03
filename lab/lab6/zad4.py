class Vehicle:
    def __init__(self, wheels, model, color,):
        self.wheels = wheels
        self.model = model
        self.color = color
    def print_out(self):
        pass
    def input_value(self):
        pass

class LuxCar(Vehicle):
    def __init__(self, wheels, model, color, passengers):
        super().__init__(wheels, model, color)
        self.passengers = passengers
    def print_out(self):
        return f"Amount of wheels: {self.wheels}, Model: {self.model}, Color: {self.color}, Passengers: {self.passengers}"
    def input_value(self):
        self.wheels = input("Number of wheels: ")
        self.model = input("Model: ")
        self.color = input("color: ")
        self.passengers = input("Passengers: ")
    
class SportsCar(Vehicle):
    def __init__(self, wheels, model, color, loadlimit):
        super().__init__(wheels, model, color)
        self.loadlimit = loadlimit
    def print_out(self):
        return f"Amount of wheels: {self.wheels}, Model: {self.model}, Color: {self.color}, Passengers: {self.loadlimit}"
    def input_value(self):
        self.wheels = input("Number of wheels: ")
        self.model = input("Model: ")
        self.color = input("color: ")
        self.laodlimit = input("Passengers: ")

        