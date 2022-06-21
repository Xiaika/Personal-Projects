import os
from dotenv.main import load_dotenv

load_dotenv()

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