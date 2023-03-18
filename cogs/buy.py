from discord.ext import commands
from tesda import Opens, datas, saves


class Buy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def buy(self, ctx, item=None, amount: int = 1):
        user = ctx.author
        Opens(user)
        users = datas()
        if item == "gold":
            if amount * 750 >= users[str(user.id)]["bank"]:
                return await ctx.send(f"Veuillez indiquer un montant inférieur.")
            else:
                users[str(user.id)]["gold"] += amount
                users[str(user.id)]["bank"] -= amount * 2250
                await ctx.send(f"Vous avez acheté {amount} <:gold:1004727089615872071> pour {amount * 750}€.")
                saves(users)
        if item == "copper":
            if amount * 292.5 >= users[str(user.id)]["bank"]:
                return await ctx.send(f"Veuillez indiquer un montant inférieur.")
            else:
                users[str(user.id)]["copper"] += amount
                users[str(user.id)]["bank"] -= amount * 225
                await ctx.send(f"Vous avez acheté {amount} <:copper:1004692203035172954> pour {amount * 292.5}€.")
                saves(users)
        if item == "steel":
            if amount * 187.5 >= users[str(user.id)]["bank"]:
                return await ctx.send(f"Veuillez indiquer un montant inférieur.")
            else:
                users[str(user.id)]["steel"] += amount
                users[str(user.id)]["bank"] -= amount * 112.5
                await ctx.send(f"Vous avez acheté {amount} <:steel:1004693606927454208> pour {amount * 292.5}€.")
                saves(users)
        if item == "tin":
            if amount * 112.5 >= users[str(user.id)]["bank"]:
                return await ctx.send(f"Veuillez indiquer un montant inférieur.")
            else:
                users[str(user.id)]["tin"] += amount
                users[str(user.id)]["bank"] -= amount * 45
                await ctx.send(f"Vous avez acheté {amount} <:tin:1004693610844917880> pour {amount * 112.5}€.")
                saves(users)
        elif item == "club":
            amount = 1
            users[str(user.id)]["bank"] -= 50000
            await ctx.send(f"Vous avez acheté {amount} <:club:999093324323500152> pour {amount * 5000}€.")
            role = ctx.guild.get_role(1014508719985410148)
            await user.add_roles(role)
            saves(users)
        elif item is None:
            return await ctx.send("Veuillez indiquer un objet à acheter.")


async def setup(client):
    await client.add_cog(Buy(client))
