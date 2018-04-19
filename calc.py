# Now we are ready!!!!
def add(num1, num2):
    """"Returns num1 plus num1 """
    return num1 + num2


def sub(num1, num2):
    """Returns num1 minus num2"""
    return num1 - num2


def mul(num1, num2):
    """Returns num1 multiply by num2"""
    return num1 * num2


def div(num1, num2):
    """Returns num1 divide by num2"""
    return num1 / num2


def main():
    #for i in range(3):
    user_continue = True
    while user_continue:
        validInput = False
        while not validInput:
            try:
                num1 = int(input("What is number 1? "))
                num2 = int(input("What is number 2? "))
                operation = int(input("What do you want to do? (1. Add, 2, Subtract, 3. Multiply, or 4. Divide. Enter number: "))
                validInput = True
            except:
                print("Invalid Input the program will now exit.")

        if (operation == 1):
            print("Adding...")
            print(add(num1, num2))
        elif (operation == 2):
            print("Subtracting...")
            print(sub(num1, num2))
        elif (operation == 3):
            print("Multiplying...")
            print(mul(num1, num2))
        elif (operation == 4):
            print("Dividing...")
            print(div(num1, num2))
        else:
            print("I don't understand")
        user_yn = input('Would you like to run another calculation? ("y" for yes or any other value to exit')
        if(user_yn != 'y'):
            user_continue = False
            break
        else:
            continue
main()

