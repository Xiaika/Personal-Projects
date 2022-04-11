from collections import Counter

def check_interval(interval: str, value):
    """Check if a value exists in the given interval"""
    lower = int(interval.split('-')[0])
    upper = int(interval.split('-')[1])
    for x in range(lower, upper + 1):
        if x == value:
            return True
    return False


def find_invalid_tickets(nearby_tickets):
    """See which tickets match none of the field intervals"""
    invalid_tickets = list()
    for ticket in nearby_tickets:
        for value in ticket:
            checked_val = value
            num_checked = 0
            for intervals in fields.values():
                isvalid = False
                for interval in intervals:
                    if check_interval(interval, value) is True:
                        isvalid = True
                        break
                    num_checked += 1
                if isvalid:
                    break
            # if all possible intervals were checked and not found then invalid
            if num_checked == (len(fields.values()) * 2):
                invalid_tickets.append(checked_val)
    return invalid_tickets


def remove_invalid(nearby_tickets, invalid_tickets):
    """Removes all invalid tickets from the nearby tickets list"""
    temp_tickets = nearby_tickets.copy()
    for ticket in nearby_tickets:
        for value in ticket:
            if value in invalid_tickets:
                temp_tickets.remove(ticket)
    return temp_tickets


def order_fields(nearby_tickets):
    """Order the fields by the order of occurring fields"""
    # Transpose the matrix to check all columns
    transpose = list(zip(*nearby_tickets))
    field_order = list()
    # For every value in the column find which field applies to all
    for column in transpose:
        counter = Counter()
        for value in column:
            temp_fields = fields.copy()
            for key, intervals in temp_fields.items():
                range1, range2 = intervals
                if check_interval(range1, value) or check_interval(range2, value):
                    if key not in field_order:
                        counter[key] += 1
        for key, count in counter.items():
            if count == len(column):  # Field applies to all values in the column
                if key not in field_order:
                    field_order.append(key)
                    break
    return field_order


with open('Problem16.txt') as infile:
    # Parse the file
    group = 0  # Counter to detect which grouping of data we are parsing
    fields = dict()
    nearby_tickets = list()
    for line in infile:
        if line.rstrip() == '':
            group += 1
        if group == 0:  # Fields
            line = line.rstrip()
            name = line.split(':')[0]
            ranges = line.split(':')[1].lstrip()
            ranges = ranges.split(' or ')
            fields[name] = ranges
        if group == 1:  # My ticket
            line = line.rstrip()
            if line != 'your ticket:' and line != '':
                my_ticket = line.split(',')
        if group == 2:  # Nearby tickets
            line = line.rstrip()
            if line != 'nearby tickets:' and line != '':
                line = line.split(',')
                nearby_ticket = [int(num) for num in line]
                nearby_tickets.append(nearby_ticket)

invalid_tickets = find_invalid_tickets(nearby_tickets)
error_rate = sum(invalid_tickets)
print(f'Ticket scanning error rate: {error_rate}')

# Remove all invalid tickets from nearby_tickets
nearby_tickets = remove_invalid(nearby_tickets, invalid_tickets)
# transpose the nearby tickets into a list of index[0] of every row
order = order_fields(nearby_tickets)
print(order)  # <-- Wrong answer!










