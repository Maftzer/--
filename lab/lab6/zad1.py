class Building:
    def __init__(self, height, area, adress):
        self.height = height
        self.area = area
        self.adress = adress
    def print_out(self):
        pass
class House(Building):
    def __init__(self, height, area, adress, floors, owner):
        super().__init__(height, area, adress)
        self.floors = floors
        self.owner = owner
    def print_out(self):
        return f"Height: {self.height}m., Area: {self.area}m^2, Adress: {self.adress}, Average height: {self.average():.2f}m., Floors: {self.floors}, Owner: {self.owner}"
    
    def average(self):
        if self.floors > 0:
            return self.height / self.floors
        return 0
    
def find_biggest_house(houses):
    if not houses:
        return None
    return max(houses, key = lambda house: house.average())

house1 = House(30, 125, "Sofia, Studenski grad, 54 blok", 4, "Danail")
house2 = House(25, 150, "Sofia, Lulin 8", 3, "Pavel")
house3 = House(45, 125, "Yambol, 5 Yanuari 22", 5, "Martin")

houses = [house1, house2, house3]

biggest_house = find_biggest_house(houses)

print("All Houses")
for house in houses:
    print(house.print_out())


print(f"The biggest house is: {biggest_house.print_out()}")


        
        