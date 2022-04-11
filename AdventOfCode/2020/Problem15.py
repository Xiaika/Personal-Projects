def getKey(index):
    return list(startNums)[index]


startNums = [0, 3, 6]

startNums = {n: 0 for n in startNums}

for counter in range(1, 4):
    currIndex = (counter - 1) % len(startNums)
    if counter < len(list(startNums)) + 1:
        startNums[getKey(currIndex)] = counter
    if currIndex - 1 ==


print(startNums)