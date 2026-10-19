"""Sum, multiply, subtract, divide and power two values."""

__all__ = ["sum", "multiply", "subtract", "divide", "power"]


def sum(a, b):
    """Return a + b.

    >>> sum(2, 3)
    5
    >>> sum(-1, 1)
    0
    """
    return a + b


def multiply(a, b):
    """Return a * b.

    >>> multiply(2, 3)
    6
    >>> multiply(-1, 4)
    -4
    """
    return a * b


def subtract(a, b):
    """Return a - b.

    >>> subtract(5, 3)
    2
    >>> subtract(-1, 1)
    -2
    """
    return a - b


def divide(a, b):
    """Return a / b.

    >>> divide(6, 3)
    2.0
    >>> divide(1, 4)
    0.25
    """
    return a / b


def power(a, b):
    """Return a ** b.

    >>> power(2, 3)
    8
    >>> power(2, -1)
    0.5
    """
    return a ** b
