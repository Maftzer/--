class NumericList:
    def __init__(self, input_list):
        self.numeric_list = [item for item in input_list if isinstance(item, (int, float))]

    def show_list(self):
        print("Съдържание на списъка:", self.numeric_list)

    def calculate_average(self):
        if not self.numeric_list:
            print("Списъкът е празен. Средна стойност не може да се изчисли.")
            return None
        return sum(self.numeric_list) / len(self.numeric_list)

input_data = [10, 'текст', 15.5, True, 3, [1, 2, 3], None, 8]
obj = NumericList(input_data)
obj.show_list()  

average = obj.calculate_average()  
print("Средна стойност на елементите:", average)
