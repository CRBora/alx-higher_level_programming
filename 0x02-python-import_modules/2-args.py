#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    if len(argv) > 1:

        arg_len = len(argv) - 1

        if arg_len == 1:
            print("{} argument".format(arg_len))
        else:
            print("{} arguments".format(arg_len))


        for l, arg in enumerate(argv[1: ], start=1):
            print("{}: {}".format(l, arg))

    else:
        print("0 arguments.")
