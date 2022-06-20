import voidcalc as vc
import math
import os
import discord
from datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
current_flag = '!VoidCalc'
            #  Command   Text to display in format "Time left until X"


def containsOnlyNumbers(value):
    digits = 0
    for character in value:
        if character.isdigit():
            digits += 1
    if digits == len(value):
        return True
    return False

@client.event
async def on_ready():
    print(f'{client.user.name} has connected')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.split(', ')
    print(msg)
    if msg[0] == current_flag:
        cot, stellar = vc.total_void(str(msg[1]), msg[2], msg[3], int(msg[4]), int(msg[5]), int(msg[6]), msg[7])
        await message.channel.send(f'Your daily income \nCoT: {cot:,}\nStellar: {stellar:,}')
        return

client.run(TOKEN)