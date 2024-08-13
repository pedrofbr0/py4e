# largest = -1
# for i in [0,12,33,2,67,11,23,6778,3,4524,63,21,113]:
#     if i >= largest:
#         largest = i
#     print("largest:",largest,"current:",i)
# print(largest)

largest = None
for i in [0,12,33,2,67,11,23,6778,3,4524,63,21,113]:
    if largest is None:
        largest = i
    elif i >= largest:
        largest = i
    print("largest:",largest,"current:",i)
print(largest)