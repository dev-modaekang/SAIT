#!/usr/bash/python

import sys
sys.argv

if len(sys.argv)<2:
    print "want some arguments"
    sys.exit(-1)

val1 = sys.argv[1]
val2 = sys.argv[2]
operation = sys.argv[3]

if operation == "plus":
    res = int(val1) + int(val2)
    print val1, "+", val2, "=", res

if operation== "minus":
    res = int(val1) - int(val2)
    print val1, "-", val2, "=", res

if operation== "times":
    res = int(val1) * int(val2)
    print val1, "x", val2, "=", res

