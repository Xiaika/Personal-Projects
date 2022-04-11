with open('day7.txt') as file:

    depths = [int(i) for i in file.readline().split(',')]

    targets = sorted(depths)
    min_fuel_cost = 9999999999999
    for target in targets:
        total_fuel = 0
        for depth in depths:
            fuel_cost = abs(target - depth)
            total_fuel += fuel_cost
        if total_fuel < min_fuel_cost:
            min_fuel_cost = total_fuel

    print(f'Puzzle Solution: {min_fuel_cost}')
