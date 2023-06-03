from twttr import shorten
import pytest

def test_shortenLower():
    assert shorten("facebook") == "fcbk"

def test_shortenUpper():
    assert shorten("GRANADA") == "GRND"

def test_shortenUppLower():
    assert shorten("Mediterranean") == "Mdtrrnn"

def test_shortenNumbers():
    assert shorten("1234") == "1234"

def test_shortenPunc():
    assert shorten("!?.,") == "!?.,"

