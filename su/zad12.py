import random

n = int(input("Vuvedete N: "))
m = int(input("Vuvedete M: "))
matrix = [[random.randint(0,100) for k in range(m)] for k in range(n)]

print("Originalnata matrica")
for row in matrix:
    print(row)

row_del = int(input(f"Въведете номер на ред за изтриване(От 0 до {n - 1}) "))
col_del = int(input(f"Въведете номер на колона за изтриване(От 0 до {m - 1}) "))

matrix.pop(row_del)

for row in matrix:
    row.pop(col_del)

print("Резултатите от действията: ")
for row in matrix:
    print(row)