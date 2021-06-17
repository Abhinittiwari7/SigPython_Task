print("Abhinit tiwari 1900300100003")


class Student:
    def __init__(self, roll,name):
        self.roll=roll
        self.name=name

    def display(self):
        print(f"Name = {self.name}\nRoll No = {self.roll}\nAge = {self.age}\nMarks = {self.marks}")

    def setAge(self):
        self.age=int(input("Enter your age : "))

    def setMarks(self):
        self.marks=int(input("Enter your marks : "))

student1 = Student(25, "Abhinit")
student1.setAge()
student1.setMarks()
student1.display()
