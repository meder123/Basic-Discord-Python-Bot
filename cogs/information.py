import discord
from discord.ext import commands
class Information(commands.Cog):

        def __init__(self, client):
            self.client = client

        @commands.command(aliases=['latency'])
        async def ping(self, ctx):
            embed = discord.Embed(title=(f'Latency is {round(self.client.latency * 1000)}ms'), colour=discord.Colour.greyple())

            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Information(client))