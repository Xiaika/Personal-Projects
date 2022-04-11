def getTotalQuestions(groups):
    total = 0
    for group in groups:

        uniqueLetters = 0
        alpha = [0] * 26
        for people in group:
            for question in people:
                index = ord(question) - 97
                alpha[index] += 1
        for letter in alpha:
            if letter != 0:
                uniqueLetters += 1
        total += uniqueLetters
    return total

def allAnswered(groups):
    total = 0
    for group in groups:
        uniqueLetters = 0
        alpha = [0] * 26
        for people in group:
            for question in people:
                index = ord(question) - 97
                alpha[index] += 1
        for letter in alpha:
            if len(group) == letter:
                total += 1
    return total

def main():
    data = []
    groups = []
    with open('Problem6.txt') as infile:
        for line in infile:
            if line != '\n':
                data.append(line.rstrip())
            else:
                groups.append(data)
                data = []

    print("Total unique questions: " + str(getTotalQuestions(groups)))
    print("Total questions all answered: " + str(allAnswered(groups)))

main()
