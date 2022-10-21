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
    parser.add_argument("-s", "--smile-exterminator", dest="smile_exterminator", action="store_true",
                        help="заменяет все '8)' из выходного файла  на 'no smile for the wicked' и делает доку грустным 8(")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    transform = cat.transform_config(args.number_nonblank, args.number, args.smile_exterminator)
    if args.files == sys.stdin:
        cat.stream_printer(sys.stdin, transform)
    else:
        cat.files_reader(args.files, transform)


if __name__ == '__main__':
    exit(main())
