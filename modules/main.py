import discord
import sys
import json
from discord.ext import commands

class Main_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command(brief='a testing command')
    async def hello(self, ctx, args=None):
        print(self)
        await ctx.send(f'hello {ctx.author.mention}!')

def setup(bot):
    bot.add_cog(Main_Commands(bot))
