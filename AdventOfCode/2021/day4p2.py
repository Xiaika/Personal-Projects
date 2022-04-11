from Board import Board

with open('day4.txt') as file:
    callouts = [int(i) for i in file.readline().split(',')]
    lines = [line.strip() for line in file.readlines()]
    boards = dict()
    num_boards = len(lines)//6
    file.readline()
    for i in range(num_boards):
        boards[i] = Board()
        boards[i].read_from_lines(lines[1 + (i*6):(5 + (i + 1) * 6)])

    winning_boards = list()
    for callout_count, callout in enumerate(callouts):
        for key in boards.keys():
            boards[key].mark_board(callout)
            if boards[key].detect_win() and key not in winning_boards:
                winning_boards.append(key)
            if len(winning_boards) == num_boards:
                score = boards[key].calculate_score()
                print(f"Board number {key + 1} won with a score of {score}")
                print(f'Puzzle Solution: {score * callout}')
                exit()