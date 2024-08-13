name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

domains = []
hist = {}
for line in handle:
    if not line.startswith('From '): continue
    lineSplit = line.split()
    email = lineSplit[1]
    # domainPos = email.find('@')
    # domain = email[domainPos+1:]
    emailSplit = email.split('@')
    domains.append(emailSplit[1])
    # domains.append(domain)

for domain in domains:
    hist[domain] = hist.get(domain,0) + 1

print(hist)

bigValue = []
bigKey = []

for key, value in hist.items():
    if bigValue == [] or value > bigValue:
        bigValue = value
        bigKey = key

print(bigKey, bigValue)