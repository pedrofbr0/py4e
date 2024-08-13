# Exercise 1: Write a simple program to simulate the operation of the 
# grep command on Unix. Ask the user to enter a regular expression and 
# count the number of lines that matched the regular expression:

# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author

import re

regex = input('Enter a regular expression: ')

fname = 'mbox.txt'

fhandle = open(fname)

count=0

print(regex)

for line in fhandle:
    if re.search(regex,line):
        count += 1

print(fname,'had', count, 'lines that matched',regex)