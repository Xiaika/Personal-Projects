# find the two entries that sum to 2020
# and then multiply those two numbers together


def main():
    infile = open('./Problem1.txt', 'r')
    dataS = []
    for line in infile:
        dataS.append(line.rstrip())

    data = []
    for i in dataS:
        data.append(int(i))

    for i in data:
        for j in data:
            for k in data:
                if (i != j) and (j != k) and (i != k) and (i + j + k) == 2020:
                    print(i * j * k)

main()