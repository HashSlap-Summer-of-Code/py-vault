#!/usr/bin/env python3

"""
Command-Line Calculator

Usage:
    python calculator.py <number1> <operator> <number2>

Example:
    python calculator.py 5 + 3
    Output: 8.0

Supported operators:
    +   Addition
    -   Subtraction
    *   Multiplication
    /   Division

Handles invalid input and displays helpful error messages.

Author: Open Source Contributor
"""

import sys

def calculate(n1, operator, n2):
    try:
        num1 = float(n1)
        num2 = float(n2)
    except ValueError:
        print("[!] Error: Both operands must be numbers.")
        return

    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            print(f"[!] Error: Unsupported operator '{operator}'. Use one of +, -, *, /.")
            return

        print(f"Result: {result}")
    except ZeroDivisionError:
        print("[!] Error: Cannot divide by zero.")

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <number1> <operator> <number2>")
        return

    _, n1, op, n2 = sys.argv
    calculate(n1, op, n2)

if __name__ == "__main__":
    main()
