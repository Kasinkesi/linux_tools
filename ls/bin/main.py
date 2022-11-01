import argparse
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from lib import ls


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
        sort_format = ls.sort_revers
    else:
        sort_format = sorted

    if args.l:
        verbose_format = ls.long_verbose
    else:
        verbose_format = None

    files_list, indir_dict = ls.files_and_indirs(args.paths, sort_format=sort_format)

    ls.files_print(files_list, sort_format=sort_format, verbose_format=verbose_format)

    if args.R:
        ls.dirs_print_recursive(indir_dict, sort_format=sort_format, verbose_format=verbose_format)
    else:
        ls.dirs_print(indir_dict, sort_format=sort_format, verbose_format=verbose_format)




if __name__ == '__main__':
    exit(main())
