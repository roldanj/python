# my_variable="hello"
#
# # Bad Code
# print("****** BAD CODE *******")
# print("print(my_variable[0])")
# print("print(my_variable[1])")
# print("print(my_variable[2])")
# print("print(my_variable[3])")
# print("print(my_variable[4])")
# print(" ")
# print(my_variable[0])
# print(my_variable[1])
# print(my_variable[2])
# print(my_variable[3])
# print(my_variable[4])
# print(" ")
#
#
# # Good Code
# print("******* GOOD CODE *******")
# print("for character in my_variable:")
# print("    print(character) ")
# for character in my_variable:  # my_variable is a new variable where for each loop it will equal the first then next
#                                # character my_string are iterables which are strings, list, sets, tuples, and more..
#     print(character)           # we run what's in the body and repeat
#
# print("")
# print("my_list =[1,2,3,4,5] ")
# print("for mynum in my_list: ")
# print("    print(mynum)")
# my_list =[1,2,3,4,5]
#
# for mynum in my_list:
#     print(mynum)
#
# # infinite loop unless we add the user inputn
# user_wants_number = True
# while user_wants_number == True:
#     print(10)
#     user_input = input("Should we print again? y/n ")
#     if user_input == 'n':
#         user_wants_number = False


# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")
#
# if person in known_people:
#     print("You know {}".format(person))
# else:
#     print("You don't know {}!".format(person))


#
# # Modify the method below to make sure only even numbers are returned.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def even_numbers():
#     evens = []
#     for number in numbers:
#         if number % 2 == 0:
#             evens.append(number)
#     return evens
#
# print(even_numbers())


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def odd_numbers():
    odds = []
    for number in numbers:
        if number % 5 == 1 :
            odds.append(number)
    return odds

print(odd_numbers())


#
# # Modify the below method so that "Quit" is returned if the choice parameter is "q".
# # Don't remove the existing code
def user_menu(choice):
    if choice == "a":
        return "Add"
    elif choice == "q":
        return "Quit"











