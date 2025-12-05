from main import *
import pytest

# def test_get_temperature():
#     assert get_temperature(21) == "hot"
#     assert get_temperature(20) == "cold"
#

def test_add():
    assert add(1, 2) == 3, "1 + 2 is 3"
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    # assert add(1, 2) == 5, "1 + 2 should 3"

def test_divide():
    with pytest.raises(ValueError, match="Can not divide by ZERO"):
        divide(10,0)
