"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""
import click
from calculator import add, subtract, multiply, divide, power, square_root, factorial


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""

    try:
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
            return

        click.echo(result)

    except TypeError as e:
        click.echo(f"Error: {e}")
    except ValueError as e:
        click.echo(f"Error: {e}")
    except Exception:
        click.echo("Unexpected error occurred.")


if __name__ == "__main__":
    calculate()
