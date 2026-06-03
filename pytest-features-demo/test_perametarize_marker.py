import pytest

def add_numbers(n1, n2):
    return n1 + n2

@pytest.mark.parametrize("n1,n2,expected",[
    (1,2,3),
    (4,5,9),
    (5,6,11)
])
def test_add_numbers(n1,n2,expected):
    assert add_numbers(n1,n2) == expected

#

# content of test_expectation.py
import pytest


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected