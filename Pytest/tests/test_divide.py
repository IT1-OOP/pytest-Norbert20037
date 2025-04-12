import pytest
from src import calculator

def test_divide():
    assert calculator.divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        calculator.divide(10, 0)