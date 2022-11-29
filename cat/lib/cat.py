import sys
import re
#enumerate + filter

def transform_config(number_nonblank_flag=0, number_flag=0, smile_exterminator_flag=0):
    """
    На вход получает значения предусмотренных флагов, в зависимости от них настривает функцию преобразования строки
    """
    if number_nonblank_flag:
        transform = number_nonblank()
    elif number_flag:
        transform = number()
    else:
        transform = None

    if smile_exterminator_flag and transform != None:
        transform = smile_exterminator_decorator(transform)
    elif smile_exterminator_flag and transform == None:
        transform = smile_exterminator


    if transform != None:
        transform.used = False

    return transform


def stream_printer(input_stream, transform):
    """
    На вход получает входной поток и функцию преобразования строки,
    если функция преобразования строки определена,
    то проверяется что она не была раньше использована,
    то каждая строка преобразуется с помощью неё, затем отправляется на выходной поток,
    после чего помечает функцию преоразования строки использованной,
    если функция была раньше использовала, то печатается соответствующее сообщение,
    если функция не определена строки отправляются на выходной поток как есть
    """
    # здесь бы хорошо выставлять номер первой строки в единицу
    if transform:
        if transform.used == False:
            for line in input_stream:
                sys.stdout.write(transform(line))
            transform.used = True
        else:
            print("функция преобразования строки не может быть использована повторно, "
                  "воспользуйтесь функцией transform_config")
    else:
        for line in input_stream:
            sys.stdout.write(line)


def files_reader(files_list, transform):
    """
    На вход получает список файлов, если этот файл существует или это не каталог,
    то открывает эти файлы и передает файловый объект функции печати потока,
    в противном случае печатает сообщение об ошибке
    """
    for file in files_list:
        try:
            with open(file, "r", errors='replace') as src:
                stream_printer(src, transform)
        except FileNotFoundError:
            print(f"cat: {file}: Нет такого файла или каталога")
        except IsADirectoryError:
            print(f"cat: {file}: Это каталог")


def number():
    """
    Устанавливает текущее значение пумерации первой строки на 1
    Возвращает функцию преобразования строки
    """
    current_line_number = 1

    def transform(line):
        """
        На вход получает строку, преобразует её к требуемому виду, инкрементирует значение текущей строки
        и возвращает преобразованную строку
        """
        nonlocal current_line_number
        formatted_line = "%+6s" % str(current_line_number) + "  " + line
        current_line_number += 1
        return formatted_line

    return transform


def number_nonblank():
    """
    Устанавливает текущее значение пумерации первой строки на 1
    Возвращает функцию преобразования строки
    """
    current_line_number = 1

    def transform(line):
        """
        На вход получает строку, если строка пустая, то возвращает её как есть,
        в противном случае преобразует её к требуемому виду, инкрементирует значение текущей строки
        и возвращает преобразованную строку
        """
        nonlocal current_line_number
        if line == "\n":
            return line
        else:
            formatted_line = "%+6s" % str(current_line_number) + "  " + line
            current_line_number += 1
            return formatted_line

    return transform


def smile_exterminator_decorator(func):
    def wrapper(line):
        line = func(line)
        sad_line = re.sub("8\)", "no smile for the wicked", line)
        return sad_line

    return wrapper


def smile_exterminator(line):
    sad_line = re.sub("8\)", "no smile for the wicked", line)
    return sad_line


if __name__ == "__main__":
    transform = transform_config(number_nonblank_flag=0, number_flag=0)
    files_reader([__file__], transform)
    transform = transform_config(number_nonblank_flag=0, number_flag=1)
    files_reader([__file__], transform)
    transform = transform_config(number_nonblank_flag=1, number_flag=0)
    files_reader([__file__], transform)
    transform = transform_config(number_nonblank_flag=1, number_flag=1)
    files_reader([__file__], transform)
    transform = transform_config(number_nonblank_flag=1, number_flag=1, smile_exterminator_flag=1)
    with open(__file__, "r") as file:
        stream_printer(file, transform)
    with open(__file__, "r") as file:
        stream_printer(file, transform)
    print(number()("hello world"))
    print(number()("\n"))
    print(number_nonblank()("hello world"))
    print(number_nonblank()("\n"))

# 8)
