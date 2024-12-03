hora = int(input("Броя на хора е: "))
godini = []
godininad18=[]
godinipod18 = []
for i in range(hora):
    godina = int(input("Vuvedete godina na choveka: "))
    godini.append(godina)

for godina in godini:
    if godina == 0 or godina < 18:
        godinipod18.append(godina)
    else:
        godininad18.append(godina)

broi_deca = len(godinipod18)
broi_golemi = len(godininad18)
if broi_golemi>0:
    sredna = sum(godininad18) / broi_golemi 
else:
    sredna = 0


print(godinipod18)
print(godininad18)
print(f"Count of childer: {broi_deca}")
print(f"Count of adults: {broi_golemi}")
print(f"Average age if adult: {sredna}")