"""
sort by absolute pathname
"""

import sys
import os

try:
    from ls.lib import ls_2
except:
    print("using alternative import")
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    from lib import ls_2


def test_empty_dir_and_no_sort(empty_dir, capsys):
    files_list, dirs_list = ls_2.files_and_dirs(empty_dir, lambda x: x)

    captured = capsys.readouterr().out
    expected = 'not_file_or_dir не файл или директория\n'
    assert captured == expected
    assert files_list == []
    assert dirs_list == [empty_dir[0]]


def test_nonempty_dir_and_no_sort(dir_list_gen, capsys):
    files_list, dirs_list = ls_2.files_and_dirs(dir_list_gen, lambda x: x)

    captured = capsys.readouterr().out
    expected = 'not_file_or_dir не файл или директория\n'
    assert captured == expected

    assert os.path.basename(files_list[0]) == 'sixteen_KB_file_1'
    assert os.path.basename(files_list[1]) == 'less_sixteen_KB_file_2'
    assert os.path.basename(files_list[2]) == 'more_sixteen_KB_file_3'

    assert os.path.basename(dirs_list[0]) == 'empty_dir_1'
    assert os.path.basename(dirs_list[1]) == 'non_empty_dir_1'
    assert os.path.basename(dirs_list[2]) == 'empty_dir_2'
    assert os.path.basename(dirs_list[3]) == 'non_empty_dir_2'
    assert os.path.basename(dirs_list[4]) == 'empty_dir_3'

def test_nonempty_dir_and_sort(dir_list_gen, capsys):
    files_list, dirs_list = ls_2.files_and_dirs(dir_list_gen, sorted)

    captured = capsys.readouterr().out
    expected = 'not_file_or_dir не файл или директория\n'
    assert captured == expected

    assert os.path.basename(files_list[0]) == 'less_sixteen_KB_file_2'
    assert os.path.basename(files_list[1]) == 'more_sixteen_KB_file_3'
    assert os.path.basename(files_list[2]) == 'sixteen_KB_file_1'

    assert os.path.basename(dirs_list[0]) == 'empty_dir_1'
    assert os.path.basename(dirs_list[1]) == 'non_empty_dir_1'
    assert os.path.basename(dirs_list[2]) == 'empty_dir_2'
    assert os.path.basename(dirs_list[3]) == 'non_empty_dir_2'
    assert os.path.basename(dirs_list[4]) == 'empty_dir_3'

def test_nonempty_dir_and_revers_sort(dir_list_gen, capsys):
    files_list, dirs_list = ls_2.files_and_dirs(dir_list_gen, ls_2.sort_revers)

    captured = capsys.readouterr().out
    expected = 'not_file_or_dir не файл или директория\n'
    assert captured == expected

    assert os.path.basename(files_list[0]) == 'sixteen_KB_file_1'
    assert os.path.basename(files_list[1]) == 'more_sixteen_KB_file_3'
    assert os.path.basename(files_list[2]) == 'less_sixteen_KB_file_2'

    assert os.path.basename(dirs_list[0]) == 'empty_dir_3'
    assert os.path.basename(dirs_list[1]) == 'non_empty_dir_2'
    assert os.path.basename(dirs_list[2]) == 'empty_dir_2'
    assert os.path.basename(dirs_list[3]) == 'non_empty_dir_1'
    assert os.path.basename(dirs_list[4]) == 'empty_dir_1'


def test_nonempty_dir_and_basename_sort(dir_list_gen, capsys):
    files_list, dirs_list = ls_2.files_and_dirs(dir_list_gen, ls_2.basename_sort)

    captured = capsys.readouterr().out
    expected = 'not_file_or_dir не файл или директория\n'
    assert captured == expected

    assert os.path.basename(files_list[0]) == 'less_sixteen_KB_file_2'
    assert os.path.basename(files_list[1]) == 'more_sixteen_KB_file_3'
    assert os.path.basename(files_list[2]) == 'sixteen_KB_file_1'

    assert os.path.basename(dirs_list[0]) == 'empty_dir_1'
    assert os.path.basename(dirs_list[1]) == 'empty_dir_2'
    assert os.path.basename(dirs_list[2]) == 'empty_dir_3'
    assert os.path.basename(dirs_list[3]) == 'non_empty_dir_1'
    assert os.path.basename(dirs_list[4]) == 'non_empty_dir_2'

def test_nonempty_dir_and_basename_sort_revers(dir_list_gen, capsys):
    files_list, dirs_list = ls_2.files_and_dirs(dir_list_gen, ls_2.basename_sort_revers)

    captured = capsys.readouterr().out
    expected = 'not_file_or_dir не файл или директория\n'
    assert captured == expected

    assert os.path.basename(files_list[0]) == 'sixteen_KB_file_1'
    assert os.path.basename(files_list[1]) == 'more_sixteen_KB_file_3'
    assert os.path.basename(files_list[2]) == 'less_sixteen_KB_file_2'

    assert os.path.basename(dirs_list[0]) == 'non_empty_dir_2'
    assert os.path.basename(dirs_list[1]) == 'non_empty_dir_1'
    assert os.path.basename(dirs_list[2]) == 'empty_dir_3'
    assert os.path.basename(dirs_list[3]) == 'empty_dir_2'
    assert os.path.basename(dirs_list[4]) == 'empty_dir_1'
