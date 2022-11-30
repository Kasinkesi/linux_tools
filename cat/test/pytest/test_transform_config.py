import sys
import os

try:
    from cat.lib import cat
except:
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    from lib import cat

def test_no_flags():
    current_transform = cat.transform_config(number_nonblank_flag=0,number_flag=0,smile_exterminator_flag=0)
    expected = None
    assert current_transform == expected

def test_s_flag():
    current_transform = cat.transform_config(number_nonblank_flag=0,number_flag=0,smile_exterminator_flag=1)
    expected = cat.smile_exterminator
    assert current_transform == expected

def test_n_flag():
    current_transform = cat.transform_config(number_nonblank_flag=0,number_flag=1,smile_exterminator_flag=0)
    expected = cat.number()
    assert current_transform.__qualname__ == expected.__qualname__

def test_n_and_s_flag():
    current_transform = cat.transform_config(number_nonblank_flag=0,number_flag=1,smile_exterminator_flag=1)
    inner_func = cat.number()
    expected = cat.smile_exterminator_decorator(inner_func)
    assert current_transform.__qualname__ == expected.__qualname__


def test_b_flag():
    current_transform = cat.transform_config(number_nonblank_flag=1,number_flag=0,smile_exterminator_flag=0)
    expected = cat.number_nonblank()
    assert current_transform.__qualname__ == expected.__qualname__

def test_b_and_s_flag():
    current_transform = cat.transform_config(number_nonblank_flag=1,number_flag=0,smile_exterminator_flag=1)
    inner_func = cat.number_nonblank()
    expected = cat.smile_exterminator_decorator(inner_func)
    assert current_transform.__qualname__ == expected.__qualname__

def test_b_and_n_flag():
    current_transform = cat.transform_config(number_nonblank_flag=1,number_flag=1,smile_exterminator_flag=0)
    expected = cat.number_nonblank()
    assert current_transform.__qualname__ == expected.__qualname__

def test_b_and_n_and_s_flag():
    current_transform = cat.transform_config(number_nonblank_flag=1,number_flag=1,smile_exterminator_flag=1)
    inner_func = cat.number_nonblank()
    expected = cat.smile_exterminator_decorator(inner_func)
    assert current_transform.__qualname__ == expected.__qualname__
