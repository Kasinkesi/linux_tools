import sys
import os
import pytest
from collections import namedtuple

try:
    from cat.bin import main
except:
    print("using alternative import")
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    from bin import main

flags_and_expect_list = [((0, 0, 0), "hi\n\nhello8)\n"),
                         ((0, 0, 1), "hi\n\nhellono smile for the wicked\n"),
                         ((0, 1, 0), "     1  hi\n     2  \n     3  hello8)\n"),
                         ((0, 1, 1), "     1  hi\n     2  \n     3  hellono smile for the wicked\n"),
                         ((1, 0, 0), "     1  hi\n\n     2  hello8)\n"),
                         ((1, 0, 1), "     1  hi\n\n     2  hellono smile for the wicked\n"),
                         ((1, 1, 0), "     1  hi\n\n     2  hello8)\n"),
                         ((1, 1, 1), "     1  hi\n\n     2  hellono smile for the wicked\n")]


def idfn(val):
    if isinstance(val, tuple):
        return str(val)


@pytest.mark.parametrize('flags, expect', flags_and_expect_list, ids=idfn)
def test_default_files_and_variable_flags(flags, expect, monkeypatch, nonempty_stream, capsys):
    monkeypatch.setattr('sys.stdin', nonempty_stream)

    def args_gen():
        args_tuple = namedtuple('args', ['files', 'number_nonblank', 'number', 'smile_exterminator'])
        return args_tuple(sys.stdin, *flags)

    monkeypatch.setattr(main, "parse_args", args_gen)

    main.main()

    captured = capsys.readouterr()
    assert captured.out == expect


def test_files(monkeypatch, files_list_gen, capsys):
    def args_gen():
        args_tuple = namedtuple('args', ['files', 'number_nonblank', 'number', 'smile_exterminator'])
        return args_tuple(files_list_gen, 1, 1, 1)

    monkeypatch.setattr(main, "parse_args", args_gen)

    main.main()

    captured = capsys.readouterr()
    expected = '     1  hi\n\n' \
               '     2  hellono smile for the wicked\n' \
               'cat: {}: Это каталог\n' \
               'cat: nothing: Нет такого файла или каталога\n'.format(files_list_gen[1])
    assert captured.out == expected
