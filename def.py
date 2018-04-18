#
# # Make a list called known_people with 3 names
# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")
#
# if person in known_people:
#     print("You know {}".format(person))
# else
#     print("You do not know {}".format(person))


def who_do_you_know():
    people = input("Enter the names of people you know separated by commas: ")  #  John,Rolf,Anna,Greg 1
    people_list = people.split(",") # ["John", "Rolf", "Anna", "Greg"]  2
    people_without_spaces = []  # 3
    return people_list  #  4

    for person in people_list:
         people_without_spaces.append(person.strip())
    return people_without_spaces





def ask_user():
    person = input("Enter a person name you know: ")  # 5
    people = who_do_you_know()  #6
    if person in people: #  7
        print("Hey you know {}".format(person))





ask_user()