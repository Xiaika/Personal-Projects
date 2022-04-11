class Seat:

    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        if char == '.':
            self.state = 0
        elif char == 'L':
            self.state = 1
        else:
            self.state = 2


    def getX(self): return self.x
    def getY(self): return self.y
    def getState(self): return self.state

    def sit(self):
        self.state = 2

    def unsit(self):
        self.state = 1

    def toString(self):
        return "x:" + str(self.x) + " y:" + str(self.y) + " state:" + str(self.state)
