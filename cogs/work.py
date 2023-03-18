from discord.ext import commands
from random import randint
from tesda import Opens, datas, saves


class Work(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["w"])
    async def work(self, ctx):
        user = ctx.author
        Opens(user)
        users = datas()

        minEarn = 5
        maxEarn = 20
        earn = randint(minEarn, maxEarn)

        users[str(user.id)]["bank"] += earn

        saves(users)
        await ctx.reply("<:banks:1009395411900964985> **{:,}**€ ont été ajouté sur votre compte".format(earn),
                        mention_author=False)


async def setup(client):
    await client.add_cog(Work(client))
