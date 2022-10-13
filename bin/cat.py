import argparse
import sys

parser = argparse.ArgumentParser(description="cat.py - объединяет файлы и направляет их на стандартный вывод.")
parser.add_argument('files', nargs='*', default=sys.stdin)
args = parser.parse_args()

if args.files == sys.stdin:
    for line in sys.stdin:
        sys.stdout.write(line)
        # print(line, end="")

else:
    for file in args.files:
        try:
            with open(file, "r", errors='replace') as src:
                for line in src:
                    sys.stdout.write(line)
                    # print(line, end="")
        except FileNotFoundError:
            print(f"cat: {file}: Нет такого файла или каталога")
        except IsADirectoryError:
            print(f"cat: {file}: Это каталог")
