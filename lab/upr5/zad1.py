class Person:
    def __init__(self,fname,lname,age,nationality):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.nationality = nationality
    def print_info(self):
        print(f"Ime: {self.fname}, Familia: {self.lname}, vuzrast: {self.age}, nacionalnost: {self.nationality}")

person1 = Person("Ivan", "Nikolov", 35, "bulgarin")
person1.print_info()

class Student(Person):
    def __init__(self,fname,lname,age,nationality, uni, yearofstudy):
        super().__init__(fname,lname,age,nationality)
        self.uni = uni
        self.yearofstudy = yearofstudy

    def print_info(self):
        super().print_info()
        print(f"Universtitet: {self.uni}, Godina na obuchenie: {self.yearofstudy}")

student1 = Student("Nikola", "Vasilev", 21, "bulgarin", "Tehnicheski Universitet", 2)
student1.print_info()

class Lecturer(Person):
    def __init__(self,fname,lname,age,nationality, uni, experience):
        super().__init__(fname,lname,age,nationality)
        self.uni = uni
        self.experience = experience
    
    def print_info(self):
        super().print_info()
        print(f"Universtitet: {self.uni}, Opit na obuchenie: {self.experience}")
lecturer1 = Lecturer("Boris", "Nachev", 50, "bulgarin", "Tehnicheski Universitet", 6)
lecturer1.print_info()

