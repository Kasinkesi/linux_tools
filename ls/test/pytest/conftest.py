import pytest
import os


@pytest.fixture()
def only_files_list(tmpdir):
    a_file = tmpdir.join('a_file')
    a_file.write('a_file')
    b_file = tmpdir.join('_b_file')
    b_file.write('b_file')
    c_file = tmpdir.join('c_file')
    c_file.write('c_file')
    return [c_file, a_file, b_file]


@pytest.fixture()
def only_dirs_list(tmpdir):
    a_dir = tmpdir.mkdir('a_dir')
    b_dir = tmpdir.mkdir('_b_dir')
    c_dir = tmpdir.mkdir('c_dir')
    return [c_dir, a_dir, b_dir]


@pytest.fixture()
def mixed_list(tmpdir):
    a_file = tmpdir.join('a_file')
    a_file.write('a_file')
    b_file = tmpdir.join('_b_file')
    b_file.write('b_file')
    c_file = tmpdir.join('c_file')
    c_file.write('c_file')

    a_dir = tmpdir.mkdir('a_dir')
    b_dir = tmpdir.mkdir('_b_dir')
    c_dir = tmpdir.mkdir('c_dir')
    return [c_file, c_dir, a_dir, a_file, b_file, b_dir]


@pytest.fixture()
def empty_dir_list(tmpdir):
    return [tmpdir]


@pytest.fixture()
def path_to_data():
    return os.path.join(os.path.dirname(__file__), "..", "data")
