from twttr import shorten

def test_lowerCase():
    assert shorten("abcde") == 'bcd'
    assert shorten("twitter") == 'twttr'

def test_upperCase():
    assert shorten("HELLO") == 'HLL'
    assert shorten("GO AWAY") == 'G WY'

def test_empty():
    assert shorten("") == ""
    assert shorten("AEioU") == ""