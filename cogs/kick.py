import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member = None, *, reason=None):
        if reason is None:
            return await ctx.send("Veuillez indiquer une raison.")
        elif user is None:
            return await ctx.send("Veuillez indiquer un membre.")

        await ctx.guild.kick(user, reason=reason)
        await ctx.send(f"{user} à été expulsé(e) (`{reason}`).")
        print(f"{ctx.author.name} à explusé(e) {user.name}")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("Vous n'avez pas la permission (`expulser des membres`).")


async def setup(client):
    await client.add_cog(Kick(client))
