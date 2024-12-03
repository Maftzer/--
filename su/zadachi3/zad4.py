import math

class Shape():
    def __init__(self, figura):
        self.figura = figura
        
    def area(self):
        return 0
        
class Square(Shape):
    def __init__(self, duljina):
        super().__init__("Square")
        self.duljina = duljina
    def area(self):
        return self.duljina **2

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius **2
    
def create_shape():
    shape_type = input("vuvedete figura(Square ili Circle): ").strip().lower()
    if shape_type == 'square':
        duljina = int(input("Vuvedete duljina na stranata: "))
        shape = Square(duljina)
    elif shape_type == 'circle':
        radius = int(input("Vuvedete radius: "))
        shape = Circle(radius)
        
    print(f"Liceto na {shape.figura} e ravno na {shape.area()}")
    
create_shape()
