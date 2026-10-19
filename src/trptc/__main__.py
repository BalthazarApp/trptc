"""Command-line interface: python -m trptc <operation> <a> <b>."""

import argparse
import sys

import trptc

OPERATIONS = ["sum", "multiply", "subtract", "divide", "power"]


def number(value):
    """Parse value as int if it is an int literal, otherwise float."""
    try:
        return int(value)
    except ValueError:
        return float(value)


def main(argv=None):
    """Run the operation on a and b and print the result."""
    parser = argparse.ArgumentParser(prog="trptc")
    parser.add_argument("operation", choices=OPERATIONS)
    parser.add_argument("a", type=number)
    parser.add_argument("b", type=number)
    args = parser.parse_args(argv)

    try:
        result = getattr(trptc, args.operation)(args.a, args.b)
    except ZeroDivisionError:
        print("error: division by zero", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
