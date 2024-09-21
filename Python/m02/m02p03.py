#!/usr/bash/python

import keyword
text = keyword.kwlist

nlist = list(text)
#nlist = ''.join(nlist)
for index in nlist:
    print index

nlist.reverse()
for index in nlist:
    print index
