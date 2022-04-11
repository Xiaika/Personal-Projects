from collections import Counter

def get_rating(bitstrings: list[str], inverse=False) -> int:
    """Checks each bit position for the most common value and assigns bit.
       Matches bitstrings with that bit and only keeps the final match."""
    bit_position = 0
    while len(bitstrings) > 1:
        counters = list()
        columns = list(zip(*bitstrings))
        c = Counter(columns[bit_position])
        if not inverse:
            current_bit = '1' if c['1'] >= c['0'] else '0'
        else:
            current_bit = '0' if c['0'] <= c['1'] else '1'
        passed = list()
        for row in bitstrings:
            if row[bit_position] == current_bit:
                passed.append(row)
        bitstrings = passed
        bit_position += 1
    return int(bitstrings[0], 2)

with open('day3.txt') as file:
    data = [line.rstrip() for line in file.read().splitlines()]

    oxygen_rating = get_rating(data)
    co2_rating = get_rating(data, inverse=True)

    print(f'Puzzle Solution: {oxygen_rating * co2_rating}')







