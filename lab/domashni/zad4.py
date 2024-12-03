dumi = str(input("Vuvedete tekst: "))
if (" ") in dumi:
    prazno = dumi.count(" ") + 1
    prazni = dumi.replace(" ", "")
    print(prazni * prazno)
