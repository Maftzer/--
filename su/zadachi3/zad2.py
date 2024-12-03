class OddNumbers():
    def __init__(self, value):
        self.value = value
    
def create_list(count):
    odd_objects = []
    for i in range(count * 2):
        if i % 2 != 0:
            odd_objects.append(OddNumbers(i))
    return odd_objects
    
value = int(input("Vuvedete broi nechetni chisla: "))
    
odd_list = create_list(value)

for obj in odd_list:
    print(obj.value)
    

