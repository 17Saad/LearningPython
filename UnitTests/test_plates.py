from plates import is_valid

def test_startWithLetter():
    assert is_valid("AB") == True
    assert is_valid("F2") == False
    assert is_valid("3V") == False
    assert is_valid("43") == False

def test_countCharacters():
    assert is_valid("S") == False
    assert is_valid("SADI121") == False
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True

def test_numAtEnd():
    assert is_valid("QD12FS") == False

def test_punc():
    assert is_valid("ZX,! 3") == False

def test_FirstZero():
    assert is_valid("AD50") == True
    assert is_valid("EF05") == False