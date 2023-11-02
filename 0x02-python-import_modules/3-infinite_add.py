#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    if len(argv) > 1:

        sum_arg = 0

        for arg in argv[1:]:
            sum_arg += int(arg)
        print(sum_arg)
    else:
        print("0")
