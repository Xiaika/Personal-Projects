from data import realms, tiers, sectors

# Actual Constants
MAX_ENERGY = 240
VORTEX_CYCLE_PER_WEEK = 2 / 7

# Constants - Variables to implement inputs from roles


# Extra command line input
CORES_MARKET = 0
CORES_BOUGHT = 0
CORES_HALL = 0

# ------------------------------------------- Cores -----------------------------------------------------------
def core_day(spheres, market=30, bought=0, hall=0):
    monthly_cores = market + bought + hall
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


# ------------------------------------------ VIP Chest ---------------------------------------------------------
def vip_chests_day(choice, chests):
    cot = 0
    stellar = 0
    if choice == 'None':
        return cot, stellar
    elif choice == 'CoT':
        cot = 2500 * chests
    elif choice == 'Stellar':
        stellar = 2500 * chests
    else:
        raise ValueError('Invalid Role for chest contents')
    return cot, stellar


# ----------------------------------------- Void Vortex --------------------------------------------------------
def vortex_day(tier, MULTIPLIER):
    cot, stellar = tiers[tier].values()
    cot = round(cot * MULTIPLIER * VORTEX_CYCLE_PER_WEEK)
    stellar = round(stellar * MULTIPLIER * VORTEX_CYCLE_PER_WEEK)
    # print(cot, stellar)
    return cot, stellar


# ----------------------------------------- Realms Gate --------------------------------------------------------
# Route Data
chest_route = {'Total': {'Phantoms': 189.95, 'Puppets': 10.02, 'Lords': 1, 'Chests': 8.73, 'Mines': 4},
               'Energy': {'Phantoms': 949.77, 'Puppets': 100.23, 'Lords': 10, 'Chests': 87.35, 'Mines': 40}}

no_chest_route = {'Total': {'Phantoms': 192.31, 'Puppets': 9.89, 'Lords': 1, 'Chests': 8.53, 'Mines': 4},
                  'Energy': {'Phantoms': 961.57, 'Puppets': 98.89, 'Lords': 10, 'Chests': 85.33, 'Mines': 40}}


def realm_cycle(level, route, MULTIPLIER):
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


def realm_day(level, route, MULTIPLIER):
    energy_total = sum(route['Energy'].values())
    cycle = realm_cycle(level, route, MULTIPLIER)
    cot_per_day = [round(value / energy_total * MAX_ENERGY) for value in cycle[0]]
    stellar_per_day = [round(value / energy_total * MAX_ENERGY) for value in cycle[1]]
    return sum(cot_per_day), sum(stellar_per_day)


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


def ark_day(MULTIPLIER):
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


def total_void(vortex_tier, corruption, core_choice, chests, chest_choice='None', hall_cot=0, hall_stellar=0,
               bs=False, privilege=False, market_cores=30, bought_cores=0, hall_cores=0, extra=False):
    # TODO: add support for dominator
    MULTIPLIER = 1
    if bool(privilege):
        MULTIPLIER += 0.15
    if bool(bs):
        MULTIPLIER += 0.15

    vortex_cot, vortex_stellar = vortex_day(vortex_tier, MULTIPLIER)
    realm_cot, realm_stellar = realm_day(corruption, chest_route, MULTIPLIER)
    core_cot, core_stellar = core_day(core_choice, market_cores, bought_cores, hall_cores)
    ark_store_cot, ark_store_stellar = ark_store_day(hall_cot, hall_stellar)
    ark_cot, ark_stellar = ark_day(MULTIPLIER)
    vip_cot, vip_stellar = vip_chests_day(chest_choice, chests)

    print(f'Vortex {vortex_cot, vortex_stellar}')
    print(f'Realms {realm_cot, realm_stellar}')
    print(f'Cores  {core_cot, core_stellar}')
    print(f'Ark Store {ark_store_cot, ark_store_stellar}')
    print(f'Ark {ark_cot, ark_stellar}')
    print(f'VIP {vip_cot, vip_stellar}')
    print('--------------------------------------')

    total_cot = vortex_cot + realm_cot + core_cot + ark_store_cot + ark_cot + vip_cot
    total_stellar = vortex_stellar + realm_stellar + core_stellar + ark_store_stellar + ark_stellar + vip_stellar

    if extra:
        cot_list = list()
        stellar_list = list()
        cot_list.append(vortex_cot)
        cot_list.append(realm_cot)
        cot_list.append(core_cot)
        cot_list.append(ark_store_cot)
        cot_list.append(ark_cot)
        cot_list.append(vip_cot)
        stellar_list.append(vortex_stellar)
        stellar_list.append(realm_stellar)
        stellar_list.append(core_stellar)
        stellar_list.append(ark_store_stellar)
        stellar_list.append(ark_stellar)
        stellar_list.append(vip_stellar)
        return cot_list, stellar_list, total_cot, total_stellar

    return total_cot, total_stellar

