# test_calculator.py

from calculator import Calculator

def test_add():
    c = Calculator()
    assert c.add(2, 3) == 5

def test_subtract():
    c = Calculator()
    assert c.subtract(5, 3) == 2

def test_multiply():
    c = Calculator()
    assert c.multiply(2, 3) == 6

def test_divide():
    c = Calculator()
    assert c.divide(6, 3) == 2
    assert c.divide(6, 0) == None
