# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)

# emails = []
# hist = {}
# for line in handle:
#     if not line.startswith('From '): continue
#     emails.append(line.split()[1])

# for email in emails:
#     hist[email] = hist.get(email,0) + 1

# highestFreq = max(hist.values())

# for key in hist:
#     if hist[key] == highestFreq:
#         print(key,hist[key])

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = []
hist = {}
for line in handle:
    if not line.startswith('From '): continue
    emails.append(line.split()[1])

for email in emails:
    hist[email] = hist.get(email,0) + 1

bigValue = []
bigKey = []

for key, value in hist.items():
    if bigValue == [] or value > bigValue:
        bigValue = value
        bigKey = key

print(bigKey, bigValue)


    