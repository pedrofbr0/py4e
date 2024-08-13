# lowest = 10000000
# for i in [13, 2348, 0,12,33,2,67,11,23,6778,3,4524,63,21,113]:
#     if i <= lowest:
#         lowest = i
#     print("lowest:", lowest, "current:", i)
# print(lowest)

# n = [13, 2348, 0,12,33,2,67,11,23,6778,3,4524,63,21,113]
# lowest = n[0]
# for i in [13, 2348, 0,12,33,2,67,11,23,6778,3,4524,63,21,113]:
#     if i < lowest:
#         lowest = i
#     print("lowest:", lowest, "current:", i)
# print(lowest)

lowest = None #flag value 
for i in [13, 2348, 0,12,33,2,67,11,23,6778,3,4524,63,21,113]:
    if lowest is None: #check if it is the first time the loop is running. If so, take first number as the smallest
        lowest = i
    elif i <= lowest:
        lowest = i
    print("lowest:", lowest, "current:", i)
print(lowest)