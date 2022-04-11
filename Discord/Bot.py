# bot.py
import datetime
import math
import os
import discord
from datetime import datetime as dt
from dotenv import load_dotenv
from math import floor

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
launch = 'Noon'
date = dt(year=2022, month=2, day=22, hour=11)
current_flag = ('WQ!', 'Witch Queen')
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

    if message.content == current_flag[0]:
        now = dt.now()
        time_left = dt(year=date.year, month=date.month, day=date.day, hour=date.hour)\
                    - dt(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute, second=now.second)
        s = time_left.seconds
        h, s = divmod(s, 3600)
        m, s = divmod(s, 60)
        await message.channel.send(f'Time left until {current_flag[1]} \n'
                                   f'**{time_left.days:02d}:{h:02d}:{m:02d}:{s:02d} @ {launch} EST**')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.split(' ')
    if msg[0].lower() in ['!tt', '!tripletap', '!fttc']:
        if msg[1].startswith('-'):
            await message.channel.send('Umm...you kinda need 4 shots...')
            return
        if containsOnlyNumbers(msg[1]):
            mag_size = int(msg[1])
            if msg[0].lower() == '!fttc':
                if mag_size in [0, 1, 2, 3] or mag_size < 0:
                    await message.channel.send('Umm...you kinda need 4 shots...')
                    return
                total_ammo = math.floor(((2 * mag_size) - 3 + (1 + (-1 ** mag_size) / 2)))
                if mag_size % 2 == 0:
                    total_ammo += 1
            if msg[0].lower() in ['!tt', '!tripletap']:
                if mag_size in [0, 1, 2] or mag_size < 0:
                    await message.channel.send('Umm...you kinda need 4 shots...')
                    return
                total_ammo = mag_size + math.floor((mag_size - 1) / 2)
            else:
                return

            await message.channel.send(f'With a magazine size of **{mag_size}** you will get **{abs(total_ammo - mag_size)}**' +
            f' extra shots for a __total of **{total_ammo}**__ in the mag.')


client.run(TOKEN)
