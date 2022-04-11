def getArrangements(numbers):
    maxVal = max(numbers) + 1
    arrangements = [0] * maxVal  # 0 1 4 5 6 7 10 11 12 15 16 19 22
    arrangements[0] = 1  # 1 1 0 0 1 1 2 4 0 0 4 4 8 0 0 8 8 0 0 8 0 0 8
                         # 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2
    for index in range(1, maxVal):  # 22
        for x in range(1, 4):  # 1 2 3
            if (index - x) in numbers:
                arrangements[index] += arrangements[index - x]
    return arrangements[-1]


def measureJolts(numbers):
    diffOfOne = 0
    diffOfThree = 0
    currIndex = 0
    while True:
        if numbers[currIndex + 1] - numbers[currIndex] == 1:
            diffOfOne += 1
            currIndex += 1
        else:
            diffOfThree += 1
            currIndex += 1
        if currIndex + 1 > len(numbers) - 1:
            break

    print("The differences of 1 are: " + str(diffOfOne) + "  The differences of 3 are: " + str(diffOfThree))
    return diffOfOne * diffOfThree

def main():

    with open("Problem10.txt") as infile:
        data = infile.read().splitlines()

    numbers = [int(i) for i in data]
    numbers = sorted(numbers)
    deviceJolts = max(numbers) + 3
    numbers.insert(0, 0)
    numbers.append(deviceJolts)
    product = measureJolts(numbers)
    arrangements = getArrangements(numbers)
    print("Product: " + str(product))
    print("Arrangements: " + str(arrangements))

main()