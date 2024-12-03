import random

numbers = []
even = []
odd = []
for i in range(0,101):
    if i%2 == 0 or i%5 == 0:
        numbers.append(i)
        if i %2 == 0:
            even.append(i)
        else:
            odd.append(i)
numbers.reverse()
print(numbers)
print(even)
print(odd)




