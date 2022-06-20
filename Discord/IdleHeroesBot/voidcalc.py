from data import realms, tiers, sectors

# Constants - Variables to implement inputs later
PRIVILEGE = True
BS_CLEAR = True
VIP_LEVEL = 10
MAX_ENERGY = 240
CORES_MARKET = 30
CORES_BOUGHT = 0
CORES_HALL = 10

VORTEX_CYCLE_PER_WEEK = 2 / 7
MULTIPLIER = 1
if PRIVILEGE:
    MULTIPLIER += 0.15
if BS_CLEAR:
    MULTIPLIER += 0.15


# ------------------------------------------- Cores -----------------------------------------------------------
def core_day(spheres):
    monthly_cores = CORES_MARKET + CORES_BOUGHT + CORES_HALL
    cot = round(monthly_cores * 8000 / 30)
    stellar = 0
    match spheres:
        case 'CoT':
            cot = cot + round(monthly_cores * 250000 / (15 * 30))
        case 'Stellar':
            stellar = round(monthly_cores * 250000 / (15 * 30))
        case _:
            raise ValueError('Invalid case for spheres')
    # print('Cores:', cot, stellar)
    return cot, stellar


core_day('Stellar')


# ------------------------------------------ VIP Chest ---------------------------------------------------------
def vip_chests_day(vip, choice):
    cot = 0
    stellar = 0
    if isinstance(vip, int):
        if vip < 0:
            raise ValueError('VIP must be positive')
        elif vip == 0:
            chests = 0
        elif vip < 5:
            chests = 1
        elif vip < 7:
            chests = 2
        elif vip < 9:
            chests = 3
        elif vip < 11:
            chests = 4
        elif vip <= 13:
            chests = 5
        else:
            raise ValueError('VIP must be a positive integer no greater than 13')
    else:
        raise ValueError('VIP must be of type integer')
    if choice == 'None':
        return cot, stellar
    elif choice == 'CoT':
        cot = 2500 * chests
    elif choice == 'Stellar':
        stellar = 2500 * chests
    else:
        raise ValueError('Invalid choice for chest contents')
    return cot, stellar


# ----------------------------------------- Void Vortex --------------------------------------------------------
def vortex_day(tier):
    cot, stellar = tiers[tier].values()
    cot = round(cot * MULTIPLIER * VORTEX_CYCLE_PER_WEEK)
    stellar = round(stellar * MULTIPLIER * VORTEX_CYCLE_PER_WEEK)
    # print(cot, stellar)
    return cot, stellar


vortex_day('Vanquisher I')

# ----------------------------------------- Realms Gate --------------------------------------------------------
# Route Data
chest_route = {'Total': {'Phantoms': 189.95, 'Puppets': 10.02, 'Lords': 1, 'Chests': 8.73, 'Mines': 4},
               'Energy': {'Phantoms': 949.77, 'Puppets': 100.23, 'Lords': 10, 'Chests': 87.35, 'Mines': 40}}

no_chest_route = {'Total': {'Phantoms': 192.31, 'Puppets': 9.89, 'Lords': 1, 'Chests': 8.53, 'Mines': 4},
                  'Energy': {'Phantoms': 961.57, 'Puppets': 98.89, 'Lords': 10, 'Chests': 85.33, 'Mines': 40}}
# corruption_level = str(input('Enter corruption level:  '))
corruption_level = '108'


def realm_cycle(level, route):
    # TODO: Check accuracy later but very good for now
    cot_values = [round(MULTIPLIER * value) for value in realms[level]['CoT'].values()]
    stellar_values = [round(MULTIPLIER * value) for value in realms[level]['Stellar'].values()]
    entity_values = list(route['Total'].values())
    cot_cycle = list()
    stellar_cycle = list()
    for c, e in zip(cot_values, entity_values):
        cot_cycle.append(round(c * e))
    for s, e in zip(stellar_values, entity_values):
        stellar_cycle.append(round(s * e))
    # Chests
    cot_per_chest = 400 * MULTIPLIER
    cot_per_mine = 9125 * MULTIPLIER
    cot_cycle.append(cot_per_chest * route['Total']['Chests'])
    cot_cycle.append(cot_per_mine * route['Total']['Mines'])
    return cot_cycle, stellar_cycle


def realm_day(level, route):
    energy_total = sum(route['Energy'].values())
    cycle = realm_cycle(level, route)
    cot_per_day = [round(value / energy_total * MAX_ENERGY) for value in cycle[0]]
    stellar_per_day = [round(value / energy_total * MAX_ENERGY) for value in cycle[1]]
    return sum(cot_per_day), sum(stellar_per_day)


# print(realm_day(corruption_level, chest_route))

# TODO: Void Ark Calculations (Fine for now make inputs variable)
HERO_COUNT = 15
HERO_MULTIPLIERS = [1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1, 1.0, 0.85, 0.7, 0.55, 0.4]
sectors_plan = {'1': {'days': 3, 'lodes': 8}, '2': {'days': 3, 'lodes': 8}, '3': {'days': 3, 'lodes': 8},
                '4': {'days': 3, 'lodes': 9}, '5': {'days': 3, 'lodes': 10}, '6': {'days': 14, 'lodes': 40}}
HEROES = [4, 3, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Function returns N largest elements
def Nmaxelements(list1, N):
    final_list = []
    for i in range(0, N):
        max1 = 0
        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j]
        list1.remove(max1)
        final_list.append(max1)
    return final_list


hero_multipliers = list()
for index, rank in enumerate(HEROES):
    temp = list()
    if rank == 0:
        hero_multipliers.append(0)
        continue
    for heroes in range(rank):
        hero_multipliers.append(HERO_MULTIPLIERS[index])
total_multiplier = sum(hero_multipliers)


def ark_day():
    lodes3 = round(sum(Nmaxelements(sorted(hero_multipliers, reverse=True), N=3)), 3)
    non3 = (total_multiplier - lodes3) / 12
    lodes4 = round(sum(Nmaxelements(sorted(hero_multipliers, reverse=True), N=4)), 3)
    non4 = (total_multiplier - lodes4) / 11
    sector_cot = list()
    sector_stellar = list()
    for key, value in sectors_plan.items():
        nodes = (value['days'] * HERO_COUNT - value['lodes']) / 2
        if value['lodes'] < 10:
            hero_mult = non3
        else:
            hero_mult = non4
        sector_cot.append(round(nodes * hero_mult * sectors[key]['CoT'] * MULTIPLIER))
        sector_stellar.append(round(nodes * hero_mult * sectors[key]['Stellar'] * MULTIPLIER))
    return round(sum(sector_cot) / 30), round(sum(sector_stellar) / 30)


def ark_store_day(cot, stellar):
    return round(cot / 30), round(stellar / 30)


def total_void(corruption, vortex_tier, core_choice, hall_cot, hall_stellar, vip_level, chest_choice):
    total_cot = realm_day(corruption, chest_route)[0] + vortex_day(vortex_tier)[0] + core_day(core_choice)[0] + ark_store_day(hall_cot, hall_stellar)[0] + ark_day()[0] + vip_chests_day(vip_level, chest_choice)[0]
    total_stellar = realm_day(corruption, chest_route)[1] + vortex_day(vortex_tier)[1] + core_day(core_choice)[1] + ark_store_day(hall_cot, hall_stellar)[1] + ark_day()[1] + vip_chests_day(vip_level, chest_choice)[1]
    return total_cot, total_stellar

