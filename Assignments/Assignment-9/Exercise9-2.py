name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

days = []
hist = {}
i = 0

# for i in range(len(handle.readlines())):
#     if not handle.readlines()[i].startswith('From '): continue
#     emails[i] = handle.split()

for line in handle:
    if not line.startswith('From '): continue
    line = line.split()
    days.append(line[2])

for day in days:
    hist[day] = hist.get(day,0) + 1

print(hist)

# for email in emails:
#     hist[email] = hist.get(email,0) + 1

# bigValue = []
# bigKey = []

# for key, value in hist.items():
#     if bigValue == [] or value > bigValue:
#         bigValue = value
#         bigKey = key

# print(bigKey, bigValue)