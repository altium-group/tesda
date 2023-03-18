from discord.ext import commands
from tesda import Opens, datas, saves


class Sell(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def sell(self, ctx, item=None, amount=1):
        user = ctx.author
        Opens(user)
        users = datas()
        if item == "gold":
            if amount > users[str(user.id)]["gold"]:
                return await ctx.send(f"Veuillez indiquer un montant inférieur.")
            else:
                users[str(user.id)]["gold"] -= amount
                users[str(user.id)]["bank"] += amount * 1500
                await ctx.send(
                    "Vous avez vendu {:,} <:gold:1004727089615872071> Or pour {:,}€.".format(amount, amount * 1500))
                saves(users)
        elif item == "copper":
            if amount > users[str(user.id)]["copper"]:
                return await ctx.send(f"Veuillez indiquer un montant inférieur.")
            else:
                users[str(user.id)]["copper"] -= amount
                users[str(user.id)]["bank"] += amount * 150
                await ctx.send("Vous avez vendu {:,} <:copper:1004692203035172954> Cuivre pour {:,}€.".format(amount,
                                                                                                              amount * 150))
                saves(users)
        elif item == "steel":
            if amount > users[str(user.id)]["steel"]:
                return await ctx.send(f"Veuillez indiquer un montant inférieur.")
            else:
                users[str(user.id)]["steel"] -= amount
                users[str(user.id)]["bank"] += amount * 75
                await ctx.send(
                    "Vous avez vendu {:,} <:steel:1004693606927454208> Métal pour {:,}€.".format(amount, amount * 75))
                saves(users)
        elif item == "tin":
            if amount > users[str(user.id)]["tin"]:
                return await ctx.send(f"Veuillez indiquer un montant inférieur.")
            else:
                users[str(user.id)]["tin"] -= amount
                users[str(user.id)]["bank"] += amount * 30
                await ctx.send(
                    "Vous avez vendu {:,} <:tin:1004693610844917880> Etain pour {:,}€.".format(amount, amount * 30))
                saves(users)
        elif item == "food":
            if amount > users[str(user.id)]["food"]:
                return await ctx.send(f"Veuillez indiquer un montant inférieur.")
            else:
                users[str(user.id)]["food"] -= amount
                users[str(user.id)]["bank"] += amount * 20
                await ctx.send("Vous avez vendu {:,} <:food:1004727082904989766> Nourriture pour {:,}€.".format(amount,
                                                                                                                amount * 20))
                saves(users)
        elif item == "trash":
            if amount > users[str(user.id)]["trash"]:
                return await ctx.send(f"Veuillez indiquer un montant inférieur.")
            else:
                users[str(user.id)]["trash"] -= amount
                users[str(user.id)]["bank"] += amount * 15
                await ctx.send(
                    "Vous avez vendu {:,} <:trash:1004693598555619368> Déchet pour {:,}€.".format(amount, amount * 15))
                saves(users)
        elif item is None:
            return await ctx.send("Veuillez indiquer un objet.")
        else:
            return await ctx.send("Objet non reconnue, Veuillez indiquer un objet")


async def setup(client):
    await client.add_cog(Sell(client))

# Gold : 1500 (1 gold -> 1 gold)
# Copper : 150 (10 copper -> 1 gold)
# Steel : 75 (20 steel -> 1 gold)
# Tin : 30 (50 tin -> 1 gold)
# Food : 20 (75 food -> 1 gold)
# Trash : 15 (100 trash -> 1 gold)
