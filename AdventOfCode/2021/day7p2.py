def summation(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

with open('day7.txt') as file:

    depths = [int(i) for i in file.readline().split(',')]

    targets = list(range(max(depths) + 1))
    min_fuel_cost = 9999999999999
    for target in targets:
        total_fuel = 0
        for depth in depths:
            fuel_cost = summation(abs(target - depth))
            total_fuel += fuel_cost
        if total_fuel < min_fuel_cost:
            min_fuel_cost = total_fuel
            min_depth = target

    print(f'Puzzle Solution: {min_fuel_cost: ,} fuel consumed at a depth of {min_depth}')