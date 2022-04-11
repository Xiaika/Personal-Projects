class Instruction:

    def __init__(self, string):
        self.operation, self.argument = string.split()
        self.operator = self.argument[0]
        self.argument = int(self.argument[1:])
        self.ran = False

    def reset(self):
        self.ran = False

    def hasRun(self):
        return self.ran

    def run(self):
        self.ran = True

    def toString(self):
        return " Instruction [" + self.operation + " " + self.operator + " " + str(self.argument) + ']'

    def getOperation(self):
        return self.operation

    def getArgument(self):
        return self.argument

    def getOperator(self):
        return self.operator
