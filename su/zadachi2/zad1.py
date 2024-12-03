class Building:
    def __init__(self, height, area, adress):
        self.height=height
        self.area = area
        self.adress = adress
    def print_out(self):
        print(f"Height: {self.height}, Area: {self.area}, Adress: {self.adress}")      

class House(Building):
    def __init__(self,height,area,adress, floors, name):
        super().__init__(height, area, adress)
        self.floors = floors
        self.name = name
    def print_out(self):
        super().print_out()
        return f"Floors: {self.floors}, Name of owner: {self.name}, average height: {self.avera():.2f}"
    def avera(self):
        if self.floors > 0:
            return self.height / self.floors 
        return 0

def find_biggest(houses):
    if not houses:
        return None
    return(max(houses, key=lambda house:house.avera()))
    

house1 = House(20, 10, "Atanas Kolev", 3, "Pavel Kolev")
house2 = House(20, 15, "Atanas KRatunov", 4, "Danas")
house3 = House(25, 16, "Studenstki", 5, "Martin" )
houses = [house1, house2,house3]
biggest_house = find_biggest(houses)

print("All houses:")
for house in houses:
    house.print_out()

print(biggest_house)
        
