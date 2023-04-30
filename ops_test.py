
import calculation

def test_add():
    assert calculation.add(2,3) == 5

def test_subtract():    
    assert calculation.subtract(2, 3) == -1

def test_multiply():
    assert calculation.multiply(2, 3) == 6

def test_divide():
    assert calculation.divide(10,5) == 2