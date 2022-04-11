with open('day2.txt') as file:
    data = [line.rstrip() for line in file.readlines()]
    commands = [command.split()[0] for command in data] # 'forward 5' -> ['forward', '5']
    values = [int(value.split()[1]) for value in data]

    x = 0
    y = 0
    aim = 0
    for command, value in zip(commands, values):
        match command:
            case 'forward': x += value; y += (aim * value)
            case 'up': aim -= value
            case 'down': aim += value

    print(f"Puzzle Solution: {x * y}")