import sys
import os

try:
    from ls.lib import ls_2
except:
    print("using alternative import")
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    from lib import ls_2


def test_empty_list_no_verbose_no_recursion(capsys):
    ls_2.dirs_print([], sort_format=lambda x: x, long_verbose_flag=0, recursion_flag=0)
    captured = capsys.readouterr().out
    expected = ''
    assert captured == expected


def test_nonempty_list_no_verbose_no_recursion(capsys, path_to_data):
    ls_2.dirs_print([path_to_data], sort_format=lambda x: x, long_verbose_flag=0, recursion_flag=0)
    captured = capsys.readouterr().out
    expected = 'sixteen_KB_file_1  nonempty_dir_1  empty_dir_1  \n'
    assert captured == expected


def test_nonempty_list_verbose_no_recursion(capsys, path_to_data, monkeypatch):
    monkeypatch.chdir(path_to_data)
    ls_2.dirs_print(['.'], sort_format=lambda x: x, long_verbose_flag=1, recursion_flag=0)
    captured = capsys.readouterr().out
    expected = 'Итого 24\n' \
               '-rw-rw-r-- 1 doka doka 16384 Dec 08 12:21 sixteen_KB_file_1\n' \
               'drwxrwxr-x 4 doka doka 4096 Dec 08 13:33 nonempty_dir_1\n' \
               'drwxrwxr-x 2 doka doka 4096 Dec 08 13:30 empty_dir_1\n'
    assert captured == expected

def test_nonempty_list__no_verbose_recursion(capsys, path_to_data, monkeypatch):
    monkeypatch.chdir(path_to_data)
    ls_2.dirs_print(['.'], sort_format=lambda x: x, long_verbose_flag=0, recursion_flag=1)
    captured = capsys.readouterr().out
    expected = '.:\n'\
               'sixteen_KB_file_1  nonempty_dir_1  empty_dir_1  \n'\
               '\n'\
               './nonempty_dir_1:\n'\
               'less_sixteen_KB_file_2  non_empty_dir_2  empty_dir_2  \n'\
               '\n'\
               './nonempty_dir_1/non_empty_dir_2:\n'\
               'more_sixteen_KB_file_3  empty_dir_3  \n'\
               '\n'\
               './nonempty_dir_1/non_empty_dir_2/empty_dir_3:\n'\
               '\n'\
               './nonempty_dir_1/empty_dir_2:\n'\
               '\n'\
               './empty_dir_1:\n'\
               '\n'
    assert captured == expected

def test_nonempty_list_verbose_recursion(capsys, path_to_data, monkeypatch):
    monkeypatch.chdir(path_to_data)
    ls_2.dirs_print(['.'], sort_format=lambda x: x, long_verbose_flag=1, recursion_flag=1)
    captured = capsys.readouterr().out
    expected = '.:\n'\
               'Итого 24\n'\
               '-rw-rw-r-- 1 doka doka 16384 Dec 08 12:21 sixteen_KB_file_1\n'\
               'drwxrwxr-x 4 doka doka 4096 Dec 08 13:33 nonempty_dir_1\n'\
               'drwxrwxr-x 2 doka doka 4096 Dec 08 13:30 empty_dir_1\n'\
               '\n'\
               './nonempty_dir_1:\n'\
               'Итого 24\n'\
               '-rw-rw-r-- 1 doka doka 16383 Dec 08 12:21 less_sixteen_KB_file_2\n'\
               'drwxrwxr-x 3 doka doka 4096 Dec 08 13:29 non_empty_dir_2\n'\
               'drwxrwxr-x 2 doka doka 4096 Dec 08 11:09 empty_dir_2\n'\
               '\n'\
               './nonempty_dir_1/non_empty_dir_2:\n'\
               'Итого 24\n'\
               '-rw-rw-r-- 1 doka doka 16385 Dec 08 12:21 more_sixteen_KB_file_3\n'\
               'drwxrwxr-x 2 doka doka 4096 Dec 08 11:11 empty_dir_3\n'\
               '\n'\
               './nonempty_dir_1/non_empty_dir_2/empty_dir_3:\n'\
               'Итого 0\n'\
               '\n'\
               './nonempty_dir_1/empty_dir_2:\n'\
               'Итого 0\n'\
               '\n'\
               './empty_dir_1:\n'\
               'Итого 0\n'\
               '\n'
    assert captured == expected
