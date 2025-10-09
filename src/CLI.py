"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""
import sys
import click

from src.calculator import add, subtract, multiply, divide, power, square_root, factorial

@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""
    try:
        if operation in ("add", "subtract", "multiply", "divide", "power") and num2 is None:
            click.echo("Unexpected error: missing second operand")
            sys.exit(1)

        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation == "sqrt":
            result = square_root(num1)
        elif operation == "factorial":
            result = factorial(int(num1))
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        click.echo(f"Result: {result}")

    except (TypeError, ValueError) as e:
        click.echo(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    calculate()  # pylint: disable=no-value-for-parameter
