class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def friend(self, friend_name):
        return Student(friend_name, self.school)

jerry = Student("Lisa", "MSU")
friend = jerry.friend("Albert")
print("friend.name: " + friend.name)
print("friend.school: " + friend.school)
# Returns
# Albert
# MSU
#[99, 71, 67, 100, 45, 89, 89]
# 80.0


# covering inheritance i the class workingStudent contains all of the stuff that Student contains
# Thsi is laike a copy and paste of line 1 thru 11

# When we inherit that does not mean cloning
class workingStudent(Student):
    # we can re-implement the init method with more stuff..
    def __init__(self, name, school, salary):
        # we can call the  class init method which adds the Student super class

        super().__init__(name, school)

        self.salary = salary



# to test this add the following and workingStudent works the same as Student and we add the salary
jerry = workingStudent("Lisa", "MSU", 20.00)



print("class workingStudent friend.name: " + friend.name)
print("class workingStudent friend.school: " + friend.school)
# Returns
# Albert
# MSU
print("")
# Print the salary
print("class workingStudent - jerry.salary: ")
print(jerry.salary)


# Test if the friend has a salary
# print(friend.salary)

classmate = Student("Jerry", "WeberState")
classmate.marks.append(99)
classmate.marks.append(71)
classmate.marks.append(67)
classmate.marks.append(100)
classmate.marks.append(45)
classmate.marks.append(89)
classmate.marks.append(89)
print("")
print("classmate.marks.append()")
print(classmate.marks)
print("")
print("classmate.average()")
print(classmate.average())