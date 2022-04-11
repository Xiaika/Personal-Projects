from collections import defaultdict
from typing import *

from typing import List

Point = Tuple[int, int, int]

class PointsMap(object):

    def __init__(self, data: List[str]):
        self.MAXX = len(data[0])
        self.MAXY = len(data)
        self.map: defaultdict[Point, chr] = defaultdict(self.__default)

        z = 0
        for y, string in enumerate(data):
            for x, char in enumerate(string):
                self.map[x, y, z] = char

    def __len__(self):
        return len(self.map)  # Number of keys

    def __getitem__(self, index):
        index1, index2, index3 = index
        return self.map[index1, index2, index3]


    def __str__(self):
        string = ''
        for y in range(self.MAXY):
            for x in range(self.MAXX):
                string += self[x, y, 0]
                if x == self.MAXX - 1:
                    string += '\n'
        return string

    def print_slice(self, zslice):
        string = ''
        keys = list(self.map.keys())
        for key in keys:
            x, y, z = key
            if z == zslice:
                string += self[x, y, z]
        return string

    @staticmethod
    def count_adjacent(points, x, y, z) -> int:
        """Check all 26 neighboring cubes and count number of active cubes"""
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if dx == 0 and dy == 0 and dz == 0:
                        continue
                    else:
                        if points[x + dx, y + dy, z + dz] == '#':
                            count += 1
        print(count)
        return count

    @staticmethod
    def becomes_active(points, x: int, y: int, z: int):
        """Computes whether a node should be active in the next iteration"""
        if points[x, y, z] == '#':  # Cube is currently active
            # Check all adjacent cubes if exactly 2 or 3 are active, remain active
            count = PointsMap.count_adjacent(points, x, y, z)
            if count == 2 or count == 3:
                return True
            return False

        else:  # Cube is currently inactive
            # Check all adjacent cubes if exactly 3 are active, become active
            count = PointsMap.count_adjacent(points, x, y, z)
            if count == 3:
                return True
            return False

    def run_cycle(self):
        # For every point in the map compute new points
        points = self.map.copy()
        keys = list(self.map.keys())
        for key in keys:
            x, y, z = key
            if PointsMap.becomes_active(points, x, y, z):
                points[x, y, z] = '#'
            else:
                points[x, y, z] = '.'
        self.map = points

    def __default(self):
        return '.'
































