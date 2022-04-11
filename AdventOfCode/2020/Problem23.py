from collections import deque
from typing import Deque, List
from pprint import pprint
INPUT = '193467258'

class LinkedListNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

my_input = [int(i) for i in INPUT]

def getDestination(cups: Deque[int], pickedCups: List[int], current_cup: int):
    """ Placeholder for possible DocString"""
    minCup = min(cups)
    for i in range(1, 11):
        if (current_cup - i) in pickedCups:
            continue
        if (current_cup - i) < minCup:
            maxCup = max(cups)
            for j in range(maxCup, -1, -1):
                if j in pickedCups:
                    continue
                else:
                    return j
        else:
            return current_cup - i


def cycle(oldcups: Deque[int]) -> Deque[int]:
    """Given a list of cups shift # of cups = index zero to be after destination"""
    cups = oldcups.copy()
    first_cup = cups[0]
    cups.append(cups.popleft())
    pickedCups = list()
    for i in range(3):
        cup = cups.popleft()
        pickedCups.append(cup)
    print("Picked up: ", pickedCups)
    destination = getDestination(cups, pickedCups, first_cup)
    print("Destination: ", destination)
    # Loop until index 0 is the destination
    num_shifts = 0
    while cups[0] != destination:
        cups.append(cups.popleft())
        num_shifts += 1
    cups.append(cups.popleft())
    num_shifts += 1
    for cup in reversed(pickedCups):
        cups.appendleft(cup)
    # Move starting cup back to starting position
    for x in range(num_shifts):
        cups.appendleft(cups.pop())
    return cups


def part1():
    cups = deque([int(num) for num in INPUT])

    for x in range(100):
        cups = cycle(cups)

    # shift until 1 is in the first element then store the rest
    for q in range(len(cups)):
        if cups[0] == 1:
            break
        else:
            cups.append(cups.popleft())
    result = list(cups)[1:]
    string = ''
    for num in result:
        string += str(num)
    print(string)


def part2():
    my_nodes = {}
    last_node = None
    for i in my_input:
        curr_node = LinkedListNode(i)
        my_nodes[i] = curr_node

        if last_node is not None:
            last_node.right = curr_node
            curr_node.left = last_node

        last_node = curr_node
    for i in range(len(my_input)+1, 1_000_001):
        curr_node = LinkedListNode(i)
        my_nodes[i] = curr_node
        if last_node is not None:
            last_node.right = curr_node
            curr_node.left = last_node
        last_node = curr_node

    # Complete the circle
    ptr = my_nodes[my_input[0]]
    last_node.right = ptr
    ptr.left = last_node

    ptr = my_nodes[my_input[0]]
    for i in range(10000000):
        p_val = ptr.item

        cup1 = ptr.right
        cup2 = cup1.right
        cup3 = cup2.right

        ptr.right = cup3.right
        ptr.right.left = ptr

        d_val = p_val - 1 or 1000000
        while d_val in (cup1.item, cup2.item, cup3.item):
            d_val = d_val - 1 or 1000000

        d_node = my_nodes[d_val]

        cup3.right = d_node.right
        cup3.right.left = cup3
        d_node.right = cup1
        cup1.left = d_node

        ptr = ptr.right

    while ptr.item != 1:
        ptr = ptr.right

    return ptr.right.item * ptr.right.right.item
print(f"Part 2 solution: {part2()}")




# part1()
part2()




