from random import choice

import datetime
import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["h"])
    async def help(self, ctx, commande=None):
        colors = [16711854, 4980991, 65344, 64511, 16768256, 16711680, 16711914]
        color = choice(colors)
        cmd = [
            {"name": "8ball", "use": "8ball [question]", "perm": "envoyer des messages", "desc": "Donne une réponse à toute vos question", "aliase": "ball", "spe": "/"},
            {"name": "new", "use": "new [salon-id] [annonce]", "perm": "bannir des membres", "desc": "Envoie un message d'annonce", "aliase": "/", "spe": "/"},
            {"name": "balance", "use": "balance <user>", "perm": "envoyer des messages", "desc": "Affiche votre compte", "aliase": "bal", "spe": "/"},
            {"name": "level", "use": "level <user>", "perm": "envoyer des messages", "desc": "Affiche votre progression", "aliase": "lvl", "spe": "/"},
            {"name": "ban", "use": "ban <user> [reason]", "perm": "bannir des membres", "desc": "Bannir un membre", "aliase": "/", "spe": "/"},
            {"name": "casino", "use": "casino [montant]", "perm": "envoyer des messages", "desc": "Tente de doubler ta mise", "aliase": "/", "spe": "/"},
            {"name": "clear", "use": "clear [nombre]", "perm": "gérer les messages", "desc": "Efface des messages", "aliase": "/", "spe": "/"},
            {"name": "emote", "use": "emote [emote]", "perm": "gérer les messages", "desc": "Affiche les infos d'emoji", "aliase": "/", "spe": "Avec ou sans `:`"},
            {"name": "role", "use": "role [role] <edit|None|add|remove> [nom]/<user>", "perm": "expulser des membres", "desc": "Affiche les infos du rôle, le modifie, l'ajoute ou le retire", "aliase": "/", "spe": "Mention/nom"},
            {"name": "idea", "use": "idea [idée]", "perm": "envoyer des messages", "desc": "Envoie votre suggestion", "aliase": "/", "spe": "/"},
            {"name": "kick", "use": "kick <user> [reason]", "perm": "expulser des membres", "desc": "Expulse un membre", "aliase": "/", "spe": "/"},
            {"name": "lban", "use": "lban", "perm": "bannir des membres", "desc": "Affiche la liste des membres banni(e)", "aliase": "/", "spe": "/"},
            {"name": "lottery", "use": "lottery", "perm": "expulser des membres", "desc": "Lance une lotterie", "aliase": "lot", "spe": "/"},
            {"name": "enew", "use": "enew [salon-id] [annonce]", "perm": "bannir des membres", "desc": "Envoie un message d'annonce", "aliase": "/", "spe": "Message: Embed"},
            {"name": "enew", "use": "enew [salon-id] [annonce]", "perm": "bannir des membres", "desc": "Envoie un message d'annonce", "aliase": "/", "spe": "Message: Embed"},
            {"name": "report", "use": "report <user> [reason]", "perm": "envoyer des messages", "desc": "Envoie une plainte", "aliase": "/", "spe": "/"},
            {"name": "luck", "use": "luck [montant]", "perm": "envoyer des messages", "desc": "Tente de doubler ta mise", "aliase": "/", "spe": "Gains: Mise * 10, Perte: Mise * 50"},
            {"name": "unban", "use": "unban <user> [reason]", "perm": "bannir des membres", "desc": "Dé-bannir un membre", "aliase": "/", "spe": "/"},
            {"name": "warn", "use": "warn <user> [reason]", "perm": "gérer les messages", "desc": "Warn un membre", "aliase": "/", "spe": "/"},
            {"name": "unwarn", "use": "unwarn <user> [reason]", "perm": "gérer les messages", "desc": "Unwarn un membre", "aliase": "/", "spe": "/"},
            {"name": "bonus", "use": "bonus", "perm": "être vip", "desc": "Bonus financier journalier", "aliase": "/", "spe": "/"},
            {"name": "work", "use": "work", "perm": "envoyer des messages", "desc": "Travailler pour gagner de l'argent", "aliase": "w", "spe": "/"},
            {"name": "leaderboard", "use": "leaderboard <balance|level|warn>", "perm": "envoyer des messages", "desc": "Affiche le top 5", "aliase": "lb", "spe": "/"},
            {"name": "market", "use": "market", "perm": "envoyer des messages", "desc": "Affiche le market", "aliase": "mrk", "spe": "/"},
            {"name": "loot", "use": "loot", "perm": "envoyer des messages", "desc": "Loot des items", "aliase": "/", "spe": "Cooldown: `2min`"},
            {"name": "buy", "use": "buy <objet> [montant]", "perm": "envoyer des messages", "desc": "Achète des objets", "aliase": "/", "spe": "/"},
            {"name": "sell", "use": "sell <objet> [montant]", "perm": "envoyer des messages", "desc": "Vend des objets", "aliase": "/", "spe": "/"},
            {"name": "inventory", "use": "inventory", "perm": "envoyer des messages", "desc": "Affiche l'inventaire", "aliase": "inv", "spe": "/"},
            {"name": "workers", "use": "workers <loot|bank> <start>", "perm": "être vip", "desc": "Faire travailler ses ouvriers", "aliase": "/", "spe": "Durée: `30min`, Cooldown: `1h`"},
            {"name": "invites", "use": "invites <user>", "perm": "envoyer des messages", "desc": "Affiche le nombre d'utilisation des invitations des membres", "aliase": "/", "spe": "/"},
            {"name": "uptime", "use": "uptime", "perm": "envoyer des messages", "desc": "Affiche le temps depuis lequel le bot est allumé", "aliase": "upt", "spe": "/"},
            {"name": "shifoumi", "use": "shifoumi <pierre|feuille|ciseaux>", "perm": "envoyer des messages", "desc": "Joue au Pierre Feuille Ciseaux", "aliase": "pfc, sfm", "spe": "/"},
            {"name": "pay", "use": "pay <user> [montant]", "perm": "envoyer des messages", "desc": "Donner de l'argent à un membre", "aliase": "/", "spe": "/"},
            {"name": "tag", "use": "tag [tag]", "perm": "envoyer des messages", "desc": "Afficher les tags", "aliase": "/", "spe": "100€/tag"},
            {"name": "ticket", "use": "ticket <create|close>", "perm": "envoyer des messages", "desc": "Créer un ticket d'aide", "aliase": "/", "spe": "/"},
            {"name": "release", "use": "release", "perm": "envoyer des messages", "desc": "Afficher les dates de releases", "aliase": "/", "spe": "/"}

        ]
        if commande is not None:
            for i in cmd:
                name = i["name"]
                use = i["use"]
                perm = i["perm"]
                desc = i["desc"]
                alias = i["aliase"]
                spe = i["spe"]
                if commande == name:
                    embed = discord.Embed(title=f"Help - {name}:", color=color)
                    embed.add_field(name="Usage:", value=f"`{use}`", inline=False)
                    embed.add_field(name="Permissions:", value=f"`{perm}`", inline=False)
                    embed.add_field(name="Description:", value=f"{desc}", inline=False)
                    embed.add_field(name="Alliasse:", value=f"`{alias}`", inline=True)
                    embed.add_field(name="Specification:", value=f"{spe}", inline=True)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001152938800058409.webp")
                    time = datetime.datetime.now()
                    embed.set_footer(text=f"{ctx.guild.name} • {time.day}/{time.month}/{time.year}",
                                     icon_url=ctx.guild.icon)
                    await ctx.send(embed=embed)
        elif commande is None:
            embed = discord.Embed(title="Help - Liste des commandes:",
                                  description="Utilise `help <command>` pour plus d'info !\n<> = Argument Défini, [] = Argument définissable.",
                                  color=color)
            embed.add_field(name="<:market:1006242574194974750> Market", value="`market`, `loot`, `sell`, `buy`, `inventory`")
            embed.add_field(name="<:banks:1009395411900964985> Economie", value="`balance`, `work`, `bounty`, `top`, `eco`, `bonus`, `workers`, `pay`", inline=False)
            embed.add_field(name="<:dice:1001152935851470999> Fun", value="`ball`, `casino`, `luck`, `level`, `shifoumi`, `tag`, `release`")
            embed.add_field(name="<:tool:999309859801534534> Utilitaire", value="`report`, `log`, `alog`, `ping`, `idea`, `club`, `invites`, `uptime`, `support`, `invite`, `leaderboard`", inline=False)
            embed.add_field(name="<:mod:999309857339482112> Modération", value="`clear`, `kick`, `ban`, `lban`, `info` `warn`, `unwarn`", inline=False)
            embed.add_field(name="<:owner:999386335452340294> Créateur", value="`lottery`, `new`, `stat`, `enew`", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001152938800058409.webp")
            time = datetime.datetime.now()
            embed.set_footer(text=f"{ctx.guild.name} • {time.day}/{time.month}/{time.year}", icon_url=ctx.guild.icon)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Commande non reconnue, tapez `help` pour la liste des commandes.")


async def setup(client):
    await client.add_cog(Help(client))
