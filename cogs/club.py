from discord.ext import commands


class Club(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def club(self, ctx):
        avantages = [
            {"name": "Workers", "desc": "accès à la commande `workers`."},
            {"name": "Bonus", "desc": "accès à la commande `bonus`."}
        ]

        await ctx.send("Voici vos avantages en tant que membre Club:")
        for i in avantages:
            name = i["name"]
            desc = i["desc"]
            await ctx.send(f"-> {name}:\n    {desc}")


async def setup(client):
    await client.add_cog(Club(client))
