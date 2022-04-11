def parse2(data):
    bound = data[0].split('-')
    letter = data[1].strip(':')
    password = data[2]

    index1 = int(bound[0]) - 1
    index2 = int(bound[1]) - 1

    if index1 <= len(password) and index2 <= len(password):
        if (password[index1] == letter and password[index2] != letter)\
        or (password[index2] == letter and password[index1] != letter):
            return True
        else:
            return False


def parse(data):
    bound = data[0].split('-')
    letter = data[1].strip(':')
    password = data[2]

    lbound = int(bound[0])
    ubound = int(bound[1])

    letters = [0]*26

    # a = 97, z = 122
    for l in password:
        index = ord(l) - 97
        letters[index] += 1

    index = ord(letter) - 97
    if letters[index] < lbound or letters[index] > ubound:
        return False
    else:
        return True




def main():
    infile = open('./Problem2.txt', 'r')
    policies = []

    for line in infile:
        policies.append(line.rstrip())

    count  = 0
    count2 = 0
    data = []
    for policy in policies:
        data = policy.split()
        if parse(data):
            count = count + 1
        if parse2(data):
            count2 += 1
    print(count, count2)




#data = [policy.split() for policy in policies]


main()
