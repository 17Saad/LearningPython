from bank import value

def test_value0():
    assert value("hello") == 0

def test_value20():
    assert value("hitman") == 20

def test_value100():
    assert value("Johnny") == 100

def test_value100_2():
    assert value("100") == 100

def test_valueCasing():
    assert value("HELLO") == 0