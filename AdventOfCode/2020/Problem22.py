
from collections import deque
player1 = deque()
player2 = deque()
with open("Problem22.txt") as infile:
    it = iter(infile.read().splitlines())
    for players in range(1, 3):
        next(it)
        for item in it:
            if item == '':

                break
            else:
                if players == 1:
                    player1.append(int(item))
                else:
                    player2.append(int(item))

numCycles = 0
while True:
    if len(player1) == 0:
        winner = player2
        break
    if len(player2) == 0:
        winner = player1
        break
    if player1[0] > player2[0]:
        player1.append(player1.popleft())
        player1.append(player2.popleft())
    elif player2[0] > player1[0]:
        player2.append(player2.popleft())
        player2.append(player1.popleft())
    numCycles += 1

score = sum((mult * card) for mult, card in enumerate(reversed(winner), start=1))

print(score)









