
fig = int(input("Vuvedete vid figura(1 - Kvadrat, 2 - Pravougulnik, 3 - prav. triugulnik): "))
def kvadrat():
        strana = int(input("Vuvedete razmer na strana: "))
        lice = strana * strana
        print(f"Liceto na kvadrata e: {lice}")
        return
def prav():
        strana = int(input("Vuvedete razmer na purvata strana: "))
        lice = strana
        strana = int(input("Vuvedete razmer na vtorata strana: "))
        lice *= strana
        print(f"Liceto na pravougulnika e: {lice}")
        return
def tri():
        strana = int(input("Vuvedete razmer na purvata strana: "))
        lice = strana
        strana = int(input("Vuvedete razmer na vtorata strana: "))
        lice = (lice * strana) / 2
        print(f"Liceto na triugulnika e: {lice}")
        return
if fig == 1:
    kvadrat()

elif fig == 2:
    prav()

elif fig == 3:
    tri()
    
else:
    print("Nqma takava figura")