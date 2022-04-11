def main():

    rules = dict()
    with open("Problem7.txt") as infile:
        data = infile.read()

        data = data.replace(".", "")
        data = data.replace(" no other bags", "")
        data = data.replace(" bags", "")
        data = data.replace(" bag", "")
        data = data.split('\n')
        for line in data:
            line = line.split(" contain ")
            left = line[0]  # Store the outer bag
            right = []
            if len(line) > 1:
                line = line[1].split(', ')  # only look at inner bags
                for bag in line:  # break bags into individual strings ['1 bright white', '2 muted yellow']
                    value = bag.split(" ", 1)[0]  # convert line into value of each bag
                    if value != "no":
                        value = int(value)
                        name = bag.split(" ", 1)[1]
                        right.append([value, name])
                    rules[left] = right

    for key, value in rules.items():
        print(key + ": " + str(value))

main()
