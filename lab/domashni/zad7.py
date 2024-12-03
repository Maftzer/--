n = int(input("Vuvedete broi imena: "))
unique = set()
for i in range(n):
    imena = input()
    unique.add(imena)

print(" ".join(unique))