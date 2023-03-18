import discord, sqlite3
from discord.ext import commands
from tesda import Opens, datas


class Bal(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["bal"])
    async def balance(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        Opens(user)
        users = datas()
        bankAmt = users[str(user.id)]["bank"]

        await ctx.reply(f"<:banks:1009395411900964985> {user.name} a" + " **{:,}**€ sur votre compte".format(bankAmt),
                        mention_author=False)


async def setup(client):
    await client.add_cog(Bal(client))
