from math import *
import time
import os
import sys

#float has decimal
#Integers Doesn't Have Decimal

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    clr()
    logo = """"
       \033[93m_________    __   __________ \033[94m  ______
      \033[93m/ ____/   |  / /  / ____/  _/ \033[94m /_  __/
     \033[93m/ /   / /| | / /  / /    / ____\033[94m__/ /
    \033[93m/ /___/ ___ |/ /__/ /____/ /____\033[94m_/ /
    \033[93m\____/_/  |_/_____\____/___/    \033[94m/_/
     \033[93m                           \033[94mV1.0
     By Yash And Yuvi....
    """
    print(logo)
    print("Welcome To Calci Terminal...")
    print("Lets Start Calculating")

def addition_start():
    try:
        clr()
        banner()
        print("We Are On Addition..")
        N1 = input("Enter A Number: ")
        N2 = input("Enter Second Number: ")
        result = float(N1) + float(N2)
        print("The Answer Is " + result)
        qw = print(int(result))
        print("Approx Value Is " + qw)

    except ValueError:
        print("Invalid Entry")

def addition_tuto():
    clr()
    banner()
    print("We Are On Addition..")
    print("Enter A Number: ")
    time.sleep(1)
    clr()
    banner()
    print("We Are On Addition..")
    print("Enter A Number: 2")
    print("Enter Another Number: ")
    time.sleep(1)
    clr()
    banner()
    print("We Are On Addition..")
    print("Enter A Number: 2")
    print("Enter Another Number: 2")
    print("The Anwer Is 4")
    print()
    print("This Was The Tutorial...")
    print("Lets Start Calculating..")
    input("Press Enter To Begin..")
    addition_start()

def addition():
    banner()
    print("1.Tutorial")
    print("2.Start")
    op = input("Choose Your Desired Option: ")
    if op == 1 :
        addition_tuto()
    elif op == 2 :
        addition_start()
    else:
        print("Invalid Option")
        print("Thanks For Using Calci Terminal")

def substraction_start():
    try:
        clr()
        banner()
        print("We Are On Substraction..")
        N1 = input("Enter A Number: ")
        N2 = input("Enter Second Number: ")
        result = float(N1) - float(N2)
        print("The Answer Is " + result)
        qw = print(int(result))
        print("Approx Value Is " + qw)
    except ValueError:
        print("Invalid Entry")

def substraction_tuto():
    clr()
    banner()
    print("We Are On Substraction..")
    print("Enter A Number: ")
    time.sleep(1)
    clr()
    banner()
    print("We Are On Substraction..")
    print("Enter A Number: 2")
    print("Enter Another Number: ")
    time.sleep(1)
    clr()
    banner()
    print("We Are On Substraction..")
    print("Enter A Number: 2")
    print("Enter Another Number: 2")
    print("The Anwer Is 0")
    print()
    print("This Was The Tutorial...")
    print("Lets Start Calculating..")
    input("Press Enter To Begin..")
    substraction_start()

def substraction():
    clr()
    banner()
    print("1.Tutorial")
    print("2.Start")
    op = input("Choose Your Desired Option: ")
    if op == 1:
        substraction_tuto()
    elif op == 2:
        substraction_start()
    else:
        print("Invalid Option")
        print("Thanks For Using Calci Terminal")

def Multiplication_start():
    try:
        clr()
        banner()
        print("We Are On Multiplication..")
        N1 = input("Enter A Number: ")
        N2 = input("Enter Second Number: ")
        result = float(N1) * float(N2)
        print("The Answer Is " + result)
        qw = print(int(result))
        print("Approx Value Is " + qw)
    except ValueError:
        print("Invalid Entry")

def Multiplication_tuto():
    clr()
    banner()
    print("We Are On Multiplication..")
    print("Enter A Number: ")
    time.sleep(1)
    clr()
    banner()
    print("We Are On Multiplication..")
    print("Enter A Number: 2")
    print("Enter Another Number: ")
    time.sleep(1)
    clr()
    banner()
    print("We Are On Multiplication..")
    print("Enter A Number: 2")
    print("Enter Another Number: 2")
    print("The Anwer Is 4")
    print()
    print("This Was The Tutorial...")
    print("Lets Start Calculating..")
    input("Press Enter To Begin..")
    Multiplication_start()

def Multiplication():
    clr()
    banner()
    print("1.Tutorial")
    print("2.Start")
    op = input("Choose Your Desired Option: ")
    if op == 1:
        Multiplication_tuto()
    elif op == 2:
        Multiplication_start()
    else:
        print("Invalid Option")
        print("Thanks For Using Calci Terminal")

def Division_start():
    try:
        clr()
        banner()
        print("We Are On Division..")
        N1 = input("Enter A Number: ")
        N2 = input("Enter Second Number: ")
        result = float(N1) / float(N2)
        print(N1 + "/" + N2)
        time.sleep(1)
        print("The Answer Is " + result)
        qw = print(int(result))
        print("Approx Value Is " + qw)
    except ValueError:
        print("Invalid Entry")

def Division_tuto():
    clr()
    banner()
    print("We Are On Division..")
    print("Enter A Number: ")
    time.sleep(1)
    clr()
    banner()
    print("We Are On Division..")
    print("Enter A Number: 2")
    print("Enter Another Number: ")
    time.sleep(1)
    clr()
    banner()
    print("We Are On Division..")
    print("Enter A Number: 2")
    print("Enter Another Number: 2")
    print("The Anwer Is 1")
    print()
    print("This Was The Tutorial...")
    print("Lets Start Calculating..")
    input("Press Enter To Begin..")
    Division_start()

def Division():
    clr()
    banner()
    print("1.Tutorial")
    print("2.Start")
    op = input("Choose Your Desired Option: ")
    if op == 1:
        Division_tuto()
    elif op == 2:
        Division_start()
    else:
        print("Invalid Option")
        print("Thanks For Using Calci Terminal")

def squaring():
    try:
        def square(num):
            return num * num

        print("You Are On Squaring A Number")
        x = float(input("Enter The Number You Want To Square: "))
        result = square(x)
        print("The Anwer is " + str(result))
    except ValueError:
        print("Invalid Entry")

def Square_tuto():
    clr()
    banner()
    print("You Are On Squaring Numbers..")
    print("Enter the number to square: ")
    time.sleep(1)
    clr()
    banner()
    print("You Are On Squaring Numbers..")
    print("Enter the number to square: 2")
    print("The Anwer Is 4")
    print()
    print("This Was The Tutorial...")
    print("Lets Start Calculating..")
    input("Press Enter To Begin..")
    Squaring()

def Square1():
    clr()
    banner()
    print("1.Tutorial")
    print("2.Start")
    op = input("Choose Your Desired Option: ")
    if op == 1:
        Square_tuto()
    elif op == 2:
        Squaring()
    else:
        print("Invalid Option")
        print("Thanks For Using Calci Terminal")

def square_root_start():
    try:
        clr()
        banner()
        print("We Are On Finding Square root..")
        N1 = input("Enter the number to find square root \n The Number is: ")
        result = sqrt(N1)
        print("The Answer Is " + (result))
        qw = print(int(result))
        print("Approx Value Is " + qw)
    except ValueError:
        print("Invalid Entry")

def square_root_tuto():
    clr()
    banner()
    print("We Are On Finding Square root..")
    print("Enter the number to find square root \n The Number is: ")
    time.sleep(1)
    clr()
    banner()
    print("We Are On Finding Square root..")
    print("Enter the number to find square root \n The Number is: 4")
    time.sleep(1)
    clr()
    banner()
    print("We Are On Finding Square root..")
    print("Enter the number to find square root \n The Number is: 4")
    print("The Anwer Is 2")
    print()
    print("This Was The Tutorial...")
    print("Lets Start Calculating..")
    input("Press Enter To Begin..")
    square_root_start()

def square_root():
    clr()
    banner()
    print("1.Tutorial")
    print("2.Start")
    op = input("Choose Your Desired Option: ")
    if op == 1:
        square_root_tuto()
    elif op == 2:
        square_root_start()
    else:
        print("Invalid Option")
        print("Thanks For Using Calci Terminal")

def cube_start():
    try:
        clr()
        banner()
        def find_cube(num):
            return num*num*num
        x = float(input("Enter The Number You Want To Cube: "))
        y = float(x)
        result = print(find_cube(y))
        print("The Answer Is " + (result))
        qw = print(int(result))
        print("Approx Value Is " + qw)
    except ValueError:
        print("Invalid Entry")

def cube_tuto():
    clr()
    banner()
    print("We Are On Finding cube..")
    print("Enter the number: ")
    time.sleep(1)
    clr()
    banner()
    print("We Are On Finding cube..")
    print("Enter the number: 2")
    time.sleep(1)
    clr()
    banner()
    print("We Are On Finding cube..")
    print("Enter the number: 2")
    print("The Anwer Is 8")
    print()
    print("This Was The Tutorial...")
    print("Lets Start Calculating..")
    input("Press Enter To Begin..")
    cube_start()

def cube():
    clr()
    banner()
    print("1.Tutorial")
    print("2.Start")
    op = input("Choose Your Desired Option: ")
    if op == 1:
        cube_tuto()
    elif op == 2:
        cube_start()
    else:
        print("Invalid Option")
        print("Thanks For Using Calci Terminal")

def cube_root_start():
    try:
        def cube_root1():
            try:
                x = int(input("Enter the number: "))
                if x > 0:
                    ans = x ** (1. / 3.)
                    if ans ** 3 != abs(x):
                        print(x, 'is not a perfect cube!')
                else:
                    ans = -((-x) ** (1. / 3.))
                    if ans ** 3 != -abs(x):
                        print(x, 'is not a perfect cube!')
                print('Cube root of ' + str(x) + ' is ' + str(ans))
                print(str(x) + " Is A Perfect Cube")
                def is_perfect_cube(x):
                    x = abs(x)
                    return int(round(x ** (1. / 3))) ** 3 == x
                print(is_perfect_cube(x))
            except ValueError:
                print("Invalid Entry")
        cube_root1()
    except ValueError:
        print("Invalid Entry")

def cube_root_tuto():
    clr()
    banner()
    print("We Are On Finding cube root..")
    print("Enter the number: ")
    time.sleep(1)
    clr()
    banner()
    print("We Are On Finding cube root..")
    print("Enter the number: 8")
    time.sleep(1)
    clr()
    banner()
    print("We Are On Finding cube..")
    print("Enter the number: 8")
    print("Cube Root of 8 Is 2")
    print()
    print("This Was The Tutorial...")
    print("Lets Start Calculating..")
    input("Press Enter To Begin..")
    cube_root_start()

def cube_root():
    clr()
    banner()
    print("1.Tutorial")
    print("2.Start")
    op = input("Choose Your Desired Option: ")
    if op == 1:
        cube_root_tuto()
    elif op == 2:
        cube_root_start()
    else:
        print("Invalid Option")
        print("Thanks For Using Calci Terminal")

banner()
print("Choose What You Want To Do..")
print("1.Addition(+)  2.Substract(-)     3.Multiply(X)    ")
print("4.Division(/)  5.Square(X²)       6.SquareRoot(2√X) ")
print("7.Cube(X³)     8.CubeRoot(3√X)    9.Exit()")
print()
op = input("Enter What You Want To Do: ")

if op == 1 or "+" :
    addition()

elif op == 2 or "-" :
    substraction()

elif op == 3 or "*" :
   Multiplication()

elif op == 4 or "/" :
    Division()

elif op == 5 :
    square1()

elif op == 6 :
    square_root()

elif op == 7 :
    cube()

elif op == 8 :
    cube_root()

elif op == 9 :
    banner()
    print("Thanks For Using Calci Terminal")
    print("We Hope To See You Again")
    exit()

else:
    banner()
    print("Thanks For Using Calci Terminal")
    print("We Hope To See You Again")
