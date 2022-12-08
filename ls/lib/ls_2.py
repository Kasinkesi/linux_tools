"""
oficial ls sort "_" not like python
"""

import os
import stat
import os.path
import pwd
import grp
import time
import math
import sys


def files_and_dirs(data_list, sort_format):
    """
    ПРИНИМАЕТ список состоящий из файлов и директорий, функцию форматирования,
    ВОЗВРАЩАЕТ кортеж из отсортированных списков файлов и директорий
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
    return sort_format(files_list), sort_format(dirs_list)


def basename_print(paths_list, long_verbose_flag):
    """
    ПРИНИМАЕТ список путей к файлам или директориям, флаг расширенного вывода,
    печать форматированного вывода в зависимости от long_verbose_flag
    """
    if not paths_list:
        pass
    else:
        if long_verbose_flag:
            for path in paths_list:
                print(long_verbose(path))
        else:
            for path in paths_list:
                print(os.path.basename(path), end='  ')
            print()


def dirs_print(dirs_list, sort_format, long_verbose_flag, recursion_flag):
    """
    ПРИНИМАЕТ список директорий, флаг расширенного вывода, и флаг рекурсивного обхода,
    для каждой директориий печатает название директории,
    в случае флага расширенного вывода выводит объем директории,
    и передает содержимое директрии функциям files_and_dirs и basename_print,
    в случае флага рекурсивного обхода, рекурсивно углубляется во все найденные директории
    """
    for dir_name in dirs_list:
        if recursion_flag == 1:
            print(f"{dir_name}:")
        indir_list = os.listdir(dir_name)

        # собирает список из относительных путей до содержимого директории
        indir_path_list = [os.path.join(dir_name, indir_name) for indir_name in indir_list]

        if long_verbose_flag:
            volume_calculate(indir_path_list)

        files_list, dirs_list = files_and_dirs(indir_path_list, sort_format=sort_format)
        basename_print(sort_format(files_list + dirs_list), long_verbose_flag)

        if recursion_flag:
            print()
            dirs_print(dirs_list, sort_format, long_verbose_flag, recursion_flag)


def volume_calculate(indir_path_list):
    """
    ПРИНИМАЕТ список путей,
    отправляет на печать кратную 4кБ сумму размеров диреторий
    """
    volume = 0
    for indir_path in indir_path_list:
        volume += 4 * math.ceil(os.stat(indir_path).st_size / 4096)
    print(f"Итого {volume}")


def long_verbose(pathname):
    """
    ПРИНИМАЕТ путь к файлу или директории
    ВОЗВРАЩАЕТ подготовленную для печати строку
    """
    stat_info = os.stat(pathname)
    return (f"{stat.filemode(stat_info.st_mode)} {stat_info.st_nlink} {pwd.getpwuid(stat_info.st_uid).pw_name} "
            f"{grp.getgrgid(stat_info.st_uid).gr_name} {stat_info.st_size:>4} "
            f"{time.strftime('%b %d %H:%M', time.localtime(stat_info.st_mtime))} {os.path.basename(pathname)}")


def basename_sort(path_list):
    return sorted(path_list, key=os.path.basename)


def basename_sort_revers(path_list):
    return sorted(path_list, key=os.path.basename, reverse=True)


def sort_reverse(any_array):
    return sorted(any_array, reverse=True)


if __name__ == "__main__":
    # data_only_curent = ['..']
    data_full = ['.', '..', 'ls_2.py', 'ls.py', 'fail_file']
    # data_only_files = ['ls.py', 'fail_file']
    # data_only_dirs = ['.', '..', 'fail_file']
    # start_from_here = ['.']
    # my_project = ['/home/doka/projects/linux_tools']

    # print(files_and_indirs(data_full))
    # print(files_and_indirs(data_only_files))
    # print(files_and_indirs(data_only_dirs))

    files_list, dirs_list = files_and_dirs(data_full, sort_format=basename_sort)
    # print(files_and_dirs(data_full, sort_format=sorted))
    basename_print(files_list, long_verbose_flag=1)
    dirs_print(dirs_list, sort_format=sorted, long_verbose_flag=1, recursion_flag=1)

    # print("dirs_print(recursive_indir_dict)")
    # dirs_print(recursive_indir_dict(data_full))

    # files_print(files_list,sort_format=sort_revers, verbose_format=long_verbose)
    # dirs_print(indir_dict,sort_format=sorted, verbose_format=None)
    # print("dirs_print_recursive(indir_dict")
    # dirs_print_recursive(indir_dict)

    # print(long_verbose('.'))
    # print()

    # print("selfmade_recursive")
    # selfmade_recursive(data_full)

string_list = ["hi hi", "hello  ", "  hio"]
