# src/cli.py

import sys
from .calculator import add, subtract, multiply, divide


def main():
    try:
        if len(sys.argv) < 4:
            print("Unexpected error: Not enough arguments")
            sys.exit(1)

        operation = sys.argv[1]
        a = float(sys.argv[2])
        b = float(sys.argv[3])

        if operation == "add":
            result = add(a, b)
            print(f"Result: {int(result)}")
        elif operation == "subtract":
            result = subtract(a, b)
            print(f"Result: {int(result)}")
        elif operation == "multiply":
            result = multiply(a, b)
            print(f"Result: {int(result)}")
        elif operation == "divide":
            result = divide(a, b)
            print(f"Result: {result:.2f}")
        else:
            print("Unexpected error: Unknown operation")
            sys.exit(1)

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
