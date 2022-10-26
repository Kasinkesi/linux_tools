import sys
import os
import os.path


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
            print(f'\n{data} не файл или директория')

    indir_dict = {}
    for dir_name in dirs_list:
        indir_dict[dir_name] = os.listdir(dir_name)

    return files_list, indir_dict


def files_print(files_list):
    """
    ПРИНИМАЕТ список файлов ,
    печатает названия файлов с двумя пробелами без символа новой строки
    """
    for file in files_list:
        print(file, end='  ')
    print()

def dirs_print(indir_dict):
    """
    ПРИНИМАЕТ словарь где ключ это название директории, а значение - названия содержимого этой директории,
    печатает название директорий и их содержимое, с добавлением двух символов новой строки перед наазванием диретории
    """
    for dir_name in indir_dict:
        print(f"\n{dir_name}:")
        for data in indir_dict[dir_name]:
            print(data, end='  ')
        print()
    print()


def dirs_print_recursion(indir_dict):
    """
    ПРИНИМАЕТ словарь где ключ это название директории, а значение - названия содержимого этой директории,
    рекурсивно углубляется во все директории которые встречаются,
    печатает название директорий и их содержимое, с добавлением двух символов новой строки перед названием диретории
    """
    for dir_name in indir_dict:
        for cur_dir, dirs_list_recursive, files_list_recursion in os.walk(dir_name):
            print(f"\n{cur_dir}:")
            for dir_recursive in dirs_list_recursive:
                print(dir_recursive, end='  ')
            for file_recursion in files_list_recursion:
                print(file_recursion, end='  ')
            print()
    print()


if __name__ == "__main__":
    data_full = ['.', '..', 'ls.py', 'test']
    data_only_files = ['ls.py']
    data_only_dirs = ['.', '..', 'test']

    # print(files_and_indirs(data_full))
    # print(files_and_indirs(data_only_files))
    # print(files_and_indirs(data_only_dirs))


    files_list, indir_dict = files_and_indirs(data_full)
    files_print(files_list)
    dirs_print(indir_dict)
    dirs_print_recursion(indir_dict)
    # data_print(data_full)
    # data_print(data_only_files)
    # data_print(data_only_dirs)

    print(os.stat(__file__))
    print(os.stat('.'))
