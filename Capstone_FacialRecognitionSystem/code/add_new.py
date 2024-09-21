from mysql_functions import *
import sys
def print_usage():
    print ("Usage python3 add_new.py filename firstname lastname [1,0]")
    print("filename: image file ( picture of the newface) ")
    print ("[1,0], is optional, default is 1,  if the new face is friend choose 1;  else choose 0")
def add_new(isfriend=1):
    file=sys.argv[1]
    fname=sys.argv[2]
    lname=sys.argv[3]
    Add_New_Face_Manual(file,fname,lname, isfriend=1)
if __name__ == '__main__':

    if len(sys.argv)<4:
        print_usage()
    elif len(sys.argv)==5:
            
            isfriend=int(sys.argv[4])
            if isfriend == 0 or isfriend ==1:
                add_new(isfriend)
                
            else:
                print_usage()
    else:
        add_new()

            