# fname = input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"

# fh = open(fname)
# count = 0

# for line in fh:
#     if not line.startswith('From '): continue
#     words = line.split()
#     print(words[1])
#     count = count + 1

# print("There were", count, "lines in the file with From as the first word")

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()

    # if line = '' : continue 

    words = line.split()
    
    #Guardian Pattern
    # if len(words) < 1 : continue #Avoid empty lines resulting in empty lists

    #Stronger Guardian Pattern
    # if len(words) < 2 : continue #avoid empty lines and lines without e-mail (second word)

    #Guardian in coumpound statement
    if len(words) < 2 or words[0] != 'From' : continue    
    print(words[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")

