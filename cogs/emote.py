import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions


class Emote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def emote(self, ctx, emote: discord.Emoji = None):
        if emote is None:
            return await ctx.send("Veuillez indiquer une emote.")
        await ctx.send(f"Voici {emote} :\nNuméros Id: {emote.id},\nUrl: {emote.url}\nRobot: \n{emote}.")

    @emote.error
    async def emote_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("Vous n'avez pas la permission (`gérer les messages`).")


async def setup(client):
    await client.add_cog(Emote(client))
