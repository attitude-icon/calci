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


banner()
print("0.Tables. \n1.Addition \n2.Substraction \n3.Multiplication \n4.Division")
print("5.Square \n6.Square Root \n7.Cube \n8.Cube Root \n9.Find Whether Perfect Cube")
OP = input("Enter your Choice: ")


if OP == "+" or "Add" or "add" or "1":
    num1 = float(input("Enter A Number: "))
    num2 = float(input("Enter Second number: "))
    result = num1 + num2
    print(result)

elif OP == "-" or "sub" or "Sub" or "2":
    num1 = float(input("Enter A Number: "))
    num2 = float(input("Enter Second number: "))
    result = num1 - num2
    print(result)

elif OP == "*" or "mul" or "Mul" or "3":
    num1 = float(input("Enter A Number: "))
    num2 = float(input("Enter Second number: "))
    result = num1 * num2
    print(result)

elif OP == "/" or "div" or "Div" or "4":
    num1 = float(input("Enter A Number: "))
    num2 = float(input("Enter Second number: "))
    result = num1 / num2
    print(result)

OP = zx
if zx == "5":
    try:
        def square(num):
            return num * num
        x = float(input("Enter The Number You Want To Square: "))
        result = square(x)
        print("The Anwer is " + str(result))
    except ValueError:
        print("Invalid Entry")

elif zx == "6":
    try:
        N1 = input("Enter the number to find square root \n The Number is: ")
        result = sqrt(N1)
        print("The Answer Is " + (result))
        qw = int(result)
        print("Approx Value Is " + str(qw))
    except ValueError:
        print("Invalid Entry")

elif zx == "7":
    try:
        def find_cube(num):
            return num * num * num
        x = float(input("Enter The Number You Want To Cube: "))
        y = float(x)
        result = print(find_cube(y))
        print("The Answer Is " + (result))
        qw = int(result)
        print("Approx Value Is " + str(qw))
    except ValueError:
        print("Invalid Entry")

elif zx == "8" :
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
    except ValueError:
        print("Invalid Entry")

elif zx == "9":
    try:
       def is_perfect_cube(x):
           x = abs(x)
           return int(round(x ** (1. / 3))) ** 3 == x
       print(is_perfect_cube(x))
    except ValueError:
        print("Invalid Entry")

elif zx == "0":
    print("Baki Sab Try Karna Kyu Idhar Tapak Raha Hai...")
else:
    print("Inavlid Input...")
    time.sleep(2)
    clr()
    banner()
    exit("Thanks For Using")





