import numpy as np


def findXMAS(numbers, head, tail):
    found = True
    while tail + 1 < len(numbers) - 1:
        stack = numbers[head: tail + 1]
        for num1 in stack[:-1]:
            for num2 in stack[1:]:
                if num1 + num2 == numbers[tail + 1]:
                    found = True
                    break
                else:  # num1 + num2 == numbers[tail + 1]
                    found = False
            if found:
                break

        if not found:
            return numbers[tail + 1]

        head += 1
        tail += 1


def findPair(xmas, numbers):
    for i in range(0, len(numbers) - 1):
        for j in range(1, len(numbers)):
            contigList = np.array(numbers[i:j])
            if np.sum(contigList) == xmas:
                return contigList.min() + contigList.max()


def main():
    debugging = False

    with open("Problem9.txt") as infile:
        data = infile.read().splitlines()

    numbers = []
    for string in data:
        numbers.append(int(string))

    preamble = 5 if debugging else 25
    head = 0
    tail = preamble - 1
    xmas = findXMAS(numbers, head, tail)
    print("The sum of the two values are: " + str(findPair(xmas, numbers)))


main()
