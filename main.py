# https://www.youtube.com/watch?v=-4tA5PAH9uU
def add(num1, num2):
    """Returns num1 plus num2."""
    return num1 + num2


def sub(num1, num2):
    """Returns num1 minu num2."""
    return num1 - num2

def mul(num1, num2):
    """Returns num1 multiply num2."""
    return num1 * num2

def div(num1, num2):
    """Returns num1 divide num2."""
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Can't do that! Zero exception error!")

def runOperation(operation, num1, num2):
    """Determine the operation to run based on the
    operation argument which should pass in as an int"""


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
        print("WTF???")
        print("I don't understand")


def main():
    #for i in range(3): # index for loop doesn't work
        user_continue = True
        while user_continue:
            validInput = False
            while not validInput:
                # Get user input
                try:
                    num1 = int(input("What is number 1?  "))
                    num2 = int(input("What is number 2?  "))
                    operation = int(input("What do you want to do? (1. add, 2. subtract, 3. multiply, and  4. divide. "
                                          "Enter number: ) "))
                    validInput = True
                except ValueError:
                    print("Invalid input the program will now exit.")
                except:
                    print("Unknown Error")
            runOperation(operation, num1, num2)

            user_yn = input('Would you like to run another calculation? ("y" for yes or any other value to exit')
            if(user_yn != 'y'):
                user_continue = False
                break
            else:
                continue


main()










