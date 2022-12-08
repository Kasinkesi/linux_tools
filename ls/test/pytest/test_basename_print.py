import sys
import os

try:
    from ls.lib import ls_2
except:
    print("using alternative import")
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    from lib import ls_2


def test_empty_paths_list_and_no_verbose(path_to_data, capsys):
    ls_2.basename_print([], long_verbose_flag=0)
    captured = capsys.readouterr().out
    expected = ''
    assert captured == expected


def test_empty_paths_list_and_verbose(path_to_data, capsys):
    ls_2.basename_print([], long_verbose_flag=1)
    captured = capsys.readouterr().out
    expected = ''
    assert captured == expected


def test_nonempty_paths_list_and_no_verbose(capsys, path_to_data):
    path_to_test_file = os.path.join(path_to_data, "sixteen_KB_file_1")
    ls_2.basename_print([path_to_test_file], long_verbose_flag=0)
    captured = capsys.readouterr().out
    expected = 'sixteen_KB_file_1  \n'
    assert captured == expected


def test_nonempty_paths_list_and_verbose(capsys, path_to_data):
    path_to_test_file = os.path.join(path_to_data, "sixteen_KB_file_1")
    ls_2.basename_print([path_to_test_file], long_verbose_flag=1)
    captured = capsys.readouterr().out
    expected = '-rw-rw-r-- 1 doka doka 16384 Dec 08 12:21 sixteen_KB_file_1\n'
    assert captured == expected
