def my_print_method(my_argument):
    print(my_argument)

my_print_method("This is being passed to my argument")

def my_multiply_method(number_one,number_two):
    return number_one * number_two

result = my_multiply_method(20,7)
my_print_method(result)


print(my_multiply_method(5,3))

my_print_method(my_multiply_method(7,8))

