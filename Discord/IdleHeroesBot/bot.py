import nextcord.ui
from nextcord.ext import commands
from math import ceil
from config import BOT_TOKEN, INITIALIZE_ROLE_LIST, BOT_INTRO
import voidcalc as vc
from Role_Views.Options_Role_View import OptionsRoleView
from Role_Views.Vip_Role_View import VipRoleView
from Role_Views.Vortex_Role_View import VortexRoleView
from Role_Views.Realms_Role_View import RealmsRoleView
from extra_view import ExtraButtonView

command_prefix = '!'

# TODO: Make initializer calls only respond to me (owner)
# TODO: have error handle for wrong role selections

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:
            # Register the persistent view for listening here.
            # Note that this does not send the view to any message.
            # To do that, you need to send a message with the View as shown below.
            # If you have the message_id you can also pass it as a keyword argument, but for this example
            # we don't have one.
            self.add_view(OptionsRoleView())
            self.add_view(VipRoleView())
            self.add_view(VortexRoleView())
            self.add_view(RealmsRoleView())
            self.persistent_views_added = True
        print(f'Logged in as {self.user}')

intents = nextcord.Intents.default()
intents.message_content = True

client = Bot(command_prefix=command_prefix, intents=intents)


@client.command()
async def options(ctx):
    view = OptionsRoleView()
    await ctx.send('Click a button to get a role. Click again to remove a role.'
                   '\n**__Global Multipliers and Spheres__**', view=view)



@client.command()
async def vip(ctx):
    view = VipRoleView()
    await ctx.send('\n**__VIP Level and Chest Preferences__**', view=view)


@client.command()
async def vortex(ctx):
    view2 = VortexRoleView()
    await ctx.send('\n**__Vortex Tiers__**', view=view2)


@client.command()
async def realm(ctx):
    view3 = RealmsRoleView()
    await ctx.send('\n**__Realms Gate Corruption Levels__**', view=view3)

@client.command()
async def tussi(ctx):
    await ctx.send(BOT_INTRO)
    await options(ctx)
    await vip(ctx)
    await vortex(ctx)
    await realm(ctx)


@client.command()
async def initialize(ctx: nextcord.ext.commands.Context):
    """Initializes the bot on a new server"""
    for initial_role in INITIALIZE_ROLE_LIST:
        name = initial_role[0]
        color = initial_role[1]
        for role in ctx.guild.roles:
            if name == role.name:
                print('ROLE ALREADY EXISTS')
                break
        else:
            if color == 0:
                await ctx.guild.create_role(name=name, reason='Tussi needs it')
            else:
                await ctx.guild.create_role(name=name, color=nextcord.Color(color), reason='Tussi needs it')

    await ctx.guild.create_text_channel(name='tussi-role-assignment', reason='Tussi needs it')
    await ctx.guild.create_text_channel(name='income-calculator', reason='To use Tussi :3')
    # Get Tussi to post her buttons
    channel = nextcord.utils.get(ctx.guild.channels, name='tussi-role-assignment')
    print(f'Tussi is ready to go on {ctx.guild.name}')


def parse_roles_and_input(roles, inputs=None):
    # TODO: Make everything Future Proof (no positional roles)
    # Match case for each role
    # Format (['@everyone', 'Vanquisher I', 'Corruption 105', 'Sphere CoT', 'Chest CoT', 'VIP 9-10', 'BS 7', 'Senior Card', 'ㅤㅤㅤㅤㅤㅤVoid Botㅤㅤㅤㅤㅤㅤ')
    for role in roles:
        if role.split(' ')[0] in ['Vanquisher', 'Defier', 'Valiant', 'Explorer', 'Pioneer', 'Forerunner']:
            vortex = role
        if role.split(' ')[0] == 'Corruption':
            corruption = role.split(' ')[1]
        if role.split(' ')[0] == 'Sphere':
            sphere = role.split(' ')[1]
        if role.split(' ')[0] == 'VIP':
            vip_level = role.split(' ')[1]
        if role.split(' ')[0] == 'Chest':
            vip_choice = role.split(' ')[1]
        chests = 0
    match vip_level:
        case '0-1': chests = 0
        case '2-4': chests = 1
        case '5-6': chests = 2
        case '7-8': chests = 3
        case '9-10': chests = 4
        case '11+': chests = 5
        case _: raise ValueError(f'Role for Vip level {vip_level} is invalid')
    bs = True if 'BS 7' in roles else False
    privilege = True if 'Senior Card' in roles else False

    # Handle additional command line inputs
    # mcore=, $core=, hcore, hcot, hstel
    market_cores, bought_cores, hall_cores, hall_cot, hall_stellar = 0, 0, 0, 0, 0
    extra_info = True
    if inputs is not None:
        for i in inputs:
            print(i)
            if 'mcore=' in i:
                market_cores = int(i[6:])
                if market_cores > 30:
                    market_cores = 30
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

def goal_time(cot, stellar):
    cot_goal = 5000000
    stellar_goal = 4935000
    return ceil(cot_goal / cot), ceil(stellar_goal / stellar)


@client.command()
async def voidcalc(ctx, *args):
    if ctx.author == client.user:
        return
    roles = get_user_roles(ctx.author.roles)
    print(roles)
    message = list()
    if args is not None:
        for arg in args:
            message.append(arg)
        print(message)
    t = parse_roles_and_input(roles, message)
    print(f'Totals: {t}')
    view = ExtraButtonView(t)
    goal_days = goal_time(t[2], t[3])
    # await ctx.message.delete()
    await ctx.send(f'{ctx.message.author.mention}\n'
                f'Daily Income:\n<:CoT:988837366976372767>   **{t[2]:,}**\n'
                f'<:Stellar:988837339616931914>   **{t[3]:,}**\n\n'
                f'Monthly Income: \n<:CoT:988837366976372767>   **{t[2] * 30:,}**\n'
                f'<:Stellar:988837339616931914>   **{t[3] * 30:,}**\n\n'
                f'Goal Values: \n'
                f'<:CoT:988837366976372767>   **5,000,000** every **{goal_days[0]}** days\n'
                f'<:Stellar:988837339616931914>   **4,935,000** every **{goal_days[1]}** days\n'
                f'━━━━━━━━━━━━━━', view=view)
    return


client.run(BOT_TOKEN)