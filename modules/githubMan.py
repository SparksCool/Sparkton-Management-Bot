import discord
import sys
import os
import json
from github import Github
from discord.ext import commands


with open('config.json') as j:
   cf = json.load(j)


class Github_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def LastCommit(self, ctx, args=None):
        await ctx.send('this command is WIP')

def setup(bot):
    bot.add_cog(Github_Commands(bot))