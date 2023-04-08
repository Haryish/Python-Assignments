# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:21:31 2023

@author: haryi
"""

# Define the calc function using lambda functions
def calc(f, a, b):
    return f(a, b)

# Define lambda functions for arithmetic operations
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y

# Define the main function to demonstrate the calc function
def main():
    while True:
        print("\nArithmetic Operations Menu")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        # Get user input for menu selection
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            # Get user input for operands
            a = float(input("Enter first operand: "))
            b = float(input("Enter second operand: "))
            # Call the calc function with the add lambda function
            result = calc(add, a, b)
            print(f"{a} + {b} = {result}")
        elif choice == 2:
            # Get user input for operands
            a = float(input("Enter first operand: "))
            b = float(input("Enter second operand: "))
            # Call the calc function with the subtract lambda function
            result = calc(subtract, a, b)
            print(f"{a} - {b} = {result}")
        elif choice == 3:
            # Get user input for operands
            a = float(input("Enter first operand: "))
            b = float(input("Enter second operand: "))
            # Call the calc function with the multiply lambda function
            result = calc(multiply, a, b)
            print(f"{a} * {b} = {result}")
        elif choice == 4:
            # Get user input for operands
            a = float(input("Enter first operand: "))
            b = float(input("Enter second operand: "))
            # Call the calc function with the divide lambda function
            result = calc(divide, a, b)
            print(f"{a} / {b} = {result}")
        elif choice == 5:
            # Exit the program
            print("Exiting...")
            break
        else:
            # Invalid menu selection
            print("Invalid choice, please try again.")

# Call the main function
main()
