my_list = [0, 1, 2, 3, 4]

an_equal_list = [x for x in range(5)]
print(an_equal_list)
# Results: [0, 1, 2, 3, 4]

# Range(5) is a list that says [0, 1, 2, 3, 4]
# The 'x' in for 'x'  is going to be the first element of [0,
# we are going to put the for 'x' inside a list of [x
# We repeat this 5 times untin all the elements are in [x


multiply_list = [x * 3 for x in range(5)]
print(multiply_list)
# Results: [0, 3, 6, 9, 12]

print(8 % 3)

print(9 % 2)

print([n for n in range(10) if n % 2 == 0])
# Results: [0, 2, 4, 6, 8]


people_you_know = ["Rolf", ""]