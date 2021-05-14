from minicomb import *

from pytest import raises

def test_factorial():
    simple_cases = zip(range(0, 12), [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800])
    for k, actual in simple_cases:
        assert factorial(k) == actual
    
    with raises(ValueError):
        factorial(-1)
    with raises(ValueError):
        factorial("hej")

def test_binomial():
    # edge cases
    assert binomial(0, 0) == 1
    assert binomial(2, 0) == 1
    assert binomial(2, -1) == 0
    assert binomial(2, 4) == 0
    assert binomial(2, -4) == 0

    with raises(ValueError):
        binomial(-2, 1)

    simple_cases = [
        ((3, 2), 3),
        ((2, 2), 1),
        ((5, 4), 5),
        ((5, 3), 10)
    ]

    for args, actual in simple_cases:
        assert binomial(*args) == actual