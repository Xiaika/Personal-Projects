from Instruction import Instruction

def execute(instructions):
    currIndex = 0
    ACCUMULATOR = 0
    while True:
        if instructions[currIndex].hasRun():
            return ACCUMULATOR
        currOpp = instructions[currIndex].getOperation()
        currArg = instructions[currIndex].getArgument()
        currOperator = instructions[currIndex].getOperator()
        if currOpp == 'nop':
            instructions[currIndex].run()
            currIndex += 1
        if currOpp == 'acc':
            instructions[currIndex].run()
            if currOperator == '+':
                ACCUMULATOR += currArg
                currIndex += 1
            else:
                ACCUMULATOR -= currArg
                currIndex += 1
        elif currOpp == 'jmp':
            instructions[currIndex].run()
            if currOperator == '+':
                currIndex += currArg
            else:
                currIndex -= currArg

def corruptedExe(instructions):
    currIndex = 0
    ACCUMULATOR = 0
    finished = False
    while not finished:
        if instructions[currIndex] == instructions[-1]:
            finished = True
        if instructions[currIndex].hasRun():
            if currOpp == 'nop':
                currOpp = 'jmp'
            elif currOpp == 'jmp':
                currOpp = 'nop'
        else:
            currOpp = instructions[currIndex].getOperation()
        currArg = instructions[currIndex].getArgument()
        currOperator = instructions[currIndex].getOperator()
        if currOpp == 'nop':
            instructions[currIndex].run()
            currIndex += 1
        if currOpp == 'acc':
            instructions[currIndex].run()
            if currOperator == '+':
                ACCUMULATOR += currArg
                currIndex += 1
            else:
                ACCUMULATOR -= currArg
                currIndex += 1
        elif currOpp == 'jmp':
            instructions[currIndex].run()
            if currOperator == '+':
                currIndex += currArg
            else:
                currIndex -= currArg
    return ACCUMULATOR

def main():
    with open("Problem8.txt") as infile:
        data = infile.read().splitlines()
    instructions = []

    for string in data:
        instruction = Instruction(string)
        instructions.append(instruction)

    #print("ACCUMULATOR: " + str(execute(instructions)))
    for instruction in instructions:
        instruction.reset()
    print("FIXED: " + str(corruptedExe(instructions)))

main()