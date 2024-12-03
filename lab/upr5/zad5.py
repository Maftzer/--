class Aritmetika:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def print_numbers(self):
        print(f"Стойността на  първото числото е {self.number1}")
        print(f"Стойността на  второто числото е {self.number2}")
    def sum(self):
        return self.number1 + self.number2
    def diff(self):
        if self.number1 >= self.number2:
            return self.number1 - self.number2
        else:
            return self.number2 - self.number1
    def mult(self):
        return self.number1 * self.number2
    def dele(self):
        if self.number2 == 0:
            print("Ne moje da se deli na nula")
        else:
            return self.number1 / self.number2
chisla = input("Въведете две числа, разделени с интервал: ")


chisla1, chisla2 = map(int, chisla.split())


num_obj = Aritmetika(chisla1, chisla2)

num_obj.print_numbers()  

print(f"Сумата е: {num_obj.sum()}")
print(f"Разликата е: {num_obj.diff()}")
print(f"Произведението е: {num_obj.mult()}")
num_obj.dele()



