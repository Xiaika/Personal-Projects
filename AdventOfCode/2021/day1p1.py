with open('day1.txt') as file:
    data = [int(i) for i in file.read().splitlines()]

    counter = 0
    for index in range(len(data)-1):
        if data[index] < data[index + 1]:
            counter += 1

    print(f'Puzzle Solution: {counter}')
