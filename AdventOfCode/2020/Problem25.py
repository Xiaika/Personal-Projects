Loop_Size = int
Encryption_Key = int
def transform(public_key) -> Loop_Size:
    subject_number = 7
    value = 1
    loop_size = 0
    while value != public_key:
        value *= subject_number
        value %= 20201227
        loop_size += 1
    return loop_size

def decrypt(loop_size, public_key) -> Encryption_Key:
    subject_number = public_key
    value = 1
    for x in range(loop_size):
        value *= subject_number
        value %= 20201227
    return value

with open('Problem25.txt') as infile:
    public_key1, public_key2 = (int(line.rstrip()) for line in infile)

loop_size1 = transform(public_key1)
encryption_key = decrypt(loop_size1, public_key2)
print("Encryption key: ", encryption_key)