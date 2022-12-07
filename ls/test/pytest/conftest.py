import pytest

@pytest.fixture()
def dir_list_gen(tmpdir):
    sixteen_KB_file_1 = tmpdir.join('sixteen_KB_file_1')
    sixteen_KB_file_1.write(bin(1 << 14))
    empty_dir_1 = tmpdir.mkdir('empty_dir_1')
    non_empty_dir_1 = tmpdir.mkdir('non_empty_dir_1')

    less_sixteen_KB_file_2 = non_empty_dir_1.join('less_sixteen_KB_file_2')
    less_sixteen_KB_file_2.write(bin((1 << 14) - 1))
    empty_dir_2 = non_empty_dir_1.mkdir('empty_dir_2')
    non_empty_dir_2 = non_empty_dir_1.mkdir('non_empty_dir_2')

    more_sixteen_KB_file_3 = non_empty_dir_2.join('more_sixteen_KB_file_3')
    more_sixteen_KB_file_3.write(bin((1 << 14) - 1))
    empty_dir_3 = non_empty_dir_2.mkdir('empty_dir_3')

    dir_list = [sixteen_KB_file_1, empty_dir_1, non_empty_dir_1, less_sixteen_KB_file_2,
                  empty_dir_2, non_empty_dir_2, more_sixteen_KB_file_3, empty_dir_3, "not_file_or_dir"]

    return dir_list


@pytest.fixture()
def nonempty_dir(tmpdir):
    sixteen_KB_file_1 = tmpdir.join('sixteen_KB_file_1')
    sixteen_KB_file_1.write(bin(1 << 14))
    empty_dir_1 = tmpdir.mkdir('empty_dir_1')
    non_empty_dir_1 = tmpdir.mkdir('non_empty_dir_1')

    less_sixteen_KB_file_2 = non_empty_dir_1.join('less_sixteen_KB_file_2')
    less_sixteen_KB_file_2.write(bin((1 << 14) - 1))
    empty_dir_2 = non_empty_dir_1.mkdir('empty_dir_2')
    non_empty_dir_2 = non_empty_dir_1.mkdir('non_empty_dir_2')

    more_sixteen_KB_file_3 = non_empty_dir_2.join('more_sixteen_KB_file_3')
    more_sixteen_KB_file_3.write(bin((1 << 14) - 1))
    empty_dir_3 = non_empty_dir_2.mkdir('empty_dir_3')

    return [tmpdir, "not_file_or_dir"]


@pytest.fixture()
def empty_dir(tmpdir):
    return [tmpdir, "not_file_or_dir"]