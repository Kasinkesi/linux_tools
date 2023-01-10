import sys


def uniq(inp, out, param):
    prev = inp.readline()
    repeat_flag = False
    for curr in inp:
        if curr == prev:
            repeat_flag = True
            if param == "all repeated":
                out.write(prev)

        elif curr != prev and not repeat_flag:
            if param == "no flags" or param == "only uniq":
                out.write(prev)

            prev = curr


        elif curr != prev and repeat_flag:
            repeat_flag = False

            if param == "no flags" or param == "repeated" or param == "all repeated":
                out.write(prev)

            prev = curr

    if param == "no flags":
        out.write(prev)
    elif param == "only uniq" and not repeat_flag:
        out.write(prev)
    elif param == "repeated" and repeat_flag:
        out.write(prev)
    elif param == "all repeated" and repeat_flag:
        out.write(prev)


def count_printer(out, count, prev):
    out.write(f'{count:>6} {prev}')

def counter(inp, out, param):
    prev = inp.readline()
    repeat_flag = False
    count = 1
    for curr in inp:
        if curr == prev:
            repeat_flag = True
            count += 1
            if param == "all repeated":
                out.write(prev)

        elif curr != prev and not repeat_flag:
            if param == "no flags" or param == "only uniq":
                count_printer(out, count, prev)

            prev = curr
            count = 1


        elif curr != prev and repeat_flag:
            repeat_flag = False

            if param == "no flags" or param == "repeated" or param == "all repeated":
                count_printer(out, count, prev)

            prev = curr
            count = 1

    if param == "no flags":
        count_printer(out, count, prev)
    elif param == "only uniq" and not repeat_flag:
        count_printer(out, count, prev)
    elif param == "repeated" and repeat_flag:
        count_printer(out, count, prev)
    elif param == "all repeated" and repeat_flag:
        count_printer(out, count, prev)


if __name__ == '__main__':
    # flag = "all repeated"
    # with open("../test/data/test_one", "r") as inp:
    #     uniq(inp, sys.stdout, flag)
    # print('\ntest two')
    # with open("../test/data/test_two", "r") as inp:
    #     uniq(inp, sys.stdout, flag)

    flag = "repeated"
    with open("../test/data/test_one", "r") as inp:
        counter(inp, sys.stdout, flag)
    print('\ntest two')
    with open("../test/data/test_two", "r") as inp:
        counter(inp, sys.stdout, flag)
