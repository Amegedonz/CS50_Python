from bank import value

def testing_h_greetings():
    assert value("Hello") == "$0"
    assert value("hello") == "$0"
    assert value("Hey") == "$20"
    assert value("How you doing?") == "$20"

def testing_non_h():
    assert value("good day!") == "$100"
    assert value("crickey") == "$100"
    assert value("Weathers fantastic") == "$100"