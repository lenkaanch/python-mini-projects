from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3
def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(5, 0) == "Cannot divide by zero"
