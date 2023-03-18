from discord.ext import commands
from random import choice
from tesda import isOwner


class Shifoumi(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["pfc", "sfm"])
    async def shifoumi(self, ctx, objet=None):
        list = ["pierre", "feuille", "ciseaux"]
        botObjet = choice(list)
        message = None
        if objet == "pierre":
            if botObjet == "ciseaux":
                message = "Vous avez gagné !"
            elif botObjet == "feuille":
                message = "Vous avez perdu !"
        elif objet == "feuille":
            if botObjet == "pierre":
                message = "Vous avez gagné !"
            elif botObjet == "ciseaux":
                message = "Vous avez perdu !"
        elif objet == "ciseaux":
            if botObjet == "feuille":
                message = "Vous avez gagné !"
            elif botObjet == "pierre":
                message = "Vous avez perdu !"
        elif objet == botObjet:
            message = "Egalité !"
        elif objet is None:
            return await ctx.send("Veuillez indiquer un objet.")
        await ctx.reply(f"J'ai choisis {botObjet},\n{message}", mention_author=False)


async def setup(client):
    await client.add_cog(Shifoumi(client))
