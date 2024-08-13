fileName = input("Enter file: ")
if len(fileName) < 1 : fileName = "mbox-short.txt"
fileHandle = open(fileName)

import string

# charStr = fileHandle.read()
# charStrClean = charStr.translate(charStr.maketrans('','',string.punctuation))

# print(charStrClean)
chars = list()
hist = dict()
count = 0

for line in fileHandle:
    cleanWhiteSpace = line.strip()
    cleanPuntuation = cleanWhiteSpace.translate(cleanWhiteSpace.maketrans('','',string.punctuation))
    cleanDigits = cleanPuntuation.translate(cleanPuntuation.maketrans('','',string.digits))
    # cleanNonPrintable = ''.join([c for c in cleanNonPrintable if c in string.printable])
    # print(cleanNonPrintable)
    cleanCase = cleanDigits.lower()
    cleanSpace = cleanCase.translate(cleanCase.maketrans('','',' '))
    cleanComma = cleanSpace.translate(cleanSpace.maketrans('','','\\t'))
 
    for char in cleanComma:

        if char in string.printable: 
            chars.append(char)
            count += 1

for ch in chars:
    hist[ch] = hist.get(ch, 0) + 1

# print("Usorted:",hist)

tulpList = list()

for k,v in hist.items():
    tulpList.append((v,k))

# print("TulpList:",tulpList)

histSortedByValue = sorted(tulpList,reverse=True)


for v, k in histSortedByValue:
    
    print((k,v),"Percentage of the total: ",100*v/count)


