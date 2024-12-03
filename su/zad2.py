n = int(input("Начало на интервал: "))
m = int(input("Край на интервал: "))
chisla = []

for i in range (n, m+1):
    if i %3 == 0 or i%4 ==0:
        if i%3 ==0 and i%4 == 0:
            continue
        chisla.append(i)
print(chisla)