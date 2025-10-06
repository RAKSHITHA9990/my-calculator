def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b
def power(a, b):
    """Raise a to the power of b"""
    return a ** b

def square_root(a):
    """Calculate square root of a"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5
def factorial(n):
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI Calculator")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide", "power", "sqrt", "factorial"],
                        help="Operation to perform")
    parser.add_argument("numbers", nargs="+", type=float, help="Numbers for the operation")

    args = parser.parse_args()

    if args.operation == "add":
        result = sum(args.numbers)
    elif args.operation == "subtract":
        result = args.numbers[0] - args.numbers[1]
    elif args.operation == "multiply":
        result = args.numbers[0] * args.numbers[1]
    elif args.operation == "divide":
        if args.numbers[1] == 0:
            raise ValueError("Cannot divide by zero")
        result = args.numbers[0] / args.numbers[1]
    elif args.operation == "power":
        result = args.numbers[0] ** args.numbers[1]
    elif args.operation == "sqrt":
        if args.numbers[0] < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = args.numbers[0] ** 0.5
    elif args.operation == "factorial":
        n = int(args.numbers[0])
        if n < 0:
            raise ValueError("Cannot calculate factorial of negative number")
        result = 1
        for i in range(2, n + 1):
            result *= i

    print(f"Result: {result}")

if __name__ == "__main__":
    main()