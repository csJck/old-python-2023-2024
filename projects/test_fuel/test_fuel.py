from fuel import gauge, convert

def test_fraction():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"



