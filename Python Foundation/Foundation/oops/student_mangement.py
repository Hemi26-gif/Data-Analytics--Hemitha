class Student:
    def __init__ (self,name,id,dept,marks,attendance):
        self.name = name
        self.id = id
        self.dept = dept
        self.marks = 0
        self.attendance = 0
    def display(self):
        return f" Name: {self.name}\n id: {self.id}\n dept: {self.dept}\n marks: {self.marks}\n attendance: {self.attendance}"
    def avg(self):
        average_mark = (sum(self.marks)/len(self.marks))
        return average_mark

std1 = Student("Abinaya","CS101","CSE",[83,78,67],0)
std2 = Student("Bharath","IT104","IT",[73,98,69],0)
std3 = Student("chanda","EC109","ECE",[93,86,79],0)
std4 = Student("Rihana","EE130","EEE",[87,70,65],0)
std5 = Student("Gokul","ME121","MECH",[80,59,61],0)

print(std2.average_mark())


