import discord
import sys
import json

TOKEN = 'no'
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    user = message.author
    
    if message.content.startswith('$'):
        content = message.content[1:].split(" ", 1)
        if len(content) > 1:
            cmd, args = content[0], content[1]
        else:
            cmd, args = content[0], ""
    else:
        return

    ##Commands
    cmd == cmd.lower()

    if cmd == 'help':
        await message.channel.send( 'there are no commands as of now rip.')


client.run(TOKEN)



