# REMASTERED MINI CALCULATOR (2025)
# USING CONSOLE AND MADE BY TALKSTERMITE
# https://github.com/talkstermite

import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.YELLOW +"====================================")
print("==== REMASTERED MINI CALCULATOR ====")
print("==== MADE BY TALKSTERMITE ==========")
print("====================================")
print(Fore.RESET)

while True:
    
    print("Choose an operator available in the list below:")
    print(Style.DIM + "- Addition (Type +)")
    print("- Subtraction (Type -)")
    print("- Multiplication (Type *)")
    print("- Division (Type /)")
    print(Style.RESET_ALL)

    op = input("What's the operator? (pick from the list): ")
    n1 = float(input("Enter the first number to calculate: "))
    n2 = float(input("Enter the second number to calculate: "))

    if op == "+":
        res = n1 + n2
        print(Back.WHITE + Fore.BLACK)
        print(f"Addition result: {round(res, 3)}")
        print(Back.RESET + Fore.RESET)
    elif op == "-":
        res = n1 - n2
        print(Back.WHITE + Fore.BLACK)
        print(f"Subtraction result: {round(res, 3)}")
        print(Back.RESET + Fore.RESET)
    elif op == "*":
        res = n1 * n2
        print(Back.WHITE + Fore.BLACK)
        print(f"Multiplication result: {round(res, 3)}")
        print(Back.RESET + Fore.RESET)
    elif op == "/":
        res = n1 / n2
        print(Back.WHITE + Fore.BLACK)
        print(f"Division result: {round(res, 3)}")
        print(Back.RESET + Fore.RESET)
    else:
        print(Fore.RED)
        print(f"{op} is not a valid operator.")

    print(Back.RESET + Fore.RESET)
    restart = input("Run again? (yes/no): ").strip().lower()
    print()
    
    if restart != "yes":
        print("Have a nice day!")
        time.sleep(2)
        break