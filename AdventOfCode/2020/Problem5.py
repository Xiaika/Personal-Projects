from BoardingPass import BoardingPass

def highSeat(passes):
    max = 0
    for p in passes:
        max = p.getSeatID() if p.getSeatID() > max else max
    return max

def findMySeat(passes):
    seats = [0]*highSeat(passes)
    for p in passes:
        seats[p.getSeatID() - 1] = 1

    count = 0
    for seat in seats:
        if seat == 0 and count < 100:
            count += 1
        elif seat == 1:
            count += 1
        else:
            return count + 1


def main():
    with open('Problem5.txt') as infile:
        data = infile.read().splitlines()

    ## Boarding Pass Array
    passes = [BoardingPass(string) for string in data]
    print("This is the highest seat ID: " + str(highSeat(passes)))
    print("My seat ID is: " + str(findMySeat(passes)))

main()
