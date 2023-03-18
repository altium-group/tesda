import discord, json
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from tesda import Opens, datas, saves


class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def eco(self, ctx, commande=None, user: discord.Member = None, amount: int = None):
        Opens(user)
        users = datas()
        if commande == "add":
            if user is None:
                return await ctx.send("Veuillez indiquer un membre.")
            elif amount is None:
                return await ctx.send("Veuillez indiquer une somme.")

            users[str(user.id)]["bank"] += amount

            saves(users)

            await ctx.reply("<:banks:1009395411900964985> **{:,}**€ ont été ajouté sur le compte de ".format(
                amount) + f"{user.name}", mention_author=False)

        elif commande == "remove":
            if user is None:
                return await ctx.send("Veuillez indiquer un membre.")
            elif amount is None:
                return await ctx.send("Veuillez indiquer une somme.")

            users[str(user.id)]["bank"] -= amount

            saves(users)

            await ctx.reply(
                "<:banks:1009395411900964985> **{:,}**€ ont été retiré du compte de ".format(amount) + f"{user.name}",
                mention_author=False)

    @eco.error
    async def eco_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("Vous n'avez pas la permission (`bannir des membres`).")


async def setup(client):
    await client.add_cog(Economy(client))
