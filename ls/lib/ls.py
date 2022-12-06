import copy
import os
import stat
import os.path
import pwd
import grp
import time


def files_and_indirs(data_list, sort_format=None):
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
    if sort_format != None:
        for dir_name in sort_format(dirs_list):
            indir_dict[dir_name] = os.listdir(dir_name)
        return sort_format(files_list), indir_dict
    else:
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
            print(file, end='  \n')
    # print()


def dirs_print(indir_dict, sort_format=None, verbose_format=None):
    """
    ПРИНИМАЕТ словарь где ключ это название директории, а значение - названия содержимого этой директории,
    печатает название директорий и их содержимое
    """
    if sort_format != None:
        indir_list = sort_format(indir_dict)
    else:
        indir_list = list(indir_dict)

    if verbose_format != None:
        for dir_name in indir_list:
            if len(indir_list) > 1 and dir_name != '.':
                print(f"\n{dir_name}:")
            for data in indir_dict[dir_name]:
                print(verbose_format(os.path.join(dir_name, data)), end='  ')
                print()
    else:
        for dir_name in indir_list:
            if len(indir_list) > 1:  # and dir_name != '.'
                print(f"\n{dir_name}:")
            # print(*indir_dict[dir_name])
            for data in indir_dict[dir_name]:
                print(data, end='  ')
            print()
    print()


def selfmade_recursive(data_list, sort_format=None, verbose_format=None):
    files_list, indir_dict = files_and_indirs(data_list, sort_format)
    files_print(files_list, sort_format, verbose_format)
    dirs_print(indir_dict, sort_format, verbose_format)
    for k, v in indir_dict.items():
        for v_path in v:
            dir_path = os.path.join(k, v_path)
            if os.path.isdir(dir_path):
                print(f"{dir_path}:")
                selfmade_recursive([dir_path], sort_format, verbose_format)


def recursive_indir_dict(indir_dict):
    """
    ПРИНИМАЕТ словарь где ключ это название директории, а значение - названия содержимого этой директории,
    ВОЗВРАЩАЕТ
    """
    indir_dict_rec = {}
    for dir_name in indir_dict:
        for cur_dir, dirs_list_recursive, files_list_recursive in os.walk(dir_name):
            indir_dict_rec[cur_dir] = files_list_recursive + dirs_list_recursive
    return indir_dict_rec


def dirs_print_recursive(indir_dict, sort_format=None, verbose_format=None):
    """
    ПРИНИМАЕТ словарь где ключ это название директории, а значение - названия содержимого этой директории,
    рекурсивно углубляется во все директории которые встречаются,
    печатает название директорий и их содержимое
    """
    for dir_name in indir_dict:
        for cur_dir, dirs_list_recursive, files_list_recursive in os.walk(dir_name):
            indir_list = []
            for file_recursive in files_list_recursive:
                indir_list.append(os.path.join(cur_dir, file_recursive))
            for dir_recursive in dirs_list_recursive:
                indir_list.append(os.path.join(cur_dir, dir_recursive))

            if sort_format != None:
                indir_list = sort_format(indir_list)
            if verbose_format != None:
                print(f"\n{cur_dir}:")
                for indir in indir_list:
                    print(verbose_format(indir), end='  ')
                    print()
            else:
                print(f"\n{cur_dir}:")
                # print(*indir_list)
                for indir in indir_list:
                    print(os.path.split(indir)[1], end='  ')
                print()
    print()


def long_verbose(pathname):
    """
    ПРИНИМАЕТ путь к файлу или директории
    ВОЗВРАЩАЕТ подготовленную для печати строку
    """
    stat_info = os.stat(pathname)
    return (f"{stat.filemode(stat_info.st_mode)} {stat_info.st_nlink} {pwd.getpwuid(stat_info.st_uid).pw_name} "
            f"{grp.getgrgid(stat_info.st_uid).gr_name} {stat_info.st_size:>4} "
            f"{time.strftime('%b %d %H:%M', time.localtime(stat_info.st_mtime))} {os.path.split(pathname)[1]}")


def sort_revers(any_array):
    return sorted(any_array, reverse=True)


if __name__ == "__main__":
    data_only_curent = ['..']
    data_full = ['.', '..', 'ls.py', 'fail_file']
    data_only_files = ['ls.py', 'fail_file']
    data_only_dirs = ['.', '..', 'fail_file']
    start_from_here = ['.']
    my_project = ['/home/doka/projects/linux_tools']

    # print(files_and_indirs(data_full))
    # print(files_and_indirs(data_only_files))
    # print(files_and_indirs(data_only_dirs))

    files_list, indir_dict = files_and_indirs(data_full)

    print("dirs_print(recursive_indir_dict")
    dirs_print(recursive_indir_dict(data_full))

    # files_print(files_list,sort_format=sort_revers, verbose_format=long_verbose)
    # dirs_print(indir_dict,sort_format=sorted, verbose_format=None)
    print("dirs_print_recursive(indir_dict")
    dirs_print_recursive(indir_dict)

    # print(long_verbose('.'))
    # print()

    print("selfmade_recursive")
    selfmade_recursive(data_full)

string_list = ["hi hi", "hello  ", "  hio"]
