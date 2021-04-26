import discord
import sys
import json
from github import Github
from discord.ext import commands

class Github_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Github_Commands(bot))