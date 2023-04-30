
from calculation import calculate


def test_add():
    assert calculate.add(2,3) == 5

def test_subtract():    
    assert calculate.subtract(2, 3) == -1

def test_multiply():
    assert calculate.multiply(2, 3) == 6

def test_divide():
    assert calculate.divide(10,5) == 2