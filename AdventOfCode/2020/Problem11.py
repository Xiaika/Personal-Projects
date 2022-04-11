from SeatGrid import SeatGrid, WaitingRoomB, WaitingRoomA


def count_occupied(room):
    while True:
        temp = room.map.copy()
        room.occupy_seats()
        room.vacate_seats()
        if room.map == temp:
            break
    count = 0
    for point in room.map:
        if room[point] == '#':
            count += 1
    return count

with open("Problem11.txt") as infile:
    data = infile.read().splitlines()

room_A = WaitingRoomA(data)
room_B = WaitingRoomB(data)
count1 = count_occupied(room_A)
print(f'There are {count1} occupied seats in room A.')
count2 = count_occupied(room_B)
print(f'There are {count2} occupied seats in room B.')


