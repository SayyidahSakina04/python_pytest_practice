from pickle import FALSE

import pytest
from isPrime import isPrime

@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (17, True),
    (18, False),
    (19, True),
    (25, False),
])
def test_is_prime(num, expected):
    # assert isPrime(7) == True
    assert isPrime(num) == expected