"""Advent of code 2020: --- Day 20: Jurassic Jigsaw ---"""
from typing import Dict

from Puzzle import Puzzle
from typing import *
from collections import Counter

pieces: List[Puzzle] = list()
tempdata = list()
with open('Problem20.txt') as file:
    for line in file.read().splitlines():               # For else clause OP AF
        if line != '':
            tempdata.append(line)
        else:
            pieces.append(Puzzle(tempdata))
            tempdata = []
    else:
        pieces.append(Puzzle(tempdata))


counter: Dict[Puzzle, int] = Counter()

for i, old_piece in enumerate(pieces):
    for j, new_piece in enumerate(pieces):
        if i != j and old_piece == new_piece:
            counter[old_piece.name] += 1

print(counter)
corners = []
for key, value in counter.items():
    if value == 2:
        corners.append(key)

value = 1
for corner in corners:
    value *= int(corner[-4:])

print(f"The four corner IDs multiplied is {value} ")
