import sys


def steam_reader(input_stream, number_nonblank_flag=0, number_flag=0):
    start_line_number = 1
    if number_nonblank_flag:
        transform = number_nonblank(start_line_number)
    elif number_flag:
        transform = number(start_line_number)
    else:
        transform = lambda x: x
    for line in input_stream:
        sys.stdout.write(transform(line))


def files_reader(files_list, number_nonblank_flag=0, number_flag=0):
    for file in files_list:
        try:
            with open(file, "r", errors='replace') as src:
                steam_reader(src, number_nonblank_flag, number_flag)
        except FileNotFoundError:
            print(f"cat: {file}: Нет такого файла или каталога")
        except IsADirectoryError:
            print(f"cat: {file}: Это каталог")


def number(current_line_number):
    def formater(line):
        nonlocal current_line_number
        formatted_line = "%+6s" % str(current_line_number) + "  " + line
        current_line_number += 1
        return formatted_line

    return formater


def number_nonblank(current_line_number):
    def formater(line):
        nonlocal current_line_number
        if line == "\n":
            return line
        else:
            formatted_line = number(current_line_number)(line)
            current_line_number += 1
            return formatted_line

    return formater


if __name__ == "__main__":
    files_reader([__file__], number_nonblank_flag=1, number_flag=1)
    files_reader([__file__], number_nonblank_flag=1, number_flag=0)
    files_reader([__file__], number_nonblank_flag=0, number_flag=1)
    files_reader([__file__])
    with open(__file__, "r") as file:
        steam_reader(file, number_nonblank_flag=0, number_flag=1)
    print(number(100500)("hello world"))
    print(number(100500)("\n"))
    print(number_nonblank(100500)("hello world"))
    print(number_nonblank(100500)("\n"))
