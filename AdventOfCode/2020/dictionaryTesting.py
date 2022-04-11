def main():

    list1 = ['ecl', 'pid', 'eyr', 'hcl']
    list2 = ['gry', 860033327, 2020, '#fffffd']

    ziped = zip(list1, list2)
    dic = dict(ziped)
    print(sorted(dic.keys()))

    iyr = 0
    eyr = 0
    byr = 0

main()