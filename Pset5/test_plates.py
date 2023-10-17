from plates import is_valid

def testing_start_numbers():
    assert is_valid("C50") == False
    assert is_valid("1234") == False

def testing_too_long_short():
    assert is_valid("H") == False
    assert is_valid("HELLO50") == False

def testing_middle_numbers():
    assert is_valid("CS50H") == False
    assert is_valid("HELP4H") == False

def testing_non_wierd_chars():
    assert is_valid("CS 50") == False
    assert is_valid("CS!50") == False

def testing_correct_format():
    assert is_valid("CS50") == True
    assert is_valid("HELLO5") == True
    assert is_valid("CS") == True