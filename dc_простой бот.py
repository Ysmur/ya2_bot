import discord
from auth_data import DC_TOKEN
TOKEN = DC_TOKEN
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} подключен к Discord!')
    for guild in client.guilds:
        print(
            f'{client.user} подключились к чату:\n'
            f'{guild.name}(id: {guild.id})'
        )


client.run(TOKEN)