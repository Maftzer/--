floors = int(input("Въведете броя на етажите: "))
results = []  
for i in range(1, floors+1):
    floor_info = (input((f"Въведете информация за етаж {i}: ")).split())
    rooms = floor_info[0].count("#")
    occupied = int(floor_info[1])
    waiting = int(floor_info[2])
    free_rooms = rooms - (occupied + waiting)
    if free_rooms > 0:
        results.append(f"Floor {i}: There are {free_rooms} free fitting rooms")
    elif free_rooms==0:
        results.append(f"Floor {i}: There are no free fitting rooms")
    elif free_rooms<0:
        free_rooms = -free_rooms
        results.append(f"Floor {i}: There are {free_rooms} people waiting")

for i in range(len(results)):
    print(results[i])
