# #Counting

# wordsDict = dict()

# fname = input('Enter a file name: ')
# fh = open(fname)

# for line in fh:
#     words = line.rstrip().split()
#     for word in words:
#         if word in wordsDict:
#             wordsDict[word] = wordsDict[word] + 1
#         else:
#             wordsDict[word] = 1
# print(wordsDict)

#Counting

wordsDict = dict()

fname = input('Enter a file name: ')
fh = open(fname)

for line in fh:
    words = line.rstrip().split()
    for word in words:
        # if word in wordsDict:
        #     wordsDict[word] = wordsDict[word] + 1
        # else:
        #     wordsDict[word] = 1
        wordsDict[word] = wordsDict.get(word,0) + 1 
        #The get(thing, default) method of the dictionary is equivalent to:
        # if thing in dict:
            # variable = dict[thing]
        # else:
            # variable = default
print(wordsDict)
print('Desktop:', wordsDict.get('desktop',0))