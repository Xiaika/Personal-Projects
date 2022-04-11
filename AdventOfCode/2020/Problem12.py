WAY_X = 10
WAY_Y = 1
currDirection = 0
BOAT_X = 0
BOAT_Y = 0

def computeActionPart2(action, value):
    global WAY_X
    global WAY_Y
    global BOAT_X
    global BOAT_Y
    global currDirection
    # Move boat to waypoint #
    if action == 'F':
        BOAT_X += WAY_X * value
        BOAT_Y += WAY_Y * value
    elif action == 'R':
        # Recalculate waypoint position #
        # find out which quadrant the waypoint is in #
        if value == 90:  # Rotate clockwise to next quadrant
            temp = WAY_X
            WAY_X = WAY_Y
            WAY_Y = -1 * temp
        elif value == 180:  # Invert x and y
            WAY_X *= -1
            WAY_Y *= -1
        elif value == 270:  # Same as left 90
            temp = WAY_Y
            WAY_Y = WAY_X
            WAY_X = -1 * temp
        else:
            print("Invalid degrees", value)
    elif action == 'L':
        if value == 90:  # Rotate anticlockwise to next quadrant
            temp = WAY_Y
            WAY_Y = WAY_X
            WAY_X = -1 * temp
        elif value == 180:  # Invert x and y
            WAY_X *= -1
            WAY_Y *= -1
        elif value == 270:  # Same as right 90
            temp = WAY_X
            WAY_X = WAY_Y
            WAY_Y = -1 * temp
        else:
            print("Invalid degrees", value)
    elif action == 'N':
        WAY_Y += value
    elif action == 'S':
        WAY_Y -= value
    elif action == 'E':
        WAY_X += value
    elif action == 'W':
        WAY_X -= value
    else:
        print("Invalid Action", action, value)

def computeAction(action, value):
    global BOAT_X
    global BOAT_Y
    global currDirection
    if action == 'F':
        if currDirection == 270:
            BOAT_Y += value
        elif currDirection == 90:
            BOAT_Y -= value
        elif currDirection == 0:
            BOAT_X += value
        elif currDirection == 180:
            BOAT_X -= value
    elif action == 'R':
        currDirection = (currDirection + value) % 360
    elif action == 'L':
        currDirection = (currDirection - value) % 360
    elif action == 'N':
        BOAT_Y += value
    elif action == 'S':
        BOAT_Y -= value
    elif action == 'E':
        BOAT_X += value
    elif action == 'W':
        BOAT_X -= value
    else:
        print("Invalid Action", action, value)

def main():
    global BOAT_X
    global BOAT_Y
    with open('Problem12.txt') as infile:
        moves = infile.read().splitlines()

    for move in moves:
        action = move[0]
        value = int(move[1:])
        computeAction(action, value)

    result1 = abs(BOAT_X) + abs(BOAT_Y)
    print("Manhattan Distance: " + str(result1))

    BOAT_X = 0
    BOAT_Y = 0
    for move in moves:
        action = move[0]
        value = int(move[1:])
        computeActionPart2(action, value)
        # print("Waypoint: " + str(WAY_X) + ',' + str(WAY_Y) +  " Boat: " + str(BOAT_X) + ',' + str(BOAT_Y))
    result2 = abs(BOAT_X) + abs(BOAT_Y)
    print("Manhattan Distance with Waypoint: " + str(result2))


main()