#!/usr/bash/python

def pascal(row, col):
    if col==0:
        return 1
    elif col==row:
        return 1
    else:
        return pascal(row-1, col) + pascal(row-1, col-1)

rows = 10
lists = []

for i in range(0, rows):
    val=0
    count = 0
    for j in range(0, i+1):
        if (i == 0):
            count += (len(str(pascal(i,j))) + 1 )
        if(val == i):
            count += len(str(pascal(i,j)))
        else:
            count += (len(str(pascal(i,j))) + 1 )
    lists.append(count)

for i in range(0, rows):     
    val=0      
    #count = 0
    count = ((27-lists[i])/2)
    print " " * count,
    for j in range(0, i+1):
        if(val == i):
            res = pascal(i, j)
            #count += len(str(res))            
            print res
        else:
            val += 1
            res = pascal(i, j)
            #count += (len(str(res))+1)
            print res,
    #print "count = ", count 
    #print " " * ((27-count)/2),


