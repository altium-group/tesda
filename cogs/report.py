import discord, datetime
from discord.ext import commands


class Report(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def report(self, ctx, user: discord.Member = None, *, reason=None):
        if reason is None:
            return await ctx.send("Veuillez indiquer une raison.")
        elif user is None:
            return await ctx.send("Veuillez indiquer un membre.")
        channel = ctx.guild.get_channel(991480707740356750)
        embed = discord.Embed(title="<:report:1001160986713149541> Report", color=16711680)
        embed.add_field(name="Auteur:", value=ctx.author.name, inline=True)
        embed.add_field(name="Accusé:", value=user.mention, inline=True)
        embed.add_field(name="Raison:", value=reason, inline=True)
        # embed.set_thumbnail(url = "https://cdn.discordapp.com/emojis/1001160986713149541.webp")
        time = datetime.datetime.now()
        embed.set_footer(text=f"{ctx.guild.name} • {time.day}/{time.month}/{time.year}", icon_url=ctx.guild.icon)
        msg = await channel.send(embed=embed)
        await msg.add_reaction("<:yes:1002224559333843024>")
        await msg.add_reaction("<:no:1002224555798044672>")
        await user.send(f"Vous avez été report ({ctx.guild.name}) par *{ctx.author.name}*.\nRaison: {reason}")


async def setup(client):
    await client.add_cog(Report(client))
