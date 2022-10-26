import os
import stat
import os.path
import pwd
import grp
import time


def files_and_indirs(data_list):
    """
    ПРИНИМАЕТ список состоящий из файлов и директорий,
    разделяет файлы от директорий,
    собирает словарь из названий директорий и их содержимого,
    ВОЗВРАЩАЕТ кортеж из списка файлов из входного списка и словаря директорий
    """
    files_list = []
    dirs_list = []
    for data in data_list:
        if os.path.isdir(data):
            dirs_list.append(data)
        elif os.path.isfile(data):
            files_list.append(data)
        else:
            print(f'{data} не файл или директория')

    indir_dict = {}
    for dir_name in dirs_list:
        indir_dict[dir_name] = os.listdir(dir_name)

    return files_list, indir_dict


def files_print(files_list, sort_format=None, verbose_format=None):
    """
    ПРИНИМАЕТ список файлов ,
    печатает названия файлов с двумя пробелами без символа новой строки
    """
    if sort_format != None:
        files_list = sort_format(files_list)
    if verbose_format != None:
        for file in files_list:
            print(verbose_format(file), end='  ')
    else:
        # print(*files_list)
        for file in files_list:
            print(file, end='  ')
    print()


def dirs_print(indir_dict):
    """
    ПРИНИМАЕТ словарь где ключ это название директории, а значение - названия содержимого этой директории,
    печатает название директорий и их содержимое
    """
    for dir_name in indir_dict:
        print(f"\n{dir_name}:")
        # print(*indir_dict[dir_name])
        for data in indir_dict[dir_name]:
            print(data, end='  ')
        print()
    print()


def dirs_print_recursion(indir_dict):
    """
    ПРИНИМАЕТ словарь где ключ это название директории, а значение - названия содержимого этой директории,
    рекурсивно углубляется во все директории которые встречаются,
    печатает название директорий и их содержимое
    """
    for dir_name in indir_dict:
        for cur_dir, dirs_list_recursive, files_list_recursion in os.walk(dir_name):
            indir_list = []
            print(f"\n{cur_dir}:")
            for dir_recursive in dirs_list_recursive:
                indir_list.append(dir_recursive)
            for file_recursion in files_list_recursion:
                indir_list.append(file_recursion)

            # print(*indir_list)
            for indir in indir_list:
                print(indir, end='  ')
            print()
    print()


def long_verbose(pathname):
    """
    ПРИНИМАЕТ путь к файлу или директории
    ВОЗВРАЩАЕТ подготовленную для печати строку
    """
    stat_info = os.stat(pathname)
    return (f"{stat.filemode(stat_info.st_mode)} {stat_info.st_nlink} {pwd.getpwuid(stat_info.st_uid).pw_name} "
            f"{grp.getgrgid(stat_info.st_uid).gr_name} {stat_info.st_size} "
            f"{time.strftime('%b %d %H:%M', time.localtime(stat_info.st_mtime))} {pathname}")


if __name__ == "__main__":
    data_full = ['.', '..', 'ls.py', 'test']
    data_only_files = ['ls.py', 'test']
    data_only_dirs = ['.', '..', 'test']

    # print(files_and_indirs(data_full))
    # print(files_and_indirs(data_only_files))
    # print(files_and_indirs(data_only_dirs))

    files_list, indir_dict = files_and_indirs(data_full)
    files_print(files_list,sort_format=reversed, verbose_format=long_verbose)
    # dirs_print(indir_dict)
    # dirs_print_recursion(indir_dict)

    # print(long_verbose('.'))
    print()


string_list = ["hi hi", "hello  ", "  hio"]





