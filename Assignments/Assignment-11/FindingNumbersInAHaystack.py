fileName = input("Enter file: ")
if len(fileName) < 1 : fileName = "regex_sum_1176850.txt"
# if len(fileName) < 1 : fileName = "regex_sum_42.txt"
fileHandle = open(fileName)

import re

# oneString = fileHandle.read()

# nums = re.findall('[0-9]+',oneString)

# numss = re.findall('[0-9]+',open("regex_sum_1176850.txt").read())



# print(numss)
# total = 0

# for num in nums:
    # total += int(num)

# print(total)


# print( sum( [ int(num) for num in nums ] ) )

print( sum( [ int(num) for num in re.findall('[0-9]+',open("regex_sum_1176850.txt").read()) ] ) )