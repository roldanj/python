
# Read the names and marks of at least 3 students
# Rank the top three students with the highest marks
# Give cash rewards. $500 for first rank, $300 for second rank and $100 for third rank. Value cannot be modified
# Appreciate students who secured 950 marks and above

import operator

def readStudentDetails():
    print()
    # { 'John': 600, 'Ben': 800, 'David': 950, 'Mark': 980 }
    print("Enter the number of students: ")
    try:
        numberOfStudents = int(input())
    except ValueError:
        print("Enter a Number value only!")
    studentRecord = {}
    for student in range(0, numberOfStudents):
        print("Enter the Name of the Student: ")
        name = input()
        print("Enter the marks of students: ")
        marks = int(input())
        studentRecord[name] = marks
    print()
    return studentRecord


def rankStudents(studentRecord):
    try:
        print()
        sortedStudentRecord = sorted(studentRecord.items(), key=operator.itemgetter(1), reverse=True)
        print(sortedStudentRecord)
        print("{} has secured first rank, scoring {} marks".format(sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
        print("{} has secured second rank, scoring {} marks".format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
        print("{} has secured third rank, scoring {} marks".format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
        print()
        return sortedStudentRecord
    except IndexError:
        print("Enter a minimum of 3 students")
        quit()  # this will end the program

def rewardStudents(sortedStudentRecord, reward):
    print()
    # reward index is pulled from the reward tuple on line 68
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[0][0], reward[0]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[1][0], reward[1]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[2][0], reward[2]))
    print()

def appreciateStudents(sortedStudentRecord):
    print()
    # Run a loop and check if the value or the mark from the student is Greater than or equal to 950
    # if it's is the send a message of appreciation
    for record in sortedStudentRecord:
        # [('Mark', 980), ('David', 950), ('Ben', 800), ('John', 600)]
        if record[1] >= 950:# First enter the marks at index position 1 then enter the name of the student at position 0
            print("Congratulations on scoring {} marks, {}".format(record[1], record[0]))
        else:  # for all marks that are less than 950 just break
            break
    print()


# We add  a return sortedStudentRecord  (line 37)
studentRecord = readStudentDetails()
sortedStudentRecord = rankStudents(studentRecord)
# When the value can't be modified it has to be a tuple
# create a tuple called reward and assign it the three reward amount
reward = (500, 300, 100)
# Next we Call the rewardStudents Function and we need the 'sortedStudentRecord' since we need the top 3 students
# We need to pass the sortedStudentRecord as a parameter from (line 31)
# sortedStudentRecord is part of the rankStudentRecord which cannot be access outside the function
# So lets first return the sortedStudentRecord (line 37) and when we return it from the function we need to have
# a variable that calls the return value.. sortedStudentRecord holds the values (line 75) and we also need to pass is
#the tuple 'reward' so the top tuple student can be rewarded
rewardStudents(sortedStudentRecord, reward)
# in the rewardStudents function accept those as parameters as well (line 42)

# Finally lets call the appreciateStudent Function and pass the sortedStudentRecord
# and in the function you receive it by adding it to the parameter (line 50)
appreciateStudents(sortedStudentRecord)