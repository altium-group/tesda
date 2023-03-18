from random import choice

import datetime
import discord
from discord.ext import commands

from tesda import datas


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def info(self, ctx, commande=None, user: discord.Member = None):
        colors = [16711854, 4980991, 65344, 64511, 16768256, 16711680, 16711914]
        color = choice(colors)
        if commande == "user":
            if user is None:
                user = ctx.author
            creation = user.created_at
            times = user.joined_at
            since = datetime.datetime.now(datetime.timezone.utc) - times
            embed = discord.Embed(title=f"Informations sur {user.display_name}:", color=color)
            embed.add_field(name="Numéros d'Id:", value=user.id, inline=True)
            embed.add_field(name="Pseudo:", value=user, inline=True)
            embed.add_field(name="Nick:", value=user.nick, inline=True)
            embed.add_field(name="Date de création:", value=f"{creation.day}/{creation.month}/{creation.year}",
                            inline=True)
            embed.add_field(name="A rejoins le:", value=f"{times.day}/{times.month}/{times.year}", inline=True)
            embed.add_field(name="A rejoins depuis:", value=f"{since.days} jour(s)", inline=True)
            role = user.roles
            roles = " "
            for i in role:
                roles = roles + " " + i.mention + ","
            embed.add_field(name="Rôles:", value=roles, inline=False)
            users = datas()
            msgAmt = users[str(user.id)]["msg"]
            lvl = users[str(user.id)]["lvl"]
            embed.add_field(name="Message Envoyé:", value="{:,}".format(msgAmt))
            bankAmt = users[str(user.id)]["bank"]
            embed.add_field(name="Argent:", value="{:,}€".format(bankAmt))
            embed.add_field(name="Niveau:", value="{:,}".format(lvl))
            embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/456/456212.png")
            time = datetime.datetime.now()
            embed.set_footer(text=f"{ctx.guild.name} • {time.day}/{time.month}/{time.year}",
                             icon_url=ctx.guild.icon)
            await ctx.send(embed=embed)
            print(f"{ctx.author.name} à demander des infos sur {user.name}")

        elif commande == "server":
            server = ctx.guild
            serverName = server.name
            txtChannels = len(server.text_channels)
            voiceChannels = len(server.voice_channels)
            memberCount = server.member_count
            time = datetime.datetime.now()
            times = ctx.guild.created_at
            since = datetime.datetime.now(datetime.timezone.utc) - times
            embed = discord.Embed(title=f"Information de *{serverName}*:", description=server.description, color=color)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
            embed.add_field(name="Numéros d'Id:", value=server.id, inline=True)
            embed.add_field(name="Serveur crée le:", value=f"{times.day}/{times.month}/{times.year}",
                            inline=True)
            embed.add_field(name="Créateur :", value=ctx.guild.owner.name, inline=True)
            embed.add_field(name="Membres:", value=f"*{memberCount}*", inline=True)
            embed.add_field(name="Salon(s):", value=f"*{txtChannels}*", inline=True)
            embed.add_field(name="Salon Vocaux:", value=f"*{voiceChannels}*", inline=True)
            embed.add_field(name="<:Badge2:1010623932409327656> Booster(s):", value=server.premium_subscription_count,
                            inline=True)
            embed.add_field(name="<:Badge1:1010623935655723069> Boost Tier:", value=server.premium_tier)
            embed.add_field(name="Créer depuis:", value=f"{since.days} jour(s)")
            # role = ctx.guild.roles
            # roles = " "
            # for i in role:
            #     roles = roles + " " + i.mention + ","
            # embed.add_field(name = "Rôles disponible :", value = roles, inline = False)
            embed.set_footer(text=f"{ctx.guild.name} • {time.day}/{time.month}/{time.year}",
                             icon_url=ctx.guild.icon)
            await ctx.send(embed=embed)
        elif commande is None:
            embed = discord.Embed(title="Help - info:")
            embed.add_field(name="usage:", value="`*info <user|server> [membre]`", inline=False)
            embed.add_field(name="permission:", value="`gérer les messages`", inline=False)
            embed.add_field(name="description:", value="Afficher des informations", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001156198474715206.webp")
            time = datetime.datetime.now()
            embed.set_footer(text=f"{ctx.guild.name} • {time.day}/{time.month}/{time.year}",
                             icon_url=ctx.guild.icon_url)
            print(f"{ctx.author.name} à demandé de l'aide")
            await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Info(client))
