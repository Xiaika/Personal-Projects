class Forest:
    def __init__(self, data):
        self.posx = 0
        self.posy = 0
        self.MAX_X = len(data[0])
        self.MAX_Y = len(data)
        self.map = [0] * self.MAX_X * self.MAX_Y
        i = 0
        for line in data:
            for char in line:
                self.map[i] = 1 if char == '#' else 0
                i += 1

    def reset(self):
        self.posx = 0
        self.posy = 0

    def move(self, x, y):
        self.posx += x
        self.posy += y
        return self.posy < self.MAX_Y

    def hasTree(self):
        return self.map[(self.posy * self.MAX_X) + (self.posx % self.MAX_X)] == 1
