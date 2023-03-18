import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from tesda import cooldConvert
import datetime


class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["to"])
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, user: discord.Member = None, time=None, *, reason=None):
        if user is None:
            return await ctx.send("Veuillez indiquer un membre.")
        elif time is None:
            return await ctx.send("Veuillez indiquer une durée.")
        elif reason is None:
            return await ctx.send("Veuillez indiquer une raison.")
        await user.timeout(until=datetime.datetime(time), reason=reason)
        await ctx.send(f"{user} à été mute pour {cooldConvert(time)} (`{reason}`).")

    @mute.error
    async def to_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("Vous n'avez pas la permission (`expulser des membres`).")


async def setup(client):
    await client.add_cog(Mute(client))
