from collections import defaultdict

Point = tuple[int, int]

def default():
    return 0

point_map: defaultdict[Point: int] = defaultdict(default)

with open('day5.txt') as file:
    data = file.read().splitlines()
    first_points = [i.split(' -> ')[0].split(',') for i in data]
    second_points = [i.split(' -> ')[1].split(',') for i in data]
    for point1, point2 in zip(first_points, second_points):
        x1 = min(int(point1[0]), int(point2[0]))
        y1 = min(int(point1[1]), int(point2[1]))
        x2 = max(int(point1[0]), int(point2[0]))
        y2 = max(int(point1[1]), int(point2[1]))

        if x1 == x2:  # Vertical line
            delta = y2 - y1
            # Draw line
            for index in range(delta + 1):
                point_map[(x1, y1 + index)] += 1
        if y1 == y2:  # Horizontal line
            delta = x2 - x1
            # Draw line
            for index in range(delta + 1):
                point_map[(x1 + index, y1)] += 1

count = 0
for value in point_map.values():
    if value >= 2:
        count += 1

print(f'Puzzle Solution: {count}')


# Print map
# for y in range(10):
#     for x in range(10):
#         print(point_map[x, y], end='')
#     print()


