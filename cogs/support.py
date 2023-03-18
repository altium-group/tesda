from discord.ext import commands


class Support(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def support(self, ctx):
        await ctx.reply("Ca marche pas ? Rejoins le serveur de support:\nhttps://discord.gg/fbubxmWsaX\n", mention_author=False)


async def setup(client):
    await client.add_cog(Support(client))
