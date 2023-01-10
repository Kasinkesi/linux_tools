import sys


def count_printer(out, count, prev):
    out.write(f'{count:>6} {prev}')


def no_count_printer(out, count, prev):
    out.write(prev)


def uniq(inp, out, flag, count_flag, skip_num, check_num):
    prev = inp.readline()
    if skip_num:
        prev_compare = prev[skip_num:]
    elif check_num:
        prev_compare = prev[:check_num]
    else:
        prev_compare = prev

    count = 1
    if count_flag:
        line_printer = count_printer
    else:
        line_printer = no_count_printer

    for curr in inp:
        if skip_num:
            curr_compare = curr[skip_num:]
        elif check_num:
            curr_compare = curr[:check_num]
        else:
            curr_compare = curr

        if curr_compare == prev_compare:
            count += 1
            if flag == "all repeated":
                out.write(prev)

        elif curr_compare != prev_compare and count == 1:
            if flag == "no flags" or flag == "only uniq":
                line_printer(out, count, prev)

            prev_compare = curr_compare
            prev = curr
            count = 1


        elif curr_compare != prev_compare and count >= 2:
            if flag == "no flags" or flag == "repeated" or flag == "all repeated":
                line_printer(out, count, prev)

            prev_compare = curr_compare
            prev = curr
            count = 1

    if flag == "no flags":
        line_printer(out, count, prev)
    elif flag == "only uniq" and count == 1:
        line_printer(out, count, prev)
    elif flag == "repeated" and count >= 2:
        line_printer(out, count, prev)
    elif flag == "all repeated" and count >= 2:
        line_printer(out, count, prev)


if __name__ == '__main__':
    # flag = "all repeated"
    # with open("../test/data/test_one", "r") as inp:
    #     uniq(inp, sys.stdout, flag)
    # print('\ntest two')
    # with open("../test/data/test_two", "r") as inp:
    #     uniq(inp, sys.stdout, flag)

    flag = "no flags"
    count_flag = True
    with open("../test/data/test_one", "r") as inp:
        uniq(inp, sys.stdout, flag, count_flag, skip_num=0, check_num=2)
    print('\ntest two')
    with open("../test/data/test_two", "r") as inp:
        uniq(inp, sys.stdout, flag, count_flag, skip_num=1, check_num=0)
