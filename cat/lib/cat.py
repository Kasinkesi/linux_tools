import sys


def steam_reader(input_stream, number_nonblank_flag=0, number_flag=0):
    if number_nonblank_flag:
        transform = number_nonblank
    elif number_flag:
        transform = number
    else:
        transform = lambda x, n: x
    current_line_number = [0]
    for line in input_stream:
        sys.stdout.write(transform(line, current_line_number))


def files_reader(files_list, number_nonblank_flag=0, number_flag=0):
    for file in files_list:
        try:
            with open(file, "r", errors='replace') as src:
                steam_reader(src, number_nonblank_flag, number_flag)
        except FileNotFoundError:
            print(f"cat: {file}: Нет такого файла или каталога")
        except IsADirectoryError:
            print(f"cat: {file}: Это каталог")


def number(line, current_line_number):
    current_line_number[0] += 1
    return "%+6s" % str(current_line_number[0]) + "  " + line


def number_nonblank(line, current_line_number):
    if line == "\n":
        return line
    else:
        return number(line, current_line_number)


if __name__ == "__main__":
    files_reader([__file__], number_nonblank_flag=1, number_flag=1)
    files_reader([__file__], number_nonblank_flag=1, number_flag=0)
    files_reader([__file__], number_nonblank_flag=0, number_flag=1)
    files_reader([__file__])
    with open(__file__, "r") as file:
        steam_reader(file, number_nonblank_flag=0, number_flag=1)
    print(number("hello world", [100500]))
    print(number("\n", [100500]))
    print(number_nonblank("hello world", [100500]))
    print(number_nonblank("\n", [100500]))
