fileName = input("Enter file name: ")
fileHandle = open(fileName)

count = 0
total = 0

for line in fileHandle:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    colonPos = line.find(":")
    strNumb = line[colonPos+1:]
    total = total + float(strNumb)
    count = count + 1

print("Average spam confidence:",total/count)

