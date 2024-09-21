#!/usr/bash/python

import sys

star_dictionary={0: [12, 13, 14, 15, 16, 17, 18], 1: [10, 11, 19, 20], 
                 2: [9, 21], 3: [7, 8, 22, 23], 4: [6, 24], 5: [5, 25], 
                 6: [4, 26], 7: [3, 27], 8: [2, 28], 9: [1, 29], 
                 10: [0, 30], 11: [31, 59], 12: [32, 58], 13: [33, 57], 
                 14: [34, 56], 15: [35, 55], 16: [36, 54], 
                 17: [37, 38, 52, 53], 18: [39, 51], 19: [40, 41, 49, 50], 
                 20: [42, 43, 44, 45, 46, 47, 48] }

for i in range(21):
    for j in range(60):
        if i == 10:
            if j in star_dictionary[i]:
                sys.stdout.write("*"),
            else:
                sys.stdout.write("-"),

        else:
            if j in star_dictionary[i]:
                sys.stdout.write("*"),
            else:
                sys.stdout.write(" "),
    print("\r")

"""
import os, sys

mydict = {"modae":"1234560777", "bob":"1234567888"} # make a dictionary
modae_phone = mydict["modae"]   # get the specific value from a dictionary

#when you don't know the key value(ex. modae)
mydict.keys()   # ['fred', 'bob'] 
for keyval in mydict.keys():
    print mydict[keyval]

# what is someone has 2 phone number
names = ['fred', 'bob', 'alice']
numbers = ['123456', '234567','34567']

for i in range(3):


if mydict.has_key('alice'):
    mydict['alice'].append('123456123')

#sin graph - tips
swave[0] = [0,30]

for i in range(60):
    if i in swave[0]:
        print '*'
    else :
        print ' '

"""