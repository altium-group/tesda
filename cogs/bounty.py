from discord.ext import commands
import discord
from tesda import Opens, datas, saves, isOwner


class Bounty(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(2, 86400)
    async def bounty(self, ctx, cmd=None, user: discord.Member = None, amount: int = None):
        Opens(user)
        users = datas()
        if user == ctx.author:
            return await ctx.send("Veuillez indiquer un autre membre")
        elif cmd is None:
            return await ctx.send("Veuillez indiquer une commande")
        elif user is None:
            return await ctx.send("Veuillez indiquer un membre")
        elif cmd == "set":
            if amount > users[str(ctx.author.id)]["bank"]:
                return await ctx.send(f"Veuillez indiquer un montant inférieur.")
            else:
                users[str(user.id)]["bounty"] = amount
                users[str(ctx.author.id)]["bank"] -= amount
                await ctx.reply("<:target:1011980645406351371> Vous avez placé une prime de {:,}€".format(amount) + f" sur {user.name}", mention_author=False)
        elif cmd == "catch":
            if users[str(ctx.author.id)]["power"] < users[str(user.id)]["power"]:
                return await ctx.send("Vous n'avez pas assez de *power*")
            else:
                users[str(ctx.author.id)]["bank"] += users[str(user.id)]["bounty"]
                users[str(user.id)]["bounty"] = 0
                await ctx.reply(f"Vous avez récupérer la prime de {user.name}", mention_author=False)
        saves(users)


async def setup(client):
    await client.add_cog(Bounty(client))
