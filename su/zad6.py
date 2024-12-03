import random

randlist = []
n = int(input("Enter count: "))

for i in range(n):
    randlist.append(random.randint(1,100))

print(randlist)