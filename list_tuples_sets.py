#  How to create a list?
#  https://www.programiz.com/python-programming/list
#  In Python programming, a list is created by placing all the items (elements)
# inside a square bracket [ ], separated by commas.


my_list = ['p','r','o','b','e']
# Output: p
print(my_list[0])


#  tuple is similar to a list. The difference between the two is that we cannot
# change the elements of a tuple once it is assigned

# tuple with mixed datatypes
# Output: (1, "Hello", 3.4)
my_tuple = (1, "Hello", 3.4)
print(my_tuple)
# tuple with mixed datatypes
# Output: (1, "Hello", 3.4)
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# tuple can be created without parentheses
# also called tuple packing
# Output: 3, 4.6, "dog"

my_tuple = 3, 4.6, "dog"
print(my_tuple)



# A set is an unordered collection of items. Every element is unique (no duplicates)
# and must be immutable (which cannot be changed).

# set of integers
my_set = {1, 2, 3}
print(my_set)
# answer: {1, 2, 3}


# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
# answer: {1.0, 'Hello', (1, 2, 3)}

# set do not have duplicates
my_set = {1,2,3,4,3,2}
print(my_set)
# answer: {1, 2, 3, 4}

#  Python dictionary is an unordered collection of items.
# While other compound data types have only value as an element, a dictionary has a key: value pair.

# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])

my_dict = {'name':'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)


# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}

# remove a particular item
# Output: 16
print(squares.pop(4))


# Output: {2: 4, 3: 9, 5: 25}
print(squares)

# delete a particular item
del squares[5]

# Output: {2: 4, 3: 9}
print(squares)

print("*" * 100)

print(' ')
print("*" * 100)

# Calculate an average

grade_one = 77
grade_two = 80
grade_three = 90
grade_four = 95
grade_five = 100

print((grade_one + grade_two + grade_three + grade_four + grade_five) / 5)



# Or we can do it this way

grades=[77,80,90,95,100]

print(len(grades))  # get the count of elements
cnt = (len(grades))  # convert the count to a variable
print(sum(grades) / cnt)  # calculate the total equation

# in short

print(sum(grades) / len(grades))

# This is a tuple. the difference is.. a tuple is immutable meaning you can't increase in size like: grades.append(108)


grades = (77,80,90,95,107)
print(sum(grades) / len(grades))


# You can also have a set.. meaning unique & unordered
set_grades = {77,80,90,95,107} #  This would not be ok for a set {77,80,90,95,107,107}
print(set_grades)



grades = {67,78,90}  # unique & unordered


tuple_grades = (67,78,90)  # immutable
tuple_grades = tuple_grades + (100,) #  you must have a coma. We haven't changes it.. we calculated and added??
print(tuple_grades)
# Prints (67, 78, 90, 100)


grades = [67,78,90]
print(grades[0])  ## Prints the 0 position of the value
# Prints 67



grades = [67,78,90]
grades[0] = 60   # assigns a new value to the 0 position and prints the element
print(grades[0])
# prints


### set_grades = {77,80,90,95,107}  # unique & unordered
### set_grades[0] = 60 #  Since set doesn't have an order what will print? An error message!
# Prints the following error message: TypeError: 'tuple' object does not support item assignment
set_grades = {77,80,90,95,107}  # unique & unordered
set_grades.add(60)  # We can however add to a set
print(set_grades)




#tuple_grades = (67,78,90)  # immutable
#tuple_grades[0] = 60  # this will cause an exception
# print(tuple_grades)
# Prints the following error message: TypeError: 'tuple' object does not support item assignment




#  How do we check if your numbers matched?
your_lottery_numbers = {1,2,3,4,5,}
winning_numbers = {1, 3, 5, 7, 9, 11}

print(your_lottery_numbers.intersection(winning_numbers))
#     {1, 3, 5}
# or we can do it this way..

print(your_lottery_numbers.union(winning_numbers))
#     {1, 2, 3, 4, 5, 7, 9, 11}
# another technique..

print({1, 2, 3, 4}.difference({1, 2}))
#      {3, 4}




print("*" * 100)

print(' ')
print("*" * 100)

# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
my_list = [25, 25, 50]
print(sum(my_list))
# Create a tuple, called my_tuple, with a single value in it (Remember to add the comma!!!!!
my_tuple = (15,)
print(my_tuple)
# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}
print(set1.intersection(set2))

