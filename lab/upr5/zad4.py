class Number:
    def __init__(self,value):
        self.value=value
    def print_value(self):
        print(f"Стойността на числото е {self.value}")
    def square(self):
        return self.value**2
    def cube(self):
        return self.value**3
number = int(input("vuvedete chislo: "))
num_obj = Number(number)
num_obj.print_value()

print(f"Числото на втора степен е: {num_obj.square()}")
print(f"Числото на трета степен е: {num_obj.cube()}")
