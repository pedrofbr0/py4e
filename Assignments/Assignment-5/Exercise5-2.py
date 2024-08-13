# largest = None
# smallest = None

# while True:
#     num = input("Enter a number: ")
#     if num == "done" : break
#     try:
#         num = int(num)
#     except:
#         print("Invalid input")
#         continue      
#     if largest is None:
#         largest = num
#     elif num > largest:
#         largest = num
#     if smallest is None:
#         smallest = num
#     elif num < smallest:
#         smallest = num

# print("Maximum is", largest)
# print("Minimum is", smallest)


#futher&beyond
largest = None
smallest = None
count = 0
sum = 0

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue      
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    count = count + 1
    sum = sum + num

print("Maximum is", largest)
print("Minimum is", smallest)
print("Count is", count)
print("Sum is", sum)
print("Average is", sum/count)

import numpy
import matplotlib