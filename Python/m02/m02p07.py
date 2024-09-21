#!/usr/bash/python

def print_user_line(username):
        if username[5].find('/home/') == 0 and username[6].find('/bin/bash') == 0:
                user = username[0]
                directory = username[5]           
                print "| %-8s| %-16s|" % (user, directory)     
        if username[0].find('usbmux') == 0:
                print "+---------+-----------------+"
        return 0

file = open("/etc/passwd", "r")
print "+---------+-----------------+"

for line in file:
        nline = line.split(":")
        print_user_line(nline)