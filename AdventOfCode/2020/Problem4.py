from Passport import Passport

def main():

    data = []
    passports = []
    with open("Problem4.txt") as infile:
        for line in infile:
            if line != '\n':
                for string in line.split():
                    data.append(string)
            else:
                p = Passport(data)
                passports.append(p)
                data = []

    count = 0
    for p in passports:
        print(p.toString())
        count += 1 if p.validate() else 0
    print(count)


main()