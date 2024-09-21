#!/usr/bin/python 

# Make the printing stop when the row would exceed 80 characters. 
# Define the function pascal(row), which takes as a parameter the list of numbers in a row, 
# and returns a list of numbers for the next row. 

def pascal(row):
	next_row = [1]
	for i in range(1,len(row)):
		next_row.append(row[i-1]+row[i])
	next_row.append(1)
	return next_row

row = [1]
max_length = 80

while 1:
	val = ""
	for i in row:
		val += str(i) + " "
	if len(val) >= max_length:
		break
	
	print (((80-len(val))/2)-3) * " ", val
	row = pascal(row)