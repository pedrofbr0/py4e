dictWords = {}

fname = input('Enter a file: ')
fhandle = open(fname)

for line in fhandle:
    words = line.split()
    for word in words:
        dictWords[word] = dictWords.get(word,0) + 1

print(dictWords)

highestFreq = max(dictWords.values())

for key in dictWords:
    if dictWords[key] == highestFreq:
        print(key,':', dictWords[key])

# for key, value in dictWords.items():
#     if value == highestFreq:
#         print(key)

# bigcount = None
# bigword = None

# for key, value in dictWords.items():
#     if bigcount is None or value > bigcount:
#         bigcount = value
#         bigword = key

# print(bigword,bigcount) #Only shows the first bigword iterated