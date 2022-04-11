from collections import Counter

with open('day3.txt') as file:
    data = [line.rstrip() for line in file.read().splitlines()]
    transpose = zip(*data)
    gamma = str()
    epsilon = str()
    for row in transpose:
        c = Counter(row)
        epsilon += '0' if c['0'] < c['1'] else '1'
        gamma += '0' if c['0'] > c['1'] else '1'

print(f'Puzzle Solution: {int(gamma, 2) * int(epsilon, 2)}')


