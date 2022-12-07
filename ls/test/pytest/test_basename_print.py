import sys
import os

try:
    from ls.lib import ls_2
except:
    print("using alternative import")
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    from lib import ls_2


def test_empty_dir_and_no_verbose(empty_dir, capsys):
    ls_2.basename_print(empty_dir[:-1], long_verbose_flag=0)
    captured = capsys.readouterr().out
    expected = 'test_empty_dir_and_no_verbose0  \n'
    assert captured == expected


def test_empty_dir_and_verbose(capsys):
    path_to_test = os.path.join(os.path.dirname(__file__), "..", "data/test_file")
    ls_2.basename_print([path_to_test], long_verbose_flag=1)
    captured = capsys.readouterr().out
    expected = '-rw-rw-r-- 1 doka doka   19 Nov 29 15:51 test_file\n'
    assert captured == expected
