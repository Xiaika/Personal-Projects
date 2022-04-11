class Board:
    def __init__(self):
        self.board = list()
        self.marked = list()
        for y in range(5):
            row = list()
            for x in range(5):
                row.append(0)
            self.marked.append(row)

    def read_from_lines(self, lines):
        for n in range(5):
            row = [int(i) for i in lines[n].split() if i != '']
            self.board.append(row)

    def __str__(self):
        string = ''
        for row in self.board:
            for square in row:
                if square < 10:
                    string += '0' + str(square) + ' '
                else:
                    string += str(square) + ' '
            string += '\n'
        return string

    def mark_board(self, callout):
        for x, row in enumerate(self.board):
            for y, square in enumerate(row):
                if square == callout:
                    self.marked[x][y] = 1

    def detect_win(self):
        row_count = 0
        col_count = 0
        for row in self.marked:
            for square in row:
                if square == 1:
                    row_count += 1
            if row_count == 5:
                return True
            row_count = 0

        for col in zip(*self.marked):
            for square in col:
                if square == 1:
                    col_count += 1
            if col_count == 5:
                return True
            col_count = 0
        return False

    def calculate_score(self):
        score = 0
        for x in range(5):
            for y in range(5):
                if self.marked[x][y] == 0:
                    score += self.board[x][y]
        return score
