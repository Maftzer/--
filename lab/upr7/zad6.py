class TriangleChecker():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        try:
            if self.a < 0 or self.b < 0 or self.c <0:
                return "Нищо няма да работи с отрицателни числа"
            elif (self.a + self.b) > self.c and (self.b + self.c) > self.a and (self.a + self.c) > self.b:
                return "Ура, можете да построите триъгълник"
            elif (self.a + self.b) <= self.c or (self.b + self.c) <= self.a or (self.a + self.c) <= self.b:
                return "Жалко, но не можете да направите триугълник от това!"
        except ValueError:
            print ("Moje samo chisla")
    
a = int(input("vuvedete purvata strana: "))
b = int(input("Vuvedete vtorata strana: "))
c = int(input("vuvedete tretata strana: "))


triangle = TriangleChecker(a,b,c)

print(TriangleChecker.is_triangle(triangle))
