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
        # Parse address
        address = ''.join(i for i in key if i != '[' if i != ']')
        address = address.replace('mem', '')

        # convert address to 36 bit binary number
        address = bin(int(address))
        address = address.replace('0b', '', 1)
        address = address[::-1]
        for x in range(len(address), 36):
            address += '0'
        address = address[::-1]

        # Mask the address
        masked_addr = str()
        for mask_bit, bit in zip(masks[cur_mask - 1], address):
            if mask_bit == 'X':
                masked_addr += 'X'
            elif mask_bit == '0':
                masked_addr += '0'
            elif mask_bit == '1':
                masked_addr += '1'
        print(masked_addr)
        # Compute all possible combinations of Xs
        num_floating = masked_addr.count('X')
        combinations = []
        for i in range(2 ** num_floating):
            combinations.append(list(bin(i)[2:].zfill(num_floating)))

        for combo in combinations:
            i = 0
            nadd = ""
            for a in masked_addr:
                if a == "X":
                    nadd+=str(combinations[i])
                    i+=1
                else:
                    nadd+=str(a)
        print(nadd)



        # Create items in dictionary for every possible floating bit

