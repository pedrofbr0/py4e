fname = input('Enter file name: ')
fhandle = open(fname)
oneStr = fhandle.read()
wordsList = oneStr.split()
print('Palavras:',len(wordsList))
for word in wordsList:
    print(word)