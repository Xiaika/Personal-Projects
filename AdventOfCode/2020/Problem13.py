def getMinTime(timeStamp, buses, counters):
    numTrue = 0
    while numTrue < len(counters):
        numTrue = 0
        for x in range(len(buses)):
            if counters[x] >= timeStamp:
                numTrue += 1
        for i in range(len(buses)):
            if counters[i] < timeStamp:
                counters[i] += buses[i]
    return min(counters)


def removeAll(list, item):
    return [int(i) for i in list if i != item]

def main():

    with open("Problem13.txt") as infile:
            schedule = infile.read().splitlines()


    timeStamp = int(schedule[0])
    buses = [i for i in schedule[1].split(',')]
    buses = removeAll(buses, 'x')
    counters = buses.copy()
    minimum = getMinTime(timeStamp, buses, counters)


    for index, counter in enumerate(counters):
        if counter == minimum:
            result1 = buses[index] * (minimum - timeStamp)
    print(result1)


main()