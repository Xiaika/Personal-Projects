from Seat import Seat
from copy import deepcopy

class WaitingRoom:
    def __init__(self, data):
        self.MAX_X = len(data[0])
        self.MAX_Y = len(data)
        self.map = [type(Seat)] * self.MAX_X * self.MAX_Y
        self.adjcounter = 0
        i = 0
        y = 0
        x = 0
        for line in data:
            for char in line:
                seat = Seat(x % self.MAX_X, y, char)
                self.map[i] = seat
                x += 1
                i += 1
            y += 1
        self.newmap = deepcopy(self.map)

    def musicalChairs(self):

        while True:
            temp = deepcopy(self.map)
            self.occupySeats()
            self.unoccupySeats()
            if self.equal(temp):
                self.printSeats()
                total = 0
                for seat in self.map:
                    total += 1 if seat.getState() == 2 else 0
                print('\n'*3)
                print(total)
                break



    def equal(self, temp):
        i = 0
        for y in range(self.MAX_Y):
            for x in range(self.MAX_X):
                if self.map[i].getState() != temp[i].getState():
                    return False
                i += 1
        return True

    def countAdjacent(self, case, seatIndex):
        # return the number of adjacent seats that are full
        count = 0
        if case == 'top left':
            if not self.isEmpty(seatIndex + 1):
                count += 1
            if not self.isEmpty(seatIndex + self.MAX_X):
                count += 1
            if not self.isEmpty(seatIndex + self.MAX_X + 1):
                count += 1
            return count

        elif case == 'top right':
            if not self.isEmpty(seatIndex - 1):
                count += 1
            if not self.isEmpty(seatIndex + self.MAX_X):
                count += 1
            if not self.isEmpty(seatIndex + self.MAX_X - 1):
                count += 1
            return count

        elif case == 'top row':
            if not self.isEmpty(seatIndex - 1):
                count += 1
            if not self.isEmpty(seatIndex + 1):
                count += 1
            if not self.isEmpty(seatIndex + self.MAX_X):
                count += 1
            if not self.isEmpty(seatIndex + self.MAX_X + 1):
                count += 1
            if not self.isEmpty(seatIndex + self.MAX_X - 1):
                count += 1
            return count

        elif case == 'bottom left':
            if not self.isEmpty(seatIndex + 1):
                count += 1
            if not self.isEmpty(seatIndex - self.MAX_X):
                count += 1
            if not self.isEmpty(seatIndex - self.MAX_X + 1):
                count += 1
            return count

        elif case == 'bottom right':
            if not self.isEmpty(seatIndex - 1):
                count += 1
            if not self.isEmpty(seatIndex - self.MAX_X):
                count += 1
            if not self.isEmpty(seatIndex - self.MAX_X - 1):
                count += 1
            return count

        elif case == 'bottom row':
            if not self.isEmpty(seatIndex - 1):
                count += 1
            if not self.isEmpty(seatIndex + 1):
                count += 1
            if not self.isEmpty(seatIndex - self.MAX_X):
                count += 1
            if not self.isEmpty(seatIndex - self.MAX_X + 1):
                count += 1
            if not self.isEmpty(seatIndex - self.MAX_X - 1):
                count += 1
            return count

        elif case == 'left column':
            if not self.isEmpty(seatIndex + 1):
                count += 1
            if not self.isEmpty(seatIndex - self.MAX_X):
                count += 1
            if not self.isEmpty(seatIndex - self.MAX_X + 1):
                count += 1
            if not self.isEmpty(seatIndex + self.MAX_X):
                count += 1
            if not self.isEmpty(seatIndex + self.MAX_X + 1):
                count += 1
            return count

        elif case == 'right column':
            if not self.isEmpty(seatIndex - 1):
                count += 1
            if not self.isEmpty(seatIndex - self.MAX_X):
                count += 1
            if not self.isEmpty(seatIndex - self.MAX_X - 1):
                count += 1
            if not self.isEmpty(seatIndex + self.MAX_X):
                count += 1
            if not self.isEmpty(seatIndex + self.MAX_X - 1):
                count += 1
            return count

        elif case == 'any other':
            if not self.isEmpty(seatIndex + 1):
                count += 1
            if not self.isEmpty(seatIndex - 1):
                count += 1
            if not self.isEmpty(seatIndex - self.MAX_X):
                count += 1
            if not self.isEmpty(seatIndex - self.MAX_X - 1):
                count += 1
            if not self.isEmpty(seatIndex - self.MAX_X + 1):
                count += 1
            if not self.isEmpty(seatIndex + self.MAX_X):
                count += 1
            if not self.isEmpty(seatIndex + self.MAX_X - 1):
                count += 1
            if not self.isEmpty(seatIndex + self.MAX_X + 1):
                count += 1
            return count

        else:
            print("Case error")


    def occupySeats(self):
        # check all seats in the waiting room and sit if condition is met #
        for index in range(self.MAX_X * self.MAX_Y):
            newseat = self.newmap[index]
            oldseat = self.map[index]
            x = oldseat.getX()
            y = oldseat.getY()
            if oldseat.getState() == 1:  # Seat is empty #
                if y == 0:  # Top of the map
                    if x == 0:
                        if self.countAdjacent('top left', index) == 0:  newseat.sit()
                    elif x == self.MAX_X - 1:
                        if self.countAdjacent('top right', index) == 0:  newseat.sit()
                    else:  # Top row #
                        if self.countAdjacent('top row', index) == 0:  newseat.sit()
                elif y == self.MAX_Y - 1:  # Bottom of the map #
                    if x == 0:
                        if self.countAdjacent('bottom left', index) == 0:  newseat.sit()
                    elif x == self.MAX_X - 1:
                        if self.countAdjacent('bottom right', index) == 0:  newseat.sit()
                    else:
                        if self.countAdjacent('bottom row', index) == 0:  newseat.sit()
                else:  # Any other row #
                    if x == 0:
                        if self.countAdjacent('left column', index) == 0:  newseat.sit()
                    elif x == self.MAX_X - 1:
                        if self.countAdjacent('right column', index) == 0:  newseat.sit()
                    else:
                        if self.countAdjacent('any other', index) == 0:  newseat.sit()
        self.map = deepcopy(self.newmap)


    def unoccupySeats(self):
        # check all seats in the waiting room and sit if condition is met #
        for index in range(self.MAX_X * self.MAX_Y):
            newseat = self.newmap[index]
            oldseat = self.map[index]
            x = oldseat.getX()
            y = oldseat.getY()
            if oldseat.getState() == 2:  # Seat is full #
                if y == 0:  # Top of the map
                    if x == 0:
                        if self.countAdjacent('top left', index) >= 4:  newseat.unsit()
                    elif x == self.MAX_X - 1:
                        if self.countAdjacent('top right', index) >= 4:  newseat.unsit()
                    else:  # Top row #
                        if self.countAdjacent('top row', index) >= 4:  newseat.unsit()
                elif y == self.MAX_Y - 1:  # Bottom of the map #
                    if x == 0:
                        if self.countAdjacent('bottom left', index) >= 4:  newseat.unsit()
                    elif x == self.MAX_X - 1:
                        if self.countAdjacent('bottom right', index) >= 4:  newseat.unsit()
                    else:
                        if self.countAdjacent('bottom row', index) >= 4:  newseat.unsit()
                else:  # Any other row #
                    if x == 0:
                        if self.countAdjacent('left column', index) >= 4:  newseat.unsit()
                    elif x == self.MAX_X - 1:
                        if self.countAdjacent('right column', index) >= 4:  newseat.unsit()
                    else:
                        if self.countAdjacent('any other', index) >= 4:  newseat.unsit()
        self.map = deepcopy(self.newmap)

    def isEmpty(self, index):
        if self.map[index].getState() == 0 or self.map[index].getState() == 1:
            return True
        else:
            return False


    def printSeats(self):
        temp = []
        for index in range(self.MAX_X * self.MAX_Y):
            state = self.map[index].getState()
            if state == 0:
                temp.append('.')
            elif state == 1:
                temp.append('L')
            else:
                temp.append('#')

        count = 0
        for char in temp:
            if count == self.MAX_X:
                print('\n', end="")
                count = 0
            print(char, end="")
            count += 1



    @property
    def toString(self):
        temp = []
        for seat in self.map:
            temp.append(seat.toString())
        return temp

