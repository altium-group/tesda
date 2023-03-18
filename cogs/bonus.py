import random
from discord.ext import commands
from tesda import Opens, datas, saves
from discord.ext.commands import MissingAnyRole


class Bonus(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 43200)
    @commands.has_any_role(1014508719985410148)
    async def bonus(self, ctx):
        user = ctx.author
        Opens(user)
        users = datas()

        minEarn = 100
        maxEarn = 1200
        earn = random.randint(minEarn, maxEarn)

        users[str(user.id)]["bank"] += earn

        saves(users)

        await ctx.reply("<:banks:1009395411900964985> **{:,}**€ ont été ajouté sur votre compte".format(earn),
                        mention_author=False)

    @bonus.error
    async def bonus_error(self, ctx, error):
        if isinstance(error, MissingAnyRole):
            await ctx.send("Vous n'avez pas la permission (`être vip`).")


async def setup(client):
    await client.add_cog(Bonus(client))
