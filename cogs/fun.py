import discord
from discord.ext import commands
import random


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook is not so good.',
                 'Very doubtful.']
        embed = discord.Embed(description=(f'{random.choice(responses)}'), colour=discord.Colour.green()
        )

        await ctx.send(embed=embed)

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(title=('Please ask a question.'), colour=discord.Colour.red())
                
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))
