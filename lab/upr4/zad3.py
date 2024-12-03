print("Vuvedete izbor na deistvie")
print("1. Subirane")
print("2. Izvajdane")
print("3. Umnojenie")
print("4. Delenie")
choice = int(input())
def subirane():
        chislo1 = int(input("Vuvedete pyrvo chislo: "))
        chislo2 = int(input("Vuvedete vtoro chislo: "))
        sum = chislo1 + chislo2
        return sum
def izvajdane():
        chislo1 = int(input("Vuvedete pyrvo chislo: "))
        chislo2 = int(input("Vuvedete vtoro chislo: "))
        izv = chislo1 - chislo2
        return izv
def umnojenie():
        chislo1 = int(input("Vuvedete pyrvo chislo: "))
        chislo2 = int(input("Vuvedete vtoro chislo: "))
        mult = chislo1 * chislo2
        return mult
def delenie():
        chislo1 = int(input("Vuvedete pyrvo chislo: "))
        chislo2 = int(input("Vuvedete vtoro chislo: "))
        if chislo1 == 0:
            print("Ne moje da se deli na 0")
            return
        dele = chislo1 / chislo2
        return dele
        print(f'Rezultat: {delenie()}')
        
if choice == 1:
    print(f'Rezultat: {subirane()}')
elif choice == 2:
    print(f'Rezultat: {izvajdane()}')
elif choice == 3:
    print(f'Rezultat: {umnojenie()}')
elif choice == 4:
    delenie()
