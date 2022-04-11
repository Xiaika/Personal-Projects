
message_rules = dict()
messages = list()
with open('Problem19.txt') as file:
    next_group = False
    for line in file:
        line = line.rstrip()
        if line == '':
            next_group = True
            continue
        if not next_group:
            line = line.split(': ')
            rule_number = int(line[0])
            rules = line[1]
            rules = rules.split(' | ')
            temp = list()
            for string in rules:
                string = string.replace('"', '')
                string = string.split()
                temp.append(string)
            rules = temp
            message_rules[rule_number] = rules
        else:
            messages.append(line)

print(message_rules)
print(messages)



