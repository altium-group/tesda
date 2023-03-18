from discord.ext import commands


class Log(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def log(self, ctx):
        msg = await ctx.send("<a:loading:1000544602081734726> Récuperation des logs...")
        await ctx.send("• Ajout de la commande `uptime`")
        await ctx.send("• Ajout de la commande `invites`")
        await ctx.send("• Ajout de la commande `workers`")
        await ctx.send("• Ajout de la commande `sell`")
        await ctx.send("• Ajout de la commande `market`")
        await ctx.send("• Ajout de la commande `loot`")
        await ctx.send("• Ajout de la commande `inventaire`")
        await msg.delete()


async def setup(client):
    await client.add_cog(Log(client))
