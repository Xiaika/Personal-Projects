with open('day6.txt') as file:
    lantern_fish = sorted([int(number) for number in file.readline().split(',')])

# For sample 3,4,3,1,2
days = [0] * 9  # [0, 1, 1, 2, 1, 0, 0, 0, 0, 0]
for fish in lantern_fish:
    days[fish] += 1

for i in range(256):
    current = i % len(days)
    days[(current + 7) % len(days)] += days[current]

print(f'Puzzle Solution: {sum(days)}')
