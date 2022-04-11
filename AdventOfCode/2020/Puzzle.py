from typing import *

Point = Tuple[int, int]
Pic = Dict[Point, chr]

class PointsMap(object):

    def __init__(self, data: List[str]):
        self.MAX_X = len(data[1])
        self.MAX_Y = len(data) - 1
        self.map: Dict[Point, chr] = dict()
        self.name = ''.join([i for i in data[0] if i != ':'])

        for y, string in enumerate(data[1:]):
            for x, char in enumerate(string):
                self[x, y] = char

    def __len__(self):
        return self.MAX_X * self.MAX_Y

    def __iter__(self):
        self.index = [0, 0]
        return self

    def __next__(self):
        x = self.index[0]
        y = self.index[1]
        if x <= y < len(self):
            result = self.map[x, y]
            x += 1; y += 1
            self.index = [x, y]
            return result
        raise StopIteration

    def __str__(self):
        string = self.name + ':' + '\n'
        i = 1
        for value in self.map.values():
            string += value
            if i % self.MAX_X == 0:
                string += '\n'
            i += 1
        return string

    def __repr__(self):
        return self.name

    def __getitem__(self, index):
        index1, index2 = index
        if index1 < self.MAX_X and index2 < self.MAX_Y:
            return self.map[index1, index2]
        raise KeyError(f"Point ({index1}, {index2}) out of range.")

    def __setitem__(self, index, item):  # [] = x
        index1, index2 = index
        if index1 < self.MAX_X and index2 < self.MAX_Y:
            self.map[index1, index2] = item
        else:
            raise KeyError(f"Point ({index1}, {index2}) out of range.")


class Puzzle(PointsMap):

    def rotate(self):
        newmap = self.map.copy()
        maxx = self.MAX_X - 1
        maxy = self.MAX_Y - 1

        for i in range(self.MAX_X):
            newmap[i, 0] = self.map[0, maxy - i]
            newmap[maxx, i] = self.map[i, 0]
            newmap[maxx - i, maxy] = self.map[maxx, i]
            newmap[0, maxy - i] = self.map[maxx - i, maxy]

        self.map = newmap

    def flip(self, axis='y'):
        newmap = self.map.copy()
        maxx = self.MAX_X - 1
        maxy = self.MAX_Y - 1
        if axis == 'y' or axis == 'Y':
            for y in range(self.MAX_Y):
                for x in range(self.MAX_X):
                    newmap[x, y] = self.map[maxx - x, y]
        elif axis == 'x' or axis == 'X':
            for x in range(self.MAX_X):
                for y in range(self.MAX_Y):
                    newmap[x, y] = self.map[x, maxy - y]
        else:
            raise ValueError('Axis must be x or y')
        self.map = newmap

    def __eq__(self, other):  # Overloads ==
        """Exhaustively check if two pieces fit together"""
        equal_side = bool
        for iterations in range(4):
            for flips in range(2):
                rotations = 0
                while rotations < 4:
                    # Check top and bottom
                    for x in range(self.MAX_X):
                        equal_side = True
                        if self[x, 0] != other[x, self.MAX_Y - 1]:
                            equal_side = False
                            break
                    if equal_side:
                        return True
                    other.rotate()
                    rotations += 1
                    # print("Rotating . . .")
                other.flip()
                # print('Flipping . . .')
            self.rotate()
        return False
