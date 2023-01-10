import sys


def count_printer(out, count, prev):
    out.write(f'{count:>6} {prev}')


"no flags"


def uniq_line_printer(inp, out):
    first_line = inp.readline()
    prev_line = first_line
    for line in inp:
        if line != prev_line:
            out.write(prev_line)
            prev_line = line
    out.write(prev_line)


"-c"


def uniq_line_counter(inp, out):
    first_line = inp.readline()
    prev_line = first_line
    count = 1
    for line in inp:
        if line != prev_line:
            count_printer(out, count, prev_line)
            prev_line = line
            count = 1
        else:
            count += 1
    count_printer(out, count, prev_line)


"-u"


def only_uniq_line_printer(inp, out):
    first_line = inp.readline()
    prev_line = first_line
    repeat_flag = False
    for line in inp:
        if line == prev_line:
            repeat_flag = True
        elif line != prev_line and not repeat_flag:
            out.write(prev_line)
            prev_line = line
        else:
            repeat_flag = False
            prev_line = line
    if not repeat_flag:
        out.write(prev_line)


"-cu"


def only_uniq_line_counter(inp, out):
    first_line = inp.readline()
    prev_line = first_line
    count = 1
    for line in inp:
        if line == prev_line:
            count += 1
        elif line != prev_line and count == 1:
            count_printer(out, count, prev_line)
            prev_line = line
        else:
            count = 1
            prev_line = line
    if count == 1:
        count_printer(out, count, prev_line)


"-d"


def repeated_line_printer(inp, out):
    first_line = inp.readline()
    prev_line = first_line
    repeat_flag = False
    for line in inp:
        if line == prev_line:
            repeat_flag = True
        elif line != prev_line and repeat_flag:
            out.write(prev_line)
            prev_line = line
            repeat_flag = False
        else:
            prev_line = line
    if repeat_flag:
        out.write(prev_line)


"-cd"


def repeated_line_counter(inp, out):
    first_line = inp.readline()
    prev_line = first_line
    count = 1
    for line in inp:
        if line == prev_line:
            count += 1
        elif line != prev_line and count >= 2:
            count_printer(out, count, prev_line)
            prev_line = line
            count = 1
        else:
            prev_line = line
    if count >= 2:
        count_printer(out, count, prev_line)


"-D"


def repeated__all_line_printer(inp, out):
    first_line = inp.readline()
    prev_line = first_line
    repeat_flag = False
    for line in inp:
        if line == prev_line:
            out.write(prev_line)
            repeat_flag = True
        elif line != prev_line and repeat_flag:
            out.write(prev_line)
            repeat_flag = False
        else:
            prev_line = line
            repeat_flag = False
    if repeat_flag:
        out.write(prev_line)


if __name__ == '__main__':
    with open("../test/data/test_one", "r") as inp:
        uniq_line_printer(inp, sys.stdout)
    print("\nonly uniq")
    with open("../test/data/test_one", "r") as inp:
        only_uniq_line_printer(inp, sys.stdout)
    print("\ncounter")
    with open("../test/data/test_one", "r") as inp, open("../test/data/test_three", "w") as out:
        repeated_line_counter(inp, sys.stdout)
    print("\nrepeated")
    with open("../test/data/test_one", "r") as inp:
        repeated_line_printer(inp, sys.stdout)
    print("\nall repeated")
    with open("../test/data/test_one", "r") as inp:
        repeated__all_line_printer(inp, sys.stdout)
