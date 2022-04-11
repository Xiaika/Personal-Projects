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

        if x1 == x2:    # Vertical line
            Δ = y2 - y1
            for index in range(Δ + 1):
                point_map[(x1, y1 + index)] += 1
        elif y1 == y2:  # Horizontal line
            Δ = x2 - x1
            for index in range(Δ + 1):
                point_map[(x1 + index, y1)] += 1
        else:           # Diagonal line
            x1 = int(point1[0])
            x2 = int(point2[0])
            y1 = int(point1[1])
            y2 = int(point2[1])
            Δx = x2 - x1
            Δy = y2 - y1
            if Δx > 0 and Δy > 0:
                for index_x in range(Δx + 1):
                    for index_y in range(Δy + 1):
                        if index_x == index_y:
                            point_map[(x1 + index_x, y1 + index_y)] += 1
            elif Δx > 0 and Δy < 0:
                for index_x in range(Δx + 1):
                    for index_y in range(abs(Δy - 1)):
                        if index_x == index_y:
                            point_map[(x1 + index_x, y1 - index_y)] += 1
            elif Δx < 0 and Δy > 0:
                for index_x in range(abs(Δx - 1)):
                    for index_y in range(Δy + 1):
                        if index_x == index_y:
                            point_map[(x1 - index_x, y1 + index_y)] += 1
            elif Δx < 0 and Δy < 0:
                for index_x in range(abs(Δx - 1)):
                    for index_y in range(abs(Δy - 1)):
                        if index_x == index_y:
                            point_map[(x1 - index_x, y1 - index_y)] += 1

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