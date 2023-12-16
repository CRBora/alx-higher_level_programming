#!/usr/bin/python
def uniq_add(my_list=[]):
    unique_int = set()
    for element in my_list:
        if element not in unique_int:
            unique_int.add(element)
    return sum(unique_int)
