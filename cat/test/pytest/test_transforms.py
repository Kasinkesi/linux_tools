import sys
import os

try:
    import cat.lib.cat as cat
except:
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    from lib import cat


def test_number_empty_string():
    t_format = cat.number()
    t_string = t_format("")
    expected = ""
    assert t_string == expected


def test_number_three_strings(three_strings):
    t_format = cat.number()
    t_string = t_format(three_strings[0])
    expected = "     1  hi"
    assert t_string == expected
    t_string = t_format(three_strings[1])
    expected = "     2  \n"
    assert t_string == expected
    t_string = t_format(three_strings[2])
    expected = "     3  hello8)"
    assert t_string == expected


def test_number_nonblank_empty_string():
    t_format = cat.number_nonblank()
    t_string = t_format("")
    expected = ""
    assert t_string == expected


def test_number_nonblank_three_strings(three_strings):
    t_format = cat.number_nonblank()
    t_string = t_format(three_strings[0])
    expected = "     1  hi"
    assert t_string == expected
    t_string = t_format(three_strings[1])
    expected = "\n"
    assert t_string == expected
    t_string = t_format(three_strings[2])
    expected = "     2  hello8)"
    assert t_string == expected

def test_smile_exterminator_empty_string():
    t_string = cat.smile_exterminator("")
    expected = ""
    assert t_string == expected


def test_smile_exterminator_three_strings(three_strings):
    t_string = cat.smile_exterminator(three_strings[0])
    expected = "hi"
    assert t_string == expected
    t_string = cat.smile_exterminator(three_strings[1])
    expected = "\n"
    assert t_string == expected
    t_string = cat.smile_exterminator(three_strings[2])
    expected = "hellono smile for the wicked"
    assert t_string == expected