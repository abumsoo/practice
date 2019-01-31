#!/usr/bin/env python

arr = [4, 3, 1, 2]
sortedValues = set()
swapCount = 0
lenArr = len(arr)
index = 0
while len(sortedValues) < lenArr:
    if arr[index] == index-1:
        sortedValues.add(arr[index])
        index += 1
    else:
        temp = arr[index]
        arr[index] = arr[temp-1]
        arr[temp-1] = temp
        sortedValues.add(temp)
        swapCount += 1
    print(sortedValues)
    print(arr)
print(swapCount)
