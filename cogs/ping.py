from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pin(self, ctx):
        await ctx.send("t")


async def setup(client):
    await client.add_cog(Ping(client))
