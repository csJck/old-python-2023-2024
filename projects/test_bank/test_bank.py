from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("hey") == 20

def test_other():
    assert value("sup") == 100

def test_white():
    assert value(" hello there") == 0

def test_case():
    assert value("Hello") == 0

