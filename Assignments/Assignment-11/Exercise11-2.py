# Exercise 2: Write a program to look for lines of the form:

# New Revision: 39772

# Extract the number from each of the lines using a regular 
# expression and the findall() method. Compute the average 
# of the numbers and print out the average as an integer.

# Enter file:mbox.txt
# 38549

# Enter file:mbox-short.txt
# 39756

#############################################################

fname = input('Enter file: ')
if len(fname) < 1: fname = 'mbox.txt'

import re

fhandle = open(fname)

oneString = fhandle.read()

matches = re.findall('New Revision: ([0-9]+)',oneString)

print(int(sum(list(int(num) for num in matches))/len(matches)))
