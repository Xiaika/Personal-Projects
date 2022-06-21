import voidcalc as vc
import os
from math import ceil
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
current_flag = '!voidcalc'
            #  Command   Text to display in format "Time left until X"

def parse_roles_and_input(roles, inputs):
    # Match case for each role
    # Format (['@everyone', 'Vanquisher I', 'Corruption 105', 'Sphere CoT', 'VIP CoT', 'VIP 9-10', 'BS 7', 'Senior Card', 'ㅤㅤㅤㅤㅤㅤVoid Botㅤㅤㅤㅤㅤㅤ')
    vortex = roles[1]
    corruption = roles[2].split(' ')[1]
    sphere = roles[3].split(' ')[1]
    vip_level = roles[4].split(' ')[1]
    vip_choice = roles[5].split(' ')[1]
    chests = 0
    match vip_level:
        case '0-1': chests = 0
        case '2-4': chests = 1
        case '5-6': chests = 2
        case '7-8': chests = 3
        case '9-10': chests = 4
        case '11+': chests = 5
        case _: raise ValueError(f'Role for Vip level {vip_level} is invalid')
    bs = True if roles[6] == 'BS 7' else False
    privilege = True if roles[7] == 'Senior Card' else False

    # Handle additional command line inputs
    # mcore=, $core=, hcore, hcot, hstel
    market_cores, bought_cores, hall_cores, hall_cot, hall_stellar = 0, 0, 0, 0, 0
    extra_info = False
    for i in inputs[1:]:
        print(i)
        if 'mcore=' in i:
            market_cores = int(i[6:])
        elif '$core=' in i:
            bought_cores = int(i[6:])
        elif 'hcore=' in i:
            hall_cores = int(i[6:])
            if hall_cores > 10:
                hall_cores = 10
            elif hall_cores < 0:
                hall_cores = 0
        elif 'hcot=' in i:
            hall_cot = int(i[5:])
            if hall_cot > 120000:
                hall_cot = 120000
            elif hall_cot < 0:
                hall_cot = 0
        elif 'hstel=' in i:
            hall_stellar = int(i[6:])
            if hall_stellar > 187500:
                hall_stellar = 187500
            elif hall_stellar < 0:
                hall_stellar = 0
        elif 'extra' in i:
            extra_info = True
        else:
            raise ValueError('Inputs dont match parameters')
    print(f'CORES - Market {market_cores}, Bought {bought_cores}, Hall {hall_cores}')
    print(f'Hall CoT {hall_cot}, Hall Stellar {hall_stellar}')

    return vc.total_void(vortex, corruption, sphere, chests, vip_choice, hall_cot=hall_cot,
                         hall_stellar=hall_stellar, bs=bs, privilege=privilege, market_cores=market_cores,
                         bought_cores=bought_cores, hall_cores=hall_cores, extra=extra_info)

def get_user_roles(user):
    roles = list()
    for role in user:
        role = str(role)
        role = role.split('name=')
        roles.append(role[0])
    return roles


def containsOnlyNumbers(value):
    digits = 0
    for character in value:
        if character.isdigit():
            digits += 1
    if digits == len(value):
        return True
    return False

def dif(a, b, length):
    temp = str()
    dif = length - abs(len(a) + len(b))
    for _ in range(dif):
        temp += ' '
    return temp

def goal_time(cot, stellar):
    cot_goal = 5000000
    stellar_goal = 4935000
    return ceil(cot_goal / cot), ceil(stellar_goal / stellar)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected')


@client.event
async def on_message(message):
    # TODO: add more output data
    LENGTH_D = 17
    LENGTH_M = 22
    if message.author == client.user:
        return
    msg = message.content.split(' ')
    if msg[0].lower() == current_flag:
        roles = get_user_roles(message.author.roles)
        t = parse_roles_and_input(roles, msg)
        if len(t) == 2:
            await message.channel.send(f'Daily Income:  \n<:CoT:988587418124976128>   **{t[0]:,}**\n'
                                       f'<:Stellar:988587432729542728>   **{t[1]:,}**\n'
                                       f'Monthly Income: \n<:CoT:988587418124976128>   **{t[0] * 30:,}**\n'
                                       f'<:Stellar:988587432729542728>   **{t[1] * 30:,}**')
            return
        else:
            # Formatting code
            vortex_dif_d = dif(str(t[0][0]), str(t[1][0]), LENGTH_D)
            realms_dif_d = dif(str(t[0][1]), str(t[1][1]), LENGTH_D)
            cores_dif_d =  dif(str(t[0][2]), str(t[1][2]), LENGTH_D)
            hall_dif_d = dif(str(t[0][3]), str(t[1][3]), LENGTH_D)
            ark_dif_d = dif(str(t[0][4]), str(t[1][4]), LENGTH_D)
            vip_dif_d = dif(str(t[0][5]), str(t[1][5]), LENGTH_D)
            vortex_dif_m = dif(str(t[0][0] * 30), str(t[1][0] * 30), LENGTH_M)
            realms_dif_m = dif(str(t[0][1] * 30), str(t[1][1] * 30), LENGTH_M)
            cores_dif_m = dif(str(t[0][2] * 30), str(t[1][2] * 30), LENGTH_M)
            hall_dif_m = dif(str(t[0][3] * 30), str(t[1][3] * 30), LENGTH_M)
            ark_dif_m = dif(str(t[0][4] * 30), str(t[1][4] * 30), LENGTH_M)
            vip_dif_m = dif(str(t[0][5] * 30), str(t[1][5] * 30), LENGTH_M)

            goal_days = goal_time(t[2], t[3])

            await message.channel.send(f'Daily Income:  \n<:CoT:988587418124976128>   **{t[2]:,}**\n'
                                       f'<:Stellar:988587432729542728>   **{t[3]:,}** \n'
                                       f'```ㅤㅤㅤㅤㅤCoT       Stellar\n'
                                       f'        ━━━━━━━━━━━━━━━━━━━━\n'
                                       f'Vortex: {t[0][0]}{vortex_dif_d}{t[1][0]}\n'
                                       f'Realms: {t[0][1]}{realms_dif_d}{t[1][1]}\n'
                                       f' Cores: {t[0][2]}{cores_dif_d}{t[1][2]}\n'
                                       f'  Hall: {t[0][3]}{hall_dif_d}{t[1][3]}\n'
                                       f'   Ark: {t[0][4]}{ark_dif_d}{t[1][4]}\n'
                                       f'   VIP: {t[0][5]}{vip_dif_d}{t[1][5]}```\n'
                                       f'Monthly Income:  \n<:CoT:988587418124976128>   **{t[2] * 30:,}**\n'
                                       f'<:Stellar:988587432729542728>   **{t[3] * 30:,}** \n'
                                       f'```ㅤㅤㅤㅤㅤ CoT          Stellar\n'
                                       f'        ━━━━━━━━━━━━━━━━━━━━━━━━\n'
                                       f'Vortex: {t[0][0] * 30}{vortex_dif_m}{t[1][0] * 30}\n'
                                       f'Realms: {t[0][1] * 30}{realms_dif_m}{t[1][1] * 30}\n'
                                       f' Cores: {t[0][2] * 30}{cores_dif_m}{t[1][2] * 30}\n'
                                       f'  Hall: {t[0][3] * 30}{hall_dif_m}{t[1][3] * 30}\n'
                                       f'   Ark: {t[0][4] * 30}{ark_dif_m}{t[1][4] * 30}\n'
                                       f'   VIP: {t[0][5] * 30}{vip_dif_m}{t[1][5] * 30}```\n'
                                       f'Goal Values: \n'
                                       f'<:CoT:988587418124976128>   **5,000,000** every **{goal_days[0]}** days\n'
                                       f'<:Stellar:988587432729542728>   **4,935,000** every **{goal_days[1]}** days')
            return

client.run(TOKEN)