import sys
import os
import io

try:
    import cat.lib.cat as cat
except:
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    from lib import cat


def test_empty_string_and_no_transform(capsys):
    t_string = io.StringIO("")
    cat.stream_printer(t_string)
    captured = capsys.readouterr()
    assert captured.out == ""
