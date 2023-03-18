from discord.ext import commands


class Join(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.channel.id != 999292002451607562:
            msg = await ctx.send("Veuillez envoyer cette commande dans <#999292002451607562>.")
            await ctx.message.delete()
            await msg.delete()
        else:
            user = ctx.author
            role = user.guild.get_role(999292727357362356)
            await user.add_roles(role)
            await ctx.message.delete()


async def setup(client):
    await client.add_cog(Join(client))
