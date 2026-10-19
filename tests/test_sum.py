import pytest

from trptc import divide, multiply, power, subtract, sum


def test_sum():
    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    assert sum(0.5, 0.25) == 0.75


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 4) == -4
    assert multiply(0.5, 0.5) == 0.25


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(0.75, 0.25) == 0.5


def test_divide():
    assert divide(6, 3) == 2
    assert divide(-4, 2) == -2
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5
