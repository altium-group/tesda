import discord, random, datetime, json
from discord.ext import commands
from tesda import Opens, datas, saves
from random import choice


class Luck(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def luck(self, ctx, *, lot: int = None):
        user = ctx.author
        Opens(user)
        users = datas()
        time = datetime.datetime.now()
        slots = ["<:casino1:1002256923548192858>", "<:casino2:1002256921140674650>"]
        slot1 = random.choice(slots)
        slot2 = random.choice(slots)
        slot3 = random.choice(slots)

        if lot is None:
            return await ctx.send("Veuillez indiquer un montant.")
        elif slot1 == slot2 == slot3:
            message = "Vous avez gagné"
            lot = lot * 10
            users[str(user.id)]["bank"] += lot
        elif lot > users[(str(user.id))]["bank"]:
            return await ctx.send("Vous n'avez pas assez d'argent.")
        elif lot < 0:
            return await ctx.send("Veuillez indiquer une somme positive.")
        elif lot == 0:
            return await ctx.send("Veuillez indiquer une somme supérieur à 0.")
        else:
            message = "Vous avez perdu"
            lot = lot * 50
            users[str(user.id)]["bank"] -= lot

        saves(users)
        colors = [16711854, 4980991, 65344, 64511, 16768256, 16711680, 16711914]
        color = choice(colors)
        embed = discord.Embed(title="<:machine:1002267483941646336> Casino", color=color)
        embed.add_field(name="Slots:", value=f"{slot1} | {slot2} | {slot3}", inline=True)
        embed.add_field(name="Résultat:", value=f"{message} {lot}€.", inline=False)
        embed.set_footer(text=f"{ctx.guild.name} • {time.day}/{time.month}/{time.year}", icon_url=ctx.guild.icon)
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Luck(client))
