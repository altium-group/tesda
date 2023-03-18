import discord, random, datetime, json
from discord.ext import commands
from tesda import Opens, datas, saves
from random import choice


class Loot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 120)
    async def loot(self, ctx):
        user = ctx.author
        Opens(user)
        users = datas()
        gold = random.randint(0, 1)
        copper = random.randint(0, 2)
        steel = random.randint(0, 3)
        tin = random.randint(0, 4)
        food = random.randint(0, 5)
        trash = random.randint(0, 5)

        users[str(user.id)]["gold"] += gold
        users[str(user.id)]["copper"] += copper
        users[str(user.id)]["steel"] += steel
        users[str(user.id)]["tin"] += tin
        users[str(user.id)]["food"] += food
        users[str(user.id)]["trash"] += trash

        saves(users)
        colors = [16711854, 4980991, 65344, 64511, 16768256, 16711680, 16711914]
        color = choice(colors)
        embed = discord.Embed(title=f"Objet ajouté à {user.name}:", color=color)
        list = [
            {"item": "<:gold:1004727089615872071> Or", "amount": gold, "desc": "Or (Métal a haute valeur.)"},
            {"item": "<:copper:1004692203035172954> Cuivre", "amount": copper, "desc": "Cuivre (Métal conducteur.)"},
            {"item": "<:steel:1004693606927454208> Métal", "amount": steel, "desc": "Métaux (Type Fer, Inox, Acier.)"},
            {"item": "<:tin:1004693610844917880> Etain", "amount": tin, "desc": "Etain (Sers à faire des vases.)"},
            {"item": "<:food:1004727082904989766> Nourriture", "amount": food,
             "desc": "Nourriture (Type Pomme, Carotte, Salade.)"},
            {"item": "<:trash:1004693598555619368> Déchets", "amount": trash,
             "desc": "Déchets Organique (Type Pomme, Poulet, Végétaux.)"}
        ]
        for item in list:
            name = item["item"]
            amount = item["amount"]
            desc = item["desc"]
            embed.add_field(name=f"+ {amount} {name},", value=desc, inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1004686314756644864.png")
        time = datetime.datetime.now()
        embed.set_footer(text=f"{ctx.guild.name} • {time.day}/{time.month}/{time.year}", icon_url=ctx.guild.icon)
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Loot(client))
