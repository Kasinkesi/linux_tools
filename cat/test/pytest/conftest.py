import pytest
from collections import namedtuple
import io

try:
    import cat.lib.cat as cat
except:
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    from lib import cat


@pytest.fixture()
def empty_stream():
    t_string = io.StringIO("")
    return t_string


@pytest.fixture()
def nonempty_stream():
    t_string = io.StringIO("hi\n\nhello8)\n")
    return t_string


@pytest.fixture()
def args_gen(files, b_flag, n_flag, s_flag):
    args_tuple = namedtuple('args', ['files', 'number_nonblank', 'number', 'smile_exterminator'])
    return args_tuple(files, b_flag, n_flag, s_flag)


@pytest.fixture()
def transform_b_n_s_unused():
    transform = cat.transform_config(1, 1, 1)
    return transform


@pytest.fixture()
def transform_b_n_s_used():
    transform = cat.transform_config(1, 1, 1)
    transform.used = True
    return transform


@pytest.fixture()
def files_list_gen(tmpdir):
    a_file = tmpdir.join('nonemty_file.txt')
    a_dir = tmpdir.mkdir('a_dir')
    a_file.write("hi\n\nhello8)\n")
    files_list = [a_file, a_dir, "nothing"]
    return files_list
