# Predefined color codes for desired colors

class Color:


    def __init__(self, letter='#', color='\033[91m'):
        self.letter = letter
        match color:
            case 'green': self.color = '\033[92m'
            case 'yellow': self.color = '\033[93m'
            case 'cyan': self.color = '\033[96m'
            case 'red': self.color =  '\033[91m'
            case 'white': self.color = '\033[89m'

    def __repr__(self):
        return self.letter


    def set_color(self, color):
        self.color = color
