import pytest
from math_utils import divide

def test_divide_valid():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    # This will pass since dividing by zero raises ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
