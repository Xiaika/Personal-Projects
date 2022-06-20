from pprint import pprint

# Create Dictionary of dictionaries for Realms Gate Corruption Level Data
with open("Corruption Data.csv") as file:
    fields = file.readline()
    realms = dict()
    for line in file.read().splitlines():
        line = line.split(',')
        corruption = str(line[0])
        cot = [int(line[value]) for value in range(1, 7, 2)]
        stellar = [float(line[value]) for value in range(2, 7, 2)]
        realms[corruption] = {'CoT': {'Phantom': cot[0], 'Puppet': cot[1], 'Lord': cot[2]},
                              'Stellar': {'Phantom': stellar[0], 'Puppet': stellar[1], 'Lord': stellar[2]}}

