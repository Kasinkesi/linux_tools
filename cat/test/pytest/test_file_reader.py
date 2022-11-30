import sys
import os

try:
    import cat.lib.cat as cat
except:
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    from lib import cat


def test_not_file_list(capsys):
    cat.files_reader('not_a_files_list')
    captured = capsys.readouterr()
    expected = "list of files expected\n"
    assert captured.out == expected


def test_file_list_and_transform(capsys, files_list_gen, transform_b_n_s_unused):
    cat.files_reader(files_list_gen, transform_b_n_s_unused)
    captured = capsys.readouterr()
    expected = '     1  hi\n\n' \
               '     2  hellono smile for the wicked\n' \
               'cat: {}: Это каталог\n' \
               'cat: nothing: Нет такого файла или каталога\n'.format(files_list_gen[1])
    assert captured.out == expected
