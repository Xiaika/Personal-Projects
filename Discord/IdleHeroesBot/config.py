import os
from dotenv.main import load_dotenv
# TODO: named tuple for roles(name, color)
load_dotenv()

# Initialization
INITIALIZE_GUILD_ID = os.getenv('INITIALIZE_GUILD_ID', '')

BOT_DIVIDER_ROLE = ('ㅤㅤㅤㅤㅤㅤVoid Botㅤㅤㅤㅤㅤㅤ', 0x2f3136)
SENIOR_CARD_ROLE = ('Senior Card', 0xffffff)
BROKEN_SPACES_ROLE = ('BS 7', 0)
CHEST_COT_ROLE = ('Chest CoT', 0x753287)
CHEST_STELLAR_ROLE = ('Chest Stellar', 0x2c7edb)
CHEST_NONE_ROLE = ('Chest None', 0)
VIP0_ROLE = ('VIP 0-1', 0x000000)
VIP2_ROLE = ('VIP 2-4', 0xa74513)
VIP5_ROLE = ('VIP 5-6', 0x5e7c8a)
VIP7_ROLE = ('VIP 7-8', 0xc57f23)
VIP9_ROLE = ('VIP 9-10', 0x2f94d8)
VIP11_ROLE = ('VIP 11+', 0x2f94d8)
SPHERE_STELLAR_ROLE = ('Sphere Stellar', 0x2c7edb)
SPHERE_COT_ROLE = ('Sphere CoT', 0x753287)
CORRUPTION1_ROLE = ('Corruption 1', 0x170638)
CORRUPTION10_ROLE = ('Corruption 10', 0x170638)
CORRUPTION20_ROLE = ('Corruption 20', 0x170638)
CORRUPTION30_ROLE = ('Corruption 30', 0x170638)
CORRUPTION40_ROLE = ('Corruption 40', 0x170638)
CORRUPTION50_ROLE = ('Corruption 50', 0x170638)
CORRUPTION60_ROLE = ('Corruption 60', 0x170638)
CORRUPTION70_ROLE = ('Corruption 70', 0x170638)
CORRUPTION80_ROLE = ('Corruption 80', 0x170638)
CORRUPTION90_ROLE = ('Corruption 90', 0x170638)
CORRUPTION100_ROLE = ('Corruption 100', 0x170638)
CORRUPTION105_ROLE = ('Corruption 105', 0x170638)
CORRUPTION110_ROLE = ('Corruption 110', 0x170638)
CORRUPTION115_ROLE = ('Corruption 115', 0x170638)
CORRUPTION120_ROLE = ('Corruption 120', 0x170638)
FORERUNNERVI_ROLE = ('Forerunner VI', 0)
FORERUNNERI_ROLE = ('Forerunner I', 0)
PIONEERVI_ROLE = ('Pioneer VI', 0xcf975c)
PIONEERI_ROLE = ('Pioneer I', 0xcf975c)
EXPLORERVI_ROLE = ('Explorer VI', 0x82b8ec)
EXPLORERI_ROLE = ('Explorer I', 0x82b8ec)
VALIANTVI_ROLE = ('Valiant VI', 0xf2c736)
VALIANTI_ROLE = ('Valiant I', 0xf2c736)
DEFIERVI_ROLE = ('Defier VI', 0x8348bd)
DEFIERI_ROLE = ('Defier I', 0x8348bd)
VANQUISHERVI_ROLE = ('Vanquisher VI', 0xf02461)
VANQUISHERI_ROLE = ('Vanquisher I', 0xf02461)
DOMINATORVI_ROLE = ('Dominator VI', 0x991d1d)
DOMINATORI_ROLE = ('Dominator I', 0x991d1d)

INITIALIZE_ROLE_LIST = [SENIOR_CARD_ROLE, BROKEN_SPACES_ROLE, CHEST_COT_ROLE, CHEST_STELLAR_ROLE, BOT_DIVIDER_ROLE, CHEST_NONE_ROLE, VIP0_ROLE, VIP2_ROLE, VIP5_ROLE, VIP7_ROLE, VIP9_ROLE,
                        VIP11_ROLE, SPHERE_STELLAR_ROLE, SPHERE_COT_ROLE, CORRUPTION1_ROLE,
                        CORRUPTION10_ROLE, CORRUPTION20_ROLE, CORRUPTION30_ROLE, CORRUPTION40_ROLE,
                        CORRUPTION50_ROLE, CORRUPTION60_ROLE, CORRUPTION70_ROLE, CORRUPTION80_ROLE,
                        CORRUPTION90_ROLE, CORRUPTION100_ROLE, CORRUPTION105_ROLE, CORRUPTION110_ROLE,
                        CORRUPTION115_ROLE, CORRUPTION120_ROLE, FORERUNNERVI_ROLE, FORERUNNERI_ROLE,
                        PIONEERVI_ROLE, PIONEERI_ROLE, EXPLORERVI_ROLE, EXPLORERI_ROLE, VALIANTVI_ROLE,
                        VALIANTI_ROLE, DEFIERVI_ROLE, DEFIERI_ROLE, VANQUISHERVI_ROLE, VANQUISHERI_ROLE,
                        DOMINATORVI_ROLE, DOMINATORI_ROLE]

BOT_INTRO = """**__Tussi Role Assignment__**
You must have all necessary roles for the void calculation function to work. You may only have 1 of each type of role and any attempt to duplicate will result in an error. The bot will not let you have more than one role if they are of similar type. If you need to switch roles click to remove the one you have then click the new one you want.

__Role Requirements__
BS 7 and Senior Card are optional roles
One Sphere role must be selected
One VIP Role must be selected (0-1 if F2P)
One Chest role must be selected (None is an option)
One Vortex Tier must be selected
One Corruption Role must be selected

__Void Calculation__
After acquiring the correct roles, goto #income-calculator and invoke the command **!voidcalc** and Tussi will swiftly calculate your void resource income. 
If you want details on how much of the resources are coming from which parts of the game, click the green **Extra Info** Button

__Additional Commands__
For each of the following commands replace X with any integer value. If your input is out of range then the bot will force it to the nearest boundary. The order of these commands does not matter at all but they must be called with **!voidcalc**
**mcore=X** Monthly Market Cores (0-30)
**$core=X** Monthly Purchased Cores (0-540)
**hcore=X** Monthly Central Hall Cores (0-10)
**hcot=X**  Monthly Central Hall CoT (0-120000)
**hstel=X** Monthly Central Hall Stellar (0-187500)
Advanced Example: 
!voidcalc hcot=120000 mcore=30 hstel=187500 $core=6 hcore=10"""


# Bot Setup
PREFIX = '!'
BOT_NAME = "Tussi"
BOT_TOKEN = os.getenv('DISCORD_TOKEN', '')

# Guild IDs
# Coffee Shop
GUILD_ID = int(os.getenv('DISCORD_GUILD', ''))

# Discord Channel IDs
LEXI_CHANNEL_ID = int(os.getenv('LEXI_CHANNEL_ID', ''))
ROLE_ASSIGNMENT_ID = int(os.getenv('ROLE_ASSIGNMENT_ID', ''))

# Options Role IDs
SENIOR_ROLE_ID = int(os.getenv('SENIOR_ROLE_ID', ''))
BS7_ROLE_ID = int(os.getenv('BS7_ROLE_ID', ''))
SPHERE_COT_ROLE_ID = int(os.getenv('SPHERE_COT_ROLE_ID', ''))
SPHERE_STELLAR_ROLE_ID = int(os.getenv('SPHERE_STELLAR_ROLE_ID', ''))

OPTIONS_IDS = [SENIOR_ROLE_ID, BS7_ROLE_ID, SPHERE_COT_ROLE_ID, SPHERE_STELLAR_ROLE_ID]

# VIP Role IDs
VOID_BOT_ROLE_ID = int(os.getenv('VOID_BOT_ID', ''))
VIP01_ROLE_ID = int(os.getenv('VIP01_ROLE_ID', ''))
VIP24_ROLE_ID = int(os.getenv('VIP24_ROLE_ID', ''))
VIP56_ROLE_ID = int(os.getenv('VIP56_ROLE_ID', ''))
VIP78_ROLE_ID = int(os.getenv('VIP78_ROLE_ID', ''))
VIP910_ROLE_ID = int(os.getenv('VIP910_ROLE_ID', ''))
VIP11_ROLE_ID = int(os.getenv('VIP11_ROLE_ID', ''))
CHEST_NONE_ROLE_ID = int(os.getenv('CHEST_NONE_ROLE_ID', ''))
CHEST_STELLAR_ROLE_ID = int(os.getenv('CHEST_STELLAR_ROLE_ID', ''))
CHEST_COT_ROLE_ID = int(os.getenv('CHEST_COT_ROLE_ID', ''))

# Vortex Role IDs
VANQUISHERI_ROLE_ID = int(os.getenv('VANQUISHERI_ROLE_ID', ''))
VANQUISHERVI_ROLE_ID = int(os.getenv('VANQUISHERVI_ROLE_ID', ''))
DEFIERI_ROLE_ID = int(os.getenv('DEFIERI_ROLE_ID', ''))
DEFIERVI_ROLE_ID = int(os.getenv('DEFIERVI_ROLE_ID', ''))
VALIANTI_ROLE_ID = int(os.getenv('VALIANTI_ROLE_ID', ''))
VALIANTVI_ROLE_ID = int(os.getenv('VALIANTVI_ROLE_ID', ''))
EXPLORERI_ROLE_ID = int(os.getenv('EXPLORERI_ROLE_ID', ''))
EXPLORERVI_ROLE_ID = int(os.getenv('EXPLORERVI_ROLE_ID', ''))
PIONEERI_ROLE_ID = int(os.getenv('PIONEERI_ROLE_ID', ''))
PIONEERVI_ROLE_ID = int(os.getenv('PIONEERVI_ROLE_ID', ''))
FORERUNNERI_ROLE_ID = int(os.getenv('FORERUNNERI_ROLE_ID', ''))
FORERUNNERVI_ROLE_ID = int(os.getenv('FORERUNNERVI_ROLE_ID', ''))

# Realms Gate Rold IDs
CORRUPTION1_ROLE_ID = int(os.getenv('CORRUPTION1_ROLE_ID', ''))
CORRUPTION10_ROLE_ID = int(os.getenv('CORRUPTION10_ROLE_ID', ''))
CORRUPTION20_ROLE_ID = int(os.getenv('CORRUPTION20_ROLE_ID', ''))
CORRUPTION30_ROLE_ID = int(os.getenv('CORRUPTION30_ROLE_ID', ''))
CORRUPTION40_ROLE_ID = int(os.getenv('CORRUPTION40_ROLE_ID', ''))
CORRUPTION50_ROLE_ID = int(os.getenv('CORRUPTION50_ROLE_ID', ''))
CORRUPTION60_ROLE_ID = int(os.getenv('CORRUPTION60_ROLE_ID', ''))
CORRUPTION70_ROLE_ID = int(os.getenv('CORRUPTION70_ROLE_ID', ''))
CORRUPTION80_ROLE_ID = int(os.getenv('CORRUPTION80_ROLE_ID', ''))
CORRUPTION90_ROLE_ID = int(os.getenv('CORRUPTION90_ROLE_ID', ''))
CORRUPTION100_ROLE_ID = int(os.getenv('CORRUPTION100_ROLE_ID', ''))
CORRUPTION105_ROLE_ID = int(os.getenv('CORRUPTION105_ROLE_ID', ''))
CORRUPTION110_ROLE_ID = int(os.getenv('CORRUPTION110_ROLE_ID', ''))
CORRUPTION115_ROLE_ID = int(os.getenv('CORRUPTION115_ROLE_ID', ''))
CORRUPTION120_ROLE_ID = int(os.getenv('CORRUPTION120_ROLE_ID', ''))
