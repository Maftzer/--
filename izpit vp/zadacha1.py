import random
while True:
    try:
        n = int(input("Vuvedete broi: "))
        if not 20 <= n <= 30:
            raise ValueError
        break
    except ValueError:
        print(f"Error: Trqvda da vuvedete chislo mejdu 20 i 30")

random_list = [random.randint(-100,100) for _ in range(n)]
print(f"Pruviq spisuk: {random_list}")


suma = sum(random_list[i] for i in range(1, len(random_list), 2) )

count = 0
mult = 1
for number in random_list:
    if number%2 == 0 and number %10 != 0:
        count +=1
    if number < 0 and number %2 == 0:
        mult *= number
        
print("Broq na chislata s edinici koito se delqt na 2: ", count)
print("Proizvedenieto na chislata, po-malki ot nula i chetni: ", mult)

print("az")

random_list1 = [item for item in random_list if item > n]

list_max = max(random_list1)
list_min = min(random_list1)

diff = list_max - list_min
    
print("Razlikata e: ", diff)

odd = [item for item in random_list1 if item %2 != 0]

broi = len(odd)

print("Broi na nechentnite chisla v spisuka: ", broi)

random_list1.remove(min(random_list1))

print("Noviq spisuk e: ", random_list1)

    