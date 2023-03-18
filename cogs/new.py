import datetime
import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions


class News(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def enew(self, ctx, channelId: int, *, reason=None):
        if reason is None:
            return await ctx.send("Veuillez indiquer une annonce.")
        elif channelId is None:
            return await ctx.send("Veuillez indiquer un salon (`id`).")
        await ctx.message.delete()
        channel = ctx.guild.get_channel(channelId)
        msg = discord.Embed(title="<:Annonce:1001106937489920071> Annonce:", description=reason,
                            color=discord.Color(0xfa43ee))
        msg.set_thumbnail(url="https://cdn.discordapp.com/emojis/1001106937489920071.webp")
        time = datetime.datetime.now()
        msg.set_footer(text=f"{ctx.guild.name} • {time.day}/{time.month}/{time.year}", icon_url=ctx.guild.icon)
        await channel.send(embed=msg)
        message = await channel.send("@everyone")
        await message.add_reaction("<a:averified:1001106934696525834>")

    @enew.error
    async def enew_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("Vous n'avez pas la permission (`bannir des membres`).")


async def setup(client):
    await client.add_cog(News(client))
