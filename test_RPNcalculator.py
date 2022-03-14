import RPNcalculator as t
import pytest
import math

c = t.calc()

def test_work():
    for e in ["c","3","4","+"]:
        result = c.work(e)
    assert result == '7.0'

    for e in ["c","3","4","5","6","+"]:
        result = c.work(e)
    assert result == '11.0'

def test_calc_e():
    for e in ["c", "e"]:
        result = c.work(e)
    assert str(c) == str([math.e])

def test_calc_ln():
    for e in ["c", "4", "ln"]:
        result = c.work(e)
    assert result == str(math.log(4))

def test_calc_add():
    for e in ["c", "3", "4", "+"]:
        result = c.work(e)
    assert result == '7.0'

def test_calc_mult():
    for e in ["c","4","3","*"]:
        result = c.work(e)
    assert result == '12.0'

def test_calc_minus():
    for e in ["c","10","30","-"]:
        result = c.work(e)
    assert result == '-20.0'

def test_calc_div():
    for e in ["c","4","2","/"]:
        result = c.work(e)
    assert result == '2.0'

def test_calc_exp():
    for e in ["c","2","3","^"]:
        result = c.work(e)
    assert result == '8.0'

def test_push():
    for e in ["c","11","22","33"]:
        result = c.work(e)
    assert str(c) == '[33.0, 22.0, 11.0]'

data = list(zip(range(-10,10),range(-10,10)))

def test_div_except():
    c.clear()
    c.push(3)
    c.push(1.0)
    c.push(0.0)
    s = str(c)
    with pytest.raises(ZeroDivisionError,match='division by zero'):
        c.div()
    assert s == str(c)
  
def test_push_except():
    c.clear()
    c.push(3)
    c.push(4)
    s = str(c)
    v = 'ab'
    with pytest.raises(ValueError, match =f"could not convert string to float: '{v}'"):
        c.push(v)
    assert s == str(c)

def test_ln_except():
    c.clear()
    c.push(7)
    c.push(0)
    s = str(c)
    with pytest.raises(ValueError, match="math domain error"):
        c.ln()
    assert s == str(c)

def test_add_except():
    c.clear()
    c.push(7)
    s = str(c)
    with pytest.raises(IndexError,match="list index out of range"):
        c.add()
    assert str(c) == s