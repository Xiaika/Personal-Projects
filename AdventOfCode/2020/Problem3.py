from Forest import Forest

def getTrees(forest, x, y):
    count = 0
    forest.reset()
    while forest.move(x, y):
        count += 1 if forest.hasTree() else 0
    return count

def main():
    data = []
    with open("Problem3.txt") as infile:
        data = infile.read().splitlines()

    forest = Forest(data)
    result = 1
    result *= getTrees(forest, 1, 1)
    result *= getTrees(forest, 3, 1)
    result *= getTrees(forest, 5, 1)
    result *= getTrees(forest, 7, 1)
    result *= getTrees(forest, 1, 2)

    print(result)

main()
