from math import gcd

def lcm(buses):
    intList = [i for i in buses if i != 0]
    lcm = intList[0]
    for integer in intList:
        lcm = lcm * integer // gcd(integer, lcm)
    return lcm


def findT(buses):
    addTo = 0
    t = buses[0]
    for i in range(1, len(buses)):
        valid = False
        while not valid:
            valid = True
            for x in range(i+1):
                if buses[x] != 0 and (t + x) % buses[x] != 0:
                    valid = False
                    break
            if valid:
                print("possible T: ", t)
                addTo = lcm(buses[:x])
                break
            else:
                t += addTo
    return t

def main():
    with open("Problem13.txt") as infile:
        schedule = infile.read().splitlines()

    data = [i for i in schedule[1].split(',')]
    buses = list()
    numZeros = 0
    for i in data:
        if i == 'x':
            buses.append(0)
            numZeros += 1
        else:
            buses.append(int(i))
    t = findT(buses)

    print("T found: ", t)

main()