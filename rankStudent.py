
import operator
def readStudentDetails():
    # {'John': 600, 'Ben': 800, 'David': 950, 'Mark': 900}
    print("Enter Number of Students: ")
    numberOfStudent = int(input())
    studentRecord = {}
    for student in range(0, numberOfStudent):
        print("Enter Student Name: ")
        name = input()
        print("Enter Student marks: ")
        marks = int(input())
        studentRecord[name] = marks
    return studentRecord

def rankStudents(studentRecord):

    sortedStudentRecord = sorted(studentRecord.items(), key=operator.itemgetter(1), reverse=True)

    print(sortedStudentRecord)
    print("{} has secured first rank, scoring {} marks".format(sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
    print("{} has secured second rank, scoring {} marks".format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
    print("{} has secured third rank, scoring {} marks".format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))



studentRecord = readStudentDetails()
rankStudents(studentRecord)