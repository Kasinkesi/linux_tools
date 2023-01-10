import argparse
import sys
import os

try:
    from uniq.lib import uniq_3
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    from lib import uniq_3


def parse_args():
    parser = argparse.ArgumentParser(description="Удаляет все кроме одной повторяющиеся строки из ВВОДА (или "
                                                 "стандартного ввода) и печатает на ВЫВОД (или стандартный вывод).")
    parser.add_argument("inp", default=sys.stdin, help="input source")
    parser.add_argument("out", nargs='?', default=sys.stdout, help="destination")
    parser.add_argument("-c", "--count", dest="count", action="store_true",
                        help="выводить число повторов в начале каждой строки")
    parser.add_argument("-u", "--unique", action="store_true",
                        help="выводить только неповторяющиеся строки")
    parser.add_argument("-d", "--repeated", action="store_true",
                        help="выводить только повторяющиеся строки")
    parser.add_argument("-D", "--all-repeated", dest="all_repeated", action="store_true",
                        help="печатать все повторяющиеся строки")
    parser.add_argument("-s", "--skip-chars", dest="skip_chars", type=int, default=0,
                        help="не сравнивать первые N знаков в строке")
    parser.add_argument("-w", "--check-chars", dest="check_chars", type=int, default=0,
                        help="сравнивать только первые N символов в строке")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    if args.count and args.all_repeated:
        print("uniq: вывод всех повторяющихся строк и числа повторений не имеет смысла")
    else:
        if args.unique:
            flag = "only uniq"
        elif args.repeated:
            flag = "repeated"
        elif args.all_repeated:
            flag = "all repeated"
        else:
            flag = "no flags"

        try:
            if args.inp != sys.stdin:
                with open(args.inp, "r") as inp:
                    if args.out != sys.stdout:
                        with open(args.out, "w") as out:
                            uniq_3.uniq(inp, out, flag, args.count, args.skip_chars, args.check_chars)
                    else:
                        uniq_3.uniq(inp, args.out, flag, args.count, args.skip_chars, args.check_chars)
            else:
                uniq_3.uniq(args.inp, args.out, flag, args.count, args.skip_chars, args.check_chars)
        except IsADirectoryError:
            print(f"uniq: {args.inp}: Это каталог")
        except FileNotFoundError:
            print(f"uniq: {args.inp}: Нет такого файла или каталога")


if __name__ == '__main__':
    exit(main())
