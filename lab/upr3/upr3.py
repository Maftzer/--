# s = [1 , 3, 5, 7]
# print(s[1])
# s[1] = 11
# print(s[1])


#добавяне с функия append()
# s = []
# s.append(5)
# s.append(10)
# s.append(20)
# print(s)

#зареждане на списък с for цикъл
# A = list(k for k in range (1,21) if k %3!=0 )
# print(A)

# списък за само двуцифрени числа
# B = list( x for x in range(1,31) if x > 9 )
# print(B)

#обръщане на стойностите с -1 и сечение на списъка
# s = [1,2,3,4,5,6]
# print(s[::-1]) #извежадме елементи в обратен ред
# print(s[:-1])  #принтираме без последния ред
# print(s[1:])   #принтираме без първия елемент
# print(s[0:2])  #първите два елемента
# print(s[-1:])  #последния елемент

#многомерен списък
# s = [[1,2,3,4] , ['a', 'b', 'c'], [10,20]]
# print(s[0][3])
# print(s[2][0])

#обжождане на списък с for
# s = [1,2,3,4,5,6]
# for i in s:
#     print(i, end=' ')

#обжождане на списък с range
# s = [1,2,3,4,5,6]
# for i in range(len(s)) : 
#     print(s[i], end= ' ')

#nz
# s = [2,4,6,8]
# print (4 in s) # True

#count, index, min, max
# s = [2,4,6,8,2]
# print(s.count(2)) # 2, дава боря на елемента
# print(s.index(3)) #ValueError: 3 is not in list, дава индекса на елемента
# print(min(s)) # 2, минимална стойност
# pirnt(max(s)) # 8, макс стойност

# s = [2,4,6,8,2]
# s.append(22) #добавя в края на списъка 22
# print(s)
# s+= [44,88] # добавя в края 44,80
# print(s)
# s.insert(0,90) #вкарва 90 преди първия елемент
# print(s)
# s.pop(0) #изтрива първия елемент
# print(s)
# s.remove(2) #изтрива елемента със стойност 2
# print(s)
# del s[4] # премахва елемент с индекс 4

# shuffle, choice (трябва да има random) и reverse
# s=[2,4,6,8,2]
# random.shuffle(s) #разбърква
# print(s)
# print(random.choice(s)) #зибира рандом и принтира
# s.reverse() #обръща реда наобратно
# print(s)

# s=[45, 10, 55, 5, 35]
# s.sort()
# print(s)    #[5,10,35,45,55]
# s.sort(reverse=True)
# print(s)    #[55,45,35,10,5]
# s1 = ['s', 'T', 'a', 'E', 'f']
# s1.sort(key=str.lower) #[a , E, f, s, T]
# print(s1)
# s1.sort()              #[E, T, a, f, s]
# print(s1)


#кортежи
# k = (7, 5, 3)
# print(k)

# tup = tuple([10,20,30]) # преубразуване списък в кортеж
# print(tup)
# tup1 = tuple('python')  # преубразуване на низ в кортеж
# print(tup1)
# tup2 = tuple            # празен кортеж


# k = (7, 5, 3, 6, 1)
# print(k[0])     #достъп до елемент по индекс
# print(k[2:3])   #сечение
# print(7 in k)   #проверка за наличие на елемент
# print(k * 3)    #повторение
# tup = k +(2,4)  #конкатенация
# print(tup)

# tup = (7,5,3,6,1)
# tup.index(1)    # 4
# tup.count(5)    # 1

#обхождане на елементи в кортеж
# for i in tup:
#     print(i, end= ' ')


#dict(<ключ1>=<стойност1>,...,<ключ n>=<стойност n>)
#dict(<списък с кортежи от по два елемента- ключ и стойност>)
# d = dict()
# d1= dict(name='ivan', last_name='petrov')
# d3 = dict([('name', 'polina'), ('l_name', 'koleva')])
# print(d3)
# print(d1)

# d = {'name': 'ivan', 'last_name': 'ivanov'}
# print(d['fname'])   #KeyError: 'fname'

# b = 'fname' in d

# del d['s_name']
# print(d)    #{'name':'ivan',''last_name':'ivanov'}

# for keys in d.keys():
#     print("( {0} => {1})".format(key,d[key]), end= ' ')
#     #(name => ivan)(last_name=>ivanov)

#за сортиране на речник трябва да се превърне в списък
# keys = list(d.keys())
# keys.sort()
# for key in keys:
#     print("{0} => {1}".format(key,d[key]), end=' ')
#     # last_name => ivanov name => ivan

#множество - функията set()
# s = set([1,2,3,1])  #list
# print(s)
# s2 = set("hello")   #string

# s2 = set("hello")
# for i in s2:
#     print(i, end=' ')

# print(len(s2))  #4

#обединение - има само уникални елементи
# s = set([1,2,3])
# s1 = set([4,2,6])
# s3 = s | s1
# print(s3)   #{1,2,3,4,6}

# s = set([1,2,3,4])
# s1 = set([2,4,6])
# s2 = s-s1 #1,3
# s3 = s1-s #6

# s4 = s & s1 # сечение, принтира само еднаквите
# print(s4)

# s5 = s ^ s1 #връша елементите, без еднаквите

#add(<element>) dobavq element
#remove(<element>) maha element, ako go nqma dava greshka
#discard(<element>) premahwa element, ako go nqma ne dava greshka
#pop() - premahva random element
#clear() - izchistva mnojectsvo

# s1 = set([2, 4, 6])
# s1.add(8)
# print(s1)       #{8,2,4,6}
# s1.remove(2)    #{8,4,6}
# print(s1)
# # s1.remove(2)    #KeyError: 2
# s1.discard(4)
# print(s1)
# s1.pop()
# print(s1)
# s1.clear()
# print(s1)

nums = [1,1,2]
chislo = 2
last_index = len(nums) - 1
for i in nums:
    while last_index != i:
        if chislo == nums[i]: 
            nums.pop(i) 
print(nums)





