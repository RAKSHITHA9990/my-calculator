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
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide a by b"""
    return a / b


def power(a, b):
    """Return a raised to the power of b."""
    return a**b


def square_root(a):
    """Return the square root of a. Raises ValueError if a < 0."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a**0.5


def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

    print(f"Multiplying {a} × {b}")  # Added logging
    result = a * b
    print(f"Result: {result}")
    return result


def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")

    print(f"Dividing {a} ÷ {b}")  # Added logging
    result = a / b
    print(f"Result: {result}")
    return result


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def factorial(n):
    """Return the factorial of n. Raises ValueError if n < 0."""
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if n in (0, 1):  # fixed R1714 warning
        return 1

    result_fact = 1
    for num in range(2, n + 1):  # fixed W0621 warning
        result_fact *= num
    return result_fact
