chisla = []
n = int(input("vuvedete broi chisla v spisuka: "))
for chislo in range (n):
    chislo = int(input("vuvedete chislo za spisuka: "))
    chisla.append(chislo)
number = int(input("Vuvedete chislo za proverqvane: "))
def proverka():
    for i in chisla:
        if chisla[i] > number:
            chisla[i] = 0
    return chisla
print(proverka())