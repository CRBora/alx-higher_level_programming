#!/usr/bin/python3

def fizzbuzz():

    for l in range(1, 101):
        if l % 3 == 0 and l % 5 != 0:
            print(" Fizz", end="")
        elif l % 5 == 0 and l % 3 != 0:
            print(" Buzz", end="")
        elif l % 3 == 0 and l % 5 == 0:
            print(" FizzBuzz", end="")
        elif l == 1:
            print (l, end="")
        else:
            print(f" {l}", end="")
