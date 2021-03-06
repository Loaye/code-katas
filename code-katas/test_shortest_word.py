"""Test Modules"""

test.describe("Basic Tests")
test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
test.assert_equals(find_short("lets talk about javascript the best language"), 3)
test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)

def test_alphabet_position():
    """Finds Alphabet Values"""
    from alphabet_replace import alphabet_position
    assert alphabet_position("abcdefg") == "1 2 3 4 5 6 7"


def test_alphabet_position():
    """Finds Alphabet Values"""
    from alphabet_replace import alphabet_position
    assert alphabet_position("The sunset sets at twelve o' clock.") == ("20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")


def test_alphabet_position():
    """Finds Alphabet Values"""
    from alphabet_replace import alphabet_position
    assert alphabet_position("The narwhal bacons at midnight.") == "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"


def test_alphabet_position():
    """Finds Alphabet Values"""
    from alphabet_replace import alphabet_position
    assert alphabet_position("Hello, my name is Jake") ==
    "8 5 12 12 15 13 25 14 1 13 5 9 19 10 1 11 5"
