# Check if a number is a multiple of 3. If it is, also check if it's a multiple of 7
# You divide your number by 3 and if the remainder of your division is 0 this means the number ia a multiple of 3
# example: if we divide 6 by 3 and the remainder of the division which is denoted by the modulus symbol
# if that has the value of 0 then it's a multiple of 3   6/3 = 2  6 % 3 = 0
# A number not a multiple of 3: 10 /3 = 3.000 10 % 3 = 2 which os a non zero number
# 21 is a 
print("Enter a number: ")
number = int(input())
#number = 15
if number % 3 is 0:
    print("Number is a multiple of 3")
    if number % 7 is 0:
        print("Number is also a multiple of 7")
    else:
        print("Number is a multple of 3, but not a mutiple of 7")
