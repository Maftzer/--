def palindrom():
    chislo = int(input("Vuvedete chislo: "))
    chislo_str = str(chislo)
    if chislo_str == chislo_str[::-1]:
        return 1
    else:
        return 0

print(palindrom())