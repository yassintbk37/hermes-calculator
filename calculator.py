"""Simple command-line calculator module."""

from __future__ import annotations


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the result of subtracting b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the result of dividing a by b.

    Raises:
        ValueError: if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main() -> None:
    """Run the calculator from the command line."""
    import sys

    if len(sys.argv) < 4:
        print("Usage: python calculator.py <add|subtract|multiply|divide> <num1> <num2>")
        sys.exit(1)

    operation = sys.argv[1]
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Error: Both arguments must be numbers.")
        sys.exit(1)

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if operation not in operations:
        print(f"Unknown operation: {operation}. Use add, subtract, multiply, or divide.")
        sys.exit(1)

    result = operations[operation](num1, num2)
    print(f"Result: {result}")