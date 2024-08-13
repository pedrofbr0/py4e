def findMax(n):
    max = n[0]
    for i in range(len(n)):
        if n[i] > max:
            max = n[i]
    return max

n = list()

while True:
    ip = input('Enter a number: ')
    if ip == "done": break
    try:
        ip = float(ip)
    except:
        print("Invalid Input!")
        continue
    n.append(ip)
print('Average:',sum(n)/len(n))
print('Max:',max(n))
print(findMax(n))
print('All done')

