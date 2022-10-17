import sys


def steam_reader(input_stream):
    for line in input_stream:
        sys.stdout.write(line)
        # print(line, end="")


def files_reader(files_list):
    for file in files_list:
        try:
            with open(file, "r", errors='replace') as src:
                steam_reader(src)
        except FileNotFoundError:
            print(f"cat: {file}: Нет такого файла или каталога")
        except IsADirectoryError:
            print(f"cat: {file}: Это каталог")
