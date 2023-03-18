import discord
from discord.ext import commands
from tesda import Opens, datas


class Level(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["lvl"])
    async def level(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        Opens(user)
        users = datas()
        xpAmt = users[str(user.id)]["xp"]
        lvlAmt = users[str(user.id)]["lvl"]
        nextlvl = users[str(user.id)]["lvl"] * 4 * 50

        await ctx.send(
            f"<:xp:999082525429338233> {user.name} est niveau {lvlAmt} (`" + "{:,}/{:,}`)".format(xpAmt, nextlvl))


async def setup(client):
    await client.add_cog(Level(client))
