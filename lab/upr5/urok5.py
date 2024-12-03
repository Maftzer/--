# class myFirstClass:
#     x=5



# myFirstObject = myFirstClass ()
# print(myFirstClass.x, end=" ") # може чрез класа и атрибута
# print(myFirstObject.x) # може и чрез обекта и атрибута

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# MyPerson=Person("Ivan", 35)
# print(MyPerson.name)
# print(MyPerson.age)
# del MyPerson.name
# print(MyPerson.name)
# del MyPerson
# print(MyPerson)

# class Car:
#     car_type="sports"
#     def __init__(self,color):
#         self.__color=color
#     def print_car(self):
#         print(self.__color, "\t", self.car_type)
#     def get_color(self):
#         return self.__color
#     def set_color(self,color):
#         self.__color=color
# car2 = Car("Yellow")
# car2.print_car()
# car2.__color= "black" # cant change private attribute value
# car2.print_car()
# print(car2.__color) # cant read private attribute outside in the class
# car2.set_color("green") # function setter
# print(car2.get_color()) # function getter
# car2.print_car()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greetings(self):
#         print("Hello, my name is " + self.name)
# MyPerson = Person("Ivan", 35)
# MyPerson.greetings()

# class FirstClass:
#     x = 5
# def FirstClassMethod():
#     print("This is class method")
# FirstClassMethod()

# class Person:
#     def __init__(self,fName,lName):
#         self.firstName=fName
#         self.lastName=lName
#     def printname(self):
#         print(self.firstName, self.lastName)
# my_input = input("Vuvedete ime i familiq: ")


# class Student(Person):
#     def __init__(self,fname,lname):
#         Person. __init__(self)




# class Student(Person):
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
person1 = Person ("polina", "koleva")
print(person1)