import math

class BoardingPass:

    def __init__(self, line):
        self.rowCode = line[0:7]
        self.colCode = line[7:10]
        self.row = 0
        self.col = 0
        self.getSeatRow()
        self.getSeatCol()

    def toString(self):
        return "BoardingPass [Row Code: " + self.rowCode + ", Column Code: " + self.colCode + ']'

    def getSeatRow(self):
        lower = 0
        upper = 127
        for char in self.rowCode:
            if char == 'F':
                upper = (upper + lower) // 2
            elif char == 'B':
                lower = math.ceil((upper + lower) / 2)
        if self.rowCode[len(self.rowCode) - 1] == 'F':
            self.row = lower
        elif self.rowCode[len(self.rowCode) - 1] == 'B':
            self.row = upper


    def getSeatCol(self):
        lower = 0
        upper = 7
        for char in self.colCode:
            if char == 'L':
                upper = (upper + lower) // 2
            elif char == 'R':
                lower = math.ceil((upper + lower) / 2)
        if self.colCode[len(self.colCode) - 1] == 'L':
            self.col = lower
        elif self.colCode[len(self.colCode) - 1] == 'R':
            self.col = upper

    def getSeatID(self):
        return (self.row * 8) + self.col
