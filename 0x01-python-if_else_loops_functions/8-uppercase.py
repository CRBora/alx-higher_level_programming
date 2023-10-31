#!/usr/bin/python3

def uppercase(str):
    upp_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            upp_char = chr(ord(char) - 32)
            upp_str += upp_char
        else:
            upp_str += char
    print("{}".format(upp_str))
