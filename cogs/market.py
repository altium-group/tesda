import discord
import datetime
from discord.ext import commands
from random import choice


class Market(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["mrk"])
    async def market(self, ctx):
        mainshop = [
            {"item": "<:gold:1004727089615872071> Or", "purchase": 2250, "resell": 1500,
             "desc": "Or (Métal a haute valeur)."},
            {"item": "<:copper:1004692203035172954> Cuivre", "purchase": 225, "resell": 150,
             "desc": "Cuivre (Métal conducteur)."},
            {"item": "<:steel:1004693606927454208> Métal", "purchase": 112.5, "resell": 75,
             "desc": "Métaux (Type Fer, Inox, Acier)."},
            {"item": "<:tin:1004693610844917880> Etain", "purchase": 45, "resell": 30,
             "desc": "Etain (Sers à faire des vases)."},
            {"item": "<:food:1004727082904989766> Nourriture", "purchase": ".", "resell": 20,
             "desc": "Nourriture (Type Pomme, Carotte, Salade)."},
            {"item": "<:trash:1004693598555619368> Déchets", "purchase": ".", "resell": 5,
             "desc": "Déchets Organique (Type Pomme, Poulet, Végétaux)."},
            {"item": "<:club:999093324323500152> Colibrye Club", "purchase": 50000, "resell": 0,
             "desc": "Colibrye Club (Accès à plus de commandes)."}
        ]
        colors = [16711854, 4980991, 65344, 64511, 16768256, 16711680, 16711914]
        color = choice(colors)
        embed = discord.Embed(title="Marché :", description="`*buy` pour l'achat, `*sell` pour la revente.",
                              color=color)
        time = datetime.datetime.now()
        embed.set_footer(text=f"{ctx.guild.name} • {time.day}/{time.month}/{time.year}", icon_url=ctx.guild.icon)
        embed.add_field(name="Objet: Achat - Revente", value="Description (Specification).")
        for item in mainshop:
            name = item["item"]
            purchase = item["purchase"]
            resell = item["resell"]
            desc = item["desc"]
            embed.add_field(name=f"{name}: {purchase}€ - {resell}€", value=desc, inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1004686314756644864.png")
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Market(client))
