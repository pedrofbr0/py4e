array = [5,6,1,23,5,324,65,234,67,235]

for i in array:
    for j in range(len(array)):
        try:
            if array[j] >= array[j+1]:
                aux = array[j]
                array[j]=array[j+1]
                array[j+1]=aux
        except:
            continue

print(array)