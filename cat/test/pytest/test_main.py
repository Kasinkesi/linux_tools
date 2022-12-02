import sys
import os
from collections import namedtuple

try:
    from cat.bin import main
except:
    print("using alternative import")
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    from bin import main


def test_default_files(monkeypatch, nonempty_stream, capsys):
    monkeypatch.setattr('sys.stdin', nonempty_stream)

    def args_gen():
        args_tuple = namedtuple('args', ['files', 'number_nonblank', 'number', 'smile_exterminator'])
        return args_tuple(sys.stdin, 1, 1, 1)

    monkeypatch.setattr(main, "parse_args", args_gen)

    main.main()

    captured = capsys.readouterr()
    expected = '     1  hi\n\n     2  hellono smile for the wicked\n'
    assert captured.out == expected


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
