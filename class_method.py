#  https://www.udemy.com/automated-software-testing-with-python/learn/v4/t/lecture/7736934?start=75

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    @staticmethod
    def go_to_school2():
        print("I'm going to school2")

    @classmethod
    def go_to_school(cls):
        print("I'm going to school")

classmate = Student("Jerry", "WeberState")
classmate.marks.append(99)
classmate.marks.append(71)
classmate.marks.append(67)
classmate.marks.append(100)
classmate.marks.append(45)
classmate.marks.append(89)
print(classmate.marks)
print(classmate.average())

Student.go_to_school()

Student.go_to_school2()