#!/usr/bash/python

import sys

while 1:
    value = raw_input("CALC:")

    if value == "exit":
        sys.exit(0)

    val1, val2, operation = value.split(" ")

    if operation == "plus":
        res = int(val1) + int(val2)
        print val1, "+", val2, "=", res

    if operation== "minus":
        res = int(val1) - int(val2)
        print val1, "-", val2, "=", res

    if operation== "times":
        res = int(val1) * int(val2)
        print val1, "x", val2, "=", res
