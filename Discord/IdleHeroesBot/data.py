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

with open('Vortex Data.csv') as file:
    fields = file.readline()
    tiers = dict()
    for line in file.read().splitlines():
        line = line.split(',')
        tier = line[0]
        cot = int(line[1])
        stellar = int(line[2])
        tiers[tier] = {'CoT': cot, 'Stellar': stellar}

with open('Ark Data.csv') as file:
    fields = file.readline()
    sectors = dict()
    for line in file.read().splitlines():
        line = line.split(',')
        sector = line[0]
        stellar = int(line[1])
        cot = int(line[2])
        sectors[sector] = {'CoT': cot, 'Stellar': stellar}