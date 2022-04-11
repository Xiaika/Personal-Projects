def bin_to_int(bin: str) -> int:
    int_val = 0
    for power, char in enumerate(reversed(bin)):
        if char == '1':
            int_val += (2 ** power)
    return int_val


with open("Problem14.txt", 'r') as infile:
    lines = [line for line in infile.read().splitlines()]

memory = dict()
masks = list()
cur_mask = 0
for line in lines:
    key, value = line.split(' = ')
    if key == 'mask':
        masks.append(value)
        cur_mask += 1
    else:
        address = ''.join(i for i in key if i != '[' if i != ']')
        address = address.replace('mem', '')
        address = int(address)
        value  = bin(int(value))
        value = value.replace('0b', '', 1)
        value = value[::-1]
        for x in range(len(value), 36):
            value += '0'
        value = value[::-1]
        masked_val = str()
        for mask_bit, bit in zip(masks[cur_mask - 1], value):
            if mask_bit == 'X':
                masked_val += bit
            elif mask_bit == '0':
                masked_val += '0'
            elif mask_bit == '1':
                masked_val += '1'
        masked_int = bin_to_int(masked_val)
        memory[address] = masked_int

result = sum(value for value in memory.values())
print('Sum of memory = ', result)






