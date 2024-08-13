name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = list()
hist = dict()

for line in handle:
    if not line.startswith("From "): continue
    lineSplit = line.split()
    time = lineSplit[5]
    timeSplit = time.split(':')
    hour = timeSplit[0]
    hours.append(hour)

for hr in hours:
    hist[hr] = hist.get(hr,0) + 1

# toSort = list()

# for k, v in hist.items():
#     toSort.append((k,v))

# print(type(toSort))

# sortedHist = toSort.sort(reverse=True)
# print(sortedHist)

# sortedHist = sorted(hist)

# for h in sortedHist:
#     print(h,hist[h])

sortedHistKeys = sorted(hist.items())

for tup in sortedHistKeys:
    print(tup)

for k,v in sortedHistKeys:
    print(k,v)