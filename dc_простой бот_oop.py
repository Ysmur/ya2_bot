import random

import discord
from discord.ext import commands

from auth_data import DC_TOKEN
TOKEN = DC_TOKEN

bot = commands.Bot(command_prefix='#!')


@bot.command(name='randint')
async def my_randint(ctx, min_int, max_int):
    num = random.randint(int(min_int), int(max_int))
    await ctx.send(num)


bot.run(TOKEN)

class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    async def on_message(self, message):
        if message.author == self.user:
            return
        await message.channel.send("Спасибо за сообщение")
        if "привет" in message.content.lower():
            await message.channel.send("И тебе привет")



client = YLBotClient()
client.run(TOKEN)