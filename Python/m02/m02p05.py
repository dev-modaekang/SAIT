#!/usr/bash/python

#!/usr/bash/python

import sys

val1 = input("First Number:")
val2 = input("Second Number:") 
operation = raw_input("Operation:")

if operation == "plus":
    res = int(val1) + int(val2)
    print val1, "+", val2, "=", res

if operation== "minus":
    res = int(val1) - int(val2)
    print val1, "-", val2, "=", res

if operation== "times":
    res = int(val1) * int(val2)
    print val1, "x", val2, "=", res

