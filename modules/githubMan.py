import discord
import sys
import os
import json
from github import Github
from discord.ext import commands


with open('config.json') as j:
   cf = json.load(j)

gh = Github(cf['config']['githubToken'])

class Github_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setNotif(self, ctx, args=None):
        cf['config']['notifChat'] = f"{ctx.message.channel}"
        os.remove('config.json')
        with open('config.json', 'w') as j:
            json.dump(cf, j, indent=4)
        await ctx.send('channel set!')

def setup(bot):
    bot.add_cog(Github_Commands(bot))