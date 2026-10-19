import doctest

import trptc


def test_doctests():
    results = doctest.testmod(trptc)
    assert results.failed == 0
    assert results.attempted > 0
