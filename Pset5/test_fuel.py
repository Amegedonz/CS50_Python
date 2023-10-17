from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("50/100") == 50

def test_gague():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(55) == "55%"