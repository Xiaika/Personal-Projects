import re

class Passport:

    def __init__(self, data):
        self.byr = 0
        self.iyr = 0
        self.eyr = 0
        self.hgt = 0
        self.hcl = ''
        self.ecl = ''
        self.pid = ''
        self.cid = 0
        self.valid = True

        # Parse the data array #
        self.dic = dict(e.split(':') for e in data)

        # print(self.dic)
        for k, v in self.dic.items():
            self.switch(k, v)
        self.valid = self.validate()

    def validate(self):
        return self.byr != 0 and self.iyr != 0 and self.eyr != 0 and self.hgt != 0 and self.hcl != '' and self.ecl != '' and self.pid != ''

    def switch(self, k, v):
        if k == 'byr':
            num = int(v)
            if 1920 <= num <= 2002:
                self.byr = num
        if k == 'iyr':
            num = int(v)
            if 2010 <= num <= 2020:
                self.iyr = num
        if k == 'eyr':
            num = int(v)
            if 2020 <= num <= 2030:
                self.eyr = num
        if k == 'hgt':
            units = str(v)
            num = str(v)
            units = units[len(units)-2 : len(units)]
            if units.isnumeric():
                return
            num = int(num.strip(units))
            if units.isalpha():
                if units == 'cm':
                    if 150 <= num <= 193:
                        self.hgt = num
                elif units == 'in':
                    if 59 <= num <= 79:
                        self.hgt = num
        if k == 'hcl':
            if re.match('^[#][0-9a-f]+$', v) is not None:
                self.hcl = v
        if k == 'ecl':
            if re.match('^(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)$', v) is not None:
                self.ecl = v
        if k == 'pid':
            if re.match('\\d{9}', v) is not None:
                self.pid = v
        if k == 'cid':
            self.cid = v
        else:
            return





    def toString(self):
        return "Passport [Birth Year: " + str(self.byr) + ", Issue Year: " + str(self.iyr) + ", Exp Year: " + str(
            self.eyr) \
               + ", Height: " + str(self.hgt) + ", Hair Color: " + str(self.hcl) + ", Eye Color: " + str(self.ecl) \
               + ", Passport ID: " + str(self.pid) + ", Country ID: " + str(self.cid) + ']'
