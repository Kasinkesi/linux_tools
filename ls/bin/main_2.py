import argparse
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from lib import ls_2


def parse_args():
    parser = argparse.ArgumentParser(description="""cat.py - осначала выводит список всех файлов (не каталогов), 
    перечисленных в командной строке, а затем выводит список всех файлов, находящихся в каталогах, 
    перечисленных в командной строке.""")
    parser.add_argument("paths", nargs="*", default=["."],
                        help="""перечисление файлов и директорий. По умолчанию принята текущая директория.""")
    parser.add_argument("-l", action="store_true",
                        help="""Выдавать (в одноколоночном формате) тип файла, права доступа к файлу, количество ссылок
                        на файл, имя владельца, имя группы, размер файла (в байтах), временной штамп и имя файла.""")
    parser.add_argument("-R", action="store_true",
                        help="Включить рекурсивную выдачу списка каталогов.")
    parser.add_argument("-U", "--sort=none", dest="sort_none", action="store_true",
                        help="Не производить сортировку.")
    parser.add_argument("-r", "--reverse", action="store_true",
                        help="Сортировать содержимое каталога в обратном порядке.")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    if args.sort_none:
        sort_format = None
    elif args.reverse:
        sort_format = ls_2.basename_sort_revers
    else:
        sort_format = ls_2.basename_sort


    files_list, dirs_list = ls_2.files_and_dirs(args.paths, sort_format=sort_format)

    ls_2.basename_print(files_list, long_verbose_flag=args.l)
    ls_2.dirs_print(dirs_list, sort_format=sort_format, long_verbose_flag=args.l, recursion_flag=args.R)



if __name__ == '__main__':
    exit(main())
