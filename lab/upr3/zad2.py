import random

spisuk = []
n  = int(input("Vuvedete broi random chisla: "))
for i in range(n):
    spisuk.append(random.randint(1,100))
print(spisuk)
