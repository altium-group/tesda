from discord.ext import commands
from discord.ext.commands import MissingPermissions


class New(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def new(self, ctx, channelId: int, *, reason=None):
        if reason is None:
            return await ctx.send("Veuillez indiquer une annonce.")
        elif channelId is None:
            return await ctx.send("Veuillez indiquer un salon `id`.")
        channel = ctx.guild.get_channel(channelId)
        msg = await channel.send(
            f"<:Annonce:1001106937489920071> **Annonce** :\n{reason}\n Veuillez réagir avec "
            f"<a:averified:1001106934696525834>\n@everyone"
        )
        await msg.add_reaction("<a:averified:1001106934696525834>")
        print(f"{ctx.author.name} à utilisé new")

    @new.error
    async def new_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("Vous n'avez pas la permission (`bannir des membres`).")


async def setup(client):
    await client.add_cog(New(client))
