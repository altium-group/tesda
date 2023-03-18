from discord.ext import commands
from discord.ext.commands import MissingPermissions


class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, nmbr: int):
        if nmbr is None:
            return await ctx.send("Veuillez indiquer un nombre.")
        messages = await ctx.channel.history(limit=nmbr + 1).flatten()
        for message in messages:
            await message.delete()
        print(f"{ctx.author.name} éffacé(e) {nmbr} messages")

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("Vous n'avez pas la permission (`gérer les messages`).")


async def setup(client):
    await client.add_cog(Clear(client))
