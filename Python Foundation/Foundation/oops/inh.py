class Person:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def display_role(self):
        return "University person"

class Student(Person):
    def __init__(self,name,email,dept):
        super().__init__(name,email)
        self.dept = dept
    def display_role(self):
        return "Student"

class Teacher(Student):
    def __init__(self,name,email,dept,subj):
        super().__init__(name,email,dept)
        self.subj = subj
    def display_role(self):
        return "Teacher"

std1 = Student("Hemitha","abs@gmail.com","CSE")
per1 = Person("Ashok","ashok@gmail.com")
tch1 = Teacher("Mallika","mkk@gmail.com","CSE","ds")
print(std1.display_role())
print(tch1.display_role())


#polymorphism
# class Animal:
#     def sound(self):
#         return "Any sound"

# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# class Bird(Animal):
#     def sound(self):
#         return "sing"

# bird1 = bird()
# print(bird1.Bird())