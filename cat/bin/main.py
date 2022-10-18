import argparse
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from lib import cat


def parse_args():
    parser = argparse.ArgumentParser(description="cat.py - объединяет файлы и направляет их на стандартный вывод.")
    parser.add_argument("files", nargs="*", default=sys.stdin,
                        help="""перечисление файлов для чтения(объеинения). Если ФАЙЛ не указан или вместо его имени стоит дефис (-), то производится чтение со стандартного ввода.""")
    parser.add_argument("-b", "--number-nonblank", dest="number_nonblank", action="store_true",
                        help="нумерует ВСЕ НЕПУСТЫЕ строки выходного файла, начиная c 1")
    parser.add_argument("-n", "--number", action="store_true",
                        help="нумерует ВСЕ строки выходного файла, начиная c 1")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.files == sys.stdin:
        cat.steam_reader(sys.stdin, args.number_nonblank, args.number)
    else:
        cat.files_reader(args.files, args.number_nonblank, args.number)


if __name__ == '__main__':
    exit(main())
