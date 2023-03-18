from random import choice

import datetime
import discord
from discord.ext import commands

from tesda import Opens, datas


class Inventory(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["inv"])
    async def inventory(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        Opens(user)
        users = datas()
        colors = [16711854, 4980991, 65344, 64511, 16768256, 16711680, 16711914]
        color = choice(colors)
        embed = discord.Embed(title=f"Inventaire de {user.name}:", color=color)
        list = [
            {"item": "<:gold:1004727089615872071> Or", "amount": users[str(user.id)]["gold"],
             "desc": "Or (Métal a haute valeur.)"},
            {"item": "<:copper:1004692203035172954> Cuivre", "amount": users[str(user.id)]["copper"],
             "desc": "Cuivre (Métal conducteur.)"},
            {"item": "<:steel:1004693606927454208> Métal", "amount": users[str(user.id)]["steel"],
             "desc": "Métaux (Type Fer, Inox, Acier.)"},
            {"item": "<:tin:1004693610844917880> Etain", "amount": users[str(user.id)]["tin"],
             "desc": "Etain (Sers à faire des vases.)"},
            {"item": "<:food:1004727082904989766> Nourriture", "amount": users[str(user.id)]["food"],
             "desc": "Nourriture (Type Pomme, Carotte, Salade.)"},
            {"item": "<:trash:1004693598555619368> Déchets", "amount": users[str(user.id)]["trash"],
             "desc": "Déchets Organique (Type Pomme, Poulet, Végétaux.)"}
        ]
        for item in list:
            name = item["item"]
            amount = item["amount"]
            desc = item["desc"]
            embed.add_field(name=f"{name}: x{amount}", value=desc, inline=False)
        time = datetime.datetime.now()
        embed.set_footer(text=f"{ctx.guild.name} • {time.day}/{time.month}/{time.year}", icon_url=ctx.guild.icon)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1004686314756644864.png")
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Inventory(client))
