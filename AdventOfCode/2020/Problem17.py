from Grid import PointsMap
from collections import defaultdict
with open('Problem17.txt') as file:
    data = file.read().splitlines()

cubes = PointsMap(data)
cubes.run_cycle()
print(cubes)


