class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

classmate = Student("Jerry", "WeberState")
classmate.marks.append(99)
classmate.marks.append(71)
classmate.marks.append(67)
classmate.marks.append(100)
classmate.marks.append(45)
classmate.marks.append(89)
classmate.marks.append(89)

print(classmate.marks)
print(classmate.average())