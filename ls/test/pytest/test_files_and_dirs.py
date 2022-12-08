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


def basename_list(path_list):
    return [os.path.basename(path) for path in path_list]


def test_empty_list_no_sort():
    files_list, dirs_list = ls_2.files_and_dirs([], lambda x: x)
    basename_files_list = basename_list(files_list)
    basename_dirs_list = basename_list(dirs_list)

    assert basename_files_list == []
    assert basename_dirs_list == []


def test_not_file_or_dir(capsys):
    ls_2.files_and_dirs(['not_file_or_dir'], lambda x: x)
    captured = capsys.readouterr().out
    expected = 'not_file_or_dir не файл или директория\n'
    assert captured == expected


def test_only_files_list_no_sort(only_files_list, capsys):
    files_list, dirs_list = ls_2.files_and_dirs(only_files_list + ['not_file_or_dir'], lambda x: x)
    basename_files_list = basename_list(files_list)
    basename_dirs_list = basename_list(dirs_list)
    captured = capsys.readouterr().out
    expected = 'not_file_or_dir не файл или директория\n'
    assert captured == expected
    assert basename_files_list == ['c_file', 'a_file', '_b_file']
    assert basename_dirs_list == []


def test_only_dirs_list_no_sort(only_dirs_list):
    files_list, dirs_list = ls_2.files_and_dirs(only_dirs_list, lambda x: x)
    basename_files_list = basename_list(files_list)
    basename_dirs_list = basename_list(dirs_list)

    assert basename_files_list == []
    assert basename_dirs_list == ['c_dir', 'a_dir', '_b_dir']


def test_mixed_list_no_sort(mixed_list):
    files_list, dirs_list = ls_2.files_and_dirs(mixed_list, lambda x: x)
    basename_files_list = basename_list(files_list)
    basename_dirs_list = basename_list(dirs_list)

    assert basename_files_list == ['c_file', 'a_file', '_b_file']
    assert basename_dirs_list == ['c_dir', 'a_dir', '_b_dir']


def test_only_files_list_sorted(only_files_list):
    files_list, dirs_list = ls_2.files_and_dirs(only_files_list, sorted)
    basename_files_list = basename_list(files_list)
    basename_dirs_list = basename_list(dirs_list)

    assert basename_files_list == ['_b_file', 'a_file', 'c_file']
    assert basename_dirs_list == []


def test_only_dirs_list_sorted(only_dirs_list):
    files_list, dirs_list = ls_2.files_and_dirs(only_dirs_list, sorted)
    basename_files_list = basename_list(files_list)
    basename_dirs_list = basename_list(dirs_list)

    assert basename_files_list == []
    assert basename_dirs_list == ['_b_dir', 'a_dir', 'c_dir']


def test_mixed_list_sorted(mixed_list):
    files_list, dirs_list = ls_2.files_and_dirs(mixed_list, sorted)
    basename_files_list = basename_list(files_list)
    basename_dirs_list = basename_list(dirs_list)

    assert basename_files_list == ['_b_file', 'a_file', 'c_file']
    assert basename_dirs_list == ['_b_dir', 'a_dir', 'c_dir']


def test_only_files_list_sort_reverse(only_files_list):
    files_list, dirs_list = ls_2.files_and_dirs(only_files_list, ls_2.sort_reverse)
    basename_files_list = basename_list(files_list)
    basename_dirs_list = basename_list(dirs_list)

    assert basename_files_list == ['c_file', 'a_file', '_b_file']
    assert basename_dirs_list == []


def test_only_dirs_list_sort_reverse(only_dirs_list):
    files_list, dirs_list = ls_2.files_and_dirs(only_dirs_list, ls_2.sort_reverse)
    basename_files_list = basename_list(files_list)
    basename_dirs_list = basename_list(dirs_list)

    assert basename_files_list == []
    assert basename_dirs_list == ['c_dir', 'a_dir', '_b_dir']


def test_mixed_list_sort_reverse(mixed_list):
    files_list, dirs_list = ls_2.files_and_dirs(mixed_list, ls_2.sort_reverse)
    basename_files_list = basename_list(files_list)
    basename_dirs_list = basename_list(dirs_list)

    assert basename_files_list == ['c_file', 'a_file', '_b_file']
    assert basename_dirs_list == ['c_dir', 'a_dir', '_b_dir']
