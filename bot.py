import discord
from discord.ext import commands

client=commands.Bot(command_prefix='!')
@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_member_join(member):
    print("A wild",member,"appeared")

@client.event
async def on_member_remove(member):
    print("The wild",member,"disappeared")

@client.command()
async def ping(ctx):
    await ctx.send(f"Hey! I am up and running with a ping of {round(client.latency*1000)}ms.")

client.run('ODQ1NzgzNTYyMzQyMTA1MDk5.YKl_Uw.W3xIDIErvstcu9U0-hoKx8e_C3Q')   #Place token between the ''
