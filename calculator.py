# https://github.com/MarceK0407/Lab-11-MK-MP
# Partner 1: Marcelo Kellert
# Partner 2: McCain Pickering
import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input values for logarithm.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b