# src/calculator.py
"""
A simple CLI calculator module that provides basic and advanced operations:
add, subtract, multiply, divide, power, square root, and factorial.
"""


def add(a, b):
    """Return the sum of two numbers a and b."""
    return a + b


def subtract(a, b):
    """Return the result of subtracting b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers with input validation."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b


def divide(a, b):
    """Divide a by b with input validation."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Return a raised to the power of b."""
    return a**b


def square_root(a):
    """Return the square root of a. Raises ValueError if a < 0."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a**0.5


def factorial(n):
    """Return the factorial of n. Raises ValueError if n < 0."""
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if n in (0, 1):
        return 1
    result_fact = 1
    for num in range(2, n + 1):
        result_fact *= num
    return result_fact
