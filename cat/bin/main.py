import sys


def steam_reader(input_stream, b, n):
    for line in input_stream:
        if b:
            sys.stdout.write(number_nonblank(line))
        elif n:
            sys.stdout.write(number(line))
        else:
            sys.stdout.write(line)


def files_reader(files_list, b, n):
    for file in files_list:
        try:
            with open(file, "r", errors='replace') as src:
                steam_reader(src, b, n)
        except FileNotFoundError:
            print(f"cat: {file}: Нет такого файла или каталога")
        except IsADirectoryError:
            print(f"cat: {file}: Это каталог")


def number(line, n=[]):
    if n == []:
        n.append(1)
    else:
        n[0] += 1
    return "%+6s" % str(n[0]) + "  " + line


def number_nonblank(line, n=[]):
    if line == "\n":
        return line
    else:
        return number(line, n)
