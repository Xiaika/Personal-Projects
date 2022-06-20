from data import realms

# Constants
PRIVILEGE = True
BS_CLEAR = True
MAX_ENERGY = 240

# TODO: Privilage Card Multiplier
# TODO: Broken Spaces Multiplier
# TODO: Market Cores
# TODO: Cores for money
# TODO: VIP Chest Logic
# TODO: Vortex
# Tiers
# Smash

# ----------------------------------------- Realms Gate --------------------------------------------------------
# Route Data
chest_route = {'Total': {'Phantoms': 189.95, 'Puppets': 10.02, 'Lords': 1, 'Chests': 8.73, 'Mines': 4},
               'Energy': {'Phantoms': 949.77, 'Puppets': 100.23, 'Lords': 10, 'Chests': 87.35, 'Mines': 40}}

no_chest_route = {'Total': {'Phantoms': 192.31, 'Puppets': 9.89, 'Lords': 1, 'Chests': 8.53, 'Mines': 4},
                  'Energy': {'Phantoms': 961.57, 'Puppets': 98.89, 'Lords': 10, 'Chests': 85.33, 'Mines': 40}}
corruption_level = str(input('Enter corruption level:  '))
def realm_cycle(level, route):
    # TODO: Check accuracy later but very good for now
    multiplier = 1
    if PRIVILEGE:
        multiplier += 0.15
    if BS_CLEAR:
        multiplier += 0.15
    cot_values = [round(multiplier * value) for value in realms[level]['CoT'].values()]
    stellar_values = [round(multiplier * value) for value in realms[level]['Stellar'].values()]
    entity_values = list(route['Total'].values())
    cot_cycle = list()
    stellar_cycle = list()
    for c, e in zip(cot_values, entity_values):
        cot_cycle.append(round(c * e))
    for s, e in zip(stellar_values, entity_values):
        stellar_cycle.append(round(s * e))
    # Chests
    cot_per_chest = 400 * multiplier
    cot_per_mine = 9125 * multiplier
    cot_cycle.append(cot_per_chest * route['Total']['Chests'])
    cot_cycle.append(cot_per_mine * route['Total']['Mines'])
    return cot_cycle, stellar_cycle

def realm_day(level, route):
    energy_total = sum(route['Energy'].values())
    cycle = realm_cycle(level, route)
    cot_per_day = [round(value / energy_total * MAX_ENERGY) for value in cycle[0]]
    stellar_per_day = [round(value / energy_total * MAX_ENERGY) for value in cycle[1]]
    return sum(cot_per_day), sum(stellar_per_day)

print(realm_day(corruption_level, chest_route))

# Corruption Level
# Puppets
# Fights
# Bosses
# Chests
# TODO: Void Ark
# Central Hall
# Daily loot
# Void Lords
# Hero multipliers
