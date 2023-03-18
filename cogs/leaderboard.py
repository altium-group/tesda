import discord, datetime
from discord.ext import commands
from tesda import datas
from random import choice


class LeaderB(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["lb"])
    async def leaderboard(self, ctx, top=None):
        if top == "bal":
            users = datas()
            x = 5
            leader_board = {}
            total = []
            for user in users:
                name = int(user)
                total_amount = users[user]["bank"]
                leader_board[total_amount] = name
                total.append(total_amount)
                emote = "<:dollars:1001521526832631849>"
                names = "Monnaie"
                type = "€"
        elif top == "level":
            users = datas()
            x = 5
            leader_board = {}
            total = []
            for user in users:
                name = int(user)
                total_amount = users[user]["lvl"]
                leader_board[total_amount] = name
                total.append(total_amount)
                names = "Niveaux"
                emote = "<:xp:999082525429338233>"
                type = " lvl"
        elif top == "bounty":
            users = datas()
            x = 5
            leader_board = {}
            total = []
            for user in users:
                name = int(user)
                total_amount = users[user]["bounty"]
                leader_board[total_amount] = name
                total.append(total_amount)
                emote = "<:target:1011980645406351371>"
                names = "Primes"
                type = "€"
        elif top == "power":
            users = datas()
            x = 5
            leader_board = {}
            total = []
            for user in users:
                name = int(user)
                total_amount = users[user]["power"]
                leader_board[total_amount] = name
                total.append(total_amount)
                emote = "<:power:1011994788452638751>"
                names = "Power"
                type = " <:power:1011994788452638751>"
        elif top == "warn":
            users = datas()
            x = 5
            leader_board = {}
            total = []
            for user in users:
                name = int(user)
                total_amount = users[user]["warn"]
                leader_board[total_amount] = name
                total.append(total_amount)
                emote = "<a:awarn:1001489503887835317>"
                names = "Warns"
                type = " warn(s)"
        elif top is None:
            return await ctx.send("Veuillez indiquer un type")

        total = sorted(total, reverse=True)
        colors = [16711854, 4980991, 65344, 64511, 16768256, 16711680, 16711914]
        color = choice(colors)
        em = discord.Embed(title=f"{emote} Classement {names} (Top {x}):", color=color)
        index = 1
        for amt in total:
            id_ = leader_board[amt]
            member = self.client.get_user(id_)
            name = member.name
            em.add_field(name=f"{index}. {name}", value="{:,}".format(amt) + type, inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/emojis/1011996114662211634.png")
            time = datetime.datetime.now()
            em.set_footer(text=f"{ctx.guild.name} • {time.day}/{time.month}/{time.year}", icon_url=ctx.guild.icon)

            if index == x:
                break
            else:
                index += 1

        await ctx.send(embed=em)


async def setup(client):
    await client.add_cog(LeaderB(client))
