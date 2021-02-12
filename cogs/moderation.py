import discord
from discord.ext import commands
class Moderation(commands.Cog):

        def __init__(self, client):
            self.client = client

        @commands.command()
        @commands.has_permissions(kick_members=True)
        async def kick(self, ctx, member : discord.Member, *, reason=None):
            await member.kick(reason=reason)
            embed = discord.Embed(description=(f'{member} was kicked. Reason: {reason}'), colour=discord.Colour.orange())

            await ctx.send(embed=embed)

        @kick.error
        async def kick_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):

                embed = discord.Embed(title=(':x: Please specify who you are trying to kick'), colour=discord.Colour.red())
                
                await ctx.send(embed=embed)

        @commands.command()
        @commands.has_permissions(ban_members=True)
        async def ban(self, ctx, member : discord.Member, *, reason=None):
            await member.ban(reason=reason)
            embed = discord.Embed(description=(f'{member.mention} was banned. Reason: {reason}'), colour=discord.Colour.orange())

            await ctx.send(embed=embed)

        @ban.error
        async def ban_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):

                embed = discord.Embed(title=(':x: Please specify who you are trying to ban.'), colour=discord.Colour.red())
                
                await ctx.send(embed=embed)

        @commands.command()
        @commands.has_permissions(ban_members=True)
        async def unban(self, ctx, *, member):
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user

                if(user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    embed = discord.Embed(description=(f'{user.mention} has been unbanned. ✔️'), colour=discord.Colour.green())

                    await ctx.send(embed=embed)
                    return

        @unban.error
        async def unban_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):

                embed = discord.Embed(title=(':x: Please specify who you are trying to unban.'), colour=discord.Colour.red())
                
                await ctx.send(embed=embed)
        
        @commands.command(aliases=['clear'])
        @commands.has_permissions(manage_messages=True)
        async def purge(self, ctx, amount : int):
            await ctx.channel.purge(limit=amount)
            embed = discord.Embed(description=(f'{amount} message/s were deleted.'), colour=discord.Colour.orange())

            await ctx.send(embed=embed)

        @purge.error
        async def purge_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):

                embed = discord.Embed(title=(':x: Please specify the amount of messages you want to be deleted.'), colour=discord.Colour.red())
                
                await ctx.send(embed=embed)

        @commands.command(alisases=['m'])
        @commands.has_permissions(kick_members=True)
        async def mute(self, ctx, member : discord.Member, *, reason=None):
            muted_role = ctx.guild.get_role(717047942934167662)
            
            await member.add_roles(muted_role)
            await member.mute(reason=reason)

            embed = discord.Embed(description=(f'{member.mention} was muted. Reason: {reason}'), colour=discord.Colour.orange())

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Moderation(client))