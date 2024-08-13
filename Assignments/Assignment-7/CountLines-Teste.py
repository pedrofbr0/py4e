# fileHandle = open("Teste2.txt")
# count = 0
# for line in fileHandle:
#     print(line)
#     count = count + 1
# print(count )

fileHandle = open("Teste2.txt")

count = 0
for line in fileHandle:
    print(line.rstrip())
    count = count + 1
print(count )
