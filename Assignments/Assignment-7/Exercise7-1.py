#Write a program to read through a file and print the contents of the file 
# (line by line) all in upper case.

fname = input('Enter a file name: ')
fhandle = open(fname)
for line in fhandle:
    print(line.rstrip().upper())
