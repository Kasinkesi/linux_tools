import sys
import os
import io

try:
    import cat.lib.cat as cat
except:
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    from lib import cat


def test_empty_string_and_no_transform(capsys, empty_stream):
    cat.stream_printer(empty_stream)
    captured = capsys.readouterr()
    expected = ""
    assert captured.out == expected


def test_nonempty_string_and_no_transform(capsys, nonempty_stream):
    cat.stream_printer(nonempty_stream)
    captured = capsys.readouterr()
    expected = "hi\n\nhello8)\n"
    assert captured.out == expected


def test_nonempty_string_and_transform(capsys, nonempty_stream, transform_b_n_s_unused):
    cat.stream_printer(nonempty_stream, transform_b_n_s_unused)
    captured = capsys.readouterr()
    expected = '     1  hi\n\n     2  hellono smile for the wicked\n'
    assert captured.out == expected


def test_empty_string_and_unused_transform(capsys, empty_stream, transform_b_n_s_unused):
    cat.stream_printer(empty_stream, transform_b_n_s_unused)
    captured = capsys.readouterr()
    expected = ""
    assert captured.out == expected


def test_empty_string_and_used_transform(capsys, empty_stream, transform_b_n_s_used):
    cat.stream_printer(empty_stream, transform_b_n_s_used)
    captured = capsys.readouterr()
    expected = 'функция преобразования строки не может быть использована повторно, ' \
               'воспользуйтесь функцией transform_config\n'
    assert captured.out == expected
