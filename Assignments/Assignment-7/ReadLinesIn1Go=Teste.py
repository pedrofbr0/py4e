fileHandle = open('Teste.txt')
oneString = fileHandle.read()
# print('Characters:',len(oneString))
# print(oneString[0:557])



oneString = oneString.splitlines()

print(oneString)