import discord
import sys
import json
from discord.ext import commands

with open('config.json') as j:
   configfile = json.load(j)

class Main_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command(brief='Suggest a mod for the modpack')
    async def suggest(self, ctx, *, arg):
        print(int(configfile['config']['suggestChat']))
        channel =  self.bot.get_channel(int(configfile['config']['suggestChat']))
        
        await channel.send(arg + " - From: - " + ctx.author.mention)
        await ctx.send(f'Mod suggestion sent!')
    @commands.command(brief='snad?')
    async def snad(self, ctx,):
        await ctx.send(f' @Sparks_Cool#8750 ADD SNAD SNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD!!!!!!!!!S')

def setup(bot):
    bot.add_cog(Main_Commands(bot))
