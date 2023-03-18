from discord.ext import commands
from discord.ext.commands import MissingPermissions


class ListBan(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def lban(self, ctx, *, type=None):
        ids = []
        bans = await ctx.guild.bans()
        for i in bans:
            ids.append(str(i.user.id))
        await ctx.send("La liste des utilisateurs banni:")
        await ctx.send(f"\n<@{ids}> - {ids}")
        print(f"{ctx.author.name} à afficher la liste des ban")

    @lban.error
    async def lban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("Vous n'avez pas la permission (`bannir des membres`).")


async def setup(client):
    await client.add_cog(ListBan(client))
