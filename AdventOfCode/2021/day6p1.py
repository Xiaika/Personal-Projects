with open('day6.txt') as file:
    lantern_fish = [int(number) for number in file.readline().split(',')]

max_iterations = 80
i = 0
while i < max_iterations:
    temp_fish = lantern_fish
    for index, fish in enumerate(lantern_fish):
        temp_fish[index] -= 1
        if temp_fish[index] < 0:
            temp_fish.append(9)
            temp_fish[index] += 7
    lantern_fish = temp_fish
    i += 1
    # print(f'Iteration: {i} -- {lantern_fish}')

print(f'Puzzle Solution: {len(lantern_fish)}')
