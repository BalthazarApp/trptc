from decimal import Decimal
from fractions import Fraction

import pytest

from trptc import multiply, subtract, sum


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10**30, 10**30, 2 * 10**30),  # large ints
        (-5, -7, -12),  # negative numbers
        (42, 0, 42),  # zero is the additive identity
        (Fraction(1, 3), Fraction(1, 6), Fraction(1, 2)),  # Fraction inputs
        (Decimal("0.1"), Decimal("0.2"), Decimal("0.3")),  # Decimal inputs
        ("a", "b", "ab"),  # duck-typed string concatenation
        ([1], [2], [1, 2]),  # duck-typed list concatenation
    ],
)
def test_sum_edge_cases(a, b, expected):
    assert sum(a, b) == expected


def test_sum_float_rounding():
    assert sum(0.1, 0.2) == pytest.approx(0.3)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10**15, 10**15, 10**30),  # large ints
        (-3, 4, -12),  # mixed-sign numbers
        (12345, 1, 12345),  # one is the multiplicative identity
        (99999, 0, 0),  # zero annihilates
        (Fraction(2, 3), Fraction(3, 4), Fraction(1, 2)),  # Fraction inputs
        (Decimal("1.5"), Decimal("2"), Decimal("3.0")),  # Decimal inputs
        ("ab", 3, "ababab"),  # duck-typed string repetition
        ([0], 3, [0, 0, 0]),  # duck-typed list repetition
    ],
)
def test_multiply_edge_cases(a, b, expected):
    assert multiply(a, b) == expected


def test_multiply_float_rounding():
    assert multiply(0.1, 3) == pytest.approx(0.3)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10**30, 10**30, 0),  # large ints
        (-5, -7, 2),  # negative numbers
        (42, 0, 42),  # subtracting zero is identity
        (0, 5, -5),  # result goes negative
        (Fraction(1, 2), Fraction(1, 6), Fraction(1, 3)),  # Fraction inputs
        (Decimal("0.3"), Decimal("0.1"), Decimal("0.2")),  # Decimal inputs
    ],
)
def test_subtract_edge_cases(a, b, expected):
    assert subtract(a, b) == expected


def test_subtract_float_rounding():
    assert subtract(0.3, 0.1) == pytest.approx(0.2)


def test_sum_type_error_on_mismatched_types():
    with pytest.raises(TypeError):
        sum(1, "a")
