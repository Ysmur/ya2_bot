import datetime

import requests

import discord

from auth_data import DC_TOKEN
TOKEN = DC_TOKEN

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "set_timer" in message.content.lower():
        hour = int(message.content.lower().split()[2])
        min = int(message.content.lower().split()[4])
        await message.channel.send(f'The timer should start in {hour} hour and {min} minutes.')
        date = datetime.datetime.now()
        delta = datetime.timedelta(hours=hour, minutes=min)
        flag = True

    if flag:
        while True:
            if datetime.datetime.now() > date + delta:
                await message.channel.send('Time X!')
                flag = False
                break




client.run(TOKEN)