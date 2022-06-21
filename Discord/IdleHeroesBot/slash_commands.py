import nextcord
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from config import BOT_TOKEN
import buttons

client = commands.Bot(command_prefix='!')

TESTING_GUILD_ID = 785377079700619264

@client.event
async def on_ready():
    print('Tussi is ready!')

@client.slash_command(guild_ids=[TESTING_GUILD_ID])
async def slashcommand_test(interaction: Interaction):
    await interaction.response.send_message("Hi Lexi")

@client.slash_command(name="repeat", description="repeats what a user says", guild_ids=[TESTING_GUILD_ID])
async def repeat(interaction: Interaction, message: str):
    await interaction.response.send_message(message)


client.run(BOT_TOKEN)