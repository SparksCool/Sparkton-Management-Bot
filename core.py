import discord
import sys
import json
from discord.ext import commands

with open('config.json') as j:
    configfile = json.load(j)
 
TOKEN = configfile['config']['token']
print('token is ' + TOKEN)

bot = commands.Bot(command_prefix=configfile['config']['prefix'], description='Management Bot',  case_insensitive=True)


if __name__ == '__main__':
    for cog in configfile['config']['cogs']:
        print(cog)
        try:
            bot.load_extension(cog['cog'])
            print(f"loaded cog: {cog['cog']}.")
        except Exception as error:
            print(f"failed to load {cog['cog']}.")


@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    print(f'Successfully logged in and booted...!')


bot.run(TOKEN, bot=True, reconnect=True)










