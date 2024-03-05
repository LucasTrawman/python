from bank import value

def test_h():
    assert value("hi") == 20
    assert value("how you doing?") == 20
    assert value("hi, hello") == 20

def test_hello():
    assert value("hello") == 0
    assert value("Hello, have a good day") == 0

def test_rest():
    assert value("what's up?") == 100
    assert value("right, hello") == 100
