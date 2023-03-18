import datetime
import discord
from discord.ext import commands


class Idea(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def idea(self, ctx, *, reason=None):
        if reason is None:
            return await ctx.send("Veuillez indiquer une raison.")
        channel = ctx.guild.get_channel(991478556355997808)
        embed = discord.Embed(title="<:vote:1006532566653874338> Suggestion", color=16711680)
        embed.add_field(name="Auteur:", value=ctx.author.name, inline=True)
        embed.add_field(name="Proposition:", value=reason, inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001160986713149541.webp")
        time = datetime.datetime.now()
        embed.set_footer(text=f"{ctx.guild.name} • {time.day}/{time.month}/{time.year}", icon_url=ctx.guild.icon)
        msg = await channel.send(embed=embed)
        await msg.add_reaction("<:yes:1002224559333843024>")
        await msg.add_reaction("<:no:1002224555798044672>")
        print(f"{ctx.author.name} à donnée une idée : {reason}")


async def setup(client):
    await client.add_cog(Idea(client))
