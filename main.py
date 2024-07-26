
from unittest import case

x = int(input('First Number: '))
y = int(input('Second Number: '))

print("""

    1 - Plus
    2 - Subtraction
    3 - Multiplication 
    4 - Division

""")

choise = int(input("Choose the option bellow for make a count: "))

def plus(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

match choise:

    case 1:
        print(plus(x,y))

    case 2:
        print(subtraction(x,y))

    case 3:
        print(multiplication(x,y))

    case 4:
        print(division(x,y))
    
    case _:
        print("Invalid Code try again")


