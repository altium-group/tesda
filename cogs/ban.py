import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions


class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member = None, *, reason=None):
        if reason is None:
            return await ctx.send("Veuillez indiquer une raison.")
        elif user is None:
            return await ctx.send("Veuillez indiquer un membre.")

        await ctx.guild.ban(user, reason=reason)
        await ctx.send(f"{user} à été banni(e) (`{reason}`).")
        print(f"{ctx.author.name} à banni(e) {user.name}")

    @ban.error
    async def ban_error(self, ctx, error):
       if isinstance(error, MissingPermissions):
           await ctx.send("Vous n'avez pas la permission (`bannir des membres`).")


async def setup(client):
    await client.add_cog(Ban(client))
