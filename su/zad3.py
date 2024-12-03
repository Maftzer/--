duma = input("Vuvedete duma: ")
d = {}

unikalni = set(duma)

for char in unikalni:
    mod = duma.replace(char, "")
    d[char] = mod

print(d)