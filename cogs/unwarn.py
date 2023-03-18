import discord, datetime
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from tesda import Opens, datas, saves


class Unwarn(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unwarn(self, ctx, user: discord.Member = None, *, reason=None):
        Opens(user)
        users = datas()
        if reason is None:
            return await ctx.send("Veuillez indiquer une raison.")
        elif user is None:
            return await ctx.send("Veuillez indiquer un membre.")
        users[str(user.id)]["warn"] -= 1
        warn = users[str(user.id)]["warn"]

        saves(users)

        embed = discord.Embed(title="<a:awarn:1001489503887835317> Warn", color=16711680)
        embed.add_field(name="Utilisateur:", value=user.name, inline=True)
        embed.add_field(name="Modérateur:", value=ctx.message.author.name, inline=True)
        embed.add_field(name="Raison:", value=reason, inline=True)
        embed.add_field(name="Warns:", value=warn, inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001160982502068324.webp")
        time = datetime.datetime.now()
        embed.set_footer(text=f"{ctx.guild.name} • {time.day}/{time.month}/{time.year}", icon_url=ctx.guild.icon)
        await ctx.send(embed=embed)
        print(f"{ctx.author.name} à unwarn {user.name} pour {reason}")

    @unwarn.error
    async def unwarn_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("Vous n'avez pas la permission (`gérer les messages`).")


async def setup(client):
    await client.add_cog(Unwarn(client))
