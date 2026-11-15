# https://github.com/MarceK0407/Lab-11-MK-MP
# Partner 1: Marcelo Kellert
# Partner 2: McCain Pickering
import math


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input values for logarithm.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b