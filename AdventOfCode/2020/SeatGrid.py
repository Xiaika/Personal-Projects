from copy import deepcopy
from typing import Dict, Tuple
Point = Tuple[int, int]

class SeatGrid:
    def __init__(self, data):
        self.MAXX = len(data[0])
        self.map: Dict[Point, chr] = dict()
        for y, line in enumerate(data):
            for x, char in enumerate(line):
                self.map[x, y] = char

    def __len__(self):
        return len(self.map.keys())

    def __setitem__(self, index, value):
        x, y = index
        if (x, y) in self.map:
            self.map[x, y] = value
        else:
            raise IndexError

    def __getitem__(self, index):
        x, y = index
        if (x, y) in self.map:
            return self.map[x, y]
        else:
            raise IndexError

    def __str__(self):
        temp = ''
        count = 1
        for point, char in self.map.items():
            temp += char
            if point[0] == self.MAXX - 1:
                temp += '\n'
                count = 0
            count += 1
        return temp

    def __eq__(self, other):
        for point in self.map.keys():
            if self[point] != other[point]:
                return False
        return True

    def isEmpty(self, point):
        if self[point] == '.' or self[point] == 'L':
            return True
        else:
            return False


class WaitingRoomB(SeatGrid):
    @staticmethod
    def rate_of_change(case) -> Point:
        """Compute the rate of change for a given direction"""
        if case == 1:  # UP
            dx = 0;  dy = -1
        elif case == 2:  # DOWN
            dx = 0;  dy = 1
        elif case == 3:  # LEFT
            dx = -1; dy = 0
        elif case == 4:  # RIGHT
            dx = 1;  dy = 0
        elif case == 5:  # UP-LEFT
            dx = -1; dy = -1
        elif case == 6:  # DOWN-LEFT
            dx = -1; dy = 1
        elif case == 7:  # UP-RIGHT
            dx = 1; dy = -1
        elif case == 8:  # DOWN-RIGHT
            dx = 1; dy = 1
        else:
            raise ValueError(f'Invalid case: {case} must be 1-8')
        return dx, dy

    def countAdjacent(self, point: Point, case):
        """Count the number of adjacent seats and return how many are full"""
        x, y = point
        # print(f'x: {x}, y: {y}')
        dx, dy = self.rate_of_change(case)
        cur_x = x + dx
        cur_y = y + dy
        while (cur_x, cur_y) in self.map:
            if self[cur_x, cur_y] == '#':
                # print('found # at index', (cur_x, cur_y))
                return 1
            elif self[cur_x, cur_y] == 'L':
                return 0
            else:
                cur_x += dx
                cur_y += dy
        return 0

    def occupy_seats(self):
        """Check all empty seats in the grid,
           if that seat has no adjacent seats then occupy the seat"""
        newmap = self.map.copy()
        for point, char in newmap.items():
            x, y = point
            if self.map[point] == 'L':
                count = sum(self.countAdjacent(point, c) for c in range(1,9))
                if count == 0:
                    newmap[x, y] = '#'
        self.map = newmap.copy()

    def vacate_seats(self):
        """Check all empty seats in the grid,
           if that seat has 5 or more adjacent seats then vacate the seat"""
        newmap = self.map.copy()
        for point, char in newmap.items():
            x, y = point
            if self.map[point] == '#':
                count = sum(self.countAdjacent(point, c) for c in range(1, 9))
                if count >= 5:
                    newmap[x, y] = 'L'
        self.map = newmap.copy()


class WaitingRoomA(SeatGrid):
    def countAdjacent(self, point: Point):
        """Count the number of adjacent seats and return how many are full"""
        cur_x, cur_y = point
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                else:
                    if ((cur_x + dx), (cur_y + dy)) in self.map:
                        if self[(cur_x + dx), (cur_y + dy)] == '#':
                            count += 1
        return count

    def occupy_seats(self):
        """Check all empty seats in the grid,
           if that seat has no adjacent seats then occupy the seat"""
        newmap = self.map.copy()
        for point, char in newmap.items():
            x, y = point
            if self.map[point] == 'L':
                count = self.countAdjacent(point)
                if count == 0:
                    newmap[x, y] = '#'
        self.map = newmap.copy()

    def vacate_seats(self):
        """Check all occupied in the grid,
           if that seat has 5 or more adjacent seats then vacate the seat"""
        newmap = self.map.copy()
        for point, char in newmap.items():
            x, y = point
            if self.map[point] == '#':
                count = self.countAdjacent(point)
                if count >= 4:
                    newmap[x, y] = 'L'
        self.map = newmap.copy()
