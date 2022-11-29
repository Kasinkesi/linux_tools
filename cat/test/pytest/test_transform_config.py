import sys
import os

try:
    import cat.lib.cat as cat
except:
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    from lib import cat

def test_no_flags():
    current_transform = cat.transform_config()
    expected = None
    assert current_transform == expected
