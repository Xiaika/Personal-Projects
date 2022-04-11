from pprint import pprint

signal_patterns = list()
output_strings = list()

def diff(a: set, b: set) -> set:
    return a.difference(b)

with open('day8.txt') as file:
    data = file.read().splitlines()
    for line in data:
        signal_patterns.append([c for c in line.split('|')[0].split()])
        output_strings.append([c for c in line.split('|')[1].split()])

total = 0
 # Determine which numbers are displayed by which letters
for signal_pattern, output_string in zip(signal_patterns, output_strings):
    top = set()
    tl = set()
    tr = set()
    mid = set()
    bl = set()
    br = set()
    bot = set()
    d = dict()
    segments = dict()
    # Known digit pass
    for pattern in signal_pattern:
        s = set(pattern)
        match len(pattern):
            case 2: d[1] = s
            case 3: d[7] = s
            case 4: d[4] = s
            case 7: d[8] = s
    top = diff(d[7], d[1])
    segments['top'] = top
    bottom_left_corner = diff(diff(d[8], d[4]), top)
    m_tl = diff(d[4], d[1])
    # 6 segments pass
    for pattern in signal_pattern:
        s = set(pattern)
        match len(pattern):
            case 6:
                if len(s.intersection(bottom_left_corner)) == 1:
                    d[9] = s
                    bot = d[9].intersection(bottom_left_corner)
                    segments['bot'] = bot
                    bl = diff(bottom_left_corner, bot)
                    segments['bl'] = bl
                elif len(s.intersection(m_tl)) == 2:
                    d[6] = s
                    br = d[6].intersection(d[1])
                    segments['br'] = br
                    tr = diff(d[1], br)
                    segments['tr'] = tr
                elif len(s.intersection(m_tl)) == 1:
                    d[0] = s
                    mid = diff(d[8], d[0])
                    segments['mid'] = mid
                    tl = m_tl.intersection(d[0])
                    segments['tl'] = tl
    d[2] = diff(d[8], tl.union(br))
    d[3] = diff(d[8], tl.union(bl))
    d[5] = diff(d[8], tr.union(bl))

    count = 0
    for string in output_string:
        string = set(string)
        if list(d.keys())[list(d.values()).index(string)] in [1, 4, 7, 8]:
            count += 1
    total += count
# for digit, letters in d.items():
#     print(digit, letters)

print(f'Puzzle Solution: {total}')