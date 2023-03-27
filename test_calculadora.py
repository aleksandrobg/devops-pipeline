# testando a calculadora

from calculadora import Calculadora

def test_add():
    c = Calculadora()
    assert c.add(2, 3) == 5

def test_subtract():
    c = Calculadora()
    assert c.subtract(5, 3) == 2

def test_multiply():
    c = Calculadora()
    assert c.multiply(2, 3) == 6

def test_divide():
    c = Calculadora()
    assert c.divide(6, 3) == 2
    assert c.divide(6, 0) == None
