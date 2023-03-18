from discord.ext import commands
import discord
from tesda import isOwner, Opens, datas, saves


class Pay(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pay(self, ctx, userToPay: discord.Member = None, amount: int = None):
        user = ctx.author
        Opens(user)
        Opens(userToPay)
        users = datas()

        if amount > users[str(user.id)]["bank"]:
            return await ctx.send(f"Veuillez indiquer un montant inférieur.")
        else:
            users[str(user.id)]["bank"] -= amount
            users[str(userToPay.id)]["bank"] += amount
            saves(users)

            await ctx.reply("<:banks:1009395411900964985> **{:,}**€ ont été ajouté sur le compte de ".format(
                amount) + f"{userToPay.name}",
                            mention_author=False)


async def setup(client):
    await client.add_cog(Pay(client))
