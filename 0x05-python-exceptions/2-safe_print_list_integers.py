#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    list_len = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                list_len += 1
    except (ValueError, TypeError):
        pass
    except IndexError:
        raise
    print()
    return list_len
