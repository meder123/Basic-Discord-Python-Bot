import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import os
import json

client = commands.Bot(command_prefix=".")
status = cycle(['random_status', 'random_status2', 'random_status3', 'random_status4', 'random_status5'])

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')

@tasks.loop(seconds=7)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server!')

def is_owner(ctx):
    return ctx.author.id == YOUR_ID_HERE

@client.command()
@commands.check(is_owner)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

    embed = discord.Embed(title=(f'{extension} was loaded.'), colour=discord.Colour.green())

    await ctx.send(embed=embed)

@client.command()
@commands.check(is_owner)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

    embed = discord.Embed(title=(f'{extension} was unloaded.'), colour=discord.Colour.red())

    await ctx.send(embed=embed)

@client.command()
@commands.check(is_owner)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

    embed = discord.Embed(title=(f'{extension} was reloaded.'), colour=discord.Colour.orange())

    await ctx.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('TOKEN_HERE')
